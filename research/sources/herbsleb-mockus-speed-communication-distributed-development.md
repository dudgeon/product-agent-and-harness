---
title: "An Empirical Study of Speed and Communication in Globally Distributed Software Development"
source_url: https://herbsleb.org/web-pubs/pdfs/Herbsleb-Empirical-2003.pdf
author: James D. Herbsleb and Audris Mockus
publisher: IEEE Transactions on Software Engineering 29(6)
published: 2003-06-01
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [coordination-cost-and-waiting, dependency-knowledge-carriers]
relevance: high
---

## Relevance to the project
The classic measured study of coordination delay: using change-management data and surveys at Lucent, work items spanning sites took about two and a half times as long as comparable single-site items, and the main mechanism was that they involved more people. It is the best-evidenced anchor for the claim that every extra party a piece of work must pass through adds calendar time, which is the core economics of cross-team and cross-platform dependencies. It was replicated in a second organisation.

## Themes
- coordination-cost-and-waiting: "distributed work items appear to take about two and one-half times as long to complete as similar items where all the work is colocated" (Abstract).
- coordination-cost-and-waiting: "the number of people involved is strongly related to the calendar time to complete a work item" (Abstract).
- dependency-knowledge-carriers: survey results on distributed social networks: less awareness of who is doing what at the other site, linked to delay (Survey sections).

## Key points
- Data: modification requests from the source-code change-management system plus survey data; sites in the UK (about 40 people), Germany (about 75) and India (about 30) in the main organisation; analysis replicated in a different organisation, product and sites.
- Cites earlier time-use studies: developers spent an average of 75 minutes a day in "unplanned interpersonal interaction" (Perry et al., cited in the introduction).
- Implication drawn by the authors: tools and practices that restore awareness and informal communication could speed distributed work "dramatically".
- Caveat for transfer: the unit is geographic distribution, not organisational boundaries, but the mechanism (more people, less awareness, slower) is the same one internal-platform dependencies trigger.
