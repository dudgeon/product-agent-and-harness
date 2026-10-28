---
title: "Opal Security Launches Opal Zero to Make Least Privilege a Reality for Enterprise AI Agents"
source_url: https://www.ciodive.com/press-release/20260916-opal-security-launches-opal-zero-to-make-least-privilege-a-reality-for-ente-1/
author: Opal Security
publisher: CIO Dive (press release)
published: 2026-09-17
retrieved: 2026-10-28
type: other
evidence: vendor-claim
filed_by: research-dependency-agent
themes: [agent-originated-requests, identity-delegation, agent-stewardship, governance-as-code]
relevance: high
---

## Relevance to the project
The furthest-reaching commercial example found of an agent requesting its own access and getting a policy decision automatically: the agent submits a request through Opal's MCP server, a reasoning model evaluates it against written policy and context (owner, purpose, whether it asks for more than its owner holds), decisions route to the agent's owner where needed, and the grant is written as scoped, time-limited policy enforced by existing MCP gateways. Vendor launch claims; no independent evaluation.

## Themes
- agent-originated-requests: "The agent submits its own access request through Opal's MCP server."
- governance-as-code: Gateway Sync writes each decision as policy specifying what the agent can reach, how long, whose approval, and when it ends; enforced by Databricks Unity Gateway and AWS AgentCore Gateway at launch.
- agent-stewardship: decisions route to the agent's owner, who can revoke or deactivate; agents flagged for review when ownership or purpose changes.
- identity-delegation: integrations with Okta Cross App Access, Claude Enterprise-Managed Authorization for MCP, Claude Compliance API; inventory from Okta, Entra, AgentCore, OpenAI, Cursor.

## Key points
- Opal Labs claims >96% of non-human identities have no recorded purpose and only 10% of their access was reviewed in the past year (vendor research).
- Design partners named: Faire, Databricks, Elastic, Superhuman; GA end of September 2026; launch price $30,000 for 12 months.

## Notable quotes
- "Least privilege for agents means grants that expire, an owner for every agent, and a decision at the point of access."

## Could not verify
- Any figure above; how the policy model's decisions are audited for error.
