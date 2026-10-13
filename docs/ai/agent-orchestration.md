# Agent Orchestration

> Purpose: how `project-manager` dispatches the implementer personas for one feature, what each may touch, and the module knowledge injected into that dispatch.
> Load rule: read when a spec crosses ownership areas, before dispatching anyone.
> Source of truth: `agents/src/*.agent.toml` + `agents/src/prompts/*.md` (generated into `.claude/agents/*.md` via `uv run poe agents:generate`; Claude Code is the only agent runtime). If this doc and a generated agent file disagree, the generated file wins — fix this doc in the same change. `scripts/tests/test_generate_agent_defs.py` fails when an ownership glob below is missing from this doc.

## Runtime Model Matrix

All nine personas use the Claude `sonnet` alias. Model selection lives only in `agents/src/*.agent.toml`; regenerate with `uv run poe agents:generate` after changing it.

## File Ownership Rule (implementers in the same worktree)

For one feature dispatch, `fastapi-backend-dev` and `web-frontend-dev` work in the SAME worktree. To prevent concurrent writes to the same file:

1. **web-frontend-dev** may create or edit: `src/web/frontend/**`, `src/web/sharepage/**`, `src/web/shareondemand/**`. It consumes the backend only through the locked `/api` contract and never edits Python.
2. **fastapi-backend-dev** may create or edit: `src/photobooth/routers/**`, `src/photobooth/services/**`, `src/photobooth/plugins/**`, `src/photobooth/utils/**`, and `src/photobooth/database/schemas.py`. It NEVER touches the SQLAlchemy models or Alembic migrations.
3. **db-architect** owns `src/photobooth/database/models.py` and `src/photobooth/database/alembic/versions/*.py`. It runs ALONE, sequentially, before the contract is locked — never as part of the concurrent pair.
4. **Shared/boundary files:** the Pydantic request/response models consumed by both sides are owned by fastapi-backend-dev, since it owns the locked contract. web-frontend-dev never edits them; a shape change goes through `project-manager`, which re-issues the contract lock.
5. Files outside every glob (`src/photobooth/appconfig.py`, `src/photobooth/container.py`, `src/photobooth/application.py`, `src/photobooth/__init__.py`, `src/photobooth/__main__.py`, `pyproject.toml`, CI) are assigned to exactly one owner by `project-manager` at contract lock — never a mid-flight ownership exception.
6. If a spec would require two agents to touch the same file, the spec is defective: split it or reassign that file before dispatch. The project manager catches this during contract lock, not after both agents report done.

## Module Briefings

Keyed by the layer the spec's file paths touch. `project-manager` copies the matching section(s) verbatim into every implementer dispatch prompt. Content is sourced from `docs/ai/module-ownership-map.md` — do not invent new facts here.

### routers
`src/photobooth/routers/api/` is unauthenticated by design (kiosk UI); `src/photobooth/routers/api_admin/` sits behind the JWT dependency. Anything that changes config, deletes data or runs system commands belongs in `api_admin`. Routers stay thin and call services through `container`.

### services
`BaseService` subclasses wired in `src/photobooth/container.py`; start/stop order is definition order. Background threads must stop on `container.stop()`. Config comes from `appconfig` groups, never ad-hoc env reads.

### backends
Camera backends in `src/photobooth/services/backends/`, loaded by backend type. Hardware calls need timeouts; tests mock the device or self-skip. Deep by default.

### plugins
pluggy hookspecs in `src/photobooth/plugins/__init__.py`; bundled plugins registered in `pyproject.toml` entry points; user plugins load from `./plugins/`. Changing a hookspec is a contract change for third-party plugins — Deep by default.

### database
SQLite via SQLAlchemy 2; Alembic runs unattended at every app start on every installed photobooth. Additive, reversible migrations only (`docs/ai/planning.md` "Migrations"). Deep by default.

### web
`src/web/frontend/` is a vendored build of photobooth-frontend; replace it from a build, never hand-edit. `src/web/shareondemand/api.php` is deployed by users on their own web hosting.

If a spec touches an area not listed here, do not invent a briefing — escalate to the repo owner instead.

## Dispatch Round Structure

The contract-first flow (`agents/src/prompts/project-manager.md` "Contract-First Dispatch") runs as separate dispatch rounds; agents inside one round run in parallel:

- **Round 0** (only if models or migrations change): spawn `db-architect` alone. Wait for completion before Round 1.
- **Round 1:** the orchestrator (top-level session, following the `project-manager` persona) locks the contract itself — not a subagent spawn.
- **Round 1b — RED:** spawn `test-engineer` alone with the locked contract and the plan's Test Matrix. It writes every required test (`test_error_` > `test_edge_` > `test_regression_` > `test_happy_`), runs `uv run poe tdd:red`, commits the tests as `test(<scope>): ...`, and reports the failing output. Round 2 does not start until that RED is recorded (`docs/ai/testing-strategy.md` "Strict TDD").
- **Round 2:** spawn `fastapi-backend-dev` and `web-frontend-dev` together in one call (only the ones the spec needs).
- **Round 3:** the orchestrator verifies the output against the locked contract and acceptance criteria itself — not a subagent spawn.
- **Round 4:** spawn `test-engineer`, `code-reviewer`, `security-auditor` together in one call — always, on every feature. Add `accessibility-auditor` when the diff touches user-visible web assets; add `ui-ux-designer` when it touches user-facing copy or UX. This is the ONE canonical QA fan-out roster. The `/qa` skill is invoked directly, not as a persona.

Never collapse Round 0/1, Round 2, or Round 3 into one dispatch. This structure is mandatory whenever a spec crosses ownership areas ("Automatic agent routing default" in `AGENTS.md`).

## Global Policy block

`scripts/generate_agent_defs.py` appends a shared `GLOBAL_POLICY` block to every persona: caveman ultra replies, the persona line, graphify-first discovery, AGENTS.md Canonical Task Flow with the `docs/ai/planning.md` / `docs/ai/execution.md` phase loads, Strict TDD, the `.ai-engineering` reads, and the migration rule pointer. Edit the policy in the generator, never in the generated files, then run `uv run poe agents:generate`.
