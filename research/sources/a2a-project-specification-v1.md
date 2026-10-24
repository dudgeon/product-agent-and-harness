---
title: Agent2Agent (A2A) Protocol Specification
source_url: https://a2a-protocol.org/latest/specification/
author: A2A Project (Linux Foundation)
publisher: a2a-protocol.org
published: 2026-03
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, harness-portability]
relevance: high
---

## Relevance to the project
The normative spec for the main vendor-neutral protocol for calling a deployed agent that runs its own loop and tools. It defines what a 'deployed task-specific agent called from a general harness' would look like on the wire (Agent Card, task lifecycle, streaming, push, auth). Bears on the capability-packaging and governance dimensions.

## Themes
- `remote-agent-invocation`: Agent Card discovery, Task object with lifecycle states (SUBMITTED, WORKING, INPUT_REQUIRED, AUTH_REQUIRED, COMPLETED, FAILED, CANCELED, REJECTED), Section 4.1.3 and Section 3.1.
- `harness-portability`: Three equivalent bindings (JSON-RPC, gRPC, HTTP+JSON) and security schemes (API key, HTTP, OAuth 2.0, OIDC, mTLS), Sections 4.5, 5, 9-12.

## Key points
- Latest released version is 1.0.0 (earlier 0.3.0, 0.2.6, 0.1.0); clients send an `A2A-Version` header (Section 3.6).
- Agent Card advertises identity, capabilities (`streaming`, `pushNotifications`, `extendedAgentCard`), skills, endpoint and auth requirements; cards can be signed (Section 8.4).
- Operations: Send Message, Send Streaming Message, Get/List/Cancel Task, Subscribe to Task, push-notification config CRUD, Get Extended Agent Card.
- Streaming = ordered status/artifact update events; push = HTTP POST webhooks to client-registered URLs.
- Interrupted states INPUT_REQUIRED and AUTH_REQUIRED model human-in-the-loop and in-task authorization (Section 7).
- Per the spec text, credential issuance and delegation are implementer responsibilities, not protocol-defined (see secondary security commentary in the A2A adoption notes).

## Could not verify
- Only the first ~100k of 256k characters were read; Agent Card field list and Appendix B (relationship to MCP) were not read in the spec itself. The A2A-and-MCP topic page was read instead.
