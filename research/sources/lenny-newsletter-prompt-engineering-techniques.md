---
title: "Five proven prompt engineering techniques (and a few more-advanced tactics)"
source_url: https://www.lennysnewsletter.com/p/five-proven-prompt-engineering-techniques
author: Mike Taylor (guest author; prompt engineer, Brightpool), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2024-10-29
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [synthetic-users-limits, evals-autonomy-trust, org-context-grounding]
relevance: low
---

## Relevance to the project
A 2024 guest post giving PMs prompt templates: role-playing, style unbundling, emotion prompting, few-shot examples, synthetic bootstrap, plus chain-of-thought, retrieval and LLM-as-a-judge. It is general rather than about agents or harnesses, and dated. It matters only as a baseline for how intent was expressed to AI before agents, and because two tactics recur in the project: generating synthetic personas and feedback (a pattern the library treats with caution) and LLM-as-a-judge as cheap evaluation.

## Themes
- synthetic-users-limits: "Synthetic bootstrap" example generates ten user personas and then "potential customer feedback" from them when "you lack real user data" (Tactic 5); presented without caveats about validity.
- evals-autonomy-trust: LLM-as-a-judge rates outputs on a 1-5 rubric, with the caveat that its judgments "may not always align perfectly with human assessments" (Tactic 8).
- org-context-grounding: retrieval (put relevant documents in the prompt) for niche or current information (Tactic 7).

## Key points
- Taylor separates planning as its own step "so I can vet the plan before I decide how to proceed" (Tactic 6), a precursor of plan-then-execute agent workflows.
- Advanced tactics are framed as building "a system that corrects for the errors AI models commonly make" (Bonus section intro).

## Could not verify
- Full post read. Linked papers were not checked. Templates are illustrated with shared ChatGPT conversations, not measured comparisons.
