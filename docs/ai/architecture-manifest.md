# Architecture Manifest

> Purpose: the shape of the system — stack, layout, request/data flow, external services.
> Load rule: read when a task needs the big picture (entry-point step 3).
> Source of truth: this is a MAP. `pyproject.toml`, `src/photobooth/application.py`, `src/photobooth/container.py` and the code win. If a map conflicts with code, code wins.

## Stack

Python ≥3.11, FastAPI + uvicorn, pydantic v2 + pydantic-settings, SQLAlchemy 2 + Alembic on SQLite, pluggy, python-statemachine, opencv/numpy/pillow/av/onnxruntime for imaging, gphoto2/linuxpy/gpiozero/pyserial for hardware. uv for environments and builds, poe for tasks, pytest, ruff, basedpyright. Versions: `pyproject.toml` and `uv.lock`. Full list with evidence: `CLAUDE.md` "Tech stack".

## Repo Layout

| Path | What |
|---|---|
| `src/photobooth/__main__.py` | CLI entry (`photobooth`): migrations → `container.start()` → uvicorn |
| `src/photobooth/application.py` | FastAPI app factory, router includes, static mounts, lifespan |
| `src/photobooth/container.py` | hand-wired service container (start/stop/reload) |
| `src/photobooth/appconfig.py` | global `appconfig` instance |
| `src/photobooth/routers/` | `api/` (unauthenticated), `api_admin/` (JWT), media/userdata/static routers |
| `src/photobooth/services/` | services, camera `backends/`, `config/`, `mediacollection/`, `mediaprocessing/`, `processor/`, `sse/` |
| `src/photobooth/plugins/` | pluggy hookspecs and bundled plugins (commander, filter_pilgram2, gpio_lights, synchronizer, wled) |
| `src/photobooth/database/` | engine + migration runner, models, Pydantic schemas, `alembic/` |
| `src/photobooth/utils/` | shared helpers (resizing, encoding, timers, resilient services, rembg, calibration) |
| `frontend/` | kiosk/admin UI source (Vue3/Quasar/TypeScript, npm), git subtree of photobooth-frontend; builds into `src/web/frontend/` |
| `src/web/` | frontend build output, sharepage, PHP shareondemand endpoint |
| `src/tests/` | `tests/` (pytest suite) and `benchmarks/` |
| `scripts/` | AI workflow tooling (TDD gate/guard, persona generator, worktree script) |
| `.github/workflows/` | lint, tests, benchmarks, PyPI publish (upstream-only), `ai-gates`, `frontend` |

## Request and data flow

1. The kiosk UI (served from `src/web/frontend/` at `/`) calls `/api/*` and listens to server-sent events at `/api/sse`.
2. Routers call services through `container`; actions (`/api/actions/{action_type}/{index}`) start the processing state machine (`src/photobooth/services/processor/machine/processingmachine.py`).
3. `AcquisitionService` drives the configured camera backends (`src/photobooth/services/backends/`) for live preview (`/api/aquisition/stream.mjpg`) and stills.
4. Captures run through the media-processing pipelines (`src/photobooth/services/mediaprocessing/`) and are stored by `MediacollectionService` (files under `./media/`, rows in SQLite, cached derivatives in `cacheditems`).
5. Plugins observe and extend each stage through pluggy hooks (`src/photobooth/plugins/__init__.py`); WLED/GPIO signal countdowns, the synchronizer uploads media, the commander runs configured commands.
6. Share actions print or hand media to share-on-demand (`src/web/shareondemand/api.php` on a user's web host) and rclone remotes.

## Storage

All runtime state lives in the working directory: `./config/` (JSON config), `./database/` (SQLite), `./media/`, `./userdata/`, `./log/`, `./tmp/`, `./cache/`, `./recycle/`, and user `./plugins/` (`src/photobooth/__init__.py`).

## External services and hardware

- Cameras: gphoto2 DSLRs, digiCamControl (Windows, HTTP), picamera2, V4L/PyAV webcams, wigglecam multicamera, virtual camera.
- GPIO buttons/lights (gpiozero), WLED over serial, printers via configured commands.
- Share-on-demand PHP endpoint and rclone remotes for uploads.
- No telemetry service; logs go to `./log/` and the UI log stream.

## Deployment

Users install from PyPI or run the `Dockerfile`; a systemd unit ships in `src/photobooth/scripts/systemservice/`. The fork itself publishes nothing (`.github/workflows/cicd.yml` is upstream-owner-gated).
