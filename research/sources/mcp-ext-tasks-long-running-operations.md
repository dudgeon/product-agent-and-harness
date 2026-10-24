---
title: MCP Tasks: asynchronous task execution for long-running MCP operations
source_url: https://modelcontextprotocol.io/specification/draft/basic/utilities/tasks
author: Model Context Protocol project
publisher: modelcontextprotocol.io
published: 2026-07-28
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, harness-portability]
relevance: high
---

## Relevance to the project
This is the MCP-native way to make an MCP server front a slow, agent-like backend: the server returns a durable task handle, the client polls, and the task can pause for input. It closes the main objection to 'agent as an MCP tool' (host timeouts) and overlaps A2A's task model. Status is an extension, so host support varies.

## Themes
- `remote-agent-invocation`: Task statuses working, input_required, completed, failed, cancelled; `tasks/get`, `tasks/update`, `tasks/cancel`; durable taskId survives client disconnect.

## Key points
- Now an official extension `io.modelcontextprotocol/tasks`, moved out of core in the 2026-07-28 revision; client and server both opt in via capabilities.
- Server decides per request whether to return a `CreateTaskResult` (taskId, status, ttlMs, pollIntervalMs); task is durably created before the response.
- `input_required` carries `inputRequests` (e.g. elicitation) answered via `tasks/update` (no second connection).
- Cancellation is cooperative; notifications optional via `subscriptions/listen`; polling is the default.
- Client matrix on the MCP site shows host support varies; not all clients implement tasks.

## Could not verify
- Client support matrix page not read.
