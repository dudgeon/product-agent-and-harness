---
title: langgraph-supervisor-py (README)
source_url: https://github.com/langchain-ai/langgraph-supervisor-py
author: LangChain
publisher: GitHub
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks]
relevance: medium
---

## Relevance to the project
The supervisor library is now archived, with LangChain recommending "the supervisor pattern directly via tools rather than this library for most use cases". Its options name the history choices precisely: handoffs pass full history by default; `output_mode` chooses whether the supervisor's history keeps a sub-agent's full history or only its last message; `forward_message` sends a sub-agent's reply to the user verbatim to avoid paraphrase.

## Themes
- handoff-context-transfer: default handoff tool "passes full message history (all of the messages generated in the supervisor up to this point)"; `output_mode="full_history"` vs `"last_message"`; `add_handoff_messages=True` by default.
- agent-frameworks: hierarchical teams by nesting supervisors; repository archived (read-only).

## Key points
- `create_forward_message_tool` adds a `forward_message(from_agent)` tool that passes a sub-agent's last message straight to graph output; saves supervisor tokens and avoids paraphrasing errors.

## Could not verify
- Archive date.
