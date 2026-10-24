---
title: "Production-ready agents with the OpenAI Agents SDK + Temporal"
source_url: https://temporal.io/blog/announcing-openai-agents-sdk-integration
author: Cornelia Davis (Temporal)
publisher: Temporal blog
published: 2025-07-30
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, shared-persistent-sessions, cost-control-routing]
relevance: medium
---
## Relevance to the project
Shows the workflow-engine-embedded agent pattern: agent loop as a Temporal workflow with each agent invocation recorded as an activity, giving retry and resume after crashes. Vendor announcement with no customer evidence; an update says the integration reached GA on 2026-03-23.

## Themes
- agent-frameworks: the integration replaces the Agents SDK Runner so every agent invocation runs as a Temporal Activity; handoffs are also recorded; workflow code holds orchestration logic
- shared-persistent-sessions: long-running tasks that crash resume where they left off because activity results and workflow progress are stored; claimed to save compute and token costs

## Key points
- No customer examples; one demo (deep-research bot) by a Temporal colleague. Traces go to both Temporal and OpenAI dashboards.
- See hackernoon-durable-execution-compared for the independent caveats (determinism, model calls outside steps).
