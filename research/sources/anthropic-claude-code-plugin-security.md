---
title: Plugin security and trust (Claude Code docs)
source_url: https://code.claude.com/docs/en/plugins/security.md
author: Anthropic
publisher: code.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-supply-chain-security, skills-marketplace]
relevance: high
---

## Relevance to the project
Anthropic states plainly that "a Claude Code plugin you install can execute arbitrary code on your machine with your user privileges" and that its permission rules and sandbox do not cover code the plugin runs by itself (hooks, monitors, MCP/LSP servers, mods). That is a key limit on the "just distribute plugins" pattern for sensitive enterprise work and an argument for a governed private marketplace or a runtime that sandboxes everything.

## Themes
- skill-supply-chain-security: hooks, monitors, mods, stdio MCP servers and LSP servers run outside the sandbox; skills/commands/agents enter context as instructions; auto-update means "the files you reviewed can change on disk".
- skills-marketplace: three trust tiers (official, community, third-party); community catalog pins nearly every plugin to a commit SHA and Claude Code refuses a different commit; `archive` sources can pin `sha256`; Anthropic "does not control what MCP servers, files, or other software are included in plugins and cannot verify that they will work as intended or that they won't change".

## Key points
- Review path: `/plugin` details pane, read hooks/hooks.json, .mcp.json, bin/; `claude plugin details` lists a component inventory.
- Reserved marketplace names only accepted from github.com/anthropics/ repos (anti-impersonation).
- Uninstall leaves cached files 14 days.

## Could not verify
- No independent audit of how effective the commit-pinning and review steps are.
