---
title: "Automate work with scheduled tasks (Claude Code routines docs)"
source_url: https://code.claude.com/docs/en/routines.md
author: Anthropic
publisher: code.claude.com docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, remote-agent-invocation, cost-control-routing, human-review-gates]
relevance: high
---
## Relevance to the project
Describes event-driven and scheduled cloud agents from the vendor: cron, API-triggered (bearer token) and GitHub-triggered runs that each become a new cloud session. Important for the 'persistent-deployed' axis because it states plainly that these tasks are personal, not team-shared, and that they act as the creating user. Contrasts with Glass scheduled tasks, which depend on a laptop.

## Themes
- shared-persistent-sessions: scheduled tasks 'belong to your individual claude.ai account. They are not shared with teammates'; everything they do through GitHub/connectors 'appears as you' (Create a scheduled task)
- remote-agent-invocation: an API trigger gives a task a /fire HTTP endpoint with a per-task bearer token that returns a session URL; fire text is wrapped as untrusted data (Add an API trigger)
- cost-control-routing: hourly caps (100 scheduled runs/hr per account, 30/hr per task for run-now and API fires) and subscription usage draw-down, no overage by default (Usage and limits)
- human-review-gates: a green run status 'does not mean the work your prompt describes succeeded'; runs start in auto mode with a classifier, and stop to wait if repeated blocks occur (View runs; Permission prompts)

## Key points
- Triggers: schedule (min interval one hour), API, GitHub events (PR, release); no session reuse across events, each run is a fresh session.
- Operational failure modes documented: missed GitHub connection skips runs for up to 72 hours then disables the task; GitHub webhook events beyond hourly caps are dropped; on-the-hour schedules can start minutes late.
- Research preview; API surface under a dated beta header and may change.
- Prompt is treated as a stored assignment, not live user consent, so it cannot approve actions during the run.
