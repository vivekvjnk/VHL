# VHL System Test Suite

This directory contains the system-level (E2E and Integration) tests for the VHL-System.

## Structure

- `e2e/`: End-to-end tests covering full user flows.
- `integration/`: Tests for interactions between modules (e.g., Runtime <-> Agent Backend).
- `fixtures/`: Shared pytest fixtures.
- `assertions/`: Custom assertion helpers.
- `test_cases/`: Complex test case definitions.

## Running Tests

### System Level (pytest)
```bash
pytest tests/
```

### Module Level

#### VHL Runtime (Vitest)
```bash
cd vhl-runtime
npm test
```

#### VHL Agent Backend (pytest)
```bash
cd vhl-agent-backend
pytest tests/
```

#### VHL WebUI (Vitest & Playwright)
```bash
cd vhl-webui
npm test          # Vitest unit tests
npm run test:e2e  # Playwright E2E tests
```

## Configuration
Configuration is managed in `tests/config/env.json`.
