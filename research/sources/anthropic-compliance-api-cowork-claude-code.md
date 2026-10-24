---
title: Compliance API coverage extends to Claude Cowork and Claude Code
source_url: https://claude.com/blog/compliance-api-cowork-and-claude-code
author: Anthropic
publisher: claude.com blog
published: 2026-08-11
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, identity-delegation, harness-portability]
relevance: high
---

## Relevance to the project
Anthropic's own enterprise "control plane" piece for its harnesses: the Compliance API now returns consolidated, server-hosted session transcripts (prompts, responses, MCP and web tool calls, skills and artifacts) with verified user identity for Cowork and Claude Code, GA from 2026-08-26 per the update note. For a regulated build on Claude Code, this is the audit trail that a third-party control plane (Agent 365 Purview, ServiceNow) would consume. The exclusions matter: Claude Code on the web, via Claude Platform, and on Bedrock, Vertex or Foundry were not covered.

## Themes
- agent-control-plane: session endpoints are additive to the existing Compliance API; uses the Compliance Access Key.
- identity-delegation: records carry verified user ID and email, org ID, session and message IDs, timestamps.
- harness-portability: coverage depends on surface and route; a Claude Code agent run through Bedrock (e.g. on AgentCore) falls outside it and must rely on the cloud's own logging.

## Key points
- Covered: Cowork (desktop, web, mobile), Claude Code (CLI and desktop). Beta: Microsoft 365 add-ins, Claude Science.
- Not covered (at post date): Claude Code on the web, Claude Code via Claude Platform, sessions on Bedrock, Vertex AI or Microsoft Foundry.
- Body text says beta; update note dated 2026-08-26 says GA for Cowork and Claude Code.
- Secondary: Microsoft Purview ingests Claude Enterprise activity via the Compliance API (Cloud Wars, search snippet only).

## Notable quotes
- "The new endpoints are additive: nothing changes about the data you already pull from the Compliance API today."
- "This beta doesn't include Claude Code on the web"

## Could not verify
- Retention periods, public-sector exclusion (stated in support article per search snippet: Compliance API excludes Public Sector orgs). Retrieved via WebFetch (model-summarised view).
