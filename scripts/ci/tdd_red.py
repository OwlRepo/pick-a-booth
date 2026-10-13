"""`uv run poe tdd:red`: run this branch's changed tests BEFORE implementing and record
that they failed. The Claude PreToolUse guard reads the marker; see
docs/ai/testing-strategy.md "Strict TDD".
Exit 0 = RED recorded, 1 = not RED (nothing written), 2 = usage/git error."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

from tdd_lib import RUNNABLE_KINDS, classify_changes, judge_red
from tdd_runner import TestRunTimeout, run_test_files

MARKER_FILE = "tdd-red.json"


class UsageError(Exception):
    pass


def git(cwd: str | Path, *args: str) -> str:
    res = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)
    if res.returncode != 0:
        raise UsageError(f"git {' '.join(args)} failed: {(res.stderr or res.stdout).strip()}")
    return res.stdout.strip()


def parse_args(argv: list[str]) -> str | None:
    if "--waiver" not in argv:
        return None
    idx = argv.index("--waiver")
    reason = argv[idx + 1].strip() if idx + 1 < len(argv) else ""
    if not reason or reason.startswith("--"):
        raise UsageError('--waiver needs a reason: uv run poe tdd:red --waiver "<reason>"')
    return reason


def changed_entries(root: str, merge_base: str) -> list[dict[str, str]]:
    """Committed + staged + unstaged changes against the merge-base, plus untracked files:
    RED happens before the tests are necessarily committed."""
    entries = []
    for line in git(root, "diff", "--name-status", "-M", merge_base).splitlines():
        parts = line.split("\t")
        entries.append({"status": parts[0], "path": parts[-1]})
    for path in git(root, "ls-files", "--others", "--exclude-standard").splitlines():
        entries.append({"status": "A", "path": path})
    return entries


def main(argv: list[str]) -> int:
    waiver = parse_args(argv)
    root = git(".", "rev-parse", "--show-toplevel")
    marker = Path(git(root, "rev-parse", "--absolute-git-dir"), MARKER_FILE)
    branch = git(root, "rev-parse", "--abbrev-ref", "HEAD")
    at = datetime.now(UTC).isoformat()

    if waiver:
        marker.write_text(json.dumps({"branch": branch, "waiver": waiver, "at": at}, indent=2) + "\n")
        print(f'tdd:red: waiver recorded for {branch}: {waiver}. Copy it into the PR body as "TDD-Waiver: {waiver}".')
        return 0

    base = os.environ.get("TDD_RED_BASE") or "origin/main"
    merge_base = git(root, "merge-base", base, "HEAD")
    groups = classify_changes(changed_entries(root, merge_base))
    test_files = [f for k in RUNNABLE_KINDS for f in groups[k]]
    if not test_files:
        print("tdd:red: no new or changed tests on this branch. Write the test_error_ and test_edge_ cases first.", file=sys.stderr)
        return 1

    run = run_test_files(root, groups, float(os.environ.get("TDD_RED_TIMEOUT_S") or 300))
    red, reason = judge_red(run.test_level, run.file_level)
    if not red:
        print(f"tdd:red: no RED. {reason}", file=sys.stderr)
        return 1
    record = {
        "branch": branch,
        "test_files": test_files,
        "failed_names": run.test_level,
        "load_failures": run.file_level,
        "at": at,
    }
    marker.write_text(json.dumps(record, indent=2) + "\n")
    print(f"tdd:red: RED recorded for {branch} ({reason}). You may implement now.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except (UsageError, TestRunTimeout) as err:
        print(f"tdd:red: {err}", file=sys.stderr)
        sys.exit(2)
