# Task Router

> Purpose: turn an incoming request into a workflow, a task size, and a risk level. Single routing table.
> Load rule: run this first on any task (flow node B) before touching code.
> Source of truth: this is a MAP. The real code and `docs/ai/risk-register.md` decide what is actually risky. If a map conflicts with code, code wins.

## Routing Table

Classification enums: `BUG_FIX` · `ENHANCEMENT` · `NEW_FEATURE` · `REFACTOR` · `PERFORMANCE` · `INFRASTRUCTURE` · `DOCUMENTATION`. Complexity: `SMALL` · `MEDIUM` · `LARGE`. Classify each task exactly once.

| Intent | Prompt doc | Skill |
|---|---|---|
| Bug / error / regression / crash / failing test | `docs/ai/prompts/bugfix-rca.md` — RCA first, NO code until approved → then `docs/ai/prompts/bugfix-plan.md` | `/investigate` |
| Enhancement of existing behavior | `docs/ai/prompts/feature-plan.md` | `ecc:plan` |
| New capability / new route / new backend or plugin | `docs/ai/prompts/feature-plan.md` | `ecc:feature-dev` |
| Cleanup / rename / restructure, no behavior change | `docs/ai/prompts/refactor-plan.md` | — |
| Performance | required analysis below | — |
| Docker / CI / systemd / packaging / infra config | required analysis below — Deep by default, with an operational-verification checklist | — |
| Documentation | required analysis below | `ecc:update-docs` |
| Question / explanation / review / discovery | read-only, no plan, no file changes | `ecc:code-review` or `/review` for diffs |
| QA | — | `/qa` (fixes), `/qa-only` (report), `ecc:test-coverage` |

For a validated structured `PAB-####` work order, an evidence-backed
Low/Medium/High bug RCA may continue into its bounded fix plan under
`docs/ai/autonomous-engineering.md`. Ambiguous root cause, changed acceptance,
Very High risk, or expanded behavior still stops for approval.

Other skills: `/plan-eng-review` (architecture plan review), `ecc:python-review` and `ecc:fastapi-review` (language/framework review). Gstack skills use short names (`/investigate`, `/qa`); never invent namespaced variants. If a skill name fails to load, report it as an unresolved mapping instead of substituting an invented command.

### Required analysis for types without a prompt doc

- `PERFORMANCE`: measured/evidenced bottleneck, baseline (use `uv run poe benchmark` / `src/tests/benchmarks/` where it applies), hot path, proposed optimization, expected impact, measurement method, regression risks, observability. Never optimize on speculation.
- `INFRASTRUCTURE`: current environment, proposed change, compatibility/deployment impact (Raspberry Pi, Linux, Windows, Docker), secrets/config impact, rollback procedure, required validation.
- `DOCUMENTATION`: audience, current gap, source-of-truth code/config, exact documents to update, examples requiring verification.

## Ambiguity Rule

When intent is unclear, pick the safest lane. Anything touching admin auth, the unauthenticated `/api` surface, config persistence, file serving, Alembic migrations, plugin loading/hookspecs, camera backends, GPIO/serial hardware, system commands (reboot/shutdown/systemctl), or share/sync credentials is Deep — no exceptions, even if the request looks small.

## Polyglot Note

This repo is not Python-only: the Python app PLUS a Vue3/Quasar/TypeScript frontend (source in `frontend/`, a git subtree of photobooth-frontend, built with npm into `src/web/frontend/`) PLUS a PHP share endpoint (`src/web/shareondemand/api.php`) PLUS GitHub Actions workflows. Route and verify for the language and runtime actually involved.

## Mandatory Classification Output

Emit this block before starting work on any non-trivial task:

```
Task Classification:
- Intent:
- Workflow:
- Task Size:
- Domain:
- Risk:
- Contract Areas:
- Next Action:
```

Domain values come from `docs/ai/module-ownership-map.md`. Risk values come from `docs/ai/risk-register.md`. Plans must then satisfy `docs/ai/planning.md` (verification, deterministic spec, completion gate) using the skeleton in `docs/ai/plan-template.md`.
