---
title: "AI (Backstage documentation)"
source_url: https://backstage.io/docs/ai/
author: Backstage project (CNCF; Spotify-originated)
publisher: backstage.io
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [legible-org-for-agents, skill-standards, skills-marketplace, agent-stewardship, pm-tool-connectivity]
relevance: high
---

## Relevance to the project
Open-source Backstage (docs v1.56.0) now treats AI at three layers: the catalog models AI resources (skills and governance rules as owned entities, MCP servers as API entities), an MCP Actions Backend exposes portal features as tools, and Backstage publishes its own skills for coding assistants. That makes the catalog a registry for agent assets with owners and lifecycle, which is close to what a product-agent harness needs for skills and context.

## Themes
- legible-org-for-agents: catalog as a context source agents query (catalog, Software Templates, search) via MCP.
- skill-standards: an `AiResource` kind models skills and governance rules with ownership, lifecycle and dependencies.
- skills-marketplace: Backstage publishes skills at a well-known endpoint, installable into repos with `skills.sh` (e.g. migrate plugins to the new frontend system, move from Material UI to Backstage UI).
- agent-stewardship: AI resources carry an owner like any other entity.
- pm-tool-connectivity: MCP servers are recorded as `API` entities with `type: mcp-server` and `remotes` endpoints.

## Key points
- MCP Actions Backend: Streamable HTTP, OAuth via Client ID Metadata Documents; can be split into several focused MCP servers by action-ID filters.
- Named clients: Claude, Cursor, VS Code Copilot.

## Could not verify
- Subpages (AI in the catalog field list, well-known actions/skills) not read; no publication date.
