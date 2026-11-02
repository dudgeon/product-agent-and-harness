---
title: "How to build an AI-native software factory"
source_url: https://www.theaithinker.com/p/how-to-build-an-ai-native-software
author: Adam Faik
publisher: The AI Thinker (Substack)
published: 2026-10-05
retrieved: 2026-11-02
type: article
evidence: independent
filed_by: competitive-teardown-uber-cortana
themes: [agent-factory-sdlc, single-agent-many-skills, one-job-per-agent, cost-control-routing, verification-capacity-gap, human-review-gates, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
The most useful independent synthesis found: it places Cortana in Uber's four agent layers as the single general agent and "front door" (cost unit: cost per query), distinct from specialised agents like Minion (cost per merged PR), and it collects Uber's cost-control history from several sources. It is derivative of Uber's talks and blogs, with the author's own PostHog experiment and competitor comparisons added. Bears on the one-general-agent-plus-specialists question and on per-layer unit costs.

## Themes
- single-agent-many-skills: Cortana is one general agent in Uber's cloud, needs no setup, and can use any skill in the marketplace (Uber section, layer table).
- one-job-per-agent: five specialised agents (Minion, uReview, Agentic XP, Conan AI, Fawkes), each with a person in the loop and its own unit cost.
- cost-control-routing: per-employee, per-coding-tool cap of $1,500/month, later replaced by live spend visibility with nudges at 50%, 80% and 100%; cost per session down 52% from peak (attributed to Uber's efficiency blog).
- verification-capacity-gap: median first review 3 h (2024) → 9 h (2026), from the uReview team; the author's own run on a public repo found a 6.1 h median wait and 40% of PRs merged without human review.
- human-review-gates: PR "hand-off" arrives with a table of passed checks and simulator screenshots; a faster medium model reviews pre-CI, a stronger reasoning model in CI.
- vendor-claims-vs-independent-evidence: 70%+ of PRs "involved" agents (August) vs ~11% of merged PRs (May) are different measures; the author flags that public cases are large firms with platform teams.

## Key points
- Cortana walkthrough as retold: tagged in a Slack thread, checks the context graph for past large-venue events, points to a North America rollout, drafts two Figma mock-ups with different button text, lists reusable screens and backend services; Huda says this alignment used to take weeks. Team channels make answers visible to the team.
- Other Uber facts gathered: context graph 24M nodes from 30+ systems; grounded agent found the right table in 38 s vs 20 min and failure ungrounded; 3,600+ skills; 100+ tools added 50-70k tokens per prompt, so 1,000+ tools became commands; model gateway 800+ projects, 100M+ requests/day; short-lived scoped tokens per hop; AI budget for the year spent in four months by June; 92% monthly agent use by March.
- Uber's other spec tool: uSpec connects a Cursor agent to Figma and writes design-system specs (screen-reader spec for three platforms in under two minutes), from a separate Uber post.
- The intent.md/spec.md/plan.md stage hand-offs in the article are from Anthropic's playbook, not Uber.

## Could not verify
- The article does not mention personas. Several Uber figures are attributed only to "Uber" in the article's source list; not checked against each original.
