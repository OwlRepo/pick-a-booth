"""Claude Code PreToolUse hook: blocks writes to src/photobooth logic until
`uv run poe tdd:red` has recorded failing tests for the current branch.
Exit 2 = block (stderr is shown to the agent), 0 = allow.
Rules: docs/ai/testing-strategy.md "Strict TDD". Stdlib only: runs with any python3."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ci"))

from tdd_lib import find_bash_write_targets, is_guarded_source, judge_red  # noqa: E402

EDIT_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}

HOW_TO = (
    "Write the tests first (test_error_ > test_edge_ > test_regression_ > test_happy_), run `uv run poe tdd:red` "
    'and see them fail. If it truly does not apply: uv run poe tdd:red --waiver "<reason>".'
)


def git(cwd: str | Path, *args: str) -> str | None:
    res = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)
    return res.stdout.strip() if res.returncode == 0 else None


def resolve_target(target: str, cwd: str) -> tuple[Path, Path] | None:
    """The target may not exist yet (Write of a new file); resolve through the nearest
    existing ancestor so symlinked temp dirs (/var vs /private/var) still match git."""
    abs_path = Path(cwd, os.path.expanduser(target))
    directory = abs_path.parent
    rest = [abs_path.name]
    while not directory.exists():
        if directory.parent == directory:
            return None
        rest.insert(0, directory.name)
        directory = directory.parent
    real = directory.resolve()
    return real, real.joinpath(*rest)


def marker_problem(toplevel: str) -> str | None:
    git_dir = git(toplevel, "rev-parse", "--absolute-git-dir") or ""
    branch = git(toplevel, "rev-parse", "--abbrev-ref", "HEAD")
    file = Path(git_dir, "tdd-red.json")
    if not file.exists():
        return f"RED first: no failing-test marker for branch {branch}."
    try:
        marker = json.loads(file.read_text())
        if not isinstance(marker, dict):
            raise ValueError
    except ValueError:
        return f"The marker {file} is corrupt; run `uv run poe tdd:red` again."
    if marker.get("branch") != branch:
        return f"RED first: the marker belongs to branch {marker.get('branch')}, not {branch}."
    waiver = marker.get("waiver")
    if isinstance(waiver, str) and waiver.strip():
        return None
    red, reason = judge_red(marker.get("failed_names") or [], marker.get("load_failures") or [])
    return None if red else f"RED first: the marker is not a valid RED ({reason})."


def main(raw: str) -> int:
    try:
        payload = json.loads(raw)
    except ValueError:
        sys.stderr.write("tdd-red-guard: hook input is not JSON; allowing.\n")
        return 0
    cwd = payload.get("cwd") or os.getcwd()
    tool_input = payload.get("tool_input") or {}
    targets: list[str] = []
    if payload.get("tool_name") in EDIT_TOOLS:
        file = tool_input.get("file_path") or tool_input.get("notebook_path")
        if file:
            targets = [file]
    elif payload.get("tool_name") == "Bash":
        targets = find_bash_write_targets(tool_input.get("command") or "")

    for target in targets:
        resolved = resolve_target(target, cwd)
        if not resolved:
            continue
        directory, abs_path = resolved
        toplevel = git(directory, "rev-parse", "--show-toplevel")
        if not toplevel:
            continue
        rel = os.path.relpath(abs_path, toplevel).replace(os.sep, "/")
        if not is_guarded_source(rel):
            continue
        problem = marker_problem(toplevel)
        if problem:
            sys.stderr.write(f"{problem} {rel} is src/photobooth logic. {HOW_TO}\n")
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.stdin.read()))
