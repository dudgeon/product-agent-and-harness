---
title: "Introducing the MCP Registry"
source_url: https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
author: Model Context Protocol maintainers
publisher: MCP blog
published: 2025-09-08
retrieved: 2026-10-28
type: article
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-legible-platform, legible-org-for-agents, agent-protocol-security]
relevance: high
---

## Relevance to the project
The MCP Registry establishes the pattern most likely to carry "what internal platforms expose to agents": one open upstream catalog with an open OpenAPI spec, and private enterprise sub-registries that pull from it and add curation. For a dependency agent, a private sub-registry is the obvious place an internal platform would list its agent interface; but the registry describes servers and tools, not intake requirements, approvers or lead times.

## Themes
- agent-legible-platform: registry is "an open catalog and API" for publicly available MCP servers; its OpenAPI spec is open so others can build compatible sub-registries (Overview).
- legible-org-for-agents: private sub-registries are expected "within enterprises that have strict privacy and security requirements", using the public registry as single upstream (Sub-registries).
- agent-protocol-security: moderation is by community flagging and maintainer denylisting, retroactively removing entries (Moderation).

## Key points
- Preview launched 8 Sep 2025, no data-durability guarantees during preview.
- Public "MCP marketplaces" tied to clients are expected to curate on top of upstream data.

## Notable quotes
- "Registry maintainers can then denylist these entries and retroactively remove them from public access."

## Could not verify
- server.json fields and namespace verification (DNS/GitHub) were not covered in this post.
