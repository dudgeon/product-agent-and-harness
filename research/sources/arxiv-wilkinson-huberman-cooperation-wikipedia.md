---
title: "Assessing the value of cooperation in Wikipedia"
source_url: https://arxiv.org/abs/cs/0702140
author: Dennis M. Wilkinson and Bernardo A. Huberman (HP Labs)
publisher: arXiv (cs.DL); also published in First Monday, 2007
published: 2007-02-23
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms]
relevance: medium
---

## Relevance to the project
The main quantitative evidence that more edits and more distinct editors go with higher quality, once you control for how visible and how old an article is. It bears on the "trust by use with corrections" mechanism for written-back context: use and repeated correction by many people predict quality, but only where enough people look. For low-traffic enterprise records (a niche platform card, a rarely used gate), the same mechanism will not run, so the signal is weakest where it is most needed.

## Themes
- context-trust-mechanisms: featured articles (1,211, chosen by the community for accuracy, neutrality, completeness, style) have significantly more edits and more distinct editors than other articles of the same PageRank band and the same age (section "Edits and article quality", Figures 4 and 5).

## Key points
- Edits accrete to an article in proportion to the edits it already has, giving a lognormal distribution with a heavy tail of highly visible, heavily edited articles (sections 2-3). Attention concentrates; most articles get little.
- The quality comparison controls for visibility (grouping articles by Google PageRank), for front-page exposure (edits during the featured period discounted), and for age (log edits normalised by the mean and variance for articles of the same age) (Figures 4-5). Without those controls the correlation would be confounded: older and more visible pages simply have more edits.
- Measurable definition the project can borrow: quality proxy = community-assigned featured status; effort proxy = age-normalised edit count and distinct-editor count.
- Featured status is itself revocable: featured articles that stop meeting the criteria are demoted (same section). A quality label with a demotion path, not a one-off certificate.

## Could not verify
- Effect sizes are shown in figures, not tabulated; I report direction and significance only.
