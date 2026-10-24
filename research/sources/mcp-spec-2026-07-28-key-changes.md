---
title: Model Context Protocol specification 2026-07-28: Key Changes
source_url: https://modelcontextprotocol.io/specification/2026-07-28/changelog
author: Model Context Protocol project
publisher: modelcontextprotocol.io
published: 2026-07-28
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, harness-portability, agent-failure-modes]
relevance: high
---

## Relevance to the project
The latest MCP revision makes MCP stateless, moves tasks to an extension, replaces server-initiated elicitation/sampling requests with multi-round-trip 'input_required' results, and deprecates Sampling. For this track: sampling (a server borrowing the host's model) is on the way out, so an MCP-served agent must bring its own model and loop; and remote MCP becomes easier to host at scale.

## Themes
- `remote-agent-invocation`: Sampling, Roots and Logging deprecated; MRTR pattern (`input_required` results) replaces server-initiated requests; tasks become an extension; sessions removed.
- `harness-portability`: Dynamic Client Registration deprecated in favour of Client ID Metadata Documents; Enterprise-Managed Authorization and OAuth Client Credentials listed as stable auth extensions.

## Key points
- Removes protocol sessions and the `initialize` handshake; every request carries version and capabilities in `_meta`; new `server/discover`.
- SSE resumability removed: a broken response stream loses the in-flight request, which makes the Tasks extension the route for long jobs.
- Deprecation policy: Active/Deprecated/Removed states with at least a twelve-month window.
- OpenTelemetry trace context conventions (`traceparent`) for `_meta`; tools/list gets caching hints.
