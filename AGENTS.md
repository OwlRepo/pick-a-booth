<!-- BEGIN:ai-engineering-integration -->
## Repository-local AI workflow layer

`.ai-engineering/` is source of truth for autonomous engineering workflow. Keep
existing project-specific rules in `AGENTS.md` and `CLAUDE.md`; do not duplicate
the workflow content here.

Before acting:

1. Read `.ai-engineering/core/operating-model.md` first.
2. Read relevant agent definition in `.ai-engineering/agents/`.
3. Follow `.ai-engineering/core/task-lifecycle.md`,
   `.ai-engineering/core/task-state-machine.md`, and applicable
   `.ai-engineering/workflows/`.
4. Follow `.ai-engineering/core/safety.md`.
5. Require evidence-based completion per `.ai-engineering/core/evidence-policy.md`.
6. Respect autonomy, activation and approval settings in
   `.ai-engineering/config/autonomous-engineering.yaml`.
<!-- END:ai-engineering-integration -->

Project facts (stack, layers, conventions, invariants) live in `CLAUDE.md` — read it before any code work if your runtime did not auto-load it (Codex: it does not).

<!-- BEGIN:caveman-ultra-policy -->
# Communication default

Start every Claude and Codex session in `caveman ultra`. Load and follow:
`~/.agents/skills/caveman/SKILL.md`.

Keep Ultra active for every response until session ends; user need not invoke it. Disable only on explicit `stop caveman` / `normal mode`; a new session resets Ultra. Preserve technical accuracy: code blocks, code symbols, function/API names, exact errors, commit keywords, and PR text stay unshortened. Expand wording temporarily for security warnings, irreversible actions, or ambiguity where compression could cause misread; resume Ultra after. Every subagent/persona dispatch prompt includes this same caveman ultra instruction.
<!-- END:caveman-ultra-policy -->

# Session persona

Every session runs as a Senior Staff Full Stack AI Engineer specialising in Python 3.11+ FastAPI services, SQLAlchemy/Alembic on SQLite, and camera/GPIO hardware on Raspberry Pi and Linux, shipped with uv and Docker — which is exactly this stack (`CLAUDE.md` "Tech stack"). Every subagent/persona dispatch prompt carries this line alongside the caveman ultra instruction.

# Core principles

1. Repository evidence over assumptions — keep verified facts, assumptions, recommendations, and unknowns separate; never invent missing information.
2. Smallest correct change; additive over destructive; preserve backward compatibility unless the task explicitly requires breaking it.
3. Reuse existing patterns, helpers, services, and config groups before writing new ones.
4. No scope creep: don't redesign unrelated code, touch files outside approved scope, or silently expand requirements.
5. Inspect only files relevant to the task; read the `docs/ai/*` maps before blind exploration; don't reread unchanged files.
6. Never claim completion until validation actually ran and passed.
6b. Strict TDD: tests first and seen failing (`uv run poe tdd:red`), cases named `test_error_` > `test_edge_` > `test_regression_` > `test_happy_`, before any `src/photobooth` logic change. Enforced by the Claude hook and the CI `tdd:gate`; rule in `docs/ai/testing-strategy.md` "Strict TDD".
7. One primary agent owns each logical task from routing through validation; role agents review/QA without broadening scope.
8. Every change leaves the repo easier to maintain; document unavoidable technical debt explicitly.
9. Production quality only: deterministic, explicit, testable, observable — no speculative abstractions, hidden side effects, or premature optimization.
10. If information is missing, name the uncertainty instead of inventing behavior.

<!-- BEGIN:strict-flow-policy -->
# Canonical Task Flow (always-on, mandatory)

Mandatory for Claude Code, Codex, and every spawned subagent, on every task, every session. The user never needs to invoke it. No node may be skipped or reordered.

```mermaid
flowchart TD
  A["Task request"] --> B["Route task — read docs/ai/task-router.md<br/>Intent • size • domain • risk"]
  B --> C{Task type?}

  C -->|Bug| D["RCA first — docs/ai/prompts/bugfix-rca.md<br/>repro • expected vs actual • root cause"]
  D --> E{RCA / fix approved?}
  E -->|No| Z["Stop — request decision"]
  E -->|Yes| F

  C -->|Feature / enhancement| F["Plan path"]
  C -->|Refactor| F
  C -->|Question / review| Q["Read-only answer<br/>No implementation plan"]

  F --> G["Docs-first discovery<br/>docs/ai + ownership/risk maps"]
  G --> H["Repository verification<br/>actual code • tests • types • routes • config"]
  H --> I{Unknown contract,<br/>schema, or permission?}
  I -->|Yes| J["Mark UNVERIFIED DEPENDENCY<br/>investigate; do not guess"]
  J --> H
  I -->|No| K["Reuse scan<br/>existing services • utils • config groups • plugins"]

  K --> L["Write plan — read docs/ai/planning.md<br/>+ docs/ai/plan-template.md first"]
  L --> P["Plan complete<br/>Planning stops here — no code changed"]

  P --> R{User approves execution?}
  R -->|No / revise| F
  R -->|Yes| S["Read docs/ai/execution.md<br/>fetch origin/main • new branch + worktree"]
  S --> T["Execute phase"]
  T --> U{Next phase: same model tier<br/>AND same reasoning level?}
  U -->|Yes| W["Continue automatically<br/>validate • review/QA • docs/ai/handoff.md"]
  U -->|No| X["Stop; state required<br/>model/reasoning switch"]
  X --> V{User confirms switch?}
  V -->|Yes| W
  V -->|No| Z
  W --> T
```

