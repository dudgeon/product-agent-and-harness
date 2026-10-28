---
title: "Accounting Versus Physics – Rewiring Organizations for Improvement"
source_url: https://itrevolution.com/articles/accounting-versus-physics-rewiring-organizations-for-improvement/
author: Leah Brown (IT Revolution), summarising a DevOps Enterprise Summit talk by Scott Prugh
publisher: IT Revolution
published: 2024-03-07
retrieved: 2026-10-28
type: article
evidence: anecdote
filed_by: research-dependency-agent
themes: [coordination-cost-and-waiting, dependency-types-and-practices, platform-as-a-product]
relevance: high
---

## Relevance to the project
A summary of a widely cited conference talk by Scott Prugh (then CTO at CSG, a billing and customer-communications provider to telecoms; later CTO at a payments company) argues that delivery speed in large enterprises is set by the "physics" of dependencies and handoffs, not by the "accounting" of estimates and utilisation. It supplies the most quotable claims in this space (each dependency halves on-time odds; each handoff loses half the context; 85% of a feature's duration is handoffs, reviews and delayed decisions), but they are a practitioner's model and a single unnamed client case, not measured research, so they must be cited as such.

## Themes
- coordination-cost-and-waiting: "every single dependency chain or additional handoff cuts the chance of on-time delivery in half"; "More coordination equals more delays"; overloaded people context-switch and lengthen queues ("wait time presenteeism") (body).
- dependency-types-and-practices: the remedies are structural: modularise along business domains, move to platform teams, embed capabilities in cross-functional product teams, deliver incrementally, maximise cohesion (body).
- platform-as-a-product: platform teams are named as one of the moves that cut coordination cost (body).

## Key points
- Figures (illustrative, from the talk via the summary; client unnamed): in a feature delivery, 85% of duration was tied up in handoffs, reviews and delayed decisions; a 50% gain in developer throughput would trim only a couple of weeks from an 18-month cycle; after restructuring, lead times fell from months to weeks and escaped defects fell 60%.
- "With each cross-team handoff, transmitted knowledge decreases by 50% as context vanishes." (a heuristic, not a measurement)
- "physics dictates the actual speed and quality outcomes"; accounting still has its place in budgeting and governance.
- Search-result descriptions of the talk video (not read; behind login) frame the halving as a 1/2^N probability model and mention "the golden rule of dependencies" and "three Cs" of coordination cost.

## Could not verify
- The original talk (IT Revolution video library, login required).
