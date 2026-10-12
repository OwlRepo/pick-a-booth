"""Persona single source of truth: agents/src/<name>.agent.toml + agents/src/prompts/<name>.md
generate .claude/agents/<prefix>-<name>.md (Claude Code) and .codex/agents/<name>.toml (Codex).
Never hand-edit the generated files. `--check` fails on drift (CI: ai-gates.yml)."""

from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

# Appended to every persona on both runtimes so repo-wide policy cannot drift per
# persona. Must never contain three double quotes in a row (ends the Codex TOML string).
GLOBAL_POLICY = """
# Global Policy (applies to every persona)

- Respond in caveman ultra per ~/.agents/skills/caveman/SKILL.md. Code, tests, commit messages, and PR text stay normal.
- Persona: Senior Staff Full Stack AI Engineer specialising in Python 3.11+ FastAPI services, SQLAlchemy/Alembic on SQLite, and camera/GPIO hardware on Raspberry Pi and Linux, shipped with uv and Docker. Simplest durable solution; never a band-aid.
- Find things with Graphify (/graphify query|path|explain); grep only when Graphify cannot answer, and say which query failed.
- Follow AGENTS.md (Canonical Task Flow) strictly; read docs/ai/planning.md before any planning and docs/ai/execution.md before any code.
- Strict TDD: tests first and seen failing with `uv run poe tdd:red`, cases ordered test_error_ > test_edge_ > test_regression_ > test_happy_ (docs/ai/testing-strategy.md "Strict TDD").
- Read .ai-engineering/core/operating-model.md first; read the relevant .ai-engineering/agents/ definition before acting; follow .ai-engineering/core/task-lifecycle.md, .ai-engineering/core/safety.md, .ai-engineering/core/evidence-policy.md, applicable .ai-engineering/workflows/, and .ai-engineering/config/autonomous-engineering.yaml.
- Migrations: additive and backward compatible; destructive operations only with explicit repo-owner approval — canonical rule in docs/ai/planning.md "Migrations".
"""

Persona = dict[str, Any]


def _escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def claude_file(root: Path, persona: Persona) -> Path:
    return root / ".claude" / "agents" / f"{persona['file_prefix']}-{persona['name']}.md"


def codex_file(root: Path, persona: Persona) -> Path:
    return root / ".codex" / "agents" / f"{persona['name']}.toml"


def render_claude_markdown(persona: Persona) -> str:
    frontmatter = "\n".join(
        [
            "---",
            f"name: {persona['name']}",
            f'description: "{_escape(persona["description"])}"',
            f"tools: {', '.join(persona['claude']['tools'])}",
            f"model: {persona['claude']['model']}",
            "---",
            "",
            "",
        ]
    )
    return frontmatter + persona["system_prompt"] + GLOBAL_POLICY


def render_codex_toml(persona: Persona) -> str:
    if '"""' in persona["system_prompt"]:
        raise ValueError(f"{persona['name']}: system_prompt contains three double quotes in a row, which ends the TOML string — rephrase it.")
    codex = persona["codex"]
    lines = [f'name = "{_escape(persona["name"])}"', f'description = "{_escape(persona["description"])}"']
    for key in ("model", "model_reasoning_effort", "sandbox_mode"):
        if codex.get(key):
            lines.append(f'{key} = "{_escape(codex[key])}"')
    if codex.get("mcp_servers"):
        lines.append("mcp_servers = [" + ", ".join(f'"{_escape(s)}"' for s in codex["mcp_servers"]) + "]")
    lines.extend(["", 'developer_instructions = """'])
    # Basic multi-line string: backslashes are escapes in TOML, so double them.
    body = (persona["system_prompt"] + GLOBAL_POLICY).replace("\\", "\\\\")
    return "\n".join(lines) + body + '"""\n'


def load_personas(src_dir: Path) -> list[Persona]:
    personas = []
    for file in sorted(src_dir.glob("*.agent.toml")):
        persona: Persona = tomllib.loads(file.read_text())
        persona.setdefault("owned_globs", [])
        persona["system_prompt"] = (src_dir / "prompts" / f"{persona['name']}.md").read_text().rstrip() + "\n"
        personas.append(persona)
    return personas


def find_duplicate_owned_globs(personas: list[Persona]) -> list[str]:
    """Exact-string collision only: catches the copy-paste-glob mistake without a glob matcher."""
    seen: dict[str, str] = {}
    failures = []
    for persona in personas:
        for glob in persona["owned_globs"]:
            owner = seen.get(glob)
            if owner and owner != persona["name"]:
                failures.append(f'owned_globs conflict: "{glob}" claimed by both "{owner}" and "{persona["name"]}"')
            else:
                seen[glob] = persona["name"]
    return failures


def compute_targets(root: Path, personas: list[Persona]) -> dict[Path, str]:
    targets: dict[Path, str] = {}
    for persona in personas:
        targets[claude_file(root, persona)] = render_claude_markdown(persona)
        targets[codex_file(root, persona)] = render_codex_toml(persona)
    return targets


def generate(root: Path) -> int:
    personas = load_personas(root / "agents" / "src")
    for path, content in compute_targets(root, personas).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        print(f"Wrote {path.relative_to(root)}")
    print(f"Generated {len(personas)} Claude + {len(personas)} Codex agent definitions from agents/src/*.agent.toml.")
    return 0


def check(root: Path) -> int:
    personas = load_personas(root / "agents" / "src")
    targets = compute_targets(root, personas)
    failures = []
    for path, expected in targets.items():
        rel = path.relative_to(root)
        if not path.exists():
            failures.append(f"{rel}: file does not exist — run 'uv run poe agents:generate' to generate it")
        elif path.read_text() != expected:
            failures.append(f"{rel}: generated content does not match agents/src — run 'uv run poe agents:generate' to regenerate")
    existing = [*(root / ".claude" / "agents").glob("*.md"), *(root / ".codex" / "agents").glob("*.toml")]
    for path in sorted(existing):
        if path not in targets:
            failures.append(f"{path.relative_to(root)}: no matching agents/src/*.agent.toml source — delete this file or add its source")
    failures.extend(find_duplicate_owned_globs(personas))
    if failures:
        print("\n".join(f"- {f}" for f in failures), file=sys.stderr)
        return 1
    print(f"Agent definitions lint passed ({len(personas)} personas, {len(personas) * 2} generated files).")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files drift from agents/src")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (tests use a scratch repo)")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    return check(root) if args.check else generate(root)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
