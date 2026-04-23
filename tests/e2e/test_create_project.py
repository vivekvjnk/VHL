import pytest

@pytest.mark.e2e
def test_create_project_flow(system):
    """
    Test the full project creation flow from system level.
    This is a placeholder for the actual E2E test.
    """
    # Step 1: Trigger
    system.clear_events()
    system.create_project(name="bms-test", zip="tests/resources/bms-project.zip")

    # Step 2 & 3: Wait for upload + CREATE_PROJECT and validate
    msg = system.wait_for_event("CREATE_PROJECT")
    assert msg.payload["zip_blob_id"].endswith(".zip")
    assert "/" not in msg.payload["zip_blob_id"] # Should be a flat hash-based filename

    # Step 4: Wait for backend completion
    created_msg = system.wait_for_event("PROJECT_CREATED")
    project_id = created_msg.payload["project_id"]

    # Step 5: Validate backend FS
    assert system.backend_has_structure(project_id)

    # Step 6: Wait for runtime completion
    system.wait_for_event("DEV_SERVER_READY")

    # Step 7: Validate runtime FS + tsci
    assert system.runtime_initialized()

    # Step 8: Validate webui reaction
    assert system.webui_reloaded()

