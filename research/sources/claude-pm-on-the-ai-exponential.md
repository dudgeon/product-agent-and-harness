---
title: Product management on the AI exponential
source_url: https://claude.com/resources/articles/product-management-on-the-ai-exponential
author: Cat Wu (Head of Product, Claude Code, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-03-19
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [pm-job-stable-methods-change, spec-becomes-prototype-and-evals, pm-persona-role-expansion, harness-over-model, human-judgment-pm-jobs]
relevance: high
---

## Relevance to the project
First-hand account from the Head of Product for Claude Code of how PM work changes when models improve mid-project: short side-quest sprints instead of locked roadmaps, demos and evals instead of docs, re-testing shipped features on each new model, and "do the simple thing" so scaffolding can be deleted. It also gives one PM's tool split (chat for thinking, Claude Code for prototypes and evals, Cowork for everything else), a direct data point for the agent-interface and target-user dimensions. It is one practitioner at a model vendor building a developer tool; the practices are claimed to work there, with no outcome metrics.

## Themes
- pm-job-stable-methods-change: the traditional playbook assumes what's possible at project start holds at the end; exponential model gains break that, so the PM's job becomes creating clarity in ambiguity and identifying "the handful of true non-negotiables" ("Leaning into the AI exponential", "Looking forward").
- spec-becomes-prototype-and-evals: team replaced documentation-first with prototype-first; stand-ups replaced by demos; pro-tip to send a written spec to Claude Code and see if it builds it; Noah's plugins spec produced a near-production prototype that anchored the shipped UX; Conner hand-crafted evals for agent teams ("Encourage demos and evals over docs").
- pm-persona-role-expansion: roles blend: designers ship code, engineers make product decisions, PMs build prototypes and evals.
- harness-over-model: todo-list reminder hack removed when the next model did it unprompted; system prompt and tool descriptions trimmed with each model, including a 20% reduction for Opus 4.6 ("Do the simple thing").
- human-judgment-pm-jobs: PM's residual job is strategy clarity, pushing ambition, and choosing non-negotiables; letting go of control is "the first thing AI product management asks you to unlearn".

## Key points
- Personal tool split ("Designing a new product management workflow"): Claude.ai as thought partner without action; Claude Code when the output is code (prototypes, evals, scripts calling the API); Cowork for everything else (inbox, todo tracking, decks, searching Slack for decision history, travel).
- Before PM-ing Claude Code, the author built Streamlit apps for large-scale user-feedback analysis and evals entirely by prompting Claude Code (hundreds of hours, no hand-written code).
- Four shifts: plan in short sprints with "side quests" (Claude Code on Desktop, AskUserQuestion and todo lists reportedly came from side quests); demos and evals over docs; revisit features with each new model (Claude Code with Chrome came from noticing users manually bridging two tools); do the simple thing.
- Prototype for capability first: "Use more tokens than you think you need"; cut cost later as cheaper models catch up. Relevant to cost-control-routing as a counterweight.
- Cites METR: Opus 4.6 completes about half the time software tasks taking humans almost 12 hours vs about 21 minutes for Sonnet 3.5 (new), "roughly 41x in 16 months" (Anthropic's summary of METR).
- External PM quotes: Bihan Jiang (Director of Product, Decagon) starts in Cowork pulling context from Slack, codebase and docs, then moves to Claude Code for a demo in a couple of hours; Kai Xin Tai (Senior PM, Datadog) describes offline evals on real production incidents for Bits AI SRE.
- Claims data science, finance, marketing, legal and design teams at Anthropic adopted the tools on their own.
- Limits: developer-tool product at an AI lab, where users are the builders; no regulated-environment discussion; nothing on how prototype-first decisions are recorded or reviewed.

## Notable quotes
- "after you write a spec, send it to Claude Code and see if it can build it." ("Encourage demos and evals over docs")
- "Every model release is an implicit prompt to revisit what you've already built." ("Revisit features with new models")
