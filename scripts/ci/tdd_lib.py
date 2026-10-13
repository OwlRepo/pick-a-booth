"""Shared rules for the TDD gate (CI), `uv run poe tdd:red` (local) and the Claude
PreToolUse guard. Pure functions only; the CLIs own git and process I/O.
Rules: docs/ai/testing-strategy.md "Strict TDD".
"""

from __future__ import annotations

import ast
import re
import xml.etree.ElementTree as ET
from typing import NamedTuple

PREFIXES = ("error", "edge", "regression", "happy")
RED_PREFIXES = ("error", "edge", "regression")
RUNNABLE_KINDS = ("unit", "migration_tests", "script_tests")
KINDS = ("logic", "unit", "migration_tests", "script_tests", "migrations")

PREFIX_RE = re.compile(r"^test_(error|edge|regression|happy)_")
PREFIX_HINT = "test_error_/test_edge_/test_regression_/test_happy_"

_MIGRATIONS = re.compile(r"^src/photobooth/database/alembic/versions/.+\.py$")
_MIGRATION_TESTS = re.compile(r"^src/tests/tests/(?:.+/)?test_[^/]*migration[^/]*\.py$")
_UNIT = re.compile(r"^src/tests/tests/(?:.+/)?test_[^/]*\.py$")
_SCRIPT_TESTS = re.compile(r"^scripts/(?:.+/)?test_[^/]*\.py$")


class TestName(NamedTuple):
    name: str
    prefix: str | None


def is_guarded_source(rel: str) -> bool:
    return re.match(r"^src/photobooth/.+\.py$", rel) is not None and not _MIGRATIONS.match(rel)


def kind_of(rel: str) -> str | None:
    if _MIGRATIONS.match(rel):
        return "migrations"
    if _MIGRATION_TESTS.match(rel):
        return "migration_tests"
    if _UNIT.match(rel):
        return "unit"
    if _SCRIPT_TESTS.match(rel):
        return "script_tests"
    if is_guarded_source(rel):
        return "logic"
    return None


def classify_changes(entries: list[dict[str, str]]) -> dict[str, list[str]]:
    """entries: [{"status": "A"|"M"|"D"|"R087"..., "path": ...}] as from `git diff --name-status`.
    Deleted files and pure renames (R100) carry no new behaviour to test."""
    groups: dict[str, list[str]] = {k: [] for k in KINDS}
    for e in entries:
        status, path = e["status"], e["path"]
        if status.startswith("D") or status == "R100":
            continue
        kind = kind_of(path)
        if kind:
            groups[kind].append(path)
    return groups


def parse_waivers(body: str | None) -> dict[str, str | None]:
    out: dict[str, str | None] = {"tdd": None, "migration": None}
    if not body:
        return out
    for m in re.finditer(r"^[ \t]*(tdd|migration)-waiver:[ \t]*(.*)$", body, re.IGNORECASE | re.MULTILINE):
        reason = m.group(2).strip()
        if reason:
            out[m.group(1).lower()] = reason
    return out


def _is_fixture(decorator: ast.expr) -> bool:
    target = decorator.func if isinstance(decorator, ast.Call) else decorator
    if isinstance(target, ast.Name):
        return target.id == "fixture"
    return isinstance(target, ast.Attribute) and target.attr == "fixture"


def _test_functions(body: list[ast.stmt]) -> list[str]:
    names: list[str] = []
    for node in body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test"):
            if not any(_is_fixture(d) for d in node.decorator_list):
                names.append(node.name)
        elif isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
            names.extend(_test_functions(node.body))
    return names


def extract_test_names(source: str | None) -> list[TestName]:
    """Test functions pytest would collect, in declaration order. Strings, comments and
    fixtures named test_* are not cases. Unparseable source yields nothing."""
    if not source:
        return []
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    out: list[TestName] = []
    for name in _test_functions(tree.body):
        m = PREFIX_RE.match(name)
        out.append(TestName(name, m.group(1) if m else None))
    return out


def check_names(added: list[tuple[str, TestName]], new_files: list[tuple[str, list[TestName]]]) -> list[str]:
    """added: names introduced by the diff (any file). new_files: full ordered names of
    files created by the diff, where declaration order is also enforced."""
    violations = [f'{file}: "{t.name}" has no {PREFIX_HINT} prefix' for file, t in added if not t.prefix]
    prefixes = {t.prefix for _, t in added}
    if "happy" in prefixes and not prefixes & {"error", "edge"}:
        violations.append("the change adds test_happy_ cases without any test_error_ or test_edge_ case")
    for path, names in new_files:
        seen_happy = False
        for t in names:
            if t.prefix == "happy":
                seen_happy = True
            elif seen_happy and t.prefix in ("error", "edge"):
                violations.append(f'{path}: "{t.name}" is declared after a test_happy_ case; error/edge cases go first')
    return violations


