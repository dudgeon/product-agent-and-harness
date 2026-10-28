---
title: "Beyond Duplicates: Towards Understanding and Predicting Link Types in Issue Tracking Systems"
source_url: https://arxiv.org/abs/2204.12893
author: Clara Marie Lüders, Abir Bouraffa, Walid Maalej
publisher: arXiv / MSR 2022
published: 2022-04-27
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [dependency-detection-automation, dependency-types-and-practices, stale-records-mislead-agents]
relevance: medium
---
## Relevance to the project
The dataset study behind issue-link prediction: 607,208 links among 698,790 issues in 15 public Jira repositories, with 75 link types (Depend, Incorporate, Split, Cause among the common custom ones) grouped into five categories. It shows that the "dependency graph" already in an organisation's tracker is a heterogeneous, inconsistently labelled thing; an agent reading it has to normalise vocabulary before it can reason about sequencing.

## Themes
- dependency-types-and-practices: 75 link types grouped into General Relation, Duplication, Composition, Temporal/Causal and Workflow (abstract); dependency-like links sit in Temporal/Causal.
- dependency-detection-automation: two state-of-the-art duplicate detectors confused Duplication with other link types in nearly all repositories; accuracy dropped about 6% and 12%; adding other link types to training partly mitigated it (abstract).
- stale-records-mislead-agents: custom link types proliferate per repository; Composition links form trees 97.7% of the time while General Relation links show higher transitivity (abstract), i.e. link semantics vary by type and by team.

## Key points
- Authors share analysis code and labelled data.
- Frequency of Depend/Block links specifically is in the full paper, not the abstract.

## Could not verify
- Per-type counts for Depend and Block.
