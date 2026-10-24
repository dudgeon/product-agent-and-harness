---
title: Building agents with the Claude Agent SDK
source_url: https://claude.com/blog/building-agents-with-the-claude-agent-sdk
author: Anthropic
publisher: Claude blog
published: 2025-09-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-over-model]
relevance: high
---

## Relevance to the project
Announces the rename of the Claude Code SDK to the Claude Agent SDK: the same loop that powers Claude Code, offered for non-coding agents. This is the base Ramp Glass is built on, so it defines what "embed a vendor SDK" gives you.

## Themes
- agent-frameworks: SDK packages loop, tools, context compaction, subagents and MCP connections as a reusable harness.
- harness-over-model: positions the harness (loop plus computer-like tools) as the reusable asset.

## Key points
- Agent loop: gather context, take action, verify work, repeat.
- Provides built-in tools, compaction, subagents with own context windows, MCP connectors, bash/file access.
- The fetched summary says the article does not cover permissions, skills or hooks (these appear in the docs, see anthropic-agent-sdk-overview).

## Notable quotes
- "Claude needs the same tools that programmers use every day."
