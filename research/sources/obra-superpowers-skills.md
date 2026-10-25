---
title: "Superpowers skills: using-superpowers, brainstorming, test-driven-development"
source_url: https://github.com/obra/superpowers/tree/main/skills
author: Jesse Vincent
publisher: GitHub (obra/superpowers)
published: 2026-10-21
retrieved: 2026-10-25
type: other
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, human-thinking-skills, human-review-gates, agent-led-intent-shaping]
relevance: high
---

## Relevance to the project
Superpowers is the most widely adopted independent skill pack (about 305k GitHub stars per the API on retrieval) and it sits at the opposite pole from Anthropic's "explain the why, avoid MUSTs" advice: mandatory invocation, an "iron law", rationalisation tables and red-flag lists designed so the agent cannot argue itself out of the process. Its brainstorming skill is also a Socratic, one-question-at-a-time intake with a hard gate before building. It shows that practitioners make process skills rigid exactly where the model is tempted to skip them. Evidence label anecdote: a practitioner's own design, no published evals.

## Themes
- rules-vs-judgment-encoding: using-superpowers: "If you think there is even a 1% chance a skill might apply... you ABSOLUTELY MUST invoke the skill", with a table of rationalisations and rebuttals ("This is just a simple question", "The skill is overkill").
- rules-vs-judgment-encoding: test-driven-development: "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"; code written before its test must be deleted; "Violating the letter of the rules is violating the spirit of the rules"; exceptions only with the human partner's permission.
- human-thinking-skills: brainstorming: investigate first, then "one question at a time", in the person's vocabulary, explaining why it matters; play back understanding in 200-300 word chunks; state defaults as your own decisions.
- human-review-gates: brainstorming hard gate: nothing is built (code, scaffolding, dependencies) until the design doc is approved; a vague "sounds good" is not approval of an unwritten doc; for larger work a fresh subagent reviews the doc "as a builder would" first.
- agent-led-intent-shaping: present two or three real approaches with trade-offs, recommend one, let the person choose; warns against "menus that steer answers".

## Key points
- Classification:
  - using-superpowers: control flow fixed (skill check before any response); gate none but social-pressure framing; stance enforce. Process skills take priority over implementation skills; user instructions override skills.
  - brainstorming: control flow fixed stages, content human-chosen; gates human approval + subagent review; standard form = design-doc outline sized to the change; stance ask. Includes a size escape: if the request is clear and small, just do it and say what you did.
  - test-driven-development: control flow fixed red-green-refactor; gate = test run (full suite, failures reported by name); stance enforce.
- Rigidity is targeted at the steps the model is most likely to rationalise away (testing first, checking for a skill, getting approval), not at content.
- Escape hatches are explicit and owned by the human (throwaway spike the person agreed to; user opted out).

## Could not verify
- Read via WebFetch summaries of raw files (verbatim limits applied); exact wording beyond short quotes not checked. No usage or quality data.
