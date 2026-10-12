# Plan Template (canonical skeleton)

Every plan in this repo uses this exact section structure. It satisfies the
deterministic-spec rules in `docs/ai/planning.md` by embedding literal
old-text/new-text blocks (or full new-file content) inline in each phase step.
Read `docs/ai/planning.md` together with this file before writing any plan.
Save the approved plan to `docs/plans/<branch-short-name>.md` before execution.

Phase-stop rule: execution stops when the next phase's model tier or reasoning
level differs from the current pair (`docs/ai/planning.md`). Identical pairs
continue automatically. A validated structured work order may resume from that
checkpoint under `docs/ai/autonomous-engineering.md`; other tasks wait for the
user.

---

## <Plan title>

<TL;DR: 2-4 plain-language sentences. What's broken/needed (root cause in one
sentence) and what will be built, understandable by a non-technical teammate.
Use an analogy for inherently technical concepts.>

### Flowchart (high-level)

<One high-level flowchart: the problem/goal on the left, the solution shape on
the right. Rendered inline via `mcp__visualize__show_widget` when available and
recorded here as a mermaid block so the saved plan keeps it. In the CLI the
mermaid block alone satisfies this section. High level only — boxes a
non-technical reviewer can scan in seconds.>

### Task metadata

- Classification: `BUG_FIX|ENHANCEMENT|NEW_FEATURE|REFACTOR|PERFORMANCE|INFRASTRUCTURE|DOCUMENTATION` · `SMALL|MEDIUM|LARGE` · <domain> · <risk>
- Docs loaded: `planning.md, plan-template.md` (mandatory canary — a plan missing this line is invalid)
- Claims reversed while investigating: <each claim asserted and later disproved, with what disproved it — or "none">
- Root cause: <one sentence with file/symbol evidence> (bug fixes only)
- Detected running model: <model currently running this session>
- Recommended model: `<tier>`, <reasoning level>; confidence <level>. Fallback: `<tier>`.
- Minimum capability: <lowest model capability that remains sufficient, with evidence>.
- Branch: `<type>/<ticket-id|no-ticket>-<short-name>` (from `origin/main`)
- Release path: one branch → one PR into `main` of `OwlRepo/pick-a-booth`, merge commit (`docs/ai/handoff.md` "Release flow").
- Required skills: </investigate, ecc:model-route, /qa, ecc:code-review, ...>
- Execution preflight: `git fetch origin`; verify/reuse a Codex-app worktree created from that `origin/main`, otherwise create one with `scripts/new-task-worktree.sh <type> <short-name>`, then `uv venv --system-site-packages && uv sync`.

### Phase 1 — RED (`<model>`, <reasoning>)

1. <Test file path. Full new-file content, or literal Old/New blocks, for every Test Matrix case, named `test_error_*` > `test_edge_*` > `test_regression_*` > `test_happy_*`.>
2. Run `uv run poe tdd:red`; paste the failing output. No `src/photobooth` logic changes in this phase.

Done: RED recorded, tests committed alone as `test(<scope>): ...`.

### Phase N — <title> (`<model>`, <reasoning>)

1. <Path to file.py. Then a literal "Old:" fenced block with the exact current text and a literal "New:" fenced block with the exact replacement text — or, for a new file, one fenced block with the complete content.>
2. ...

Done: <objective, observable completion condition for the phase.>

### Validation and acceptance

- **Test Matrix (mandatory table):** one row per layer from `docs/ai/testing-strategy.md` "Mandatory Test Layers" — `layer | required / not required + reason | file | cases`, cases listed `test_error_` > `test_edge_` > `test_regression_` > `test_happy_`.
- A layer may be dropped ONLY with an explicit waiver line naming it and the reason — never silently.
- Hardware: which paths are proven by mocks/self-skipping tests and which need a manual check on real hardware (name the device).
- Run: `uv run poe lint`, targeted `uv run pytest --basetemp=./tests_tmp/ <files>`, `uv run poe test` before the PR, `uv run poe test:scripts` and `uv run poe agents:lint` when tooling or personas change, plus a smoke run (`uv run photobooth`, `/api/doc` responds) for any runtime change.
- Graphify gate (MANDATORY after every implementation): load `$graphify`, run `/graphify . --update` after the final indexed edit, re-run after a corpus-changing rebase/edit, and report graph diff plus semantic input/output tokens (actual, or a clearly labeled bounded estimate + method).

### Compatibility, docs, and scans

- <What existing behavior is preserved; migration backward-compat statement per `docs/ai/planning.md` "Migrations" when a migration exists.>
- <docs/ai files to update in the same change (`docs/ai/handoff.md` "Docs and learning sync").>
- <No forbidden language (see `docs/ai/planning.md`).>
- Optimization scan: <opportunity or "not worth it, left as-is">.
- Cache scan (media cache / `Cacheditem`): <opportunity or "not worth it, left as-is">.
- DB impact: <sessions, columns, limits, concurrency; or "none">.
- Outcome states: <how success and each error surface to the API caller / UI>.
