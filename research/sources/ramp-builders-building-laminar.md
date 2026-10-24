---
title: Building Laminar: Ramp's Managed Agents Platform
source_url: https://builders.ramp.com/post/building-laminar
author: Sam Kronick (contributors Alexander Osmonov, Kiryl Liaushun, Vincent Capol, Alexander Shevchenko, Alex Levinson)
publisher: Ramp Builders (builders.ramp.com)
published: 2026-10-20
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-ramp-glass
themes: [build-vs-buy, harness-over-model, cost-control-routing, agent-factory-sdlc, shared-persistent-sessions]
relevance: high
---

## Relevance to the project

Ramp's own account of the harness that now runs Glass (and Stack, Inspect, support and OCR agents). It supersedes two April 2026 statements about Glass: that it was "built on Anthropic's Claude Agent SDK" (Charles) and that it "turns your laptop into a server" (Goddijn). By October Glass sits on Laminar, a provider-agnostic, cloud-first harness Ramp built in six weeks from about May 2026. This is the single most important source for the loop-source, runtime-location, model-provider-coupling and harness-upkeep dimensions, and it shows how quickly a company's answer to those choices can change.

## Themes

- **build-vs-buy**: "We studied the other offerings on the market and decided that we could do better, move faster and have stronger alignment to where we want to go by building in house." Tried "model providers' agent SDKs, managed agent APIs, open source coding agents, popular agent frameworks, third-party vendor solutions, and several generations of in-house agent frameworks". Decided ~May 2026; v1 in 6 weeks; "five months later, every agentic product at Ramp runs on Laminar". Caveat in their own words: "you still need good engineers to be on-call, keep the platform healthy, and figure out what product teams actually need".
- **harness-over-model**: the harness's 15 responsibilities (storage, compaction, MCP, queuing/steering, lifecycle hooks, durable execution, multi-provider interop, sandboxes, tool search, subagents, streaming, HITL, generative UI protocol, multiplayer, observability); provider-agnostic by design; a bespoke session-debug UI because "building great agents requires you to read the traces".
- **cost-control-routing**: Ramp Router is the LLM gateway in the architecture diagram; model choice "optimizing for cost, latency, and performance as the application demands".
- **agent-factory-sdlc**: one harness under four archetypes: interactive support chat, headless data processing (Bill Pay Contextual OCR), coding (Inspect), long-horizon knowledge work (Stack, Glass).
- **shared-persistent-sessions**: non-blocking async agents by default; sessions "always open to new input"; multiplayer sessions and deep Slack integration; session state in Postgres independent of sandbox lifetime ("sandbox-as-a-tool").

## Key points

- Glass as described here: "a general-purpose collaborative agentic coworker" that manages "subagents, automations, sandboxes, cloud browsers, and MCP connectors to complete tasks that can take minutes or hours", with multiplayer sessions and Slack integration. Elsewhere: "customizing our own desktop agent for knowledge work across the org".
- Runtime: "Going all-in on the cloud" — the whole stack runs on "a fleet of generic disposable workers"; the local-agent era of late 2025/early 2026 is called "a weird blip"; "our customers don't need to worry about where their Ramp Agents do their work, never mind if their laptop goes to sleep". Clients are "Web + desktop" (diagram).
- Stack: FastAPI API, SSE streaming, Temporal for durable orchestration, worker fleet, PostgreSQL for sessions and messages, S3, Ramp Router as LLM gateway. "Boring technology" by choice.
- Why not managed agents APIs: single-provider lock-in; building a cross-provider abstraction over several managed-agent APIs judged not much less work than building their own; in-house team sits next to product teams; own observability.
- Economics claim: with coding agents, "the cost of building and maintaining our own platform was marginal compared to taking on one or more vendor dependencies" (no numbers given). New Stack notes no cost comparison was published.
- Process: "agent-owned codebase"; "calling the codebase 'vibe coded' doesn't capture what we've built"; small team of experienced engineers steering agents; every contribution reviewed against the platform architecture. Contrast with Buchan's April account of Glass as "pretty much vibe coded".
- Four companion deep dives are linked (Tools, Sandboxes, Connectors, Developer Experience); not read.

## Notable quotes

- "Our early motto was 'build agents, not infrastructure'."
- "The operative word here is 'loop' — and the 'harness' is the thing that orchestrates and manages that loop."
- "Would we do it again? Absolutely! ... But even though building in-house has never been cheaper, you still need good engineers to be on-call."

## Could not verify

No usage, cost or reliability numbers beyond "every agentic product" and (via daily.dev's summary) "tens of millions of sessions". Whether the Glass desktop client still runs anything locally (e.g. local files) is not stated. The deep-dive posts were not read.
