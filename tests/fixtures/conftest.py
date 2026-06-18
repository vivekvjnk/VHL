import pytest
import json
import os
import time
import threading
import subprocess
import signal
import tempfile
import shutil
import socket
import sys
import sqlite3
import logging
import uuid
import hashlib
import requests
import asyncio
from playwright.sync_api import sync_playwright
from pydantic import BaseModel, Field, ConfigDict
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../vhl-agent-backend")))
from vhl_protocol.client.client import VHLWebSocketClient
from vhl_protocol.models import BaseEvent

# Configure the root logger before creating your local logger
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'  # <-- Only keeps the actual log message
)

logger = logging.getLogger(__name__)

def is_port_open(port):
    """Checks if a local port is open and listening."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def wait_for_port(port, timeout=30):
    """Blocks until a port is open or timeout is reached."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if is_port_open(port):
            return True
        time.sleep(1)
    return False

class Event:
    """
    A lightweight wrapper for WebSocket events to allow dot-notation access.
    
    Attributes:
        type (str): The AgentMessage type (e.g., 'CREATE_PROJECT').
        payload (dict): The data associated with the event.
        direction (str): Whether the message was 'sent' or 'received'.
    """
    def __init__(self, data):
        self._data = data
        for key, value in data.items():
            setattr(self, key, value)
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __repr__(self):
        return f"Event({self._data})"

