import pytest

@pytest.mark.e2e
def test_create_project_flow(system):
    """
    Test the full project creation flow from system level.
    This is a placeholder for the actual E2E test.
    """
    # Step 1: Trigger
    system.create_project(name="test", zip="file.zip")

    # Step 2: Wait for upload + CREATE_PROJECT
    system.wait_for_event("CREATE_PROJECT")

    # Step 3: Validate message content
    msg = system.get_event("CREATE_PROJECT")
    assert "blob_id" in msg.payload

    # Step 4: Wait for backend completion
    system.wait_for_event("PROJECT_CREATED")

    # Step 5: Validate backend FS
    assert system.backend_has_structure(...)

    # Step 6: Wait for runtime completion
    system.wait_for_event("DEV_SERVER_READY")

    # Step 7: Validate runtime FS + tsci
    assert system.runtime_initialized()

    # Step 8: Validate webui reaction
    assert system.webui_reloaded()

