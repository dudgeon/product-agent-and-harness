---
title: "Customize Claude Code with mods in TypeScript"
source_url: https://claude.com/resources/articles/claude-code-mods
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-10-01
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [meta-harness, skill-supply-chain-security, enterprise-admin-controls, policy-enforcement-fail-open]
relevance: medium
---

## Relevance to the project
Mods are TypeScript functions that hook Claude Code's internal events (tool calls, permission requests, prompt submission, screen drawing) to run before, after, instead of or around them, so a company can rewrite prompts, block or retry tool calls, auto-approve or deny permissions, redact secrets and add UI. That makes the harness itself a customization layer, and Anthropic is moving built-ins (e.g. /diff) into mods toward a small core. Mods are unsandboxed and ship inside plugins, so trust rests on marketplace allow/block lists and a built-in "sec-default" mod that loads first. First-party launch post; no adoption data.

## Themes
- meta-harness: harness behaviour itself is replaceable; built-in features shipping as mods; plan to "pare Claude Code down to a small core" (section "Swap built-in features").
- skill-supply-chain-security: mods "aren't sandboxed" and run with Claude Code's access; install only from trusted sources (opening).
- enterprise-admin-controls: plugin marketplace allow/block via admin console or managed settings; admin mods can load first; audit-logging mod example (section "Mods for teams and enterprises").
- policy-enforcement-fail-open: sec-default stops user mods overriding permission deny rules, but admins who load their own mods first must add sec-default back or lose its restrictions (enterprise section).

## Key points
- Events have before/after/instead/wrap hooks; mods stack in load order (first loaded sees the event first and the result last).
- Capabilities beyond hooks: rewrite events, draw UI (terminal, desktop or both), add buttons other mods respond to.
- Claude Code can write, install and hot-reload a mod in session.
- Team examples: CI/CD status pane, confirmation before touching production config, first-loaded audit-log mod.
- Design was shared on GitHub before launch for feedback.
- Limits: launch post, no security review details beyond sec-default; ordering-based security means a misconfigured load order weakens controls.

## Notable quotes
- "Mods run with the same access to your machine as Claude Code itself. They aren't sandboxed."

## Could not verify
- Exactly what sec-default restricts (source linked, not read).