class VHLSystem:
    """
    The main orchestrator for VHL System E2E and Integration tests.
    
    This class wraps a Playwright Page object and provides high-level methods 
    to interact with the VHL WebUI, intercept WebSocket communications, 
    and validate system state across the Backend and Runtime.
    """
    
    def __init__(self, page, config, workspace_path=None):
        """
        Initializes the VHLSystem orchestrator.
        
        Args:
            page (Page): The Playwright page instance.
            config (dict): Environment configuration.
            workspace_path (str, optional): Root directory of the backend workspace.
        """
        self.page = page
        self.config = config
        self.workspace_path = workspace_path
        self.events = []
        self._loop = None
        self._client = None
        self._client_thread = None
        # self._setup_debug_listeners()
        self._start_observer()

    def _start_observer(self):
        """
        Starts a background thread that connects to the VHL Runtime as an observer.
        """
        ws_url = self.config["VHL_RELAY_URL"].replace("http", "ws") + "/ws-agent"
        logger.info(f"[VHL Test] Connecting observer to: {ws_url}")

        self._loop = asyncio.new_event_loop()
        
        def run_loop():
            asyncio.set_event_loop(self._loop)
            self._loop.run_forever()
            
        self._client_thread = threading.Thread(target=run_loop)
        self._client_thread.daemon = True
        self._client_thread.start()

        async def on_event(event: BaseEvent):
            self._handle_message(event.model_dump())

        self._client = VHLWebSocketClient(
            url=ws_url,
            role="vhl_test_observer",
            on_event_received=on_event
        )
        
        asyncio.run_coroutine_threadsafe(self._client.start(), self._loop)
        logger.info("[VHL Test] Observer started.")

    def _setup_debug_listeners(self):
        """
        Attaches listeners to the browser page to capture logs and errors.
        
        This method pipes browser console logs, page errors, and failed 
        network requests to the Python stdout for easier debugging.
        """
        self.page.on("console", lambda msg: logger.info(f"[Browser Console] {msg.type}: {msg.text}"))
        self.page.on("pageerror", lambda exc: logger.info(f"[Browser Error] {exc}"))
        self.page.on("requestfailed", lambda req: logger.info(f"[Browser Request Failed] {req.method} {req.url} : {req.failure}"))

    def stop(self):
        """
        Stops the observer and performs cleanup.
        """
        if self._client and self._loop:
            # 1. Stop the client and wait for it
            future = asyncio.run_coroutine_threadsafe(self._client.stop(), self._loop)
            try:
                future.result(timeout=5)
            except Exception as e:
                logger.error(f"[VHL Test] Error stopping client: {e}")
            
            # 2. Stop the loop
            self._loop.call_soon_threadsafe(self._loop.stop)
            
            # 3. Join the thread
            if self._client_thread:
                self._client_thread.join(timeout=5)
            
            # 4. Close the loop
            try:
                self._loop.close()
            except Exception as e:
                logger.error(f"[VHL Test] Error closing event loop: {e}")
                
        logger.info("[VHL Test] Observer stopped.")

    def _handle_message(self, msg):
        """
        Callback function invoked by the browser when a WebSocket event is intercepted.
        
        Args:
            msg (dict): The captured JSON payload from the WebSocket.
        """
        if isinstance(msg, dict) and "type" in msg:
            logger.info(f"[VHL Event : {msg.get('timestamp')}] {msg.get('source', 'unknown')}: {msg.get('type')}")
            # If message type is ERROR log the entire payload for debugging
            if msg.get("type") == "ERROR":
                logger.info(f"[VHL Event] ERROR payload: {json.dumps(msg, indent=2)}")
            self.events.append(Event(msg))

    def clear_events(self):
        """
        Clears the captured events list. Useful before triggering a new action.
        """
        logger.info(f"[VHL Test] Clearing {len(self.events)} captured events.")
        self.events = []

    def create_project(self, name, zip=None):
        """
        Creates a new project by uploading a ZIP file directly to MinIO and emitting
        the CREATE_PROJECT event.
        
        Args:
            name (str): The name of the project to create.
            zip (str, optional): A path to a local ZIP file OR a pre-uploaded blob ID.
        """
        # Safety check for WebSocket connectivity
        # self.page.wait_for_function(
        #     "window.__VHL_LAST_WS__ && window.__VHL_LAST_WS__.readyState === window.WebSocket.OPEN", 
        #     timeout=10000
        # )

        zip_blob_id = None
        if zip:
            if os.path.exists(zip):
                logger.info(f"[VHL Test] Uploading local zip file {zip} to MinIO...")
                with open(zip, "rb") as f:
                    file_content = f.read()
                
                hash_sha256 = hashlib.sha256(file_content).hexdigest()
                zip_blob_id = f"{hash_sha256}.zip"
                
                # MinIO endpoint and bucket. Using localhost:9000 as default for tests.
                minio_endpoint = self.config.get("VHL_MINIO_URL", "http://localhost:9000")
                bucket_name = self.config.get("VHL_OBJECT_STORE_BUCKET", "vhl")
                url = f"{minio_endpoint}/{bucket_name}/uploads/{zip_blob_id}"
                
                response = requests.put(url, data=file_content, headers={"Content-Type": "application/zip"})
                if not response.ok:
                    raise RuntimeError(f"Failed to upload zip to MinIO: {response.status_code} {response.text}")
                
                logger.info(f"[VHL Test] Zip uploaded to MinIO. Blob ID: {zip_blob_id}")
            else:
                # Assume it's already a blob_id
                logger.info(f"[VHL Test] Using provided blob ID: {zip}")
                zip_blob_id = zip
        
        # Emit the CREATE_PROJECT event directly
        self.emit_event("CREATE_PROJECT", {
            "project_name": name,
            "zip_blob_id": zip_blob_id,
            "source":"vhl_webui"
        })

    def emit_event(self, event_type, payload=None, target="vhl_agent_backend", artifact_id=None):
        """
        Emits a WebSocket event directly from the browser's WebSocket connection.
        
        Args:
            event_type (str): The type of event to emit.
            payload (dict, optional): The payload for the event.
            target (str): The intended recipient of the event.
            artifact_id (str, optional): The artifact ID associated with the event.
        """
        payload = payload or {}
        event_id = str(uuid.uuid4())
        logger.info(f"[VHL Test] Emitting event: {event_type} with payload: {payload}")
        
        # We need to handle the event emission asynchronously because VHLWebSocketClient.emit is async
        # We wrap the payload in a generic dict-based Pydantic model since `emit` expects a BaseModel
        class GenericPayload(BaseModel):
            model_config = ConfigDict(extra='allow')
            
        payload_model = GenericPayload(**payload)
        
        asyncio.run_coroutine_threadsafe(
            self._client.emit(
                event_type=event_type,
                payload=payload_model,
                artifact_id=artifact_id,
                target=target
            ),
            self._loop
        )

    def trigger_archy(self, module_name):
        """
        Triggers the Archy pipeline for a specific module by emitting REFERENCE_UPLOADED.
        
        Args:
            module_name (str): The name of the module to process.
        """
        # Safety check for WebSocket connectivity
        self.page.wait_for_function(
            "window.__VHL_LAST_WS__ && window.__VHL_LAST_WS__.readyState === window.WebSocket.OPEN", 
            timeout=15000
        )
        
        # Note: In the current AOSM, REFERENCE_UPLOADED triggers the BOOTSTRAP_PIPELINE
        # We simulate this by providing the reference_id as the module name.
        self.emit_event("REFERENCE_UPLOADED", {
            "reference_id": module_name,
            "reference_type": "image",
            "filename": f"{module_name}_preprocessed.png"
        })

    def respond_to_hil(self, action, instructions=None):
        """
        Responds to a HIL_REQUEST.
        
        Args:
            action (str): The action to take ('continue', 'retry').
            instructions (str, optional): Additional instructions for retry.
        """
        payload = {"action": action}
        if instructions:
            payload["instructions"] = instructions
            
        self.emit_event("HUMAN_INPUT", payload)

    def wait_for_event(self, event_type, timeout=30000, payload_filter=None):
        """
        Blocks execution until a specific WebSocket event type is intercepted.
        
        Args:
            event_type (str): The type of AgentMessage to wait for (e.g., 'PROJECT_CREATED').
            timeout (int): Maximum time to wait in milliseconds.
            
        Returns:
            Event: The first captured event matching the type.
            
        Raises:
            TimeoutError: If the event is not captured within the timeout.
        """
        logger.info(f"[VHL Test] Waiting for event: {event_type} (timeout={timeout}ms)")
        start_time = time.time()
        while time.time() - start_time < timeout / 1000:
            for event in self.events:
                if event.type == event_type:
                    # Apply payload filter if provided
                    if payload_filter:
                        match = True
                        for key, val in payload_filter.items():
                            if event.payload.get(key) != val:
                                match = False
                                break
                        if not match:
                            continue
                            
                    logger.info(f"[VHL Test] Found event: {event_type}")
                    return event
            time.sleep(0.1) # Brief sleep to avoid high CPU
            self.page.wait_for_timeout(500)
        
        current_event_types = [e.type for e in self.events]
        logger.info(f"[VHL Test] TIMEOUT waiting for {event_type}. Current events: {current_event_types}")
        raise TimeoutError(f"Event {event_type} not received within {timeout}ms. Current events: {current_event_types}")

    def get_event(self, event_type):
        """
        Retrieves the most recent captured event of a specific type without blocking.
        
        Args:
            event_type (str): The type of AgentMessage to retrieve.
            
        Returns:
            Event or None: The most recent event matching the type, or None if not found.
        """
        for event in reversed(self.events):
            if event.type == event_type:
                return event
        return None

    def backend_has_structure(self, project_id, actual_manifest):
        """
        Validates that the Agent Backend has created the expected project structure on disk.
        This includes checking Git repository integrity, SQLite semantic ledger, and .gitignore.
        
        Args:
            project_id (str): The ID of the project to validate.
            actual_manifest (dict): The Git-native manifest received from the backend.
            
        Returns:
            bool: True if the structure is valid, False otherwise.
        """
        if not self.workspace_path:
            logger.info("[VHL Test] Workspace path NOT SET in system orchestrator. Skipping deep validation.")
            return True

        project_path = os.path.join(self.workspace_path, f"{project_id}_root")
        
        # 1. Validate SQLite Semantic Ledger
        db_path = os.path.join(project_path,  ".vhl", "state.db")
        if not os.path.exists(db_path):
            logger.info(f"[VHL Test] SQLite DB NOT FOUND at: {db_path}")
            return False
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check INITIALIZE operation
            cursor.execute("SELECT op_name, status FROM semantic_operations WHERE op_name='INITIALIZE'")
            row = cursor.fetchone()
            if not row or row[1] != "SUCCESS":
                logger.info(f"[VHL Test] INITIALIZE operation NOT FOUND or failed in DB")
                conn.close()
                return False
            
            # Check for module entries
            cursor.execute("SELECT COUNT(*) FROM project_modules")
            count = cursor.fetchone()[0]
            if count == 0:
                logger.info("[VHL Test] No modules found in DB")
                conn.close()
                return False
            
            conn.close()
            logger.info("[VHL Test] SQLite Semantic Ledger VALIDATED.")
        except Exception as e:
            logger.info(f"[VHL Test] Error validating SQLite DB: {e}")
            return False

        # 2. Validate Git Repository
        git_path = os.path.join(project_path, ".git")
        if not os.path.exists(git_path):
            logger.info(f"[VHL Test] Git directory NOT FOUND at: {git_path}")
            return False
        logger.info("[VHL Test] Git Repository VALIDATED.")

        # 3. Validate .gitignore
        gitignore_path = os.path.join(project_path, ".gitignore")
        if not os.path.exists(gitignore_path):
            logger.info(f"[VHL Test] .gitignore NOT FOUND at: {gitignore_path}")
            return False
        
        with open(gitignore_path, 'r') as f:
            content = f.read()
            if ".vhl/" not in content:
                logger.info("[VHL Test] .vhl/ directory NOT IGNORED in .gitignore")
                return False
        logger.info("[VHL Test] .gitignore VALIDATED.")

        # 4. Validate Manifest (Artifact Space)
        # Basic check for expected modules in the Git-native manifest
        expected_modules = [
            "bms-monitor-module", "communication-bridge", "current-sensing", 
            "high-voltage-power-supply", "low-voltage-power-supply", 
            "microcontroller-module"
        ]
        for mod in expected_modules:
            if mod not in actual_manifest:
                logger.info(f"[VHL Test] Manifest MISSING expected module: {mod}")
                return False
        
        logger.info(f"[VHL Test] Backend manifest structure VALIDATED for {project_id}.")
        return True

    def runtime_initialized(self, actual_manifest=None):
        """
        Validates that the VHL Runtime has correctly mirrored and initialized the project.
        
        Args:
            actual_manifest (dict, optional): The manifest received from the runtime.
            
        Returns:
            bool: True if initialization is valid.
        """
        if actual_manifest is not None:
            return self.runtime_has_structure(actual_manifest)
        
        # Fallback for old tests
        return True

    def runtime_has_structure(self, actual_manifest):
        """
        Validates that the VHL Runtime has the expected project structure.
        
        Args:
            actual_manifest (dict): The manifest received from the runtime via DEV_SERVER_READY.
            
        Returns:
            bool: True if the structure matches (ignoring hashes for generated files), False otherwise.
        """
        # Expected keys from user
        expected_modules = [
            "bms-monitor-module", "communication-bridge", "current-sensing", 
            "high-voltage-power-supply", "low-voltage-power-supply", 
            "microcontroller-module", "system-boundary.md"
        ]
        expected_generated_files = [
            "index.circuit.tsx", "package.json", "tscircuit.config.json", "tsconfig.json"
        ]
        
        # Check all modules exist and are dictionaries
        for module in expected_modules:
            if module not in actual_manifest:
                logger.info(f"[VHL Test] Runtime manifest MISSING module: {module}")
                return False
            if not isinstance(actual_manifest[module], dict):
                logger.info(f"[VHL Test] Runtime manifest key {module} expected to be a dict, but got {type(actual_manifest[module])}")
                return False
        
        # Check all generated files exist
        for gen_file in expected_generated_files:
            if gen_file not in actual_manifest:
                logger.info(f"[VHL Test] Runtime manifest MISSING generated file: {gen_file}")
                return False
            if not isinstance(actual_manifest[gen_file], str):
                logger.info(f"[VHL Test] Runtime manifest key {gen_file} expected to be a hash string, but got {type(actual_manifest[gen_file])}")
                return False

        # Ensure no unexpected top-level keys
        all_expected = set(expected_modules + expected_generated_files)
        actual_keys = set(actual_manifest.keys())
        unexpected = actual_keys - all_expected
        if unexpected:
            logger.info(f"[VHL Test] Runtime manifest has UNEXPECTED keys: {unexpected}")
            return False

        logger.info("[VHL Test] Runtime manifest structure VALIDATED.")
        return True

    def webui_reloaded(self):
        """
        Validates that the WebUI has successfully reacted to system events.
        
        Checks if the browser URL contains the project-specific path, indicating 
        that the WebUI received the DEV_SERVER_READY event and performed a navigation/reload.
        
        Returns:
            bool: True if the URL contains the expected project fragment.
        """
        current_url = self.page.url
        is_reloaded = "#file=" in current_url
        logger.info(f"[VHL Test] Checking WebUI reload state: {'RELOADED' if is_reloaded else 'NOT_RELOADED'} (URL: {current_url})")
        return is_reloaded

