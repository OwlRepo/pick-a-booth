# Entry Point

> Purpose: the front door to the `docs/ai/*` navigation tree — what this repo is and how these docs fit together.
> Load rule: read this first when you land in the repo and need orientation.
> Source of truth: all files here are MAPS, never proof. Real code, tests, schemas, and routes are the truth. If a map conflicts with code, code wins.

pick-a-booth is OwlRepo's public fork of photobooth-app: a Python/FastAPI photobooth that drives DSLR, Raspberry Pi and web cameras, processes stills/GIFs/collages/videos, and serves a Vue3 kiosk UI built from `frontend/`. The authoritative project context lives in `CLAUDE.md` and `AGENTS.md` at the repo root — do not restate them; read them. The workflow core (Canonical Task Flow) lives in `AGENTS.md`; the phase docs `planning.md`, `execution.md`, and `handoff.md` here carry the plan-time, execute-time, and completion rules, loaded at their flow node. The rest of `docs/ai/*` is a navigation layer: `task-router.md` classifies the task, the manifest and ownership map describe the system, `contracts/*`, `testing-strategy.md` and `risk-register.md` describe the surfaces you must not break, and `file-index/repository-map.md` saves you from blind search. `operating-contract.md` is a compatibility pointer only. Unknowns are written as `TODO: Fill after repository analysis. Do not treat as verified.` and inferences as `(inferred, please correct if wrong)`.

## Context Order

Load in this order for a code-changing task:

1. `AGENTS.md` — workflow core (Canonical Task Flow, core principles, stop conditions).
2. `docs/ai/task-router.md` — classify intent, size, domain, risk; exact skill mappings.
3. `docs/ai/architecture-manifest.md` — system shape.
4. `docs/ai/module-ownership-map.md` — which layer owns what you are touching.
5. `docs/ai/agent-orchestration.md` — before dispatching implementer personas together.
6. `docs/ai/contracts/api-contracts.md` — the API surface.
7. `docs/ai/contracts/db-contracts.md` — the data model.
8. `docs/ai/testing-strategy.md` — how to test at this task size.
9. `docs/ai/risk-register.md` — is this a Deep-by-default area?
10. `docs/ai/file-index/repository-map.md` — exact paths and lines.
11. Related tests under `src/tests/tests/`.
12. The target source file(s).

Phase docs load at their flow node, not up front: `docs/ai/planning.md` + `docs/ai/plan-template.md` before writing a plan; `docs/ai/execution.md` before writing code; `docs/ai/handoff.md` before declaring done; `docs/ai/pr-evidence.md` before creating any PR.

Everything above is a map. When the map and the code disagree, trust the code and fix the map in the same change.
