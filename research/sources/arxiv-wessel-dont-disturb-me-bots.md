---
title: "Don't Disturb Me: Challenges of Interacting with Software Bots on Open Source Software Projects"
source_url: https://arxiv.org/abs/2103.13950
author: Mairieli Wessel, Igor Wiese, Igor Steinmacher, Marco A. Gerosa
publisher: arXiv / Proc. ACM CSCW 2021
published: 2021-03-25
retrieved: 2026-10-26
type: paper
evidence: independent
filed_by: research-shared-persistent-agents
themes: [public-by-default-agent-work, agent-failure-modes, human-review-gates]
relevance: high
---
## Relevance to the project
The pre-LLM baseline for the "noise" objection to shared agents: interviews with 21 maintainers, contributors and bot developers found that noise is the central problem bots create in pull requests, overwhelming and distracting people and disrupting both communication and workflow. Agents that post into shared threads, PRs or channels (catalogue items 5, 6, 4's morning reports) inherit this failure mode; the paper's fix (reconfigure or redesign the bot) and the follow-up "bot mediator" idea are design inputs. Independent academic evidence, 2021, so about deterministic bots rather than LLM agents.

## Themes
- public-by-default-agent-work: developers perceive repetitive bot behaviour ("creating numerous pull requests and leaving dozen of comments in a row") as noise that leads to information overload (findings; CSCW 2021)
- agent-failure-modes: noise was the most prominent of the challenges and disrupts communication and workflow (abstract)
- human-review-gates: the coping response was to reconfigure or redesign the bot; the follow-up ICSE 2022 design-fiction study ("Bots for Pull Requests: The Good, the Bad, and the Promising", 32 practitioners, 22 design strategies) proposed a separate interface area for bot output and a "bot mediator" that summarises other bots

## Key points
- Main contribution: a theory of how developers come to see annoying bot behaviour as noise on social coding platforms.
- Implication for agent design: summarisation/digest of agent activity and a quieter separate lane, rather than per-event comments.
- Counter-evidence for targeted requests (added by research-dependency-agent, 2026-10-28): Microsoft's Nudge (arxiv-maddila-nudge-overdue-pull-requests) cut overdue pull-request resolution time by 60% in a randomised trial and had 73% of reminders resolved as positive, by suppressing reminders where work was already moving and nudging only the identified blocker; the Dependabot study (arxiv-he-dependabot-exploratory-study) found high receptiveness but heavy configuration to cut notifications and 11.3% of projects abandoning the bot.

## Could not verify
- Read via abstract page and search summaries; the follow-up ICSE 2022 paper was not opened.
