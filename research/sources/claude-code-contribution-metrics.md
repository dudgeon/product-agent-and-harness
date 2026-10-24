---
title: Measure Claude Code's impact with contribution metrics
source_url: https://claude.com/resources/articles/contribution-metrics
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-01-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [outcome-measurement-gap, enterprise-admin-controls, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
Anthropic's built-in impact measure for Claude Code is output volume (PRs merged and lines committed with and without Claude, per user), joined from session activity and GitHub. It shows what the vendor offers for measurement and its limits: Anthropic itself calls PRs "an incomplete measure" and suggests pairing it with DORA metrics. Nothing comparable exists for product work, which is the gap a product harness would have to fill.

## Themes
- outcome-measurement-gap: the metric is activity (PRs, lines), not outcomes; Anthropic concedes PRs are "an incomplete measure of developer velocity" and positions them as a proxy ("How we're shipping at Anthropic").
- enterprise-admin-controls: dashboard visible to workspace admins and owners; per-user contribution data to "identify adoption patterns" ("Measure velocity").
- vendor-claims-vs-independent-evidence: Anthropic reports a 67% increase in PRs merged per engineer per day internally and 70-90% of code written with Claude Code assistance, method not given ("How we're shipping at Anthropic").

## Key points
- Public beta for Team and Enterprise; install the Claude GitHub App, toggle GitHub Analytics in admin settings, authenticate the GitHub org.
- Attribution matches Claude Code session activity to commits and PRs; counted "conservatively", only where involvement is high-confidence.
- Recommends using alongside DORA metrics and sprint velocity for "directional changes".
- **Limits:** per-user tracking raises surveillance questions the page does not address; no quality, defect or rework signal.
