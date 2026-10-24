---
title: Run Claude Code programmatically (headless / claude -p / Agent SDK CLI)
source_url: https://code.claude.com/docs/en/headless
author: Anthropic
publisher: code.claude.com
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, harness-portability]
relevance: high
---

## Relevance to the project
The headless interface is what lets another system call Claude Code as a task-specific agent: `-p`, JSON/stream-json output, `--json-schema` structured output, session resume, permission modes, `--bare` for reproducible CI, cost in the result. It is the thin wrapper layer under most 'Claude Code as a service' designs, and its warnings (MCP tasks not awaited, permission prompts denied) show where unattended use bites.

## Themes
- `remote-agent-invocation`: Non-interactive runs cannot answer prompts: with `--permission-prompts none` anything needing approval is denied and MCP elicitation is cancelled; `-p` does not wait for MCP tasks.
- `harness-portability`: `--bare` skips hooks, skills, plugins, MCP, CLAUDE.md for identical results across machines; will become the default for `-p` in future.

## Key points
- Output formats text/json/stream-json; `--json-schema` returns `structured_output`; `total_cost_usd` is a client-side estimate.
- `--max-budget-usd` and `--max-turns` cap spend; SIGTERM leaves turn unfinished.
- Without `--bare`, `-p` loads hooks and `.mcp.json` from the repo even in untrusted folders (a supply-chain surface).
- Skills can be invoked by name in `-p` prompts.
