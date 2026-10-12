# Every repo path the workflow docs cite must exist, so no doc reference dangles.
import re
from pathlib import Path

from repo_fixture import REPO_ROOT

DOCS = [
    REPO_ROOT / "AGENTS.md",
    REPO_ROOT / "CLAUDE.md",
    REPO_ROOT / "AI_WORKFLOW.md",
    REPO_ROOT / "PLANNING_STANDARDS.md",
    *sorted((REPO_ROOT / "docs/ai").rglob("*.md")),
    *sorted((REPO_ROOT / ".ai-engineering").rglob("*.md")),
    *sorted((REPO_ROOT / "agents/src/prompts").glob("*.md")),
]
ROOTS = ("AGENTS.md", "CLAUDE.md", "graphify-out/", "docs/", ".ai-engineering/", "scripts/", "agents/", ".claude/", ".codex/", ".github/", "src/", "pyproject.toml")
TICKED = re.compile(r"`([^`\s]+)`")
MD_LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def cited_paths(doc: Path, text: str) -> list[str]:
    out = []
    for m in TICKED.finditer(text):
        token = m.group(1).rstrip(".,:;")
        if token.startswith(ROOTS) and not any(c in token for c in "*<>{}$|"):
            out.append(token.split(":")[0].split("::")[0])
    for m in MD_LINK.finditer(text):
        target = m.group(1)
        if not target.startswith(("http://", "https://", "mailto:")):
            out.append(str((doc.parent / target).resolve().relative_to(REPO_ROOT)))
    return out


def test_error_workflow_docs_exist():
    missing = [str(d.relative_to(REPO_ROOT)) for d in DOCS[:4] if not d.exists()]
    assert missing == []
    assert (REPO_ROOT / "docs/ai/task-router.md").exists()


def test_edge_no_cited_path_dangles():
    dangling = []
    for doc in DOCS:
        if not doc.exists():
            continue
        for rel in cited_paths(doc, doc.read_text()):
            if not (REPO_ROOT / rel).exists():
                dangling.append(f"{doc.relative_to(REPO_ROOT)} -> {rel}")
    assert dangling == []


def test_edge_no_absolute_home_paths_in_public_docs():
    offenders = [str(d.relative_to(REPO_ROOT)) for d in DOCS if d.exists() and "/Users/" in d.read_text()]
    assert offenders == []


def test_happy_claude_md_imports_agents_md_first():
    assert (REPO_ROOT / "CLAUDE.md").read_text().startswith("@AGENTS.md\n")
