# Execution Rules

> Purpose: every rule that governs IMPLEMENTING an approved plan — worktree, code, review, QA.
> Load rule: read at flow node S, before creating the worktree or writing any code.
> Source of truth: real code and the `pyproject.toml` poe tasks beat this map.

## Worktree and branch isolation

Planning, investigation, and review-only sessions need no worktree. Any session that modifies application code requires one dedicated task branch and worktree:

1. `git fetch origin` first. In a Codex app task created in worktree mode from that fetched `origin/main`, verify the current checkout is that dedicated app-managed worktree, record its path/branch/base SHA, and reuse it; never run `scripts/new-task-worktree.sh` inside it. In every other session, create a NEW worktree and branch from the fetched `origin/main` HEAD with `scripts/new-task-worktree.sh <type> <short-name>`, then `uv venv --system-site-packages && uv sync` inside it. Never silently reuse an unverified or stale worktree. Full verification contract: `docs/ai/autonomous-engineering.md` "Origin freshness and app-managed worktrees". Then copy the approved plan from the harness plan file (Claude Code keeps it at `~/.claude/plans/<slug>.md`) to `docs/plans/<branch-short-name>.md` in the new worktree and commit it alone (`docs(<scope>): approved plan ...`) before the RED commit.
2. Branch naming: `fix|feat|enhancement|refactor|perf|infra/<ticket-id|no-ticket>-<short-name>`.
3. Never modify the primary checkout for an application-code task. Never reuse another task's worktree. Never create nested/duplicate worktrees for one branch. Never delete a worktree automatically. One branch + worktree per logical task.
4. If safe worktree creation is unavailable, stop before modifying code and report the exact command required.

## Single-task rule

When implementing one task from a batch plan: implement ONLY the selected task; all other tasks are read-only context. No partial implementation of future tasks, no speculative code, no touching files "because a later task may need them". Follow the approved plan unless repository evidence proves it invalid — then stop and report the contradicted assumption, the code evidence, and the required correction.

## Implementation rules

1. One logical change at a time; minimal diff; no unrelated cleanup; no speculative abstractions.
2. Preserve existing naming and architecture conventions (`CLAUDE.md` "Coding conventions").
3. Add or update tests with behavior changes. Never weaken or remove tests to make them pass.
4. Fix type/lint/runtime errors; never suppress them.
5. No breaking API/schema/behavior changes without approval. No dependency or `uv.lock` changes unless the plan requires them. No destructive DB operations without explicit approval.
6. After each validated logical unit, create a focused commit: `<type>(<scope>): <concise description>`. Never combine unrelated changes in one commit.

## Mandatory Graphify closeout

After the final change to any indexed source or document, load the `$graphify`
skill and run `/graphify . --update` from the repository root before review,
commit, and handoff. Re-run after a later indexed edit or a rebase that changes
indexed files. Failure, skipped execution, or unreviewed graph/token evidence
blocks completion. Changes produced solely by that update do not trigger an
immediate second update. An installed Graphify hook does not replace this gate.

Select task-relevant Graphify capabilities and token controls from
`docs/ai/planning.md` "Mandatory Graphify phase".

## Testing requirements

This repo uses pytest (`pyproject.toml` `[tool.poe.tasks]` `test`); run it through `uv run`.

- RED first, always: write every test in the plan's Test Matrix (cases named `test_error_*` > `test_edge_*` > `test_regression_*` > `test_happy_*`), run `uv run poe tdd:red`, see it fail, and commit the tests alone as `test(<scope>): ...` BEFORE touching `src/photobooth` logic. The Claude hook blocks logic edits until then, and the CI `tdd:gate` re-proves the RED against the base. Full rule: `docs/ai/testing-strategy.md` "Strict TDD".
- Coverage of ALL of these is mandatory: happy path, error cases, and edge cases. Backend changes also cover rare/boundary cases, stop/restart behavior of services and threads, and performance-relevant behavior.
- Bugs found during testing are fixed in the same task, never deferred.
- Tests create runtime folders in the working directory; run them from the worktree root and never point them at a real photobooth's data.
- Local environment, admin login, hardware notes: `docs/ai/dev-environment.md`.

## Review mode

Review runs separately from implementation (fresh session or different model preferred). Invoke `ecc:code-review` (or `/review` for the gstack pre-landing pass; `ecc:python-review` / `ecc:fastapi-review` for language depth) and inspect the actual diff, not just final file state. Check: acceptance criteria, root-cause correctness, scope creep, hidden regressions, breaking changes, architecture violations, duplicate logic, dead code, security, performance, missing/weak tests, error handling, compatibility. Never approve solely because tests pass.

## QA mode

Invoke `/qa` (test-and-fix) or `/qa-only` (report-only). Run the validation the approved plan defines — the standard command set, stated once for all phases:

- targeted `uv run pytest --basetemp=./tests_tmp/ <files>` first, then `uv run poe test`
- `uv run poe lint` (basedpyright + ruff check + ruff format --check)
- `uv run poe test:scripts` and `uv run poe agents:lint` when `scripts/`, `agents/src/` or docs change
- a smoke run (`uv run photobooth`, then `http://localhost:8000/api/doc`) for any runtime change, and a live check in the browser for user-visible changes (`docs/ai/testing-strategy.md` "Live verification")

Report each command and its result. Never claim validation that was not executed. Validation is complete only when acceptance criteria pass, required tests pass, review findings are resolved, and the final diff has no unrelated changes. Then proceed to `docs/ai/handoff.md`.
