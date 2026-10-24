---
title: "[FEATURE] Multi-agent collaboration across machines (Agent-to-Agent protocol) (anthropics/claude-code #28300)"
source_url: https://github.com/anthropics/claude-code/issues/28300
author: MarioK1975 and commenters
publisher: GitHub
published: 2026-02-24
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, harness-portability]
relevance: medium
---

## Relevance to the project
The main public request for A2A in Claude Code. Open eight months with about 55 comments and no comment from Anthropic staff in the thread (all commenters show author association NONE apart from a duplicate-detection bot); a GitHub search of the repo for "A2A" returns 23 issues and none shows shipped support. Most commenters solve the "developer as message broker between two Claude Code instances" problem with their own transports (git-as-wire, MCP servers, shared rooms), not A2A. So, as of 2026-10-24, Claude Code has no native A2A client; reaching an A2A agent from it means a community bridge or wrapping the A2A agent as an MCP server.

## Themes
- `remote-agent-invocation`: Requested use case is peer coordination between Claude Code instances on different machines/repos (API contracts, schemas), not delegation to an enterprise agent.
- `harness-portability`: Community answers are many incompatible bridges (apra-fleet MCP server, inter-agent-deaddrop/wire, Fleetpost, threadcarry, Sqwakie, Braid, BaseThread), several self-promotional.

## Key points
- Labels: enhancement, area:agents; state open at retrieval.
- Recurring point in comments: transport is "the easy 80 percent"; the missing pieces are an agreement/contract object and evidence of what was agreed (delivery, agreement, evidence layers).
- Related closed requests: #79507 (distributed agent teams over LAN), #48965 (multi-session coordination primitives).

## Could not verify
- Whether Anthropic has commented elsewhere on A2A; no official Anthropic statement on A2A was found by web search. Anthropic is not listed among A2A supporters in the sources read.
