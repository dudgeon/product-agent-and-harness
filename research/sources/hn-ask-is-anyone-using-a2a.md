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
- Exact thread date and the original news.ycombinator.com URL were not confirmed (mirror only). Comment attributions are paraphrased from a summariser, not read verbatim. (Resolved in the follow-up below.)

## Follow-up (2026-10-24)
Filed by research-runtime-patterns-follow-up-round. Read verbatim through the HN Algolia API (`hn.algolia.com/api/v1/items/48582679`). Original URL: https://news.ycombinator.com/item?id=48582679. Posted 2026-06-18 by asim; 96 points; 31 top-level comments.

- **Date:** 2026-06-18 (so `published` above should read 2026-06-18).
- **Usage numbers in the thread:** benclarkeio, who says he is biased because he publishes A2A packages, cites a2a-sdk at "~10.9M" monthly downloads against MCP's 257M, "so MCP is downloaded about 24x more than A2A", and says A2A is more popular in enterprise than startups. Current figures are in [pepy-a2a-sdk-downloads](pepy-a2a-sdk-downloads.md).
- **Verbatim short quotes:** siva7: "not a single use case i witnessed used a2a in the final product". time0ut: "we tried it a bit, but have stayed with agent-behind-MCP style patterns for now". thallavajhula: "for the most part, it's back to Agent <> MCP now". lazharichir: "I am using A2A at work. It's a bit like the 'microservices architecture' for agents". techwizrd: "I'm using it at work as well. It's quite challenging to manage." bckr: built an AgentCard registry and SSE messaging, "then we realized we didn't need an agent on the other side". holografix: "nothing stops me from having a full blown agent _behind_ my MCP server". ahmed89: "who delegated that authority? what it's allowed to do? whether that authority has been revoked?" pfannl: "Agent identity is just OAuth in a fake mustache."
- **Harness signal not in the original note:** roblourens (on the VS Code team) says VS Code is "rebuilding our agent infrastructure on top of a new protocol, AHP" (Microsoft's Agent Host Protocol, a multi-client session protocol, not A2A). broknbottle claims Gemini CLI "is deprecated and replaced by antigravity-cli" (unverified).
- **Other:** calny points to a skeptical talk by Laurie Voss on agent protocols (not watched). david_shi: "There's a way higher incentive to build an MCP server than an A2A one".
