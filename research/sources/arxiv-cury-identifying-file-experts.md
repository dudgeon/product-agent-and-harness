---
title: "Identifying Source Code File Experts"
source_url: https://arxiv.org/abs/2208.07501
author: Otávio Cury, Guilherme Avelino, Pedro Santos Neto, Ricardo Britto, Marco Túlio Valente
publisher: arXiv / ESEM 2022
published: 2022-08-16
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [ownership-inference, tacit-knowledge-capture]
relevance: medium
---
## Relevance to the project
The accuracy ceiling for "who knows this code" from repository history: against an oracle built from history plus developer self-reports across 113 projects, machine-learning classifiers reached F-measure 71-73% on public data, and on private (company) data linear techniques scored 55-68% and ML 58-67%. So commit-history ownership inference is right roughly two times in three inside a company; a dependency agent routing asks by code history needs a human confirmation step.

## Themes
- ownership-inference: "First Authorship" correlates most positively with knowledge and "Recency of Modification" most negatively (abstract); ML gives higher precision, linear techniques higher recall.
- tacit-knowledge-capture: the oracle relies on developers' own reports of what they know, the signal history alone misses.

## Key points
- Journal extension (Information and Software Technology, 2024) reports the models improved a Truck Factor algorithm (search summary).

## Could not verify
- Per-technique precision/recall and oracle size.
