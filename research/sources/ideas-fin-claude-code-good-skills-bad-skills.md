---
title: "Claude Code: Good skills, bad skills"
source_url: https://ideas.fin.ai/p/claude-code-good-skills-bad-skills
author: Brian Scanlan (Fin / Intercom)
publisher: Fin Ideas (Intercom Substack, ideas.fin.ai)
published: 2026-07-15
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [skills-marketplace, one-job-per-agent, evals-autonomy-trust, org-learning-loop]
relevance: medium
---

## Relevance to the project
States how Intercom governs the skills that sit under its write-the-code and review rows: a private auto-updating marketplace run by "team-2x", 267 skills from 153 contributors (about 31% of R&D), and a public curated subset (github.com/intercom/2x-skills). Useful as a design pattern for a harness's skill layer. It names only engineering skills; no product-process (spec, research, planning) skills.

## Themes
- skills-marketplace: private, auto-updating plugin marketplace maintained by team-2x; the plugins repo became the most actively contributed-to project at Fin within three months (153 contributors, 267 skills).
- one-job-per-agent: good skills "do one thing well", use scripts for deterministic work and include guardrails; "Best-effort attempts by Agents that go off-script often result in bad outcomes."
- evals-autonomy-trust: good skills have evals "regularly used and maintained"; bad ones have nobody looking at output or are judged by non-experts.
- org-learning-loop: skills refreshed with new learnings by the skill itself or periodic analysis of session data.

## Key points
- Curated public set: skill-tools (skill-review against a 7-category rubric), security-tools (secure-github-actions, a 14-rule checklist loaded by a hook when a workflow file is edited), claude-code-tools (permissions-analyzer, tool-misses, cc-cost-analysis from OpenTelemetry), test-tools (fix-flaky-tests; green CI is the only verification), code-review-tools (thermo-nuclear-code-review: structural simplification review), pr-tools (create-pr with diff validation; attach-github-assets for screenshots and recordings).
- Users described: engineers ("hundreds"). PMs and designers not mentioned.

## Could not verify
- No numbers on skill quality or usage per skill; no product-process skills described.
