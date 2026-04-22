import pytest
import json
import os
import time
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
            config (dict): The test configuration loaded from env.json.
        """
        self.page = page
        self.config = config
        self.events = []
        self._setup_debug_listeners()

    def _setup_debug_listeners(self):
        """
        Attaches listeners to the browser page to capture logs and errors.
        
        This method pipes browser console logs, page errors, and failed 
        network requests to the Python stdout for easier debugging.
        """
        self.page.on("console", lambda msg: print(f"[Browser Console] {msg.type}: {msg.text}"))
        self.page.on("pageerror", lambda exc: print(f"[Browser Error] {exc}"))
        self.page.on("requestfailed", lambda req: print(f"[Browser Request Failed] {req.method} {req.url} : {req.failure}"))

    def inject_ws_wrapper(self):
        """
        Injects a JavaScript wrapper into the browser to intercept WebSocket traffic.
        
        This method MUST be called before page.goto(). It performs several critical tasks:
        1. Exposes a 'onVHLMessage' function to the browser to bridge messages back to Python.
        2. Replaces the global 'window.WebSocket' constructor with a proxy.
        3. Captures all outgoing (send) and incoming (message) JSON payloads.
        4. Preserves static WebSocket constants (OPEN, CONNECTING, etc.) to ensure 
           compatibility with application logic.
        5. Stores a reference to the active socket at 'window.__VHL_LAST_WS__' for 
           connection state monitoring.
        """
        self.page.expose_function("onVHLMessage", self._handle_message)
        self.page.add_init_script("""
            console.log("[VHL Test] Injecting WebSocket wrapper...");
            const OriginalWebSocket = window.WebSocket;
            
            const WrappedWebSocket = function(url, protocols) {
                console.log("[VHL Test] New WebSocket connection to:", url);
                const ws = new OriginalWebSocket(url, protocols);
                
                // Store reference for the test fixture to check readyState
                window.__VHL_LAST_WS__ = ws;
                
                // Proxy the send method to capture outgoing AgentMessages
                const originalSend = ws.send;
                ws.send = function(data) {
                    try {
                        const msg = typeof data === 'string' ? JSON.parse(data) : data;
                        window.onVHLMessage({ direction: 'sent', ...msg });
                    } catch(e) {
                        console.warn("[VHL Test] Failed to parse sent message:", e);
                    }
                    return originalSend.apply(this, arguments);
                };
                
                // Add listener to capture incoming AgentMessages
                ws.addEventListener('message', (event) => {
                    try {
                        const msg = typeof event.data === 'string' ? JSON.parse(event.data) : event.data;
                        window.onVHLMessage({ direction: 'received', ...msg });
                    } catch(e) {
                        console.warn("[VHL Test] Failed to parse received message:", e);
                    }
                });
                
                return ws;
            };
            
            // Critical: Copy prototype and static constants to the wrapper
            WrappedWebSocket.prototype = OriginalWebSocket.prototype;
            WrappedWebSocket.CONNECTING = OriginalWebSocket.CONNECTING;
            WrappedWebSocket.OPEN = OriginalWebSocket.OPEN;
            WrappedWebSocket.CLOSING = OriginalWebSocket.CLOSING;
            WrappedWebSocket.CLOSED = OriginalWebSocket.CLOSED;
            
            window.WebSocket = WrappedWebSocket;
            console.log("[VHL Test] WebSocket wrapper injected successfully.");
        """)

    def _handle_message(self, msg):
        """
        Callback function invoked by the browser when a WebSocket event is intercepted.
        
        Args:
            msg (dict): The captured JSON payload from the WebSocket.
        """
        if isinstance(msg, dict) and "type" in msg:
            print(f"[VHL Event] {msg.get('direction', 'unknown')}: {msg.get('type')}")
            self.events.append(Event(msg))

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
            time.sleep(0.5)
        
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

    def backend_has_structure(self, structure):
        """
        Validates that the Backend's filesystem contains the expected project structure.
        
        Note: Currently a placeholder for future implementation via direct FS check or API.
        """
        return True

    def runtime_initialized(self):
        """
        Validates that the VHL Runtime has correctly initialized the project workspace.
        
        Note: Currently a placeholder for future implementation.
        """
        return True

    def webui_reloaded(self):
        """
        Validates that the WebUI has successfully reacted to system events (e.g., reloaded).
        
        Note: Currently a placeholder for future implementation.
        """
        return True

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
            "VHL_WEBUI_URL": "http://localhost:3020"
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
            browser.close()
            print(f"[VHL Test] Browser closed.\\n")
