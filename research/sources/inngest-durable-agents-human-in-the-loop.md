---
title: "Human-in-the-loop (HITL) (Inngest durable agents docs)"
source_url: https://www.inngest.com/docs/durable-execution/durable-agents/human-in-the-loop
author: Inngest
publisher: Inngest docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [durable-external-waits, human-review-gates, agent-frameworks, identity-delegation]
relevance: high
---

## Relevance to the project
Inngest's documented way for an agent to wait on a person: `step.waitForEvent()` suspends the function until an event with a matching correlation key arrives or a timeout passes, at no compute cost. It is the plainest durable-engine model of "hold the ask open, then resume with the answer", and it shows the gap that matters for a regulated dependency ask: the engine records that an event arrived, but who answered (`respondedBy`) is whatever the sending application writes into the payload.

## Themes
- durable-external-waits: "The function is suspended while waiting, so there's no compute cost while a human reviews"; gates are "durable and independent" (example: approval at 2 AM, legal sign-off three days later).
- human-review-gates: gate only the dangerous tools inside the agent's tool loop so safe tools (search) run freely; on timeout your code chooses auto-reject, auto-approve, escalate with a second wait, or re-notify ("No event means it timed out").
- identity-delegation: the response payload carries `approvalId`, `approved`, optional `reason` and `respondedBy`, filled in by your Slack or dashboard handler; the Slack example is pseudo code without request-signature verification.
- agent-frameworks: correlation by `match: "data.approvalId"` (TypeScript) or an expression (Python, Go); the approval id must be unique per request (built from task id, iteration and tool name).

## Key points
- Example waits use 4h, 24h, 48h and 72h timeouts; the step reference page (https://www.inngest.com/docs/reference/functions/step-wait-for-event) shows "7d" and "30d" and states no maximum.
- Who sends the answer: your application, not Inngest (`inngest.send` with `agent/approval.response`).
- Companion page (https://agentkit.inngest.com/advanced-patterns/human-in-the-loop): AgentKit's `ask_developer` tool waits up to "4h" on `app/support.ticket.developer-response`, matched on `data.ticketId`; the answer and its timestamp are returned to the calling agent as the tool result; with no response the example returns `{ error: "No developer response provided" }` (inferred timeout behaviour). The AgentKit network must run inside an Inngest function for the wait to be durable.
- Neither page says whether an event sent before the wait begins is matched.

## Could not verify
- Platform maximum wait duration and plan limits; behaviour across Inngest server restarts is asserted ("resumes exactly where it left off") but not detailed.
- Pages undated; read via WebFetch (model-summarised view).
