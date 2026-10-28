---
title: "Nudge: Accelerating Overdue Pull Requests Towards Completion"
source_url: https://arxiv.org/abs/2011.12468
author: Chandra Maddila, Sai Surya Upadrasta, Chetan Bansal, Nachiappan Nagappan, Georgios Gousios, Arie van Deursen
publisher: arXiv / ACM TOSEM 32(2)
published: 2020-11-25
retrieved: 2026-10-28
type: paper
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-originated-requests, coordination-cost-and-waiting, ownership-inference]
relevance: high
---
## Relevance to the project
The strongest evidence that machine-originated chasers work when they are targeted: Microsoft's Nudge predicts when a pull request is overdue, suppresses the reminder if enough activity is already happening, identifies who is actually blocking it (author or a specific reviewer), and nudges only that person. In a randomised trial over 8,500 pull requests in 147 repositories it cut resolution time by 60% against overdue PRs that got no nudge; 73% of notifications were resolved as positive; scaled to 8,000 repositories it sent 210,000 notifications in a year with similar results. These are the three design moves a dependency agent's chasing loop needs.

## Themes
- agent-originated-requests: effort-estimation/ML completion-time prediction, activity detection to filter PRs already moving, actor identification "to nudge the appropriate blocker" (abstract).
- coordination-cost-and-waiting: 60% reduction in PR resolution time in the randomised trial.
- ownership-inference: actor identification decides who the blocker is; the authors list dependencies among PRs and developer availability as future work.

## Key points
- Deployed at Microsoft since 2019; Microsoft and academic authors, labelled first-party.
- Counterpoint to bot-noise findings (arxiv-wessel-dont-disturb-me-bots): selective, well-targeted nudges were welcomed.
