---
title: "Action Fabric: MCP Server, MCP Client, and A2A explained"
source_url: https://www.servicenow.com/community/servicenow-otto-articles/action-fabric-mcp-server-mcp-client-and-a2a-explained/ta-p/3557794
author: Ashley Snyder (ServiceNow employee)
publisher: ServiceNow Community
published: 2026-06-16
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, identity-delegation, agent-protocol-security]
relevance: high
---

## Relevance to the project
ServiceNow supports A2A in both directions, but its own governance layer does not cover it: "AI Gateway currently governs MCP traffic only; A2A is outside its scope as of the current GA release." For a regulated setting that needs audit, this is a concrete finding: on at least one major enterprise platform, MCP traffic is governed and A2A traffic is not. A2A auth is per-connection OAuth 2.0 or API key, i.e. typically a service identity rather than the end user.

## Themes
- `remote-agent-invocation`: ServiceNow can be A2A client (primary, orchestrates and delegates) or server (secondary, receives tasks). Guidance: MCP for discrete "do X in that system" tool calls; A2A for "handle the Y part of this" multi-turn collaboration and long-running work. A2A needs an A2A-capable agent on the other side, setup is more complex and adds latency.
- `identity-delegation`: "A2A connections use OAuth 2.0 or API key authentication, configured per external agent in AI Agent Studio"; MCP Server Console enforces OAuth 2.1 on every connection.
- `agent-protocol-security` (proposed theme): AI Gateway governs inbound and outbound MCP; A2A outside its scope at current GA.

## Key points
- Planning an update to A2A v1.0 (forward-looking); community posts elsewhere say current support targets v0.3 and arrived with Now Assist AI Agents 6.0.x (Zurich Patch 4+, December 2025) (search snippets, not read).
- Scenarios (Workday, Salesforce, Jira) are illustrative; no customer deployments named.
- Last edited 2026-07-30.

## Could not verify
- Official ServiceNow product documentation (docs.servicenow.com) was not read; this is an employee community article. Other community posts disagree on A2A endpoint paths and note async mode silently cancels without a public callback URL (search snippets only).
