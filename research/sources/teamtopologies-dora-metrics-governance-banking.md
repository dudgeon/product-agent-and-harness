---
title: "When DORA metrics meet governance in banking - Expert View"
source_url: https://teamtopologies.com/news-blogs-newsletters/when-dora-metrics-meet-governance-in-banking
author: Team Topologies (with contributions from Kosli, Google Cloud DORA and Deutsche Bank)
publisher: Team Topologies
published: 2026-01-22
retrieved: 2026-10-28
type: article
evidence: anecdote
filed_by: research-dependency-agent
themes: [process-governance-load, coordination-cost-and-waiting, human-review-gates, governance-as-code, regulatory-drivers-of-process]
relevance: medium
---

## Relevance to the project
A practitioner round-up on change governance in banks: a large bank still approving production releases through CAB meetings after a decade of DevOps, a Morgan Stanley engineer's count of "3 different Jiras, a change ticket, and 81 individual steps" to get one line of code through paperwork and approval, and Deutsche Bank's experience running DORA surveys across a global engineering organisation. It is the clearest first-hand description in this sweep of the evidence-gathering burden on a regulated product team, though the figures are single anecdotes and one contributor sells change-evidence tooling.

## Themes
- process-governance-load: one engineer's documented path for a single line of code: "It required 3 different Jiras, a change ticket, and 81 individual steps just to get the paperwork created and approved" (Morgan Stanley example).
- human-review-gates: restates the FCA finding that "CABs approved over 90% of the major changes they reviewed" and Accelerate's finding that external approval is negatively correlated with lead time, deployment frequency and restore time, with no correlation to change fail rate.
- governance-as-code: code review, security checks, change approvals, audit reporting and deployment gates are mostly human-driven; evidence gathering is manual and audits find gaps that create more remediation paperwork, a "doom loop".
- regulatory-drivers-of-process: banks must implement change management, but the processes are manual and slow to keep pace; a regulator reported significant findings about the bank's CAB.

## Key points
- Deutsche Bank: about 75% of teams identified trunk-based development as low-capability, high-impact; it found DORA's four keys coarse-grained and added custom lower-level measures; "Treat DORA as the start of a conversation, not the end."
- DORA's perceptual survey can skew: more mature teams may rate themselves more harshly.
- Recommendations mirror DORA's: peer review as segregation of duties, continuous risk analysis, platform as a product, clear communication of approval processes.

## Could not verify
- The year is inferred from page screenshots dated January 2026. The Morgan Stanley figure is reported second-hand through a contributor (Kosli, a change-evidence vendor), not from a Morgan Stanley publication; treat as anecdote.
