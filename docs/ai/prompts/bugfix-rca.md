# Template: Bugfix RCA

> Purpose: root-cause a bug BEFORE writing any code.
> When to use: any bug, error, regression, crash, failing test, or broken behavior (from `docs/ai/task-router.md`).
> Source of truth: this is a MAP of the process. The real code proves the root cause. If a map conflicts with code, code wins.

Rule: produce the RCA with NO code, then STOP and wait for approval. Do not propose the fix as edits; only a direction.

Fill every section:

## Issue Selected
Which reported issue/behavior this RCA addresses.

## Bug Summary
One or two lines: observed vs expected.

## Reproduction Flow From Code
The exact path through the code that produces the bug (files + functions + lines), not a guess. Include the request route, service, backend or plugin hook involved.

## Layer Investigation
What the UI/API caller does, what the router does, and what the service/backend/plugin does, separately. Note whether hardware, threads, or config state are involved.

## Contract Check
Where the layers agree or disagree (request/response models, config schema, DB shape, hook signatures, thread/stop assumptions).

## Root Cause
The single underlying cause, stated precisely, with the evidence for it and the observation that would disprove it.

## Why Existing Code Allows The Bug
The missing guard, wrong assumption, or gap that lets it happen.

## Eliminated Causes
Plausible causes you ruled out, with why.

## Remaining Uncertainties
What you could not fully verify (for example: only reproducible on specific hardware).

## Confidence Level
High / Medium / Low, with a one-line justification.

## Basic Solution Direction
The shape of the fix (not the diff). Stop here and wait for approval.
