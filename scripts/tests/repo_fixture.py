# Disposable git repos for the tdd_* integration tests. Not a test module itself.
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
REPO_ROOT = SCRIPTS.parent


def git(cwd: str | Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def write(root: str | Path, rel: str, content: str) -> None:
    path = Path(root, rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


@dataclass
class Repo:
    root: Path

    def commit(self, files: dict[str, str | None], message: str = "change") -> None:
        for rel, content in files.items():
            if content is None:
                git(self.root, "rm", "-q", rel)
            else:
                write(self.root, rel, content)
        git(self.root, "add", "-A")
        git(self.root, "commit", "-q", "-m", message)

    def cleanup(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


# Base commit on `main`, then a `feature` branch checked out. `origin/main` is faked
# as a local ref so the scripts' default base resolves without a network remote.
def make_repo(base_files: dict[str, str] | None = None) -> Repo:
    root = Path(tempfile.mkdtemp(prefix="tdd-repo-")).resolve()
    git(root, "init", "-q", "-b", "main")
    git(root, "config", "user.email", "t@t.test")
    git(root, "config", "user.name", "t")
    git(root, "config", "commit.gpgsign", "false")
    write(root, ".gitignore", "__pycache__/\n")
    write(root, "src/photobooth/__init__.py", "")
    for rel, content in (base_files or {}).items():
        write(root, rel, content)
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "base")
    git(root, "update-ref", "refs/remotes/origin/main", "HEAD")
    git(root, "checkout", "-q", "-b", "feature")
    return Repo(root)


def run_script(script: str, cwd: str | Path, *args: str, env: dict[str, str] | None = None, stdin: str | None = None):
    merged = {k: v for k, v in os.environ.items() if not k.startswith(("TDD_", "PR_BODY", "GITHUB_"))}
    merged.update(env or {})
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args], cwd=cwd, env=merged, input=stdin, capture_output=True, text=True, timeout=300
    )


VAT_BUGGY = "def vat(amount: float) -> float:\n    return amount * 0.1\n"
VAT_FIXED = (
    "def vat(amount: float) -> float:\n"
    "    if amount < 0:\n"
    "        raise ValueError('negative')\n"
    "    return round(amount * 0.13, 2)\n"
)
VAT_TEST = "\n".join(
    [
        "import pytest",
        "",
        "from photobooth.vat import vat",
        "",
        "",
        "def test_error_rejects_negative_amounts():",
        "    with pytest.raises(ValueError):",
        "        vat(-1)",
        "",
        "",
        "def test_edge_zero_gives_zero():",
        "    assert vat(0) == 0",
        "",
        "",
        "def test_happy_thirteen_percent_of_100():",
        "    assert vat(100) == 13",
        "",
    ]
)
