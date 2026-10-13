# Bug Workflow

1. Reproduce the issue.
2. Identify the root cause (`docs/ai/prompts/bugfix-rca.md`); stop for approval.
3. Create the fix plan (`docs/ai/prompts/bugfix-plan.md`).
4. Write the failing regression test first (`uv run poe tdd:red`).
5. Implement.
6. Validate the regression.
7. Review.
8. QA.
9. Create the PR.
