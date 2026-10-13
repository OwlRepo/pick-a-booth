# Development Environment

> Purpose: where development, manual QA and live checks actually run.
> Load rule: read before any live verification or when setting up a worktree.
> Source of truth: `CONTRIBUTING.md`, `pyproject.toml`, `Dockerfile`, and `src/photobooth/__init__.py` beat this map.

## There is no shared DEV server

The fork has no deployment, no staging, and no hosted environment. Everything runs
locally in the task worktree. Real photobooth installations belong to their
owners; never point a test or migration at one.

## Setup (per worktree)

```bash
uv venv --system-site-packages   # system packages give access to libcamera/picamera2 on a Raspberry Pi
uv sync                          # installs the locked dependencies incl. the dev group
```

Source: `CONTRIBUTING.md` "Setting Up the Repo". System libraries used by CI:
`libturbojpeg`, `libgl1`, `libcap-dev`, `ffmpeg`, `rclone` (`.github/workflows/pytests.yml`).
On macOS, `linuxpy` (V4L) and the Raspberry Pi camera stack are unavailable, so those
backends and their type checks do not resolve locally.

## Run the app

```bash
uv run photobooth                 # http://localhost:8000/ , API docs at /api/doc
```

- Entry: `src/photobooth/__main__.py` (`--host`, `--port`).
- Importing `photobooth` creates `./database`, `./media`, `./userdata`, `./config`, `./log`, `./tmp`, `./cache`, `./recycle` in the working directory (`src/photobooth/__init__.py`). Run from the worktree root; these folders are gitignored.
- Admin UI login: user `admin`, password from `common.admin_password` (default `0000`, `src/photobooth/services/config/groups/common.py`). The repo owner types credentials during live checks.
- No camera attached: select the VirtualCamera backend in the admin config (`src/photobooth/services/backends/virtualcamera.py`).
- Docker alternative: `Dockerfile` (`uv run photobooth`, port 8000).

## Frontend (Node)

The kiosk/admin UI source is in `frontend/` (Vue3/Quasar/TypeScript, npm), a git subtree of upstream photobooth-frontend. Needs Node 22 or newer.

```bash
cd frontend
npm ci                           # install the locked dependencies
npm run dev                      # dev server with hot reload; proxies /api, /media, /userdata to 127.0.0.1:8000
npm run lint:check && npm run typecheck && npm run test   # same checks as .github/workflows/frontend.yml
npm run build                    # writes the bundle into src/web/frontend/
```

- `npm run dev` needs the backend: run `uv run photobooth` from the worktree root alongside it.
- Run `npm run build` before committing a UI change; the app serves the committed bundle, not the source. Never hand-edit the hashed files in `src/web/frontend/assets/`.
- Pull upstream: `git subtree pull --prefix=frontend https://github.com/photobooth-app/photobooth-frontend.git main --squash`.

## Database and migrations

SQLite at `./database/database.sqlite`; `create_db_and_tables()` applies Alembic migrations at every start (`src/photobooth/database/database.py`). To test a migration against old data, copy a database from a previous release into a scratch working directory — never a production photobooth's live file.

## Hardware

Hardware tests self-skip without the device (`src/tests/tests/backends/`, `src/tests/tests/plugins/test_wled.py`). The upstream project runs them on a self-hosted Raspberry Pi runner that does not run for this fork (`.github/workflows/pytests.yml` `tests-hardware-rpi`). Hardware checks for this fork are manual: name the device and what was verified.

## Mock data

Use the bundled demo assets (`src/photobooth/demoassets/`) and the test fixtures in `src/tests/tests/conftest.py`. Data created during a live check stays in the worktree's runtime folders and is deleted with the worktree.
