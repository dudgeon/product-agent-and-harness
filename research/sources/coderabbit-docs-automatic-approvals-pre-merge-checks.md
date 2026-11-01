---
title: "Automatic approvals and Pre-merge checks (CodeRabbit docs)"
source_url: https://docs.coderabbit.ai/pr-reviews/automatic-approvals
author: CodeRabbit
publisher: CodeRabbit docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [human-review-gates, gate-judge-separation, risk-sloped-review, agent-ready-intent]
relevance: high
---

## Relevance to the project
CodeRabbit is the reviewer agent that can block: with automatic approvals on, it submits a request-changes review on actionable findings (which blocks merge under required-review rules) and approves once threads are resolved, checks pass and risk is within limits; custom pre-merge checks in natural language, including "Issue Assessment" against linked issues, can be set to `error` and block. This is the clearest documented case of a checker agent waiting on a shared artifact with an enforced, overridable gate, and of who may override it.

## Themes
- human-review-gates: CodeRabbit "requests changes on actionable findings and approves once its feedback is resolved"; it "does not merge the pull request, and your Git provider's other merge requirements still apply"; off by default; it checks HEAD has not changed immediately before approving.
- gate-judge-separation: pre-merge check modes `off`, `warning` (default, non-blocking) and `error` (blocks only with automatic approvals, "until resolved or manually overridden"); "Inconclusive" does not block; authors can "Ignore failed checks" per PR unless `override_requested_reviewers_only: true` restricts overrides to requested reviewers.
- risk-sloped-review: `max_merge_risk` and `max_security_risk` thresholds (minimal to critical) withhold approval; team or path overrides change limits.
- agent-ready-intent: built-in "Issue Assessment" checks PRs "address linked issues without containing out-of-scope changes"; custom checks (name 50 chars, instructions 1,000 chars, Team plan) run in a read-only sandbox with the diff, linked issues and MCP context.

## Key points
- Triggers: each new commit is reviewed; manual `@coderabbitai review`; `@coderabbitai run pre-merge checks`.
- Companion page: https://docs.coderabbit.ai/pr-reviews/pre-merge-checks (read). The older `reviews.request_changes_workflow` key maps to `reviews.auto_approvals.enabled`.
- Failure reported in CodeRabbit's KB (March 2026): GitHub Code Review Limits can stop the bot posting approve or request-changes reviews; a third-party repo disabled the workflow because CHANGES_REQUESTED blocked merges under an org ruleset (anecdote).
- Related: [claude-coderabbit-plan-orchestration](claude-coderabbit-plan-orchestration.md) (planning layer); Cursor's own comparison table puts CodeRabbit's resolution rate at 48.96% ([cursor-bugbot-learning](cursor-bugbot-learning.md), vendor-claim).

## Could not verify
- Which issue trackers count as "linked issues" (Jira, Linear, GitHub). Pages undated; read via WebFetch (model-summarised view).
