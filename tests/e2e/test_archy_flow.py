import pytest
import time
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
logger = logging.getLogger(__name__)

@pytest.mark.e2e
def test_archy_full_flow(system):
    """
    Test the full Archy workflow from project creation to SCUD generation and HIL review.
    """
    # module_name = "communication-bridge"
    module_name = "bms-monitor-module"  # This module is included in the bms-project.zip for testing
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
    system.trigger_archy(module_name)

    # Step 3: Monitor State Transitions
    logger.info("\n[Test] Step 3: Monitoring AOSM state transitions...")
    
    # Wait for WORKFLOW_COMPLETED event from VHL_AGENT_BACKEND indicating workflow 1 completion
    workflow_event = system.wait_for_event("WORKFLOW_COMPLETED", timeout=3600000, payload_filter={"workflow": "workflow_1", "module": module_name})
    assert workflow_event is not None
    logger.info("[Test] Received WORKFLOW_COMPLETED event for workflow_1. Proceeding to check for HIL request.")

"""
TODO
====
Following features are not yet validated for Archy 
## 1. HIL interaction
Current implementation of Archy URP instructs agent to consult user(experienced engineer) to resolve ambiguities.
URP system uses "check_postcondition" method to determine if agent is either "finished" the task or "waiting" for user input.
Orchestration layer relies on the state of URP agent(which in turn uses the post condition check as explained above) to decide the next step

Happy path for this workflow is 
- No HIL interaction
- Archy finish scud generation without any errors
- "check_postcondition" is successful

We've successfully validated the "Happy path" multiple times.

HIL interaction path needs to be thoroughly validated.
For this, following is the pre-requisite:
- Module with sufficient ambiguity in input data so that Archy should raise concerns

"""