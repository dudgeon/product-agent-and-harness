---
title: "Operational Readiness Reviews (ORR) (AWS Well-Architected whitepaper)"
source_url: https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html
author: Amazon Web Services
publisher: AWS documentation
published: 2022-06-30
retrieved: 2026-11-06
type: docs
evidence: first-party
filed_by: design-requirements-agent
themes: [launch-readiness-review, skill-improvement-loops, rules-vs-judgment-encoding, compounding-context-repo]
relevance: high
---

## Relevance to the project
AWS's description of how it built its Operational Readiness Review program: post-incident analyses (Correction of Errors) are distilled into curated questions with guidance, checklist templates are generated per workload type, teams self-assess across the whole lifecycle, an "Ops Champion" challenges the answers, and a working group turns new incidents into new questions. It is the cleanest public example of an obligation library that is grown from the organisation's own failures rather than written top-down, with a stated rule to include only risks severe enough to block general availability. Read pages: the overview, "The ORR tool" and "Iteration".

## Themes
- launch-readiness-review: ORR "distills the learnings from AWS operational incidents into curated questions with best practices guidance"; teams review the appropriate checklist "from inception to post-release operations" (overview).
- rules-vs-judgment-encoding: each question has guidance and a risk-rated answer (example: "Do any of your hosts pin certificates?" Yes = High Risk, No = No Risk) (The ORR tool).
- skill-improvement-loops: Ops Champions both challenge teams during the review and act as a working group that reviews COE outcomes and creates new questions, verifying results can be measured and setting risk severity (Iteration).
- compounding-context-repo: the core value is "using the data from your own post-incident analysis to generate best practices"; checklists are tailored by workload type (serverless application, user console, server agent) from user feedback (overview; Iteration).

## Key points
- Inclusion rule: only critical risks "that would prevent a General Availability (GA) launch" go in; medium and low risks are left out to keep the process light (The ORR tool).
- Sources for questions: real incidents, near-misses, and failure modes that have not happened yet but worry you.
- Suggested grouping: architecture, release quality, event management; or finer: deployment safety, defence against customers, defence against dependencies, data recovery, operator safety, blast radius, event detection, restart, forensics, escalation.
- Tooling: a web service generates templates, records results and residual risk, links cautionary tales and files action items into the ticketing system; customers can build checklists as Well-Architected custom lenses.
- A yearly ORR per workload with a subset of best practices picks up newly added questions (from the related Well-Architected best practice OPS07-BP02, seen in search results only).

## Notable quotes
- "distills the learnings from AWS operational incidents into curated questions" (overview)

## Could not verify
- Appendix A (creating guidance from an incident) and Appendix B (example questions) were not read. The OPS07-BP02 yearly-review point is from a search-result summary, not a fetched page.
