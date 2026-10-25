---
title: "Agent Skills: production-grade engineering skills for AI coding agents (interview-me, doubt-driven-development, constraint-driven-development, idea-refine)"
source_url: https://github.com/addyosmani/agent-skills
author: Addy Osmani
publisher: GitHub (addyosmani/agent-skills)
published: 2026-10-13
retrieved: 2026-10-25
type: other
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, human-thinking-skills, human-review-gates, evals-autonomy-trust, agent-led-intent-shaping]
relevance: high
---

## Relevance to the project
A popular (about 110k stars, created 2026-02-15) lifecycle skill pack by Google's Addy Osmani that spans the whole spectrum in one place and names the moves explicitly. interview-me is a Socratic intake with a confidence number and a stop condition; doubt-driven-development makes a fresh-context adversarial reviewer check "non-trivial" decisions, with a definition of non-trivial; constraint-driven-development turns the quality bar into a written CONSTRAINTS.md and watches diffs for a weakened bar. Its README states the thesis that judgement moves "out of your head and into checks" when agents write more than a human reads. Product-relevant: Define-phase skills (idea-refine, interview-me, spec) map to discovery and PRD work.

## Themes
- human-thinking-skills: interview-me: write a one-sentence hypothesis with a confidence number, then ask "one question at a time, each with a guess attached", until ~95% confidence; listen for "want vs. should want" and ask "If you didn't have to justify this to anyone, what would you actually want?" (Steps 1-3).
- human-review-gates: interview-me gate is "an explicit 'yes'"; "Whatever you think is best", "Sounds good" and "Sure, let's go" are listed as not-yes; restatement must include "Out of scope", which is "non-negotiable" (Steps 4-5).
- rules-vs-judgment-encoding: constraint-driven-development: "An agent writes more in an afternoon than you will read that week, so the judgement moves out of your head and into checks that run around the loop"; checks need "numbers you actually chose" (Overview).
- evals-autonomy-trust: `/build auto`: approve the plan once, then it runs autonomously; "It removes the human stepping between tasks, not the verification" (README).
- agent-led-intent-shaping: doubt-driven-development materialises "a fresh-context reviewer — biased to disprove, not approve" for decisions that cross a boundary, assert unverifiable properties, or are irreversible; explicitly not for mechanical work ("If you doubt every keystroke, you ship nothing").

## Key points
- Classification:
  - interview-me: control flow fixed steps, human answers; gate = explicit human yes; standard form = intent template (outcome, user, why now, success, constraint, out of scope); stance = ask.
  - doubt-driven-development: control flow fixed five-step cycle (claim, extract, doubt, reconcile, stop) with a copyable checklist; gate = model judgment by an isolated reviewer; stop after trivial findings, 3 cycles, or user override; stance = red-team.
  - constraint-driven-development: control flow interview then detect; gate = deterministic checks against recorded thresholds plus diff watching for new suppressions, skipped tests, thresholds edited down; standard form = CONSTRAINTS.md; stance = enforce.
  - idea-refine: divergent then convergent phases producing a one-pager with "Not Doing (and Why)" and assumptions to validate; includes "Common Rationalizations" and "Red Flags" sections (same device as Superpowers).
- "Loading constraints" sections: interview skills refuse to run in non-interactive contexts (CI, `/loop`); there they flag a blocker or apply a stated floor and note it. A clean rule for when Socratic skills must degrade.
- "Never ask what you can read": detect stack and existing linters before the first question.

## Notable quotes
- "the judgement moves out of your head and into checks that run around the loop" (constraint-driven-development)

## Could not verify
- No eval results in the files read, though the repo has an `evals` folder (not read).