def parse_junit_failures(xml_text: str | None) -> tuple[list[str], list[str]]:
    """Reads pytest --junitxml. A collection failure (usually a module that does not exist
    yet) is file-level; every other failure/error is test-level."""
    test_level: list[str] = []
    file_level: list[str] = []
    if not xml_text:
        return test_level, file_level
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return test_level, file_level
    for case in root.iter("testcase"):
        name = case.get("name", "")
        failure = case.find("failure")
        error = case.find("error")
        if error is not None and (error.get("message") or "").startswith("collection failure"):
            file_level.append(name)
        elif failure is not None or error is not None:
            test_level.append(name)
    return test_level, file_level


def judge_red(test_level: list[str], file_level: list[str]) -> tuple[bool, str]:
    red_names = [n for n in test_level if (m := PREFIX_RE.match(n)) and m.group(1) in RED_PREFIXES]
    if red_names:
        return True, f"failing: {', '.join(red_names)}"
    if not test_level and file_level:
        return True, f"cannot load (module does not exist yet): {', '.join(file_level)}"
    if test_level:
        return False, (
            f"only cases without a test_error_/test_edge_/test_regression_ prefix fail ({', '.join(test_level)}); "
            "RED must start with errors and edges"
        )
    return False, "no test fails: the tests do not pin the new behaviour"


# --- Bash write detection (heuristic, not a shell parser) ---------------------------


def _shell_mask(command: str) -> tuple[str, list[bool]]:
    """Quoted contents blanked (quote chars kept) and `#` comments dropped, so
    `-m "a > src/x.py"` or `# > src/x.py` never read as redirections."""
    mask = list(command)
    comment = [False] * len(command)
    quote: str | None = None
    i = 0
    while i < len(command):
        c = command[i]
        if quote:
            if c == "\\" and quote == '"':
                mask[i] = " "
                if i + 1 < len(command):
                    i += 1
                    mask[i] = " "
            elif c == quote:
                quote = None
            else:
                mask[i] = " "
        elif c in ("'", '"'):
            quote = c
        elif c == "#" and (i == 0 or command[i - 1].isspace()):
            while i < len(command) and command[i] != "\n":
                mask[i] = " "
                comment[i] = True
                i += 1
            continue
        i += 1
    return "".join(mask), comment


class _Segment(NamedTuple):
    text: str
    mask: str
    clean: str


def _segments(command: str) -> list[_Segment]:
    mask, comment = _shell_mask(command)
    bounds: list[tuple[int, int]] = []
    start = 0
    for m in re.finditer(r"\|\||&&|;|\||\n", mask):
        bounds.append((start, m.start()))
        start = m.end()
    bounds.append((start, len(command)))
    return [_Segment(command[a:b], mask[a:b], "".join(command[i] for i in range(a, b) if not comment[i])) for a, b in bounds]


def _tokenize(segment: str) -> list[str]:
    tokens: list[str] = []
    for m in re.finditer(r"'([^']*)'|\"([^\"]*)\"|(\S+)", segment):
        g1, g2, g3 = m.groups()
        tokens.append(g1 if g1 is not None else g2 if g2 is not None else g3 or "")
    return tokens


def _is_path_arg(t: str) -> bool:
    return not t.startswith(("-", "<", ">")) and re.match(r"^\d*>", t) is None


_REDIRECT_RE = re.compile(r"(?<![0-9&<>])>{1,2}(?!&)[ \t]*")
_TARGET_RE = re.compile(r"'([^']+)'|\"([^\"]+)\"|([^\s'\"<>&;|]+)")


def find_bash_write_targets(command: str | None) -> list[str]:
    """Best-effort: the file paths a shell command would write. Reads yield nothing."""
    targets: list[str] = []
    if not command:
        return targets
    for seg in _segments(command):
        if not seg.mask.strip():
            continue
        stripped = ""
        last = 0
        for m in _REDIRECT_RE.finditer(seg.mask):
            if m.end() >= len(seg.mask):
                continue
            t = _TARGET_RE.match(seg.text, m.end())
            if not t:
                continue
            targets.append(t.group(1) or t.group(2) or t.group(3))
            stripped += seg.text[last : m.start()]
            last = t.end()
        stripped += seg.text[last:]
        first = _segments(stripped)
        without_comment = first[0].clean if first else stripped
        tokens = _tokenize(re.sub(r"<<-?\s*['\"]?\w+['\"]?", "", without_comment).strip())
        if not tokens:
            continue
        cmd, rest = tokens[0], tokens[1:]
        if cmd == "tee":
            targets.extend(t for t in rest if _is_path_arg(t))
        elif cmd in ("sed", "perl") and any(re.match(r"^-[a-z]*i", t) for t in rest):
            args: list[str] = []
            skip_next = False
            for t in rest:
                if skip_next:
                    skip_next = False
                    continue
                if t == "-e":
                    skip_next = True
                    continue
                if t.startswith("-") or t == "":
                    continue
                args.append(t)
            # sed: first non-flag arg is the script unless -e was used.
            files = args[1:] if cmd == "sed" and "-e" not in rest else args
            targets.extend(t for t in files if re.search(r"[./]", t))
        elif cmd in ("cp", "mv", "install", "rsync"):
            paths = [t for t in rest if _is_path_arg(t)]
            if len(paths) >= 2:
                targets.append(paths[-1])
    return [t for t in targets if t and not t.startswith("/dev/")]
