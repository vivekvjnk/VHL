# Snapshot-Replay Feasibility Study for E2E Test Cases

## 1. Executive Summary
This document analyzes the feasibility of integrating "snapshot-replay" functionality into the End-to-End (E2E) test cases of the VHL system. By leveraging the existing `ReplayLLM` infrastructure, we aim to enable deterministic, LLM-augmented testing at the system level.

## 2. Analysis of Existing Infrastructure

### 2.1 ReplayLLM & SnapshotLoader
Located at: `vhl-agent-backend/tests/fixtures/replay_snapshot_test_llm/`

*   **ReplayLLM**: A mock LLM that satisfies the OpenHands `LLM` interface but returns scripted responses from historical snapshots.
*   **SnapshotLoader**: Handles path resolution and event extraction from OpenHands-style persistence directories.
*   **Current Usage**: Primarily used in unit/module tests (e.g., `test_archy_urp.py`) where the test runner has direct control over agent instantiation.

### 2.2 Agent Orchestration (AOSM & Supervisor)
*   **AOSM**: The central state machine (`vhl-agent-backend/aosm/state_machine/aosm.py`) that manages the project lifecycle and triggers workflows.
*   **Supervisor**: Manages agent lifecycles, claiming, and routing.
*   **Workflow1Controller**: Coordinates the sequential execution of Archy, Librarian, and Ana.
*   **Registration**: Agents are registered and instantiated dynamically within the `AOSM` process using `AgentRegistry`.

### 2.3 Agent Implementation (URP Agents)
*   Agents (Archy, Librarian, Ana) inherit from `AbstractURPAgent`.
*   Most agents instantiate their `LLM` during the `_on_initialize` phase if one is not provided.
*   **Key Files**:
    *   `vhl-agent-backend/archy/archy_agent/urp_archy.py`
    *   `vhl-agent-backend/librarian/librarian_agent/urp_librarian.py`
    *   `vhl-agent-backend/ana/ana_agent/ana_urp/urp_ana.py`

## 3. Challenges for E2E Integration

1.  **Process Isolation**: E2E tests run `aosm` in a separate process. Standard dependency injection of `ReplayLLM` instances via constructor is not possible.
2.  **Multi-Agent Coordination**: A single E2E flow involves multiple agents. Each agent requires its own specific snapshot for replay.
3.  **Path Stability**: Snapshots contain absolute paths (e.g., workspace paths) that change across different test runs. `ReplayLLM` already has some logic for this, but it needs to be generalized.
4.  **Configuration**: We need a standard way to signal to all agents in the system when they should operate in "replay mode".

## 4. Proposed Implementation Strategy (Minimal Changes)

### 4.1 Global Replay Signal
Leverage the existing `VHL_E2E_REPLAY_DIR` environment variable. When set, agents should attempt to find snapshots within this directory.

### 4.2 Standardized LLM Injection Point
Instead of agents creating their own `LLM` instances directly via environment variables, we should introduce a utility function:

```python
# vhl_common/utils/llm_utils.py (Conceptual)
def get_llm_for_agent(agent_id: str, workspace_path: str) -> LLM:
    replay_base = os.getenv("VHL_E2E_REPLAY_DIR") # Assumption: replay_base directory contain agent snapshots for the sample project
    if replay_base:
        # agent_id follows the convention <module_name>.<agent_name>; eg: communication-bridge.archy
        agent_id_parts = agent_id.split('.')  
        module_name = agent_id_parts[0]
        agent_type = agent_id_parts[1] # e.g., 'archy'
        agent_replay_dir = os.path.join(replay_base, module_name, agent_type)
        if os.path.exists(agent_replay_dir):
            return ReplayLLM.from_persistence(
                agent_replay_dir, 
                current_workspace=workspace_path
            )
    # Fallback to standard LLM creation
    ...
```

### 4.3 Update Agent Initialization
Modify the `_on_initialize` method in all URP agents to use the standardized LLM factory.

### 4.4 Enhance Replay Discovery
Update `SnapshotLoader` to support a structured replay directory:
```
VHL_E2E_REPLAY_DIR/
├── archy/
│   └── events/
├── librarian/
│   └── events/
└── ana/
    └── events/
```

## 5. Feasibility Conclusion
The integration is **highly feasible**. The core replay logic is already implemented. The primary effort lies in:
1.  Moving `ReplayLLM` from test fixtures to a permanent location in `vhl_common` or a dedicated library to make it available to the production code during tests.
2.  Standardizing LLM instantiation across all agents.
3.  Updating the E2E test fixture to organize snapshots into the expected directory structure.

This approach maintains the system-level integrity of E2E tests while providing the determinism needed for regression testing.
