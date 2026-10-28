---
title: "On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub"
source_url: https://arxiv.org/abs/2509.14745
author: Miku Watanabe, Hao Li, Yutaro Kashiwa, Brittany Reid, Hajimu Iida, Ahmed E. Hassan
publisher: arXiv
published: 2025-09-18
retrieved: 2026-10-26
type: paper
evidence: independent
filed_by: research-shared-persistent-agents
themes: [verification-capacity-gap, human-review-gates, vendor-claims-vs-independent-evidence]
relevance: medium
---
## Relevance to the project
An independent study of 567 Claude Code-generated PRs across 157 open-source projects: 83.8% were eventually merged (versus about 91% for human PRs in the authors' comparison), but 45.1% of merged agent PRs needed human revision first, mostly for bug fixes, documentation and project-specific standards. It tempers both the "slop" story and the vendor story: agent PRs are mostly accepted, and the cost shows up as human revision against local conventions, which is exactly what shared corrections (catalogue item 1) are meant to remove.

## Themes
- verification-capacity-gap: 45.1% of merged agent PRs required additional human changes before merge (abstract; v3 2026-02-09)
- human-review-gates: revisions cluster on bug fixes, documentation and "project-specific standards", the part a shared baseline could encode (abstract)
- vendor-claims-vs-independent-evidence: 83.8% merge rate measured on public repos; agents were used mostly for refactoring, docs and tests (abstract)

## Key points
- 54.9% of merged agent PRs went in unchanged.
- The human-PR comparison figure (about 91%) and the finding that rejections were often about project context (duplicate work, PR size) come from search-result summaries of the full paper, not verified by me.

## Could not verify
- Full text not read; rejection reasons and the human baseline are second-hand. No peer-reviewed venue listed on arXiv (a search summary says accepted to TOSEM; unconfirmed).
