# Template: Feature Plan

> Purpose: plan a new capability or enhancement end to end.
> When to use: new capability, enhancement, new route, backend, plugin or config (from `docs/ai/task-router.md`).
> Source of truth: this is a MAP of the process. The real code, contracts, and tests win.
> Deterministic implementation rule: expand this plan per `docs/ai/planning.md` and `docs/ai/plan-template.md`; every path, symbol, operation, dependency, test, acceptance mapping, and regression risk must be explicit.

Every plan opens with a TL;DR: plain English, lead with an analogy, add a tiny visualization when it helps.

Fill every section:

## TL;DR
Analogy-led, plain-English summary of what the feature does and how it fits.

## Feature Discovery
Existing patterns and helpers to reuse — Graphify FIRST (`/graphify query|path|explain`; grep only when Graphify cannot answer, naming the failed query — `docs/ai/planning.md` "Graphify is the discovery tool"). Candidates: the services wired in `src/photobooth/container.py`, `BaseService` (`src/photobooth/services/base.py`), config groups in `src/photobooth/services/config/groups/`, pluggy hooks in `src/photobooth/plugins/__init__.py`, helpers in `src/photobooth/utils/`, and the media pipeline in `src/photobooth/services/mediaprocessing/`. Note what already exists so you do not duplicate it.

## Data / Contract Changes
Pydantic request/response models, config fields (with defaults and validation), hook signatures, DB changes (with the migration rules in `docs/ai/contracts/db-contracts.md`). If a schema/permission/contract is unverified, mark `UNVERIFIED DEPENDENCY` and stop.

## Files To Create / Change
Exact paths. New admin capabilities go under `src/photobooth/routers/api_admin/`; nothing destructive goes into the unauthenticated `/api` router.

## Tests First
The pytest files and `test_error_*` > `test_edge_*` > `test_regression_*` > `test_happy_*` cases you will write before implementing, recorded with `uv run poe tdd:red`.

## Steps
Ordered implementation steps.

## Verification
`uv run poe lint`, targeted pytest, `uv run poe test`, and live verification where the change is user-visible or hardware-facing.

## QA Gate
`/qa` for user-visible changes; the five-bucket sweep for backend-only (`docs/ai/testing-strategy.md`). Mandatory for MEDIUM and LARGE.

## docs/ai Sync
Which `docs/ai/*` entries and `docs/ai/file-index/repository-map.md` symbols you will update in this same change.
