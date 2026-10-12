# `uv run poe tdd:red`: records that the branch's new tests fail BEFORE implementation.
import json
from pathlib import Path

from repo_fixture import VAT_BUGGY, VAT_FIXED, VAT_TEST, git, make_repo, run_script, write

SCRIPT = "ci/tdd_red.py"


def marker(root: Path) -> Path:
    return Path(git(root, "rev-parse", "--absolute-git-dir")) / "tdd-red.json"


def test_error_no_changed_tests_exits_1_without_marker():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/photobooth/vat.py": VAT_FIXED})
        res = run_script(SCRIPT, repo.root)
        assert res.returncode == 1, res.stdout + res.stderr
        assert "no new or changed tests" in res.stderr
        assert not marker(repo.root).exists()
    finally:
        repo.cleanup()


def test_error_unknown_base_exits_2():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        res = run_script(SCRIPT, repo.root, env={"TDD_RED_BASE": "origin/does-not-exist"})
        assert res.returncode == 2, res.stdout + res.stderr
    finally:
        repo.cleanup()


def test_error_new_tests_already_passing_write_no_marker():
    repo = make_repo({"src/photobooth/vat.py": VAT_FIXED})
    try:
        repo.commit({"src/tests/tests/test_vat.py": VAT_TEST})
        res = run_script(SCRIPT, repo.root)
        assert res.returncode == 1, res.stdout + res.stderr
        assert "no test fails" in res.stderr
        assert not marker(repo.root).exists()
    finally:
        repo.cleanup()


def test_edge_untracked_test_file_counts():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        write(repo.root, "src/tests/tests/test_vat.py", VAT_TEST)
        res = run_script(SCRIPT, repo.root)
        assert res.returncode == 0, res.stdout + res.stderr
        assert marker(repo.root).exists()
    finally:
        repo.cleanup()


def test_edge_waiver_with_reason_writes_waiver_marker():
    repo = make_repo()
    try:
        res = run_script(SCRIPT, repo.root, "--waiver", "docs only")
        assert res.returncode == 0, res.stdout + res.stderr
        data = json.loads(marker(repo.root).read_text())
        assert data["branch"] == "feature"
        assert data["waiver"] == "docs only"
        assert "TDD-Waiver: docs only" in res.stdout
    finally:
        repo.cleanup()


def test_edge_waiver_without_reason_is_rejected():
    repo = make_repo()
    try:
        res = run_script(SCRIPT, repo.root, "--waiver")
        assert res.returncode == 2
        assert not marker(repo.root).exists()
    finally:
        repo.cleanup()


def test_edge_marker_lives_in_the_worktree_git_dir():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    wt = repo.root.parent / (repo.root.name + "-wt")
    try:
        git(repo.root, "worktree", "add", "-q", "-b", "other", str(wt))
        write(wt, "src/tests/tests/test_vat.py", VAT_TEST)
        res = run_script(SCRIPT, wt)
        assert res.returncode == 0, res.stdout + res.stderr
        assert marker(wt).exists()
        assert not marker(repo.root).exists()
    finally:
        git(repo.root, "worktree", "remove", "--force", str(wt))
        repo.cleanup()


def test_regression_only_happy_failing_is_not_red():
    happy_only = "from photobooth.vat import vat\n\n\ndef test_happy_thirteen_percent():\n    assert vat(100) == 13\n"
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/tests/tests/test_vat.py": happy_only})
        res = run_script(SCRIPT, repo.root)
        assert res.returncode == 1, res.stdout + res.stderr
        assert not marker(repo.root).exists()
    finally:
        repo.cleanup()


def test_happy_failing_error_case_writes_marker_with_branch_and_names():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/tests/tests/test_vat.py": VAT_TEST})
        res = run_script(SCRIPT, repo.root)
        assert res.returncode == 0, res.stdout + res.stderr
        data = json.loads(marker(repo.root).read_text())
        assert data["branch"] == "feature"
        assert "test_error_rejects_negative_amounts" in data["failed_names"]
        assert data["test_files"] == ["src/tests/tests/test_vat.py"]
    finally:
        repo.cleanup()
