---
title: Ask HN: Is anyone using the A2A protocol?
source_url: https://hn.svelte.dev/item/48582679
author: Hacker News commenters
publisher: Hacker News (mirror hn.svelte.dev)
published: 2026
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, agent-failure-modes]
relevance: medium
---

## Relevance to the project
The best direct practitioner read on A2A uptake: a mix of 'using it at work' (mostly enterprise/Google-ecosystem, or as a standard for endpoints, catalogs and long-running tasks) and many 'tried it, went back to MCP/HTTP'. Small, self-selected sample, but it is independent of vendor marketing.

## Themes
- `remote-agent-invocation`: Users: benclarkeio (enterprises use it heavily; startups mainly for standard endpoints, agent catalogs, long-running tasks), lazharichir ('microservices for agents'), techwizrd ('quite challenging to manage'), fhrow4484 (remote A2A agents from Gemini CLI). Skeptics: siva7 (no A2A in any final product at a large company), time0ut (over-complicated, stayed with agent-behind-MCP), thallavajhula (MCP to A2A and back), nyellin (ignores prompt caching, latency, token cost), simonreiff (assumes stable agent identity), fizx (real problem is trusting what an agent claims; needs evals).

## Key points
- Thread date shown only as '4 months ago'; 92 points on the mirror.
- Recurring theme: the hard problems are delegated authority, revocation, trust in claimed capability and evals, not message format.
- Pattern 'agent behind an MCP server' is what several skeptics use instead of A2A.

## Could not verify
- Exact thread date and the original news.ycombinator.com URL were not confirmed (mirror only). Comment attributions are paraphrased from a summariser, not read verbatim.
