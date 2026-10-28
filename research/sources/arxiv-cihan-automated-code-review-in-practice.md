---
title: "Automated Code Review In Practice"
source_url: https://arxiv.org/abs/2412.18531
author: Umut Cihan, Vahid Haratian, Arda İçöz, Mert Kaan Gül, Ömercan Devran, Emircan Furkan Bayendur, Baykal Mehmet Uçar, Eray Tüzün
publisher: arXiv (ICSE 2025 SEIP track)
published: 2024-12-24
retrieved: 2026-10-26
type: paper
evidence: independent
filed_by: research-shared-persistent-agents
themes: [human-review-gates, verification-capacity-gap, vendor-claims-vs-independent-evidence, agent-failure-modes]
relevance: high
---
## Relevance to the project
An independent industrial study of an LLM reviewer agent (built on the open-source Qodo PR Agent) used by about 238 practitioners: 73.8% of its comments were resolved, but average PR closure time rose from 5h52m to 8h20m. This is the measured counterweight to catalogue item 5 (a reviewer agent waiting on a shared artifact): the reviewer was mostly heeded, yet it added reviewer and author load rather than removing it. Useful for the "reviewer load" side of any review-agent proposal.

## Themes
- human-review-gates: 73.8% of automated comments were resolved across 4,335 PRs in three projects (1,568 with automated reviews) (abstract; independent, 2024-12)
- verification-capacity-gap: "the average pull request closure duration increased from five hours 52 minutes to eight hours 20 minutes", trends varying by project (abstract)
- agent-failure-modes: practitioners reported "faulty reviews, unnecessary corrections, and irrelevant comments" (abstract; survey of 22 practitioners)
- vendor-claims-vs-independent-evidence: an academic/industry study of a deployed tool, contrasting with vendor resolution-rate tables (e.g. cursor-bugbot-learning)

## Key points
- Method: PR data with labels for whether developers acted on comments; per-PR surveys; a general survey of 22 practitioners.
- Most practitioners saw a minor quality improvement; benefits cited were bug detection, code-quality awareness and best practices.
- "Resolved" is not the same as "correct": resolution can include dismissal-by-fix of trivial comments.

## Notable quotes
- "73.8% of automated comments were resolved."
- "...it also led to longer pull request closure times..."

## Could not verify
- The company is not named on the abstract page; read via abstract only, not full text.
