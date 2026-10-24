---
title: "Designing Experimentation Guardrails"
source_url: https://medium.com/airbnb-engineering/designing-experimentation-guardrails-ed6a976ec669
author: Tatiana Xifara, Reid Andersen, Kathy Yang, Ali Rauh (Airbnb)
publisher: The Airbnb Tech Blog (Medium)
published: 2021-01-27
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [risk-sloped-review, human-review-gates, certified-metrics-layer, svpg-four-risks]
relevance: medium
---

## Relevance to the project
A concrete, quantified review gate at Airbnb's release step: a company-wide system (since 2019) that blocks an experiment from launching without escalation if it hurts a protected metric or is underpowered. About 25 experiments a month are escalated and about 5 are stopped. For the project it is a working example of review sloped to risk and of automated pre-launch checks that route only exceptions to humans, which is the pattern an agent review harness would copy. It also shows that, despite Chesky's 2023 rhetoric, Airbnb ran "thousands" of experiments a week.

## Themes
- risk-sloped-review: three guardrails (Impact: effect not worse than threshold t; Power: standard error below 0.8t; Stat Sig Negative for top metrics like revenue) and coverage-adjusted thresholds; auto-approval carve-outs (non-inferiority pass for positive point estimates).
- human-review-gates: triggered experiments go to "an escalation process... where stakeholders can discuss the results transparently"; "roughly 25 experiments per month for escalation/review. Of these 80% eventually launch... and 20% (5 per month) are stopped" (Airbnb, Jan 2021).
- certified-metrics-layer: guardrail metrics fall into business/financial, user-experience, and strategic-priority categories; warns that more guardrails add friction (50 metrics at 0.05 gives a false alert 92% of the time in an A/A test).
- svpg-four-risks: guardrails protect against one team's win harming another team's metric (example: hiding house rules at checkout raises bookings but lowers ratings).

## Key points
- Scale: "thousands of online experiments run concurrently" each week, "tens of metrics per experiment" (Airbnb, Jan 2021, pre-dating the 2023 public comments).
- Setting each metric's escalation parameter T is "as much an art as it is a science"; backtest against six months of launches to tune.
- Requiring escalations "slows down the speed at which you iterate"; balance protection and speed.

## Could not verify
- Whether the guardrails system and experiment volume survived the post-2020 shift is not stated in any later source found.
