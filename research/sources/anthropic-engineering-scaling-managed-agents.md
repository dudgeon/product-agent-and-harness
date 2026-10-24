---
title: "Scaling Managed Agents: Decoupling the brain from the hands"
source_url: https://anthropic.com/engineering/managed-agents
author: Lance Martin, Gabe Cemaj, Michael Cohen (Anthropic)
publisher: Anthropic Engineering
published: 2026-04-08
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, meta-harness, harness-portability, agent-frameworks]
relevance: high
---
## Relevance to the project
The clearest primary statement of the durable-session architecture: session as an append-only log outside both harness and sandbox, so a crashed harness is restarted with wake(sessionId) and a failed container is just a tool error. This is the reference design for the 'persistent-deployed' pattern and also frames Managed Agents as a meta-harness with stable interfaces. Vendor claims; no independent measurement.

## Themes
- shared-persistent-sessions: first design ran session, harness and sandbox in one container, making it a 'pet'; decoupling into session (durable log), harness (loop) and sandbox (hands) lets any piece fail or be replaced (Decoupling)
- meta-harness: harness is explicitly treated as replaceable behind stable interfaces ('brains' stateless, 'hands' = execute(name,input)->string); cited example: context resets needed for Sonnet 4.5 became unnecessary with Opus 4.5
- memory-architecture: the session log is the durable store outside the context window; getEvents() allows positional slices and rewind; irreversible compaction is avoided in the store (Session as durable event store)
- harness-portability: credentials are never visible to the harness; git tokens used at sandbox init, MCP OAuth tokens held in a vault behind a proxy (Credential handling)
- harness-over-model, build-vs-buy (added by research-agent-runtime-patterns-taxonomy, Track 2): central claim is that 'harnesses encode assumptions about what Claude can't do on its own' and those assumptions go stale as models improve (a context-reset for Sonnet 4.5 'context anxiety' was dead weight on Opus 4.5); relevant to the maintenance cost of any own harness.

## Key points
- Reported performance: p50 time-to-first-token down about 60% and p95 over 90% from provisioning containers only when needed (Anthropic's claim, no method given).
- Crash recovery: new harness reloads the event log and resumes from the last event; container failure becomes a tool-call error Claude can handle.
- Debugging benefit stated: in the coupled design a harness bug, a dropped packet and an offline container looked identical in the event stream.

## Could not verify
- Whether Managed Agents sessions are multi-user is not stated in this post.
