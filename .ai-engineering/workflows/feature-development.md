# Feature Workflow

1. `NEW → TRIAGED`: Product Manager defines requirements, priority, ownership, unknowns, risks, and dependencies.
2. `TRIAGED → ANALYZING`: Architect evaluates the new feature, affected systems, alternatives, tradeoffs, and risks.
3. If all acceptance criteria are already proven, `ANALYZING → SKIPPED_ALREADY_IMPLEMENTED → REPORTED`: Coordinator records acceptance-by-acceptance evidence and dispatches no implementer or PR work. Otherwise `ANALYZING → PLANNED → READY`: Coordinator creates the plan, assigns agents, records evidence requirements, and confirms blockers are clear.
4. `READY → BUILDING`: test-engineer records RED, then the implementer applies the approved plan and records files, tests, and commit evidence.
5. `BUILDING → REVIEW`: Reviewer independently checks requirements, correctness, security, architecture, maintainability, regressions, and tests.
6. `REVIEW → QA`: QA validates happy paths, failures, edges, regressions, and applicable UI states.
7. `QA → PR_READY`: Coordinator confirms acceptance evidence, review status, QA status, and validation results.
8. `PR_READY → WAITING_APPROVAL`: Reporter prepares the PR report. No merge or release happens automatically without the required approval.
9. `WAITING_APPROVAL → MERGED`: a human approves and merges; rejected or unclear decisions remain blocked.
10. `MERGED → VERIFIED → REPORTED`: verify the merged result with evidence, then the Reporter records the handoff.
