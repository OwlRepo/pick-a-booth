# Testing Strategy

> Purpose: how every change is tested — Strict TDD, layers, commands, live verification.
> Load rule: read before writing a plan's Test Matrix and before implementing.
> Source of truth: `pyproject.toml` (`[tool.pytest.ini_options]`, `[tool.poe.tasks]`), `src/tests/`, and `.github/workflows/` beat this map.

## Strict TDD

Enforced, not advisory: the local guard blocks the agent and the CI gate blocks the PR.

1. **RED before any implementation.** Write every test the task's Test Matrix
   requires, run `uv run poe tdd:red`, and see it fail. Commit the tests on their
   own as `test(<scope>): ...` before any `src/photobooth` logic changes.
   `tdd:red` records the RED in `<git-dir>/tdd-red.json` (per worktree, never committed).
2. **Case order: `test_error_` > `test_edge_` > `test_regression_` > `test_happy_`.**
   Every new test function name starts with one of those prefixes and is declared
   in that order (pytest runs a file in declaration order, so errors and edges
   also run first). A valid RED has at least one `test_error_`, `test_edge_` or
   `test_regression_` case failing, or a test file that cannot be collected yet
   because its module does not exist. Only `test_happy_` failing is not a RED.
3. **Then implement until green.** Implementers may add tests. They never weaken
   or delete a RED test without saying why in the PR.

What counts as what (`scripts/ci/tdd_lib.py`):

| Kind | Paths |
|---|---|
| guarded logic | `src/photobooth/**/*.py` except Alembic versions |
| unit tests | `src/tests/tests/**/test_*.py` |
| migration tests | `src/tests/tests/**/test_*migration*.py` (also run as unit tests) |
| migrations | `src/photobooth/database/alembic/versions/*.py` |
| tooling tests | `scripts/**/test_*.py` |
| not gated | `src/tests/benchmarks/*_test.py`, `src/web/**` (vendored build), docs |

Enforcement:

| Where | What | Bypass |
|---|---|---|
| Claude session | `.claude/settings.json` PreToolUse hook `scripts/hooks/tdd_red_guard.py` blocks Edit/Write (and Bash `sed -i`, `>`, `tee`, `cp`/`mv`) on `src/photobooth/**/*.py` logic until a valid RED marker exists for the current branch | `uv run poe tdd:red --waiver "<reason>"`, which then must appear in the PR as `TDD-Waiver:` |
| Human edits (no hook) | `uv run poe tdd:red` is a mandatory step in `AGENTS.md` | CI gate below |
| Every commit (push and PR) | `uv run poe ci:layers <base> HEAD` (`scripts/ci/check_test_layers.py`, first step of `.github/workflows/ci.yml` job `gate`): each commit that changes `src/photobooth` code also changes a test in the matching area of `src/tests/tests/` (services → `services/`, routers → `router/`, backends → `backends/`, plugins → `plugins/`, utils → `utils/`, migrations → `test_*migration*.py`) | `Test-Layers-Skip: <reason>` as a git trailer in that commit's final paragraph (a line in the body does not count) |
| Every PR | `uv run poe tdd:gate` (`scripts/ci/tdd_gate.py`, workflow `.github/workflows/ci.yml` job `gate`): tests present for changed logic; migration test for changed migrations; names prefixed and ordered; **the PR's tests run against the merge-base code and must fail** (`TDD-Waiver: refactor ...` inverts this: they must pass there) | `TDD-Waiver:` / `Migration-Waiver:` lines in the PR body, all listed in the CI job summary |

Known limits:

- The Bash guard is a heuristic; a human editing by hand bypasses the local guard, never the CI gate.
- Existing test files are grandfathered: only test names a diff adds are checked.
- Tests that need hardware (cameras, serial WLED, GPIO) or the PHP share endpoint self-skip, so they cannot prove RED in CI. Use a mock-based test for the RED, or a waiver that says which hardware check was done by hand.
- The gate copies only the changed test files into the base worktree. A test that depends on a changed `conftest.py` or helper fails to load at the base and counts as RED; reviewers check that the RED is for the intended reason.
- PRs whose head branch is `main` (upstream syncs) skip the gate. Waivers are self-declared; review is where they get challenged.
- CI reads the PR body from the `pull_request` event: editing the description alone does not re-run the gate with the new text. Push a commit to fire a fresh event.

