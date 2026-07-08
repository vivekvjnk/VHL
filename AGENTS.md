# VHL System Agent Knowledge Base

The Virtual Hardware Laboratory (VHL) is an automated system for electronic circuit design, utilizing multi-agent orchestration, deterministic runtime validation, and real-time frontend visualization.

## System Architecture

The VHL system follows a layered architecture:

1.  **Frontend (`vhl-webui`)**: React-based UI for user interaction and circuit visualization.
2.  **Orchestration (`vhl-agent-backend`)**: The "brain" of the system. A state-aware orchestration layer (AOSM) coordinating specialized agents (`ana`, `archy`, `librarian`) to process design intents.
3.  **Runtime (`vhl-runtime`)**: The core infrastructure bridging the agents to the physical environment. Handles file operations, WebSocket communication, and circuit evaluation (VAP).

## Key Components

- **[vhl-agent-backend](vhl-agent-backend/AGENTS.md)**: Agent orchestration, state machine logic, and multi-agent circuit design workflows.
- **[vhl-runtime](vhl-runtime/AGENTS.md)**: Infrastructure core, filesystem abstractions, WebSocket communication, and circuit evaluation engine.
- **[vhl-webui](vhl-webui/AGENTS.md)**: Frontend architecture, API interactions, and UI components.

## Workflow Patterns

### Integrated Design Loop
1.  **Perception**: User uploads schematic -> `vhl-webui` -> `archy` analyzes images into SCUD.
2.  **Resolution**: `librarian` uses MCP to fetch necessary libraries based on SCUD.
3.  **Synthesis**: `ana` iterative loop (Generator/Validator/Observer) creates/refines circuit code (`.tsx`).
4.  **Validation**: Code staged via `vhl-runtime` -> `vap` engine runs evaluations -> results fed back to `ana`.
5.  **Commit**: Validated components are persisted to the library.

## Testing & Stability
The VHL system supports deterministic E2E testing using a snapshot-replay mechanism, ensuring stability and reducing costs during regression testing.

### E2E Testing with Snapshot Replay

- **vhl_common.llm.ReplayLLM**: Replays recorded responses from a conversation snapshot.
- **Path Substitution**: `ReplayLLM` automatically adjusts absolute paths from snapshots to the current workspace, essential for `FileEditorTool`.

### How to use Replay in Tests

1. Set `VHL_E2E_REPLAY_DIR` to the base directory containing your snapshots.
2. Ensure agents are initialized through the URP `initialize()` method, which calls `get_llm_for_agent()`.
3. In tests, you can also manually instantiate `ReplayLLM` using `ReplayLLM.from_persistence(path, current_workspace=...)` to enable path substitution.
