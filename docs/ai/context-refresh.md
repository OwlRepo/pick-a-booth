# Context Refresh

> Purpose: the procedure for re-verifying and updating the `docs/ai/*` maps against real code.
> Load rule: run when maps look stale, after a large merge or upstream sync, or when explicitly asked to refresh context.
> Source of truth: this is a MAP of the refresh process. Real code, tests, schemas, and routes are the truth. If a map conflicts with code, code wins.

Unknowns are written as `TODO: Fill after repository analysis. Do not treat as verified.` Inferences are marked `(inferred, please correct if wrong)`.

## Scope

- Read-only for source. A refresh reads code; it does NOT change implementation.
- Only the context docs (`AGENTS.md`, `CLAUDE.md`, `docs/ai/*`, `.ai-engineering/memory/*`) may be edited, and only when a refresh is requested.
- No feature work, no fixes, no refactors during a refresh.

## Files To Refresh

- `CLAUDE.md` (project facts) and `AGENTS.md` (workflow core)
- `docs/ai/entry-point.md`
- `docs/ai/task-router.md`
- `docs/ai/planning.md`
- `docs/ai/plan-template.md`
- `docs/ai/execution.md`
- `docs/ai/handoff.md`
- `docs/ai/pr-evidence.md`
- `docs/ai/dev-environment.md`
- `docs/ai/agent-orchestration.md`
- `docs/ai/autonomous-engineering.md`
- `docs/ai/operating-contract.md` (compatibility pointer only)
- `docs/ai/architecture-manifest.md`
- `docs/ai/module-ownership-map.md`
- `docs/ai/contracts/api-contracts.md`
- `docs/ai/contracts/db-contracts.md`
- `docs/ai/testing-strategy.md`
- `docs/ai/risk-register.md`
- `docs/ai/file-index/repository-map.md`
- `docs/ai/prompts/bugfix-rca.md`
- `docs/ai/prompts/bugfix-plan.md`
- `docs/ai/prompts/feature-plan.md`
- `docs/ai/prompts/refactor-plan.md`
- `docs/ai/context-refresh.md`
- `.ai-engineering/memory/lessons-learned.md`

## Source Verification Rules

Verify every fact against the real artifact:

- Symbols and line numbers → the actual source file.
- API surface → `src/photobooth/routers/` (or the generated `/api/openapi.json` of a running app).
- Schema → `src/photobooth/database/models.py` and `src/photobooth/database/alembic/versions/`.
- Test claims → `pyproject.toml` poe tasks and `src/tests/tests/` (re-run `uv run poe test` if needed).
- Stack and versions → `pyproject.toml` and `uv.lock`.

## Drift Markers

- `CONTEXT DRIFT` — for the general maps (AGENTS.md, CLAUDE.md, planning/execution/handoff, entry-point, manifest, ownership map, repository-map, prompts, and the operating-contract pointer).
- `CONTRACT DRIFT` — for `contracts/api-contracts.md`, `contracts/db-contracts.md`, `testing-strategy.md`, and `risk-register.md`.

When drift is found: report the stale file and section, use the code as truth for the current task, and do NOT edit the context docs unless the refresh (or the user) asked you to.

## Refresh Steps

1. Diff the tree since the last refresh (new/moved/removed files, new routes, new migrations, upstream merges).
2. For each doc, re-verify its facts against source per the rules above.
3. Mark each drifted section with the right drift marker and correct it.
4. Re-check every line number in `repository-map.md`.
5. Re-run `uv run poe test` and `uv run poe test:scripts` (doc links) and record the result.
6. Record any genuinely new pattern in `.ai-engineering/memory/lessons-learned.md`.

## Output Summary

End a refresh with: files reviewed, sections corrected, drift markers raised (with file + section), any TODO that is still unresolved, and the current test-suite status.
