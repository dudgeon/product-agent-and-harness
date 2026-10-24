---
title: "Snowflake-managed MCP server (Snowflake docs)"
source_url: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp
author: Snowflake
publisher: docs.snowflake.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [pm-tool-connectivity, identity-delegation, metrics-review-agents]
relevance: medium
---

## Relevance to the project
A representative data-warehouse MCP server. It shows how governed data reaches agents (per-tool grants, admin-created OAuth integration) and the limits: tools-only, 50 tools, 250 KB response truncation. Admin setup is a prerequisite a PM cannot do alone.

## Themes
- pm-tool-connectivity: server is a database object created by an admin via `CREATE MCP SERVER ... FROM SPECIFICATION`; OAuth security integration must be created manually (no dynamic client registration).
- identity-delegation: 'Access to the MCP Server does not give access to the tools'; each tool needs its own grant; users sign in with own credentials.
- artifact-standardization: supports only tool capabilities, not MCP resources or prompts; response truncation at 250 KB; max 50 tools; recursion depth 10.

## Key points
- Snowflake recommends exposing one Cortex Agent as the client-facing tool for governed business questions.
- Supports MCP revision 2025-11-25 per this page (search summary showed another page version saying 2025-06-18).

## Could not verify
- Protocol revision differs across page versions.
