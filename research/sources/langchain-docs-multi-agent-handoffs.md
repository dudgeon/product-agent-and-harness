---
title: Handoffs (LangChain multi-agent docs)
source_url: https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs
author: LangChain
publisher: LangChain docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks, single-agent-many-skills]
relevance: high
---

## Relevance to the project
LangChain implements a handoff as a tool returning a `Command` that changes state, and recommends, for most cases, a single agent whose prompt and tools change by middleware rather than separate agents. Where separate agent subgraphs are used, it advises passing only the handoff tool call and its `ToolMessage`, "not the full subagent history". That is a first-party statement that a full-transcript handoff is often harmful.

## Themes
- handoff-context-transfer: "Pass only these two messages, not the full subagent history"; passing full history means "The receiving agent may become confused by irrelevant internal reasoning, and token costs increase unnecessarily"; a `ToolMessage` is required "whenever your handoff tool updates messages" or the receiver sees an incomplete conversation.
- single-agent-many-skills: "Use single agent with middleware for most handoffs use cases—it's simpler"; the tool sets `current_step` and middleware swaps prompt and tools.
- agent-frameworks: subgraph handoffs use `Command(goto=..., update=..., graph=Command.PARENT)` and an `active_agent` state key.

## Key points
- Summarising the subagent's work in the `ToolMessage` content is suggested when more context is needed.
- The last-message example assumes no parallel tool calls.

## Could not verify
- No measurements behind the recommendation.
