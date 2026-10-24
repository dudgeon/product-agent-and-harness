---
title: Thoughts On A Month With Devin
source_url: https://www.answer.ai/posts/2025-01-08-devin
author: Answer.AI (Hamel Husain and colleagues)
publisher: answer.ai
published: 2025-01-08
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, agent-failure-modes, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
The best-known independent evaluation of a fully delegated cloud agent: 20 real tasks over a month, 3 successes, 14 failures, 3 inconclusive; success was unpredictable and Devin pursued impossible tasks rather than flagging blockers. Dated (January 2025; product has changed) but it states the failure modes any delegation-to-remote-agent design must handle: unpredictability, no early blocker detection, hard-to-review output.

## Themes
- `agent-failure-modes`: Failure modes: overcomplicated 'code soup', loops, pursuing infeasible goals for days, hallucinated features and false-positive security findings, poor fit with existing codebase conventions, debugging tunnel vision.
- `evals-autonomy-trust`: Team preferred incremental human-guided tools (Cursor); salvaging failed runs often cost more than doing the task.
- `remote-agent-invocation`: Interaction via Slack with a Docker-based agent (browser, editor, shell); async chat UX was polished.

## Key points
- Successes: planet tracker, Notion-to-Google-Sheets migration, Discord-summary-bot research. Inconclusive included a security review of a small codebase.
- Could not predict which tasks would work, even among similar tasks.

## Could not verify
- Evaluates Devin as of late 2024/early 2025; no later independent equivalent was found for Devin, Codex cloud, Jules or Claude Code web.
