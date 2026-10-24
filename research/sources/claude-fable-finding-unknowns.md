---
title: "A field guide to Claude Fable 5: Finding your unknowns"
source_url: https://claude.com/resources/articles/a-field-guide-to-claude-fable-finding-your-unknowns
author: Thariq Shihipar (member of technical staff, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-07-06
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-led-intent-shaping, spec-becomes-prototype-and-evals, spec-edge-case-review, human-review-gates, intent-factory-before-discovery]
relevance: medium
---

## Relevance to the project
An Anthropic engineer argues that with Fable-generation models the bottleneck on quality is the human's ability to clarify their own "unknowns", and gives a concrete before/during/after routine in which the agent helps shape intent: blind-spot passes, brainstorm prototypes, one-question-at-a-time interviews, reference code, decision-first implementation plans, deviation logs, explainers and comprehension quizzes. This is direct practitioner evidence for agent-led intent shaping and for a review step built around understanding rather than diff-reading. It is one person's practice with example prompts, no metrics, and framed for coding (plus one video-editing story).

## Themes
- agent-led-intent-shaping: the agent is asked to surface "unknown unknowns" ("blind spot pass"), brainstorm wildly different directions, and interview the user "one question at a time", prioritising questions that would change the architecture ("Pre-implementation").
- spec-becomes-prototype-and-evals: unknown knowns are found by throwaway HTML prototypes with fake data before wiring anything ("Brainstorms and prototypes").
- spec-edge-case-review: implementation plan leads with the decisions most likely to change (data models, type interfaces, user-facing flows) and buries mechanical refactoring ("Implementation Plans").
- human-review-gates: the author merges only after passing a Claude-written quiz on the change; pitch/explainer artifacts package prototype, spec and notes for approvers ("Post implementation").
- intent-factory-before-discovery: four-quadrant framing (known knowns, known unknowns, unknown knowns, unknown unknowns) as the start of every task ("Knowing your unknowns").

## Key points
- **Map vs territory:** the prompt, skills and context are the map; the codebase and real constraints are the territory; the gaps are "unknowns" the agent must guess at. More work means more unknowns.
- **Two-sided failure:** too specific and Claude follows instructions when it should pivot; too vague and it falls back on generic best practice. The fix is telling Claude where you are in your thinking and your experience with the problem.
- **Pre-implementation patterns:** blind spot pass; brainstorms and prototypes (e.g. "4 wildly different design directions" as HTML); interviews; references (point at source code, even in another language, rather than screenshots); implementation plan for review.
- **Handoff to a fresh session:** after planning, start a new session and pass the artifacts (spec file, prototype) so the implementer gets clean context with the planning output.
- **During implementation:** a temporary `implementation-notes.md` where the agent logs deviations, choosing "the conservative option" when an edge case forces a change.
- **Post implementation:** package prototype, spec and implementation notes into one doc to drop in Slack for buy-in; an HTML report plus quiz that must be passed before merge.
- **Worked example:** the Fable launch video was edited end-to-end with Claude Code (transcription, ffmpeg cuts, a Remotion prototype, learning colour grading before asking for variations).
- **Limits:** single practitioner, coding-centric, no evidence on whether the routine improves outcomes; the "best agentic coders" comparison names internal staff only by first name. Relevance to PMs is by analogy: the same routine maps onto shaping a product intent before an agent executes it.

## Notable quotes
- "Claude Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns."
- "Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture." (example prompt)

## Could not verify
- The linked follow-up "the new rules of context engineering" was not read.
