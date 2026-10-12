# Persona single source: agents/src/*.agent.toml + prompts/*.md -> .claude/agents + .codex/agents.
import shutil
import tomllib
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
        "codex": {"model": "gpt-x", "model_reasoning_effort": "medium", "sandbox_mode": "read-only", "mcp_servers": []},
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
                "[codex]",
                'model = "gpt-x"',
                'model_reasoning_effort = "medium"',
                'sandbox_mode = "read-only"',
                "mcp_servers = []",
                "",
            ]
        )
    )
    (root / "agents/src/prompts/fixture-dev.md").write_text("You are a fixture.\n")
    return root


def test_error_prompt_with_toml_terminator_is_rejected():
    try:
        gen.render_codex_toml(fixture_persona(system_prompt='bad """ text\n'))
    except ValueError as err:
        assert "fixture-dev" in str(err)
    else:
        raise AssertionError("expected ValueError")


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
    (root / ".codex/agents/ghost.toml").write_text('name = "ghost"\n')
    res = run_script(SCRIPT, root, "--root", str(root), "--check")
    assert res.returncode == 1
    assert "ghost.toml" in res.stderr


def test_error_check_fails_when_generated_file_is_missing(tmp_path):
    root = scratch_root(tmp_path)
    res = run_script(SCRIPT, root, "--root", str(root), "--check")
    assert res.returncode == 1
    assert "does not exist" in res.stderr


def test_error_duplicate_owned_glob_across_personas_is_reported():
    failures = gen.find_duplicate_owned_globs([fixture_persona(), fixture_persona(name="other-dev")])
    assert failures and "src/photobooth/fixture/**" in failures[0]


def test_edge_codex_toml_omits_mcp_servers_when_empty():
    assert "mcp_servers" not in gen.render_codex_toml(fixture_persona())


def test_edge_codex_toml_includes_mcp_servers_when_populated():
    persona = fixture_persona(codex={**fixture_persona()["codex"], "mcp_servers": ["github"]})
    assert 'mcp_servers = ["github"]' in gen.render_codex_toml(persona)


def test_edge_global_policy_is_toml_safe_and_has_no_absolute_home_path():
    assert '"""' not in gen.GLOBAL_POLICY
    assert "/Users/" not in gen.GLOBAL_POLICY
    assert "~/.agents/skills/caveman/SKILL.md" in gen.GLOBAL_POLICY


def test_regression_real_repo_check_passes():
    res = run_script(SCRIPT, REPO_ROOT, "--check")
    assert res.returncode == 0, res.stdout + res.stderr


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


def test_happy_codex_toml_parses_and_carries_instructions():
    data = tomllib.loads(gen.render_codex_toml(fixture_persona()))
    assert data["name"] == "fixture-dev"
    assert data["model_reasoning_effort"] == "medium"
    assert data["sandbox_mode"] == "read-only"
    assert data["developer_instructions"].startswith("You are a fixture.")
    assert "Global Policy" in data["developer_instructions"]


def test_happy_check_passes_right_after_generation(tmp_path):
    root = scratch_root(tmp_path)
    assert run_script(SCRIPT, root, "--root", str(root)).returncode == 0
    res = run_script(SCRIPT, root, "--root", str(root), "--check")
    assert res.returncode == 0, res.stdout + res.stderr
    shutil.rmtree(root)
