---
title: "How eight people hold the bar for 200+ builders"
source_url: https://ideas.fin.ai/p/how-eight-people-hold-the-bar-for
author: Clíona de Róiste (Senior Engineering Manager, Frontend Infrastructure, Fin / Intercom)
publisher: Fin Ideas (Intercom Substack, ideas.fin.ai)
published: 2026-07-09
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [legible-org-for-agents, compounding-context-repo, evals-autonomy-trust, non-engineer-builders]
relevance: high
---

## Relevance to the project
Shows how intent and quality standards are carried into the write-the-code row as tooling rather than documents: an eight-person frontend infrastructure team encodes conventions and "design taste" into a design-system knowledge layer (Surge Intelligence) reached through skills, so agents and non-specialist builders land on the right path by default. Gives before/after numbers for agent output with and without that context. Bears on how a harness should hold design and product standards between "shape" and "build".

## Themes
- legible-org-for-agents: conventions encoded "into the tooling so anyone building UI, human or Agent, ends up on the right path by default"; Surge Intelligence is a maintained knowledge base of patterns and design taste that agents reason over, with skills as the access point.
- compounding-context-repo: "the knowledge layer is the real asset, and it compounds".
- evals-autonomy-trust: with vs without Surge Intelligence: design-system components used 7% → 96%; code passing typecheck 0% → 74%; components in correct context 42% → 68%; about a quarter of pages still use wrong props. Evals exist for measurable things "but not yet a way to judge" design-guidance compliance.
- non-engineer-builders: designers prototype in code; engineers ship whole surfaces without a designer; about 450 engineers have shipped React code, most without prior React experience.

## Key points
- More than 90% of PRs written with an agent; "half are auto-approved by Agents" (frontend context; no rules given).
- A "react" skill enforces React standards; migration skills (Principal Engineer Pat O'Callaghan) generate migration plans and verify migrated features; skills auto-installed for everyone.
- React grew from 0% to about a third of the product (1.4M lines); React support load grew from 2 to up to 104 engineers a week.
- Open problems: taste-driven composition and product knowledge "still mostly live in people"; agents claim success on tasks they cannot complete.

## Could not verify
- How "200+ builders" is counted; CI/lint setup; auto-approval rules; eval sample sizes.
