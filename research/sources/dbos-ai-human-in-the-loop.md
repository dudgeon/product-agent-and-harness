---
title: "Human-in-the-Loop (DBOS AI docs)"
source_url: https://docs.dbos.dev/ai/hitl
author: DBOS
publisher: DBOS docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [durable-external-waits, human-review-gates, agent-frameworks]
relevance: medium
---

## Relevance to the project
DBOS keeps an agent's wait in the application's own Postgres: `DBOS.recv` blocks the workflow durably with a deadline, `DBOS.send` from an HTTP endpoint delivers the answer, and an "inbox" lists every agent waiting for input. Because the waiting state is rows in the application database, the list of open asks is queryable like any other record, which is close to what a dependency register needs; the docs leave authentication and "who answered" to the implementer.

## Themes
- durable-external-waits: "Because the workflow's progress is checkpointed and both the deadline and notification are stored in your database", an agent can wait "hours or days" and after a restart or upgrade "will recover and keep waiting until the notification arrives or the deadline is reached".
- human-review-gates: timeout is the denial branch ("Agent denied or timed out"); the agent publishes status with `DBOS.set_event`; `/agents/waiting` lists PENDING workflows whose status is `pending_approval`.
- agent-frameworks: "All messages are persisted to the database", so a completed send reaches the workflow.

## Key points
- Endpoint `/agents/{agent_id}/respond` calls `DBOS.send(agent_id, response)`; no authentication shown.
- No maximum wait stated. Companion example: https://docs.dbos.dev/python/examples/agent-inbox (not read in full).
- Already cited in the independent comparison [hackernoon-durable-execution-compared](hackernoon-durable-execution-compared.md) as the option for app-data transactions.

## Could not verify
- Whether the persisted message is retained as an audit record, and for how long.
- Page undated; read via WebFetch (model-summarised view).
