# Bootstrap Validation Workflow

Purpose: validate that the autonomous engineering layer is installed and internally consistent.

Run checks:

1. Folder completeness
   - Required directories exist (`agents`, `config`, `core`, `memory`, `runtime`, `templates`, `validation`, `workflows`).
   - Required agent, workflow and template files exist.
2. Reference validation
   - Workflows reference existing agents; agents reference existing rules.
   - `uv run poe test:scripts` passes (`scripts/tests/test_doc_links.py` checks every cited path).
3. Lifecycle validation
   - every state is defined; every transition has a reason; blocked states are handled; completion requires evidence.
4. Safety validation
   - no instruction bypasses approvals; no workflow allows destructive actions; no workflow exposes secrets.
   - `config/autonomous-engineering.yaml` `activation` is one of `PILOT_FROZEN`, `ACTIVE`, `RELEASE_FROZEN`.
5. Runtime validation
   - Claude Code instructions exist (`runtime/claude.md`), no other agent runtime is configured; scheduler behavior is defined; manual execution is supported.

Output:

```
VALIDATION REPORT
Status: PASS / NEEDS_REPAIR
Issues:
Affected files:
Recommended fixes:
```
