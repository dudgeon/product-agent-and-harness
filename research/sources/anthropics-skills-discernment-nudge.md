---
title: "discernment-nudge SKILL.md"
source_url: https://github.com/anthropics/skills/blob/main/skills/discernment-nudge/SKILL.md
author: Anthropic
publisher: GitHub (anthropics/skills)
published: 2026-08-17
retrieved: 2026-10-25
type: other
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [human-thinking-skills, rules-vs-judgment-encoding, human-judgment-pm-jobs]
relevance: high
---

## Relevance to the project
A first-party skill whose only job is to make the human think: after a substantive answer the user may act on, append two or three specific follow-up questions that help them check facts, probe reasoning and notice missing context. It is the purest public example of the "up-level the human's judgment" job, and its design is instructive: tight trigger boundaries, a once-per-conversation limit, an exact output format, and a long list of cases where the nudge would be paternalistic. Directly reusable for PM agents drafting plans, estimates or recommendations.

## Themes
- human-thinking-skills: purpose is "to *model* three discernment habits from the AI Fluency framework, not to lecture about them": checking facts, questioning reasoning, noticing missing context (Why this exists).
- human-thinking-skills: each prompt must reference "something concrete from the answer you just gave — a number, a named step, an assumption"; "Generic prompts... defeat the purpose" (Writing the prompts).
- rules-vs-judgment-encoding: judgment-heavy trigger (what counts as "actable") but rigid output: exact lead-in line "A few things worth a second look:", two or three bullets, under ~120 characters each, nothing after (Output format).
- human-judgment-pm-jobs: skip when the user asked for a take ("takes are weighed, not fact-checked"), when they supplied the material, when they asked you to check theirs ("circular"), or asked for the quick version ("lands as paternalistic") (When not to).

## Key points
- Classification: control flow = a single conditional step after the answer; gate = model judgment on whether the answer is consequential; standard form = criteria with many worked boundary cases (Roth IRA definition vs "which one should I open?"); stance = ask (Socratic), deferential.
- "Silence is the right default"; at most once per conversation, because repeating "turns a light suggestion into nagging".
- Code the user will run is excluded ("running it is the verification") but architecture advice is not.
- Prompts are phrased as things the user could send back verbatim, so the nudge is also a next-action affordance.

## Notable quotes
- "Silence is the right default" (When not to)

## Could not verify
- No data on whether users act on the nudges. The AI Fluency framework it cites was not read.
