---
title: "Human in the loop (Cloudflare Agents SDK docs)"
source_url: https://developers.cloudflare.com/agents/concepts/human-in-the-loop/
author: Cloudflare
publisher: Cloudflare Developers docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [durable-external-waits, human-review-gates, shared-persistent-sessions]
relevance: high
---

## Relevance to the project
Cloudflare's agents are Durable Objects that hand long waits to Workflows: `waitForApproval()` is "a durable gate" that "can continue for months or longer without keeping an Agent running", the agent's own `schedule()` sends reminders and escalations, and the docs recommend an `approval_audit` table recording who decided, when and why. That combination (persistent agent plus durable wait plus own scheduler plus own audit table) is the closest single-vendor fit to a three-week dependency ask, with the same caveat as the other engines: the approver is a caller-supplied string.

## Themes
- durable-external-waits: Workflows `waitForEvent` defaults to 24 hours and accepts "between 1 second and up to 365 days"; events can be sent "before the workflow reaches the matching waitForEvent call", and are buffered (companion page https://developers.cloudflare.com/workflows/build/events-and-parameters/).
- human-review-gates: three mechanisms: Workflow approval (`approveWorkflow()` / `rejectWorkflow()`), MCP elicitation (form or URL mode; "typically complete within minutes"), and Code Mode tool approval (`requiresApproval: true`, replaying completed calls from the durable log on approval); multi-approver example counts `currentApprovals` against `requiredApprovals`.
- shared-persistent-sessions: example uses `schedule()` to remind after 4 hours and escalate after 24 hours if status is still "waiting"; pending approvals kept in agent state "survive disconnections" and Durable Object hibernation.

## Key points
- Approver identity: `approvedBy` is an argument to the approve call; authentication is not described. Audit: recommended table with `decided_by`, `decided_at`, `reason` "for compliance".
- Events reach a waiting instance via the Workers binding `instance.sendEvent` or the REST Events endpoint; who may send is not specified.
- The earlier note [cloudflare-agents-long-running-agents](cloudflare-agents-long-running-agents.md) covers what is lost on eviction and that recovery logic is the developer's job.

## Could not verify
- Transport for the `@callable()` approve methods; Code Mode approval expiry configuration. Pages undated; read via WebFetch (model-summarised view).
