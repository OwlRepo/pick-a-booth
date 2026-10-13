"""Runs changed test files with pytest and collects --junitxml failures.
Shared by tdd_gate (against the merge-base) and tdd_red (now)."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import NamedTuple

from tdd_lib import parse_junit_failures


class TestRunTimeout(Exception):
    pass


class RunResult(NamedTuple):
    test_level: list[str]
    file_level: list[str]
    any_failure: bool


# App tests and tooling tests run in separate pytest processes: each tree has its own
# conftest.py and sys.path layout.
BATCHES = (("unit", "migration_tests"), ("script_tests",))


def _env(root: Path) -> dict[str, str]:
    # PYTHONPATH precedes site-packages, so <root>/src shadows the uv editable install
    # of `photobooth`: the gate's base worktree runs the base code, not the checkout's.
    env = {k: v for k, v in os.environ.items() if not k.startswith("PYTEST_")}
    env["PYTHONPATH"] = os.pathsep.join(p for p in (str(root / "src"), env.get("PYTHONPATH", "")) if p)
    return env


def run_test_files(root: str | Path, groups: dict[str, list[str]], timeout_s: float) -> RunResult:
    root = Path(root)
    test_level: list[str] = []
    file_level: list[str] = []
    any_failure = False
    for kinds in BATCHES:
        files = [f for k in kinds for f in groups.get(k, [])]
        if not files:
            continue
        with tempfile.TemporaryDirectory(prefix="tdd-run-") as tmp:
            report = Path(tmp, "report.xml")
            cmd = [
                sys.executable,
                "-m",
                "pytest",
                "-q",
                "-p",
                "no:cacheprovider",
                "-o",
                "log_cli=false",
                "--continue-on-collection-errors",
                f"--basetemp={Path(tmp, 'basetemp')}",
                f"--junitxml={report}",
                *files,
            ]
            try:
                res = subprocess.run(cmd, cwd=root, env=_env(root), capture_output=True, text=True, timeout=timeout_s)
            except subprocess.TimeoutExpired as err:
                raise TestRunTimeout(f"timeout: the tests ({', '.join(kinds)}) did not finish in {timeout_s:g} s") from err
            # 5 = no tests collected: nothing failed.
            if res.returncode not in (0, 5):
                any_failure = True
            tl, fl = parse_junit_failures(report.read_text() if report.exists() else "")
            test_level.extend(tl)
            file_level.extend(fl)
    return RunResult(test_level, file_level, any_failure)
