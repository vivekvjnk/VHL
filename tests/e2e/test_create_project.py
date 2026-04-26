import pytest

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
    msg = system.wait_for_event("CREATE_PROJECT")
    assert msg.payload["zip_blob_id"].endswith(".zip")
    assert "/" not in msg.payload["zip_blob_id"] # Should be a flat hash-based filename

    # Step 4: Wait for backend completion
    created_msg = system.wait_for_event("PROJECT_CREATED")
    payload = created_msg.payload
    
    # Validate payload structure
    assert "project_id" in payload
    assert "project_root" in payload
    assert "workspace_info" in payload
    
    project_id = payload["project_id"]
    workspace_info = payload["workspace_info"]
    manifest = workspace_info["project_manifest"]

    # Step 5: Validate backend FS
    assert system.backend_has_structure(manifest)

    # Step 6: Wait for runtime completion
    runtime_msg = system.wait_for_event("DEV_SERVER_READY",timeout=60000) # Increased timeout for project creation flow
    runtime_manifest = runtime_msg.payload.get("manifest")

    # Step 7: Validate runtime FS + tsci
    assert system.runtime_initialized(runtime_manifest)

    # Step 8: Validate webui reaction
    assert system.webui_reloaded()

