---
title: "Prompting best practices (Use examples effectively)"
source_url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
author: Anthropic
publisher: Claude Developer Platform docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [standard-form-spectrum]
relevance: medium
---

## Relevance to the project
Anthropic's current guidance on exemplars as an encoding: examples are called "one of the most reliable ways to steer Claude's output format, tone, and structure", with three qualities (relevant, diverse, structured in example tags) and a recommended count of three to five. It also notes that worked examples shape the model's reasoning when thinking is on, and that Claude can be asked to critique or extend the example set. For dimension 3 this is the vendor's position that the exemplar rung is the main lever for tone and structure, which rules and rubrics carry poorly.

## Themes
- standard-form-spectrum: "A few well-crafted examples ... improve accuracy and consistency"; make them relevant (mirror the use case), diverse (cover edge cases so the model does not pick up unintended patterns) and structured in `<example>` tags; "Include 3-5 examples for best results" (Use examples effectively).
- standard-form-spectrum: "Worked examples in your prompt shape how Claude approaches similar problems in its own thinking blocks"; present each as problem, method, expected answer (thinking section).

## Key points
- The page is the consolidated prompting reference for current models (the older multishot-prompting page redirects here).
- Also recommends asking Claude to evaluate the examples for relevance and diversity or to generate more from an initial set.
- Self-check instruction ("verify your answer against [test criteria]") is recommended for most models but said to cause over-verification on Claude Opus 5, a reminder that encoded checks are model-version-sensitive.
