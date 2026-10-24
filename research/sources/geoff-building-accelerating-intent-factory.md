---
title: Building and Accelerating the Intent Factory
source_url: https://claude.ai/artifact/KD7oCzhwgca9bvr2mq3ADC
author: Geoff Dudgeon (written collaboratively with Claude)
publisher: Claude Docs (private artifact)
published: 2026-09-20
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-product-agent-and-harness
themes: [intent-factory-before-discovery, agent-led-intent-shaping, agent-ready-intent, compounding-context-repo, risk-sloped-review]
relevance: high
---

## Relevance to the project

This is Geoff's own position piece, and it probably sets the frame for "product agent and harness". It defines the *intent factory* (refining intent and delivering it) and argues that it has to be automated before AI can help much with discovery. Its five actions read like a requirements list for a product agent and harness: a shaping skill, agent-ready intent standards, and a context repo. It bears on the open questions of what a product agent does, where the harness boundary sits, and which teardown targets to pick (Stripe and Ramp). Its Stripe and Ramp numbers come from public sources that the doc links; they are second-hand here.

## Themes

- **intent-factory-before-discovery**: §Introduction. Accelerate intent definition and delivery first, then improve problem and solution discovery. Discovery without faster delivery "balloons backlogs".
- **agent-led-intent-shaping**: §Vision, steps 1–3. Agents start the work (Ramp's agent reads 90 days of tickets in about 8 minutes), run parallel research streams that each write to a file, and put a structured interrogation to the PM (Ramp's seven questions, which challenge any requirement that lacks evidence).
- **agent-ready-intent**: §Vision step 4 and Action 3. A short spec tied to evidence, not a PRD. Product and tech agree a completeness standard: templates, examples, evals for delivery-readiness, and a feedback loop.
- **compounding-context-repo**: Action 5. A shared, agent-readable repo that holds "evidence, not yet fact", with a domain owner per topic. Every spec writes its evidence back. The layer is plain text and harness-agnostic.
- **risk-sloped-review**: §Vision step 7. Ramp scores PRs for complexity and auto-approves a double-digit share. Stripe requires human review on every change ("not moving money without human review").

## Key points

- **TL;DR:** product leaders should prioritise automating intent definition and delivery. Stripe and Ramp, both regulated, have largely done so. Most organisations have gaps at nearly every stage, and five concrete actions follow.
- **The eight-step Stripe/Ramp loop (§Vision):**
  1. informal high-level intent, increasingly agent-originated
  2. agent-led research (Stripe's Kai; Ramp's shaping skill)
  3. structured interrogation (Ramp only; at Stripe, people settle it among themselves)
  4. a spec, not a PRD (Stripe builds a Harbor prototype instead)
  5. coding starts once intent is defined, triggered by an emoji, ticket button or automation, with standing requirements held in rule files
  6. self-verification until intent equals execution (tests, telemetry, flags and screenshots; Stripe caps it at two CI rounds)
  7. review sloped to risk
  8. staged release (dogfood, alpha, 10% beta, GA); failures are fixed in the prompt, skill or rule, not the feature
- **Stats cited:**
  - Stripe Minions: more than 1,000 (1,300) merged PRs a week by March 2026, reportedly about 7,000 a week (~30% of merges) by August.
  - Ramp Inspect: 75% of merged PRs by May 2026.
  - Kai: 83% weekly use at Stripe.
  - Harbor: 12,000 prototypes since May 2026.
- **Current-state gaps (§Current State):**
  - refinement is the bottleneck: years of goals but only 1–2 sprints of shovel-ready intent
  - refinement is done bespoke each time
  - context is scattered across private docs and SMEs
  - PRDs are vague
  - refinement happens just in time
  - coding agents are adopted inconsistently
  - SDLC gates are manual
- **Five actions (§Where to begin):**
  1. Make delivery automation a business goal, with KRs. Litmus test: vulnerability and defect remediation should be near-instant.
  2. Put sustained capacity into the software factory, like a "debt snowball". Choose one SDD approach.
  3. Commit to agent-ready intent: a completeness standard, measured as a KR, that gates delivery.
  4. Mechanize shaping with one versioned shaping skill: a standard question set, a named source per question, answers written back, and revisions on a cadence based on how specs perform in delivery.
  5. Build a context architecture that grows with each feature: start with support-channel FAQs; don't wait for orchestration patterns to settle.

## Could not verify

I did not re-check the linked public sources (Stripe dev blog, Ramp builders blog, YouTube talks, Pragmatic Engineer) in this pass. The stats are as the doc states them.
