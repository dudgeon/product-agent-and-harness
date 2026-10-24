---
title: Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic
source_url: https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-09-14
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-factory-sdlc, shared-persistent-sessions, remote-agent-invocation]
relevance: medium
---

## Relevance to the project
An Anthropic engineer reports that once agents write and review most code, the bottleneck moves downstream: CI jobs rose 25x in six months and the test-selection service needed three stopgap patches and then a full redesign. It supports the "bottleneck keeps shifting" reading of an agentic SDLC: accelerating one stage loads the next, so a product-agent strategy should expect pressure on review, test and merge infrastructure, not only gains at the define stage. It also shows a long-lived Slack-style agent session used as a monitoring companion for months.

## Themes
- agent-factory-sdlc: Anthropic engineers ship 8x the code per quarter compared with 2021-2025; Claude writes 80% of it and plays a large role in review and approval; tests grew 10x and CI jobs 25x in six months ("AI is evolving CI").
- shared-persistent-sessions: a long-running session in an internal version of Claude Tag monitored the service for months and pinged the engineer when listener lag passed 50,000 jobs, resuming with retained context ("Patch 2").
- remote-agent-invocation: the monitoring session was event-triggered (lag threshold) and resumed the conversation, rather than started by a person ("Patch 2").

## Key points
- **Service:** deterministic test impact analysis: a "listener" records CI results, a "selector" picks tests per PR from history and package relevance. The author notes agents need a specific valid test set to self-verify, whereas humans can ignore irrelevant failures.
- **Failure mode of lag:** 20 minutes of listener lag can mean tens of thousands of test updates not applied, causing wasted investigations, flaky reds blocking merges, and new or fixed tests not running.
- **Patches:** bigger machine (lasted 70 days), per-package sharding (29 days), daily restarts (less than a day, and the service fell further behind). Ownership was "murky"; no team wanted another piece of infrastructure.
- **Redesign:** stateless listener workers append to a journal in an in-memory store; a consumer rolls it into per-test history every few seconds. Three weeks for one engineer, estimated at a quarter a year earlier; Claude did much of the tuning autonomously.
- **Advice:** assume 25x load within two quarters; keep state out of process; instrument services as "Claude's eyes and ears" so it can hill-climb fixes. Claude prefers smaller PRs, raising CI job counts; agents push overnight and at weekends, raising the activity floor.
- **Limits:** single internal account; the author is unnamed in the extract; Anthropic is an extreme case (monorepo merges from about 2,500 to 30,000+ a day per a related article) and may not transfer to a typical enterprise.

## Notable quotes
- "Writing code is no longer the constraint, and once PR review gets accelerated, CI starts feeling the pressure." ("AI is evolving CI")

## Could not verify
- Author's name (the extract shows first person but no byline).
