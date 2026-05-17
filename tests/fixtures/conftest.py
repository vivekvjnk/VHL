import pytest
import json
import os
import time
import threading
import websocket
import subprocess
import signal
import tempfile
import shutil
import socket
import sys
import sqlite3
from playwright.sync_api import sync_playwright

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
        self._observer_ws = None
        self._observer_thread = None
        self._stop_observer = threading.Event()
        self._setup_debug_listeners()
        self._start_observer()

    def _start_observer(self):
        """
        Starts a background thread that connects to the VHL Runtime as an observer.
        """
        ws_url = self.config["VHL_RELAY_URL"].replace("http", "ws") + "/ws-agent"
        print(f"[VHL Test] Connecting observer to: {ws_url}")

        def on_message(ws, message):
            try:
                msg = json.loads(message)
                self._handle_message(msg)
            except Exception as e:
                print(f"[VHL Test] Observer failed to parse message: {e}")

        def on_error(ws, error):
            print(f"[VHL Test] Observer error: {error}")

        def on_close(ws, close_status_code, close_msg):
            print(f"[VHL Test] Observer closed: {close_msg}")

        def on_open(ws):
            print(f"[VHL Test] Observer connected. Identifying...")
            ws.send(json.dumps({
                "type": "IDENTIFY",
                "payload": {"role": "vhl_test_observer"}
            }))

        self._observer_ws = websocket.WebSocketApp(
            ws_url,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )

        self._observer_thread = threading.Thread(target=self._observer_ws.run_forever)
        self._observer_thread.daemon = True
        self._observer_thread.start()

        # Wait for connection
        start = time.time()
        while time.time() - start < 5:
            if self._observer_ws.sock and self._observer_ws.sock.connected:
                print("[VHL Test] Observer ready!")
                return
            time.sleep(0.1)
        print("[VHL Test] WARNING: Observer connection timed out.")

    def _setup_debug_listeners(self):
        """
        Attaches listeners to the browser page to capture logs and errors.
        
        This method pipes browser console logs, page errors, and failed 
        network requests to the Python stdout for easier debugging.
        """
        self.page.on("console", lambda msg: print(f"[Browser Console] {msg.type}: {msg.text}"))
        self.page.on("pageerror", lambda exc: print(f"[Browser Error] {exc}"))
        self.page.on("requestfailed", lambda req: print(f"[Browser Request Failed] {req.method} {req.url} : {req.failure}"))

    def stop(self):
        """
        Stops the observer and performs cleanup.
        """
        if self._observer_ws:
            self._observer_ws.close()
        print("[VHL Test] Observer stopped.")

    def inject_ws_wrapper(self):
        """
        Injects a minimal synchronization wrapper into the browser.
        
        Note: Actual message interception is now handled by the central 
        relay observer. This wrapper only exists to provide synchronization 
        points (like window.__VHL_LAST_WS__) for the test fixture.
        """
        self.page.add_init_script("""
            console.log("[VHL Test] Injecting Lite WebSocket wrapper...");
            const OriginalWebSocket = window.WebSocket;
            
            const WrappedWebSocket = function(url, protocols) {
                const ws = new OriginalWebSocket(url, protocols);
                window.__VHL_LAST_WS__ = ws;
                return ws;
            };
            
            // Copy static constants
            WrappedWebSocket.prototype = OriginalWebSocket.prototype;
            WrappedWebSocket.CONNECTING = OriginalWebSocket.CONNECTING;
            WrappedWebSocket.OPEN = OriginalWebSocket.OPEN;
            WrappedWebSocket.CLOSING = OriginalWebSocket.CLOSING;
            WrappedWebSocket.CLOSED = OriginalWebSocket.CLOSED;
            
            window.WebSocket = WrappedWebSocket;
            console.log("[VHL Test] Lite wrapper ready.");
        """)

    def _handle_message(self, msg):
        """
        Callback function invoked by the browser when a WebSocket event is intercepted.
        
        Args:
            msg (dict): The captured JSON payload from the WebSocket.
        """
        if isinstance(msg, dict) and "type" in msg:
            print(f"[VHL Event : {msg.get('timestamp')}] {msg.get('source', 'unknown')}: {msg.get('type')}")
            # If message type is ERROR log the entire payload for debugging
            if msg.get("type") == "ERROR":
                print(f"[VHL Event] ERROR payload: {json.dumps(msg, indent=2)}")
            self.events.append(Event(msg))

    def clear_events(self):
        """
        Clears the captured events list. Useful before triggering a new action.
        """
        print(f"[VHL Test] Clearing {len(self.events)} captured events.")
        self.events = []

    def create_project(self, name, zip=None):
        """
        Triggers the project creation workflow in the WebUI.
        
        This method bypasses the manual UI clicks by calling the 'createProject' 
        hook exposed in ChatInterface.tsx. It waits for the WebSocket to be 
        in the OPEN state before execution to avoid 'Socket not open' errors.
        
        Args:
            name (str): The name of the project to create.
            zip (str, optional): A path to a local ZIP file OR a pre-uploaded blob ID.
        """
        # Safety check for WebSocket connectivity
        self.page.wait_for_function(
            "window.__VHL_LAST_WS__ && window.__VHL_LAST_WS__.readyState === window.WebSocket.OPEN", 
            timeout=10000
        )
        
        if zip and os.path.exists(zip):
            print(f"[VHL Test] Detected local zip file: {zip}. Uploading via WebUI...")
            import base64
            with open(zip, "rb") as f:
                content = base64.b64encode(f.read()).decode()
            
            self.page.evaluate(f"""
                (async () => {{
                    const base64Content = "{content}";
                    const binaryString = window.atob(base64Content);
                    const bytes = new Uint8Array(binaryString.length);
                    for (let i = 0; i < binaryString.length; i++) {{
                        bytes[i] = binaryString.charCodeAt(i);
                    }}
                    const blob = new Blob([bytes], {{ type: 'application/zip' }});
                    const file = new File([blob], 'project.zip', {{ type: 'application/zip' }});
                    
                    if (window.__VHL_TEST_HOOKS__ && window.__VHL_TEST_HOOKS__.createProject) {{
                        await window.__VHL_TEST_HOOKS__.createProject("{name}", file);
                    }} else {{
                        console.error("[VHL Test] createProject hook NOT FOUND");
                    }}
                }})();
            """)
        else:
            raise ValueError(f"Invalid zip path provided: {zip}")

    def emit_event(self, event_type, payload=None):
        """
        Emits a WebSocket event directly from the browser's WebSocket connection.
        
        Args:
            event_type (str): The type of event to emit.
            payload (dict, optional): The payload for the event.
        """
        payload = payload or {}
        print(f"[VHL Test] Emitting event: {event_type} with payload: {payload}")
        payload_json = json.dumps(payload)
        
        # We use window.__VHL_LAST_WS__ which was injected by inject_ws_wrapper
        self.page.evaluate(f"""
            (async () => {{
                if (window.__VHL_LAST_WS__ && window.__VHL_LAST_WS__.readyState === window.WebSocket.OPEN) {{
                    const event = {{
                        type: "{event_type}",
                        source: "vhl_webui",
                        payload: {payload_json},
                        timestamp: new Date().toISOString()
                    }};
                    console.log("[VHL Test] Sending event via WS:", event);
                    window.__VHL_LAST_WS__.send(JSON.stringify(event));
                }} else {{
                    console.error("[VHL Test] Cannot emit event: WebSocket not open or not found.", window.__VHL_LAST_WS__);
                }}
            }})();
        """)

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
        print(f"[VHL Test] Waiting for event: {event_type} (timeout={timeout}ms)")
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
                            
                    print(f"[VHL Test] Found event: {event_type}")
                    return event
            time.sleep(0.1) # Brief sleep to avoid high CPU
            self.page.wait_for_timeout(500)
        
        current_event_types = [e.type for e in self.events]
        print(f"[VHL Test] TIMEOUT waiting for {event_type}. Current events: {current_event_types}")
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
            print("[VHL Test] Workspace path NOT SET in system orchestrator. Skipping deep validation.")
            return True

        project_path = os.path.join(self.workspace_path, project_id)
        
        # 1. Validate SQLite Semantic Ledger
        db_path = os.path.join(project_path, ".vhl", "state.db")
        if not os.path.exists(db_path):
            print(f"[VHL Test] SQLite DB NOT FOUND at: {db_path}")
            return False
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check INITIALIZE operation
            cursor.execute("SELECT op_name, status FROM semantic_operations WHERE op_name='INITIALIZE'")
            row = cursor.fetchone()
            if not row or row[1] != "SUCCESS":
                print(f"[VHL Test] INITIALIZE operation NOT FOUND or failed in DB")
                conn.close()
                return False
            
            # Check for module entries
            cursor.execute("SELECT COUNT(*) FROM project_modules")
            count = cursor.fetchone()[0]
            if count == 0:
                print("[VHL Test] No modules found in DB")
                conn.close()
                return False
            
            conn.close()
            print("[VHL Test] SQLite Semantic Ledger VALIDATED.")
        except Exception as e:
            print(f"[VHL Test] Error validating SQLite DB: {e}")
            return False

        # 2. Validate Git Repository
        git_path = os.path.join(project_path, ".git")
        if not os.path.exists(git_path):
            print(f"[VHL Test] Git directory NOT FOUND at: {git_path}")
            return False
        print("[VHL Test] Git Repository VALIDATED.")

        # 3. Validate .gitignore
        gitignore_path = os.path.join(project_path, ".gitignore")
        if not os.path.exists(gitignore_path):
            print(f"[VHL Test] .gitignore NOT FOUND at: {gitignore_path}")
            return False
        
        with open(gitignore_path, 'r') as f:
            content = f.read()
            if ".vhl/" not in content:
                print("[VHL Test] .vhl/ directory NOT IGNORED in .gitignore")
                return False
        print("[VHL Test] .gitignore VALIDATED.")

        # 4. Validate Manifest (Artifact Space)
        # Basic check for expected modules in the Git-native manifest
        expected_modules = [
            "bms-monitor-module", "communication-bridge", "current-sensing", 
            "high-voltage-power-supply", "low-voltage-power-supply", 
            "microcontroller-module"
        ]
        for mod in expected_modules:
            if mod not in actual_manifest:
                print(f"[VHL Test] Manifest MISSING expected module: {mod}")
                return False
        
        print(f"[VHL Test] Backend manifest structure VALIDATED for {project_id}.")
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
                print(f"[VHL Test] Runtime manifest MISSING module: {module}")
                return False
            if not isinstance(actual_manifest[module], dict):
                print(f"[VHL Test] Runtime manifest key {module} expected to be a dict, but got {type(actual_manifest[module])}")
                return False
        
        # Check all generated files exist
        for gen_file in expected_generated_files:
            if gen_file not in actual_manifest:
                print(f"[VHL Test] Runtime manifest MISSING generated file: {gen_file}")
                return False
            if not isinstance(actual_manifest[gen_file], str):
                print(f"[VHL Test] Runtime manifest key {gen_file} expected to be a hash string, but got {type(actual_manifest[gen_file])}")
                return False

        # Ensure no unexpected top-level keys
        all_expected = set(expected_modules + expected_generated_files)
        actual_keys = set(actual_manifest.keys())
        unexpected = actual_keys - all_expected
        if unexpected:
            print(f"[VHL Test] Runtime manifest has UNEXPECTED keys: {unexpected}")
            return False

        print("[VHL Test] Runtime manifest structure VALIDATED.")
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
        print(f"[VHL Test] Checking WebUI reload state: {'RELOADED' if is_reloaded else 'NOT_RELOADED'} (URL: {current_url})")
        return is_reloaded

