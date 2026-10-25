---
title: "smolagents conceptual guide: Introduction to agents (agency levels)"
source_url: https://huggingface.co/docs/smolagents/conceptual_guides/intro_agents
author: Hugging Face (smolagents maintainers)
publisher: Hugging Face docs
published: unknown (library launched 2024-12)
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [work-structure-spectrum, levels-of-automation-frameworks, agent-frameworks]
relevance: high
---

## Relevance to the project
The most compact statement of dimension 1 (control flow) as a graded scale with code examples: agency is "how much the LLM's output controls the workflow", from a simple processor (no impact) through router (if/else), tool call, multi-step loop, multi-agent, to code agents that define their own tools. The guide's rule, "regularize towards not using any agentic behaviour" and code the workflow when it can be determined in advance, is the clearest vendor articulation that rigidity is the default and model-chosen control flow must be earned by the task's unpredictability.

## Themes
- work-structure-spectrum: six-row agency table from ☆☆☆ "LLM output has no impact on program flow" to ★★★ "LLM acts in code, can define its own tools / start other agents" (table).
- levels-of-automation-frameworks: agency "evolves on a continuous spectrum, as you give more or less power to the LLM on your workflow" (intro); an LLM-era restatement of levels of automation applied to control flow rather than to action.
- agent-frameworks: "If that deterministic workflow fits all queries, by all means just code everything! This will give you a 100% reliable system"; agents are for when "the pre-determined workflow falls short too often" (When to use agents).

## Key points
- Multi-step agent loop: memory starts with the task; while the LLM says continue, pick an action, execute, append observation.
- Argues that writing actions as code rather than JSON tool calls is more composable and better represented in training data (citing three papers).
- The table conflates two things the project separates: who picks the next step (router, loop) and how much the model can reshape the system (define tools, spawn agents); the latter is closer to the project's dimension 7 (self-rewriting).

## Could not verify
- Page publication or revision date.
