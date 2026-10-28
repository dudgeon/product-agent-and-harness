---
title: "Bugbot now self-improves with learned rules"
source_url: https://cursor.com/blog/bugbot-learning
author: Michael Zhao (Cursor)
publisher: Cursor blog
published: 2026-04-08
retrieved: 2026-10-26
type: article
evidence: vendor-claim
filed_by: research-shared-persistent-agents
themes: [org-learning-loop, skill-improvement-loops, human-review-gates, vendor-claims-vs-independent-evidence]
relevance: high
---
## Relevance to the project
A shipped mechanism for "one person's correction becomes everyone's baseline" (catalogue item 1) inside a reviewer agent (item 5): Bugbot turns reactions and replies to its comments, plus human reviewers' comments, into candidate rules, promotes them as signal accumulates, and disables ones that attract negative signal. Cursor reports 110,000+ repos with learning on, 44,000+ learned rules, and a resolution rate rising from 52% (July 2025) to 78.13%. All vendor-reported, measured by an LLM judge on public repos, with competitors' rates in the same table.

## Themes
- org-learning-loop: each review is "a natural experiment that Bugbot can use to self-improve"; candidate rules come from reactions, replies and human reviewer comments on merged PRs (blog, 2026-04-08; vendor-claim)
- skill-improvement-loops: "As signal accumulates, Bugbot can promote a candidate rule to active status"; active rules with consistent negative signal are disabled; humans can edit or delete rules (blog)
- human-review-gates: resolution rate (comment addressed by merge, LLM-judged) Bugbot 78.13% on 50,310 PRs vs Greptile 63.49%, CodeRabbit 48.96%, GitHub Copilot 46.69%, Codex 45.07%, Gemini Code Assist 30.93% (comparison table; vendor-run)
- vendor-claims-vs-independent-evidence: the comparison is run by Cursor with its own LLM judge; contrast the independent 73.8% resolved / longer closure time in arxiv-cihan-automated-code-review-in-practice

## Key points
- "more than 110,000 repos have enabled learning, generating more than 44,000 learned rules"; Bugbot reviews "hundreds of thousands of PRs per day".
- Before this, improvement was "propelled exclusively by offline experiments".
- Scope of a learned rule (repo, team, org) is not stated.

## Could not verify
- No independent replication of the resolution figures; the judge prompt and sampling are not published.
