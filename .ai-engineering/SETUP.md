# Autonomous Engineering Layer — Setup

Goal: a repository-local AI engineering operating layer for pick-a-booth. This
layer defines behavior; Claude Code or Codex executes it. Project facts live in
`CLAUDE.md`; the always-on task flow lives in `AGENTS.md`; this folder does not
duplicate either.

Installed from the reference workflow using `AUTONOMOUS_ENGINEERING_BOOTSTRAP.md`
(reference repository, v1.0.0) as the specification for activation semantics.
The full installer output (manifest, schemas, validator, simulation cases) is
NOT installed here; see `config/autonomous-engineering.yaml` for the activation
state.

## Layout

- `agents/` — role contracts (product manager, architect, coordinator, implementer, reviewer, QA, reporter).
- `config/autonomous-engineering.yaml` — autonomy level, activation state, approvals.
- `core/` — operating model, lifecycle, state machine, safety, evidence, decisions.
- `memory/` — project memory, architecture decisions, lessons learned (append-only).
- `runtime/` — Claude Code, Codex and scheduler rules.
- `templates/` — task, plan, ADR, execution, review, QA, PR and EOD report skeletons.
- `validation/` — bootstrap check, contract tests, workflow tests, repair loop.
- `workflows/` — intake, feature, bug fix, review, release, blockers, daily cycle.

## Rules for changing this layer

1. Inspect the repository (stack, architecture, existing instructions, testing, CI) before changing anything.
2. Preserve existing project rules in `AGENTS.md` and `CLAUDE.md`.
3. Never modify application code as part of a change to this layer.
4. Report detected project information, installed workflow, configured agents, automation recommendations, and unresolved decisions.

## Post-change validation

1. Run `validation/bootstrap-check.md`, the workflow tests and the agent contract tests.
2. Run `uv run poe test:scripts`: `scripts/tests/test_doc_links.py` proves every path these docs cite exists.
3. If anything fails, follow `validation/repair-loop.md` (layer files only), then re-run.

Complete only when validation passes, no workflow conflict remains, and safety rules are intact.
