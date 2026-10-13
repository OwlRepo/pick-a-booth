# Engineering Rules

Before coding:

- understand the request
- inspect the existing implementation
- identify affected areas
- check existing patterns

During coding:

- write the failing tests first (`uv run poe tdd:red`)
- make minimal correct changes
- avoid unrelated refactors
- keep backwards compatibility when possible

Before PR:

- review the diff
- run validation (`uv run poe lint`, targeted pytest, `uv run poe test:scripts` when tooling changed)
- confirm acceptance criteria
