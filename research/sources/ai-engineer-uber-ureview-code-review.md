---
title: "Building uReview, Uber's Multi-Agent Code Review Engine"
source_url: https://www.youtube.com/watch?v=EL123UNokkI
author: Will Bond and Ameya Ketkar (Uber)
publisher: AI Engineer (YouTube; AI Engineer World's Fair 2026); talk page and transcript at ai.engineer
published: 2026-08-28
retrieved: 2026-11-02
type: video
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [verification-capacity-gap, human-review-gates, risk-sloped-review, skill-improvement-loops, rules-vs-judgment-encoding, ownership-inference, outcome-measurement-gap, cost-control-routing]
relevance: medium
---

## Relevance to the project
The companion talk to Uber's software-factory session: the review stage that sits between Minion's draft PR and merge. Its useful lessons for a PM-agent harness are general: writing a team skill is easy, running it consistently and cheaply at scale is the hard part; customisations live next to the code and route by the existing ownership model; and an agent-facing reviewer needs higher accuracy than a human-facing one, or the agent thrashes. Bears on how team-owned rules plug into a shared platform, and on review as the new bottleneck.

## Themes
- verification-capacity-gap: time to first review rose from within 3 hours (2024) to 9 hours (2026) as PR volume and size grew; review is "the bottleneck" (~0:50-1:15).
- human-review-gates: GitHub, Phabricator and "the agent loop" all send requests to one uReview service; generators run broadly, then post-processing rates, categorises, filters and dedups before an engineer sees anything (~2:57-4:10).
- risk-sloped-review: reviews should account for risk and complexity; review effort varies with change risk (~2:05-2:40).
- rules-vs-judgment-encoding: the model "doesn't know that it's wrong"; teams must supply style guides and anti-patterns; AI linters use few-shot, deterministic context plus rules for mechanical issues (~6:35-8:25).
- ownership-inference: team custom agents and rules are co-located with code and routed deterministically through Uber's ownership model, which picks the model and generator per team (~8:40-8:55).
- skill-improvement-loops: teams asked Claude to derive a review skill from past PR reviews; observability on whether rules are liked is fed back to the owning team (~9:20-9:46).
- outcome-measurement-gap: early measures (cost, NPS, Google Forms, Slack feedback) could not explain quality; moved to reply sentiment, addressal rate and agent trajectories (~4:27-6:10).
- cost-control-routing: ~60% lower cost than a naive implementation, via routing among generators tuned for cost/performance and runtime time budgets (~10:53; mechanisms per talk page).

## Key points
- Context: thousands of engineers, hundreds of teams, 12 sites, six language monorepos; third-party review tools lacked Phabricator support, so Uber built its own (~0:33-1:35).
- Goal for the agentic SDLC: agents in the inner loop get the same rules and review as humans; security and compliance reviews must run everywhere, not depend on teams remembering.
- Review stack: single-file reviewers, multi-file reviewers, deep reviews with per-monorepo anti-pattern guides; AI linters; team-owned custom agents linked to a knowledge base, past PRs and a review skill.
- Results (Uber's claims, ~10:13-10:58): ~25,000 comments a week; ~10% get feedback; ~4% of PRs get negative feedback; ~67% addressal overall; about three quarters of high-severity issues addressed; ~60% cost reduction and ~70% accuracy gain vs a naive build (the talk page notes the accuracy metric is undefined).
- Inner vs outer loop (~12:20-14:00): inner-loop accuracy must be higher or agents fix, re-review and revert; agents "will happily fix a hundred nits"; human feedback still tunes prompts; engineers shift to architecture, domain expertise and product thinking.

## Could not verify
- YouTube auto-captions could not be downloaded (rate-limited); content is from the ai.engineer talk page summary and its transcript endpoint, read through a summarising fetch, so timestamps are approximate and there are no verbatim quotes. Talk page resource date is 2026-08-28; the exact upload date is unconfirmed.
- The talk does not mention Cortana or Minion by name ("the agent loop" only).
