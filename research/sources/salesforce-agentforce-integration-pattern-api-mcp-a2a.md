---
title: "Choose the Right Agentforce Integration Pattern: API, MCP, or A2A"
source_url: https://www.salesforce.com/blog/how-to-choose-integration-pattern-for-agentforce/
author: Scott Ratliff (Principal Architect Evangelist, Salesforce)
publisher: Salesforce Blog
published: 2026-04-01
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, skill-supply-chain-security]
relevance: medium
---

## Relevance to the project
Salesforce's own decision rule for when an Agentforce agent should use a plain API, MCP or A2A. Useful because it is a vendor that ships all three saying A2A is for delegating to an agent that already exists or to split load off an overloaded main agent, while APIs remain the route for sensitive data and bulk work. As of April 2026 both MCP and A2A were beta in Agentforce, and no customer is named.

## Themes
- `remote-agent-invocation`: API when data is sensitive or bulk, or APIs already configured; MCP when a suitable server exists or reuse is high; A2A when "an external agent for the use case already exists" or "specialization of agents is needed to reduce strain on the main interfacing agent". Keep an agent under about 10 topics before splitting.
- `skill-supply-chain-security`: For MCP, if a tool description changes significantly, Agentforce suspends the tool until an admin reviews it (a concrete rug-pull control). A2A discovery is via Agent Card and an OAuth 2.0 handshake.

## Key points
- Describes "two beta features for Agentforce, Model Context Protocol (MCP) and Agent2Agent (A2A)".
- Hypothetical order-returns example only; no named customers or traffic.
- Salesforce's architect interoperability guide (not read; search snippet) describes A2A Outbound with admin registration of each external agent's skills and A2A Inbound for external agents calling Agentforce.

## Could not verify
- Current (October 2026) GA status of Agentforce A2A; Salesforce developer docs on A2A were not reached.
