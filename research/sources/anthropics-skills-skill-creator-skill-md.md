---
title: "skill-creator SKILL.md"
source_url: https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
author: Anthropic
publisher: GitHub (anthropics/skills)
published: 2026-04-20
retrieved: 2026-10-25
type: other
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, evals-autonomy-trust, skill-standards]
relevance: high
---

## Relevance to the project
The skill file Anthropic ships for writing skills, read in full (485 lines plus grader, comparator and analyzer agent files and Python scripts). It carries the strongest first-party statement against rule-heavy skills: all-caps ALWAYS/NEVER and "super rigid structures" are "a yellow flag"; explain the why instead. It also shows the mixed design in practice: loose prose for the conversation with the user, rigid scripts and exact JSON field names for the eval machinery. The blog post about it is noted separately (claude-skill-creator-evals).

## Themes
- rules-vs-judgment-encoding: "Try to explain to the model why things are important in lieu of heavy-handed musty MUSTs"; "If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag" (sections "Writing Style", "How to think about improvements").
- rules-vs-judgment-encoding: against overfitting to a few test cases: rather than "fiddly overfitty changes, or oppressively constrictive MUSTs", try "different metaphors" or "different patterns of working" (section "How to think about improvements").
- evals-autonomy-trust: every iteration runs with-skill and baseline (no skill) in parallel, grades against assertions, and puts outputs in a viewer for a human before the model revises; "for assertions that can be checked programmatically, write and run a script rather than eyeballing it" (sections "Running and evaluating test cases", step 4).
- skill-standards: the file itself uses rigidity where machines read the output: "ALWAYS use this exact template" for reports, required field names in grading.json "the viewer depends on these exact field names".

## Key points
- Classification: control flow = a suggested sequence (capture intent, interview, write, test, iterate, optimise description) with explicit permission to drop it ("if the user is like 'I don't need to run a bunch of evaluations, just vibe with me', you can do that"); gates = scripts (quick_validate, run_eval, aggregate_benchmark) plus human review in the viewer; standard form = assertions per test case plus blind comparison by an independent agent; stance = interview the user, then do.
- The file breaks its own rule once and says so: "Sorry in advance but I'm gonna go all caps here: GENERATE THE EVAL VIEWER *BEFORE* evaluating inputs yourself" (Cowork section). Shows where the author judged a rule worth the cost: getting outputs in front of the human.
- Description advice: make descriptions "a little bit 'pushy'" because Claude tends to "undertrigger".
- Calibrates jargon to the user ("JSON", "assertion" only when the user shows they know the terms): the skill adjusts to a non-engineer author.
- Principle of lack of surprise: a skill's contents should not surprise the user given its description.

## Notable quotes
- "Today's LLMs are *smart*. They have good theory of mind" (Explain the why)

## Could not verify
- Whether the no-MUSTs style measurably beats rule-heavy style; the file gives no data.
