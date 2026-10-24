---
title: Agent Client Protocol (ACP)
source_url: https://zed.dev/acp
author: Zed Industries (with JetBrains and community)
publisher: zed.dev
published: unknown
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, skill-standards]
relevance: high
---

## Relevance to the project
ACP standardises the editor-to-agent boundary (an 'LSP for agents'), so one agent can work in many front ends. It is the front-end counterpart to Omnigent's back-end layer: it makes the UI harness-agnostic, not governance or sharing.

## Themes
- [[harness-portability]]: 50+ listed agents (Claude Agent, Codex CLI, Gemini CLI, Cursor, GitHub Copilot, Devin, Goose, OpenCode, Qwen Code) usable from Zed, JetBrains, VS Code, Emacs, Neovim, Obsidian and others; Claude Code and Codex reach ACP through adapters rather than natively.

## Key points
- Apache-licensed, created by Zed, co-developed with JetBrains (Oct 2025) and Google (Gemini CLI, Aug 2025); community-governed GitHub org.
- JSON-RPC over stdio per codepick's summary; the page itself gives little architecture detail.
- 'Nothing touches our servers' when third-party agents are used in Zed (privacy claim).

## Could not verify
- No date on the page; adapter mechanics not described on it. Governance model not verified.
