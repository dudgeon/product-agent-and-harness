---
title: "Build a human-in-the-loop document approval Workflow (Temporal docs)"
source_url: https://docs.temporal.io/guides/reliable-document-approvals
author: Cecil Phillip (Temporal)
publisher: Temporal docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [durable-external-waits, human-review-gates, deterministic-scaffold-model-nodes, identity-delegation]
relevance: high
---

## Relevance to the project
Temporal's worked guide for an approval that may take days: decisions arrive as Signals, resubmissions as Updates, status and an audit trail as Queries, with reminders every 24 hours, an SLA, automatic escalation to a second contact and auto-reject on silence. It is the most complete first-party template found for "hold an ask open for weeks, remind, escalate, record the answer", which is the shape of a delivery dependency ask. Two limits matter: the approver's identity is a field in the payload, not verified by the server, and Event History has a hard cap that long, chatty asks can hit.

## Themes
- durable-external-waits: the Workflow waits "for as long as it takes"; timers are persisted on the Server and survive Worker restarts and deploys; "Temporal's Event History replays the Workflow to its exact pre-failure state"; a suspended Workflow uses no compute.
- human-review-gates: reminder loop (`reminder_interval_seconds` default 86400, `max_reminders` default 3); on SLA expiry it escalates to `escalation_email` and opens a second wait; with no escalation contact or a second timeout it auto-rejects with `TIMED_OUT` ("If no one responds in time, escalation happens automatically").
- identity-delegation: `approver_email` is supplied in the decision payload and the Signal handler does not check it against the sender; the audit record holds a caller-supplied value.
- deterministic-scaffold-model-nodes: the approval flow is code-owned (Workflow definition); audit entries written "both in-memory and via an Activity", with the Activity left as a stub for your own store; upsert keyed on Workflow Id and stage.

## Key points
- Limits: "Temporal's Event History has a hard limit of 51,200 events or 50 MB", warnings near 10,240 events or 10 MB; one approval with reminders and escalation is about 40-80 events; use Continue-As-New for long or looping runs.
- Resubmission window defaults to 7 days (604800 s).
- Ownership of the Workflow definition and how changes roll out are not discussed beyond a link to Worker Versioning.
- Companion page (https://docs.temporal.io/ai-cookbook/human-in-the-loop-python): an LLM proposes an action; risky actions wait on an `approval_decision` Signal checked against `pending_request_id`; the agent can wait "for hours, days or indefinitely" consuming no compute; the sample default timeout is 5 minutes, after which the action is cancelled.
- Extends [temporal-dynamic-ai-agents](temporal-dynamic-ai-agents.md), whose note says the human-gate mechanism was not read first-hand.

## Notable quotes
- "Temporal's Event History has a hard limit of 51,200 events or 50 MB."
- "If no one responds in time, escalation happens automatically."

## Could not verify
- Whether Temporal Server records any caller identity for a Signal (the page shows none). Pages undated; read via WebFetch (model-summarised view).
