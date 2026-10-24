---
title: "Community Wisdom: Building a PM copilot with a large context window, navigating career growth and relocation, managing product backlogs effectively, office seating dynamics, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-building-a-pm-copilot
author: Lenny's Newsletter community (Slack members); compiled by Kiyani
publisher: Lenny's Newsletter
published: 2026-01-10
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [compounding-context-repo, org-context-grounding, feedback-triage-agents, harness-portability]
relevance: low
---

## Relevance to the project
Two threads touch the project. In the first, a PM hits upload limits building a "PM copilot" in ChatGPT, Gemini Gems and NotebookLM, and the community's consensus answer is to switch to a coding agent (Claude Code or Codex) over a local folder or a Drive folder, with a core document plus subfolders as the knowledge base, which is evidence that practitioners already treat a general coding harness over files as the PM agent's context layer. One reply names the limit: most tools require uploading context to a separate platform, maintaining it is constant manual work, and it is "difficult or impossible to share context across your org". The backlog-intake thread describes request intake without agents (department champions, traceability between requests and roadmap items). Thin and anecdotal. Bears on context-and-memory.

## Themes
- compounding-context-repo: suggested pattern: a primary-source document with context that applies across all use cases, plus folders and subfolders as deeper paths the agent goes into as needed, rather than loading everything each time (thread 1). Another member says a 60,000-line codebase uses only 2% of Codex's context, so a coding agent can "double as a copilot" (thread 1).
- org-context-grounding: one reply: "Maintaining context is constant manual work, and it's difficult or impossible to share context across your org"; IDE-based tools mostly understand only text files (thread 1).
- harness-portability: Obsidian vault plus Claude Code is recommended by several members, including a well-known discovery coach ("It can grep through your Vault and find what's most relevant") (thread 1). Claude Code is valued for files, slash commands as stored prompts, background agents with isolated context, skills, and quick web UIs over content (thread 1).
- feedback-triage-agents: thread 3 (backlog intake) is mostly non-agent process, but one PM says "I haven't manually written a ticket in over 6 months", and another describes department "champions" who collect ideas, turn them into clear product requests, enrich them with signals (segment, customers, prospects, lost deals) and de-dupe, with every roadmap item linked to at least one request for traceability (thread 3).

## Key points
- The original poster's real use case was a personal coaching agent over years of highlights and articles; he planned to try Claude Code first.
- A member built a zero-install web app that works on local files as project context and produces PM docs as Markdown, MARP slides and CSVs (thread 1); an example of the same need.
- A three-state model for request review: "Not for now", "On roadmap" (intent exists, timing undecided), "Committed" (delivery planned with ETA) (thread 3).
- Threads 2 and 4 (relocation, office seating) are off-topic.

## Could not verify
- Community Slack threads; all claims are personal. The 2% context figure is one member's observation. Relevance is low: generic advice, no organisational deployment.
