---
title: "PerfInsights: Detecting Performance Optimization Opportunities in Go Code using Generative AI"
source_url: https://www.uber.com/us/en/blog/perfinsights/
author: Sung Whang, Joseph Wang, Lavanya Verma (Uber)
publisher: Uber Engineering Blog
published: 2025-07-22
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [deterministic-scaffold-model-nodes, model-judge-biases, evals-autonomy-trust]
relevance: low
---

## Relevance to the project
PerfInsights is a narrow, managed code-maintenance agent: fleet profiles pick the 30 hottest functions per Go service, an LLM checks each against a curated antipattern catalogue, and an LLM jury plus a rule-based checker cut false positives from over 80% to the low teens before suggestions flow to a code-optimisation tool. It is an example of the "managed agents" Uber says it is shifting to, and of deterministic filtering around model judgement.

## Themes
- deterministic-scaffold-model-nodes: static filtering to service-owned, top-cost functions ("the unsung hero"); one prompt per antipattern; LLMCheck rule validators (Architecture).
- model-judge-biases: multiple LLMs independently vote on each detection and fix (LLM jury).
- evals-autonomy-trust: detection accuracy metrics logged to spot model drift; validated detections 265/day (Feb) to 176 (June) as code improved.

## Key points
- Hackdayz 2024 finalist turned production; "hundreds" of merged diffs; detection-and-fix time from 14.5 hours to about 1 hour.
- Validated suggestions feed Optix, Uber's continuous code optimisation tool.

## Notable quotes
- "Tasks that once required days now take hours."

## Could not verify
- Total cost savings not given.
