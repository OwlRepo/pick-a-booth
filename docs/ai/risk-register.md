# Risk Register

> Purpose: the areas where a small change can do large damage, and the checks each requires.
> Load rule: read before planning (entry-point step 9); reviewers and security-auditor check the matching row.
> Source of truth: this is a MAP. The code wins. Observed facts below cite the file; they describe upstream behavior, not decisions made by this fork.

## Register

| Risk area | Why risky | Default task size | Required checks | Manual QA | Notes |
|---|---|---|---|---|---|
| Unauthenticated `/api` surface | `src/photobooth/routers/api/__init__.py` mounts every `/api` router without auth. It includes `GET /api/system/host/{reboot\|shutdown}` and `/api/system/systemctl/{...}` (`src/photobooth/routers/api/system.py`), `DELETE /api/mediacollection/` (deletes all items, `src/photobooth/routers/api/mediacollection.py`) and `GET /api/debug/log/latest`. Anyone on the network can call them. | LARGE / Deep | security-auditor in the QA fan-out; new destructive or system routes go under `api_admin`; router tests for auth | yes, on the LAN setup | upstream design; changing it is a product decision for the repo owner |
| Admin auth | Plaintext password compare against `common.admin_password` (default `0000`); JWT HS256 signed with `misc.secret`, random per process unless persisted (`src/photobooth/routers/auth_dependencies_bearer.py`, `src/photobooth/services/config/groups/common.py`). | Deep | tests for 401 on every new admin route; no weakening of compare/expiry | login flow | |
| Migrations on user devices | `create_db_and_tables()` upgrades every installed photobooth at start; a failed migration stops the app (`src/photobooth/database/database.py`). | Deep | `docs/ai/planning.md` "Migrations"; migration test from previous head and empty DB; reversible `downgrade()` | upgrade a copy of an old DB | |
| Config persistence | Field names and types persist in users' `./config/config.json`; JSON beats env (`src/photobooth/services/config/baseconfig.py`). Renames or type changes break existing installs. | Deep | defaults for new fields; no renames without a migration path; config tests | load an old config file | |
| File serving and uploads | Media, userdata and admin file routes read/write paths derived from requests (`src/photobooth/routers/media.py`, `src/photobooth/routers/userdata.py`, `src/photobooth/routers/api_admin/files.py`). | Deep | path-traversal tests (reuse `filenames_sanitize` in `src/photobooth/utils/helper.py`) | — | |
| System commands | Reboot/shutdown commands come from config and run via `subprocess` (`src/photobooth/routers/api/system.py`); the commander plugin runs configured commands. | Deep | no `shell=True`; list args; timeouts | on a disposable machine only | |
| Camera backends and GPIO | Hardware calls block, hang or fail on unplug; threads must stop on `container.stop()`. | Deep | mock-based tests + named manual hardware check; timeouts | on the target device | hardware tests self-skip in CI |
| Plugin hookspecs | Third-party plugins implement the specs in `src/photobooth/plugins/__init__.py`; user plugins load from `./plugins/`. | Deep | signature compatibility; plugin tests | load a bundled plugin | |
| Share/sync credentials | Share-on-demand API key and rclone remotes; `src/web/shareondemand/api.php` ships the placeholder `changedefault!`. | Deep | never log or expose secrets; security-auditor | — | |
| Import-time side effects | Importing `photobooth` creates folders and a link in the working directory (`src/photobooth/__init__.py`). | Standard | run tests from the repo root; do not add more side effects | — | |
| CI gates | `.github/workflows/ci.yml` (layer guard, TDD gate, persona lint, tooling tests, type-check, lint, unit and desktop tests) can block every PR when broken. | Deep | `uv run poe test:scripts`; dry-run the gate locally | — | branch protection is off: checks are advisory unless read by hand |
| Upstream sync | The fork diverges into our desktop app; merging upstream photobooth-app now conflicts with our CI and docs. | Standard | merge upstream only by choice, in its own PR; keep `.github/` ours | — | |
| Dependency updates | Dependabot was removed with the upstream CI; nothing proposes dependency bumps. | Standard | check `uv run poe list_outdated` periodically; bump `uv.lock` in its own PR | — | |

## Default-Deep Rule

Touching any listed area defaults the task to Deep unless repository evidence proves the specific change is isolated and low-risk. When in doubt, stay Deep and get approval.

## Accepted / deferred risks

Record accepted risks here with date, owner, and reason. None yet.
