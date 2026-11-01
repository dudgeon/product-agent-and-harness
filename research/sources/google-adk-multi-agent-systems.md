---
title: Multi-Agent Systems in ADK (archived 1.x page)
source_url: https://github.com/google/adk-docs/blob/50f7df7f460b5aaaca550098a0243674f4d69ae2/docs/agents/multi-agents.md
author: Google
publisher: Agent Development Kit docs (GitHub google/adk-docs)
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks, process-artifacts-as-coordination]
relevance: high
---

## Relevance to the project
Google ADK's 1.x reference for three ways agents pass work: shared session state (passive, by keys), LLM-driven transfer (`transfer_to_agent`, which moves execution focus to another agent in the hierarchy), and explicit invocation (`AgentTool`, where the parent stays in control). It is the clearest case of shared state as the handoff medium, close to model A's "context written somewhere the next agent reads". The page was removed from the live site in the ADK 2.0 restructure (May 2026); this note cites the last version in the docs repository.

## Themes
- handoff-context-transfer: transfer "updates the `InvocationContext` to switch execution focus" (section b); `AgentTool` "runs the target agent, captures its final response, forwards any state/artifact changes back to the parent's context, and returns the response as the tool's result" (section c).
- process-artifacts-as-coordination: shared `session.state` is "the most fundamental way" agents in one invocation communicate; `output_key` saves an agent's final response to a state key that later agents read (section a).
- agent-frameworks: `SequentialAgent` passes the same `InvocationContext` in order; `ParallelAgent` gives each child its own `branch` but all share the same `session.state` ("use distinct keys to avoid race conditions"); `LoopAgent` passes the same context each iteration.

## Key points
- Transfer requires clear `description`s on target agents and instructions on the caller; scope (parent, sub-agent, siblings) is configurable via `disallow_transfer_to_parent` / `disallow_transfer_to_peers`.
- `temp:` state is shared between parent and sub-agent within one invocation, for data only relevant to the current turn.
- Related setting on `LlmAgent` (llm-agents page): `include_contents='none'` makes an agent receive no prior conversation history, only its instruction and the current turn input; the default sends "the relevant conversation history".
- Patterns listed: coordinator/dispatcher, sequential pipeline, parallel fan-out/gather, hierarchical decomposition, generator-critic, iterative refinement, human-in-the-loop (now on the live patterns page: [google-adk-workflow-patterns](google-adk-workflow-patterns.md)).

## Could not verify
- Exactly which history a transferred-to agent sees under `include_contents='default'` ("relevant" history is not defined on the page).
