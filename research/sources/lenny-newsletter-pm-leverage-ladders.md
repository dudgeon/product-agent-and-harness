---
title: "How top PMs increase their leverage with AI"
source_url: https://www.lennysnewsletter.com/p/how-top-pms-increase-their-leverage
author: Colin Matthews (guest author; Head of Education at Lenny's, AI course instructor), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2026-06-30
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [pm-job-stable-methods-change, evals-autonomy-trust, spec-becomes-prototype-and-evals, prototyping-agents-limits, pm-tool-connectivity, non-engineer-builders, work-structure-spectrum, human-review-gates, org-learning-loop]
relevance: high
---

## Relevance to the project
A mid-2026 practitioner framework for what "AI-native" PM work looks like: three ladders of leverage (personal, product, systems), each with three rungs that move from assistance, to delegation with review, to agents that complete multi-step work and check their own output. Its most useful contribution is the **systems ladder**: PM work run as loops where a subagent "judge" grades output against a PM-written rubric, then scheduled. That is a concrete answer to how a PM's judgment gets encoded so review moves from per-output edits to rubric design, and it bears on review-and-autonomy, pm-agent-evaluation, work-structure and sequencing. The author sells a course launched with this post, so treat it as an informed instructor's view, not measured evidence.

## Themes
- pm-job-stable-methods-change: "the PM job drifted toward coordinating and aligning people. That version of the role is fading" (intro, Lenny); executives now expect employees to "use AI to complete entire tasks", not just prototype (author intro).
- evals-autonomy-trust: systems ladder rung 2 is a rubric plus "judge agent"; the rubric is YAML with structural and binary-LLM checks and a rationale per check, derived from example changelogs (Linear, Vercel, Stripe); the main agent spawns one subagent per check and iterates until all pass ("The systems leverage ladder").
- human-review-gates: "You will always apply some level of review at the end"; the systems ladder aims to stop "re-edit[ing] every AI output", and expects "only two or three loops for most PM tasks" (ladder intro, systems ladder).
- spec-becomes-prototype-and-evals: product ladder rungs go web prototype (communication only, code has no value) → prototype on the real codebase → agent-authored PR an engineer reviews and merges ("The product leverage ladder").
- prototyping-agents-limits: web prototyping tools "have limited context on our real components, pages, and data models, so this prototype is removed from reality"; the fix is a UI-only repo with a mock data store built by an engineer (product ladder, rung 2).
- pm-tool-connectivity: personal ladder rung 3 depends on MCP connectors to Amplitude, Drive, Notion, Canva, PostHog, Pendo, Figma; "once you create this connection, you'll never have to touch it again" (pro tip).
- non-engineer-builders: PRs suit "copy changes, small UI/UX tweaks, and changes to views that use existing backend code"; "it does not make sense to spend time being a worse engineer than the rest of your team" (product ladder, rung 3).
- org-learning-loop: iterate a task until good, then "lock in the workflow by creating a skill" in the same chat (personal ladder, rung 3).
- work-structure-spectrum: "Not every task, workflow, or company demands that you move up to the highest rung"; the right rung depends on the work (ladder intro).

## Key points
- **Personal ladder:** (1) AI writes text you paste elsewhere (most PMs are here "or even lower"); (2) AI creates the artifact itself (slides, Excel model, small prototype); example prompt builds a self-host vs managed-agents cost model assuming 5M+ agent-instance-hours a year; (3) AI completes a whole to-do via connectors, e.g. Claude + PostHog retention analysis output as an HTML doc, with "Cite all your sources so I can validate".
- **Product ladder:** (1) Lovable/Replit/Magic Patterns prototypes for concept testing; (2) Claude Code or Codex prototypes on the real codebase, using a stripped repo with "all of the base UI elements, styles, routes, pages, and components" and a local mock data store so it runs with no backend; (3) agent ships a PR, engineer reviews and merges. Knowing "when you should write a doc, ship a prototype, or create a PR" is framed as the PM's technical judgment.
- **Systems ladder:** (1) subagents for parallel pulls (Linear, Intercom, PostHog) and as "fresh" graders not biased by the main context; (2) rubrics plus judge agent; a changelog example goes from two pages of technical language to a short, user-impact changelog, "The only difference between these results is the rubric"; (3) scheduled tasks via Claude Code / Codex automation, and the `/goal` command with a rubric for long-running work; cites a morning routine shared by Fiona Fung (head of engineering for Claude Code and Cowork).
- Forward look: managed agents from Anthropic and OpenAI, "dreaming" for agent memory review, `/goal` and routines; predicts the most meaningful PM work becomes systems leverage, and that marketers, GTM and ops will run "small always-on agents" too.
- Author context: has trained "over 30,000 PMs"; built bespoke programs for product and design ICs in healthcare, legal and streaming; sees two gaps: knowing what level of AI to reach for, and the technical skills to use the tools fully.

## Notable quotes
- "Instead of thinking in better prompts, build a better system that can begin to take on more ownership of tasks" (systems ladder).
- "Instead of checking unit tests for failures, you'll check if outputs pass your rubrics" (systems ladder).
- "I did not write this. Claude wrote this prompt for another instance of Claude" (systems ladder, on the per-check grader prompt).

## Could not verify
- Screenshots of prompts and outputs (the PRD prompt, the cost model, the PostHog result, before/after changelogs) were images not in the text; described from the surrounding prose only.
- The post launches the author's paid course; no data on how many PMs are on each rung beyond "most people are at this rung, or even lower".
- Stride is a fictional product used for demos; no first-party company practice is described.
