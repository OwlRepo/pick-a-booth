# Codex Runtime Rules

Codex loads `AGENTS.md` natively but not `CLAUDE.md`: read `CLAUDE.md` before any code work.

Codex should:

- read repository instructions first
- inspect before editing
- use the assigned persona (`.codex/agents/*.toml`, generated from `agents/src/`)
- run `uv run poe tdd:red` itself: Codex has no project hook, CI `tdd:gate` is the backstop
- keep tasks isolated (one worktree per task)
- provide structured evidence
- create focused changes
