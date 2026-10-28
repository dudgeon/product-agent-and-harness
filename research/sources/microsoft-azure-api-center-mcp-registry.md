---
title: "Inventory and Discover MCP Servers in Your API Center"
source_url: https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server
author: Microsoft
publisher: Microsoft Learn
published: 2026-05-29
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-legible-platform, legible-org-for-agents, pm-tool-connectivity]
relevance: high
---

## Relevance to the project
The clearest shipped example of an enterprise private MCP registry: Azure API Center inventories MCP servers alongside APIs, exposes a registry endpoint that VS Code and GitHub Copilot can point at, and lets the org attach custom metadata (e.g. owner, data classification) that is returned to agents in the `_meta` of tool responses. This is the nearest existing mechanism for a platform to publish governance metadata to an agent at call time, though the metadata schema is whatever the org defines.

## Themes
- agent-legible-platform: registry endpoint `https://<apic>.data.<region>.azure-apicenter.ms/workspaces/default/v0.1/servers` usable from VS Code/Copilot (Configure MCP registry metadata).
- legible-org-for-agents: custom metadata properties mapped into namespaces appear in the `_meta` section of MCP server responses to tool calls (same section).
- pm-tool-connectivity: auto-sync from Azure API Management and from Git repos keeps inventory current (Synchronize MCP servers from API sources).

## Key points
- Register remote (URL + environment) or local (npm/pypi package + runtime hint) MCP servers with title, summary, use cases, version and lifecycle stage, license, docs.
- API Center auto-generates OpenAPI definitions (SSE and streamable) for a registered remote MCP server.
- Partner MCP servers (Logic Apps, GitHub, others) can be added from a curated list.
- Portal shows tool schemas, a test console and one-click install in VS Code; registered servers can feed Microsoft Foundry private tool catalogs.
- Access to the inventory can be restricted with API Center access management.

## Could not verify
- Whether any approval workflow gates registering a new MCP server (not described on this page).
