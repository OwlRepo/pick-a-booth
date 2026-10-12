# Per-commit test-layer guard (optra's check-test-layers, ported): every commit that
# changes app code carries the tests for the layers it touches.
from repo_fixture import git, make_repo, run_script

from check_test_layers import problems_for

SCRIPT = "ci/check_test_layers.py"
ZERO = "0" * 40


def run(repo, base, head="HEAD"):
    return run_script(SCRIPT, repo.root, base, head)


def base_sha(repo):
    return git(repo.root, "rev-parse", "origin/main")


def test_error_service_change_without_service_test_fails():
    repo = make_repo()
    try:
        repo.commit({"src/photobooth/services/share.py": "x = 1\n"}, "feat: share")
        res = run(repo, base_sha(repo))
        assert res.returncode == 1, res.stdout + res.stderr
        assert "MISSING TESTS" in res.stdout
        assert "src/tests/tests/services/" in res.stdout
    finally:
        repo.cleanup()


def test_error_router_change_without_router_test_fails():
    repo = make_repo()
    try:
        repo.commit({"src/photobooth/routers/api/actions.py": "x = 1\n"}, "feat: route")
        assert run(repo, base_sha(repo)).returncode == 1
    finally:
        repo.cleanup()


def test_error_migration_without_migration_test_fails():
    repo = make_repo()
    try:
        repo.commit(
            {
                "src/photobooth/database/alembic/versions/abc_add_x.py": "revision = 'abc'\n",
                "src/tests/tests/services/test_collection.py": "def test_happy_x():\n    pass\n",
            },
            "feat: migration",
        )
        res = run(repo, base_sha(repo))
        assert res.returncode == 1
        assert "migration" in res.stdout
    finally:
        repo.cleanup()


def test_error_skip_line_in_body_not_trailer_does_not_count():
    repo = make_repo()
    try:
        msg = "chore: x\n\nTest-Layers-Skip: not a trailer\n\nmore words after it"
        repo.commit({"src/photobooth/services/share.py": "x = 1\n"}, msg)
        assert run(repo, base_sha(repo)).returncode == 1
    finally:
        repo.cleanup()


def test_edge_docs_only_commit_passes():
    repo = make_repo()
    try:
        repo.commit({"docs/ai/x.md": "# x\n", "README.md": "readme\n"}, "docs: words")
        assert run(repo, base_sha(repo)).returncode == 0
    finally:
        repo.cleanup()


def test_edge_test_in_wrong_area_does_not_count():
    repo = make_repo()
    try:
        repo.commit(
            {"src/photobooth/services/share.py": "x = 1\n", "src/tests/tests/utils/test_helper.py": "def test_happy_x():\n    pass\n"},
            "feat: share",
        )
        assert run(repo, base_sha(repo)).returncode == 1
    finally:
        repo.cleanup()


def test_edge_deleted_files_are_ignored():
    repo = make_repo({"src/photobooth/services/old.py": "x = 1\n"})
    try:
        repo.commit({"src/photobooth/services/old.py": None}, "chore: remove old")
        assert run(repo, base_sha(repo)).returncode == 0
    finally:
        repo.cleanup()


def test_edge_empty_or_zero_base_falls_back_to_merge_base_with_origin_main():
    repo = make_repo()
    try:
        repo.commit({"src/photobooth/services/share.py": "x = 1\n"}, "feat: share")
        assert run(repo, "").returncode == 1
        assert run(repo, ZERO).returncode == 1
    finally:
        repo.cleanup()


def test_edge_no_base_at_all_checks_nothing():
    repo = make_repo()
    try:
        repo.commit({"src/photobooth/services/share.py": "x = 1\n"}, "feat: share")
        git(repo.root, "update-ref", "-d", "refs/remotes/origin/main")
        res = run(repo, "")
        assert res.returncode == 0
        assert "nothing checked" in res.stderr
    finally:
        repo.cleanup()


def test_edge_init_files_and_tooling_are_not_policed():
    assert problems_for(["src/photobooth/services/__init__.py"]) == []
    assert problems_for(["scripts/ci/tdd_gate.py", ".github/workflows/ci.yml", "pyproject.toml"]) == []


def test_edge_each_layer_maps_to_its_test_area():
    assert problems_for(["src/photobooth/services/backends/gphoto2.py", "src/tests/tests/backends/test_gphoto2.py"]) == []
    assert problems_for(["src/photobooth/plugins/wled/wled.py", "src/tests/tests/plugins/test_wled.py"]) == []
    assert problems_for(["src/photobooth/utils/helper.py", "src/tests/tests/utils/test_resizer.py"]) == []
    assert problems_for(["src/photobooth/routers/api_admin/files.py", "src/tests/tests/router/api_admin/test_files.py"]) == []
    assert problems_for(["src/photobooth/routers/auth_dependencies_bearer.py", "src/tests/tests/router/test_authentication.py"]) == []
    assert problems_for(["src/photobooth/routers/media.py", "src/tests/tests/router/test_media.py"]) == []
    assert problems_for(["src/photobooth/services/mediaprocessing/steps/image.py", "src/tests/tests/mediaprocessing/test_imagesteps.py"]) == []
    assert problems_for(["src/photobooth/application.py", "src/tests/tests/test_application.py"]) == []
    assert problems_for(["src/photobooth/database/alembic/versions/abc_x.py", "src/tests/tests/database/test_migration_abc.py"]) == []


def test_regression_later_commit_test_does_not_excuse_earlier_commit():
    repo = make_repo()
    try:
        repo.commit({"src/photobooth/services/share.py": "x = 1\n"}, "feat: share")
        repo.commit({"src/tests/tests/services/test_share.py": "def test_error_x():\n    pass\n"}, "test: later")
        res = run(repo, base_sha(repo))
        assert res.returncode == 1
        assert "feat: share" in res.stdout
    finally:
        repo.cleanup()


def test_happy_backend_change_with_its_test_passes():
    repo = make_repo()
    try:
        repo.commit(
            {"src/photobooth/services/share.py": "x = 1\n", "src/tests/tests/services/test_share.py": "def test_error_x():\n    pass\n"},
            "feat: share",
        )
        res = run(repo, base_sha(repo))
        assert res.returncode == 0, res.stdout + res.stderr
        assert "carries its tests" in res.stdout
    finally:
        repo.cleanup()


def test_happy_skip_trailer_passes_and_prints_reason():
    repo = make_repo()
    try:
        msg = "chore: rename a local\n\nTest-Layers-Skip: rename only, no behaviour moved"
        repo.commit({"src/photobooth/services/share.py": "x = 1\n"}, msg)
        res = run(repo, base_sha(repo))
        assert res.returncode == 0, res.stdout + res.stderr
        assert "rename only, no behaviour moved" in res.stdout
    finally:
        repo.cleanup()
