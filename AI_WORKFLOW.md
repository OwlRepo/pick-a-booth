# AI Software Engineering Workflow — pointer

The workflow rules live in phase-loaded docs so every session and subagent
dispatch loads only what its current step needs:

- Always-on core (Canonical Task Flow, core principles, stop conditions,
  caveman default, agent routing): `AGENTS.md`.
- Task routing, classification enums, and exact skill mappings:
  `docs/ai/task-router.md`.
- Plan-time rules (verification, deterministic spec, forbidden language,
  completion gate, migrations, DB discipline, scans):
  `docs/ai/planning.md` + `docs/ai/plan-template.md`.
- Execute-time rules (worktree isolation, single-task rule, implementation,
  testing, review, QA): `docs/ai/execution.md`.
- Integration, docs sync, completion gate, final report: `docs/ai/handoff.md`.

If a doc cites a section of this file, fix it to point at those files in the same change.
