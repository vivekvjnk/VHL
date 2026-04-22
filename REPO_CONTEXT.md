# Repository Context: Virtual Hardware Laboratory (VHL)

## Project Overview
VHL is an agentic AI system for automated electronic circuit design. It transitions from high-level visual/textual intent to verified `tscircuit` code. The project is organized into three primary repositories/directories behaving as a single platform.

---

## 1. VHL Agent Backend (`/vhl-agent-backend`)
The "Brain" of the system. A Python-based multi-agent orchestration layer.

- **Orchestration (AOSM)**: `/vhl-agent-backend/aosm/state_machine/aosm.py`
  - The top-level Agent Orchestration State Machine. Manages project lifecycle and agent hand-offs.
- **Archy Agent**: `/vhl-agent-backend/archy/archy_agent/`
  - Generates the Shared Circuit Understanding Document (SCUD) from schematic images. Uses SAM3 for segmentation.
- **Librarian Agent**: `/vhl-agent-backend/librarian/librarian_agent/`
  - Resolves component inventories into actual library imports via MCP.
- **ANAlog Designer (ANA-D)**: `/vhl-agent-backend/ana/ana_agent/`
  - `state_machine/ana_sm.py`: Manages the iterative refinement loop.
  - `ana_worker_1/`: LLM-based code generator (Writes `.tsx`).
  - `ana_worker_2/`: Deterministic validation trigger (Client for VAP).
  - `observer/`: Analyzes evaluation results and "commits" findings via MCP.
- **Workspace Management**: `/vhl-agent-backend/workspace/manager.py` (referenced as `vhl_workspace`)
  - Handles the local side of the Copy-on-Write workspace and iteration directories.
- **Communication Protocol**: `/vhl-agent-backend/vhl_protocol/`
  - Shared models and WebSocket client implementation for Backend <-> Runtime sync.

## 2. VHL Runtime (`/vhl-runtime`)
The "Environment". A Docker-contained Node.js environment for execution and verification.

- **WebSocket Relay**: `/vhl-runtime/src/server/`
  - Hub for communication between runframe (UI) and AOSM (Backend).
- **Workspace Manager**: `/vhl-runtime/src/workspace/`
  - **Sync Logic**: `syncManager.ts` (Implements the hashing/transfer protocol).
  - **VAP Handlers**: `vapHandlers.ts` (Handles evaluation requests from the agent).
- **MCP Servers**: `/VHL_runtime/src/mcp/`
  - **Python Servers**: Manages `tsci` library operations.
  - **ANA MCP**: Internal server for agent observations.
- **Configuration**: `/vhl-runtime/src/config/`
  - Environment-specific paths and settings.

## 3. runframe (`/vhl-webui`)
The "Interface". A React-based web UI for circuit visualization and agent interaction.

- **Agent UI Components**: `/vhl-webui/lib/components/ChatInterface/`
  - `ChatInterface.tsx`: The primary entry point for the Agent HUD.
  - `hooks/`: Integration hooks for WebSockets and agent status tracking.
- **Circuit Preview**: Integrated `tsci` preview components.

## 4. Supporting Repositories
These are internal modules used by the runtime but often treated as sub-modules or future-use repos:
- `/vhl-cli`: tscircuit CLI core tuned for VHL.

---

## Key Data Artifacts
- **SCUD (Shared Circuit Understanding Document)**: Markdown file describing circuit intent.
- **StableCircuit**: The verified and accepted `.tsx` file in the project's `Stable/` directory.
- **Iteration Directories**: `iterations/iteration_<suffix>/` where active design work happens.

## Spelling Invariant
*   **Virtual Hardware Labratary**: The misspelling "Labratary" is intentional in certain logs/repos to acknowledge the potential for system error.
