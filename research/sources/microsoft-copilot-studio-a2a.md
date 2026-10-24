---
title: Connect to an agent over the Agent2Agent (A2A) protocol (Copilot Studio)
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-agent-to-agent
author: Microsoft
publisher: learn.microsoft.com
published: 2026-08-26
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, identity-delegation]
relevance: medium
---

## Relevance to the project
A shipping product that consumes remote A2A agents: a Copilot Studio agent adds an A2A endpoint (agent card auto-populates name and description) with None, API key or OAuth 2.0 auth, and delegates tasks with full chat history in metadata. The docs explicitly say the customer is responsible for permissions, data flows and oversight of external agents. Confirms A2A client support in an enterprise orchestrator.

## Themes
- `remote-agent-invocation`: Orchestrator decides when to delegate; payload carries contextId and the complete chat history, not just the last utterance.
- `identity-delegation`: Auth options None/API key/OAuth 2.0 per connection; no user-token propagation described.

## Key points
- Recommends A2A for agents on external frameworks hosted outside Copilot Studio; MCP for tools; custom connectors for plain APIs.
- Works with on-prem or VNet agents through the custom-connector infrastructure.
