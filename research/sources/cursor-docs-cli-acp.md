---
title: ACP (Cursor CLI docs)
source_url: https://cursor.com/docs/cli/acp
author: Cursor (Anysphere)
publisher: cursor.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-portability, meta-harness]
relevance: low
---

## Relevance to the project
Cursor's agent can be driven by other clients (Zed, JetBrains, Neovim, custom clients) over the Agent Client Protocol, which is how meta-harnesses and other editors host it. The page says nothing about the Cursor IDE hosting third-party agents; the direction is outward (Cursor as a harness others call), matching the SDK.

## Themes
- harness-portability: "ACP enables Cursor's AI agent to work with editors beyond the Cursor desktop app."
- meta-harness: makes Cursor Agent wrappable by layers such as Superset, Omnigent, OpenClaw.

## Key points
- agent acp runs JSON-RPC 2.0 over stdio; auth cursor_login, API key or auth token; modes agent, plan, ask; permission requests (allow-once, allow-always, reject-once).
- Limits: "Team-level MCP servers configured through the Cursor dashboard are not supported in ACP mode"; tools block if the client does not answer permission requests.

## Could not verify
- Whether the Cursor IDE can host Claude Code or Codex as agents. Separately, Anthropic's docs (per search snippet, not read) say the Claude Code extension installs in Cursor as a VS Code fork, running as its own panel with its own context and billing (DataCamp tutorial, April 2026, per search summary).
