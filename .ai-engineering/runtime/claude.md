# Claude Code Runtime Rules

Claude Code follows the same operating model.

- Loads `CLAUDE.md` (which imports `AGENTS.md`) automatically.
- Enforced locally by the PreToolUse hook in `.claude/settings.json` (`scripts/hooks/tdd_red_guard.py`).
- Personas: `.claude/agents/*.md`, generated from `agents/src/` — never hand-edited.

Use for analysis, planning, implementation, and review. All outputs follow the agent contracts in `agents/`.
