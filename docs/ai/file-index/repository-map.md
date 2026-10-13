# Repository Map

> Purpose: exact paths and lines for the symbols agents reach for most, so nobody greps blind.
> Load rule: check here (and graphify) before searching (entry-point step 10).
> Source of truth: the code. Every entry was verified on 2026-10-13 against `origin/main` `e2db0d33`. A stale entry is `CONTEXT DRIFT`: fix it in the same change.

Format: `` `symbol` -> `path:line` — purpose ``.

## Startup and wiring

- `main` -> `src/photobooth/__main__.py:25` — CLI entry: migrations, `container.start()`, uvicorn.
- `_create_basic_folders` -> `src/photobooth/__init__.py:30` — creates runtime folders in the working directory at import.
- `_create_app` -> `src/photobooth/application.py:59` — FastAPI factory: routers, static mounts, lifespan.
- `app` -> `src/photobooth/application.py:106` — module-level app instance.
- `Container` -> `src/photobooth/container.py:20` — hand-wired services; start/stop/reload.
- `container` -> `src/photobooth/container.py:94` — global container instance.

## Configuration

- `appconfig` -> `src/photobooth/appconfig.py:11` — global `AppConfig` instance.
- `AppConfig` -> `src/photobooth/services/config/appconfig_.py:26` — top-level config groups.
- `BaseConfig` -> `src/photobooth/services/config/baseconfig.py:19` — pydantic-settings base (env `__` delimiter, env files).
- `BaseConfig.settings_customise_sources` -> `src/photobooth/services/config/baseconfig.py:31` — source order (JSON beats env).
- `ConfigurationService` -> `src/photobooth/services/configuration.py:12` — read/patch/reset configurables for the admin API.

## Services

- `BaseService` -> `src/photobooth/services/base.py:24` — base class for every service (status, start/stop).
- `AcquisitionService` -> `src/photobooth/services/acquisition.py:21` — camera backends, preview, stills.
- `AcquisitionService._import_backend` -> `src/photobooth/services/acquisition.py:165` — dynamic backend import by type.
- `AbstractBackend` -> `src/photobooth/services/backends/abstractbackend.py:250` — camera backend contract.
- `ProcessingService` -> `src/photobooth/services/processing.py:92` — runs capture jobs through the state machine.
- `ActionType` -> `src/photobooth/services/processing.py:33` — `image | collage | animation | video | multicamera`.
- `ProcessingMachine` -> `src/photobooth/services/processor/machine/processingmachine.py:8` — job state machine.
- `Pipeline` -> `src/photobooth/services/mediaprocessing/pipeline.py:49` — step pipeline for media processing.
- `MediacollectionService` -> `src/photobooth/services/collection.py:27` — media items: files, DB rows, cache.
- `ShareService` -> `src/photobooth/services/share.py:22` — share/print actions and limits.
- `GpioService` -> `src/photobooth/services/gpio.py:126` — GPIO buttons and triggers.
- `SystemService` -> `src/photobooth/services/system.py:24` — systemd service control.
- `PluginManagerService` -> `src/photobooth/services/pluginmanager.py:13` — plugin lifecycle.
- `SseService` -> `src/photobooth/services/sse/sse_.py:188` — server-sent events to the UI.

## Plugins

- `pm` -> `src/photobooth/plugins/__init__.py:21` — the pluggy `PluginManager`.
- `PluginManagementSpec` -> `src/photobooth/plugins/__init__.py:26` — first of the hookspec classes (statemachine, acquisition, mediaprocessing, mediacollection follow).
- `BasePlugin` -> `src/photobooth/plugins/base_plugin.py:11` — base class for plugins with config.

## Database

- `create_db_and_tables` -> `src/photobooth/database/database.py:25` — Alembic stamp/upgrade at start.
- `Mediaitem` -> `src/photobooth/database/models.py:34` — media item model.
- `increment_revision` -> `src/photobooth/database/models.py:59` — `before_update` listener bumping `Mediaitem.revision`.
- `Cacheditem` -> `src/photobooth/database/models.py:63` — cached derivative model.
- `MediaitemPublic` -> `src/photobooth/database/schemas.py:26` — API read model.

## Routers and auth

- `router` (api) -> `src/photobooth/routers/api/__init__.py:20` — unauthenticated `/api`.
- `router` (api_admin) -> `src/photobooth/routers/api_admin/__init__.py:18` — `/api/admin` with JWT dependency per sub-router.
- `authenticate_user` -> `src/photobooth/routers/auth_dependencies_bearer.py:63` — admin password check.
- `get_current_active_user` -> `src/photobooth/routers/auth_dependencies_bearer.py:101` — admin auth dependency.

## Utils

- `filenames_sanitize` -> `src/photobooth/utils/helper.py:24` — resolve a path and keep it inside a base dir.
- `is_rpi` -> `src/photobooth/utils/helper.py:46` — Raspberry Pi detection (used by hardware tests).

## Tests

- `client` -> `src/tests/tests/conftest.py:23` — TestClient on `/api/` with the container started.
- `client_authenticated` -> `src/tests/tests/conftest.py:34` — client with an admin bearer token.

## Workflow & Agent Tooling

- `classify_changes` / `judge_red` / `find_bash_write_targets` -> `scripts/ci/tdd_lib.py` — TDD rules shared by gate, red and hook.
- `run_test_files` -> `scripts/ci/tdd_runner.py` — pytest runner with junit parsing.
- `main` -> `scripts/ci/tdd_red.py` — `uv run poe tdd:red`.
- `main` -> `scripts/ci/tdd_gate.py` — `uv run poe tdd:gate` (CI `.github/workflows/ci.yml`).
- `problems_for` / `main` -> `scripts/ci/check_test_layers.py` — per-commit test-layer guard, `uv run poe ci:layers`.
- `main` -> `scripts/hooks/tdd_red_guard.py` — Claude PreToolUse hook (`.claude/settings.json`).
- `GLOBAL_POLICY` / `check` -> `scripts/generate_agent_defs.py` — persona generator (Claude Code only) and `agents:lint`.
- `scripts/new-task-worktree.sh` — fresh task worktree from `origin/main`.
- `graphify-out/graph.json` — the knowledge graph used for discovery (flow node K).

## Maintenance Rules

1. Check this index (and graphify) before searching. A stale entry is `CONTEXT DRIFT`; fix it in the same turn.
2. A new or moved significant symbol gets an entry in the same change.
3. After a green targeted test pass, refresh the changed files' entries only — never a full re-index.
