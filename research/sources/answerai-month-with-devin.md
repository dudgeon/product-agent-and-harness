---
title: "Thoughts On A Month With Devin"
source_url: https://www.answer.ai/posts/2025-01-08-devin
author: Hamel Husain, Isaac Flath, Johno Whitaker (Answer.AI)
publisher: Answer.AI
published: 2025-01-08
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-failure-modes, human-review-gates, shared-persistent-sessions]
relevance: high
---
## Relevance to the project
One of the few independent, first-hand accounts of using an autonomous async cloud agent with Slack-based sessions: 3 successes, 14 failures, 3 inconclusive across 20 tasks. Names stuck runs, impossible-task persistence, over-engineering and unpredictability as failure modes. Dated January 2025, so Devin has since changed; treat as evidence about the autonomy pattern, not the current product.

## Themes
- agent-failure-modes: stuck loops (an HTML-parsing scraper task), a day spent on a platform-unsupported deployment while hallucinating features, tunnel vision on the wrong root cause, false-positive security findings
- human-review-gates: 'autonomy became a liability when Devin pursued dead ends instead of flagging blockers'; team found developer-driven tools like Cursor more effective for larger tasks because they allow incremental steering
- shared-persistent-sessions: the Slack-based chat and visible environment setup were polished; the unreliability was in the agent

## Key points
- Worked: small well-defined tasks, API glue code, research notes and plans.

## Could not verify
- Task list only partially visible in the retrieved summary.
