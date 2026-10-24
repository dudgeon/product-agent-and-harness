---
title: "AI steering experiments"
source_url: https://stripe.dev/blog/ai-steering-experiments
author: James Beswick, Peter Epsteen (Stripe)
publisher: Stripe Dot Dev Blog
published: 2026-05-14
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [skill-standards, single-agent-many-skills, enablement-by-product]
relevance: medium
---

## Relevance to the project
External-facing (steering developers' coding agents to use Stripe correctly), but the results are about how agents consume skills and context, which applies to any skill library: modular, progressively disclosed skills beat a monolith by ~10% on Stripe's eval suite and use fewer tokens; passive hints (AGENTS.md in dependencies, API warnings) are ignored; errors and in-path prompts work; distribution, not content, is the bottleneck ("awareness → install → load → follow").

## Themes
- skill-standards: progressive disclosure (top-level skill referencing on-demand sub-skills) outperformed a monolithic skill by roughly 10%; sub-skills can be owned by product teams.
- single-agent-many-skills: "If your guidance wasn't in the loaded context, it didn't happen."
- enablement-by-product: CLI login page prompt to install the skill: 30-35% copied the command; "agent-facing developer experience is a distribution problem, not a content problem".

## Key points
- ~a dozen experiments early 2026: passive hints failed; active prompts and distribution plays worked; hard steers (errors) work, soft steers (warnings) do not.

## Could not verify
- Eval suite details are in a separate post not read here.
