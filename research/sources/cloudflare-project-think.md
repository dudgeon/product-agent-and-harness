---
title: Project Think: building the next generation of AI agents on Cloudflare
source_url: https://blog.cloudflare.com/project-think/
author: Cloudflare
publisher: Cloudflare Blog
published: 2026-04-15
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, shared-persistent-sessions, harness-over-model]
relevance: medium
---

## Relevance to the project
Cloudflare's own harness for 'third-wave' agents that run on the internet, are durable, cost nothing idle and serve many users. Useful as the contrast case to laptop-bound Claude Code in the runtime-location axis.

## Themes
- [[shared-persistent-sessions]]: fibers (`runFiber`, `stash`, recovery) give durable execution; session API stores conversations as trees with forking and FTS5 search; sub-agents are Durable Objects with their own SQLite.
- [[agent-frameworks]]: `Think` is 'an opinionated harness that handles the full chat lifecycle' with lifecycle hooks (beforeTurn, beforeToolCall, onStepFinish).
- [[harness-over-model]]: positions the harness/runtime, not the model, as the differentiator.

## Key points
- Frames Claude Code as 'second wave': runs 'on your laptop, for one user, with no durability guarantees'.
- Claims: Dynamic Workers ~100x faster/more memory-efficient than containers; a Code Mode MCP server uses ~1,000 tokens vs ~1.17M for tool-per-endpoint; 10,000 agents at 1% activity need ~100 active at once. No independent benchmarks.
- Experimental; APIs may change.
