# Autonomy Levels

Level 1: AI analyzes and recommends.

Level 2: AI implements and creates PRs; it never approves, merges, or closes them (`docs/ai/handoff.md` Integration sequence step 7).

Level 3: AI merges approved low-risk changes.

Level 4: AI deploys automatically.

Default: Level 2, with activation `PILOT_FROZEN` (`config/autonomous-engineering.yaml`).

Production, security, permissions, and destructive actions require human approval at every level.
