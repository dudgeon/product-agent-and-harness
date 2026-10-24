---
title: Codex as an MCP server (removed): migration notice
source_url: https://learn.chatgpt.com/docs/mcp-server
author: OpenAI
publisher: learn.chatgpt.com (formerly developers.openai.com/codex/guides/agents-sdk)
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, harness-portability, agent-failure-modes]
relevance: high
---

## Relevance to the project
A cautionary data point: OpenAI removed `codex mcp-server` (and the standalone binary) that let the Agents SDK or other MCP clients drive Codex as a tool, replacing it with an experimental Codex app server speaking its own JSON-RPC (not MCP, 'not supported for production workloads'). Third-party blog posts still describe the old path. So 'wrap a coding harness as an MCP agent' is not a stable vendor-supported route for Codex; OpenAI's own Claude Code plugin uses the app server instead.

## Themes
- `harness-portability`: Hosting Codex over MCP no longer supported; external MCP servers still supported via `codex mcp`.
- `agent-failure-modes`: Integrations that launched the MCP server must migrate before upgrading; the replacement is experimental.

## Key points
- The app server handles authentication, conversation history, approvals and streamed agent events over its own protocol.
- Date of removal is not on the page; third-party posts from March-May 2026 still documented `codex mcp-server`.

## Could not verify
- Removal date and exact version not found.
