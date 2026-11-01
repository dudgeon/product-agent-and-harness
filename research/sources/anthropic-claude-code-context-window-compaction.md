---
title: "Explore the context window (Claude Code docs): what survives compaction"
source_url: https://code.claude.com/docs/en/context-window
author: Anthropic
publisher: Claude Code docs (code.claude.com)
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [memory-architecture, task-context-isolation, through-line-context-budget]
relevance: high
---

## Relevance to the project
Model B (through line) depends on one session holding a piece of work for weeks. This page states exactly what a Claude Code session keeps when it compacts: files on disk (CLAUDE.md, auto memory, the plan-mode plan, skill descriptions) come back, while the conversation, hook-added context and path-scoped rules are summarised away. So the durable through line is whatever is written to files, not the conversation. That supports writing intent and dependency state to records the session re-reads, whichever model is chosen.

## Themes
- through-line-context-budget: auto-compaction "replaces the conversation with a structured summary"; 1M-token windows on recent models but "Compaction works the same way at the larger limit."
- memory-architecture: "Project-root CLAUDE.md and unscoped rules: Re-injected from disk"; "Auto memory: Re-injected from disk"; "The plan Claude wrote in plan mode: Re-injected from disk".
- task-context-isolation: a subagent "handles the research in its own separate context window ... Only the summary and a small metadata trailer come back."

## Key points
- Survives compaction table: system prompt and output style still apply; root CLAUDE.md, unscoped rules, auto memory and plan re-injected from disk; skill descriptions rebuilt (v2.1.304+); up to five recently modified files re-read (over 5,000 tokens become a path reference); invoked skill bodies re-injected capped at 5,000 tokens each and 25,000 total, oldest dropped; background subagents keep running; context hooks added earlier is summarised; SessionStart hooks matching `compact` run again.
- Path-scoped rules and nested CLAUDE.md are summarised away; "If a rule must persist across compaction, drop the paths: frontmatter or move it to the project-root CLAUDE.md."
- Skill truncation keeps the start of the file: "put the most important instructions near the top of SKILL.md."
- User controls: `/compact` with a focus, `/rewind` summarise from or up to a message, `/autocompact <tokens>`, `/clear` between tasks, delegate large reads to subagents; idle compaction exists.

## Could not verify
- Default auto-compact thresholds per model are on another page (model-config), not read.
- No quality data on what compaction summaries lose.
