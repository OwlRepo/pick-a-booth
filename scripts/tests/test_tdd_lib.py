# Pure rules shared by tdd_red, tdd_gate and the Claude hook.
# Order: error > edge > regression > happy (docs/ai/testing-strategy.md "Strict TDD").
from tdd_lib import (
    check_names,
    classify_changes,
    extract_test_names,
    find_bash_write_targets,
    is_guarded_source,
    judge_red,
    parse_junit_failures,
    parse_waivers,
)


def entry(status: str, path: str) -> dict[str, str]:
    return {"status": status, "path": path}


def added(file: str, source: str):
    return [(file, t) for t in extract_test_names(source)]


def test_error_name_without_prefix_is_a_violation():
    violations = check_names(added("src/tests/tests/test_a.py", "def test_something():\n    pass\n"), [])
    assert any("test_something" in v and "prefix" in v for v in violations)


def test_error_happy_without_error_or_edge_is_a_violation():
    violations = check_names(added("src/tests/tests/test_a.py", "def test_happy_works():\n    pass\n"), [])
    assert any("happy" in v and "error" in v for v in violations)


def test_error_edge_declared_after_happy_in_new_file_is_a_violation():
    src = "def test_error_a():\n    pass\n\ndef test_happy_b():\n    pass\n\ndef test_edge_c():\n    pass\n"
    names = extract_test_names(src)
    violations = check_names([("src/tests/tests/test_a.py", n) for n in names], [("src/tests/tests/test_a.py", names)])
    assert any("test_edge_c" in v and "after" in v for v in violations)


def test_error_junit_with_only_happy_failing_is_not_red():
    red, reason = judge_red(["test_happy_works"], [])
    assert not red
    assert "happy" in reason


def test_error_no_failures_is_not_red():
    red, reason = judge_red([], [])
    assert not red
    assert "no test fails" in reason


def test_error_parse_junit_failures_on_empty_or_invalid_xml():
    assert parse_junit_failures("") == ([], [])
    assert parse_junit_failures("<not-xml") == ([], [])


def test_edge_parse_waivers_null_and_empty():
    assert parse_waivers(None) == {"tdd": None, "migration": None}
    assert parse_waivers("") == {"tdd": None, "migration": None}


def test_edge_parse_waivers_case_insensitive_but_needs_reason():
    body = "Intro\ntdd-waiver: docs only\nMigration-Waiver:   \n"
    assert parse_waivers(body) == {"tdd": "docs only", "migration": None}


def test_edge_classify_ignores_deletes_and_pure_renames():
    groups = classify_changes([entry("D", "src/photobooth/a.py"), entry("R100", "src/photobooth/b.py")])
    assert groups["logic"] == []


def test_edge_classify_groups_each_kind():
    groups = classify_changes(
        [
            entry("M", "src/photobooth/services/share.py"),
            entry("A", "src/tests/tests/services/test_share.py"),
            entry("A", "src/tests/tests/database/test_migration_cache.py"),
            entry("A", "src/photobooth/database/alembic/versions/abc123_add_x.py"),
            entry("A", "scripts/tests/test_tool.py"),
            entry("M", "src/tests/benchmarks/encode_image_test.py"),
            entry("M", "src/web/frontend/index.html"),
            entry("M", "README.md"),
        ]
    )
    assert groups["logic"] == ["src/photobooth/services/share.py"]
    assert groups["unit"] == ["src/tests/tests/services/test_share.py"]
    assert groups["migration_tests"] == ["src/tests/tests/database/test_migration_cache.py"]
    assert groups["migrations"] == ["src/photobooth/database/alembic/versions/abc123_add_x.py"]
    assert groups["script_tests"] == ["scripts/tests/test_tool.py"]


def test_edge_is_guarded_source_covers_app_logic_only():
    assert is_guarded_source("src/photobooth/services/share.py")
    assert is_guarded_source("src/photobooth/plugins/__init__.py")
    assert not is_guarded_source("src/photobooth/database/alembic/versions/abc_x.py")
    assert not is_guarded_source("src/tests/tests/test_main.py")
    assert not is_guarded_source("src/web/frontend/index.html")
    assert not is_guarded_source("scripts/ci/tdd_lib.py")
    assert not is_guarded_source("docs/ai/planning.md")


