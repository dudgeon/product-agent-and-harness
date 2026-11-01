---
title: "Subagents in VS Code"
source_url: https://code.visualstudio.com/docs/copilot/agents/subagents
author: Microsoft (VS Code team)
publisher: code.visualstudio.com
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [task-context-isolation, delegation-return-contract, harness-portability, meta-harness]
relevance: medium
---

## Relevance to the project
VS Code now hosts several agent harnesses (Local, Copilot, Claude, Codex) and delegates to subagents through each harness's own mechanism: `runSubagent` for Local, Copilot's `task` tool, and the Claude and Codex native subagent systems. The page states the subagent contract plainly for the Local harness: no inherited history, a self-contained task, a focused result back, and each invocation stateless. It also reserves edit tools for the coordinator in its examples, which is one answer to "who is allowed to write the record".

## Themes
- task-context-isolation: "a subagent does not inherit the main conversation history. The delegated task must be self-contained, covering the goal, relevant context, allowed actions (research only or changes), and the expected result."
- delegation-return-contract: the main agent receives the subagent's result; the person can inspect the subagent's prompt, tool calls and result in chat; "Each Local invocation is stateless. Follow-up work requires a new invocation with the needed context"; combined findings should be reviewed before acting.
- harness-portability: the same editor delegates through four different subagent systems depending on harness.
- meta-harness: VS Code is a host above the Copilot, Claude and Codex harnesses.

## Key points
- Nesting off by default; `chat.subagents.allowInvocationsFromSubagents` allows depth up to five.
- Coordinator `agents` frontmatter restricts which custom agents can be subagents; listing one overrides its `disable-model-invocation: true`.
- Local subagents lose the clarifying-question and todo tools.
- Subagent model order: explicit parameter, custom agent's model, Auto (experimental), main model; checked against the main model's cost tier.
- Patterns: coordinator plus read-only subagents; multi-perspective review then deduplicate; not for quick lookups.

## Could not verify
- Whether subagents run in parallel (not stated); page dated 10/28/2026 in its footer.
