---
title: Minions: Stripe's one-shot, end-to-end coding agents
source_url: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
author: Alistair Gray (Stripe)
publisher: Stripe Dev Blog
published: 2026-02-09
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [build-vs-buy, agent-frameworks, harness-portability]
relevance: high
---

## Relevance to the project
Stripe built an unattended coding agent by forking Block's Goose and wrapping it in deterministic steps (git, lint, tests), devboxes and an internal MCP tool server. It is the main non-Ramp example of owning a harness, and it shows "fork an open-source harness" rather than "write from scratch or use a framework".

## Themes
- build-vs-buy: reasons to build in-house: huge Ruby/Sorbet monorepo with homegrown libraries, payments-critical code, existing developer tooling for humans; claims over 1,000 merged PRs per week fully agent-written, human-reviewed.
- agent-frameworks: core loop runs on a Goose fork; orchestration interleaves agent steps with deterministic ones.
- harness-portability: a central MCP "Toolshed" with 400+ tools; minions get curated subsets.

## Key points
- Devboxes pre-warmed in about 10 seconds, isolated from production and the internet, enabling parallel runs without human permission checks.
- At most one or two CI runs, after local fixes.

## Notable quotes
- "if it's good for humans, it's good for LLMs, too."

## Could not verify
- Volume claims are Stripe's own; no independent verification. Search results gave differing numbers (1,000 vs 1,300 per week).

## Added by research-agent-runtime-patterns-taxonomy (track 6, work-structure fit)
- Work-structure reading (first-party): the orchestration "interleaves agent loops with deterministic code": git operations, linters and testing are deterministic nodes; open-ended coding is the agentic node; MCP tools are run deterministically beforehand to hydrate context. Stripe's stated reason: "the creativity of an agent with the assurance that they'll always complete Stripe-required steps like linters." CI is capped at two rounds; humans still review every PR ("human-reviewed" yet "no human-written code"). Evidence for a hybrid (structured wrapper, open-ended core) as the pattern for repeatable engineering work. Stripe's own page does not use the word "blueprint" (third-party write-ups do).

## Added by competitive-teardown-stripe-knowledge-agents (2026-10-24)
- Re-read for the internal-docs question: "Our internal docs platform, feature flag platform, and internal ticketing UI all integrate with minions" (entry points section); minions gather "internal documentation, ticket details, build statuses, code intelligence via Sourcegraph" over MCP, with relevant MCP tools run deterministically over likely links before a run; minions read the same agent rule files as Cursor and Claude Code, "almost all ... conditionally applied based on subdirectories". The docs platform is presumably Trailhead (named in [the Sessions 2024 panel](stripe-sessions-2024-10x-engineer-panel.md)); the post does not name it.
- Entry points: CLI, web, and most often Slack (tag the app in the thread; the minion reads the whole thread).
