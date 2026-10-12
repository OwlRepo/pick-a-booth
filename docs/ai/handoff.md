# Handoff and Integration

> Purpose: everything between "code validated" and "task done" — rebase, push, docs sync, PR, final report.
> Load rule: read at flow node W, before declaring any task done. The Completion Gate below is mandatory.

## Integration sequence (stated once — this is THE list)

1. Confirm the current worktree and branch match the selected task, and the diff contains no unrelated changes.
2. Commit all validated changes with focused messages (`<type>(<scope>): <description>`).
3. `git fetch origin`, then reconcile with `origin/main`. Rebase only a branch that has not been pushed for review yet; once a PR exists and someone reviewed it, merge `origin/main` into the branch instead.
4. Resolve conflicts using both changes' intent — never blindly ours/theirs. If a conflict forces choosing between product behaviors, stop and request a decision. Upstream-sync conflicts (photobooth-app changes) keep upstream behavior unless the task explicitly overrides it.
5. Re-run all required validation after the reconcile; review the post-reconcile diff.
6. Push: first push `git push --set-upstream origin <branch>`; after a rebase of an already-pushed branch, `git push --force-with-lease origin <branch>` (only then).
7. Creating a pull request is autonomous (autonomy Level 2, `.ai-engineering/core/autonomy-levels.md`) once steps 1-6 are done. Always `gh pr create --repo OwlRepo/pick-a-booth --base main` — without `--repo`, `gh` opens the PR against the upstream parent. Approving, merging, or closing a pull request needs explicit instruction from the repo owner; the layer is `PILOT_FROZEN` (`.ai-engineering/config/autonomous-engineering.yaml`). Never push to `main`; never delete the branch or worktree automatically. All PR paths read `docs/ai/pr-evidence.md` first — a PR without the evidence its Change Type requires stays a draft.
8. After one task merges, dependent/overlapping branches reconcile with the updated `origin/main` before any later merge. Do not merge completed worktrees simultaneously without coordination.

Manual testing happens in the task worktree (`uv run photobooth`). From another checkout: `git fetch origin && git switch --track origin/<branch>`.

## Release flow (task branch → main)

The fork has one long-lived branch, `main` (`git ls-remote --heads origin`), and
no deployment of its own: the PyPI publish job and the Raspberry Pi test runner
only run for the upstream owner (`.github/workflows/cicd.yml`,
`.github/workflows/pytests.yml`). So:

1. One task branch, cut from `origin/main`, carrying only that task's commits.
2. One PR `<branch>` → `main` on `OwlRepo/pick-a-booth`.
3. CI green (`gh pr checks <number>`: `ai-gates`, `lint`, `tests`), then the repo owner merges with **"Create a merge commit"** — the RED `test(...)` commit stays visible ahead of the implementation in history.

Syncing upstream photobooth-app into the fork is its own PR whose head is
`main` of the upstream; the TDD gate skips it (`scripts/ci/tdd_gate.py`
`PROMOTION_REFS`).

## Docs and learning sync (same change, mandatory)

- Update `docs/ai/file-index/repository-map.md` for every touched source file, plus the matching `docs/ai/*` contract/ownership/risk/architecture/testing map. Scope to what changed — never a blanket re-index. Docs-only changes update only what they affect.
- For genuinely new patterns/libraries/decisions: record a one-line prediction before implementation, append the verified result to `.ai-engineering/memory/lessons-learned.md` after.

## Final integration gate (multi-task batches)

After all planned tasks merge: full test suite, lint, type check, migration validation, live QA, smoke tests, cross-task regression checks. Individually correct changes must also work together.

## Completion Gate

A task is not complete unless ALL are true:

- Changes committed; branch reconciled with `origin/main`; validation re-run green afterwards; branch pushed.
- Exact branch and latest commit SHA reported; remote branch ready for required manual testing, or evidence states why manual testing is not required.
- No PR approved, merged, or closed without explicit instruction from the repo owner; PR creation follows Integration sequence step 7.
- Docs sync done (section above).
- `$graphify` incremental maintenance ran after the final indexed edit (and again after any corpus-changing rebase/edit); its graph diff and semantic input/output token evidence were reviewed. A skipped or failed update blocks completion.
- If a PR exists: its CI checks are green, verified with `gh pr checks <number>` — never assumed. Branch protection is NOT enabled on `main`, so a red PR can still be merged and nothing will stop it. Checking this by hand is part of the gate, not a formality.

## Required final report

- Task ID · implemented behavior · files changed/created.
- Compatibility: behavior preserved, public-contract impact, migration/rollout impact on installed photobooths.
- Validation: each command run and its result (tests, lint, type check, live checks). Never claim a gate passed if it was not run.
- Graphify evidence: exact command/mode, changed-file count, graph diff, semantic input/output tokens (actual, or a labeled bounded estimate + method), and any integrity warning.
- Review findings: resolved and remaining risks.
- Git state: worktree path, local branch, remote branch, target base, latest commit SHA, commits created, rebase status.
- Manual test scenarios + command to switch to the branch + `uv run photobooth`, or `NOT REQUIRED` with evidence.

End with this exact status block:

```text
Ready for manual testing: YES/NO/NOT REQUIRED
Ready for PR creation: YES/NO
PR created: YES/NO
Merged: YES/NO
Production verified: YES/NO/NOT APPLICABLE
```
