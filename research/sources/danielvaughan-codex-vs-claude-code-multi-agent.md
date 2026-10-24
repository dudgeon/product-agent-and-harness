---
title: "Codex CLI vs Claude Code Multi-Agent: Subagents, Agent Teams and the Protocol Gap"
source_url: https://codex.danielvaughan.com/2026/04/09/codex-vs-claude-code-multi-agent/
author: Daniel Vaughan
publisher: codex.danielvaughan.com (personal blog)
published: 2026-04-09
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, single-agent-many-skills]
relevance: medium
---

## Relevance to the project
Evidence that subagent definitions are not portable: Codex uses TOML files in `.codex/agents/` (name, description, developer_instructions, optional model/sandbox_mode/mcp_servers), Claude Code uses Markdown+YAML in `.claude/agents/`. Delegation semantics also differ (explicit user-directed spawning in Codex vs description-matched in Claude Code).

## Themes
- harness-portability: no shared subagent spec; neither tool natively supports A2A as of April 2026 (reach it via community MCP bridges); Codex `max_depth` 1 / `max_threads` 6 defaults; Claude Code Agent Teams (2-16 agents, peer messaging) are experimental behind an env flag.

## Could not verify
- Claims about internal defaults are blog-reported; Codex subagents official page (developers.openai.com/codex/subagents) only seen in search results; GitHub Copilot `.agent.md` compatibility unverified.
