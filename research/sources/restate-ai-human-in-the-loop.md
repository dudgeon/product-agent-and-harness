---
title: "Human-in-the-loop (Restate AI patterns docs)"
source_url: https://docs.restate.dev/ai/patterns/human-in-the-loop
author: Restate
publisher: Restate docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [durable-external-waits, human-review-gates, agent-frameworks]
relevance: medium
---

## Relevance to the project
Restate models a human answer as an "awakeable", a durable promise with a callback id that the agent hands to the approver; anyone holding the id can resolve it over HTTP. The pattern holds a wait open through crashes and redeploys, but it makes the callback id the credential: the docs do not say how the resolving party is authenticated or recorded, which is the open question for a dependency ask answered by an owner outside the team.

## Themes
- durable-external-waits: the agent "creates a durable promise and gets a unique callback ID"; "Even if the process or infrastructure changes, the agent resumes when the approval arrives"; Restate "persists both the timer and the approval promise", so after a restart the wait continues with the remaining time.
- human-review-gates: race the approval against a timer (`orTimeout`, or `restate.select` with a sleep); the example caps the wait at "At most 3 hours, to reach our SLA" and on timeout falls back to an AI decision.
- agent-frameworks: suspended agents use no compute ("no idle billing on serverless"); integrations shown for the Vercel AI SDK, OpenAI Agents SDK and Pydantic AI.

## Key points
- Resolution: `curl .../restate/awakeables/<id>/resolve --json 'true'`; the payload is the decision value.
- No documented maximum wait; the only explicit bound is the example's 3-hour timeout.
- Approver identity and audit are not covered.

## Could not verify
- Authentication of the resolve endpoint in production deployments; whether Restate's journal records the caller of a resolve.
- Page undated; read via WebFetch (model-summarised view).
