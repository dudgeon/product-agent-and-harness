---
title: "Tools: agents as tools (OpenAI Agents SDK)"
source_url: https://openai.github.io/openai-agents-python/tools/
author: OpenAI
publisher: OpenAI Agents SDK docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks, task-context-isolation]
relevance: high
---

## Relevance to the project
The counterpart to handoffs: `Agent.as_tool()` runs a specialist as a nested call whose input is a single string (or a declared structured schema) and whose output is the nested agent's final answer. The parent's conversation is not inherited unless the same session is passed explicitly. This is the mechanism behind model B (through line): the calling agent keeps the user and the context, and the specialist sees only what it is handed.

## Themes
- handoff-context-transfer: "By default, `Agent.as_tool()` expects an object with one string field, `input`"; "the parent run's conversation state is not inherited automatically"; share history only by passing "the same `session` to both".
- task-context-isolation: structured input via `parameters` (Pydantic model or dataclass), `include_input_schema`, `input_builder`; output post-processed by `custom_output_extractor`, which sees the nested `RunResult`.
- agent-frameworks: framed as a way to "expose an agent as a callable tool without a full handoff"; the central agent keeps control.

## Key points
- The nested run should use one state strategy: a client-managed session, or server-managed continuation.
- `custom_output_extractor` can scan the nested run's items for a specific payload, reformat, or supply a fallback; `agent_tool_invocation` exposes the outer call id and raw arguments, useful for audit.
- Read with the existing note [openai-agents-sdk-multi-agent-orchestration](openai-agents-sdk-multi-agent-orchestration.md), which states the manager-keeps-the-conversation rule.

## Could not verify
- Page undated.
