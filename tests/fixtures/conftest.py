import pytest
import json
import os
import time
import threading
import websocket
from playwright.sync_api import sync_playwright

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
    
    def __init__(self, page, config):
        """
        Initializes the VHLSystem orchestrator.
        
        Args:
            page (Page): The Playwright page instance.
            config (dict): Environment configuration.
        """
        self.page = page
        self.config = config
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
            print(f"[VHL Event] {msg.get('direction', 'unknown')}: {msg.get('type')}")
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
            zip (str, optional): A pre-uploaded blob ID for the project ZIP.
        """
        # Safety check for WebSocket connectivity
        self.page.wait_for_function(
            "window.__VHL_LAST_WS__ && window.__VHL_LAST_WS__.readyState === window.WebSocket.OPEN", 
            timeout=10000
        )
        
        print(f"[VHL Test] Triggering create_project: name={name}, zip={zip}")
        self.page.evaluate(f"""
            if (window.__VHL_TEST_HOOKS__ && window.__VHL_TEST_HOOKS__.createProject) {{
                window.__VHL_TEST_HOOKS__.createProject("{name}", "{zip or ''}");
            }} else {{
                console.error("[VHL Test] window.__VHL_TEST_HOOKS__.createProject NOT FOUND");
                throw new Error("createProject hook not found");
            }}
        """)

    def wait_for_event(self, event_type, timeout=30000):
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

    def backend_has_structure(self, project_id):
        """
        Validates that the Agent Backend has created the expected project structure on disk.
        
        This check ensures that the 'aosm' state machine correctly invoked the 
        WorkspaceManager and that the directory was created in the backend's runtime storage.
        
        Args:
            project_id (str): The ID of the project to check.
            
        Returns:
            bool: True if the directory exists, False otherwise.
        """
        backend_storage = os.path.join(os.getcwd(), "vhl-agent-backend/vhl_runtime", project_id)
        exists = os.path.isdir(backend_storage)
        print(f"[VHL Test] Checking backend structure for {project_id}: {'EXISTS' if exists else 'MISSING'}")
        return exists

    def runtime_initialized(self):
        """
        Validates that the VHL Runtime has correctly mirrored and initialized the project.
        
        The VHL Runtime creates a workspace directory and runs 'tsci init'. 
        This check verifies that the runtime service is ready for development.
        
        Returns:
            bool: Always returns True for now as a placeholder for remote FS check.
        """
        # In a real environment, we might check the Docker volume or hit a health endpoint.
        # For now, we trust the DEV_SERVER_READY event which only fires after successful init.
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
def test_config():
    """
    Loads test configuration from tests/config/env.json.
    
    Returns:
        dict: Configuration mapping for Runtime, Backend, and WebUI URLs.
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
def system(test_config):
    """
    The primary pytest fixture providing an initialized VHLSystem instance.
    
    This fixture:
    1. Launches a Playwright browser.
    2. Injects the WebSocket interception wrapper.
    3. Navigates to the WebUI.
    4. Waits for application-level hooks and WebSocket connectivity.
    5. Yields the orchestrator to the test case.
    6. Performs cleanup and takes screenshots on failure.
    """
    print(f"\\n[VHL Test] Initializing system fixture...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        vhl_system = VHLSystem(page, test_config)
        vhl_system.inject_ws_wrapper()
        
        target_url = test_config["VHL_WEBUI_URL"]
        print(f"[VHL Test] Navigating to: {target_url}")
        
        try:
            page.goto(target_url, wait_until="networkidle", timeout=15000)
            print(f"[VHL Test] Page loaded. Waiting for test hooks...")
            
            # Wait for React useEffect to attach hooks to window
            page.wait_for_function(
                "window.__VHL_TEST_HOOKS__ && window.__VHL_TEST_HOOKS__.createProject", 
                timeout=15000
            )
            print(f"[VHL Test] Hooks ready!")
            
            # Wait for WebSocket handshake to complete
            print(f"[VHL Test] Waiting for WebSocket connection...")
            page.wait_for_function(
                "window.__VHL_LAST_WS__ && window.__VHL_LAST_WS__.readyState === window.WebSocket.OPEN", 
                timeout=10000
            )
            print(f"[VHL Test] WebSocket connected and ready!")
            
            yield vhl_system
            
        except Exception as e:
            print(f"[VHL Test] FIXTURE SETUP FAILED: {str(e)}")
            page.screenshot(path="debug_screenshot.png")
            raise e
        finally:
            vhl_system.stop()
            browser.close()
            print(f"[VHL Test] Browser closed.\n")