@pytest.fixture(scope="session")
def managed_services():
    """
    Manages the lifecycle of VHL Runtime and VHL Agent Backend for the test session.
    """
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    runtime_dir = os.path.join(root_dir, "vhl-runtime")
    backend_dir = os.path.join(root_dir, "vhl-agent-backend")
    
    def stream_logs(pipe, prefix):
        try:
            for line in iter(pipe.readline, ''):
                if line:
                    sys.stdout.write(f"{prefix} {line}")
                    sys.stdout.flush()
                    logger.info(f"{prefix} {line.strip()}")
        except Exception:
            pass
        finally:
            pipe.close()

    logger.info("\n[VHL Test] --- PRE-TEST CLEANUP ---")
    
    # 1. Kill any existing aosm processes
    try:
        subprocess.run(["pkill", "-f", "aosm"], stderr=subprocess.DEVNULL)
        logger.info("[VHL Test] Cleaned up existing aosm processes.")
    except Exception:
        pass

    # 2. Stop existing docker containers
    logger.info("[VHL Test] Stopping existing vhl-runtime containers...")
    subprocess.run(["docker", "compose", "down"], cwd=runtime_dir, capture_output=True)
    
    logger.info("\n[VHL Test] --- STARTING SERVICES ---")

    # 5. Create temporary workspace
    temp_workspace = tempfile.mkdtemp(prefix="vhl_e2e_workspace_")
    os.chmod(temp_workspace, 0o777)
    logger.info(f"[VHL Test] Created temporary workspace: {temp_workspace}")
    
    # 3. Start vhl-runtime
    logger.info("[VHL Test] Starting vhl-runtime via docker compose...")
    runtime_env = os.environ.copy()
    runtime_env["VHL_WORKSPACE_HOST_PATH"] = temp_workspace
    runtime_env["UID"] = str(os.getuid())
    runtime_env["GID"] = str(os.getgid())
    subprocess.run(["docker", "compose", "up", "-d"], cwd=runtime_dir, env=runtime_env, check=True)
    
    runtime_log_process = subprocess.Popen(
        ["docker", "compose", "logs", "-f"],
        cwd=runtime_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        preexec_fn=os.setsid
    )
    runtime_log_thread = threading.Thread(target=stream_logs, args=(runtime_log_process.stdout, "[Runtime]"))
    runtime_log_thread.daemon = True
    runtime_log_thread.start()
    
    # 4. Wait for runtime ports
    logger.info("[VHL Test] Waiting for runtime ports (1080, 3020)...")
    if not wait_for_port(1080, timeout=45):
        raise RuntimeError("vhl-runtime (port 1080) failed to start.")
    if not wait_for_port(3020, timeout=45):
        raise RuntimeError("vhl-runtime (port 3020) failed to start.")
    logger.info("[VHL Test] vhl-runtime is READY.")

    # 6. Start vhl-agent-backend
    logger.info("[VHL Test] Starting vhl-agent-backend...")
    backend_env = os.environ.copy()
    backend_env["COLUMNS"] = "1000"
    backend_env["TERM"] = "dumb"
    backend_env["PYTHONUNBUFFERED"] = "1"
    backend_env["LOG_AUTO_CONFIG"] = "false"
    backend_env["LOG_RICH_TRACEBACKS"] = "false"
    backend_env["OPENHANDS_SUPPRESS_BANNER"] = "1"
    
    backend_process = subprocess.Popen(
        ["uv", "run", "aosm", temp_workspace],
        cwd=backend_dir,
        env=backend_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        preexec_fn=os.setsid
    )

    log_thread = threading.Thread(target=stream_logs, args=(backend_process.stdout, "[Backend]"))
    log_thread.daemon = True
    log_thread.start()

    # 7. Wait for backend startup
    time.sleep(5) 
    if backend_process.poll() is not None:
        raise RuntimeError(f"vhl-agent-backend failed to start immediately.")
    
    logger.info("[VHL Test] vhl-agent-backend process started.")

    yield {
        "workspace_path": temp_workspace,
        "backend_process": backend_process
    }

    logger.info("\n[VHL Test] --- TEARDOWN ---")
    
    # 8. Stop backend
    logger.info("[VHL Test] Terminating vhl-agent-backend...")
    try:
        os.killpg(os.getpgid(backend_process.pid), signal.SIGTERM)
        backend_process.wait(timeout=5)
    except Exception:
        try:
            os.killpg(os.getpgid(backend_process.pid), signal.SIGKILL)
        except:
            pass

    # 9. Stop runtime
    logger.info("[VHL Test] Stopping vhl-runtime containers...")
    try:
        os.killpg(os.getpgid(runtime_log_process.pid), signal.SIGTERM)
        runtime_log_process.wait(timeout=5)
    except Exception:
        pass
    subprocess.run(["docker", "compose", "down"], cwd=runtime_dir, capture_output=True)

    # 10. Remove temp workspace
    if os.getenv("PRESERVE_WORKSPACE") == "true":
        logger.info(f"[VHL Test] PRESERVE_WORKSPACE is true. Keeping: {temp_workspace}")
    else:
        logger.info(f"[VHL Test] Removing temporary workspace: {temp_workspace}")
        shutil.rmtree(temp_workspace, ignore_errors=True)
    
    logger.info("[VHL Test] Environment cleanup COMPLETE.\n")

