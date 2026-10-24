---
title: Best practices for getting started with Claude Cowork
source_url: https://claude.com/resources/articles/best-practices-for-getting-started-with-claude-cowork
author: Austin Lau (growth marketing, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-06-03
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [non-engineer-builders, metrics-review-agents, status-update-agents, agent-led-intent-shaping, enablement-by-product]
relevance: medium
---

## Relevance to the project
An Anthropic growth marketer's heuristic for which knowledge-work tasks to delegate to an agent ("Cowork-shaped" tasks: several inputs, a file out, recurring, you know what good looks like, the middle is the boring part) is directly reusable as an adoption filter for PMs, designers and analysts. It also gives three small, concrete recurring workflows (daily Slack/Gmail briefing, ad-spend pacing dashboard, weekly Search Console report) and one habit with design implications: make the agent restate the ask and ask clarifying questions before starting. It predates the September 2026 merge of chat and Cowork, so its "which workspace" advice is superseded by `claude-cowork-chat-unified`, though the task heuristic still stands. Single-person account; time savings are the author's own estimates.

## Themes
- non-engineer-builders: the author went from not knowing what a terminal was to Claude Code workflows within a week, and now does 90% of their work in Cowork (intro).
- metrics-review-agents: weekly Search Console report reconciled into one sheet with a 7-vs-7-day comparison and flags; time cut from ~30 to ~5 minutes per week, the rest spent on judgement (How I use Cowork, "Reporting").
- status-update-agents: 6am scheduled "daily briefing" that buckets unread email and chosen Slack channels and flags overnight incidents (How I use Cowork, "Daily briefing").
- agent-led-intent-shaping: "Make Claude ask you questions before it starts", repeating the ask back and asking clarifying questions, called the single most useful habit (Your first 10 minutes).
- enablement-by-product: delegation checklist and chat-vs-Cowork examples as the adoption guidance, with "ask Claude which of your tasks to hand off" using memory of past conversations (When should you use Cowork; Your first 10 minutes).

## Key points
- **Surface split (pre-merge).** Chat for answers that fit in a few exchanges ("the output is a thought in your head"); Cowork for deliverables someone else will open, multi-step or multi-file or multi-app work ("something you'll hand to someone else"); Claude Code for developers. Cowork and Claude Code are said to run on the same engine.
- **Five ingredients of a delegable task:** more than one input; a file comes out; recurring; you already know what good looks like (can judge in 15 seconds whether it is right or "70% there"); the thinking is at the start and end, the middle is extraction, compilation, reconciliation and reformatting.
- **Budget pacing.** Connectors to Google Ads and Meta Ads feed a "live artifact" (HTML dashboard in the desktop app) that recalculates pacing on demand, replacing manual exports or a third-party ETL tool.
- **Context over prompt.** The author says output quality depends almost never on the prompt and mostly on giving rich context (files, folders, connectors).
- **Scheduling** of recurring tasks is presented as the sweet spot.
- **Limits:** one marketer's usage; no error rates or failure cases; time savings self-reported; written before the chat/Cowork merge, so the surface guidance is dated.

## Notable quotes
- "The thinking lives at the start (deciding what you want) and the end (deciding if it's right)." (Five ingredients)
- "Chat is for when the output is a thought in your head, and Claude Cowork is for when the output is something you'll hand to someone else." (When I still reach for chat)
