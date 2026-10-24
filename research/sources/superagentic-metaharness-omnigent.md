---
title: Optimizing Databricks Omnigent Agents with MetaHarness
source_url: https://shashikantjagtap.net/optimizing-databricks-omnigent-agents-with-metaharness/
author: Shashikant Jagtap (Superagentic AI)
publisher: shashikantjagtap.net
published: 2026-06-13
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, harness-portability]
relevance: low
---

## Relevance to the project
A third-party tool vendor integrating with Omnigent on launch day: shows both senses of "meta-harness" meeting (a vertical harness optimiser driving the horizontal Omnigent layer). It reports practical friction (bundle layout, tmux, scratch files) from actually running it. Self-promotional, one smoke test.

## Themes
- [[meta-harness]]: MetaHarness 0.4.0 adds an experimental `OmnigentCliBackend` using Omnigent as the proposer; automatic meta-harness optimisation is only on Databricks' roadmap.
- [[harness-portability]]: the run used Omnigent's `codex` path because `codex-native` needed tmux locally; Codex scratch files (`.codex-tmp`) polluted diffs.

## Key points
- Smoke test result `best_objective=0.875` with no baseline or definition; winning candidate edited `AGENTS.md`, `config.yaml` and a review `SKILL.md`.
- Omnigent expects agent bundles as directories with `config.yaml`, not single YAML files; `os_env.cwd` had to point at the candidate workspace.
