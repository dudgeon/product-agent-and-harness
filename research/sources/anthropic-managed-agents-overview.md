---
title: Claude Managed Agents overview
source_url: https://platform.claude.com/docs/en/managed-agents/overview
author: Anthropic
publisher: Claude Platform docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, shared-persistent-sessions, build-vs-buy]
relevance: high
---

## Relevance to the project
Anthropic's hosted harness: the "buy" end of the build-vs-buy ladder for a Claude-based deployed agent. It is beta and not eligible for Zero Data Retention or HIPAA BAA, which matters for enterprise governance.

## Themes
- build-vs-buy: pre-built configurable harness in managed infrastructure; you define agent, environment, session and send events.
- shared-persistent-sessions: stateful by design, event history persisted server-side, steer or interrupt, scheduled deployments on cron.

## Key points
- Concepts: Agent (model, prompt, tools, MCP, skills), Environment (Anthropic cloud sandbox or self-hosted sandbox), Session, Events.
- Built-in tools: bash, file ops, web search/fetch, MCP.
- Status: beta (header managed-agents-2026-04-01); MCP tunnels and dreaming in limited research preview.
- Because stateful, not currently eligible for ZDR or HIPAA BAA; sessions and uploaded files can be deleted via API.
- Pricing not on this page (a third-party blog cites $0.08 per session-hour with free tier; unverified).

## Could not verify
- Pricing not verified from a primary source.
