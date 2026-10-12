# Template: Bugfix Plan

> Purpose: turn an approved RCA into a concrete, testable fix.
> When to use: after a `docs/ai/prompts/bugfix-rca.md` is approved (from `docs/ai/task-router.md`).
> Source of truth: this is a MAP of the process. The real code and tests win.
> Deterministic implementation rule: expand this plan per `docs/ai/planning.md` and `docs/ai/plan-template.md`; every path, symbol, operation, dependency, test, acceptance mapping, and regression risk must be explicit.

Every plan opens with a TL;DR: plain English, lead with an analogy, add a tiny visualization when it helps.

Fill every section:

## TL;DR
Analogy-led, plain-English summary of the bug and the fix.

## Issue Selected
The issue this plan fixes.

## Root Cause Recap
One or two lines from the approved RCA.

## Files To Change
Exact paths (and functions) that will change.

## Failing Test First
The pytest case(s) you will write first that fail because of the bug, named `test_regression_*` (plus any `test_error_*` / `test_edge_*` the RCA exposed), in `src/tests/tests/<area>/test_<module>.py`, and what each asserts. Recorded with `uv run poe tdd:red`.

## Implementation Steps
Ordered, minimal steps to make the tests pass without unrelated changes.

## Verification
`uv run pytest --basetemp=./tests_tmp/ <files>`, `uv run poe lint`, `uv run poe test`, plus live verification for user-visible or hardware-facing bugs (`docs/ai/testing-strategy.md` "Live verification").

## Rollback / Risk
How to revert, and any residual risk (user data, migrations, hardware, unauthenticated API surface).
