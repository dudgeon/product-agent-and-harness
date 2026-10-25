---
title: "Superpowers: How I'm using coding agents in October 2025"
source_url: https://blog.fsck.com/2025/10/09/superpowers/
author: Jesse Vincent
publisher: Massively Parallel Procrastination (blog.fsck.com)
published: 2025-10-09
retrieved: 2026-10-25
type: article
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, evals-autonomy-trust, org-learning-loop]
relevance: high
---

## Relevance to the project
The author of Superpowers explains how his rigid skills are made and tested: Claude writes most skills; Claude extracts skills from books and from ~2,249 past-conversation memory files; skills are pressure-tested by subagents under realistic time-pressure and sunk-cost scenarios; and persuasion principles (Cialdini's authority, commitment, etc.) are deliberately used to make the agent comply. It is the best practitioner account of why someone would choose enforcement language over explanation, and of a test method (adversarial scenarios) for rule skills.

## Themes
- rules-vs-judgment-encoding: persuasion principles from Cialdini's Influence applied to skills; he reports Dan Shapiro's study with Cialdini showing the principles affect LLMs; skills already used "authority framing and commitment prompts" to make the agent more disciplined.
- evals-autonomy-trust: first tests were quiz-style and gave perfect scores with little insight; replaced by pressure scenarios ("Every minute costs $5k"; a finished solution not yet checked against a skill); each failure strengthened the bootstrap skill.
- org-learning-loop: skills mined from source material: a programming book, and memory files from past conversations clustered by topic; before writing a new skill Claude checks whether it is needed (only one or two proposals actually required changes).

## Key points
- Bootstrap rule: "If you have a skill to do something, you _must_ use it to do that activity."
- Flow: brainstorm with the user before implementing, git worktree per task, then either a second session acting as a PM or subagent dispatch with code review after each task, red/green TDD throughout, then PR/merge/stop choice.
- The design choice (my reading): where judgment would let the model skip a costly discipline, the author encodes the discipline as non-negotiable and tests it under pressure rather than explaining it.

## Could not verify
- The Cialdini/Shapiro paper itself was not read (likely Meincke et al. 2025, "Call Me A Jerk"); its effect sizes are not reported here.
