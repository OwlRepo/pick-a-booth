# DB Contracts

> Purpose: the data model and the rules every change to it follows.
> Load rule: read before touching models, schemas, or migrations (entry-point step 7).
> Source of truth: `src/photobooth/database/models.py` and `src/photobooth/database/alembic/versions/`. Do NOT hand-transcribe columns here; point to them.

## Engine

SQLite at `./database/database.sqlite`, `check_same_thread=False`, one engine per process (`src/photobooth/database/database.py`). Sessions are opened by the services that use them (`src/photobooth/services/mediacollection/`).

## Known tables (pointers)

- `usagestats` — `UsageStats`, PK `action`; counters per action (`src/photobooth/database/models.py`).
- `sharelimits` — `ShareLimits`, PK `action`; share quota counters.
- `mediaitems` — `Mediaitem`, UUID PK; one row per captured/processed item; `revision` incremented by the `before_update` listener; `pipeline_config` JSON.
- `cacheditems` — `Cacheditem`, FK to `mediaitems.id`; cached derivatives keyed by (mediaitem, dimension, processed); valid only while its `revision` equals the media item's.

Pydantic read models: `src/photobooth/database/schemas.py` (`MediaitemPublic`, `UsageStatsPublic`, `ShareLimitsPublic`).

## Migration chain

`src/photobooth/database/alembic/versions/`: `7e0d6dfb1b1d_initial_schema` → `24456e322528_add_captured_original_to_mediaitem` → `543b0c11a790_modify_fields_to_improve_cache_` (head at the time of writing; verify with the files).

A database created before Alembic existed is stamped `7e0d6dfb1b1d` and then upgraded (`src/photobooth/database/database.py`).

## Migration rules

Canonical: `docs/ai/planning.md` "Migrations". In short: additive, backward compatible, reversible, one linear chain, migration test required, destructive changes only with explicit repo-owner approval — because every installed photobooth applies migrations unattended at start.

## Traps

- Updating a `Mediaitem` bumps its `revision`; code that writes derivatives must store the matching revision or the cache is silently invalid.
- SQLite allows one writer at a time; long transactions in a request block the processing thread.
- Tests and the app both create `./database/` in the working directory: never run them where a real photobooth database lives.
