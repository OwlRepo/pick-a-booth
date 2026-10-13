"""CI TDD gate for pull requests. Rules: docs/ai/testing-strategy.md "Strict TDD".
Exit 0 = pass, 1 = TDD violation, 2 = could not evaluate (git/timeout/usage)."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from tdd_lib import RUNNABLE_KINDS, TestName, check_names, classify_changes, extract_test_names, judge_red, parse_waivers
from tdd_runner import RunResult, TestRunTimeout, run_test_files

# A PR whose head is `main` syncs upstream photobooth-app code; its tests are not ours to RED.
PROMOTION_REFS = {"main"}


class GateError(Exception):
    pass


def git(*args: str, check: bool = True) -> str:
    res = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and res.returncode != 0:
        raise GateError(f"git {' '.join(args)} failed: {(res.stderr or res.stdout).strip()}")
    return res.stdout if res.returncode == 0 else ""


def changed_entries(merge_base: str, head: str) -> list[dict[str, str]]:
    entries = []
    for line in git("diff", "--name-status", "-M", merge_base, head).splitlines():
        parts = line.split("\t")
        entries.append({"status": parts[0], "path": parts[-1]})
    return entries


def collect_names(
    merge_base: str, head: str, entries: list[dict[str, str]], test_paths: list[str]
) -> tuple[list[tuple[str, TestName]], list[tuple[str, list[TestName]]]]:
    status_of = {e["path"]: e["status"] for e in entries}
    added: list[tuple[str, TestName]] = []
    new_files: list[tuple[str, list[TestName]]] = []
    for file in test_paths:
        names = extract_test_names(git("show", f"{head}:{file}"))
        if status_of.get(file) == "A":
            new_files.append((file, names))
            added.extend((file, t) for t in names)
        else:
            before = {t.name for t in extract_test_names(git("show", f"{merge_base}:{file}", check=False))}
            added.extend((file, t) for t in names if t.name not in before)
    return added, new_files


def run_against_base(merge_base: str, head: str, groups: dict[str, list[str]], timeout_s: float) -> RunResult:
    """Runs the PR's test files against the merge-base source in a throwaway worktree."""
    tmp = Path(tempfile.mkdtemp(prefix="tdd-gate-base-"))
    try:
        git("worktree", "add", "--detach", "--quiet", str(tmp), merge_base)
        for file in (f for k in RUNNABLE_KINDS for f in groups[k]):
            target = tmp / file
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(git("show", f"{head}:{file}"))
        try:
            return run_test_files(tmp, groups, timeout_s)
        except TestRunTimeout as err:
            raise GateError(f"{err} against the base") from err
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", str(tmp)], capture_output=True)
        shutil.rmtree(tmp, ignore_errors=True)
        subprocess.run(["git", "worktree", "prune"], capture_output=True)


def main() -> int:
    base = os.environ.get("TDD_GATE_BASE")
    if not base:
        raise GateError("TDD_GATE_BASE is missing (e.g. origin/main)")
    head_ref = os.environ.get("TDD_GATE_HEAD_REF", "")
    if head_ref in PROMOTION_REFS:
        print(f"skip: PR from {head_ref} (upstream sync); its code is not authored on this branch")
        return 0
    head = os.environ.get("TDD_GATE_HEAD") or "HEAD"
    timeout_s = float(os.environ.get("TDD_GATE_TIMEOUT_S") or 300)

    merge_base = git("merge-base", base, head).strip()
    entries = changed_entries(merge_base, head)
    groups = classify_changes(entries)
    waivers = parse_waivers(os.environ.get("PR_BODY"))
    violations: list[str] = []
    notes: list[str] = []

    runnable = [f for k in RUNNABLE_KINDS for f in groups[k]]
    tdd_waiver = waivers["tdd"]

    if groups["logic"] and not runnable:
        if tdd_waiver:
            notes.append(f"TDD-Waiver: {tdd_waiver}")
        else:
            violations.append(f"logic changed without any test: {', '.join(groups['logic'])}")
    if groups["migrations"] and not groups["migration_tests"]:
        if waivers["migration"]:
            notes.append(f"Migration-Waiver: {waivers['migration']}")
        else:
            violations.append(f"migration without a migration test (test_*migration*.py): {', '.join(groups['migrations'])}")

    violations.extend(check_names(*collect_names(merge_base, head, entries, runnable)))

    refactor = bool(tdd_waiver and re.match(r"refactor\b", tdd_waiver, re.IGNORECASE))
    if groups["logic"] and runnable:
        if tdd_waiver and not refactor:
            notes.append(f"TDD-Waiver: {tdd_waiver} (RED proof skipped)")
        else:
            run = run_against_base(merge_base, head, groups, timeout_s)
            if refactor:
                notes.append(f"TDD-Waiver: {tdd_waiver} (tests must pass against the base)")
                if run.any_failure:
                    failing = ", ".join([*run.test_level, *run.file_level])
                    violations.append(f"refactor: the tests fail against the old code, so behaviour changed: {failing}")
            else:
                red, reason = judge_red(run.test_level, run.file_level)
                if red:
                    notes.append(f"RED against base: {reason}")
                else:
                    violations.append(f"RED: {reason}")

    report(violations, notes)
    return 1 if violations else 0


def report(violations: list[str], notes: list[str]) -> None:
    for n in notes:
        print(f"note: {n}")
    for v in violations:
        print(f"TDD: {v}")
    if not violations:
        print("ok: TDD gate passed")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary:
        return
    lines = ["## TDD gate", ""]
    if not violations:
        lines.append("Passed.")
    lines.extend(f"- FAIL: {v}" for v in violations)
    lines.extend(f"- {n}" for n in notes)
    with open(summary, "a") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GateError as err:
        print(f"tdd-gate: {err}", file=sys.stderr)
        sys.exit(2)
