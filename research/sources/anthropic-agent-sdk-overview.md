---
title: Agent SDK overview (Claude Code docs)
source_url: https://code.claude.com/docs/en/agent-sdk/overview
author: Anthropic
publisher: Claude Code docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-portability, skill-standards]
relevance: high
---

## Relevance to the project
The authoritative statement of what the Agent SDK includes and the four ways Anthropic offers to build (Agent SDK, CLI, Client SDK, Managed Agents). Also contains terms that matter for lock-in: API-key auth only for third-party products, branding limits, Commercial Terms.

## Themes
- agent-frameworks: SDK exposes built-in tools, hooks, subagents, MCP, permissions, sessions, skills/commands/memory loaded from .claude/, and plugins.
- harness-portability: SDK "runs the Claude Code binary", so a product built on it inherits the Claude Code harness, and Claude-only models.
- build-vs-buy: lays out Agent SDK vs Client SDK (write the loop yourself or beta tool runner) vs Managed Agents (hosted) as a ladder of how much you own.

## Key points
- Table of four options: Agent SDK (embed in your process), Claude Code CLI, Client SDK (you write the loop), Managed Agents (Anthropic hosts the loop).
- Capabilities list: built-in tools, hooks, subagents, MCP, permissions, sessions (resume/fork), skills/commands/memory, plugins.
- Non-Claude-Code languages can drive the loop by running the CLI as a subprocess with -p and JSON output.
- Terms: Anthropic does not allow third parties to offer claude.ai login or its rate limits in products built on the SDK; use API keys. Branding: may not present as "Claude Code".
- Governed by Anthropic Commercial Terms of Service.
