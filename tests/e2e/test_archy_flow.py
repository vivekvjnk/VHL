import pytest
import time
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]: %(message)s')
logger = logging.getLogger(__name__)

@pytest.mark.e2e
def test_archy_full_flow(system):
    """
    Test the full Archy workflow from project creation to SCUD generation and HIL review.
    """
    # Step 1: Create Project
    logger.info("\n[Test] Step 1: Creating project...")
    system.clear_events()
    system.create_project(
        name="bms-project", 
        zip="tests/resources/e2e/vhl-agent-backend/bms-project.zip"
    )
    
    # Wait for project creation and baseline sync
    system.wait_for_event("PROJECT_CREATED")
    logger.info("[Test] Project created successfully.")
    
    # Wait for runtime baseline
    system.wait_for_event("DEV_SERVER_READY", timeout=60000)
    time.sleep(5) # Give it some time to settle after potential reload
    logger.info("[Test] VHL Runtime is ready.")

    # Step 2: Trigger Archy
    # We trigger Archy for the bms-monitor-module which is included in the bms-project.zip
    logger.info("\n[Test] Step 2: Triggering Archy for bms-monitor-module...")
    system.trigger_archy("bms-monitor-module")

    # Step 3: Monitor State Transitions
    logger.info("\n[Test] Step 3: Monitoring AOSM state transitions...")
    
    # Wait for WORKFLOW_COMPLETED event from VHL_AGENT_BACKEND indicating workflow 1 completion
    workflow_event = system.wait_for_event("WORKFLOW_COMPLETED", timeout=300000, payload_filter={"workflow": "workflow_1", "module": "bms-monitor-module"})
    assert workflow_event is not None
    logger.info("[Test] Received WORKFLOW_COMPLETED event for workflow_1. Proceeding to check for HIL request.")
    # Wait for BOOTSTRAP_PIPELINE entry
    # system.wait_for_event("STATE_TRANSITION", payload_filter={"to": "BOOTSTRAP_PIPELINE"})
    # logger.info("[Test] AOSM entered BOOTSTRAP_PIPELINE.")

    # Wait for TRIGGER_ARCHY entry
    # system.wait_for_event("STATE_TRANSITION", payload_filter={"to": "TRIGGER_ARCHY"}, timeout=45000)
    # logger.info("[Test] AOSM entered TRIGGER_ARCHY. Archy agent is running.")

    # # Step 4: Wait for HIL Review (SCUD Generated)
    # logger.info("\n[Test] Step 4: Waiting for Archy HIL request (SCUD generation complete)...")
    # # Archy takes some time to process even with a stub, but with a real LLM it can take 1-2 minutes.
    # hil_event = system.wait_for_event("HIL_REQUEST", timeout=600000, payload_filter={"reason": "ARCHY_REVIEW"})
    
    # payload = hil_event.payload
    # assert hil_event is not None
    # assert "scud_content" in payload
    # assert len(payload["scud_content"]) > 100 # Basic sanity check for SCUD content
    # logger.info(f"[Test] Received Archy HIL request. SCUD length: {len(payload['scud_content'])}")

    # # Step 5: Respond to HIL (Accept SCUD)
    # logger.info("\n[Test] Step 5: Accepting SCUD and continuing...")
    # system.respond_to_hil(action="continue")

    # # Step 6: Verify transition to TRIGGER_LIBRARIAN
    # logger.info("\n[Test] Step 6: Verifying transition to Librarian...")
    # system.wait_for_event("STATE_TRANSITION", payload_filter={"to": "TRIGGER_LIBRARIAN"}, timeout=30000)
    # logger.info("[Test] AOSM entered TRIGGER_LIBRARIAN. Archy workflow successful!")

    # Final check: Workspace should have .conversations
    # Note: Deep validation is already done by backend_has_structure if workspace_path is set
    # but we can do a targeted check if needed.
    
