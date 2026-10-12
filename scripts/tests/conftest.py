# Makes scripts/ci, scripts/hooks and scripts/ importable for the tooling tests.
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
for sub in (SCRIPTS, SCRIPTS / "ci", SCRIPTS / "hooks"):
    if str(sub) not in sys.path:
        sys.path.insert(0, str(sub))
