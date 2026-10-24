---
title: "Stripe's payment method factory: orchestrating agents for repeated custom integrations"
source_url: https://stripe.dev/blog/stripes-payment-method-factory-orchestrating-agents-for-repeated-custom-integrations
author: David Dunne, Xenofon Vourliotis, Sai Samant (Stripe)
publisher: Stripe Dot Dev Blog
published: 2026-09-30
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [org-learning-loop, work-structure-spectrum, agent-factory-sdlc, human-review-gates, compounding-context-repo, agent-led-intent-shaping]
relevance: medium
---

## Relevance to the project
An engineering (not knowledge-worker) agent system, filed because its mechanisms generalise to repeated structured knowledge work: an **observer agent** reads the implementation agent's transcript to harden reusable prompts; **learning logs, decision logs, transcripts and reviewer comments** feed an agent that proposes prompt updates (some applied in one click via Minions); a planning phase where the agent **interviews the engineer** and writes a shared knowledge base; and the finding that orchestration belongs in code, not an orchestrator LLM. Bears on work-structure, review-and-autonomy, intent-shaping-and-spec and harness-upkeep.

## Themes
- org-learning-loop / compounding-context-repo: 100+ saved prompts kept current by a "continuous knowledge loop" from per-run artifacts (learning logs, decision logs, transcripts, PR review comments); an agent suggests improvements.
- work-structure-spectrum: "although an LLM can orchestrate a workflow, predictable coordination is better implemented in code"; an orchestrator agent was "expensive, slow, and sometimes unreliable" and sometimes did steps itself, eating its context.
- agent-led-intent-shaping: in planning, "the agent interviews the engineer for context on the payment method", exported to a shared knowledge base for implementation agents.
- human-review-gates: one step = one PR; review became the bottleneck; agents testing their own work against provider sandboxes and recorded contracts gives reviewers "the most confidence".
- agent-factory-sdlc: integrations from up to six months to 2-6 weeks; 3 new and 10 migrated integrations; bake-off: vanilla Claude Code ~20 engineer-days vs 4 days with hardened prompts. Copied by the tax and verification teams.

## Key points
- Platform-then-factory framing; the template prompt is payment-method agnostic, built from 125+ past implementations.
- Scaffolding step (5,000+ lines, 100+ files, 15 ordered generators) from about a week to a day.

## Could not verify
- Bake-off is n=1 per arm; Stripe-reported.
