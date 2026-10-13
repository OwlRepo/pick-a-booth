# Planning Rules

> Purpose: every rule that governs WRITING a plan. Mandatory read before any plan.
> Load rule: read together with `docs/ai/plan-template.md` at flow node L. A plan written without both is invalid; the plan's metadata must state `Docs loaded: planning.md, plan-template.md`.
> Source of truth: real code, tests, schemas, routes, and `pyproject.toml` always beat maps and prose.

## Docs-first, then repository verification

Before reading source for a new plan, check `docs/ai/` for existing answers. If a doc contradicts code, trust the code and fix the doc in the same change.

Then verify against the repository itself:

1. Search exhaustively, not just the referenced files: enumerate every call site, consumer, test, route, config field, plugin hook, and migration the change can reach, then inspect each. Verify every referenced path and symbol exists. Exhaustive search up front is what prevents a plan from correcting itself mid-execution.
2. Search all usages of each symbol that will change.
3. Verify reusable services, utils, config groups, and plugins BEFORE proposing any new file or abstraction. If nothing is reusable, name the inspected candidates and why each fails.
4. Never guess file names, symbols, APIs, DB fields, env vars, or patterns. Report missing files/symbols explicitly; never invent replacements.
5. Every fact in a plan traces to a file/line actually read this session. Cite important facts as path + symbol + verified behavior + why it matters.
6. A task depending on an unverified schema, permission model, API contract, hardware behavior, or external integration is marked `UNVERIFIED DEPENDENCY` — stop and investigate before writing code that assumes it.

## Phases, model detection, and the switch stop

Every plan is cut into phases. Each phase names BOTH the model tier and the reasoning level (use `ecc:model-route` heuristics — it cannot detect the running model, so first detect and state the model running the session from its own system context, and assign tiers relative to it).

During execution, at the end of each phase compare the next phase's (model tier, reasoning level) pair with the current one:

- Identical pair → continue automatically, no confirmation stop.
- Different in either dimension → STOP, state the required switch, wait for the user.

### Structured automation exception

A validated `PAB-####` work order may replace repeated user confirmation with
the standing authorization envelope in `docs/ai/autonomous-engineering.md`.
The stop remains a real validated checkpoint. Very High work, scope expansion,
product decisions, breaking changes, and insufficient model capability still
require the user.

## Plan format

Use the canonical skeleton in `docs/ai/plan-template.md` exactly. Plans are deterministic: every step is a literal old-text/new-text block (or, for a new file, the complete new-file content) copied from the actual current repository content — never a prose description of the change. The executing model decides nothing that was decidable at plan time. Save the approved plan to `docs/plans/<branch-short-name>.md` before execution begins.

Always prefer the simplest, most efficient correct solution — a plan that solves the same problem with fewer moving parts, fewer new files, or fewer new abstractions wins. Simple is not shallow: the solution must hold long term. A fix that only covers the reported path is a band-aid — say so and propose the durable version instead of planning the band-aid. State any fact in exactly ONE place in the plan and have every other step reference it.

### Forbidden language

Never use vague operations in a plan: "update component", "adjust layout", "modify styles", "preserve behavior" (without naming the behavior and proof), "where needed", "update consumers", "improve implementation", "if necessary", "etc.", "appropriate files", "relevant modules". This includes any prose paraphrase of a code/text change ("rename the function", "add a check for X") when a literal old-text/new-text block is possible. Prose is only acceptable for genuinely new content with no old state to diff against.

### Plan completion gate

A plan is invalid until all are true:

- Every file path is explicit.
- Every modified symbol is identified.
- Every code operation is a literal old-text/new-text block or full new-file content.
- Every dependency is listed.
- Every acceptance criterion is mapped (criterion → file → symbol → step → validation).
- Every test is mapped (exact file, scenario, assertions — never "extend tests").
- Every regression risk is mapped (file, symbol, reason, proving validation).
- Every new file is justified against verified reuse candidates.
- No forbidden language remains.
- No two steps or phases restate or contradict the same fact.
- The chosen approach is the simplest correct one — a rejected simpler alternative is named with the reason.
- Every causal claim ("X causes Y") names both the evidence FOR it and the observation that would DISPROVE it. An unfalsifiable cause is labelled a hypothesis. "Checked, not it" is evidence worth stating.
- Every measurement states what its metric divides by and why the sample is valid for that metric; fixed overhead is amortised or reported separately and cache/warm-up state is controlled.
- No gaps, no unverified items, no guesswork, no unsafe steps. Every open question is answered with a file/line or listed as a blocker that stops the plan.
- Every edge case and error case found during the search is enumerated with its handling (which file, which branch of which function), independent of the tests that prove it.
- The plan carries a high-level flowchart of problem/goal → solution (`docs/ai/plan-template.md` "Flowchart").

## Batch scheduling (multi-task plans)

Produce Parallel Group A, Parallel Group B, Sequential Tasks, and Merge Order. Only parallelize tasks that share no files, symbols, schemas, APIs, config fields, or business logic. Merge order preference: shared foundations → DB models/migrations → API contracts (Pydantic schemas, routes) → services/backends/plugins → web assets → dependent enhancements → independent fixes.

