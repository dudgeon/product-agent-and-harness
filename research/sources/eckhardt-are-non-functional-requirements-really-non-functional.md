---
title: "Are \"Non-functional\" Requirements really Non-functional? An Investigation of Non-functional Requirements in Practice"
source_url: https://arxiv.org/abs/1611.08868
author: Jonas Eckhardt, Andreas Vogelsang, Daniel Méndez Fernández
publisher: Proceedings of the 38th International Conference on Software Engineering (ICSE 2016); arXiv preprint
published: 2016-05-14
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: define-shaping-and-dependency-agents
themes: [requirements-partitions]
relevance: medium
---

## Relevance to the project
Empirical evidence that the functional versus non-functional split does not survive contact with real specifications: the authors classified 530 requirements labelled "non-functional" in 11 industrial specifications and found that most describe system behaviour, so they could be specified and tested like functional requirements. For a requirements taxonomy that an agent will use to sort a feature's obligations, this says a quality-attribute partition will put many "quality" items in the functional class once they are written precisely enough to act on, which is exactly the point at which the agent needs them. The companion survey (arXiv 1611.08830, 103 practitioners) found that teams treat the two kinds differently in process, for reasons "based on expectations rather than on evidence".

## Themes
- requirements-partitions: 530 NFRs from 11 industrial specifications; "most" describe system behaviour and are therefore not non-functional in the usual sense (abstract). The 2016 PROFES companion paper reports that practitioners' process differences between functional and quality requirements rest on expectation, not evidence (abstract of arXiv 1611.08830).

## Key points
- Research question: do requirements documented as non-functional actually describe how the system behaves, rather than qualities of it?
- Method: manual classification of 530 NFRs across 11 industrial requirements specifications.
- Finding: the majority describe behaviour; the authors argue they can be handled with functional-requirement methods (precise specification, testing).
- Implication drawn by the authors: the FR/NFR label should be a conscious decision with known risks, not a default.

## Could not verify
- The exact share ("most") is not given on the abstract page; the full paper gives the breakdown by kind and was not read in this pass.
