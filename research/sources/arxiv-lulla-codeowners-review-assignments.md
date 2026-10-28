---
title: "Automated Code Review Assignments: An Alternative Perspective of Code Ownership on GitHub"
source_url: https://arxiv.org/abs/2512.05551
author: Jai Lal Lulla, Raula Gaikovina Kula, Christoph Treude
publisher: arXiv
published: 2025-12-05
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [ownership-inference, stale-records-mislead-agents, legible-org-for-agents]
relevance: medium
---
## Relevance to the project
The first large-scale study of GitHub's CODEOWNERS (844,000+ pull requests, 1.9M comments, 2M+ reviews, 10,287 code owners): owners generally follow their files' rules, behave like traditional ownership metrics predict, and adopting CODEOWNERS shifts review load away from core developers. It is evidence that a declared, enforced ownership file is a usable "who to ask" signal for code, but it is "sparsely adopted" and the study does not measure staleness.

## Themes
- ownership-inference: declared owners' collaboration behaviour "is similar to traditional ownership metrics" (abstract), so commit-derived and declared ownership tend to agree where both exist.
- legible-org-for-agents: CODEOWNERS is a machine-readable ownership record enforced at review time; regression discontinuity shows adoption moves review responsibility (abstract).
- stale-records-mislead-agents: the paper does not measure decay; practitioner and patent sources assert ownership files go stale without measuring it (search results), a gap.

## Key points
- v2 revised 5 Aug 2026; not peer-reviewed at time of reading.
- 675 repositories with CODEOWNERS (645 syntactically valid) versus 675 without (search summary).

## Could not verify
- Adherence percentages and any staleness analysis in the full text.
