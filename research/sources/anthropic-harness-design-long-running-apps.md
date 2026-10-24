---
title: Harness design for long-running application development
source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
author: Prithvi Rajasekaran (Anthropic Labs)
publisher: Anthropic Engineering
published: 2026-03-24
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-over-model, cost-control-routing, build-vs-buy]
relevance: high
---

## Relevance to the project
Gives rare cost-of-harness numbers: the same task cost $9 solo vs $200 with a planner-generator-evaluator harness, and shows a harness component (sprints) being removed when the model improved. Evidence both for harness value and for harness maintenance churn.

## Themes
- cost-control-routing: solo Opus 4.5 run 20 min / $9; full harness 6 h / $200 (over 20x); updated harness on Opus 4.6 about 4 h / $124.70.
- harness-over-model: every component encodes an assumption about what the model cannot do; sprint construct removed with Opus 4.6, planner and evaluator kept.
- build-vs-buy: cites "find the simplest solution possible" from Building Effective Agents.

## Key points
- Planner expands prompt to spec; generator builds; evaluator tests with Playwright and grades against criteria.
- Stress-test harness components on each model release.

## Notable quotes
- "every component in a harness encodes an assumption about what the model can't do on its own"
