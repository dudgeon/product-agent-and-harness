---
title: "Amplitude MCP in Claude Code (Amplitude docs)"
source_url: https://amplitude.com/docs/amplitude-ai/amplitude-mcp/claude-code
author: Amplitude
publisher: amplitude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [pm-tool-connectivity, metrics-review-agents, identity-delegation]
relevance: medium
---

## Relevance to the project
Shows that a major product-analytics tool is reachable from Claude Code via a hosted, OAuth-authenticated MCP server, so connectivity for Amplitude is not the blocker; the friction is per-region setup and per-user auth.

## Themes
- pm-tool-connectivity: `claude mcp add -t http -s user Amplitude https://mcp.amplitude.com/mcp`, then OAuth via /mcp; EU customers use a different URL and must re-run and re-authenticate to switch.
- identity-delegation: server inherits the authenticating user's Amplitude permissions and grants nothing extra.

## Key points
- Queries cover funnels, cohorts, charts, dashboards, experiments.
- Page lists no specific tools, rate limits or plan requirements.
- Scope flag `-s user` makes it global; `-s local` limits to one project directory.

## Could not verify
- Tool list, rate limits and plan tier not stated.
