# Architecture Decision Record (append-only)

Use `templates/adr.md` for each entry. Newest last.

## ADR-0001 — AI engineering workflow ported from the reference repository (2026-10-13)

Decision: adopt the route → plan → approve → worktree → RED → build → validate → handoff flow (`AGENTS.md`), enforced by a Claude Code hook and the CI `ai-gates` workflow, with Python stdlib tooling run through poe.

Context: the repository is a public fork of photobooth-app (Python/FastAPI, uv, pytest); the reference workflow was written for a Node/Next.js app.

Alternatives: Node scripts plus a package.json (rejected: second toolchain in a Python repo); full bootstrap installer output (rejected: larger and diverges from the reference's actual runtime).

Tradeoffs: the scripts are rewrites, not copies; `verified-tree` caching and git pre-commit hooks were not ported (no persistent CI runner, no npm `prepare`).

Result: `docs/plans/ai-workflow-port.md`.

## ADR-0002 — Claude Code is the only agent runtime (2026-10-13)

Decision: drop Codex support. Personas generate only `.claude/agents/`; `uv run poe agents:lint` fails if a `.codex` directory reappears.

Context: the repo owner's instruction — the team works with Claude only.

Tradeoffs: dispatch rounds stay as explicit boundaries (`docs/ai/agent-orchestration.md` "Dispatch Round Structure") even though Claude Code could run them inside one session, so RED is always recorded before implementers start.

Result: `scripts/generate_agent_defs.py`, `agents/src/*.agent.toml`.

## ADR-0003 — Desktop app; our own CI, no server deploy (2026-10-13)

Decision: pick-a-booth becomes our own desktop app built on the fork. All CI and GitHub config inherited from upstream photobooth-app (lint, test matrix, benchmarks, PyPI publish, dependabot, issue templates, funding, PR template) is replaced by one workflow, `.github/workflows/ci.yml`, modeled on optra's quality gate: per-commit test-layer guard, TDD gate, script tests, agent lint, type-check, lint, unit tests, then a Windows/macOS/Linux test matrix.

Context: the repo owner's instruction; optra's CI is the house pattern, minus its VPS deploy and backup jobs because a desktop app has no server.

Alternatives: keep upstream CI and add ours (rejected: two gates, upstream-only jobs inert on the fork); host on a VPS (rejected for now: the app drives local cameras/GPIO, a VPS cannot reach them).

Tradeoffs: upstream merges now conflict in `.github/`; dependency bumps are manual without dependabot; desktop packaging and releases are still to be built.

Result: `docs/plans/desktop-ci.md`, `.github/workflows/ci.yml`, `scripts/ci/check_test_layers.py`.
