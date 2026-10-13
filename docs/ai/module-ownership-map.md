# Module Ownership Map

> Purpose: which layer owns what, where its tests live, and its default risk. Domain values for `docs/ai/task-router.md` come from the first column.
> Load rule: read before planning any change (entry-point step 4).
> Source of truth: this is a MAP. The code wins. Persona ownership globs: `docs/ai/agent-orchestration.md`.

| Domain | Code | Owner persona | Tests | Default risk | Notes |
|---|---|---|---|---|---|
| `api` | `src/photobooth/routers/api/` | fastapi-backend-dev | `src/tests/tests/router/api/` | Standard; Deep for destructive or system routes | unauthenticated by design |
| `admin-api` | `src/photobooth/routers/api_admin/`, `src/photobooth/routers/auth_dependencies_bearer.py` | fastapi-backend-dev | `src/tests/tests/router/api_admin/`, `src/tests/tests/router/test_authentication.py` | Deep | JWT admin boundary |
| `media-routes` | `src/photobooth/routers/media.py`, `src/photobooth/routers/userdata.py`, `src/photobooth/routers/static.py` | fastapi-backend-dev | `src/tests/tests/router/` | Deep | file serving, path handling |
| `acquisition` | `src/photobooth/services/acquisition.py`, `src/photobooth/services/backends/` | fastapi-backend-dev | `src/tests/tests/services/test_acquisition.py`, `src/tests/tests/backends/` | Deep | hardware, threads |
| `processing` | `src/photobooth/services/processing.py`, `src/photobooth/services/processor/`, `src/photobooth/services/mediaprocessing/` | fastapi-backend-dev | `src/tests/tests/services/test_processing.py`, `src/tests/tests/mediaprocessing/` | Standard | state machine, pipelines |
| `collection` | `src/photobooth/services/collection.py`, `src/photobooth/services/mediacollection/` | fastapi-backend-dev | `src/tests/tests/services/test_collection.py` | Standard; Deep when deleting media | media files + DB rows + cache |
| `config` | `src/photobooth/services/config/`, `src/photobooth/services/configuration.py`, `src/photobooth/appconfig.py` | fastapi-backend-dev (appconfig.py: assigned at contract lock) | `src/tests/tests/services/test_config.py`, `src/tests/tests/test_appconfig.py` | Deep | field names persist in users' `config.json` |
| `share` | `src/photobooth/services/share.py`, `src/web/shareondemand/` | fastapi-backend-dev / web-frontend-dev | `src/tests/tests/services/test_share.py`, `src/tests/tests/plugins/test_synchronizer_shareondemand.py` | Deep | credentials, external hosts |
| `plugins` | `src/photobooth/plugins/` | fastapi-backend-dev | `src/tests/tests/plugins/` | Deep for hookspecs, Standard for one plugin | third-party plugin contract |
| `gpio` | `src/photobooth/services/gpio.py` | fastapi-backend-dev | `src/tests/tests/services/test_gpio.py` | Deep | hardware |
| `system` | `src/photobooth/services/system.py`, `src/photobooth/routers/api/system.py` | fastapi-backend-dev | `src/tests/tests/services/test_system.py`, `src/tests/tests/router/api/test_system.py` | Deep | reboot/shutdown/systemd |
| `database` | `src/photobooth/database/` | db-architect (models, migrations), fastapi-backend-dev (`schemas.py`) | `src/tests/tests/services/test_collection.py` | Deep | migrations run unattended at start |
| `app-core` | `src/photobooth/application.py`, `src/photobooth/container.py`, `src/photobooth/__init__.py`, `src/photobooth/__main__.py` | assigned at contract lock | `src/tests/tests/test_application.py`, `src/tests/tests/test_container.py`, `src/tests/tests/test_init.py`, `src/tests/tests/test_main.py` | Deep | startup, import side effects |
| `utils` | `src/photobooth/utils/` | fastapi-backend-dev | `src/tests/tests/utils/` | Standard | shared helpers |
| `web` | `frontend/`, `src/web/frontend/`, `src/web/sharepage/` | web-frontend-dev | `frontend/src/**/*.spec.ts` (vitest) + live verification | Standard | `frontend/` is a git subtree of photobooth-frontend; `src/web/frontend/` is its build output |
| `tooling` | `scripts/`, `agents/src/`, `.github/workflows/`, `docs/ai/`, `.ai-engineering/` | assigned at contract lock | `scripts/tests/` | Standard; Deep for CI gates | AI workflow layer |

## Default Deep Domains

Admin auth, the unauthenticated API surface, config persistence, file serving, migrations, plugin hookspecs, camera backends and GPIO, system commands, and share/sync credentials are Deep regardless of the request size (`docs/ai/task-router.md` "Ambiguity Rule").
