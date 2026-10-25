---
title: "Building agents: When to fold subagents into your main agent loop"
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-10-22
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [single-agent-many-skills, one-job-per-agent, harness-over-model, evals-autonomy-trust, skill-standards]
relevance: high
---

## Relevance to the project
Anthropic's Applied AI team argues that in enterprise deployments a single agent loop with progressively disclosed skills and tools frequently beats both a monolithic prompt and an orchestrator with team-owned subagents, on quality and often on cost and latency. That is direct first-party evidence for the single-agent-many-skills side of the strategy's agent-structure choice, and it names the organisational cause of the opposite pattern (agent architecture copying the org chart). It also supplies an ownership model (small central team owns system prompt and end-to-end evals; domain teams own skills and tools with their own evals) and a migration method, though its comparison data is anecdotal and undisclosed.

## Themes
- single-agent-many-skills: "a single agent with skills frequently outperformed both the one-prompt-for-everything design and the subagent design on quality, and often at a lower cost and latency per task" (intro).
- one-job-per-agent: sharpens the counter-case: subagents kept only for measurable context bloat, parallel discardable work, or tool-selection or instruction conflicts; split by context, not by problem type, to avoid a "telephone game" (intro; "Using an agent loop with progressive disclosure").
- harness-over-model: since Opus 4.5 models manage more in one loop; rigid multi-agent structures blocked migrations to newer models; Claude Code's system prompt for advanced models was cut by over 80% (three reasons section).
- evals-autonomy-trust: one shared end-to-end eval set owned centrally plus per-skill evals owned by each team; start with 10 golden examples; check which tasks flipped and run each more than once (section "Task-completion evals"; "Folding subagents").
- skill-standards: per-team DRIs own skills, ship them with evals; /skill-creator and /skill-doctor audit, deduplicate and prune by cost and usage (section "Skills").

## Key points
- Named enterprise failure modes when each team builds its own agent under a central orchestrator: lossy context exchange, subagent sprawl ("hundreds of overlapping subagents with no enforced standards and no specific owner"), the "Frankenprompt" of conflicting team sentences, local evals nobody owns, and latency (one customer saw roughly 2x faster runtime with a single loop).
- Typical over-built designs (intent classifier, fixed pipeline, segment buckets, orchestrator) are said to be replaceable by one clear system prompt, 4-5 thin data tools and firm output guardrails.
- Target design: one model, one context window, open-ended tool loop; harness sets turn and cost budgets and write gates; parallel tool batches; optional goal or verifier check after the answer; the model writes and revises its own plan.
- Placement rules: ordering and domain procedure go into skills; hard limits (validation, approval gates) and per-user permissions go into tools, which return plain refusals the model can read, so "one loop can serve users with different access without a separate agent per permission level"; reference facts go behind lookup tools or skill reference files, not pasted by code.
- Tool guidance: group tools by user intent, not one per API; tool choice degrades past 30-50 definitions in the prompt; use tool search with deferred loading.
- Migration path: build a small end-to-end eval; call surviving subagents as tools (keep full handoff only when the subagent must talk to the user); merge tightly coupled specialists; fold subagents one at a time into skills plus MCP tools and keep a subagent only if the folded version scores worse.
- Worked failure: folding a shipping specialist into a support agent lowered latency but broke a passing process; it showed in one run of two, hence the advice to rerun tasks.
- Org model: "One central team should own end-to-end quality and the system prompt, vetting every new tool and eval before it ships"; teams move from owning agents to owning skills and tools.
- Tooling plugged: /claude-api build-eval, prompt-audit, hillclimb, cost-optimize, and a migration kit with a demo.
- Limits: comparisons are "across several enterprise deployments" with no numbers beyond the 2x latency anecdote; customer agents here are customer-facing, not internal PM agents; the article also sells Anthropic's own skills tooling.

## Notable quotes
- "the agent architecture becoming a copy of their org chart (Conway's law at work)" (intro)
- "measure, change one thing at a time, and keep what holds up" (closing section)

## Could not verify
- The underlying comparison data, sample sizes, and which deployments were compared.
