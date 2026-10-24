---
title: "Moving to issues as the new PRs"
source_url: https://goose-docs.ai/blog/2026/07/30/issues-are-the-new-prs
author: Douwe Osinga (software engineer, goose)
publisher: goose blog
published: 2026-07-30
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [agent-ready-intent, human-review-gates, human-judgment-pm-jobs, opportunity-to-code-chain]
relevance: medium
---

## Relevance to the project
The goose team's own answer to "what does a human hand an agent?": once agents make plausible code cheap, contribution moves upstream from the patch to the issue, and an issue passes Inbox, Accepted/design, Ready (an agent can now write the code), In progress, Verification (a human confirms it works), Done. PRs that do not implement a Ready issue are closed. It is a clean, documented example of shape-the-intent and review-the-change as the human gates, with the issue as the handoff artifact, though for an open-source project rather than a Block product team.

## Themes
- agent-ready-intent / opportunity-to-code-chain: the Accepted/design stage settles "intended design, architectural constraints, and verification approach" before an issue becomes Ready for an agent (issue lifecycle section).
- human-review-gates: human judgment sits at design before implementation and at Verification after (lifecycle).
- human-judgment-pm-jobs: deciding "whether a change belongs" and what the right design is stays expensive and human; "The unit of open source contribution is no longer the patch." (argument section)

## Key points
- Agent PRs arrive with design questions "apparently answered" by a chain of plausible choices; that is why design discussion moves into issues.
- Valued non-code contributions: reporting, reproducing bugs, domain knowledge, shaping design; all credited as commit co-authors.
- No issue template or acceptance-criteria format given; header image shows 184 open PRs.

## Could not verify
- Whether Block product teams use the same issue-first flow internally; the post is about the open-source goose repository only.
