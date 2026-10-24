---
title: "Streamlining Detection Development with Goose Recipes"
source_url: https://goose-docs.ai/blog/2025/07/28/streamlining-detection-development-with-goose-recipes
author: Glenn Edwards (Detection Engineer, Block)
publisher: goose blog
published: 2025-07-28
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [one-job-per-agent, human-review-gates, harness-portability, non-engineer-builders]
relevance: medium
---

## Relevance to the project
The best worked example of an internal Block team turning goose into a task agent: a main recipe orchestrating six single-purpose sub-recipes from repo setup to draft PR, with Jinja-coded conditions and JSON hand-offs. Also covers the earlier post "Democratizing Detection Engineering at Block" (Tomasz Tchorz and Glenn Edwards, 2025-06-02, https://goose-docs.ai/blog/2025/06/02/goose-panther-mcp), also read, which introduced the Panther MCP and the review gate.

## Themes
- one-job-per-agent: sub-recipes `workflow_setup`, `similar_rule_analyzer`, `schema_and_sample_events_analyzer`, `rule_creator`, `testing_validator`, `pr_creator`; each returns standard JSON; main recipe stops on critical failure.
- human-review-gates: output is a draft PR; detection team "reviews each detection against defined quality benchmarks" before staging or production (June post); at least two unit tests per detection.
- harness-portability: AGENTS.md is the single source of standards; `.goosehints` and `CLAUDE.md` point to it.
- non-engineer-builders: threat intel, compliance and subject-matter experts in other services can write detections (June post).

## Key points
- Explicit parameters (`skip_similar_rules_check`, `create_pr`) and runtime conditions make the agent follow rules rather than infer them.
- Recipes preferred over always-on context files because only task-relevant instructions load.
- No measured results ("minutes instead of hours").
