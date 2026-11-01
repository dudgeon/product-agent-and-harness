---
title: Multi-agent (LangChain docs)
source_url: https://docs.langchain.com/oss/python/langchain/multi-agent
author: LangChain
publisher: LangChain docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, single-agent-many-skills, agent-frameworks, cost-control-routing]
relevance: high
---

## Relevance to the project
LangChain's 2026 docs present five multi-agent patterns side by side, including "skills" (one agent loading context on demand) as a multi-agent alternative, and say who talks to the user in each: subagents never talk to the user, handoff agents do. The model-call comparison table is one of the few published side-by-side cost figures. Directly maps onto model B (subagents or skills under one agent) versus a control-transfer chain.

## Themes
- handoff-context-transfer: subagents "start fresh on each invocation" and "all routing passes through the main agent"; handoffs: "Tool calls update a state variable that triggers routing or configuration changes" and the active agent persists across turns.
- single-agent-many-skills: skills pattern: "A single agent stays in control while loading context from skills as needed"; best for focused tasks and repeat requests.
- agent-frameworks: patterns are subagents, handoffs, skills, router, custom workflow.
- cost-control-routing: table of model calls: multi-domain task: subagents 5 calls about 9K tokens; handoffs 7+ calls about 14K+ tokens; skills 3 calls about 15K tokens; router 5 calls about 9K tokens.

## Key points
- "At the center of multi-agent design is context engineering—deciding what information each agent sees."
- Handoffs noted as strong for multi-hop tasks and direct user interaction, weaker for multi-domain work because they run sequentially.
- Subagents recommended for distributed development, parallelisation, too many tools, or domains that need extensive context.

## Could not verify
- How the call and token counts were measured (illustrative scenario, not a benchmark).