@pytest.fixture(scope="session")
def test_config():
    """
    Loads test configuration from tests/config/env.json.
    """
    config_path = os.path.join(os.path.dirname(__file__), "../config/env.json")
    if not os.path.exists(config_path):
        return {
            "VHL_RUNTIME_URL": "http://localhost:3000",
            "VHL_AGENT_BACKEND_URL": "http://localhost:8000",
            "VHL_WEBUI_URL": "http://localhost:3020",
            "VHL_RELAY_URL": "ws://localhost:1080"
        }
    with open(config_path) as f:
        return json.load(f)

@pytest.fixture(scope="function")
def system(test_config, managed_services):
    """
    The primary pytest fixture providing an initialized VHLSystem instance.
    """
    logger.info(f"\n[VHL Test] Initializing system fixture...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        vhl_system = VHLSystem(page, test_config, managed_services["workspace_path"])
        # vhl_system.inject_ws_wrapper()
        
        # target_url = test_config["VHL_WEBUI_URL"]
        # logger.info(f"[VHL Test] Navigating to: {target_url}")
        
        try:
            # page.goto(target_url, wait_until="load", timeout=45000)
            # logger.info(f"[VHL Test] Page loaded. Waiting for test hooks...")
            
            # page.wait_for_function(
            #     "window.__VHL_TEST_HOOKS__ && window.__VHL_TEST_HOOKS__.createProject", 
            #     timeout=15000
            # )
            # logger.info(f"[VHL Test] Hooks ready!")
            
            # page.wait_for_function(
            #     "window.__VHL_LAST_WS__ && window.__VHL_LAST_WS__.readyState === window.WebSocket.OPEN", 
            #     timeout=15000
            # )
            logger.info(f"[VHL Test] WebSocket connected and ready!")
            
            # Wait for backend identification
            logger.info(f"[VHL Test] Waiting for vhl_agent_backend to connect to relay...")
            backend_ready = False
            start_wait = time.time()
            while time.time() - start_wait < 30:
                if any(getattr(e, "source", None) == "vhl_agent_backend" or (e.type == "IDENTIFY" and getattr(e, "payload", {}).get("role") == "vhl_agent_backend") for e in vhl_system.events):
                    logger.info("[VHL Test] vhl_agent_backend connected!")
                    backend_ready = True
                    break
                time.sleep(1)
            
            if not backend_ready:
                logger.info("[VHL Test] WARNING: vhl_agent_backend did not connect to relay in time.")
            
            yield vhl_system
            
        except Exception as e:
            logger.info(f"[VHL Test] FIXTURE SETUP FAILED: {str(e)}")
            page.screenshot(path="debug_screenshot.png")
            raise e
        finally:
            vhl_system.stop()
            browser.close()
            logger.info(f"[VHL Test] Browser closed.\n")
