---
title: Build programmatic agents with the Cursor SDK
source_url: https://cursor.com/blog/typescript-sdk
author: Roshan Sadanani (Cursor)
publisher: cursor.com
published: 2026-04-29
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-over-model, remote-agent-invocation, build-vs-buy]
relevance: high
---

## Relevance to the project
Cursor's stance on harnesses is to export its own: the TypeScript SDK gives third parties Cursor's full harness (indexing, MCP, skills, hooks, subagents) locally or in Cursor-hosted VMs or self-hosted workers, with any model Cursor supports. It makes Cursor a loop source for an own product (a P2 option comparable to the Claude Agent SDK and Codex SDK, but model-agnostic), including for non-coding internal tools.

## Themes
- harness-over-model: "Route agents to the best model for the task at hand" by changing one field; same harness whatever the model.
- remote-agent-invocation: cloud runs on a dedicated VM per agent continue while the laptop sleeps and appear in the Agents Window and web app.
- build-vs-buy: pitched as a way to avoid building and maintaining an agent stack.

## Key points
- Harness features: codebase indexing and semantic search; MCP via .cursor/mcp.json or inline; skills from .cursor/skills/; hooks from .cursor/hooks.json; named subagents.
- Runtimes: local; Cursor cloud ("Each agent gets its own dedicated VM with strong sandboxing"); self-hosted workers keep code and tool execution in your network.
- "billed based on standard, token-based consumption pricing"; auth via CURSOR_API_KEY.
- Use cases named include internal tools letting GTM teams query product data without code, and embedding Cursor in customer-facing products.
- Customers named: Faire (quote), Rippling, Notion, C3 AI.
- No Python SDK at launch (secondary coverage).

## Could not verify
- Enterprise controls specific to SDK agents; whether BYOK applies to SDK runs.
