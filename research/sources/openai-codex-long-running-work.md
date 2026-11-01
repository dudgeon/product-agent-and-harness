---
title: "Long-running work (Codex docs, ChatGPT Learn)"
source_url: https://learn.chatgpt.com/docs/long-running-work
author: OpenAI
publisher: learn.chatgpt.com
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [through-line-context-budget, human-review-gates, work-structure-spectrum]
relevance: medium
---

## Relevance to the project
OpenAI's guidance for keeping one piece of work going in Codex or ChatGPT Work: Goal mode, one chat per related stream, projects to group chats and files. It is OpenAI's version of the through line inside the person's own harness, and it is noticeably thinner than Anthropic's on what persists: the page says to keep related work in the same chat "so ChatGPT keeps its context" and does not discuss compaction, memories or local-to-cloud handoff.

## Themes
- through-line-context-budget: "Keep related work in the same chat so ChatGPT keeps its context"; each chat keeps its own context, messages, results and goal; group related chats and files in a project.
- human-review-gates: "Starting a goal doesn't grant broader access. It keeps the existing sandbox and approval policy and pauses when it needs a decision."
- work-structure-spectrum: `/plan` to refine an unclear outcome, then `/goal`, where the goal text is both the first prompt and the completion criteria; write it so ChatGPT can "verify its own progress".

## Key points
- Goal mode in the ChatGPT desktop app, Codex CLI and IDE extension; pause, resume, edit or clear the goal; side chat for a status recap without interrupting.
- Avoid two chats changing the same files or writing to the same connected source; use worktrees for parallel coding chats.
- Prevent sleep while running for local macOS work.

## Could not verify
- No page date; compaction, memories, maximum task duration and multi-week guidance are not on this page (linked pages not read). Related prior notes: [Codex /goal](howiai-claire-vo-codex-goal.md), [Codex cloud](openai-codex-cloud-docs.md).
