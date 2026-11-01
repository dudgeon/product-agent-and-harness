---
title: Build collaborative agent teams (ADK 2.0)
source_url: https://adk.dev/workflows/collaboration/
author: Google
publisher: Agent Development Kit docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks, task-context-isolation, human-review-gates]
relevance: high
---

## Relevance to the project
ADK 2.0 (2026) replaced open-ended agent transfer with three explicit sub-agent modes that say who talks to the user and how control returns: `chat` (the sub-agent holds the user until it transfers back), `task` (the sub-agent may ask the user clarifying questions, then returns automatically via `finish_task`), and `single_turn` (no user contact, returns a result, can run in parallel). This is first-party evidence that a framework vendor moved from "the conversation follows the transfer" toward "control returns to the coordinator", which is the model B (through line) shape.

## Themes
- handoff-context-transfer: mode table ("Human in the Loop: Full interaction / For clarification only / Disallowed"; "Return to parent: Manual (via transfer) / Automatic (via finish_task) / Automatic (with result)").
- task-context-isolation: "Each task or single-turn mode agent operates in its own isolated session branch"; parallel agents "cannot see what its peer agents are doing"; the parent receives the collected results.
- agent-frameworks: declaring `sub_agents` auto-injects a delegation tool named after each sub-agent; `input_schema` / `output_schema` give typed task objects.
- human-review-gates: task mode allows the sub-agent to ask the user for clarification while the coordinator keeps ownership.

## Key points
- Same task agent can be a graph node (control advances to the next node) or a transferee from an LlmAgent (control returns to the originating agent).
- `chat` is the default and "current behavior"; mode is only for sub-agents, not the root.
- Limitations: task-mode agents must be leaf agents; task mode is disabled in graph-based workflows in ADK Python 2.0.0.
- ADK 2.0 also adds graph workflows, dynamic workflows and an experimental `RoutedAgent` (code chooses the agent per invocation, with fallback on error).

## Could not verify
- Release date of ADK 2.0 (page says Python and Go v2.0.0; docs repository commit removing the 1.x multi-agent page is dated 2026-05-19).
