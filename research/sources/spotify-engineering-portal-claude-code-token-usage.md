---
title: "Portal by Spotify cut my Claude Code token usage by 90%"
source_url: https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90
author: Dimitri Mazmanov (Principal Product Manager, Spotify)
publisher: Spotify Engineering blog
published: 2026-09-03
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [cost-control-routing, non-engineer-builders, single-agent-many-skills, harness-portability]
relevance: medium
---

## Relevance to the project
A Spotify product manager writes his own Claude Code plugin ("shunt") that routes bulk file reading and boilerplate to a cheaper model through Portal's AiKA "modes", and reports about 90% savings on bulk reads. It is evidence that PMs at Spotify work directly in coding agents and build harness pieces (hooks, skills, CLI calls), and a concrete cost-routing pattern.

## Themes
- cost-control-routing: PreToolUse hooks block large file reads and send them to a worker model (Gemini 2.5 Flash in the examples) via Portal CLI; mean bulk-read token saving about 90% on a Java monorepo across four scenarios (author claim, Sep 2026).
- non-engineer-builders: author is a principal PM building and publishing a Claude Code plugin.
- single-agent-many-skills: skill files tell Claude when to delegate; two modes, `bulk-reader` and `code-writer`.
- harness-portability: Portal modes let any configured model be the worker.

## Key points
- Excluded: debugging, architecture, safety-critical code.
- Limits: worker summaries lack reliable line numbers; worker missed a thread-safety bug Claude caught; 10-30 s per delegation, 30 s cap per invocation; small reads slower, so a 350-line threshold.
- No absolute token counts; code-write savings not measured.
