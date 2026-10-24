---
title: Deep Agents vs LangChain vs LangGraph
source_url: https://langchain.com/blog/deep-agents-vs-langchain-vs-langgraph
author: Sydney Runkle (LangChain)
publisher: LangChain blog
published: 2026-08-06
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-over-model]
relevance: medium
---

## Relevance to the project
LangChain's 2026 layering: Deep Agents (harness) is "just the core LangChain agent plus middleware", built on LangGraph. Shows a major framework vendor repositioning around the harness, and middleware as the extension mechanism.

## Themes
- agent-frameworks: runtime gives most control and least abstraction; harness the inverse; all composable.

## Key points
- Deep Agents includes filesystem, subagents, skills, memory, context compression defaults.
- Advice: start with Deep Agents, drop to LangChain for loop control, LangGraph for deterministic custom workflows.

## Notable quotes
- "The runtime offers the most control and the least abstraction; the harness offers the inverse."