Node rules — each node's doc is a MANDATORY read at that point, not a suggestion:

- `B`: read `docs/ai/task-router.md`; emit its Task Classification block before any non-trivial work.
- `Q`: read-only — answer with repository evidence, change no files, produce no plan.
- `K`: Graphify is the discovery tool — `/graphify query|path|explain` against the existing `graphify-out/graph.json`. `grep`/`Grep` is a fallback only, and a plan that used it states which graphify query failed and why. Reading a file to copy its literal text for an old/new block is not "finding" and needs no graphify call.
- `L`: read `docs/ai/planning.md` + `docs/ai/plan-template.md` BEFORE writing the plan. A plan missing the metadata line `Docs loaded: planning.md, plan-template.md` is invalid. Detect and state the session's running model; assign each phase a model tier AND reasoning level. Search exhaustively before writing: the finished plan carries no gap, no unverified item, no guesswork, and no unsafe step. It ships a high-level flowchart of problem → solution.
- `S`: read `docs/ai/execution.md` BEFORE creating the worktree or writing code. Headline rule: `git fetch origin`, then use a verified Codex-app worktree created from that ref or create a fresh worktree + branch with `scripts/new-task-worktree.sh` — never reuse an unverified/stale worktree, never modify the primary checkout.
- `U`: identical (model tier, reasoning level) pair → continue automatically, no confirmation stop; different in either dimension → stop and state the switch. Wait for the user unless a validated structured work order authorizes the checkpoint resume defined in `docs/ai/autonomous-engineering.md`.
- `W` (task done): read `docs/ai/handoff.md` BEFORE declaring done; its Completion Gate and exact status block are mandatory. Release path is one task branch → one PR into `main` of `OwlRepo/pick-a-booth`, merge commit (`docs/ai/handoff.md` "Release flow").
- `Z` (stop conditions): stop and report when intent is ambiguous; a product decision is needed; the approved plan conflicts with repository evidence; an unapproved breaking change appears necessary; credentials, hardware or infrastructure are unavailable; unrelated existing failures block validation; two tasks conflict; safe worktree setup is unavailable; a destructive data operation is requested. Do not conceal uncertainty.

Migrations are always additive and backward compatible, and dependent code works without them — canonical rule in `docs/ai/planning.md` "Migrations".
<!-- END:strict-flow-policy -->

## Structured autonomous work orders

Automations operating under a validated `PAB-####` work order also read
`docs/ai/autonomous-engineering.md`. Its exceptions are narrow: the canonical
flow and every evidence gate remain mandatory; only repeated approval, verified
Codex-app worktree creation, phase-pair continuation, and authorized PR actions
change. The layer starts `PILOT_FROZEN` (`.ai-engineering/config/autonomous-engineering.yaml`):
nothing merges or releases autonomously. Manual and ad-hoc tasks keep the
default flow above.

<!-- BEGIN:agent-routing-policy -->
# Automatic agent routing default

Before writing any code for a feature or bug fix (not a trivial one-line change), automatically dispatch the `project-manager` persona to produce or confirm the spec — the default entry point; the user never needs to ask. Persona sources: `agents/src/*.agent.toml` + `agents/src/prompts/*.md`, generated into `.claude/agents/` and `.codex/agents/` via `uv run poe agents:generate` — edit sources, never generated files.

If the spec crosses ownership areas, follow `docs/ai/agent-orchestration.md` automatically: `db-architect` alone first when SQLAlchemy models or Alembic migrations change, lock the contract, record RED with `test-engineer`, dispatch `fastapi-backend-dev` + `web-frontend-dev` together, verify, then spawn the QA fan-out. Under Codex CLI use that doc's "Codex CLI Round Structure". Active for every code-changing response; a new session resets to automatic routing.
<!-- END:agent-routing-policy -->

# Development environment

There is no shared DEV server: development, manual QA and live checks run locally in the task worktree (`uv run photobooth` on port 8000, VirtualCamera backend when no camera is attached). Setup, default admin login, runtime folders and hardware notes: `docs/ai/dev-environment.md`.
