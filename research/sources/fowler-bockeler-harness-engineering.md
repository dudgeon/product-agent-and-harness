---
title: "Harness engineering for coding agent users"
source_url: https://martinfowler.com/articles/harness-engineering.html
author: Birgitta Böckeler (Thoughtworks)
publisher: martinfowler.com
published: 2026-04-02
retrieved: 2026-10-25
type: article
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, harness-over-model, human-review-gates, verification-capacity-gap]
relevance: high
---

## Relevance to the project
Böckeler gives a two-axis vocabulary for the rigidity question that holds up better than a single spectrum: controls are guides (feedforward, before the agent acts) or sensors (feedback, after), and each is computational (deterministic: tests, linters, type checks) or inferential (semantic: AI review, LLM-as-judge). Skills appear on both axes (conventions are inferential guides; review instructions are inferential sensors). She also says plainly which problems neither kind catches: misdiagnosis, unnecessary features and misunderstood instructions, which is where PM judgment sits.

## Themes
- rules-vs-judgment-encoding: control table: coding conventions in AGENTS.md or Skills = feedforward/inferential; code mods = feedforward/computational; structural tests in a hook = feedback/computational; review instructions in Skills = feedback/inferential; project bootstrap (skill plus script) = both.
- harness-over-model: feedback-only harnesses repeat mistakes; feedforward-only harnesses never verify their rules work.
- human-review-gates: humans run a "steering loop": when an issue recurs, improve the guides or sensors; agents lack accountability and organisational memory, so the harness should direct human input to where it matters.
- verification-capacity-gap: computational sensors reliably catch structural issues; LLM judgment partly covers semantic issues (redundant tests, over-engineering) but is costly and probabilistic; neither reliably catches misdiagnosed issues, unnecessary features or misunderstood instructions.

## Key points
- Timing: fast controls before integration; expensive ones (mutation testing, broad architecture review) after; drift and runtime sensors outside the change lifecycle.
- Linter messages written for LLM consumption are especially useful sensors.
- "Harnessability": typed languages, clear module boundaries and opinionated frameworks are "ambient affordances" that make computational controls possible; Ashby's Law argues for narrowing what agents can produce.
- Behaviour harnesses are an open problem; AI-generated tests are not yet good enough alone.
- Supersedes her February 2026 memo.

## Could not verify
- Read via WebFetch summary; exact wording beyond short phrases not checked.
