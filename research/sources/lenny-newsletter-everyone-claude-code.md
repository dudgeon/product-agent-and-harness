---
title: "Everyone should be using Claude Code more"
source_url: https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code
author: Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2025-10-14
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [non-engineer-builders, research-synthesis-agents, prd-agents, pm-tool-connectivity, docs-as-code-prd, pm-ai-usage-surveys, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Lenny reframes Claude Code as "Claude Local or Claude Agent" for non-technical people and curates 50 reader use cases from over 500 submissions. For us it is a crowd-sourced catalogue of what product people actually point a local agent at: customer-call synthesis against a running assumption tally, Linear/Jira ticket creation from call transcripts, PRDs reverse-built from code and conversation, changelogs from commits, roadmapping from repo context. It is also, by a later account, the list a PM at Anthropic used as a pre-launch eval for Cowork (48 of 50 passed; see [Cherny](lenny-podcast-boris-cherny-after-coding.md)), which makes it a de facto benchmark for the "general work harness for product people" job set. Anecdotes, self-selected, no outcomes measured.

## Themes
- non-engineer-builders: "forget that it's called Claude Code and instead think of it as Claude Local or Claude Agent" (intro); install via terminal, with Warp suggested to get past setup errors (setup section).
- research-synthesis-agents: a PM synthesises customer-call transcripts "to compile evidence that supports or invalidates a running tally of assumptions/requirements/hypotheses", with Fireflies, Linear and Notion via MCP, making it "my hub for ongoing product research" (#11). A founder asks it to find every time he "subtly avoided conflict" across meeting recordings (#4).
- prd-agents / docs-as-code-prd: a PM "reverse-build[s] documentation and requirements" from code and pasted conversations into a PRD "for better internal discoverability, decision logging, and source listing" (misc list); a `{project}-product` repo whose CLAUDE.md points at engineering repos for architectural review, with verbose commit messages as future decision context (#20). Linked advanced guides include turning discovery notes into PRDs "optimized for coding agents".
- pm-tool-connectivity: call transcript to Jira tickets via MCP; Intercom tickets to Asana bug reports; custom commands for refining Linear issues; a daily "Claude CEO" report across Gmail, Brex, Mercury and Linear (misc list).
- evals-autonomy-trust: a slide-builder notes "hallucinations happen, that has to be accepted going in" (#18); changelog drafts "usually need few quick edits", hours down to 10-15 minutes (#17).
- pm-ai-usage-surveys: 500+ submissions on X and LinkedIn; a self-selected sample of enthusiasts, not a survey.

## Key points
- Lenny's own uses are utility tasks (disk space, image upscaling, downloads, raffle pick); the PM-relevant uses come from readers.
- "Self-driving documentation": Claude Code with Playwright explores the product, finds documentation gaps and writes the changes (#14).
- A new CPO uses Claude Code on the codebase to learn "what our code can/can't do before asking" the dev team (misc list): the agent as a way to reduce dependence on engineers for answers.
- A hiring collateral pack (JD, hiring plan, interview plan, rubric) generated in plan mode from a folder of internal Notion pages and peer JDs (#10).
- Footnote corrects the "local" framing: the model runs in the cloud; commands and file access are local.

## Could not verify
- Post read in full. All 50 items are self-reported anecdotes; time savings are the contributors' own.
- The Cowork-eval link comes from the Cherny episode (2026-02-19), not from this post.
