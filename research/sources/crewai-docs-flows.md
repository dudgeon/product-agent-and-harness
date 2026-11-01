---
title: Flows (CrewAI docs)
source_url: https://docs.crewai.com/en/concepts/flows
author: CrewAI
publisher: CrewAI docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [deterministic-scaffold-model-nodes, process-artifacts-as-coordination, human-review-gates]
relevance: medium
---

## Relevance to the project
Flows are CrewAI's deterministic layer: typed state (a Pydantic model with an automatic id), event-style `@start` / `@listen` / `@router` methods, `@persist` to SQLite with resume by id, and `@human_feedback` pauses. Crews run inside flow steps and "do not share state with each other directly"; data moves through flow state. This is the state-object-as-handoff shape, with code, not an agent, holding the through line.

## Themes
- deterministic-scaffold-model-nodes: flow methods chain by listeners and routers; crews are invoked with `kickoff()` using state values and their `raw` output written back to state.
- process-artifacts-as-coordination: `self.state` is the medium between steps.
- human-review-gates: `@human_feedback` (CrewAI 1.8.0+) pauses for input; with `emit`, an LLM maps free-form feedback to a listed outcome that triggers a listener.

## Key points
- `restore_from_state_id` forks a new run from a saved snapshot, keeping the original history.
- `flow.usage_metrics` aggregates tokens across crews.

## Could not verify
- Production durability of the SQLite default for long-lived runs.
