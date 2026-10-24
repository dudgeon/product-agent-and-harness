---
title: "How I turned Claude into a self-improving PM assistant | Daniel Blum (PM, Melio)"
source_url: https://www.lennysnewsletter.com/p/how-i-turned-claude-into-a-self-improving
author: Claire Vo (host), Daniel Blum (PM, Melio)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-08-31
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [meta-harness, memory-architecture, org-learning-loop, enablement-by-product, skills-marketplace, status-update-agents, org-context-grounding, pm-tool-connectivity]
relevance: high
---

## Relevance to the project
The closest public example of a working PM-side harness built by an individual PM in a real company: a Claude/Cowork plugin that runs weekly prep, a morning brief, open-loop tracking and a weekly self-improvement loop, which Blum says now carries 70-80% of his workday, and which he packaged as a "Workstation" onboarding plugin for every Melio employee (about 15 minutes to set up). It bears on harness-layering (a personal meta-harness on top of Cowork), context-and-memory (a CLAUDE.md "routing brain" plus topic memory files kept on the machine), capability-distribution-trust and adoption-model (distributing one person's setup as a plugin). Evidence is one PM's own account; no transcript was available, so this note works from the show notes and the public repo.

## Themes
- meta-harness: a personal PM layer on top of Cowork/Claude Code with four workflows that "build on each other" (weekly prep, morning brief, open loops, self-improvement) (repo README; show notes 09:00-11:00, 26:30).
- memory-architecture: setup writes a CLAUDE.md "routing brain" that loads memory by topic from a memory/ folder (role, people, priorities, decisions, voice); memory "stays on your machine" (repo README). Morning brief flags unknown internal terms and saves them to context (show notes 15:00).
- org-learning-loop / skills-marketplace: a self-improvement loop "watches Daniel's edits, spots recurring friction, and suggests new skills to build"; an "Improve" skill judges outside AI tips against the current setup before adopting them (show notes 26:30, 31:00).
- enablement-by-product: the "Workstation" plugin gets any Melio employee a personalised Claude setup in about 15 minutes; a "UX lesson learned the hard way" from distributing an earlier version (show notes 25:00, 32:00).
- status-update-agents: weekly prep fills a Notion board from scratch every Sunday; Notion is now "read-only" for him (show notes 06:00-09:00).
- pm-tool-connectivity: Chrome connector vs MCPs for tools without integrations (show notes 19:00).
- org-context-grounding: context fed by voice memos, links and recurring updates (show notes 07:30).

## Key points
- Stack: Claude and Cowork at Melio (a B2B payments company), Notion, Slack and email (show notes 03:30).
- "Two rules that make any AI system powerful aren't about the tool you pick" (05:00); the rules themselves are not in the show notes.
- ROI: the early weeks feel slow and you push through (20:00). The remaining 20% that Claude can't yet do is discussed at 38:00 (gap not named in the notes).
- Public repo IamBlum/pm-copilot (MIT): a plugin marketplace with 9 skills (morning-brief, weekly-prep, open-loops, self-improvement, memory-keeper, sync, consolidate, improve, get-started) and 3 commands (setup, first-run, improve). It asks before acting. Workflows are run manually because scheduled tasks ran in the cloud and couldn't reach local memory, so scheduling is "not available yet" (README, retrieved 2026-10-24).
- The local-memory vs cloud-schedule conflict is a concrete instance of the runtime-location trade-off: a personal harness whose memory lives on the laptop can't be driven by cloud routines.

## Notable quotes
- "A co-pilot for Claude that learns how you work and runs your weekly PM overhead." (repo README)

## Could not verify
- No transcript file was available. This note uses only the episode show notes (chapter titles and "What you'll learn") and the public GitHub README. The demo content, the "two rules", the Workstation UX lesson and the remaining-20% gap are unread.
- 70-80% of the workday and the 15-minute onboarding are the guest's own claims; there's no adoption number for Workstation across Melio.
- The repo README doesn't mention the Notion board or the Workstation plugin; those come only from the show notes.
