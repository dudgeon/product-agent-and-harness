---
title: Agent Development Kit (ADK) documentation
source_url: https://adk.dev/
author: Google
publisher: ADK docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks]
relevance: medium
---

## Relevance to the project
Google's open-source, model-agnostic agent framework with workflow agents, sessions/memory, A2A support and managed deployment on Google Cloud. A framework-class option that ships runtime and eval pieces, in contrast to coding harnesses.

## Themes
- agent-frameworks: what ADK provides versus leaves to you.

## Key points
- LLM agents, graph-based workflows, sequential/loop/parallel workflow agents, multi-agent routing.
- Tools: function, MCP, OpenAPI, auth, Google Search grounding.
- Sessions, state, memory, artifacts, context compression and caching.
- Deploy anywhere, or Google Cloud (Agent Runtime, Cloud Run, GKE); A2A expose/consume; evaluation, simulation, observability.
- Model-agnostic (Gemini plus adapters for Claude, OpenAI, Ollama, vLLM, LiteLLM). Python, TypeScript, Go, Java, Kotlin.
- ADK 2.0 is current major release (graph workflows); TypeScript 2.0 GA.

## Added by research-skill-rigidity-spectrum (2026-10-25)
Read the workflow pages (docs moved from google.github.io/adk-docs to adk.dev): https://adk.dev/agents/workflow-agents/, https://adk.dev/agents/, https://adk.dev/workflows/ (first-party).
- Workflow agents ("template workflows": Sequential, Loop, Parallel) control sub-agent execution "without consulting an AI model for assistance with the orchestration", so their flow is deterministic; Loop repeats "until a specific termination condition is met".
- In ADK 2.0 (Python, Go) "template workflows have been superseded" by graph-based workflows ("composable, reliable execution paths that combine AI reasoning with deterministic code logic", with decision branching) and dynamic workflows (flow written in ordinary code). Reasons given to move from one LLM agent to a workflow: instruction-following reliability, context limits, modularity, and mixing deterministic code with model calls.
- Other modes: collaborative workflows (a coordinator agent directs sub-agents), experimental Agent Routing (runtime selection among agents). The navigation lists "Human input" nodes under graph workflows; not read.
- Could not verify: loop-termination details (max iterations, escalation), routing semantics on edges, and the human-input node page.
- Themes: deterministic-scaffold-model-nodes, work-structure-spectrum.
