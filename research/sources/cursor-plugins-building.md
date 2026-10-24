---
title: Building plugins (Cursor docs)
source_url: https://cursor.com/docs/plugins/building
author: Cursor (Anysphere)
publisher: cursor.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skills-marketplace, harness-portability, skill-standards]
relevance: medium
---

## Relevance to the project
Cursor's plugin format mirrors Claude Code's (manifest + rules, skills, agents, commands, hooks, MCP servers) under a different manifest path, and expands both `${CURSOR_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_ROOT}`: an example of "convergence by imitation" rather than a shared standard.

## Themes
- skills-marketplace: `.cursor-plugin/plugin.json`; marketplace repo can hold several plugins in `.cursor-plugin/marketplace.json`; team admins set plugin variables in the dashboard; public submission at cursor.com/marketplace/publish.
- harness-portability: the page describes two formats: "Agent Plugins" (open standard, `plugin.json` at root, only skills and MCP servers) and full "Cursor Plugins"; does not expand the standard's `${PLUGIN_ROOT}` / `${PLUGIN_DATA}` variables. Skills are also read from `.claude/skills/` and `.codex/skills/` per search summaries of Cursor's skills page.

## Could not verify
- The "Agent Plugins open standard" referenced here was not located or checked; Cursor skills availability dates (one source says v2.4, Jan 2026) conflict.
