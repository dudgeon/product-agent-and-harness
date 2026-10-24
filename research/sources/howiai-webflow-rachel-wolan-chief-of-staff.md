---
title: "How Webflow's CPO built an AI chief of staff to manage her calendar, prep for meetings, and drive AI adoption | Rachel Wolan"
source_url: https://www.lennysnewsletter.com/p/how-webflows-cpo-built-an-ai-chief
author: Claire Vo (host), Rachel Wolan (CPO, Webflow)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-12-29
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [memory-architecture, identity-delegation, human-review-gates, status-update-agents, leadership-permission-mandate, enablement-by-product, outcome-measurement-gap, org-context-grounding]
relevance: medium
---

## Relevance to the project
A CPO's personal harness for leadership work (calendar audit, meeting and dinner prep, email triage) built in Claude Code with Markdown files as the store, plus a first-party account of how she drove adoption across Webflow's product org with "builder days". Two things matter for the register: her scoped, hand-tuned permissions per tool (calendar read-only; Gmail can read, archive, label and draft but not send) as an n-of-one model of delegation guardrails; and the adoption pattern (top-down mandate, "you can't get into a meeting with me without a prototype", plus bottom-up early adopters who scaffolded the event). Slack triage is where it broke down: "almost too much data". Bears on agent-identity-delegation, context-and-memory, adoption-model and target-user (product leaders, not only PMs). Evidence is one person's workflow; the adoption numbers are her own.

## Themes
- memory-architecture: "I try to do everything in Markdown just so it's easier for the models to understand it"; "about me" docs, a communication-style doc, and a monthly regenerated summary of Webflow releases from release notes give the agent context; each dinner prep is saved as a Markdown file that any other agent can later reference (25:16-26:35). An "ongoing PRD that's self-documenting this app" (28:02).
- identity-delegation / human-review-gates: Google API tokens in a .env file; calendar read-only; Gmail limited to read, archive, label and draft; she often "take[s] some of the power away" after realising she gave "too much authority to act on my behalf" (11:26-12:57). Drafts, never sends: a human gate by permission design.
- status-update-agents: morning triage suggests what to delegate and to whom, which meetings to make async, and drafts decline messages (13:23-17:37); a "brutal truth" weekly time audit ("you're operating as a senior PM, not a CPO") (16:44-18:45).
- org-context-grounding: Slack triage is her "next hill to climb" because "even with where the models are at, it's almost too much data to triage" (19:48); host: "an indictment" of what humans are expected to triage (21:07).
- leadership-permission-mandate: "it needs to be both a top down mandate ... you can't get into a meeting with me without a prototype ... but then it's also a bottoms up" (32:34); career ladder being rewritten to expect people to "lead and own and understand what is possible" with AI (40:06); "it would be inauthentic for me to tell them, hey, you need to prototype with AI if this isn't something that I'm doing every single day" (6:40).
- enablement-by-product: builder day = whole org stops and builds a prototype; tools lit up (Cursor, Figma Make, Webflow), tracks per function, warm-up assignments, engineers on call, judging panel with the CEO, prizes (33:42). After builder day one (design only) about half the design team used Cursor with sustained use; builder day two spanned design, product, data science, research, analytics and engineering with "80 plus prototypes" (31:03).
- outcome-measurement-gap: impact measured by a Hex dashboard of Cursor usage by role and a post-event survey (fun, empowering, not frustrating) (31:03, 35:49); usage, not outcomes. Personal outcome: "close to the metal" on AI products and on Webflow's code base (28:32).

## Key points
- Stack: Claude Code in several terminals (to keep context separate and similar questions together), Codex, Cursor, a local web app with a custom note-card UI; Google Calendar and Gmail via API token, not MCP ("I don't think there's an official MCP") (8:25, 14:03).
- Dinner prep: screenshot of a guest list, agent searches web and LinkedIn per guest, combines with her context files, writes a prep doc with priority connections and conversation starters (23:44-25:16). She hadn't checked it: "Buyer beware."
- The time audit "wasn't like 100% correct", but she treats it as a signal (10:11).
- Lightning round: thinks parts of this become a product, maybe from Anthropic; "still the very early days of being able to access company data" (39:04).
- Host recap: personal software running locally with internally approved API keys "helps you bypass some of the security concerns around using third party tools" (36:28): a governance claim worth noting, not demonstrated.

## Notable quotes
- "You can't get into a meeting with me without a prototype. So there's a mandate" (32:34).
- "Even with where the models are at, it's almost too much data to triage" (19:48).

## Could not verify
- Transcript read in full. The Substack auto-transcription swaps speaker labels for most of the episode (lines labelled "Claire Vo" are mostly Rachel Wolan and vice versa); attributions above follow content, not labels.
- Adoption figures (half the design team, 80+ prototypes) come from her own dashboard and are not shown in a form we can check; sustained use after builder day two was not yet known.
