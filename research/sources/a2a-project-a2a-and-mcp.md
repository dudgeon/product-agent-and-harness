---
title: A2A and MCP: complementary protocols
source_url: https://a2a-protocol.org/latest/topics/a2a-and-mcp/
author: A2A Project (Linux Foundation)
publisher: a2a-protocol.org
published: unknown
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, harness-portability]
relevance: medium
---

## Relevance to the project
The A2A project's own positioning against MCP: MCP is agent-to-tool (vertical), A2A is agent-to-agent (horizontal). Useful as the 'official' framing, but it is the protocol owner's view and is the very distinction critics contest. Also shows the intended pattern: each agent uses MCP internally, agents talk A2A to each other.

## Themes
- `remote-agent-invocation`: Frames deployed agents as stateful autonomous peers (A2A) versus stateless tools (MCP); an A2A server may also expose skills as MCP-compatible resources.

## Key points
- MCP = tools, APIs, resources; A2A = discovery, coordination and shared tasks between autonomous, often cross-organisation agents.
- Example: a Shop Manager agent talks A2A to a customer and a Mechanic agent; the Mechanic uses MCP for its diagnostic tools and A2A to reach a Parts Supplier agent.
- Contested in practice: MCP servers wrapping whole agents (Glean, Sentry Seer) blur the line, and MCP now has tasks and input-required results (see MCP notes).
