---
title: Ramp: Lessons from Building a New AI Product - The Pragmatic Summit
source_url: https://www.youtube.com/watch?v=NMs8C2_3M0w
author: Ramp engineers and product staff (speakers: Nick, Viral, Will, Ian; surnames not in captions)
publisher: The Pragmatic Engineer (YouTube)
published: 2026-03-09
retrieved: 2026-10-24
type: video
evidence: first-party
filed_by: competitive-teardown-ramp-glass
themes: [single-agent-many-skills, evals-autonomy-trust, cost-control-routing, non-engineer-builders, legible-org-for-agents]
relevance: high
---

## Relevance to the project

Eight months before Glass's external launch, Ramp engineers describe the infrastructure and agent philosophy Glass sits on: one agent with many skills, a shared tool catalog, an LLM proxy with cost tracing, and the Inspect background coding agent. It does not mention Glass by name, so it is context for the harness, not a Glass source. Strong on evals, autonomy sliders and trust, which bear directly on agent design.

## Themes

- **single-agent-many-skills**: Teams built four versions of the same agent; the lesson is 'a single agent with a thousand skills' instead of a thousand agents; OmniChat consolidated ~5 conversational UXs into one.
- **evals-autonomy-trust**: Policy Agent: start with suggestions, then an autonomy slider (e.g. auto-approve under $200); weekly cross-functional labeling sessions create ground truth; evals started with five examples; 'users are wrong sometimes' so define your own correctness; auditability matters more as the agent becomes a black box.
- **cost-control-routing**: Applied-AI service = LLM proxy with structured outputs across providers, batch handling, per-team/product cost tracing, one-line config model swaps.
- **non-engineer-builders**: One PM vibe-coded ~20 tools; Ramp Inspect (Modal sandbox, multiplayer-first, Slack/Kanban/API triggers) >50% of merged PRs, used by product, design, legal, finance, marketing, CX.
- **legible-org-for-agents**: Internal tool catalog of hundreds of tools, shared across all agents, built with product teams.

## Key points

- Events + prompt + guardrails (policy) + context + tools framing; traditional software only did context and tools.
- Policy Agent evolution: simple LLM chain -> classification + conditional prompting -> full agentic loop with read/write tools; capability and autonomy rise while traceability falls.
- Expense policy doc acts like a CLAUDE.md for finance users, editable with instant feedback.
- Inspect: sandboxed background coding agent, VS Code/VNC, 150k+ tests; Ramp open-sourced the blueprint (builders.ramp.com, 'open inspect' repo, per speaker).
- Culture section: judgment/context matter more than raw coding speed; building the wrong thing faster is the risk.

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify

Speaker surnames are not in the captions. Auto-caption ASR errors: 'Brian'/'Brazilian agents', 'Cloud Code', 'LM'. No mention of Glass.

