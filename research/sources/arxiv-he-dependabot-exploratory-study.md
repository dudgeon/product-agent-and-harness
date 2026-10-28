---
title: "Automating Dependency Updates in Practice: An Exploratory Study on GitHub Dependabot"
source_url: https://arxiv.org/abs/2206.07230
author: Runzhi He, Hao He, Yuxia Zhang, Minghui Zhou
publisher: arXiv / IEEE Transactions on Software Engineering
published: 2022-06-15
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [agent-originated-requests, public-by-default-agent-work]
relevance: medium
---
## Relevance to the project
The largest study of a bot that opens requests to humans about dependencies (here, package versions) across 1,823 GitHub projects. Developers are "highly receptive" to its pull requests and technical lag falls, yet they configure the bot to cut notifications, compatibility signals are too scarce to reduce suspicion, and 11.3% of projects dropped it. The authors' recipe for an ideal dependency bot (configurability, autonomy, transparency, self-adaptability) transfers directly to an agent that sends asks to owners.

## Themes
- agent-originated-requests: high receptiveness but notification management is the main coping behaviour; 11.3% of projects deprecated Dependabot (abstract).
- public-by-default-agent-work: volume of bot-originated requests drives configuration to suppress them.

## Key points
- Merge rate is the receptiveness measure (around 70-76% across groups in a results table seen via search; not verified).
- Package dependencies, not organisational ones: an analogy, not a direct test.
