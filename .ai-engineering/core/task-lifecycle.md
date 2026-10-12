# Task Lifecycle

Canonical transitions:

NEW → TRIAGED → ANALYZING → PLANNED → READY → BUILDING → REVIEW → QA →
PR_READY → WAITING_APPROVAL → MERGED → VERIFIED → REPORTED

When every acceptance criterion is already proven:

ANALYZING → SKIPPED_ALREADY_IMPLEMENTED → REPORTED

State meanings and rules: `core/task-state-machine.md`.

`SKIPPED_ALREADY_IMPLEMENTED` requires acceptance-by-acceptance evidence and
must not create a branch, worktree, plan, commit, PR, merge, or release.

`COMPLETED` is human-facing language; operational state ends at `REPORTED`.

Blocked states:

- `BLOCKED_REQUIREMENT`
- `BLOCKED_TECHNICAL`
- `BLOCKED_EXTERNAL`
- `BLOCKED_SECURITY`
