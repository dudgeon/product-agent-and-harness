---
title: "Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency"
source_url: https://arxiv.org/abs/2605.30208
author: Chris Adams et al. (31 authors, Meta, incl. Audris Mockus, Peter Rigby, Nachiappan Nagappan)
publisher: arXiv
published: 2026-05-28
retrieved: 2026-10-28
type: paper
evidence: first-party
filed_by: research-dependency-agent
themes: [risk-sloped-review, human-review-gates, coordination-cost-and-waiting, vendor-claims-vs-independent-evidence]
relevance: medium
---
## Relevance to the project
The strongest production evidence that risk-stratified automation can take routine approvals off humans without raising incidents: RADAR combines eligibility gates, heuristics, the Diff Risk Score, LLM review and deterministic checks to auto-review and land low-to-medium-risk diffs at Meta, and has reviewed 535K+ and landed 331K+. It is the model for how a dependency agent could earn the right to auto-clear low-risk asks while routing the rest to people, and it is driven by the same pressure: agentic AI accounts for over 80% of the growth in code volume that outran reviewer capacity.

## Themes
- risk-sloped-review: relaxing the risk threshold from the 25th to the 50th percentile raised the approve rate to 60.31% (abstract).
- human-review-gates: riskier diffs go to human review; deterministic validation precedes landing.
- coordination-cost-and-waiting: median time to close down "by over 330%" (the paper's phrasing) and median review wall time down 35%; lines per landed diff +105.9% YoY and per-developer diff volume +51%.
- vendor-claims-vs-independent-evidence: revert rate one-third and production incident rate one-fiftieth of non-RADAR diffs, but RADAR handles the easier, eligible population, so the comparison is not like-for-like.

## Key points
- Meta authors on Meta practice: first-party; not peer-reviewed at time of reading.
