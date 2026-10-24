---
title: "The non-technical PM's guide to building with Cursor | Zevi Arnovitz (Meta)"
source_url: https://www.lennysnewsletter.com/p/the-non-technical-pms-guide-to-building-with-cursor
author: Lenny Rachitsky (host), Zevi Arnovitz (product manager, Meta)
publisher: Lenny's Podcast
published: 2026-01-18
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [non-engineer-builders, opportunity-to-code-chain, human-review-gates, skill-standards, compounding-context-repo, docs-as-code-prd, harness-portability, human-judgment-pm-jobs]
relevance: medium
---

## Relevance to the project
A non-technical PM at Meta shows the structured workflow he uses to build and ship his own side-project apps (one with over a thousand paying users): a chain of slash commands, create issue (in Linear), exploration, create plan, execute, review, peer review across models, update docs, plus a "learning opportunity" command. It is a compact, personal instance of the opportunity-to-code chain with the PM shaping intent and the agent asking clarifying questions, and of cross-vendor review as a substitute for reviewing code you cannot read. His advice for larger companies is cautious: make the codebase "AI native" first (done by engineers), then PMs ship contained UI work and hand the PR to a developer. Bears on intent-shaping-and-spec, review-and-autonomy, capability-format-portability and target-user.

## Themes
- opportunity-to-code-chain: slash-command sequence (15:00-20:44): /create issue (brief questions, writes a Linear ticket, 20:44-22:22), /exploration (Claude analyses the codebase and asks clarifying questions only, 16:26), /create plan (TL;DR, critical decisions, tasks with status trackers, 29:50), /execute, /review, /peer review, /update docs.
- human-review-gates: manual QA first, then /review by Claude, then Codex and Cursor each review the branch; /peer review pastes "dev lead one" and "dev lead two" findings back and has the models "fight it out" (38:33-45:04).
- compounding-context-repo / docs-as-code-prd: after mistakes he asks "What in your system prompt or tooling made you make this mistake?" and updates commands and docs so it doesn't recur (45:52); codebase has many Markdown files telling agents how to work in each area (51:28).
- skill-standards: commands are reusable prompts stored in the codebase with placeholders and output-format instructions (14:50; show notes takeaways).
- harness-portability: model roles: Claude as communicative, opinionated "CTO"; Codex as quiet engineer for hard bugs; Gemini for UI with a chaotic process (40:55-42:28).
- non-engineer-builders: at a larger company, PMs should not ship database migrations or big projects, but contained UI work with the PR finished by a developer (51:28); the codebase must be made AI-native by technical people first.
- human-judgment-pm-jobs: slop "is human error"; "you own your own outputs" (54:25-56:00).

## Key points
- Origin: began with a ChatGPT project acting as "CTO" whose system prompt held the step-by-step workflow; later moved to Claude Code and Cursor; "exposure therapy" path ChatGPT project, then Bolt/Lovable, then Cursor in light mode (8:03, 19:31, show notes).
- He says Linear tickets created this way are good for a "company of one" but he would not create work tickets this way at Meta, where context lives across teams (26:08).
- Engineers at Meta reportedly ask him to teach them his workflow (5:06, per a quote from Tal Raviv).
- Predicts titles and responsibilities will "collapse" and everyone will build, but advises winning over sceptical developers first (52:42).

## Notable quotes
- "What in your system prompt or tooling made you make this mistake?" (45:52)
- "titles are going to collapse and responsibilities are going to collapse and everyone's just going to be building" (52:42)

## Could not verify
- Show notes and takeaways read in full; transcript read by search for slash commands, review, Linear, context, docs, Meta and the large-company question (roughly 14:00-58:00 read in parts); interview-prep and career sections skimmed.
- The workflow is for his own side projects, not Meta's process; Meta is his employer, not the subject. Revenue and user numbers are his own.
