---
title: "Getting started with the Atlassian Rovo MCP server"
source_url: https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [harness-portability, identity-delegation]
relevance: high
---

## Relevance to the project

Shows how a major PM-artifact platform exposes itself to external agents: a remote MCP server on OAuth 2.1 that respects the user's permissions, metered in Rovo credits. This is the access path a product meta-harness would use for Jira and Confluence rather than a bespoke integration.

## Themes

- harness-portability: any MCP-compatible client can connect; setup guides for Claude Code, Claude Desktop, Cursor, Codex, VS Code/Copilot, Windsurf.
- identity-delegation: OAuth 2.1 primary; actions respect each user's existing access controls; API token optional.

## Key points

- Server URL https://mcp.atlassian.com/v2/mcp; v1 usage moves to v2 tools on 2027-03-01 (per the page).
- Covers Jira, Jira Service Management, Confluence, Bitbucket, Projects, Goals, plus Loom recordings; named context tools include getTeamworkGraphContext and searchAtlassian.
- Usage draws from the organisation's shared Rovo credit pool (also used by Rovo Chat, Studio, Agents and Teamwork Graph); cost per call depends on context volume and reasoning depth.
- A ?tools=all override exposes a flat paginated tool list for MCP gateways.

## Could not verify

Plan allowances / credit limits sit on a separate page not fetched. Page said it does not mention Compass.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.
