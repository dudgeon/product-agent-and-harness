---
title: "How I built LennyRPG"
source_url: https://www.lennysnewsletter.com/p/how-i-built-lennyrpg
author: Ben Shih (growth designer, Miro), guest post; intro by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2026-03-17
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [docs-as-code-prd, prd-agents, non-engineer-builders, one-job-per-agent, human-judgment-pm-jobs, legible-org-for-agents, skill-standards]
relevance: medium
---

## Relevance to the project
A non-technical designer's detailed build log shows the PRD surviving as the agent's anchor document: an AI interviews him into a PRD, the PRD becomes a Markdown file in the repo, and he sends the agent back to it "whenever the AI hits a wall or the context window runs out". He says nailing the idea and PRD "determines 80% of how smooth the rest of the build will be". That supports the film's claim that intent quality is the new bottleneck, from the builder's side. It also shows role-split agents (Claude Code as "lead engineer" planning, Codex executing, Composer for small tasks) and Markdown logs as working memory. Lenny's intro adds that he released his whole archive as AI-friendly Markdown plus an MCP server, an example of making a body of knowledge legible to agents. Bears on intent-shaping-and-spec and work-structure. A side project, not enterprise practice.

## Themes
- docs-as-code-prd: the PRD is "the single source of truth for the build", moved into Cursor as a Markdown file; used to realign the agent when it drifts or context runs out (sections 2-3). Claude Code also keeps a Markdown log of every attempt at a hard fix so it can refer back (Challenge #3), and UI issues are logged in a Markdown file for the AI to work through (section 5).
- prd-agents: "instead of writing the PRD myself from scratch, I let the AI interview me": ChatGPT asked 17 grouped clarifying questions; he answered by dictation (Wispr Flow) on a Miro board; the answers plus Miro artifacts were chained into a full PRD (section 2). Answering "forced me to think through gaps and assumptions".
- non-engineer-builders: a "non-technical product designer" shipped a public game with a Supabase leaderboard; Supabase MCP created the project and migrations from a description (section 4).
- one-job-per-agent: Claude Code as "lead engineer" for planning, architecture and library search; Codex for executing plan tasks ("very good at following instructions accurately", larger token limit); Cursor Composer for small scripts and formatting (section 3).
- human-judgment-pm-jobs: game balance, pacing and stress level were "all manual"; AI only sanity-checked numbers; "Good UX still requires intention, taste, and judgment" (sections 4 and lessons).
- legible-org-for-agents: Lenny releases ~350 posts and ~300 transcripts as Markdown with an MCP server and GitHub repo (LennysData.com), built "agentically" with Codex and Claude Code (intro).
- skill-standards: final QA used a "review skill" downloaded from a Claude Code skills marketplace; he "did not blindly accept everything it suggested" (section 5).

## Key points
- **Six-step flow** (How I built it): define core idea (sketch for visual products) -> PRD -> proof of concept -> remaining features -> polish -> ship. "The process isn't that different from before the AI era", but more time goes into the first two steps.
- **Visual context first** (section 1): rough Miro concept on top of reference screenshots so the AI can read visuals with text; ChatGPT asked to turn a liked avatar into a reusable prompt template.
- **Pivots** (section 3): RPG-JS got a demo running in about five minutes but fought the quiz mechanics; after discussing with Claude Code he switched to Phaser.
- **Batch jobs by CLI** (section 4): Claude Code wrote CLI tools to generate five quiz questions per transcript via the OpenAI API (about 20 minutes for 300+) and to generate 250+ avatars from episode covers; every avatar still checked by hand for edge cases (two guests on one cover).
- **Informal play-testing** in the office before scaling the POC (section 3).
- Lesson: "building is no longer the bottleneck"; creativity and judgment matter more (lessons 1 and 3).

## Notable quotes
- "Nailing the core idea and PRD determines 80% of how smooth the rest of the build will be." (How I built it)
- "Whenever the AI hits a wall or the context window runs out, you can refer it back to the PRD to realign." (section 2)

## Could not verify
- Read in full. Screenshots referenced in the post (prompts, PRD, logs) were not available as images. "Built in a few hours" is the author's own description and conflicts with the multi-stage effort described.
- The skills marketplace is named loosely ("Claude Code Awesome Skills marketplace"); which skill was used is not specified.
