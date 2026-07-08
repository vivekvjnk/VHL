# Repository Context: Virtual Hardware Laboratory (VHL)

## Project Overview
VHL is an agentic AI system for automated electronic circuit design. It transitions from high-level visual/textual intent to verified `tscircuit` code. The project is organized into a platform composed of backend, runtime, and web UI components, orchestrated via a Supervisor/Controller architecture designed to support modular, multi-step workflows.

---

## 1. VHL Agent Backend (`/vhl-agent-backend`)
The "Brain" of the system. A Python-based multi-agent orchestration layer.

- **Orchestration (AOSM)**: `/vhl-agent-backend/aosm/`
  - The top-level Agent Orchestration State Machine (`AOSM`). Manages project lifecycle, agent hand-offs, and communication.
- **Supervisor & Workflow Controllers**: `/vhl-agent-backend/vhl_common/supervisor/`
  - **Supervisor**: The central authority that manages agent registration, lifecycle, and authority delegation (claiming/releasing agents).
  - **Workflow Controllers**: Implement specific orchestration workflows (e.g., `Workflow1Controller`). A controller claims agents from the Supervisor, sends work, handles outcomes (retries, escalations, HIL interactions), and advances the workflow logic.
- **Agent Framework (URP)**: `/vhl-agent-backend/vhl_common/urp/`
  - Unified Resource Protocol used to define agents (`Archy`, `Librarian`, `ANA-D`) and their communication interfaces.
- **Agents**:
  - **Archy Agent**: `/vhl-agent-backend/archy/archy_agent/`
  - **Librarian Agent**: `/vhl-agent-backend/librarian/librarian_agent/`
  - **ANA-D Agent**: `/vhl-agent-backend/ana/ana_agent/`
    - ANA is now a standardized agent operating within the URP framework, not a state machine. It handles code generation, evaluation, and refinement.
- **Workspace Management**: `/vhl-agent-backend/vhl_common/workspace_manager/`
  - Handles the local side of the Copy-on-Write workspace and iteration directories.
- **Communication Protocol**: `/vhl-agent-backend/vhl_protocol/`
  - Shared models and WebSocket client implementation for Backend <-> Runtime sync.

## 2. VHL Runtime (`/vhl-runtime`)
The "Environment". A Docker-contained Node.js environment for execution and verification.

- **WebSocket Relay**: `/vhl-runtime/src/server/`
- **Workspace Manager**: `/vhl-runtime/src/workspace/`
- **VHL WebUI Backend Service (`vhlWebUI.ts`)**: `/vhl-runtime/src/workspace/vhlWebUI.ts`
  - Acts as the backend API and dev server manager for the `vhl-webui`. It runs `tsci dev` processes for circuit development, proxies traffic, manages project/module file access, and relays events between the UI and the Backend/AOSM.
- **MCP Servers**: `/vhl-runtime/src/mcp/`
  - Provides tools to the agents (e.g., library resolution, evaluation).

## 3. VHL Webui (`/vhl-webui`)
The "Interface". A React-based web UI for circuit visualization and agent interaction.

---

## Key Data Artifacts
- **SCUD (Shared Circuit Understanding Document)**: Markdown file describing circuit intent.

