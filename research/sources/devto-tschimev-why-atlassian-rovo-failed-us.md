---
title: "Why Atlassian Rovo Failed Us (and What We Built Instead)"
source_url: https://dev.to/mitkotschimev/why-atlassian-rovo-failed-us-and-what-we-built-instead-2e19
author: Mitko Tschimev
publisher: DEV Community
published: unknown
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-pm-agents-jobs-to-be-done
themes: [agent-failure-modes, org-context-grounding, compounding-context-repo]
relevance: low
---

## Relevance to the project
A single team's account of abandoning Rovo for Jira-ticket-to-code automation and building its own pipeline (Jira automation, GitHub webhook and runner, Cursor agent) grounded in repo files (.cursorrules, a skills/ directory, ADRs). It is an engineering use, not a PM job, but it shows the recurring pattern that platform agents fail on team conventions while a home-built harness with curated context is preferred. Low weight: no method, no numbers.

## Themes
- agent-failure-modes: Rovo "can't handle nuanced tickets, doesn't understand team conventions, and needs constant supervision"; "polished in demos but struggles in production".
- org-context-grounding / compounding-context-repo: the replacement works, the author says, because conventions, skills and ADRs live in the repo.

## Key points
- No test protocol, task set, duration or team size; "After weeks of frustration" is the only time reference.
- No metrics for either Rovo or the replacement; the claim that agent code "passes review" is unsupported.
- Author's affiliation not stated; no sign of selling a competing product; replacement appears internal. Part of a planned series.

## Could not verify
- Publication date not captured; author's employer unknown.

Retrieved via WebFetch (model-summarised view); quotes returned as verbatim, re-check before publication.
