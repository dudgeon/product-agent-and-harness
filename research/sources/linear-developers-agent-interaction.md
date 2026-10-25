---
title: Agent interaction (Linear developers)
source_url: https://linear.app/developers/agent-interaction
author: Linear
publisher: Linear developer docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [shared-persistent-sessions, process-artifacts-as-coordination, product-artifact-primitives]
relevance: medium
---

## Relevance to the project
Linear's agent session protocol is a worked design for agents as visible participants in a multi-person tracker: every run is an AgentSession on an issue, with typed activities (thought, elicitation, action, response, error) and a checklist-style plan. The typed "elicitation" activity is a first-class open-question primitive; the plan is a process artifact the humans can watch.

## Themes
- shared-persistent-sessions: sessions are created when an agent is mentioned or delegated an issue; states pending, active, awaitingInput, error, complete, stale are set by Linear from the agent's last activity (body).
- process-artifacts-as-coordination: plans (technology preview) are checklists of steps with status pending, inProgress, completed or canceled; agents must replace the whole plan on each update (body).
- product-artifact-primitives: workspace and team guidance (preferred repos, constraints) arrives in promptContext and guidance fields (body).

## Key points
- Users reply with prompt activities, which agents cannot create.
- Elicitation activities ask for clarification or confirmation; uncertain repository choice falls back to an elicitation listing options.
- Timing rules: webhook response within 5 s; first activity or external URL within 10 s of a created event, or the session may be marked unresponsive.
- The page does not say whether the human stays assignee while the agent is delegate (other Linear docs suggest delegation keeps a human owner; not verified here).

## Could not verify
- Assignee vs delegate semantics. Retrieved via WebFetch, a model-summarised view.
