# Agent Contract Validation

Validate every agent.

- Product Manager: must create requirements.
- Architect: must create technical decisions when needed.
- Coordinator: must assign work and manage state.
- Implementer: must provide implementation evidence, RED first.
- Reviewer: must independently inspect changes.
- QA: must validate behavior.
- Reporter: must summarize evidence.

Failure: if an agent has no clear input/output contract, repair the agent definition.
Executable personas are checked mechanically by `uv run poe agents:lint`.
