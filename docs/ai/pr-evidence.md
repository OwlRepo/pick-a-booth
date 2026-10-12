# Mandatory Pull Request Evidence

> Purpose: what evidence a PR must carry before it's ready for review, by change type.
> Load rule: read before creating any PR — pointed to from `docs/ai/handoff.md`'s Integration sequence.
> Source of truth: this is a MAP. Where it asks for facts already governed elsewhere (migrations, tests, refactor safety, performance), that governing doc wins — this file only requires reporting those facts in the PR body.

A PR is not complete until its evidence matches its Change Type below and has actually been produced — never claimed without having been run.

## Change Type

One or more of: `UI / user-facing` · `Backend / API` · `Database` · `Hardware` · `Bug fix` · `Refactor` · `Performance` · `Infrastructure`.

This is a reviewer-facing tag on the diff, distinct from the routing `Classification` in `docs/ai/task-router.md` (that one answers why the task started; this one answers what the diff looks like).

## Evidence by Change Type

### 1. UI / user-facing

Triggers: a new frontend bundle, sharepage changes, or backend changes with visible effect in the kiosk/admin UI.

Attach a short screen recording of the live flow (`docs/ai/testing-strategy.md` "Live verification"): starting state, user actions, completed result, and relevant error states. GitHub has no API to attach a video to a PR body; hand the file to the repo owner to attach and open the PR as a draft (`gh pr create --draft`) until it is attached, stating the exact file path.

### 2. Backend, API, database, or logic-only

Skip the recording unless the change has meaningful user-visible behavior. Include instead:

- The exact previous behavior and the exact new behavior.
- Tests added/updated, the exact command run, and the result.
- Example request/response for API changes (path, method, status, body).
- Relevant logs or output when useful.
- Migration details when applicable — the facts required by `docs/ai/planning.md` "Migrations (canonical rule)".
- Known risks and rollback steps.

### 3. Hardware

Which hardware paths are covered by mocks or self-skipping tests, and which were checked by hand on which device (camera model, Raspberry Pi model, OS). An unverified hardware path is stated as unverified.

### 4. Bug fixes without meaningful UI change

A regression test that fails before the fix and passes after it (`docs/ai/testing-strategy.md` "Strict TDD"). State how the bug was reproduced, the root cause, why the fix resolves it, and which test prevents recurrence.

### 5. Refactors

No recording. Report the results of `docs/ai/prompts/refactor-plan.md` "Behavior-Preservation Statement" and "Characterization Tests First": what changed, why, confirmation that behavior did not change, the covering tests, and any gain or new risk.

### 6. Database migrations

Purpose, schema changes, backfill behavior, reversibility (`downgrade()`), effect on existing photobooth databases (migrations run unattended at app start), compatibility of the old code with the new schema and of the new code with the old schema, and the migration test output.

### 7. Performance changes

The fields required by `docs/ai/task-router.md` `PERFORMANCE`: measured baseline, result after the change, method, environment, metrics, tradeoffs. No claimed improvement without measurement.

## Required PR structure

PR title and body are in English, in plain language a non-technical reviewer can follow, with no AI co-author trailer in the PR text. Fill every section of `.github/pull_request_template.md`: Summary, What changes, How to test, Change Type, Evidence (from the section above), Testing, TDD evidence (Test Matrix, the `uv run poe tdd:red` RED output, and any `TDD-Waiver:` / `Migration-Waiver:` lines, each on its own line — the CI `tdd:gate` reads them from the body), Risk, and Rollback. Delete a section's placeholder comment once it is filled; never delete the section.

## Mandatory rules

- Do not claim a test passed without having run it.
- Never use a recording as a replacement for an automated test where one is possible.
- Never expose secrets or private data in PR evidence.
- Do not mark a PR ready for review until its evidence matches its Change Type.
- If required evidence cannot be produced, leave the PR as a draft and report the exact blocker.
