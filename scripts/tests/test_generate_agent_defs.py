# Persona single source: agents/src/*.agent.toml + prompts/*.md -> .claude/agents (Claude Code only).
import shutil
from pathlib import Path

import generate_agent_defs as gen
from repo_fixture import REPO_ROOT, run_script

SCRIPT = "generate_agent_defs.py"


def fixture_persona(**overrides):
    persona = {
        "name": "fixture-dev",
        "file_prefix": "99",
        "description": 'Fixture persona with "quotes".',
        "owned_globs": ["src/photobooth/fixture/**"],
        "claude": {"tools": ["Read", "Grep"], "model": "sonnet"},
        "system_prompt": "You are a fixture.\n",
    }
    persona.update(overrides)
    return persona


def scratch_root(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    (root / "agents/src/prompts").mkdir(parents=True)
    (root / "agents/src/fixture-dev.agent.toml").write_text(
        "\n".join(
            [
                'name = "fixture-dev"',
                'file_prefix = "99"',
                'description = "Fixture persona."',
                'owned_globs = ["src/photobooth/fixture/**"]',
                "[claude]",
                'tools = ["Read"]',
                'model = "sonnet"',
                "",
            ]
        )
    )
    (root / "agents/src/prompts/fixture-dev.md").write_text("You are a fixture.\n")
    return root


def test_error_check_fails_when_generated_file_is_hand_edited(tmp_path):
    root = scratch_root(tmp_path)
    assert run_script(SCRIPT, root, "--root", str(root)).returncode == 0
    claude = root / ".claude/agents/99-fixture-dev.md"
    claude.write_text(claude.read_text() + "hand edit\n")
    res = run_script(SCRIPT, root, "--root", str(root), "--check")
    assert res.returncode == 1
    assert "does not match" in res.stderr


def test_error_check_fails_on_orphan_generated_file(tmp_path):
    root = scratch_root(tmp_path)
    assert run_script(SCRIPT, root, "--root", str(root)).returncode == 0
    (root / ".claude/agents/42-ghost.md").write_text("---\nname: ghost\n---\n")
    res = run_script(SCRIPT, root, "--root", str(root), "--check")
    assert res.returncode == 1
    assert "42-ghost.md" in res.stderr


def test_error_check_fails_when_generated_file_is_missing(tmp_path):
    root = scratch_root(tmp_path)
    res = run_script(SCRIPT, root, "--root", str(root), "--check")
    assert res.returncode == 1
    assert "does not exist" in res.stderr


def test_error_duplicate_owned_glob_across_personas_is_reported():
    failures = gen.find_duplicate_owned_globs([fixture_persona(), fixture_persona(name="other-dev")])
    assert failures and "src/photobooth/fixture/**" in failures[0]


def test_error_check_fails_when_codex_definitions_exist(tmp_path):
    root = scratch_root(tmp_path)
    assert run_script(SCRIPT, root, "--root", str(root)).returncode == 0
    (root / ".codex/agents").mkdir(parents=True)
    (root / ".codex/agents/fixture-dev.toml").write_text('name = "fixture-dev"\n')
    res = run_script(SCRIPT, root, "--root", str(root), "--check")
    assert res.returncode == 1
    assert ".codex" in res.stderr


def test_edge_global_policy_has_no_absolute_home_path():
    assert "/Users/" not in gen.GLOBAL_POLICY
    assert "~/.agents/skills/caveman/SKILL.md" in gen.GLOBAL_POLICY


def test_regression_generate_writes_no_codex_files(tmp_path):
    root = scratch_root(tmp_path)
    assert run_script(SCRIPT, root, "--root", str(root)).returncode == 0
    assert not (root / ".codex").exists()


def test_regression_real_repo_check_passes():
    res = run_script(SCRIPT, REPO_ROOT, "--check")
    assert res.returncode == 0, res.stdout + res.stderr
    assert not (REPO_ROOT / ".codex").exists()


def test_regression_every_owned_glob_is_documented_in_agent_orchestration():
    doc = (REPO_ROOT / "docs/ai/agent-orchestration.md").read_text()
    personas = gen.load_personas(REPO_ROOT / "agents/src")
    globs = [g for p in personas for g in p["owned_globs"]]
    assert globs, "expected at least one owned glob"
    missing = [g for g in globs if f"`{g}`" not in doc]
    assert missing == []


def test_happy_claude_markdown_has_frontmatter_body_and_policy():
    out = gen.render_claude_markdown(fixture_persona())
    assert out.startswith('---\nname: fixture-dev\ndescription: "Fixture persona with \\"quotes\\"."\ntools: Read, Grep\nmodel: sonnet\n---\n\n')
    assert "You are a fixture.\n" in out
    assert out.endswith(gen.GLOBAL_POLICY)


def test_happy_check_passes_right_after_generation(tmp_path):
    root = scratch_root(tmp_path)
    assert run_script(SCRIPT, root, "--root", str(root)).returncode == 0
    res = run_script(SCRIPT, root, "--root", str(root), "--check")
    assert res.returncode == 0, res.stdout + res.stderr
    shutil.rmtree(root)
