@AGENTS.md

# pick-a-booth — Project Context

> Every fact below cites the file that proves it. If something here contradicts
> the code, the code wins — and fix this file in the same PR.

## What it is

pick-a-booth is OwlRepo's **public fork** of
[photobooth-app](https://github.com/photobooth-app/photobooth-app)
(`gh api repos/OwlRepo/pick-a-booth` → `fork: true`, parent
`photobooth-app/photobooth-app`). The package is still named `photobooth-app`,
version `v9.0.0` (`pyproject.toml` `[project]`). It is a photobooth for events:
stills, animated GIFs, collages, boomerang/video and 3D wigglegrams from DSLR
(gphoto2, digiCamControl), Raspberry Pi cameras (picamera2) and webcams, with a
live preview, printing, sharing and WLED/GPIO hardware integration
(`README.md` "Features"). It runs on Linux, Raspberry Pi and Windows.

The kiosk and admin UI is a **prebuilt Vue3 bundle** in `src/web/frontend/`; its
source lives in the separate photobooth-frontend repository
(`CONTRIBUTING.md` "Running & Testing Locally"). There is no JS/TS source and no
Node tooling in this repository.

Direction: pick-a-booth is being built into **our own desktop app** on top of the
fork (repo owner, 2026-10-13). There is no server deployment; CI is a quality
gate only (`.github/workflows/ci.yml`). Upstream photobooth-app changes are
merged by choice, not by default.

## Tech stack

- **Python ≥3.11** (`pyproject.toml` `requires-python`), CI desktop matrix Linux 3.11/3.14, Windows 3.12/3.14, macOS 3.13/3.14 (`.github/workflows/ci.yml` `desktop-tests`).
- **uv** for environments and builds (`uv_build` backend, `uv.lock`); tasks via **poethepoet** (`[tool.poe.tasks]`).
- **FastAPI** + **uvicorn**, **pydantic** v2 + **pydantic-settings** for config.
- **SQLAlchemy 2** + **Alembic** on **SQLite** (`src/photobooth/database/database.py`).
- **pluggy** plugin system (`src/photobooth/plugins/__init__.py`), **python-statemachine** for the processing machine.
- Imaging/video: opencv-python-headless, numpy, pillow, simplejpeg, av, onnxruntime (background removal), pilgram2 filters.
- Hardware: gphoto2, linuxpy (V4L), gpiozero, pyserial (WLED), wigglecam (`pyproject.toml` `dependencies`).
- Tests: pytest + pytest-asyncio + pytest-httpserver + pytest-benchmark + pytest-cov (`[dependency-groups] dev`).
- Quality: **ruff** (line length 150; rules E, W, F, B, UP, I) and **basedpyright** standard mode (`[tool.ruff]`, `[tool.basedpyright]`).
- CI: one workflow, `.github/workflows/ci.yml` — job `gate` (test-layer guard, TDD gate, script tests, agent lint, basedpyright, ruff, unit tests), then job `desktop-tests` (OS matrix). No deploy, no PyPI publish. Desktop packaging/installers: not built yet. Docker image (inherited): `Dockerfile` (`uv run photobooth`, port 8000).

## Layers

- Entry point: `photobooth = photobooth.__main__:main` (`pyproject.toml` `[project.scripts]`); `main()` runs migrations, starts the container, then uvicorn (`src/photobooth/__main__.py`).
- App factory: `src/photobooth/application.py` `_create_app()` — routers `api`, `api_admin`, `media`, `static`, `userdata`; mounts `/sharepage/` and the SPA at `/`.
- Routers: `src/photobooth/routers/api/` (prefix `/api`, **unauthenticated**) and `src/photobooth/routers/api_admin/` (prefix `/api/admin`, every sub-router except `auth` behind `Depends(get_current_active_user)`, `src/photobooth/routers/api_admin/__init__.py`).
- Services: classes extending `BaseService` (`src/photobooth/services/base.py`), hand-wired in `src/photobooth/container.py` `Container` and started/stopped in definition order.
- Camera backends: `src/photobooth/services/backends/`, loaded dynamically by backend type (`src/photobooth/services/acquisition.py`).
- Config: `AppConfig` groups under `src/photobooth/services/config/`; plugins carry their own config files.
- Plugins: pluggy hookspecs in `src/photobooth/plugins/__init__.py`; bundled plugins registered under `[project.entry-points.photobooth11]`; user plugins load from `./plugins/` in the working directory.
- Database: `src/photobooth/database/` (`models.py`, `schemas.py`, `alembic/`).

## Coding conventions

- `uv run poe lint` (basedpyright + `ruff check` + `ruff format --check`) and `uv run poe format` (`pyproject.toml` `[tool.poe.tasks]`).
- Full tests: `uv run poe test`; targeted: `uv run pytest --basetemp=./tests_tmp/ <path>::<test>`. Tests write runtime folders into the working directory: run them from the repository root.
- Routers stay thin; logic lives in services reached through `container`.
- Settings belong in a config group with a default and validation; env overrides use the `__` nested delimiter (`src/photobooth/services/config/baseconfig.py` `env_nested_delimiter`).
- Comments explain why, never what.

## Database rules

- SQLite at `./database/database.sqlite`, created on demand (`src/photobooth/__init__.py` `DATABASE_PATH`, `src/photobooth/database/database.py`).
- `create_db_and_tables()` runs Alembic `upgrade head` at every app start; a pre-Alembic database is stamped `7e0d6dfb1b1d` first (`src/photobooth/database/database.py`). **Migrations therefore run unattended on every installed photobooth.**
- `Mediaitem.revision` is incremented by a `before_update` listener and `Cacheditem.revision` must match it for a cached image to be valid (`src/photobooth/database/models.py`).
- Migrations are additive, backward compatible and reversible; destructive operations only with explicit repo-owner approval — canonical rule `docs/ai/planning.md` "Migrations".

## Config and runtime rules

- Importing `photobooth` creates `./database`, `./media`, `./userdata`, `./config`, `./log`, `./tmp` and more in the current working directory, plus a demoassets link (`src/photobooth/__init__.py` `_create_basic_folders`). These folders are gitignored (`.gitignore`).
- Config source order is init → `./config/config.json` → dotenv → environment → secrets, so the JSON file beats environment variables (`src/photobooth/services/config/baseconfig.py` `settings_customise_sources`).
- Admin login: single user `admin`, password `common.admin_password` (default `0000`, `src/photobooth/services/config/groups/common.py`); JWT issued by `src/photobooth/routers/auth_dependencies_bearer.py`.

## How agents operate

- Follow `AGENTS.md`: route → plan → approve → worktree → RED → build → validate → handoff.
- Worktree per task: `scripts/new-task-worktree.sh <fix|feat|enhancement|refactor|perf|infra> <short-name>` (branch `<type>/no-ticket-<short-name>` from `origin/main`; the worktree lands in the gitignored .claude/worktrees folder). Then `uv venv --system-site-packages && uv sync` inside it.
- **Never commit to `main`. Always a PR.** The only long-lived branch is `main` (`git ls-remote --heads origin`). Open PRs with `gh pr create --repo OwlRepo/pick-a-booth --base main` — without `--repo`, `gh` targets the upstream parent of a fork. Merge with "Create a merge commit". Full rules: `docs/ai/handoff.md`.
- Branch protection is **not** enabled on `main` (GitHub API: "Branch not protected"). Check CI by hand with `gh pr checks <number>` before any merge.
- PR titles and bodies are English, plain language for a non-technical reviewer, filled into `.github/pull_request_template.md` (our own template) with the evidence in `docs/ai/pr-evidence.md`.
- Persona definitions: edit `agents/src/`, then `uv run poe agents:generate`; never edit `.claude/agents/` by hand. Claude Code is the only agent runtime used in this repository.

## Don't

- Don't add dependencies without approval; never regenerate `uv.lock` from scratch.
- Don't add import-time side effects or new global singletons.
- Don't hand-edit the hashed files in `src/web/frontend/assets/`; replace the bundle from a photobooth-frontend build.
- Don't commit credentials: `.env*` is gitignored, `src/web/shareondemand/api.php` ships a placeholder key, and `.vscode/sftp.json` must never gain secrets.
- Don't add workflows besides `.github/workflows/ci.yml` without a plan; keep one gate so a green run has one meaning.
- Don't reimplement helpers that exist in `src/photobooth/utils/` or a service — search with graphify first (`/graphify query`), grep only if graphify cannot answer.
