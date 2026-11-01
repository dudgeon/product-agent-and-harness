---
title: "Using PLANS.md for multi-hour problem solving"
source_url: https://developers.openai.com/cookbook/articles/codex_exec_plans
author: OpenAI
publisher: OpenAI Cookbook
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, decision-rationale-records, relay-information-loss, sdd-input-contracts]
relevance: high
---

## Relevance to the project
OpenAI's own pattern for long autonomous Codex runs makes the plan file the full contract: self-contained enough that a newcomer could finish, a living document with mandatory Progress, Surprises & Discoveries, Decision Log and Outcomes sections, and "it should always be possible to restart from only the ExecPlan and no other work". It is the most explicit first-party design for an artifact that carries reasoning, not just requirements, across a session boundary: the fix for the S05 Journey A failure beat.

## Themes
- process-artifacts-as-coordination: AGENTS.md says when to write an ExecPlan; PLANS.md defines the format; the human reviews the plan before implementation.
- decision-rationale-records: key design decisions go in the Decision Log with reasoning, dated with author; every revision noted at the bottom with why.
- relay-information-loss: "Every ExecPlan must be fully self-contained"; restartability from the plan alone is the design rule.

## Key points
- Who decides the next step: the implementing agent; it proceeds to the next milestone without asking for next steps, resolves ambiguities itself and commits often.
- Human role: reviews the approach up front; customises required sections.
- Record type: prose with mandatory sections, not a schema.
- Cookbook marks the recipe archived and naming an older model; a similar PLANS.md reportedly kept Codex working more than seven hours from one prompt (first-party claim, no method).

## Could not verify
- Exact publish date (search says the PR landed October 2025). Model-summarised fetch.

## Added by research-sdd-ready-intent (2026-11-01)
Raw article re-read from [the cookbook repository](https://raw.githubusercontent.com/openai/openai-cookbook/main/articles/codex_exec_plans.md) (verbatim).
- sdd-input-contracts: the skeleton's sections are Purpose / Big Picture; Progress (checkboxes, the only place lists are allowed); Surprises & Discoveries; Decision Log; Outcomes & Retrospective; Context and Orientation; Plan of Work; Concrete Steps; Validation and Acceptance; Idempotence and Recovery; Artifacts and Notes; **Interfaces and Dependencies** ("Name the libraries, modules, and services to use and why").
- The plan must be self-contained: "Do not point to external blogs or docs; if knowledge is required, embed it in the plan itself in your own words." For enterprise requirements this means an ExecPlan cannot cite a policy by link alone; the obligation and its fit criterion must be restated in the plan.
- "Every ExecPlan must produce a demonstrably working behavior, not merely code changes to 'meet a definition'"; milestones are each "independently verifiable".
- Format: one fenced Markdown block; "Write in plain prose. Prefer sentences over lists." No requirement identifiers, no requirement notation and no blocked state; an outside dependency would be written as prose in Context, Interfaces and Dependencies, or Surprises.
