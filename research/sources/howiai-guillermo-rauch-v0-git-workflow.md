---
title: "Guillermo Rauch: Vercel CEO on how v0 hit 3,200 PRs merged per day (and lets anyone ship)"
source_url: https://www.lennysnewsletter.com/p/anyone-can-cook-how-v0-is-bringing
author: Claire Vo (host), Guillermo Rauch (CEO, Vercel)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-02-04
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [non-engineer-builders, prototyping-agents-limits, human-review-gates, skills-marketplace, skill-supply-chain-security, metrics-review-agents, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
Vercel's CEO demos v0 turning a non-engineer's prompt into a branch, a production-like preview and a pull request, so a prototype becomes a reviewable change instead of a "petition" to engineering. It bears on the hand-off edge of a PM harness (prototype or change as the artifact that goes to engineering review), on non-engineer-builders, and on capability-distribution-trust through skills.sh (a public skills hub with ratings added because quality and injection risk are concerns). It is a live event with a vendor selling its own product; the headline 3,200 PRs/day figure comes from an internal agent's answer on stage.

## Themes
- non-engineer-builders: marketers used to "petition the government" (ask engineers) or hope the CMS was wired up; now they open the page in v0 and prompt, but "it would be somewhat irresponsible to just ship it", so they open a PR with a preview (18:48-20:22).
- prototyping-agents-limits: "really easy to go from zero to one ... harder is to iterate on a project at scale and to deploy changes safely" (4:51); before PR handoff, his own prototypes were "playing in La La Land" (18:48).
- human-review-gates: v0 now follows the branch, preview, code review, merge workflow; the PR description is generated; the preview runs on production-grade infrastructure (13:22-15:00). Rauch wants skills to bring feature flags, experiments and event tracking rigor into vibe-coded changes (21:03).
- skills-marketplace: skills.sh is "like NPM ... an open ecosystem of skills" (1:35); the show notes say 34,000+ community skills and 500 new submissions per hour; skills.sh itself began as four or five v0 prompts before the VP of design, CTO and product lead refined it (36:38).
- skill-supply-chain-security: the demoed feature is a five-star rating so users can tell whether a skill is "high quality, vetted, verified" (9:08); Vo notes skills "can be a prompt injection vector" (10:26).
- metrics-review-agents: Vercel's internal data agent D0 answered the PR-growth question on stage; it runs in a sandbox, writes and runs Python, queries Snowflake and searches the web, "a four or five minute process" (15:40, 37:08).
- vendor-claims-vs-independent-evidence: "3,200 PRs merged per day by January 28" from near zero in early January, read out from D0's answer, during an early preview (16:47). Not clear whether that is internal Vercel use or all v0 users.

## Key points
- **Demo (6:21-15:00):** pick a GitHub repo, v0 creates a branch named contributor/feature, boots a VM sandbox with dependencies and a VS Code editor beside a live preview; a three-sentence prompt adds skill ratings with persistence; Rauch fixes a layout shift; v0 opens a PR and the Vercel bot deploys a preview.
- **Product discovery model (35:04):** "customer zero" is Vercel itself (its own taste), "customer one" is close design partners (enterprises, community members, Claire Vo texting bug reports).
- **Durable workflows (38:16):** Vercel's workflow engine retries through provider outages and timeouts; Rauch's example of a background agent is "at v0 ... go and spec out this PRD for me" from Slack; Vo says her own PRD agent runs on such workflows.
- **Escape hatch when stuck (32:02):** clone the repo locally or bring in a collaborator; ask another model to explain, paste the answer back; ask v0 to build debug tools.
- **Agents' power comes from a computer (37:08):** "what's actually making agents really capable is not that they're perfect, is that they have a computer at their disposal".

## Notable quotes
- "Until I had this mechanism, to hand it off as a pull request to the engineering team, then I was kind of like playing in La La Land" (18:48).
- "It would be somewhat irresponsible to just ship it" (20:22).

## Could not verify
- Transcript read 0:00-22:00 and 32:00-43:00 in full; the 22:00-32:00 lightning round and chess demo skimmed by search. Auto-transcription renders v0 as "VZero"/"Vizier".
- 3,200 PRs/day and 500 skills/hour are vendor figures with no method; the population (internal vs all users) is not stated. Recorded at a live event in late January 2026.
- Related library note: [vercel-skills-sh-open-skills-ecosystem](vercel-skills-sh-open-skills-ecosystem.md).
