---
title: Effective context engineering for AI agents
source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
author: Anthropic Applied AI team
publisher: Anthropic Engineering
published: 2025-09-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-over-model, memory-architecture]
relevance: high
---

## Relevance to the project
Defines context engineering and its core techniques (compaction, structured note-taking, sub-agents, just-in-time retrieval): the context-management part of what a harness must do. Useful as the checklist for judging what a framework leaves to you.

## Themes
- harness-over-model: treats curating the tokens the model sees at each step as the harness job.
- memory-architecture: structured note-taking to memory outside the context window.

## Key points
- Context is a finite resource with diminishing returns.
- Compaction: summarise near-limit context and restart with the summary.
- Sub-agents work in clean windows and return condensed summaries.
- Just-in-time retrieval via lightweight references (paths, queries) rather than preloading.

## Notable quotes
- "must be treated as a finite resource with diminishing marginal returns"
