---
title: Sentry MCP Server (remote, OAuth) with Seer analysis
source_url: https://docs.sentry.io/ai/mcp/
author: Sentry
publisher: docs.sentry.io
published: unknown
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, identity-delegation]
relevance: medium
---

## Relevance to the project
A production-grade vendor-hosted remote MCP server (OAuth, no install) that exposes Sentry data plus Seer, Sentry's own root-cause-analysis agent, to Claude Code and others. A real example of a vendor agent reached from a general harness, and of OAuth skill-level scopes at approval time. No independent account of quality was found.

## Themes
- `remote-agent-invocation`: Endpoint https://mcp.sentry.dev/mcp; example prompt 'Use Sentry's Seer to analyze and propose a solution for issue'.
- `identity-delegation`: OAuth consent lets the user grant permission sets (a test doc lists inspect, docs, triage, seer, project-management).

## Key points
- Hosted and managed by Sentry; mcp-remote bridge is the fallback for clients without native OAuth or Streamable HTTP.
- Seer is paid; exact Seer tool name not confirmed.

## Could not verify
- Found via search excerpts; page not read in full. Exact tool names and whether Seer calls are asynchronous were not verified.
