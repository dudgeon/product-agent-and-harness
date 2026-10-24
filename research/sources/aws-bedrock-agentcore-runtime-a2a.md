---
title: Deploy A2A servers in AgentCore Runtime
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html
author: Amazon Web Services
publisher: docs.aws.amazon.com
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, identity-delegation]
relevance: medium
---

## Relevance to the project
Shows the managed-hosting route for an A2A agent on a hyperscaler: AgentCore proxies JSON-RPC to a container on port 9000, serves the Agent Card, adds session isolation and SigV4 or OAuth/JWT auth. A real, documented platform integration (supports the 'platform adoption' tier for A2A) but not evidence of user adoption.

## Themes
- `remote-agent-invocation`: Stateless streamable HTTP server on :9000; MCP servers use :8000/mcp and plain HTTP :8080; Agent Card at /.well-known/agent-card.json.
- `identity-delegation`: Inbound auth via custom JWT authorizer (e.g. Cognito) or SigV4; bearer token passed to the container via an allowed header.

## Key points
- Example uses Strands agents with the a2a-sdk (0.3.x).
- Error mapping to JSON-RPC codes (-32051 .. -32055); 5-minute client timeout in the sample.
