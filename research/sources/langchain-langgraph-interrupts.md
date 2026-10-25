---
title: Interrupts (LangGraph docs)
source_url: https://docs.langchain.com/oss/python/langgraph/interrupts
author: LangChain
publisher: LangChain docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [human-review-gates, agent-frameworks, deterministic-scaffold-model-nodes]
relevance: medium
---

## Relevance to the project
The framework-level mechanism for a human gate placed by code: `interrupt()` inside a node pauses the graph, persists state and waits indefinitely for a human value. It lists four human-gate patterns that map onto PM review steps (approve or reject, edit state, review a tool call, re-ask on invalid input) and states placement rules (side effects after the gate).

## Themes
- human-review-gates: patterns: approve/reject before critical actions; review and edit LLM output; approve, edit or cancel a tool call; validate human input with a loop-back edge.
- deterministic-scaffold-model-nodes: the gate is a code-placed node in the graph, resumed with `Command(resume=...)`; requires a checkpointer ("use a durable checkpointer in production"); the run "waits indefinitely until you resume execution".

## Key points
- Dynamic interrupts (inside nodes) versus static breakpoints; "Static interrupts are not recommended for human-in-the-loop workflows."
- Rules: one interrupt per node invocation; keep interrupt order stable across runs; don't wrap in bare try/except; put non-idempotent side effects after the interrupt or in a separate node.

## Could not verify
- Page undated; no guidance on which steps deserve a human gate (only how).
