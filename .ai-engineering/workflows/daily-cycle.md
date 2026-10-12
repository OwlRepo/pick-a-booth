# Daily Cycle

No schedule is configured (`config/autonomous-engineering.yaml` `schedule: NONE`);
runs are manual. When a schedule is added, it follows this shape:

## Planning

Product Manager: read incoming requests; analyze requirements, unknowns, risks,
and dependencies; create the prioritized queue.

## Engineering

Coordinator: select ready tasks; assign agents; execute the workflow; create
PRs; stop at `WAITING_APPROVAL` when approval is required.

## Reporting

Reporter: summarize evidence and current task state; report progress,
blockers, risks, and next actions (`templates/eod-report.md`).
