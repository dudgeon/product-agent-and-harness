---
title: "1,500+ PRs Later: Spotify's Journey with Our Background Coding Agent (Honk, Part 1)"
source_url: https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1
author: Max Charas (Senior Staff Engineer) and Marc Bruggmann (Principal Engineer), Spotify
publisher: Spotify Engineering blog
published: 2025-11-06
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [agent-factory-sdlc, remote-agent-invocation, non-engineer-builders, harness-portability, one-job-per-agent, outcome-measurement-gap]
relevance: high
---

## Relevance to the project
The first post in Spotify's Honk series explains where its coding agent came from: an existing fleet-change system (Fleet Management / Fleetshift) whose deterministic scripts were swapped for a prompt-driven agent, while targeting, PR opening, review and merge stayed the same. It is a clear case of an agent dropped into an existing, well-instrumented pipeline instead of a new surface. It also names product managers as users who propose small changes from Slack without cloning repos, which is an early sign of non-engineers reaching code through an agent. All outcome numbers are Spotify's own.

## Themes
- agent-factory-sdlc: the agent replaced only the "transformation" step of an existing pipeline; targeting, PRs, review and merge infrastructure were unchanged (section "Enter AI coding agents").
- remote-agent-invocation: the background agent is exposed over MCP so it can be started from Slack and GitHub Enterprise; an interactive agent first gathers task details, then hands a prompt to the coding agent (section "Beyond migrations").
- non-engineer-builders: product managers use it to propose simple changes without cloning and building repos (same section).
- harness-portability: a small internal CLI wraps the agent so Spotify can swap agents and LLMs; it runs MCP formatting/linting tools, LLM judges on diffs, log upload to GCP and MLflow traces.
- one-job-per-agent: multi-agent setup for planning, generating and reviewing PRs (figure 6).
- outcome-measurement-gap: 60-90% time saving versus hand-written migrations is claimed without a stated method.

## Key points
- Fleet Management runs source-to-source transformations as containerised jobs that open PRs. Since mid-2024 about half of Spotify's PRs come from it (Spotify claim, Nov 2025).
- Limit of scripts: the Maven dependency updater grew past 20,000 lines; only a few teams could write complex fleet changes.
- Work on an agent started in February 2025, aiming to let engineers define fleet-wide changes in natural language.
- More than 1,500 agent PRs merged into production by Nov 2025 (Spotify claim). Examples: Java value types to records, Scio upgrades with breaking changes, migrating UIs to Backstage's new frontend system, schema-checked YAML/JSON config changes.
- "Hundreds of developers" use the agent. Ad hoc uses include capturing architecture decision records (ADRs) from Slack threads.
- Shared plumbing applies to every agent PR whatever its origin: commit tagging, LLM quota management, trace collection.
- Open problems named: slow and unpredictable runs, safety/sandboxing, cost.

## Notable quotes
- "We don't have all the answers yet." (closing section)

## Could not verify
- The 60-90% saving and 50% share of PRs are unaudited Spotify figures; no method is given.