## Runner and Commands

| Command | What |
|---|---|
| `uv run poe test` | whole suite with coverage (`src/tests/tests`) |
| `uv run pytest --basetemp=./tests_tmp/ <path>::<test>` | one test or file |
| `uv run poe lint` | basedpyright + `ruff check` + `ruff format --check` |
| `uv run poe benchmark` | benchmarks (`src/tests/benchmarks`) |
| `uv run poe tdd:red` | record RED for this branch |
| `uv run poe tdd:gate` | the CI gate, locally (`TDD_GATE_BASE=origin/main`) |
| `uv run poe test:scripts` | tests for `scripts/` (TDD tooling, generator, doc links) |
| `uv run poe agents:lint` | persona definitions match `agents/src/` |

Fixtures (`src/tests/tests/conftest.py`): `client` (TestClient on `/api/`, starts the container), `client_authenticated` (admin bearer token), per-test `appconfig.reset_defaults()`, gpiozero `MockFactory`, and a guaranteed media item.

## Targeted Runs (default) vs Whole Suite

Verify a change by running ONLY the tests for the files you touched first; the whole suite runs before the PR and in CI. A green targeted run is the trigger for the docs sync (`docs/ai/handoff.md` "Docs and learning sync").

## Verification Level Per Task Size

- SMALL: lint plus the obviously-affected tests.
- MEDIUM: targeted unit tests plus contract checks (route models, config schema, DB shape).
- LARGE / Deep: full RCA (for bugs) + regression coverage + live verification + rollback notes.

## Mandatory Test Layers (every implementation plan)

| Diff touches | Required | Not required when |
|---|---|---|
| `src/photobooth/**` logic | unit test in `src/tests/tests/` | never |
| a route in `src/photobooth/routers/` | router test through `client` / `client_authenticated` | the route signature and behavior are unchanged |
| an Alembic migration | migration test (`test_*migration*.py`) | never |
| a camera backend, GPIO or serial path | mock-based unit test + a named manual hardware check | pure refactor proven by characterization tests |
| any runtime change | smoke: `uv run photobooth` starts and `/api/doc` answers | docs/tooling-only diff |

Each layer is written RED-first. The regression layer is a test that fails on the pre-fix code; state that it was seen failing. A layer may be dropped only with an explicit waiver line in the plan naming the layer and the reason — a silently missing layer makes the plan invalid.

## Mandatory State Coverage

Every task covers happy path, error cases, and — most importantly — edge cases, plus stop/restart behavior when services or threads are involved. Bugs found while testing are fixed in the same task.

## Backend Five-Bucket Sweep

Backend changes have unit coverage across: happy path, error cases, edge cases, rare/boundary, and performance-relevant. This is the backend QA gate.

Mutation check for critical logic: delete or invert the code under test, confirm a case fails, restore it, confirm `git diff` is empty. Paste the output in the PR.

## Live verification: drive the app AND watch the server

Mandatory for user-visible or hardware-facing changes before they are declared done. Do both sides at once:

1. **Front:** run `uv run photobooth` in the task worktree and use the real UI at `http://localhost:8000/` in Brave (the user's global CLAUDE.md, "Default browser: Brave"). Admin pages need the admin login; the repo owner types credentials — the agent never enters them.
2. **Back:** watch what really happened: the server log (`./log/`), the SQLite rows (`./database/database.sqlite`, read-only queries), and the files written under `./media/`.
3. **Cross-check:** a toast is not proof until the row, file or log line behind it is confirmed, and the reverse. Report measured numbers, not "it works".

Guardrails: never run against a real event's photobooth data; use the VirtualCamera backend when no camera is attached; if a check is blocked (no hardware, no credentials, browser not connected), say which check went unverified — never imply it passed.

## Post-Implementation QA Gate

Scope: the touched files/feature only.

- User-visible changes: `/qa` (or `/qa-only`) plus live verification.
- Backend-only: the five-bucket sweep above.
- Mandatory for MEDIUM and LARGE tasks.
- On a green targeted pass, refresh `docs/ai/file-index/repository-map.md` and the matching `docs/ai/*` entries in the same change.
