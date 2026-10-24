---
title: Building effective agents
source_url: https://www.anthropic.com/engineering/building-effective-agents
author: Erik S. and Barry Zhang (Anthropic engineering)
publisher: Anthropic Engineering blog
published: 2024-12-19
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [work-structure-spectrum, single-agent-many-skills, one-job-per-agent, evals-autonomy-trust, agent-frameworks]
relevance: high
---

## Relevance to the project
The canonical vendor statement of the workflow/agent split: predefined code paths for well-defined tasks, model-directed loops for open-ended ones. It is the main citation for the first half of Geoff's hypothesis (structured work wants a workflow, open work wants an agent), but it frames the split by *predictability of steps*, not by user activity type, and it says start with the simplest thing. The page now notes the tooling landscape has changed since 2024.

## Themes
- work-structure-spectrum: workflows = "predefined code paths"; agents = LLM "dynamically direct their own processes"; choose by whether steps can be predicted in advance (Summary, "When to use agents").
- single-agent-many-skills: start simple; many applications need only one optimized LLM call with retrieval.
- evals-autonomy-trust: agents need "some level of trust" in the model; checkpoints, max-iteration stops, sandbox testing; coding agents work because output is verifiable by tests, but human review stays essential (Appendix 1).
- agent-frameworks: frameworks help getting started but obscure prompts; start with raw APIs.

## Key points
- Workflow patterns: prompt chaining, routing, parallelization (sectioning, voting), orchestrator-workers, evaluator-optimizer. Agents are "typically just LLMs using tools based on environmental feedback in a loop".
- Workflows "offer predictability and consistency for well-defined tasks"; agents when "flexibility and model-driven decision-making are needed at scale". Agents trade latency and cost; risk of compounding errors.
- Good agent use cases (customer support, coding) share: verifiable outcomes, tool integration, human-checkable results.
- Not stated: any guidance on user-activity classes (ideation vs review), team-process standardization, or multi-user settings.

## Could not verify
- Page header says much has changed since Dec 2024 and points to newer Managed Agents material; not read.
