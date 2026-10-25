---
title: Define outcomes (Claude Managed Agents docs)
source_url: https://platform.claude.com/docs/en/managed-agents/define-outcomes
author: Anthropic
publisher: Claude Platform docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [gate-judge-separation, evals-autonomy-trust, method-as-harness]
relevance: high
---

## Relevance to the project
A shipped, harness-level model-judgment gate: the caller states an outcome and a markdown rubric, the harness provisions a separate grader in its own context window, and the agent iterates until the grader is satisfied or an iteration cap is hit. This is the clearest vendor primitive for a rubric-gated PM artifact (PRD, spec) and it states the rubric-writing rule that matters: explicit, gradeable criteria.

## Themes
- gate-judge-separation: "the harness automatically provisions a grader to evaluate the artifact against a rubric. The grader uses a separate context window to avoid being influenced by the main agent's implementation choices."
- evals-autonomy-trust: results `satisfied`, `needs_revision`, `max_iterations_reached`, `failed` (rubric contradicts description), `interrupted`; `max_iterations` default 3, max 20.
- method-as-harness: "Structure the rubric as explicit, gradeable criteria ... rather than 'The data looks good.' The grader scores each criterion independently, so vague criteria produce noisy evaluations."

## Key points
- Rubric is required, a markdown document of per-criterion checks (example: DCF model rubric mixing checklist items, e.g. "Projects revenue for at least 5 years forward", with judgment items, e.g. "Growth rate assumptions are explicitly stated and reasonable").
- No rubric? Give Claude a known-good artifact, ask what makes it good, turn that into a rubric ("often produces better results than writing criteria with no example").
- Humans can still steer: `user.message` events mid-outcome; `user.interrupt` pauses. One outcome at a time; outcomes can be chained.
- Grader reasoning is opaque in the event stream (heartbeat only); the end event gives an explanation.
- Beta (`managed-agents-2026-04-01`).

## Could not verify
- No grader accuracy or calibration data; page undated.
