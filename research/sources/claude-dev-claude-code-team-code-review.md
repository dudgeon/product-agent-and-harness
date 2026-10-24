---
title: How the Claude Code team does code review
source_url: https://claude.dev/blog/solving-code-review-at-anthropic/
author: Addy Osmani, Morgan Westlee Lunt and Qing Wang (Anthropic)
publisher: claude.dev blog (Anthropic)
published: 2026-10-15
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [risk-sloped-review, human-review-gates, evals-autonomy-trust, org-learning-loop, agent-factory-sdlc, public-by-default-agent-work, compounding-context-repo]
relevance: high
---

## Relevance to the project
This is the most detailed first-party account of how one Anthropic product team runs the review, release and operate tasks now that Claude writes about 90% of the team's code. It covers seven layers of checks, a classifier that sets each change's risk tier, low-risk changes merging with no human approval, and incidents used as the reviewer's eval set. The playbook links to it for its Deploy stage, and it is the evidence for the review and release rows of the Anthropic PDLC map. It also says plainly what replaced review's second job, sharing context: there is no formal process. People ask Claude for an explainer of the code they need, and the team works in open Slack channels. That bears on the project's question of where context breaks between people. All figures are self-reported.

## Themes
- risk-sloped-review: three risk tiers set by the change, not the author: low (docs, copy, flagged additive changes) needs no human approval once checks are green; medium needs one person; high needs two. A classifier picks the tier and a second classifier can demand another person; some paths always need a human (§5 "Human approval, scaled by risk").
- human-review-gates: "an agent's approval never counts as a person's"; the person who directed the agent counts as one of the required reviewers; an approval covers one commit and is dismissed on new pushes (§5).
- evals-autonomy-trust: past incident-causing PRs, confirmed by engineers, form an eval the reviewer runs against daily; every reviewer change is scored on it; noise is measured by how authors respond to comments (§How we make the reviewer better).
- org-learning-loop: repeated reviewer findings are fixed at the source (skill, lint rule, CLAUDE.md, REVIEW.md); incident reviews ask "which layer should have caught the issue" (§1, §7).
- agent-factory-sdlc: a change can start "from an engineer's laptop (or a Claude session in Slack)" and passes self-verification, AI review, blocking security review, CI, risk-based approval, merge queue, flags and staged release (§The life of a change).
- public-by-default-agent-work: review's second job, building shared understanding, is now covered by Claude-written explainers on demand and by "our culture of defaulting to working on open Slack channels" (§Sharing context across the team).
- compounding-context-repo: CLAUDE.md (stack, conventions, goals, non-goals) loads on every review; code owners write REVIEW.md; the reviewer flags changes that make CLAUDE.md out of date (§1).

## Key points
- **Goal and measures.** The aim is for most PRs in the Claude Code repos to merge with at most one human (who can be the author), with no rise in reverts or incidents. The team tracks human approvals per PR, human comments and wait time; revert and incident rates are the guardrail. Reported: merged PRs more than doubled from June to September while the revert share fell by more than 40%. Monorepo changes landing per day went from about 2,500 in May to more than 30,000 in September.
- **The seven layers.**
  1. Self-verification before a PR exists: tests, build or screenshot output, a fresh-context subagent review, and internal skills for bug hunting, diff simplification and end-to-end checks.
  2. A Claude review on every PR against the repo and the PR's stated intent. Parallel agents find bugs and a separate group votes on each finding, so style-only findings are dropped. Every finding must be fixed or resolved with a reason. Substantive-comment share went from 16% to 54% at launch.
  3. A security review that can block merge.
  4. CI. The PR template asks how the change was tested and how to undo it; Claude can fill it in, but the requester signs off.
  5. Risk-tiered human approval.
  6. A merge queue, feature flags, release to Anthropic employees first, then the latest channel, with the stable channel trailing.
  7. Fast detection and rollback: flags turn off without a deploy, plus a weekly on-call rotation.
- **Convergence problem.** An agent author and an agent reviewer can loop: one PR went through more than fifty rounds overnight, and about 59% of repeat findings were old code. Fixes adopted: a three-round cap, diff-only re-review, flagging bug classes rather than single lines, and no repeated findings.
- **Where humans stay:** deciding whether to build ("direction, taste and scope"); risky code (billing, auto-updater, CI workflows); architecture that sets patterns; reading the evidence; owning the outcome ("you land it, you own it").
- **Changing direction** happens in the channel thread: "someone in the channel asks why, points at an earlier decision, or suggests a simpler route", and the author closes or reshapes the PR. The advice is to raise a different direction early, not as a blocking comment on a finished PR.
- **Open gap they name:** no circuit breakers that tighten approval when revert or incident numbers move.
- **Limits:** one team's repos (Claude Code is separate from the monorepo); self-reported numbers; no false-positive rates published.

## Notable quotes
- "An agent's approval never counts as a person's, either."
- "We don't have a formal process for this." (on sharing codebase understanding)
