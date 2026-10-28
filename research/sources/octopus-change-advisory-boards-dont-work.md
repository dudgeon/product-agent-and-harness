---
title: "Change Advisory Boards Don't Work"
source_url: https://octopus.com/blog/change-advisory-boards-dont-work
author: Alex Yates
publisher: Octopus Deploy blog
published: 2020-07-16
retrieved: 2026-10-28
type: article
evidence: anecdote
filed_by: research-dependency-agent
themes: [process-governance-load, coordination-cost-and-waiting, human-review-gates, risk-sloped-review]
relevance: low
---

## Relevance to the project
A practitioner's statement of the "CAB is theatre" case: a weekly CAB turns a one-hour change into a 40-business-hour wait, batches changes into riskier deployments, and reviews with too little context, producing "a theater of security". Useful as the canonical critique and for its list of alternatives (audited pull requests, pipeline approval steps, low-risk bypass criteria, a daily mini-CAB for low and medium risk). Written by a consultant partnered with a deployment-tool vendor, so read as opinion.

## Themes
- coordination-cost-and-waiting: a change that takes an hour to write can wait 40 business hours (168 clock hours) for a weekly CAB.
- human-review-gates: reviewers lack context, individual changes get little scrutiny, meetings become rubber-stamping.
- risk-sloped-review: let low-risk changes bypass the CAB if they meet criteria (automated pipeline, peer review, passing tests, within error budget); keep the full CAB for high-risk changes.
- process-governance-load: auditability matters more to regulators than the review format; pull requests with branch protection or logged pipeline approvals can provide it (author's view; advises seeking legal advice).

## Key points
- Cites Accelerate (Forsgren, Humble, Kim, 2018; data from the 2014-2017 State of DevOps surveys): external approvals negatively correlated with lead time, deployment frequency and restore time, no correlation with change fail rate.
- Cites "about 80%" of outages resulting from change (attributed to Visible Ops, The DevOps Handbook and Gartner; not verified).
- Accepts CAB goals as "undoubtedly positive"; the problem is implementation.
