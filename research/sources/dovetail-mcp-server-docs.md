---
title: "Dovetail MCP (Dovetail developer docs)"
source_url: https://developers.dovetail.com/docs/mcp
author: Dovetail
publisher: developers.dovetail.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [pm-tool-connectivity, feedback-triage-agents, identity-delegation]
relevance: high
---

## Relevance to the project
A research repository (Dovetail) is reachable via MCP and can both read (transcripts, highlights, docs as markdown) and write, but the auth model shows typical gaps: no dynamic client registration, API-token fallback, and some clients needing a self-hosted STDIO server.

## Themes
- pm-tool-connectivity: hosted endpoint https://dovetail.com/api/mcp; OAuth 2.1 with protected-resource metadata, or Bearer API token; DCR and CIMD unsupported so some clients must use tokens.
- pm-tool-connectivity: read covers search, projects, folders, data entries, docs as markdown, highlights, comments, themes, tags, file URLs; write covers create projects/docs/highlights/comments/tags; docs list no update or delete tools and no rate limits.
- identity-delegation: access matches the user's own account/role (from search summary of the main Dovetail help page).

## Key points
- File uploads single PUT, capped at 5 GB; download URLs short-lived presigned links.
- Search summary also said HIPAA workspaces disable API key generation by default, which disables MCP connectors (not verified on the page itself).

## Could not verify
- HIPAA claim not verified on a first-party page.
- Whether the hosted endpoint is GA vs beta not stated.
