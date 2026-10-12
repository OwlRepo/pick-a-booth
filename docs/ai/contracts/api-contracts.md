# API Contracts

> Purpose: the HTTP surface the kiosk UI, admin UI and external callers depend on.
> Load rule: read before changing any route, request/response model, or SSE event (entry-point step 6).
> Source of truth: the routers in `src/photobooth/routers/` and the OpenAPI document a running app serves at `/api/openapi.json` (docs UI at `/api/doc`). Bodies stay `TODO` here until read from code; never transcribe them from memory.

## Auth model

- `/api/*` — no authentication (`src/photobooth/routers/api/__init__.py`).
- `/api/admin/*` — `POST /api/admin/auth/token` (OAuth2 password flow, user `admin`) issues a JWT; every other admin router is included with `Depends(get_current_active_user)` (`src/photobooth/routers/api_admin/__init__.py`).
- `/media`, `/userdata`, `/private.css`, `/` and `/sharepage/` are served without auth (`src/photobooth/application.py`).

## Route groups

| Route group | File | Purpose (one line) | Bodies |
|---|---|---|---|
| `/api/actions` | `src/photobooth/routers/api/actions.py` | trigger a configured action (image, collage, animation, video, multicamera) | TODO |
| `/api/aquisition` | `src/photobooth/routers/api/acquisition.py` | MJPEG preview stream, stills, multicam files, backend mode | TODO |
| `/api/config` | `src/photobooth/routers/api/config.py` | public `AppConfig` without secrets | `AppConfig` |
| `/api/debug` | `src/photobooth/routers/api/debug.py` | latest log file | TODO |
| `/api/filter` | `src/photobooth/routers/api/filter.py` | list filters, preview and apply a filter to a media item | TODO |
| `/api/mediacollection` | `src/photobooth/routers/api/mediacollection.py` | list/get/delete media items | `MediaitemPublic` |
| `/api/processing` | `src/photobooth/routers/api/processing.py` | approval image, next/confirm/reject/abort the running job | TODO |
| `/api/share` | `src/photobooth/routers/api/share.py` | run share actions, download by id | TODO |
| `/api/sse` | `src/photobooth/routers/api/sse.py` | server-sent event stream (events in `src/photobooth/services/sse/sse_.py`) | `SseEventModel` |
| `/api/system` | `src/photobooth/routers/api/system.py` | reboot/shutdown host, reload services, systemctl control | TODO |
| `/api/admin/auth` | `src/photobooth/routers/api_admin/auth.py` | token, current user | `User` |
| `/api/admin/config` | `src/photobooth/routers/api_admin/config.py` | list, read, schema, patch, reset configurables | TODO |
| `/api/admin/enumerate` | `src/photobooth/routers/api_admin/enumerate.py` | serial ports, USB cameras, user files, rclone remotes | TODO |
| `/api/admin/files` | `src/photobooth/routers/api_admin/files.py` | browse, download, upload, create, delete, zip files | TODO |
| `/api/admin/information` | `src/photobooth/routers/api_admin/information.py` | reset statistics counters | — |
| `/api/admin/multicamera` | `src/photobooth/routers/api_admin/multicamera.py` | multicamera calibration | TODO |
| `/api/admin/share` | `src/photobooth/routers/api_admin/share.py` | reset share-limit counters | — |
| `/media` | `src/photobooth/routers/media.py` | media files and cached derivatives | TODO |
| `/userdata` | `src/photobooth/routers/userdata.py` | user-provided assets | TODO |

## Contract rules

- Response models are part of the contract: a field rename or removal breaks the vendored frontend bundle and third-party callers. Additive changes only, unless the plan coordinates a new frontend bundle.
- The path prefix `/api/aquisition` is misspelled upstream; it is part of the contract — do not "fix" it.
- New destructive, config-changing, or system-level routes go under `/api/admin`.
- SSE event shapes (`src/photobooth/services/sse/sse_.py`) are consumed by the frontend; treat them like response models.
