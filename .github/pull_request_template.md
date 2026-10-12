<!-- Plain language first: the reviewer may not be technical. English only. No emojis. -->

## Summary

<!-- 2-4 plain sentences: what problem there was and what this change does. -->

## What changes

-

## How to test

1.

<!-- Technical evidence below, per docs/ai/pr-evidence.md. CI (layer guard, TDD gate, script tests, agent lint, type-check, lint, unit tests, desktop OS matrix) runs on its own; this section covers what CI cannot see. -->

## Change Type

<!-- One or more: UI / user-facing · Backend / API · Database · Hardware · Bug fix · Refactor · Performance · Infrastructure -->

-

## Evidence

<!-- What docs/ai/pr-evidence.md requires for the Change Type(s) above. -->

## Testing

- Commands executed:
- Tests passed:
- Manual verification performed (device / OS):
- Important cases covered:

## TDD evidence

- Test Matrix (layer | required / not required | file):
- RED run (`uv run poe tdd:red` output from before implementing):
- Waivers, one per line, only if used (the CI `tdd:gate` reads these lines):
  <!-- TDD-Waiver: <reason> -->
  <!-- Migration-Waiver: <reason> -->

## Risk

- Possible regressions:
- Backward-compatibility concerns (API, config files, databases on installed copies):
- Security impact:

## Rollback

- Exact steps to revert safely:
