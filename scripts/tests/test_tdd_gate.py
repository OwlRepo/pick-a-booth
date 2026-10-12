# CI TDD gate: tests present, names prefixed + ordered, and RED against the merge-base.
from repo_fixture import VAT_BUGGY, VAT_FIXED, VAT_TEST, git, make_repo, run_script

SCRIPT = "ci/tdd_gate.py"
BASE = {"TDD_GATE_BASE": "origin/main"}


def test_error_missing_base_env_exits_2():
    repo = make_repo()
    try:
        assert run_script(SCRIPT, repo.root).returncode == 2
    finally:
        repo.cleanup()


def test_error_unknown_base_exits_2():
    repo = make_repo()
    try:
        assert run_script(SCRIPT, repo.root, env={"TDD_GATE_BASE": "origin/nope"}).returncode == 2
    finally:
        repo.cleanup()


def test_error_logic_change_without_tests_blocks():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/photobooth/vat.py": VAT_FIXED})
        res = run_script(SCRIPT, repo.root, env=BASE)
        assert res.returncode == 1, res.stdout + res.stderr
        assert "logic changed without any test" in res.stdout
    finally:
        repo.cleanup()


def test_error_test_hanging_on_base_times_out_and_cleans_worktree():
    hang = "import time\n\n\ndef test_error_hangs():\n    time.sleep(60)\n"
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/photobooth/vat.py": VAT_FIXED, "src/tests/tests/test_hang.py": hang})
        res = run_script(SCRIPT, repo.root, env={**BASE, "TDD_GATE_TIMEOUT_S": "3"})
        assert res.returncode == 2, res.stdout + res.stderr
        assert "timeout" in res.stderr
        assert git(repo.root, "worktree", "list").count("\n") == 0
    finally:
        repo.cleanup()


def test_edge_docs_only_change_passes():
    repo = make_repo()
    try:
        repo.commit({"docs/x.md": "# x\n"})
        res = run_script(SCRIPT, repo.root, env=BASE)
        assert res.returncode == 0, res.stdout + res.stderr
    finally:
        repo.cleanup()


def test_edge_tests_only_change_needs_prefixes_but_no_red():
    repo = make_repo({"src/photobooth/vat.py": VAT_FIXED})
    try:
        repo.commit({"src/tests/tests/test_vat.py": VAT_TEST})
        assert run_script(SCRIPT, repo.root, env=BASE).returncode == 0
        repo.commit({"src/tests/tests/test_more.py": "def test_unprefixed():\n    pass\n"})
        res = run_script(SCRIPT, repo.root, env=BASE)
        assert res.returncode == 1
        assert "test_unprefixed" in res.stdout
    finally:
        repo.cleanup()


def test_edge_upstream_sync_pr_from_main_is_skipped():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/photobooth/vat.py": VAT_FIXED})
        res = run_script(SCRIPT, repo.root, env={**BASE, "TDD_GATE_HEAD_REF": "main"})
        assert res.returncode == 0
        assert "skip" in res.stdout
    finally:
        repo.cleanup()


def test_edge_tdd_waiver_lets_logic_without_tests_pass():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/photobooth/vat.py": VAT_FIXED})
        res = run_script(SCRIPT, repo.root, env={**BASE, "PR_BODY": "TDD-Waiver: comment-only change"})
        assert res.returncode == 0, res.stdout + res.stderr
        assert "TDD-Waiver: comment-only change" in res.stdout
    finally:
        repo.cleanup()


def test_edge_migration_without_migration_test_blocks_unless_waived():
    mig = "revision = 'abc'\ndown_revision = None\n"
    repo = make_repo()
    try:
        repo.commit({"src/photobooth/database/alembic/versions/abc_add_x.py": mig})
        res = run_script(SCRIPT, repo.root, env=BASE)
        assert res.returncode == 1
        assert "migration" in res.stdout
        res = run_script(SCRIPT, repo.root, env={**BASE, "PR_BODY": "Migration-Waiver: covered by test_db_init"})
        assert res.returncode == 0, res.stdout + res.stderr
    finally:
        repo.cleanup()


def test_edge_new_module_missing_on_base_counts_as_red():
    test = "from photobooth.newmod import f\n\n\ndef test_error_f_rejects_none():\n    assert f(None) is None\n"
    repo = make_repo()
    try:
        repo.commit({"src/photobooth/newmod.py": "def f(x):\n    return x\n", "src/tests/tests/test_newmod.py": test})
        res = run_script(SCRIPT, repo.root, env=BASE)
        assert res.returncode == 0, res.stdout + res.stderr
        assert "RED against base" in res.stdout
    finally:
        repo.cleanup()


def test_regression_tests_already_passing_on_old_code_block():
    repo = make_repo({"src/photobooth/vat.py": VAT_FIXED})
    try:
        repo.commit({"src/photobooth/vat.py": VAT_FIXED + "\n# touched\n", "src/tests/tests/test_vat.py": VAT_TEST})
        res = run_script(SCRIPT, repo.root, env=BASE)
        assert res.returncode == 1, res.stdout + res.stderr
        assert "RED:" in res.stdout
    finally:
        repo.cleanup()


def test_regression_refactor_waiver_requires_tests_to_pass_on_base():
    repo = make_repo({"src/photobooth/vat.py": VAT_FIXED})
    try:
        repo.commit({"src/photobooth/vat.py": VAT_FIXED + "\n# moved\n", "src/tests/tests/test_vat.py": VAT_TEST})
        res = run_script(SCRIPT, repo.root, env={**BASE, "PR_BODY": "TDD-Waiver: refactor split module"})
        assert res.returncode == 0, res.stdout + res.stderr
    finally:
        repo.cleanup()
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/photobooth/vat.py": VAT_FIXED, "src/tests/tests/test_vat.py": VAT_TEST})
        res = run_script(SCRIPT, repo.root, env={**BASE, "PR_BODY": "TDD-Waiver: refactor split module"})
        assert res.returncode == 1
        assert "behaviour changed" in res.stdout
    finally:
        repo.cleanup()


def test_happy_fix_with_tests_failing_on_base_passes():
    repo = make_repo({"src/photobooth/vat.py": VAT_BUGGY})
    try:
        repo.commit({"src/tests/tests/test_vat.py": VAT_TEST}, "test(vat): RED")
        repo.commit({"src/photobooth/vat.py": VAT_FIXED}, "fix(vat): 13%")
        res = run_script(SCRIPT, repo.root, env=BASE)
        assert res.returncode == 0, res.stdout + res.stderr
        assert "ok: TDD gate passed" in res.stdout
    finally:
        repo.cleanup()
