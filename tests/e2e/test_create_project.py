import pytest
import os
import sqlite3
import logging 
import time
logger = logging.getLogger(__name__)

@pytest.mark.e2e
def test_create_project_flow(system):
    """
    Test the full project creation flow from system level.
    This is a placeholder for the actual E2E test.
    """
    # Step 1: Trigger
    system.clear_events()
    system.create_project(name="bms-project", zip="tests/resources/e2e/vhl-agent-backend/bms-project.zip")
    
    # Step 2 & 3: Wait for upload + CREATE_PROJECT and validate
    # Note: Using new flow, we don't upload to MinIO. 
    # The fixture emits CREATE_PROJECT with zip_blob_id="local_zip"
    
    # Step 4: Wait for backend completion
    created_msg = system.wait_for_event("PROJECT_CREATED")
    dev_server_ready_message = system.wait_for_event("DEV_SERVER_READY",timeout=60000)
    time.sleep(10) # simple sleep before moving forward
    payload = created_msg.payload
    
    # Validate payload structure
    assert "project_id" in payload
    assert "project_root" in payload
    assert "workspace_info" in payload
    
    project_id = payload["project_id"]
    workspace_info = payload["workspace_info"]
    manifest = workspace_info["project_manifest"]

    # Step 5: Validate backend FS
    assert system.backend_has_structure(project_id, manifest)
    # Step 5b: Validate Project Creation Evaluation in SQLite DB
    db_path = os.path.join(system.workspace_path, f"{project_id}_root", ".vhl", "state.db")
    
    assert os.path.exists(db_path), f"SQLite DB not found at {db_path}; workspace_path:{system.workspace_path}; project_id: {project_id}"
    
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT op_name, author, status, payload FROM semantic_operations WHERE op_name='CREATE_PROJECT_EVAL'"
        )
        row = cursor.fetchone()
        assert row is not None, "Semantic operation entry 'CREATE_PROJECT_EVAL' not found in database"
        assert row[1] == "PROJECT_CREATION_EVALUATOR", f"Expected author 'PROJECT_CREATION_EVALUATOR', got '{row[1]}'"
        assert row[2] == "SUCCESS", f"Project creation evaluation failed. Status: {row[2]}, Payload: {row[3]}"
        print("[VHL Test] SQLite DB verified: Project Creation Evaluation entry found and is SUCCESS!")
    finally:
        conn.close()

    # Step 6: Wait for runtime completion
    runtime_msg = system.wait_for_event("DEV_SERVER_READY",timeout=60000) # Increased timeout for project creation flow
    runtime_manifest = runtime_msg.payload.get("manifest")

    


