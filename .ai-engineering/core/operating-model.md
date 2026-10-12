# Operating Model

The system behaves as an AI engineering department.

Primary loop:

Human Request
→ Product Manager
→ Architect (when required)
→ Coordinator
→ Implementer
→ Reviewer
→ QA
→ Pull Request
→ Human Approval
→ Report

The executable flow every session follows is the Canonical Task Flow in
`AGENTS.md`; this loop maps its roles to the personas in `agents/src/`.

Goals:

- reduce repetitive engineering work
- improve consistency
- preserve safety
- keep humans in control of important decisions
