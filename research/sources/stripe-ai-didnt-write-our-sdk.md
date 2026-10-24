---
title: "AI didn't write our SDK. It changed how we built it."
source_url: https://stripe.dev/blog/ai-didnt-write-our-sdk-it-changed-how-we-built-it
author: Mike North (Stripe)
publisher: Stripe Dot Dev Blog
published: 2026-08-28
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [spec-becomes-prototype-and-evals, agent-ready-intent, tacit-knowledge-capture, human-review-gates, human-judgment-pm-jobs]
relevance: medium
---

## Relevance to the project
A Stripe platform team's account of AI across the extensibility SDK: a two-day prototype that moved a prioritisation decision weeks earlier; **spec-first delegation** (agent drafts a spec, the team reviews it as a GitHub issue, then implementation), used for ~20 ESLint rules; and **repository-local documentation written for AI consumption** (principles, boundaries, anti-patterns) that also cut onboarding for humans. Evidence for intent-shaping and for capturing architectural tacit knowledge as persistent agent guidance.

## Themes
- spec-becomes-prototype-and-evals: one engineer built a working prototype with demo and docs in about two days (vs 2-3 weeks); it "convinced us to reprioritize the feature into scope for our next major launch".
- agent-ready-intent: five-step workflow; specs define rule name, purpose, spec reference, severity, auto-fix, valid/invalid examples; spec review caught design issues earlier than code review would.
- tacit-knowledge-capture: "We invested in repository-local documentation written for AI consumption - architectural principles, boundary definitions, known anti-patterns ... The documentation that helped agents helped humans too."
- human-judgment-pm-jobs: "AI did not replace architectural judgment ... It could make plausible architectural claims that were subtly wrong."
- human-review-gates: "The more AI amplified output volume, the more important review discipline became."

## Key points
- Feedback turnaround same-day vs 2-3 days each near the deadline.

## Could not verify
- Stripe-reported; no counts beyond ~20 rules.
