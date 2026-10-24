---
title: A2A joins AAIF's open agentic stack
source_url: https://aaif.io/blog/a2a-joins-aaif
author: Agentic AI Foundation (AAIF)
publisher: aaif.io
published: 2026-08-17
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
A2A moved from its own Linux Foundation project into the Agentic AI Foundation, the LF directed fund that already hosts MCP, AGENTS.md and goose (and, from 2026-10-22, Agent Skills). So MCP and A2A now share one foundation, which OpenAI and Anthropic co-founded. This is the first A2A announcement that names production users, but the named ones are consumer-phone and commerce cases, not enterprise agent-to-agent traffic of the kind an internal intent-shaping agent would need. It bears on whether to expect A2A or MCP as the route to deployed agents (remote-invocation-route).

## Themes
- `remote-agent-invocation`: A2A joins AAIF as a hosted project; AAIF frames MCP (agent-to-tool) and A2A (agent-to-agent) as complementary layers of one stack, with no merger or joint interop spec mentioned.
- `vendor-claims-vs-independent-evidence`: Names Huawei (Celia OS assistant to in-app agents on HarmonyOS), Tencent WeChat (integrating with Huawei and other Android OEM assistants "over A2A"), and Google Cloud plus PayPal (agentic commerce with AP2). The WeChat claim is not confirmed by independent reporting, which does not name the protocol (see [KrASIA](kr-asia-wechat-phone-agents-a2a.md)).

## Key points
- History as stated: launched by Google April 2025; donated to LF with AWS, Cisco, Microsoft, Salesforce, SAP, ServiceNow as founding organisations; IBM's ACP merged into A2A in August 2025; v1.0 in March 2026 (multi-protocol bindings, version negotiation, multi-tenancy, signed agent cards).
- Adoption claim: 150+ organisations; "production use in supply chain, financial services, and mobile platforms". No volumes, no enterprise customer named.
- Platform support listed: Google Cloud (ADK, Agent Engine, Cloud Run, GKE), Azure AI Foundry, AWS Bedrock AgentCore.
- Quotes from AAIF CTO Manik Surtani and Google Cloud's Rao Surapaneni.
- The A2A project's own post dates the move 2026-08-27 and says A2A was accepted at "Growth Stage" ([A2A blog](a2a-project-joining-aaif.md)).
- Confirms the IBM ACP merger (August 2025) at a primary-ish source, which Track 3 had only from search summaries.

## Notable quotes
- "As organizations move multi-platform agentic systems into production, interoperability is becoming essential" (Rao Surapaneni, Google Cloud).

## Could not verify
- Huawei and WeChat use of the LF A2A protocol (as opposed to a Huawei HarmonyOS agent protocol or Huawei's telecom A2A-T) was not confirmed at a primary Huawei or Tencent source.
- Whether the PayPal and Google Cloud agentic commerce offering (announced 2025-10-28) is generally available with live A2A traffic.