def test_edge_extract_handles_async_methods_and_skips_fixtures():
    src = "\n".join(
        [
            "import pytest",
            "@pytest.fixture",
            "def test_client_fixture():",
            "    return 1",
            "async def test_edge_async_case():",
            "    pass",
            "class TestGroup:",
            "    def test_error_in_class(self):",
            "        pass",
            "def helper():",
            "    pass",
        ]
    )
    names = [t.name for t in extract_test_names(src)]
    assert names == ["test_edge_async_case", "test_error_in_class"]


def test_edge_extract_returns_nothing_for_unparseable_source():
    assert extract_test_names("def broken(:\n") == []


def test_edge_junit_collection_failure_is_file_level():
    xml = (
        '<testsuites><testsuite name="pytest" errors="1">'
        '<testcase classname="" name="src.tests.tests.test_vat" time="0.0">'
        '<error message="collection failure">ModuleNotFoundError</error></testcase>'
        "</testsuite></testsuites>"
    )
    assert parse_junit_failures(xml) == ([], ["src.tests.tests.test_vat"])


def test_edge_load_failure_only_counts_as_red():
    red, reason = judge_red([], ["src.tests.tests.test_vat"])
    assert red
    assert "cannot load" in reason


def test_edge_find_bash_write_targets_ignores_reads():
    assert find_bash_write_targets("grep -n foo src/photobooth/a.py && cat src/photobooth/b.py") == []
    assert find_bash_write_targets("sed -n '1,5p' src/photobooth/a.py") == []


def test_edge_find_bash_write_targets_detects_writes():
    assert find_bash_write_targets("sed -i '' 's/a/b/' src/photobooth/a.py") == ["src/photobooth/a.py"]
    assert find_bash_write_targets("perl -pi -e 's/a/b/' src/photobooth/a.py") == ["src/photobooth/a.py"]
    assert find_bash_write_targets("echo x | tee src/photobooth/a.py") == ["src/photobooth/a.py"]
    assert find_bash_write_targets("echo x > src/photobooth/a.py") == ["src/photobooth/a.py"]
    assert find_bash_write_targets("echo x >> 'src/photobooth/b.py'") == ["src/photobooth/b.py"]
    assert find_bash_write_targets("cp /tmp/x.py src/photobooth/c.py") == ["src/photobooth/c.py"]
    assert find_bash_write_targets("mv a.py src/photobooth/d.py") == ["src/photobooth/d.py"]


def test_regression_def_test_inside_string_or_comment_is_not_counted():
    src = 'SNIPPET = """\ndef test_fake():\n    pass\n"""\n# def test_commented():\ndef test_error_real():\n    pass\n'
    assert [t.name for t in extract_test_names(src)] == ["test_error_real"]


def test_regression_redirect_inside_quotes_or_comment_is_not_a_write():
    assert find_bash_write_targets('git commit -m "a > src/photobooth/x.py"') == []
    assert find_bash_write_targets("ls # > src/photobooth/x.py") == []


def test_regression_stderr_dup_is_not_a_write():
    assert find_bash_write_targets("uv run pytest 2>&1 | tail -5") == []
    assert find_bash_write_targets("cmd > /dev/null 2>&1") == []


def test_regression_parametrized_failure_keeps_prefix():
    xml = (
        "<testsuites><testsuite>"
        '<testcase classname="src.tests.tests.test_vat" name="test_error_bad[-1]"><failure message="x"/></testcase>'
        "</testsuite></testsuites>"
    )
    test_level, file_level = parse_junit_failures(xml)
    assert test_level == ["test_error_bad[-1]"]
    assert judge_red(test_level, file_level)[0]


def test_happy_ordered_new_file_has_no_violations():
    src = "\n".join(
        [
            "def test_error_a():\n    pass",
            "def test_edge_b():\n    pass",
            "def test_regression_c():\n    pass",
            "def test_happy_d():\n    pass",
        ]
    )
    names = extract_test_names(src)
    assert [t.prefix for t in names] == ["error", "edge", "regression", "happy"]
    assert check_names([("f.py", n) for n in names], [("f.py", names)]) == []


def test_happy_error_or_regression_failing_is_valid_red():
    assert judge_red(["test_error_x", "test_happy_y"], [])[0]
    assert judge_red(["test_regression_x"], [])[0]
