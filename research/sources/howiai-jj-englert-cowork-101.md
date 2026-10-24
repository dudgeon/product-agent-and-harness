---
title: "Claude Cowork 101: How to automate your workday without touching code | JJ Englert (Tenex)"
source_url: https://www.lennysnewsletter.com/p/claude-cowork-101-how-to-automate
author: Claire Vo (host), JJ Englert (community enablement, Tenex)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-04-13
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [product-artifact-primitives, project-taxonomy, human-review-gates, evals-autonomy-trust, synthetic-users-limits, prd-agents, memory-architecture, enablement-by-product]
relevance: medium
---

## Relevance to the project
A walk-through of how a non-engineer assembles a personal harness in Claude Cowork: a project is a folder plus shared memory across chats, a "brain" preferences file and a "workspace map" route context, connectors carry per-tool permissions (draft-only, ask-first), skills package repeatable work, scheduled tasks run inside a project's context, and a "sub-advisory" skill spins up persona sub-agents to review a draft. That is a small-scale version of several pieces of a PM meta-harness (persona sub-agents, project containers, progressive trust). Bears on artifact-and-project-structure, context-and-memory, review-and-autonomy and trust-privacy-defaults. The guest's company runs workshops for Anthropic (42:29), so this is partly enablement content for the vendor's product.

## Themes
- product-artifact-primitives / project-taxonomy: "a project is a folder on your computer" (6:20); a Cowork project chains tasks with "shared memory" across chats, project instructions, and a context panel listing folder files and generated memory (15:35-17:43). Claire Vo: "a skill is literally like a file"; "a project is just literally a folder with files in it" (9:23).
- memory-architecture: a "brain" markdown file of working preferences and teammates is read at the start of work (7:52); a generated "workspace map" lets Claude go to the right sub-folder and skill instead of ingesting everything, saving tokens (10:44).
- human-review-gates: connector permissions can be set per action to allowed, blocked, or "always ask me for permission" (18:47); project instruction "never send emails on my behalf. Only write them as drafts" (22:35). Vo notes non-technical users still meet raw bash approval prompts (25:07).
- evals-autonomy-trust: "progressive trust": drafts first, then reading email, then calendar and Slack, eventually an independent agent; framed as trading information for productivity (Vo, 41:01).
- synthetic-users-limits / prd-agents: the "sub-advisory board" skill launches three persona sub-agents with fresh context windows (e.g. ICP segments, a security-worried reader) to critique a draft (30:04); Vo suggests PMs run "every PRD review" past simulated boss, engineering partner and customer (31:55); Englert suggests researching your real boss to simulate their feedback (33:33). No evidence offered on how well simulated reviewers match real ones.
- enablement-by-product: Cowork's built-in idea list for "what can I do" and a skill test interface are credited with getting non-technical users started (44:09, 35:03).

## Key points
- **Positioning (5:11):** desktop app has three modes (chat, Cowork, Code); Cowork "is literally doing it for you" with access to files, browser and connected apps. Mobile Cowork works less well than mobile Claude Code (6:20).
- **Onboarding pattern (12:31-14:03):** create an empty folder, describe the system you want, and Claude asks clarifying questions before building skills; Englert always adds "ask me any questions if you're unclear" (28:59).
- **Ingest path through connectors (20:20, 27:28):** analyse 30 days of sent mail (46 emails) to produce an email style guide and voice profile saved to memory, then a writing skill. Vo calls this burning down an "anti-to-do list".
- **Orchestrator view (24:27):** project screen lists running agents and which need attention, so non-developers "orchestrate" several agents.
- **Long multi-step skill (33:33-35:03):** a ~10-step newsletter skill interviews him, runs a research sub-agent, uses sub-skills per section, then an evaluation step (checklists plus the advisory board) and feeds back past performance with good and bad examples: "if you don't tell AI what success is ... AI doesn't know".
- **Scheduled tasks (36:36-40:08):** a 7:30 a.m. "morning debrief" reads email, Slack and calendar inside the project, so it inherits skills and connectors; he suggests a daily per-project plan posted to Slack for project managers.
- **Cowork vs OpenClaw (26:19):** he uses Cowork for business tools and OpenClaw as a personal assistant with limited, separate accounts.

## Notable quotes
- "With co-work, you're not starting over from the start" (7:52).
- "You can define three individual personas with like a fresh context window, meaning like fresh perspective" (30:04).

## Could not verify
- Transcript read 0:00-46:25 in full; lightning round skimmed. Auto-transcription renders "Cowork" variously and "10x" for Tenex.
- Quality claims ("the results have been really good") are the guest's own; no measures. Product behaviour shown is as of April 2026 and Cowork has changed since.
