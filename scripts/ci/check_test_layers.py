"""Require the tests for every layer a commit touches (CI: ci.yml, job `gate`).

    uv run poe ci:layers <base-sha> [head]

Checked per commit, not per push, so code and the tests that prove it land
together - the order Strict TDD produces them in. For every non-merge commit in
base..head, each changed `src/photobooth` file needs a test changed in the
matching area of `src/tests/tests/` in that same commit (LAYERS below).

A commit that genuinely needs no new test says so with a git trailer in the
message's final trailer block (not anywhere in the body); the reason is printed:

    Test-Layers-Skip: comment-only change, no behaviour moved

Deleted files are ignored. `__init__.py` files that only hold imports, a
docstring or `__all__` are wiring, not behaviour. Rules: docs/ai/testing-strategy.md.
Exit 0 = every commit carries its tests, 1 = missing tests, 2 = usage/git error.
"""

from __future__ import annotations

import ast
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

ZERO = "0" * 40

# (changed-file pattern, test pattern that must also change, where to look). First match wins.
LAYERS: list[tuple[str, str, str]] = [
    (
        r"^src/photobooth/database/alembic/versions/.+\.py$",
        r"^src/tests/tests/(?:.+/)?test_[^/]*migration[^/]*\.py$",
        "a src/tests/tests/**/test_*migration*.py",
    ),
    (r"^src/photobooth/routers/api/.+\.py$", r"^src/tests/tests/router/api/test_[^/]+\.py$", "src/tests/tests/router/api/"),
    (
        r"^src/photobooth/routers/(?:api_admin/.+|auth_dependencies_bearer)\.py$",
        r"^src/tests/tests/router/(?:api_admin/test_[^/]+|test_authentication)\.py$",
        "src/tests/tests/router/api_admin/ or router/test_authentication.py",
    ),
    (r"^src/photobooth/routers/[^/]+\.py$", r"^src/tests/tests/router/(?:.+/)?test_[^/]+\.py$", "src/tests/tests/router/"),
    (r"^src/photobooth/services/backends/.+\.py$", r"^src/tests/tests/backends/test_[^/]+\.py$", "src/tests/tests/backends/"),
    (
        r"^src/photobooth/services/(?:mediaprocessing|processor)/.+\.py$",
        r"^src/tests/tests/(?:mediaprocessing|services)/test_[^/]+\.py$",
        "src/tests/tests/mediaprocessing/ or services/",
    ),
    (r"^src/photobooth/services/.+\.py$", r"^src/tests/tests/services/test_[^/]+\.py$", "src/tests/tests/services/"),
    (r"^src/photobooth/plugins/.+\.py$", r"^src/tests/tests/plugins/test_[^/]+\.py$", "src/tests/tests/plugins/"),
    (r"^src/photobooth/utils/.+\.py$", r"^src/tests/tests/utils/test_[^/]+\.py$", "src/tests/tests/utils/"),
    (r"^src/photobooth/.+\.py$", r"^src/tests/tests/(?:.+/)?test_[^/]*\.py$", "src/tests/tests/"),
]

Reader = Callable[[str], str]


class UsageError(Exception):
    pass


def git(*args: str, check: bool = True) -> str:
    res = subprocess.run(["git", *args], capture_output=True, text=True)
    if res.returncode != 0:
        if check:
            raise UsageError(f"git {' '.join(args)} failed: {(res.stderr or res.stdout).strip()}")
        return ""
    return res.stdout.strip()


def _working_tree(path: str) -> str:
    file = Path(path)
    return file.read_text() if file.exists() else ""


def _is_wiring_only(source: str) -> bool:
    try:
        body = ast.parse(source).body
    except SyntaxError:
        return False
    for node in body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            continue
        if isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) and t.id == "__all__" for t in node.targets):
            continue
        return False
    return True


def problems_for(files: list[str], read: Reader = _working_tree) -> list[str]:
    """Missing-test messages for one commit's changed files."""
    out = []
    for file in files:
        if file.endswith("/__init__.py") and _is_wiring_only(read(file)):
            continue
        for pattern, test_pattern, where in LAYERS:
            if re.match(pattern, file):
                if not any(re.match(test_pattern, f) for f in files):
                    out.append(f"  {file} changed, but no test in {where} did")
                break
    return out


def resolve_base(base: str, head: str) -> str:
    if base and base != ZERO and git("rev-parse", "--verify", "--quiet", f"{base}^{{commit}}", check=False):
        return base
    # A new branch's first push has no `before`; compare with main instead.
    return git("merge-base", head, "origin/main", check=False)


def main(argv: list[str]) -> int:
    head = argv[1] if len(argv) > 1 else "HEAD"
    base = resolve_base(argv[0] if argv else "", head)
    if not base:
        print("check-test-layers: no base commit to compare against - nothing checked", file=sys.stderr)
        return 0

    failures = 0
    for commit in git("rev-list", "--no-merges", "--reverse", f"{base}..{head}").split():
        files = git("diff-tree", "--no-commit-id", "--name-only", "-r", "--diff-filter=ACMR", commit).splitlines()
        problems = problems_for(files, lambda path, c=commit: git("show", f"{c}:{path}", check=False))
        if not problems:
            continue
        title = f"{git('rev-parse', '--short', commit)} {git('log', '-1', '--format=%s', commit)}"
        # Only a real trailer counts: a line mid-body is prose, not a decision.
        reason = git("log", "-1", "--format=%(trailers:key=Test-Layers-Skip,valueonly)", commit).partition("\n")[0].strip()
        if reason:
            print(f"skipped {title}\n  reason: {reason}")
        else:
            print(f"MISSING TESTS in {title}")
            failures += 1
        print("\n".join(problems))

    if failures:
        print(
            f"\n{failures} commit(s) change code without the tests for the layers they touch.\n"
            "Add the tests to the same commit, or state why none are needed with a\n"
            "'Test-Layers-Skip: <reason>' trailer in the message's final paragraph.\n"
            "See docs/ai/testing-strategy.md."
        )
        return 1
    print(f"check-test-layers: every commit in {git('rev-parse', '--short', base)}..{git('rev-parse', '--short', head)} carries its tests")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except UsageError as err:
        print(f"check-test-layers: {err}", file=sys.stderr)
        sys.exit(2)
