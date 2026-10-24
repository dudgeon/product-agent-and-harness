---
title: "When AI Agents Go Rogue: Agent Session Smuggling Attack in A2A Systems"
source_url: https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/
author: Royce Lu, Jay Chen (Palo Alto Networks Unit 42)
publisher: Unit 42
published: 2025-10-31
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-protocol-security, remote-agent-invocation, human-review-gates]
relevance: high
---

## Relevance to the project
A worked attack on stateful agent-to-agent delegation: a malicious remote agent uses an established A2A session to inject instructions into the calling agent across turns, causing data leakage and an unauthorised stock purchase. Unit 42 is a security vendor (it sells defences) but has no stake in A2A adoption, so this is labelled independent. The lesson applies to any route where an intent-shaping agent delegates to an agent it does not control (A2A or an agent behind MCP): the remote is an untrusted, adaptive input, and sensitive actions need out-of-band human confirmation.

## Themes
- `agent-protocol-security` (proposed): Not a protocol flaw ("This research does not reveal any vulnerability in the A2A protocol itself"); the weakness is agents trusting collaborating agents by default, and it applies to any stateful agent-to-agent protocol.
- `remote-agent-invocation`: Test setup: Google ADK and A2A; client = ADK financial-advisor sample on Gemini 2.5 Pro with buy/sell tools; malicious remote = research assistant on Gemini 2.5 Flash.
- `human-review-gates`: First mitigation is human approval of sensitive actions delivered out of band, outside the LLM's influence; also show remote instructions and tool calls to the user.

## Key points
- PoC 1: through follow-up questions the client disclosed chat history, system instructions, tools and schemas. PoC 2: client invoked `buy_stock` for 10 shares without the user asking.
- Injected instructions are invisible to end users who see only the final consolidated answer.
- Mitigations: human-in-the-loop for sensitive actions; context grounding (terminate if remote drifts from the original intent); signed AgentCards for verified identity; user visibility of remote exchanges.
- Not observed in the wild; "its low barrier to execution makes it a realistic risk".

## Could not verify
- Whether A2A v1.0 (March 2026) changes anything relevant; the research predates it (the authors say it is not protocol-specific).
