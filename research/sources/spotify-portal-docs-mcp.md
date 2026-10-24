---
title: "MCP (Spotify Portal docs: core features and plugins)"
source_url: https://backstage.spotify.com/docs/portal/core-features-and-plugins/mcp
author: Spotify
publisher: Spotify Portal docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [pm-tool-connectivity, org-context-grounding, identity-delegation, policy-enforcement-fail-open]
relevance: medium
---

## Relevance to the project
How Spotify's commercial Backstage turns the developer portal into tools any agent can call: each plugin registers actions, one MCP endpoint serves them to AiKA, Claude Code, Cursor and Copilot. For us it is the concrete mechanism behind "Backstage as a context layer for agents", and a warning that permissions are left to each tool.

## Themes
- pm-tool-connectivity: one Streamable HTTP endpoint (`/api/mcp-actions/v1`) gathers all plugin actions (Catalog, Soundcheck, Scaffolder shown).
- org-context-grounding: agents can query ownership, templates and health data from the catalog.
- identity-delegation: two auth methods: static bearer tokens (CI, quick setup) or OAuth via client metadata discovery (CIMD).
- policy-enforcement-fail-open: per search snippet of the companion "Registering MCP Tools" page, the Actions Registry does not enforce permissions; each tool must check authorisation itself.

## Key points
- Named clients: AiKA, Claude Code, Cursor, VS Code Copilot. SSE transport deprecated.
- Built on open-source `@backstage/plugin-mcp-actions-backend`.

## Could not verify
- The "Available Tools" list and the registering-tools page were not read in full.
