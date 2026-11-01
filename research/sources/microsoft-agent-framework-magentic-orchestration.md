---
title: Microsoft Agent Framework Workflows Orchestrations - Magentic
source_url: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/magentic
author: Microsoft (Tao Chen)
publisher: Microsoft Learn
published: 2026-09-04
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [agent-frameworks, process-artifacts-as-coordination, human-review-gates, handoff-context-transfer]
relevance: high
---

## Relevance to the project
Magentic is the shipped form of an orchestrator that keeps a shared ledger: a task ledger (facts and plan) and a per-round progress ledger (satisfied? looping? progressing? next speaker, instruction), with stall detection, replanning and optional human plan sign-off. The ledger is the closest framework analogue to a record the through-line agent keeps for the whole piece of work, and the plan review is a natural human gate.

## Themes
- process-artifacts-as-coordination: the manager "maintains a shared context, tracks progress, and adapts the workflow"; progress ledger fields are emitted each round as events.
- human-review-gates: plan review (approve or revise); off by default in Python (`enable_plan_review=False`), on by default in .NET (`RequirePlanSignoff` true).
- agent-frameworks: same architecture as group chat "with a very powerful manager"; limits `max_round_count`, `max_stall_count`, `max_reset_count`.
- handoff-context-transfer: participants receive an instruction or question from the manager each round; the manager synthesises the final answer.

## Key points
- "it is untested how well the Magentic orchestration will perform outside of the original Magentic-One design" (note on the page).
- Don't share a stateful manager across concurrent workflows.
- Magentic types are marked experimental in .NET.

## Could not verify
- Exactly what conversation each participant sees (not specified).
