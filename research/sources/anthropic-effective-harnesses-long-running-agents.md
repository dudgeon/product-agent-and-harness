---
title: Effective harnesses for long-running agents
source_url: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
author: Anthropic Engineering
publisher: Anthropic Engineering
published: 2025-11-26
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-over-model, memory-architecture, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Concrete harness design for work spanning many context windows: an initializer agent plus a coding agent that hand off through a feature list, progress file, git history and init script. Shows that memory and verification scaffolding, not the model, decide long-task success.

## Themes
- harness-over-model: compaction alone was not enough; Opus 4.5 in a loop failed to build a production web app from one prompt.
- memory-architecture: handoff artifacts (JSON feature list, progress log, git commits, init script) act as cross-session memory.
- evals-autonomy-trust: models marked features done after unit tests/curl; browser-automation testing raised reliability.

## Key points
- Failure modes: declaring victory early, leaving bugs/undocumented progress, premature done-marking, wasting time running the app.
- Fixes: feature list (JSON because models alter it less than Markdown), progress file, git, init script, self-verification.

## Notable quotes
- "getting agents to make consistent progress across multiple context windows remains an open problem"
