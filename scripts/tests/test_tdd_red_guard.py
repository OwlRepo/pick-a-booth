# Claude PreToolUse hook: blocks src/photobooth logic writes until a valid RED marker exists.
import json
from pathlib import Path

from repo_fixture import git, make_repo, run_script, write

SCRIPT = "hooks/tdd_red_guard.py"


def call(cwd, tool_name: str, tool_input: dict):
    return run_script(SCRIPT, cwd, stdin=json.dumps({"tool_name": tool_name, "cwd": str(cwd), "tool_input": tool_input}))


def put_marker(root: Path, data: dict | str) -> None:
    path = Path(git(root, "rev-parse", "--absolute-git-dir")) / "tdd-red.json"
    path.write_text(data if isinstance(data, str) else json.dumps(data))


LOGIC = "src/photobooth/services/share.py"


def test_error_non_json_stdin_fails_open_with_warning():
    repo = make_repo()
    try:
        res = run_script(SCRIPT, repo.root, stdin="not json")
        assert res.returncode == 0
        assert "not JSON" in res.stderr
    finally:
        repo.cleanup()


def test_error_edit_without_file_path_is_allowed():
    repo = make_repo()
    try:
        assert call(repo.root, "Edit", {}).returncode == 0
    finally:
        repo.cleanup()


def test_error_corrupt_marker_blocks():
    repo = make_repo()
    try:
        put_marker(repo.root, "{broken")
        res = call(repo.root, "Edit", {"file_path": str(repo.root / LOGIC)})
        assert res.returncode == 2
        assert "corrupt" in res.stderr
    finally:
        repo.cleanup()


def test_error_logic_edit_without_marker_blocks():
    repo = make_repo()
    try:
        res = call(repo.root, "Write", {"file_path": str(repo.root / LOGIC)})
        assert res.returncode == 2
        assert "RED first" in res.stderr
        assert "uv run poe tdd:red" in res.stderr
    finally:
        repo.cleanup()


def test_edge_marker_from_other_branch_is_invalid():
    repo = make_repo()
    try:
        put_marker(repo.root, {"branch": "other", "failed_names": ["test_error_x"], "load_failures": []})
        assert call(repo.root, "Edit", {"file_path": str(repo.root / LOGIC)}).returncode == 2
    finally:
        repo.cleanup()


def test_edge_tests_docs_scripts_and_migrations_are_never_blocked():
    repo = make_repo()
    try:
        for rel in [
            "src/tests/tests/test_x.py",
            "docs/ai/planning.md",
            "scripts/ci/tdd_lib.py",
            "src/photobooth/database/alembic/versions/abc_x.py",
            "src/web/frontend/index.html",
        ]:
            assert call(repo.root, "Edit", {"file_path": str(repo.root / rel)}).returncode == 0, rel
    finally:
        repo.cleanup()


def test_edge_file_outside_any_repo_is_allowed(tmp_path):
    assert call(tmp_path, "Write", {"file_path": str(tmp_path / "src/photobooth/x.py")}).returncode == 0


def test_edge_read_only_bash_mentioning_src_is_allowed():
    repo = make_repo()
    try:
        assert call(repo.root, "Bash", {"command": f"grep -n share {LOGIC} && cat {LOGIC}"}).returncode == 0
    finally:
        repo.cleanup()


def test_edge_sed_in_place_on_test_allowed_on_logic_blocked():
    repo = make_repo()
    try:
        assert call(repo.root, "Bash", {"command": "sed -i '' 's/a/b/' src/tests/tests/test_x.py"}).returncode == 0
        assert call(repo.root, "Bash", {"command": f"sed -i '' 's/a/b/' {LOGIC}"}).returncode == 2
    finally:
        repo.cleanup()


def test_edge_relative_bash_paths_resolve_against_tool_cwd():
    repo = make_repo()
    try:
        write(repo.root, "src/photobooth/services/.keep", "")
        res = call(repo.root / "src/photobooth/services", "Bash", {"command": "echo x > share.py"})
        assert res.returncode == 2
    finally:
        repo.cleanup()


def test_edge_main_without_marker_blocks():
    repo = make_repo()
    try:
        git(repo.root, "checkout", "-q", "main")
        assert call(repo.root, "Edit", {"file_path": str(repo.root / LOGIC)}).returncode == 2
    finally:
        repo.cleanup()


def test_edge_waiver_marker_allows():
    repo = make_repo()
    try:
        put_marker(repo.root, {"branch": "feature", "waiver": "comment-only change"})
        assert call(repo.root, "Edit", {"file_path": str(repo.root / LOGIC)}).returncode == 0
    finally:
        repo.cleanup()


def test_regression_marker_with_only_happy_failures_does_not_allow():
    repo = make_repo()
    try:
        put_marker(repo.root, {"branch": "feature", "failed_names": ["test_happy_x"], "load_failures": []})
        assert call(repo.root, "Edit", {"file_path": str(repo.root / LOGIC)}).returncode == 2
    finally:
        repo.cleanup()


def test_happy_valid_red_marker_allows():
    repo = make_repo()
    try:
        put_marker(repo.root, {"branch": "feature", "failed_names": ["test_error_x"], "load_failures": []})
        assert call(repo.root, "MultiEdit", {"file_path": str(repo.root / LOGIC)}).returncode == 0
    finally:
        repo.cleanup()
