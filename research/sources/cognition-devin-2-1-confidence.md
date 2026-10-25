---
title: "Devin 2.1"
source_url: https://cognition.com/blog/devin-2-1
author: Cognition
publisher: Cognition blog
published: 2025-05-15
retrieved: 2026-10-25
type: article
evidence: vendor-claim
filed_by: research-skill-rigidity-spectrum
themes: [evals-autonomy-trust, agent-led-intent-shaping, human-review-gates]
relevance: medium
---

## Relevance to the project
Devin's confidence score is a shipped mechanism for deciding when an agent should ask rather than act: a green/yellow/red self-rating at session start, after planning and when answering code questions; below green, Devin asks clarifying questions. Cognition also uses the score to triage a backlog (score issues in Linear or Jira without starting sessions, then work only the high-confidence ones). It contrasts with Ramp's Policy Agent, which rejected numeric confidence in favour of categories (ramp-builders-agents-users-can-trust).

## Themes
- evals-autonomy-trust: vendor claims "Confidence Scores are highly correlated with task success" and green gives "twice the likelihood of a merged PR compared to" red.
- agent-led-intent-shaping: below green, Devin asks clarifying questions; developers raise the score by answering or giving guidance.
- human-review-gates: batch confidence scoring of Linear/Jira issues lets teams route only high-confidence work to the agent; can auto-scan new issues.

## Key points
- Classification: gate = model self-assessment (three categories, not a number); stance = ask when uncertain; decision rights = humans pick which scored issues to delegate.

## Could not verify
- The 2x merged-PR figure has no published method or sample size. Current docs may differ from this 2025 post.
