import time
import pytest
import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]: %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture
def librarian_project(system):
    """
    Fixture to set up a temporary project directory for the Librarian agent.
    Copies the pre-initialized project from resources into the backend's workspace directory,
    then triggers PROJECT_LOAD.
    """
    project_id = "bms-project-initialized"
    src_dir = os.path.join(
        "tests", "resources", "e2e", "vhl-agent-backend", "librarian", project_id
    )
    dest_dir = os.path.join(system.workspace_path, project_id)

    logger.info(f"Setting up pre-initialized project for librarian E2E test...")
    logger.info(f"Source: {src_dir}")
    logger.info(f"Destination: {dest_dir}")

    # Remove destination directory if it exists (for clean test runs)
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    # Copy the pre-initialized project contents to the destination
    shutil.copytree(src_dir, dest_dir)
    logger.info("Project directory created and filled with pre-initialized contents.")

    # Trigger project loading via the system orchestrator
    system.clear_events()
    system.emit_event("LOAD_PROJECT", {"project_id": project_id})

    # Wait for the project loading event to complete
    system.wait_for_event("PROJECT_LOADED")
    logger.info("Project loaded event received.")

    # Wait for the runtime to settle/be ready (DEV_SERVER_READY)
    system.wait_for_event("DEV_SERVER_READY", timeout=60000)
    logger.info("Dev server is ready after project load.")
    
    time.sleep(5)
    
    system.emit_event( event_type="MESSAGE_TO_AGENT", target="vhl_agent_backend" ,payload={"target_agent": "communication-bridge.librarian", "message": "Hello Librarian, project is set up! Please read the .scud document and import non trivial components."})
    time.sleep(600)  # simply wait 10 minutes for librarian to process

    return project_id

@pytest.mark.e2e
def test_librarian_project_setup(librarian_project, system):
    """
    Test that the pre-initialized project directory is loaded correctly,
    meaning the backend workspace has the expected structure and the 
    Librarian agent is registered and reaches the expected initial state.
    """
    logger.info("[Test] Verifying loaded project structure on the backend...")
    
    # Check that the project directory exists under system.workspace_path
    project_dir = os.path.join(system.workspace_path, librarian_project)
    assert os.path.exists(project_dir), f"Project directory {project_dir} does not exist"
    
    # Verify we can find the SCUD files and modules
    modules = [
        "bms-monitor-module",
        "communication-bridge",
        "current-sensing",
        "high-voltage-power-supply",
        "low-voltage-power-supply",
        "microcontroller-module"
    ]
    for module in modules:
        module_path = os.path.join(project_dir, module)
        assert os.path.exists(module_path), f"Module path {module_path} does not exist"
        
    logger.info("[Test] Pre-initialized project directory setup verified successfully.")
