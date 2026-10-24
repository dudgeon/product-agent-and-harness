---
title: Plugin manifest reference (Claude Code docs)
source_url: https://code.claude.com/docs/en/plugins-reference
author: Anthropic
publisher: code.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skills-marketplace, harness-portability, skill-standards]
relevance: high
---

## Relevance to the project
Defines what a "plugin" actually bundles in Claude Code and therefore the practical upper bound of what can be packaged and distributed without building a harness. It shows plugins moving beyond prompts into hooks, background monitors, MCP/LSP servers, executables on PATH, workflows (JS) and TUI "mods": i.e. a plugin is a software package that extends the harness, not just a content bundle.

## Themes
- skills-marketplace: plugin = unit of distribution; `marketplace.json` catalogs plugins; `version` pins a plugin until changed; `dependencies` between plugins; `userConfig` prompts for values and keeps secrets in the credential store.
- harness-portability: bundle components are Claude Code-specific (hooks, monitors, `bin/`, `workflows`, `outputStyles`, `lspServers`, `settings.json` with `agent`); claude.ai and Cowork refuse a plugin that has a top-level `bin/` directory; `${CLAUDE_PLUGIN_ROOT}` is Claude-named.
- skill-standards: plugin name must not impersonate Anthropic (`claude-`, `anthropic-` prefixes are errors).

## Key points
- Only `name` required; manifest optional (layout discovery). Components: skills/, commands/ (legacy, prefer skills), agents/, hooks/hooks.json, .mcp.json, .lsp.json, output-styles/, workflows/, themes/, monitors/, bin/, settings.json.
- Components are namespaced by plugin (`deploy-tools:reviewer`).
- `claude plugin validate [--strict]` for CI; `experimental.evals` points to eval cases (see plugin-evals note).
- A `CLAUDE.md` at the plugin root is not loaded; instructions must go in a skill.

## Could not verify
- Which of these components Codex, Copilot or Cursor ignore vs. honour; only Cursor's doc was read (see cursor note).
