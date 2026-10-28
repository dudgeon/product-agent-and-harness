---
title: "DeepTriage: Automated Transfer Assistance for Incidents in Cloud Services"
source_url: https://arxiv.org/abs/2012.03665
author: Phuong Pham, Vivek Jain, Lukas Dauterman, Justin Ormont, Navendu Jain (Microsoft)
publisher: arXiv / KDD 2020
published: 2020-11-25
retrieved: 2026-10-28
type: paper
evidence: first-party
filed_by: research-dependency-agent
themes: [ownership-inference, agent-originated-requests, human-review-gates]
relevance: medium
---
## Relevance to the project
The production precedent for "route this to the right owning team" at enterprise scale: Microsoft Azure's incident router (gradient-boosted classifiers, clustering, deep nets) has run since October 2017, used daily by thousands of teams, at 82.9% F1 overall (76.3-91.3% for high-impact incidents). It is evidence both that owner routing can be learned from history and that it works as a recommender with a human in the loop, not as an autonomous router. A wrong assignment can increase time to mitigate by 10x.

## Themes
- ownership-inference: team recommendation from incident text and metadata, 82.9% F1 on real Azure incidents (abstract).
- agent-originated-requests: misrouting cost is large ("increase its time to mitigate by 10x"), the same failure a dependency agent risks by sending asks to the wrong owner.
- human-review-gates: engineers must trust recommendations; the paper frames it as transfer assistance (search summary notes top-5 recommendation matters less than top-1 only when a human corrects).

## Key points
- Hard because incident distributions are highly imbalanced across many teams and input formats vary.
- Microsoft authors describing Microsoft practice: labelled first-party.
