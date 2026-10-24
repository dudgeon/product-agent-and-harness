---
title: "Use Looker with MCP, Gemini CLI and other Agents (Google Cloud docs)"
source_url: https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox
author: Google Cloud
publisher: docs.cloud.google.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [pm-tool-connectivity, metrics-review-agents]
relevance: low
---

## Relevance to the project
BI access for agents is currently done through a self-run toolbox with client ID/secret env vars (or OAuth app registration), which is heavier than the hosted OAuth servers of Amplitude or Dovetail.

## Themes
- pm-tool-connectivity: setup needs Looker URL, client ID and secret env vars, or an OAuth application; Google also mentions a Looker-managed MCP server for managed setups (details not read).

## Key points
- Docs are versioned per Looker release (2514 ... 2610) and config layout differs by version.

## Could not verify
- Only read via a web-search summary, not fetched directly; Tableau MCP (tableau/tableau-mcp, Node 22.7.5+, personal access token) was seen only in directory listings and is not filed.
