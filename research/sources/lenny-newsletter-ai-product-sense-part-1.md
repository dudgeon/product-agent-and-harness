---
title: "How to build AI product sense"
source_url: https://www.lennysnewsletter.com/p/how-to-build-ai-product-sense
author: Tal Raviv and Aman Khan (guest authors; AI product builders and workshop instructors), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2026-02-03
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [docs-as-code-prd, memory-architecture, compounding-context-repo, harness-over-model, pm-tool-connectivity, pm-job-stable-methods-change, work-structure-spectrum]
relevance: medium
---

## Relevance to the project
Two experienced AI PMs argue that PMs should do their non-technical work (strategy, prioritization, PRDs, analysis) inside a coding agent (Cursor, Claude Code) rather than a chat app, because a file-based workspace makes knowledge "malleable": the agent edits the documents directly, so outputs live in files and chats become disposable. That is the same pattern as this project's own setup and a practitioner datapoint for the context-and-memory and artifact-and-project-structure dimensions (folders of Markdown, an AGENTS.md as memory, selective context per chat). It also gives a PM-legible explanation of the harness (Cursor as "agent harness" that executes tool calls) that could help the film explain the concept. Part 2 of the series is filed separately as lenny-newsletter-ai-product-sense-part-2.

## Themes
- docs-as-code-prd: "Cursor is fundamentally the same idea as ChatGPT projects: files as knowledge, chat as interface, and instructions that always apply", but the AI "edits your files directly (malleable knowledge)" (Step 3, "Cursor is our choice for getting real work done").
- compounding-context-repo: "outputs live in documents and chats become disposable one-offs because the value lives in documents, not in conversation history"; the knowledge base "will cover more ground, and update more frequently" (Step 3).
- memory-architecture: memory "is just a text file prepended to every conversation"; AGENTS.md content costs context in every chat, so choose memory (persistent, always relevant) versus retrieval (task-specific) deliberately (Step 9).
- harness-over-model: "There are only a few frontier LLMs, and they're available to all product teams. Innovation is how we apply them" (Step 5); tool calling is "its own behavior, separate from reasoning or writing quality" (Step 6); Cursor plays the "MCP client" or "agent harness" role (Step 6).
- pm-tool-connectivity: MCP framed as USB for SaaS data (Linear, Figma, Notion, Snowflake, BigQuery, Amplitude, Mixpanel) (Step 6, "what's the MCP").
- pm-job-stable-methods-change: the authors "now spend most of our days in coding agents for non-technical tasks": strategy, prioritization, decision-making, data analysis (intro, Step 3).
- work-structure-spectrum: Cursor preferred for pairing and watching the agent; Claude Code for "delegating long-running independent tasks" (Step 1).

## Key points
- Personal OS scaffold (Step 7): `Knowledge/`, `Tasks/` (Markdown task files), `GOALS.md`, `AGENTS.md` with rules such as "Never write code — only Markdown", keep tasks tied to goals, suggest at most three daily priorities.
- PRD context checklist (Step 10): a folder of research transcripts, existing landing page or sales deck, research papers or tech docs, an analytics MCP, saved instructions, a request to search, an area of the codebase.
- Context engineering = what you include per chat plus what is always included (AGENTS.md, MCPs, tools); watch the context meter "like a car's gas tank"; "context rot" hurts precision tasks (finance, coding, data analysis) more than brainstorming (Step 10).
- Footnote techniques: progressive disclosure (Claude Skills as example), subagents returning only the "bottom line", condensing MCP tools, pruning or summarizing near the limit.
- Model observations (as of early 2026): Claude Opus for writing and complex planning; Sonnet with 1M context as workhorse; Claude refused to alter Disney lyrics on copyright grounds; OpenAI models "stumbled" calling Cursor's apply_patch (Step 5). Tal's student, a salesperson: Cursor is "AI that can touch any file on my computer" (Step 3).
- Method claim: the post is an interactive tutorial; the authors "ran dozens of usability sessions, wrote evals, optimized each prompt" (Lenny intro); readers can continue inside Cursor via a tutor prompt.

## Notable quotes
- "AI agents are a three-way group chat between an LLM, a human, and tools" (Step 6).
- "Mensa geniuses with the short-term memory of a hamster" (Step 9, on statelessness).

## Could not verify
- Screenshots (Cursor UI, Anthropic's context-engineering diagram) were images not in the text.
- Partnership with Cursor (free credits) is disclosed; the authors sell a workshop. No data on how many PMs work this way.
