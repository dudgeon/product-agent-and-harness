---
title: Design topics as mini-agents that avoid duplicate messages (Microsoft Copilot Studio guidance)
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-orchestration-topics
author: Microsoft (Karima KT)
publisher: Microsoft Learn
published: 2026-08-27
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [deterministic-scaffold-model-nodes, work-structure-spectrum, gate-judge-separation]
relevance: high
---

## Relevance to the project
Microsoft's design rule for mixing rigid and loose parts inside a model-orchestrated agent: keep deterministic logic and guardrails inside the topic (a fixed island), let the orchestrator handle conversation, inputs and wording. It is the inverse of Stripe's blueprint (model nodes inside a code-fixed flow): here code nodes sit inside a model-chosen flow. Both converge on "deterministic where a rule must hold, generative where talk and interpretation happen".

## Themes
- deterministic-scaffold-model-nodes: "keep deterministic logic inside the topic and leave user communication to the orchestration layer" (Tip, intro); "Keep the logic and the guardrails in the topic" (section).
- gate-judge-separation: entities, validation and Power Fx "act as deterministic checks" that can stop an input being filled or a topic acting; "Deterministic input checks are as reliable as code, so business rules and compliance constraints are respected even when the rest of the plan is generated" (§Collect inputs).

## Key points
- A topic with a description, typed inputs and outputs behaves like a mini-agent the planner calls like a tool.
- Input descriptions are prompts to the orchestrator (how to interpret, constrain or format a value); entities fix the allowed type and range.
- Return results as outputs (`answered`, `choiceReceived`, `messageSummary`); a topic that returns no outputs "is a red flag" and the most common cause of duplicate messages. Newer models also need a top-level instruction to check outputs, which shows prompt and code co-evolving with the model.

## Could not verify
- Guidance only; no measured reduction in duplicate messages or rule violations.
