---
title: Processes and Tasks (CrewAI docs)
source_url: https://docs.crewai.com/en/concepts/processes
author: CrewAI
publisher: CrewAI docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks, human-review-gates]
relevance: medium
---

## Relevance to the project
CrewAI's sequential process is a literal finish-to-start relay: "the output of one task serving as context for the next", with `context` choosing which earlier task outputs a task receives, guardrails validating output "before they are passed to the next task", and optional `output_file`. The hierarchical process puts a manager LLM or agent in charge of planning, delegation and validation. Together they are the framework form of model A (relay of task outputs) and of a manager-led hierarchy. Also read the Tasks page (https://docs.crewai.com/en/concepts/tasks).

## Themes
- handoff-context-transfer: "In CrewAI, the output of one task is automatically relayed into the next one"; `TaskOutput` holds `raw` by default plus `pydantic` or `json_dict` if configured (Tasks page).
- agent-frameworks: hierarchical needs `manager_llm` or `manager_agent`; tasks are not pre-assigned; the manager reviews outputs.
- human-review-gates: `human_input=True` has a human review the agent's final answer; guardrails retry up to `guardrail_max_retries`.

## Key points
- What crosses is a task output (text or structured object), not a transcript.

## Could not verify
- Behaviour of `allow_delegation` (not on these pages).
