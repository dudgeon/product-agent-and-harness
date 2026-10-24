---
title: "Notion MCP (Notion developer docs)"
source_url: https://developers.notion.com/docs/mcp
author: Notion
publisher: developers.notion.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [pm-tool-connectivity, identity-delegation]
relevance: medium
---

## Relevance to the project
Notion is a common home for PRDs and wikis. Its MCP is hosted and OAuth-based, so reachable from Claude Code, but client allow-listing and connection revocation are enterprise-gated admin features, an example of permissions friction.

## Themes
- pm-tool-connectivity: remote MCP hosted by Notion; connection by OAuth; search, read, create, update pages and databases; Claude Code, Cursor and Codex named as clients.
- identity-delegation: workspace owners manage allowed MCP clients in Settings; restricting clients requires Enterprise; org owners can list/revoke members' connections via Admin API.

## Key points
- Page does not specify rate limits or quotas.

## Could not verify
- Tool list is on a separate Supported tools page, not read.