## DB discipline (SQLAlchemy + SQLite)

Every database-touching step states:

- the session/transaction scope it runs in and who closes it,
- the exact columns read or written; no unbounded `select()` over `mediaitems` or `cacheditems` without a limit or a reason,
- no N+1 patterns in list endpoints,
- behavior under concurrent access (SQLite single writer; `check_same_thread=False` in `src/photobooth/database/database.py`),
- the `Mediaitem.revision` / `Cacheditem.revision` invariant when media is modified (`src/photobooth/database/models.py`).

## Migrations (canonical rule)

Any plan including an Alembic migration must satisfy ALL of:

- Additive and backward compatible: never modifies or removes existing user data, never drops/renames tables or columns in a way that breaks code running against the old schema, never adds a NOT NULL column without a server default.
- Dependent code is graceful WITHOUT the migration: the plan names how each dependent path behaves against the old schema.
- Reversible: `downgrade()` restores the previous schema; a migration test (`src/tests/tests/**/test_*migration*.py`) upgrades from the previous head and from an empty DB.
- Destructive operations happen ONLY with explicit approval from the repo owner, recorded in the plan.
- One linear chain: `down_revision` points at the current head; never two heads.

**How migrations actually get applied:** `create_db_and_tables()` runs
`alembic upgrade head` at every app start (`src/photobooth/__main__.py`,
`src/photobooth/database/database.py`). There is no operator in the loop: a
migration runs unattended on every photobooth that installs the release, against
whatever data that device holds. A failed migration stops the app from starting.

## Hardware and kiosk realities

- Hardware-dependent code paths (cameras, GPIO, serial/WLED, printers) are tested with mocks or self-skipping tests; the plan states which paths are verified only on hardware and by whom.
- Long-running work (capture, processing, sync) runs in services/threads; the plan states how it stops on `container.stop()`.
- Every user action surfaces success or a clear error through the API; failed background work is logged and visible, never silent.

## Mandatory Graphify phase (every implementation plan)

### Graphify is the discovery tool (not just the maintenance gate)

Finding things — where a symbol is used, what calls what, which layer owns a
file, what a module connects to — goes through Graphify against the existing
`graphify-out/graph.json`: `/graphify query "<question>"`, `/graphify path
"<a>" "<b>"`, `/graphify explain "<symbol>"`. `grep`/`Grep`/`rg` is a fallback
for when Graphify cannot answer (literal string search, a file type the graph
does not index, an empty or stale graph). A plan that used grep names the
graphify query that failed and why.

Scope note: copying the exact current text of a file to build a literal
old-text/new-text block is not discovery. Read the file (or `git show`) for that.

Every implementation plan MUST include a final Graphify maintenance step.
After the last change to any indexed source or document and before review,
commit, and handoff, load the `$graphify` skill and run `/graphify . --update`
from the repository root. Direct `graphify update .` is acceptable only for
code-only changes because the installed CLI shortcut performs AST extraction;
docs, papers, images, and video MUST follow the `$graphify` skill's incremental
semantic flow. Re-run after any later indexed edit or rebase that changes
indexed files.

A task is incomplete if the update is skipped, fails, or its graph diff and
token-cost evidence are not reviewed. Changes produced solely by that update
do not trigger an immediate second update. `graphify hook install` supplements
this gate but never replaces it because the hook ignores document and image changes.

Use the installed Graphify capability surface according to task need. Check
`graphify --help` before selection; report unsupported commands instead of
emulating them. Examples (not an allowlist):

```bash
/graphify .
/graphify . --update
/graphify . --cluster-only
/graphify . --no-viz
/graphify query "what calls the processing machine?"
/graphify path "AcquisitionService" "ProcessingService"
/graphify explain "Container"
graphify hook install
graphify merge-graphs a.json b.json
```

Token efficiency is mandatory:

- Prefer the existing graph and incremental `--update`; full extraction requires
  a missing, corrupt, or intentionally replaced baseline with the reason stated.
- Use bounded `query`, `path`, or `explain` for narrow questions.
- Use `--no-viz` for CI or a large graph unless visualization is required.
- Extract only changed or uncached files.
- Report the exact Graphify command/mode, changed-file count, graph diff, and
  semantic input/output token usage. Use actual runtime counters when exposed;
  otherwise report a clearly labeled bounded estimate, its method, and the
  runtime limitation. Never present an estimate as actual. Report zero only
  when no semantic extraction ran.

## Closing scans (every plan)

- Optimization scan, scoped to what the plan touches: backward-compatible only; state how functionality re-verifies; "not worth it, left as-is" is a valid answer.
- Cache scan: check the existing media cache (`src/photobooth/services/mediacollection/`, `Cacheditem`) before proposing any new caching mechanism; same honesty rule.
- Best practices, without forcing scope: separation of concerns, reuse before new code, TDD for testable logic.
