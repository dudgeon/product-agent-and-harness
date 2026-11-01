---
title: "Software Documentation Issues Unveiled"
source_url: https://emadpres.github.io/pdfs/icse2019.pdf
author: Emad Aghajani, Csaba Nagy, Olga Lucero Vega-Márquez, Mario Linares-Vásquez, Laura Moreno, Gabriele Bavota, Michele Lanza
publisher: ICSE 2019 (IEEE/ACM 41st International Conference on Software Engineering), pp. 1199-1210
published: 2019-05
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms, stale-records-mislead-agents]
relevance: medium
---

## Relevance to the project
A taxonomy of 162 documentation issue types from 878 real artefacts (issues, pull requests, mailing lists, Stack Overflow) that gives the project usable definitions for its criteria: correctness, completeness and up-to-dateness are distinct failures, and up-to-dateness means information that was right until something changed. It bears on how to define freshness and accuracy measurably for written-back context, and shows the preventive mechanisms projects actually adopted: docs updates as a required item in the contribution checklist or pull request acceptance.

## Themes
- context-trust-mechanisms: content issues ("what" is written) appear in 485 artefacts: completeness 268, up-to-dateness 190, correctness 72 (section IV.A); up-to-dateness is 39% of content issues, completeness 55%.
- stale-records-mislead-agents: "A document is outdated when it is not in sync with other parts of a system"; outdated references (links to old versions) were the most frequent up-to-dateness issue (section IV.A, Up-to-dateness).

## Key points
- Definitions (section IV.A): correctness = accurate in accordance with facts; completeness = contains what users need to do their tasks; up-to-dateness differs from both because "the information was correct and complete before a change was introduced". These map onto the project's accuracy, coverage and freshness criteria respectively.
- In 21% of up-to-dateness cases the mismatch was between system behaviour and its description; sometimes it was unclear whether the code or the doc was wrong ("Is this an error in the code, or an error in the documentation?") (same section). A written-back record can be right while the world is wrong; contestability must allow either side to move.
- Incorrect documentation can cause real harm: a false "safe to delete" claim could cause permanent data loss (correctness example).
- Preventive practice observed: docs update as a contribution checklist item, or mandatory for pull request acceptance (Up-to-dateness discussion). Implication proposed by the authors: traceability between docs and the things they describe, and regression tests for code examples (Discussion and Implications).
- Method: 878 artefacts sampled for 99% confidence ± 4.5% and manually labelled (section III).
