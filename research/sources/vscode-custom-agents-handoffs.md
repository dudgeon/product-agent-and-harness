---
title: "Custom agents in VS Code (handoffs between agents)"
source_url: https://code.visualstudio.com/docs/copilot/customization/custom-agents
author: Microsoft (VS Code team)
publisher: code.visualstudio.com
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [human-review-gates, harness-portability, work-structure-spectrum, process-artifacts-as-coordination]
relevance: high
---

## Relevance to the project
VS Code custom agents can declare handoffs: after a response, a button switches to another named agent "with the conversation context and a pre-filled prompt", and the person reviews and sends it (or `send: true` submits automatically). This is a shipped, person-gated version of model A (finish-to-start relay) inside one editor session: planner agent, then implementer, then reviewer, with the human clicking at each seam. Unlike a relay through the feature repo, what crosses is the conversation itself, so nothing is written down unless an agent writes it.

## Themes
- human-review-gates: "you select Implement Plan, review the pre-filled prompt, and send it"; `send: true` removes the gate.
- work-structure-spectrum: listed uses are plan to implementation, implementation to code review, failing tests to passing tests; the relay is configured, not improvised.
- harness-portability: custom agents are `.agent.md` files with YAML frontmatter, stored in `.github/agents` or `.claude/agents` in the workspace, or `~/.copilot/agents` and `~/.claude/agents` for the user; previously called custom chat modes.
- process-artifacts-as-coordination: the handoff payload is the chat context plus a prompt, not a file; a team wanting an auditable seam must make the agent write the plan to a file.

## Key points
- Handoff frontmatter shown: `label`, `agent`, `prompt`, `send`; a model option for the next step is referenced.
- Handoffs available in the Local harness.
- A custom agent can also be run as a subagent by another agent; `user-invocable: false` hides it from the picker while keeping it callable; `disable-model-invocation` controls subagent use.
- A tools list restricts the agent to "only those tools".

## Could not verify
- Introduction date of handoffs (page footer 10/28/2026); whether custom agents and handoffs work in the Copilot cloud agent.
