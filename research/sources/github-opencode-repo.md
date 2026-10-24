---
title: OpenCode (anomalyco/opencode) repository
source_url: https://github.com/sst/opencode
author: OpenCode maintainers
publisher: GitHub
published: unknown
retrieved: 2026-10-24
type: other
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-portability, build-vs-buy]
relevance: medium
---

## Relevance to the project
Most-starred open-source coding agent (MIT, about 221k stars at retrieval). A candidate base harness; the key risk it illustrates is dependence on vendor model access: its Anthropic subscription OAuth support was removed after legal demands (see venturebeat/new-stack coverage).

## Themes
- agent-frameworks: open-source coding agent with build/plan agents, a general subagent, desktop beta, SDK directory.
- harness-portability: provider-agnostic harness; docs say any LLM provider via API key.

## Key points
- MIT licence; about 220.9k stars, 29.5k forks; repo served from anomalyco/opencode (previously sst/opencode; rename not confirmed on page).
- Built-in agents: build (full access), plan (read-only), @general subagent.
- Docs site (opencode.ai/docs, updated 2026-10-23) notes OpenCode 1 and 2 share the opencode command and can conflict on install.

## Could not verify
- Client/server architecture, SDK docs and provider list not on the pages read; the arXiv study describes OpenCode as having the most thoroughgoing client/server architecture.

## Follow-up (2026-10-24)
Filed by research-runtime-patterns-follow-up-round.
- Enterprise offer now filed: [opencode-enterprise-docs](opencode-enterprise-docs.md) (central config plus SSO that forces traffic through an internal AI gateway; no code or context stored by OpenCode; share pages must be disabled, self-hosted share pages on the roadmap; no audit-log feature on the page; per-seat pricing).
- Anthropic OAuth removal is now dated: PR #18186 merged 2026-03-19 after legal demands ([falcao](falcao-anthropic-claude-access-crackdown.md), independent).
- Company and risk: Anomaly (ex-SST), undisclosed funding; Go and Zen paid tiers ([Ry Walker](rywalker-research-opencode.md), independent, mostly unsourced). Independent ratings: Thoughtworks Assess, April 2026 ([note](thoughtworks-radar-opencode.md)); RUBINLAKE Assess with "most permissions default to allow" ([note](rubinlake-radar-opencode.md)).
- Server and SDK: `opencode serve` exposes an HTTP server with SSE streaming and an npm SDK (@opencode-ai/sdk); TanStack AI, Promptfoo and others ship adapters that drive it (search summaries of their docs, not filed). This is the route for using OpenCode as an embedded loop rather than a fork.
