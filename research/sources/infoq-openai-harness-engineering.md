---
title: OpenAI Introduces Harness Engineering: Codex Agents Power Large-Scale Software Development
source_url: https://www.infoq.com/news/2026/02/openai-harness-engineering-codex
author: Leela Kumili (InfoQ), reporting OpenAI (Ryan Lopopolo)
publisher: InfoQ
published: 2026-02-21
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-over-model, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Secondary report of OpenAI's "harness engineering" experiment (about a million lines, no hand-written code, about five months). The harness here is the repo environment (docs, linters, layered architecture, observability), not a runtime, which widens the meaning of "harness" for the taxonomy. OpenAI's own post returned HTTP 403 to the fetcher.

## Themes
- harness-over-model: engineer work shifts to designing environments, intent and feedback; harness = docs as source of truth, enforced architecture layers, observability agents can read.
- evals-autonomy-trust: structural tests and linters enforce constraints.

## Key points
- Source of truth is a structured docs directory with execution plans and design specs, enforced by linters and CI.
- Layered architecture: Types, Config, Repo, Service, Runtime, UI, checked by structural tests.
- Agents read logs, metrics and spans to reproduce bugs.
- Figures (about 1M lines, about 1,500 PRs, 3 to 7 engineers, about 1/10th the time) are OpenAI's own and per other coverage; not independently verified.
- Martin Fowler calls harness engineering a valuable framing.

## Could not verify
- OpenAI primary post (openai.com/index/harness-engineering/) not fetched: HTTP 403. Metrics come from InfoQ and search summaries.
- InfoQ states it does not discuss limitations.
