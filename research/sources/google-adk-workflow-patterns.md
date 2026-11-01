---
title: Multi-agent workflow patterns (ADK)
source_url: https://adk.dev/workflows/patterns/
author: Google
publisher: Agent Development Kit docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [agent-frameworks, deterministic-scaffold-model-nodes, human-review-gates]
relevance: medium
---

## Relevance to the project
Google's catalogue of seven patterns with the primitive each uses and how agents communicate in it. It makes plain that ADK's fixed pipelines communicate through shared session state keys, while coordinator and hierarchical patterns communicate through transfer or agent-as-tool calls, with results "returned up the hierarchy (via tool responses or state)".

## Themes
- agent-frameworks: coordinator/dispatcher ("Primarily uses LLM-Driven Delegation ... or Explicit Invocation (`AgentTool`)"); sequential pipeline ("Primarily uses Shared Session State"); parallel fan-out and gather; hierarchical task decomposition; generate and review; iterative refinement (LoopAgent until a quality threshold or max iterations); human-in-the-loop.
- deterministic-scaffold-model-nodes: SequentialAgent / ParallelAgent / LoopAgent are code-defined scaffolds with LLM agents at nodes.
- human-review-gates: a `PolicyEngine` plus `SecurityPlugin` intercepts tool calls and returns `PolicyOutcome.CONFIRM` to pause for user confirmation, described as "more robust for enforcing governance and security rules".

## Key points
- The page says patterns should be evaluated "against your project requirements before committing"; no measured comparisons.

## Could not verify
- No dates or performance data.
