---
title: Rovo A2A (Atlassian A2A Gateway developer documentation)
source_url: https://developer.atlassian.com/cloud/rovo-a2a/
author: Atlassian
publisher: developer.atlassian.com
published: 2026-08-07
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, identity-delegation, pm-tool-connectivity]
relevance: high
---

## Relevance to the project
Atlassian runs a hosted A2A server in front of Rovo so external agents (Gemini is the featured one) can hand Jira and Confluence requests to Rovo, acting as the signed-in user. For a PM intent-shaping agent this is the most directly relevant A2A endpoint found: the systems where intent and constraints live (Jira, Confluence) are reachable as an agent over A2A as well as tools over the Rovo MCP server. It is also the clearest example of A2A carrying user-delegated authority (OAuth, user's own permissions), unlike Copilot Studio or ServiceNow API-key setups.

## Themes
- `remote-agent-invocation`: Third-party agents call Rovo (direction is inbound only; Rovo does not call out). Agent card at `https://a2a.atlassian.com/.well-known/agent.json`. Sync responses capped at "roughly 30 seconds" by the CDN; use `message/stream` for longer requests.
- `identity-delegation`: "OAuth 2.0 only" with PKCE; clients register via Dynamic Client Registration (manual client creation not supported); "All actions respect the authenticated user's existing Atlassian permissions." Org admins must enable A2A and can turn it off; org AI and Rovo policies still apply (support page).
- `pm-tool-connectivity`: Atlassian positions MCP for invoking individual tools and A2A for handing off "higher-level requests to Rovo"; separate domains (`mcp.atlassian.com` vs `a2a.atlassian.com`); MCP also accepts API tokens, A2A does not.

## Key points
- Implements A2A protocol version 0.3.0 (not v1.0) as of the 2026-08-07 update.
- A community post titled "Now GA: Connect any third-party AI agent to Rovo with A2A" exists; its body could not be read.
- Support page ([Set up Agent2Agent connections](https://support.atlassian.com/atlassian-ai-gateway/docs/set-up-agent2agent-connections/), undated, read 2026-10-24): two setup paths (pick Rovo from the other agent's catalog, or paste the agent card URL), OAuth 2.1 sign-in, "Rovo can't do anything you can't already do"; Gemini via Google Cloud Marketplace is the only named partner. No mention of audit logging.

## Could not verify
- GA date, usage numbers, named customers, whether Atlassian admin audit logs record A2A calls. Community GA post body not retrievable.
