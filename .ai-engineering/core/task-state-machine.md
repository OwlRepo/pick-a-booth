# Task State Machine

Canonical transition:

NEW → TRIAGED → ANALYZING → PLANNED → READY → BUILDING → REVIEW → QA →
PR_READY → WAITING_APPROVAL → MERGED → VERIFIED → REPORTED

Already-implemented transition:

ANALYZING → SKIPPED_ALREADY_IMPLEMENTED → REPORTED

Rules:

- `NEW`: request exists but is not understood.
- `TRIAGED`: priority, ownership, and required agents identified.
- `ANALYZING`: requirements, repository, dependencies, and risks inspected.
- `SKIPPED_ALREADY_IMPLEMENTED`: every acceptance criterion is proven by existing repository evidence. Do not create implementation work, branch, worktree, plan, commit, PR, merge, or release.
- `PLANNED`: implementation approach and acceptance criteria approved.
- `READY`: plan complete, dependencies available, and work authorized to begin.
- `BUILDING`: implementer applies the approved plan (RED first).
- `REVIEW`: independent reviewer inspects the proposed change.
- `QA`: QA validates behavior, failures, edges, and regressions.
- `PR_READY`: evidence is complete and PR handoff is prepared.
- `WAITING_APPROVAL`: human decision required before merge or release. While activation is `PILOT_FROZEN`, every task stops here.
- `MERGED`: approved PR merged by an authorized human.
- `VERIFIED`: accepted or released with evidence.
- `REPORTED`: included in the engineering report.

Blocked states (`BLOCKED_REQUIREMENT`, `BLOCKED_TECHNICAL`, `BLOCKED_EXTERNAL`,
`BLOCKED_SECURITY`) can be entered from any state and leave only by a human
decision or new evidence; the reason is recorded with the block.