@pytest.fixture(scope="session")
def managed_services():
    """
    Manages the lifecycle of VHL Runtime and VHL Agent Backend for the test session.
    """
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    runtime_dir = os.path.join(root_dir, "vhl-runtime")
    backend_dir = os.path.join(root_dir, "vhl-agent-backend")
    
    print("\n[VHL Test] --- PRE-TEST CLEANUP ---")
    
    # 1. Kill any existing aosm processes
    try:
        subprocess.run(["pkill", "-f", "aosm"], stderr=subprocess.DEVNULL)
        print("[VHL Test] Cleaned up existing aosm processes.")
    except Exception:
        pass

    # 2. Stop existing docker containers
    print("[VHL Test] Stopping existing vhl-runtime containers...")
    subprocess.run(["docker", "compose", "down"], cwd=runtime_dir, capture_output=True)
    
    print("\n[VHL Test] --- STARTING SERVICES ---")
    
    # 3. Start vhl-runtime
    print("[VHL Test] Starting vhl-runtime via docker compose...")
    subprocess.run(["docker", "compose", "up", "-d"], cwd=runtime_dir, check=True)
    
    # 4. Wait for runtime ports
    print("[VHL Test] Waiting for runtime ports (1080, 3020)...")
    if not wait_for_port(1080, timeout=45):
        raise RuntimeError("vhl-runtime (port 1080) failed to start.")
    if not wait_for_port(3020, timeout=45):
        raise RuntimeError("vhl-runtime (port 3020) failed to start.")
    print("[VHL Test] vhl-runtime is READY.")

    # 5. Create temporary workspace
    temp_workspace = tempfile.mkdtemp(prefix="vhl_e2e_workspace_")
    print(f"[VHL Test] Created temporary workspace: {temp_workspace}")

    # 6. Start vhl-agent-backend
    print("[VHL Test] Starting vhl-agent-backend...")
    backend_env = os.environ.copy()
    replay_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "archy", "resources", "e2e_conversations")
    if os.path.exists(replay_dir):
        backend_env["VHL_E2E_REPLAY_DIR"] = replay_dir
        print(f"[VHL Test] Setting VHL_E2E_REPLAY_DIR to {replay_dir}")

    backend_process = subprocess.Popen(
        ["uv", "run", "aosm", temp_workspace],
        cwd=backend_dir,
        env=backend_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        preexec_fn=os.setsid
    )

    def stream_logs(pipe, prefix):
        try:
            for line in iter(pipe.readline, ''):
                if line:
                    sys.stdout.write(f"{prefix} {line}")
                    sys.stdout.flush()
        except Exception:
            pass
        finally:
            pipe.close()

    log_thread = threading.Thread(target=stream_logs, args=(backend_process.stdout, "[Backend]"))
    log_thread.daemon = True
    log_thread.start()

    # 7. Wait for backend startup
    time.sleep(5) 
    if backend_process.poll() is not None:
        raise RuntimeError(f"vhl-agent-backend failed to start immediately.")
    
    print("[VHL Test] vhl-agent-backend process started.")

    yield {
        "workspace_path": temp_workspace,
        "backend_process": backend_process
    }

    print("\n[VHL Test] --- TEARDOWN ---")
    
    # 8. Stop backend
    print("[VHL Test] Terminating vhl-agent-backend...")
    try:
        os.killpg(os.getpgid(backend_process.pid), signal.SIGTERM)
        backend_process.wait(timeout=5)
    except Exception:
        try:
            os.killpg(os.getpgid(backend_process.pid), signal.SIGKILL)
        except:
            pass

    # 9. Stop runtime
    print("[VHL Test] Stopping vhl-runtime containers...")
    subprocess.run(["docker", "compose", "down"], cwd=runtime_dir, capture_output=True)

    # 10. Remove temp workspace
    if os.getenv("PRESERVE_WORKSPACE") == "true":
        print(f"[VHL Test] PRESERVE_WORKSPACE is true. Keeping: {temp_workspace}")
    else:
        print(f"[VHL Test] Removing temporary workspace: {temp_workspace}")
        shutil.rmtree(temp_workspace, ignore_errors=True)
    
    print("[VHL Test] Environment cleanup COMPLETE.\n")

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
    print(f"\n[VHL Test] Initializing system fixture...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        vhl_system = VHLSystem(page, test_config, managed_services["workspace_path"])
        vhl_system.inject_ws_wrapper()
        
        target_url = test_config["VHL_WEBUI_URL"]
        print(f"[VHL Test] Navigating to: {target_url}")
        
        try:
            page.goto(target_url, wait_until="load", timeout=45000)
            print(f"[VHL Test] Page loaded. Waiting for test hooks...")
            
            page.wait_for_function(
                "window.__VHL_TEST_HOOKS__ && window.__VHL_TEST_HOOKS__.createProject", 
                timeout=15000
            )
            print(f"[VHL Test] Hooks ready!")
            
            page.wait_for_function(
                "window.__VHL_LAST_WS__ && window.__VHL_LAST_WS__.readyState === window.WebSocket.OPEN", 
                timeout=15000
            )
            print(f"[VHL Test] WebSocket connected and ready!")
            
            # Wait for backend identification
            print(f"[VHL Test] Waiting for vhl_agent_backend to connect to relay...")
            backend_ready = False
            start_wait = time.time()
            while time.time() - start_wait < 30:
                if any(getattr(e, "source", None) == "vhl_agent_backend" or (e.type == "IDENTIFY" and getattr(e, "payload", {}).get("role") == "vhl_agent_backend") for e in vhl_system.events):
                    print("[VHL Test] vhl_agent_backend connected!")
                    backend_ready = True
                    break
                time.sleep(1)
            
            if not backend_ready:
                print("[VHL Test] WARNING: vhl_agent_backend did not connect to relay in time.")
            
            yield vhl_system
            
        except Exception as e:
            print(f"[VHL Test] FIXTURE SETUP FAILED: {str(e)}")
            page.screenshot(path="debug_screenshot.png")
            raise e
        finally:
            vhl_system.stop()
            browser.close()
            print(f"[VHL Test] Browser closed.\n")
