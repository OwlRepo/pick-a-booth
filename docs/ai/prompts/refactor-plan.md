# Template: Refactor Plan

> Purpose: restructure code without changing behavior.
> When to use: cleanup, rename, or restructure with no behavior change (from `docs/ai/task-router.md`).
> Source of truth: this is a MAP of the process. The real code and tests win.
> Deterministic implementation rule: expand this plan per `docs/ai/planning.md` and `docs/ai/plan-template.md`; every path, symbol, operation, dependency, test, acceptance mapping, and regression risk must be explicit.

Every plan opens with a TL;DR: plain English, lead with an analogy, add a tiny visualization when it helps.

Required analysis before planning: the current structural problem with evidence (duplication, coupling, complexity, or maintainability issues), and whether the refactor is actually necessary for the requested outcome. Upstream-sync cost counts: a refactor of upstream code makes every future photobooth-app merge harder.

Fill every section:

## TL;DR
Analogy-led, plain-English summary of what is being reshaped and why.

## Behavior-Preservation Statement
Explicit promise that observable behavior does not change, and how you will prove it.

## Scope
Exact files in scope. Nothing outside this list changes.

## Characterization Tests First
The pytest cases that pin current behavior BEFORE the refactor, so a green suite proves nothing changed. In the PR, declare `TDD-Waiver: refactor <reason>` so the CI gate requires these tests to PASS against the base.

## Steps
Ordered, small, reversible steps.

## Verification
Same behavior, tests green: targeted pytest, `uv run poe lint`, `uv run poe test`.

## Explicitly NOT Changing
Public API routes and models, config field names (they persist in users' `config.json`), plugin hookspecs, DB schema, and any file outside Scope. If a rename touches one of these, stop and discuss first.
