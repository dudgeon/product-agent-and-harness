---
title: Codex SDK and app server documentation
source_url: https://learn.chatgpt.com/docs/codex-sdk
author: OpenAI
publisher: OpenAI docs (learn.chatgpt.com)
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-portability]
relevance: medium
---

## Relevance to the project
Shows OpenAI's analogue to the Agent SDK: control the Codex harness programmatically (TypeScript and Python) or build custom clients over the Codex app server. Together with the Claude Agent SDK it supports the pattern "the vendor CLI harness is now an importable SDK".

## Themes
- agent-frameworks: SDK drives local Codex over JSON-RPC (app-server); Python builds pin a Codex CLI runtime.
- harness-portability: codex-mcp-server removed in favour of the app server.

## Key points
- TypeScript @openai/codex-sdk (Node 18+), Python openai-codex (3.10+).
- Threads: start, run, resume; sandbox presets read_only, workspace_write, full_access.
- App server is the lower-level option for custom clients handling auth, history, approvals and streamed events.
- SDK works with the CLI, IDE extension or Codex cloud.

## Could not verify
- Licence of the CLI not stated on this page (other sources describe it as open source).
