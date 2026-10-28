---
title: "Dev Portal MCP server (Kong Konnect)"
source_url: https://developer.konghq.com/dev-portal/mcp-servers/
author: Kong
publisher: Kong Developer docs
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-originated-requests, agent-legible-platform, onboarding-as-code]
relevance: high
---

## Relevance to the project
The clearest shipped example of an API platform's onboarding being legible and submittable by an agent: every Kong Dev Portal can expose an MCP server from which an agent lists APIs, reads specs and the portal's registration form, and (if write operations are enabled) creates an application and registers it to an API for the developer. Two human checkpoints remain by design: agents "can never generate application's credentials themselves", and registration still goes through the portal's approval settings (manual by default).

## Themes
- agent-legible-platform: read tools: `list_apis`, `fetch_api_spec(_raw)`, `list_api_documents`, `get_portal_form`, `list_application_auth_strategies` and others (Tools).
- agent-originated-requests: write tools `create_application`, `create_application_registration`, `delete_*` require Dev Portal login plus the "MCP server write operations" toggle under AI Settings.
- onboarding-as-code: modes: public read-only, authenticated read-only, authenticated read-write; OAuth 2.0 with PKCE for clients that support discovery.

## Key points
- Authorising the MCP connection does not grant API credentials; a developer creates them and shares them separately.
- The page does not say whether manual approval applies to agent-created registrations; Kong's self-service docs say developer sign-ups and app creation require admin approval by default (see `kong-docs-dev-portal-self-service`).
- Kong blog (24 Sep 2026, search result) announced a dedicated MCP server for every Dev Portal.

## Notable quotes
- "Agents can never generate application's credentials themselves."
