---
title: "Reliable Product Launches at Scale (Site Reliability Engineering, chapter 27)"
source_url: https://sre.google/sre-book/reliable-product-launches/
author: Rhandeev Singh and Sebastian Kirsch, with Vivek Rau (ed. Betsy Beyer)
publisher: Google (O'Reilly)
published: unknown
retrieved: 2026-11-06
type: docs
evidence: first-party
filed_by: design-requirements-agent
themes: [launch-readiness-review, checklist-implementation-fidelity, skill-improvement-loops, risk-sloped-review]
relevance: high
---

## Relevance to the project
Google's own account of its launch review function (Launch Coordination Engineering) is the best public description of a launch checklist run at very high volume (up to 70 launches a week) and of how such a checklist is kept useful: every item must be justified, ideally by a past launch disaster; items must be concrete actions; the list is curated continuously and reviewed in full once or twice a year; shared infrastructure replaces long sections with one line; and low-risk launches get a shortened path. These are exactly the curation rules an obligation library for a requirements agent needs, and the fast-path idea is a model for risk-sloped questioning. It covers reliability, not legal or privacy review.

## Themes
- launch-readiness-review: a launch is "any new code that introduces an externally visible change"; LCE audits against reliability standards, liaises between SRE, development and product, and acts as gatekeeper signing off launches (LCE section).
- checklist-implementation-fidelity: engineers skip processes they see as burdensome, so the process must be "lightweight yet thorough"; a high-touch approach by experienced engineers tailors it per launch (Key lessons).
- skill-improvement-loops: every question must be substantiated, ideally by a previous launch disaster; adding one once required vice-president approval; full review once or twice a year with service owners (Keeping the checklist short).
- risk-sloped-review: low-risk launches get a shortened checklist; by 2008 about 30% of reviews were classed low-risk.

## Key points
- Nine checklist categories: architecture and dependencies; integration; capacity planning; failure modes; client behaviour; processes and automation; development process; external dependencies; rollout planning. Each pairs example questions with action items and links.
- Convergence on shared infrastructure shortens the checklist: instead of a section on rate limiting, one line pointing to the shared system. (The equivalent for obligations: point to the platform that already satisfies them.)
- Scale: one LCE handled 350 launches in 3.5 years; a new LCE needs about six months of training (the tacit knowledge an agent would have to carry).
- Limits: LCE could not fix scalability rearchitecture or infrastructure churn; those needed platform work.

## Could not verify
- Read through WebFetch's model-summarised view; the book was published in 2016 and the page shows a 2017 copyright, so the day-level publication date is left unknown. Google's separate privacy, security and legal launch approvals (sometimes reported under the internal tool name "Ariane") are not described in this chapter and were not found in any primary public source.
