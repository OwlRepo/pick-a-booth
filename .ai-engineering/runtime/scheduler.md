# Scheduler Rules

No scheduler is configured (`config/autonomous-engineering.yaml` `schedule: NONE`).
If one is added, scheduled agents must:

- load current state
- avoid duplicate execution
- respect ownership
- respect approvals and the activation state

Failures must be reported.
