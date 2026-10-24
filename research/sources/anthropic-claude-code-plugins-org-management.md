---
title: Manage Claude Code plugins for your organization (docs)
source_url: https://code.claude.com/docs/en/plugins/org
author: Anthropic
publisher: code.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skills-marketplace, org-learning-loop, harness-portability]
relevance: high
---

## Relevance to the project
Shows what a first-party enterprise control plane for a private marketplace looks like: managed settings that register an org marketplace, force-enable plugins, allow/block marketplace sources, set update policy and audit usage. It is the Claude-Code analogue of Ramp's Dojo governance, but delivered as vendor product features. All of it governs Claude Code only.

## Themes
- skills-marketplace: `extraKnownMarketplaces` + `enabledPlugins` push an org marketplace and force-enable plugins; `strictKnownMarketplaces` allowlist / `blockedMarketplaces`; per-marketplace `autoUpdate`; release channels via two marketplaces pointing at different refs; `CLAUDE_CODE_PLUGIN_SEED_DIR` seeds containers and CI.
- org-learning-loop: org-synced plugins reach claude.ai, Cowork and Claude Code ("synced plugins"); Enterprise Analytics API gives per-plugin install and invocation counts (third-party plugins aggregated as `third-party`).
- harness-portability: `disableSideloadFlags`, `strictPluginOnlyCustomization` (blocks non-plugin skills/agents/hooks/MCP) are Claude Code settings; nothing here travels to Codex or Copilot.

## Key points
- Server-managed settings (admin console), MDM or managed-settings.json; first delivering source wins unless `managedSourcesBehavior: merge`.
- Limitation stated: server-managed settings apply to every user; per-group targeting needs endpoint-managed settings or a gateway policy.
- Allowlist does not restrict entries inside an allowed marketplace; block a single plugin with `enabledPlugins: false`.
- Telemetry: OTel `plugin_installed` / `plugin_loaded` events.

## Could not verify
- Real-world adoption of these controls (no independent reports found).
