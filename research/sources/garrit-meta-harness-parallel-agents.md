---
title: Be using a meta harness for agents
source_url: https://garrit.xyz/posts/2026-07-15-you-should-be-using-a-meta-harness-for-agents
author: Garrit Franke
publisher: Garrit's Notes
published: 2026-07-15
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness]
relevance: medium
---

## Relevance to the project
Shows the other common meaning of 'meta harness' in practitioner use: a local parallel-session manager (Conductor, Superset, Cursor) rather than a governance layer. Notes the context-switching limit.

## Themes
- [[meta-harness]]: defines it as an environment that manages many parallel agents (new sessions on demand, optional git worktree, notifications). Recommends Conductor (polished, Claude Code/Codex), Cursor ('not strictly a meta harness'), Superset (most flexible, his favourite).

## Key points
- Trade-off: heavy context switching; suits quick tasks; for larger features he still uses an IDE with one focused agent.
- Single-user anecdote.
