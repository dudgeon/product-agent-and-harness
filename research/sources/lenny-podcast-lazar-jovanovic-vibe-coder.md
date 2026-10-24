---
title: "The rise of the professional vibe coder (a new AI-era job) | Lazar Jovanovic (Professional Vibe Coder)"
source_url: https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code
author: Lenny Rachitsky (host), Lazar Jovanovic (professional vibe coder, Lovable)
publisher: Lenny's Podcast
published: 2026-02-08
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [docs-as-code-prd, agent-ready-intent, prototyping-agents-limits, pm-persona-role-expansion, non-engineer-builders, human-judgment-pm-jobs]
relevance: medium
---

## Relevance to the project
A concrete agent-ready intent stack from a non-engineer who ships production apps at Lovable. A day of planning yields four PRD files (master plan, implementation plan, design guidelines, user journeys), which compile into a tasks.md plus a rules file the agent reads before every prompt. After that his prompts reduce to "proceed with the next task". That supports "the bottleneck moved to intent" ("Coding is no longer the bottleneck—clarity is") and the spec as the handoff artifact. It bears on intent-shaping-and-spec and artifact-and-project-structure. He works for the vendor whose tool he uses.

## Themes
- docs-as-code-prd / agent-ready-intent: four PRDs are "sources of truth" feeding tasks.md; rules.md or agents.md (Lovable "project knowledge") tells the agent to read all PRDs first, take the next task, then report what it did and how to test it (31:34-34:36, 45:12-47:48).
- prototyping-agents-limits: start 4-5 parallel builds with increasing specificity (brain dump, then more specific, then visual references, then code templates) to find clarity, then write the PRDs from the winner (27:21-31:34). In regulated settings ("healthcare or finance ... something regulatory") teams prototype but can't push to production (51:48, 53:23).
- pm-persona-role-expansion: engineer, designer and PM "Venn diagrams ... are converging" (0:25, 1:04:54); "we're all becoming product managers on steroids" (47:48).
- human-judgment-pm-jobs: PMs are "not compensated for writing good PRDs ... for good judgment. Somebody else can do the writing" (47:48). Taste, fonts and emotional design stay human (19:38, 58:34).
- non-engineer-builders: before Lovable he built a prototype in 4 hours that engineers took 6-7 months to productionise; describing it in words would have taken "a week or two" (51:48).

## Key points
- Time split: 80% planning and chat mode, 20% building (show-notes takeaway). Context windows are a "genie with three wishes" budget, so he gives the agent "perpetual context" via files (30:02).
- Rules files as a learning loop: after each fix, ask the agent how to prompt it better next time and add the answer to rules.md (1:11:44).
- Four-step unblock: let the tool fix it, add console logs, bring in another tool (Codex), revert and re-prompt (1:05:37).
- Obsolescence: his March 2025 course became "completely obsolete" as Lovable absorbed the workarounds natively, a direct example of scaffolding being eaten (1:19:33).
- Elite engineering is still needed for maintenance, scaling and infrastructure (1:01:05).

## Notable quotes
- "My prompts have become, 'Proceed with the next task.'" (34:36)
- "We won't be rewarded in the world of AI for faster raw output; we will be rewarded for better judgment." (19:38)

## Could not verify
- Transcript read 5:47-9:00, 18:08-19:38, 27:21-55:25, 1:00:56-1:01:05 and 1:19:33-1:22:34; the rest was skimmed by search. "At least half of S&P 500" companies having Lovable users is a vendor-employee claim (53:23). There's no evidence that the four-PRD approach beats alternatives.
