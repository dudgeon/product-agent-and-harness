---
title: "Knowledge-Based Trust: Estimating the Trustworthiness of Web Sources"
source_url: https://arxiv.org/abs/1502.03519
author: Xin Luna Dong, Evgeniy Gabrilovich, Kevin Murphy, Van Dang, Wilko Horn, Camillo Lugaresi, Shaohua Sun, Wei Zhang (Google)
publisher: arXiv; PVLDB 8(9), 2015
published: 2015-02-12
retrieved: 2026-10-31
type: paper
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms]
relevance: high
---

## Relevance to the project
Google's method for judging a source by the correctness of the facts it states (endogenous) rather than by its popularity or links (exogenous), and the finding that the two signals are almost orthogonal. It bears on which trust mechanism to use: "trust by use" (how often a record is read or linked) measures popularity, not correctness; a source's trust should come from how often its claims check out against other evidence. It also names the weaknesses of consensus from several sources: copying between sources, trivial or off-topic facts, and limited coverage.

## Themes
- context-trust-mechanisms: of 15 popular gossip sites, 14 had PageRank in the top 15% but all had KBT in the bottom 50%; of 100 sampled sites with KBT above 0.9, 85 were judged truly trustworthy on manual review, but only 20 of those 85 had PageRank over 0.5 (section 5.4.1).

## Key points
- Scale: 2.8B facts extracted from 2B+ pages on 26M sites; enough correctly extracted facts (at least 5 triples) to score 119M pages and 5.6M sites; 52% of sites scored above 0.8 (section 5.4).
- Trustworthiness is defined as the probability that a source provides a correct value for a fact (section 1). A measurable definition the project can use directly for an expert or a document: share of its checkable claims that later checks confirm.
- Multi-layer model separates extraction errors (the reader misread the source) from source errors (the source is wrong) (abstract, section 3). The analogue: an agent mis-summarising an owner is a different failure from the owner being wrong; both must be tracked.
- Manual check of high-KBT sites: 12 of 100 had too few non-trivial facts and 2 were off-topic (section 5.4.1). Agreeing on trivial facts inflates trust.
- Stated limits (section 5.4.2): need to filter topic-irrelevant and trivial triples; extractors cover only some sites; "Some websites scrape data from other websites", so copy detection is needed before agreement counts as independent confirmation.
- Evaluation is by the method's own authors; there is no ground truth for web-page quality, so PageRank is used as a contrast, not a benchmark.

## Notable quotes
- "As expected, the two signals are almost orthogonal." (section 5.4.1, KBT vs PageRank)
