---
title: "How Uber Executed A JUnit Migration at Massive Scale"
source_url: https://www.uber.com/us/en/blog/junit-migration/
author: Anshuman Mishra, Kaushik Vejju (Uber Java Platform)
publisher: Uber Engineering Blog
published: 2026-04-07
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [deterministic-scaffold-model-nodes, agent-failure-modes]
relevance: low
---

## Relevance to the project
The only blog post found that names Shepherd, Uber's large-scale code-change tool: Shepherd generated 5,000+ diffs to move 75,000+ test classes to JUnit 5 in four months, but the transformations were deterministic OpenRewrite recipes because a generative-AI attempt at multi-file migration failed. It is a useful counterweight to "agents do migrations" claims and places Shepherd as a change-delivery primitive that agents can sit on, not an agent itself.

## Themes
- deterministic-scaffold-model-nodes: recipes do the change; AI used only to debug test and build failures; a script applies the patch, updates deps, builds and runs tests, and only passing targets go forward (Architecture).
- agent-failure-modes: "a deterministic approach proved more practical than an AI-driven migration." (Approach)

## Key points
- Scope: 600,000+ JUnit 4 tests, ~15M lines; 75,000+ classes and ~1.25M lines changed; 2,000+ diffs in the first rollout, 5,000+ total.
- Shepherd produces diffs; CI validates with integration tests, linters and coverage; failing files reverted to JUnit 4.

## Notable quotes
- "a deterministic approach proved more practical than an AI-driven migration."

## Could not verify
- Shepherd's own design and any agent integration are not described; no human approval step is described.
