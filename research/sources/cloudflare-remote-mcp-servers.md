---
title: Build and deploy Remote Model Context Protocol (MCP) servers to Cloudflare
source_url: https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/
author: Cloudflare
publisher: blog.cloudflare.com
published: 2025-03-25
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, identity-delegation]
relevance: medium
---

## Relevance to the project
Shows the hosting pattern for a remote agent behind MCP on an edge platform: workers-oauth-provider makes the MCP server its own OAuth provider (and a client of GitHub/Google), McpAgent on Durable Objects holds per-session state. Directly relevant to org-deployed services that must authenticate users and call upstream systems.

## Themes
- `identity-delegation`: The MCP server issues its own tokens to clients and keeps upstream tokens encrypted in KV, which lets it enforce narrower permissions than the upstream token.
- `remote-agent-invocation`: McpAgent (Agents SDK) + Durable Objects give each MCP session persistent SQL state across tool calls.

## Key points
- Package: workers-oauth-provider, McpAgent, mcp-remote, AI Playground as remote MCP client.
- Post dated 2025-03-25 (metadata); page last modified 2026-07-15. Pre-dates stateless MCP and Tasks.
- The post describes agents as MCP clients; it does not describe hosting an agent as an MCP server.

## Could not verify
- Cloudflare OS / Agents Week material is Track 1's scope and was not read here.
