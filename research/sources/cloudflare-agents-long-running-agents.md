---
title: "Long-running agents (Cloudflare Agents SDK docs)"
source_url: https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/
author: Cloudflare
publisher: Cloudflare Developers docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, agent-frameworks, memory-architecture]
relevance: high
---
## Relevance to the project
Primary docs for durable persistent agents on Durable Objects: durable identity that runs intermittently, SQLite-backed state, alarms, fibers/checkpoints and Workflows delegation. It states what is lost on eviction and that idempotency and recovery logic are the developer's job. Reference for the persistent-deployed and workflow-engine axes. Cross-reference Track 1 for Cloudflare OS.

## Themes
- shared-persistent-sessions: agents are 'durable identities, not always-on processes': wake on HTTP, WebSocket, RPC, alarm or inbound email, hibernate after about 2 minutes idle; eviction can occur at any point
- memory-architecture: state survives via setState/this.sql/scheduled tasks/fiber stash; lost: in-memory fields, timers, in-flight fetches, closures
- agent-frameworks: recovery after eviction is not automatic replay: onFiberRecovered runs and 'you decide what resuming means'; keepAlive suits minutes not hours, use Workflows for longer work

## Key points
- Caveats listed by the docs: idempotency is your responsibility; destroy() deletes all data; long histories can exhaust the context window; the doc's own example executeNextStep marks a step failed but does not reschedule, so the plan stalls.
- Version note: the docs were read at the current published page; search surfaced versions 0.20.1 and 0.24.0 with differences in fiber details.
