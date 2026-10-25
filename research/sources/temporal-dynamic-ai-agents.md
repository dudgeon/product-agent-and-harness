---
title: Of course you can build dynamic AI agents with Temporal
source_url: https://temporal.io/blog/of-course-you-can-build-dynamic-ai-agents-with-temporal
author: Mason Egger, Steve Androulakis (Temporal)
publisher: Temporal blog
published: 2025-11-12
retrieved: 2026-10-25
type: article
evidence: vendor-claim
filed_by: research-skill-rigidity-spectrum
themes: [deterministic-scaffold-model-nodes, work-structure-spectrum, agent-frameworks]
relevance: medium
---

## Relevance to the project
Separates two meanings of "deterministic" that the rigidity question tends to merge: the orchestration (the loop, sequencing, retries, replay) can be deterministic while the decisions inside it (plan, tool choice) are fully model-chosen. Durable-execution vendors thus place rigidity in the runtime, not in the step list, and record model choices so a resumed run follows the path already taken.

## Themes
- deterministic-scaffold-model-nodes: "The orchestration of the LLM and tool calls is deterministic, while the calls, the plan, the tools executed are completely non-deterministic."
- work-structure-spectrum: LLM output captured as Activity results in Event History; on recovery the Workflow replays recorded results rather than re-asking the model.

## Key points
- Only Workflow code must be deterministic; LLM calls run as Activities.
- An LLM-generated plan supplies steps; each step can run as a child Workflow with its own loop.
- Human-in-the-loop is not discussed beyond the model choosing to ask the user (search results say Temporal's ADK integration uses signals for human waits; not read).

## Could not verify
- Vendor post; no reliability numbers; human-gate mechanism not read first-hand.
