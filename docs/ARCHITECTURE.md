# Virtual Hardware Laboratory (VHL) Design Document

## 1. Introduction

The Virtual Hardware Laboratory (VHL) is an agentic AI system designed to automate the process of creating electronic circuits from high-level functional descriptions or schematic images.

VHL bridges the gap between intent and implementation by leveraging a sophisticated multi-agent orchestration layer that translates high-level concepts into verified `tscircuit` code. The system is designed around the following core philosophies:

*   **Modular Agentic Orchestration**: Rather than a monolithic control loop, VHL uses a **Supervisor/Controller** architecture. A central `Supervisor` manages agent lifecycles, while specialized `WorkflowControllers` orchestrate multi-step processes, delegating tasks to agents based on their capabilities.
*   **Unified Runtime Primitives (URP)**: All agents (Archy, Librarian, ANA-D) are built upon the URP, a language-agnostic, message-driven primitive. This ensures consistent initialization, communication, and state management across the system.
*   **Deterministic Evaluation (VAP)**: VHL complements agentic reasoning with the **VAP (VHL Ana Process)**, a deterministic validation pipeline. This pipeline ensures that generated circuit code is not only syntactically correct but also physically valid (linting, rendering, connectivity checks).
*   **Human-in-the-Loop (HIL)**: VHL is designed as a collaborative tool. When the system encounters ambiguity or architectural conflicts, it safely escalates to the user for guidance, maintaining a balance between automation and human oversight.

The system is organized into three primary domains:

1.  **VHL Agent Backend**: The "Brain" of the system, implementing the Supervisor/Controller architecture, workflow logic, and URP-based agents.
2.  **VHL Runtime**: The execution environment containing the `tscircuit` toolchain, MCP infrastructure, and VAP engine.
3.  **VHL WebUI**: The interface for circuit visualization, chat-based interaction, and project management.

## 2. Core Abstractions

### 2.1 Unified Runtime Primitive (URP)
The URP is the foundational execution model for VHL agents. It provides a standardized interface for:
*   **Addressable Identity**: Each agent has a unique runtime ID.
*   **Mailbox-driven Invocation**: Asynchronous, decoupled communication via message envelopes.
*   **Capability Declaration**: Agents advertise their supported operations.
*   **Persistent State**: State management isolated within the agent's context.

### 2.2 VHL Ana Process (VAP)
VAP is the deterministic validation pipeline triggered by the `ANA-D` agent. It provides a reliable feedback loop for synthesis:
*   **Rendering**: Compiles and renders `.tsx` circuit code.
*   **Linting & Checking**: Performs deterministic checks (connectivity, footprint validity, spacing).
*   **Decision Mapping**: Evaluates the output to determine if the design should be **ACCEPTED**, **REJECTED** (with feedback), or requires **HIL** intervention.

## 3. Backend Architecture (`/vhl-agent-backend`)
The backend is a Python-based multi-agent orchestration layer.

### 3.1 Orchestration (AOSM)
The AOSM is the top-level orchestration layer responsible for project lifecycle management and system-wide communication.

### 3.2 Supervisor & Workflow Controllers
The system utilizes a Supervisor/Controller pattern to handle modular, multi-step workflows.

*   **Supervisor**: The central authority that manages agent registration, maintains the system-wide agent registry, and handles authority delegation (claiming/releasing agents).
*   **Workflow Controllers**: Controllers (e.g., `Workflow1Controller`) implement specific business logic. They claim agents from the Supervisor, coordinate task execution, handle outcomes (including retries, escalations, and HIL interactions), and advance the workflow.

### 3.3 Agent Ecosystem
Agents in VHL are built on the **URP (Unified Runtime Primitive)**. Standardized agents include:

*   **Archy Agent**: Handles schematic parsing and SCUD generation.
*   **Librarian Agent**: Manages component resolution via MCP.
*   **ANA-D Agent**: Performs synthesis, evaluation, and refinement loops.

## 4. Runtime Architecture (`/vhl-runtime`)
The Runtime provides the execution environment for VHL.

*   **Workspace Manager**: Manages project state, file operations, and Copy-on-Write (CoW) iteration handling.
*   **VHL WebUI Backend Service (`vhlWebUI.ts`)**: Acts as the backend API and dev server manager for the `vhl-webui`. It runs `tsci dev` processes for circuit development, proxies traffic, manages project/module file access, and relays events between the UI and the Backend.
*   **MCP Infrastructure**: Provides necessary tools (Library Resolution, Ana Observation) to the agents.
*   **VAP Engine**: The deterministic validation engine.
