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
