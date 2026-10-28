---
title: "Google DORA issues platform engineering caveats"
source_url: https://www.techtarget.com/searchITOperations/news/366615375/Google-DORA-issues-platform-engineering-caveats
author: Beth Pariseau
publisher: TechTarget (SearchITOperations)
published: 2024-11-07
retrieved: 2026-10-28
type: article
evidence: independent
filed_by: research-dependency-agent
themes: [platform-as-a-product, coordination-cost-and-waiting, process-governance-load, cognitive-load-and-platforms]
relevance: high
---

## Relevance to the project
Trade-press report of the 2024 DORA (Accelerate State of DevOps) findings on internal developer platforms: platform users report higher productivity and team performance, but throughput and change stability fall, which DORA attributes partly to the extra checks and handoffs a platform puts between a team and production. It is the clearest numeric evidence that a platform can add coordination cost even while it helps. For a dependency agent, it means "onboard to the platform" is not automatically a win, and the handoffs a platform introduces are themselves dependencies to track.

## Themes
- platform-as-a-product: platform gains follow a J-curve (early gains, a dip, recovery as the platform matures) "provided they listen to developer feedback" (article body, citing the report).
- coordination-cost-and-waiting: throughput fell 8% for platform users; the report notes platforms usually add "handoffs" between systems and teams (article body).
- process-governance-load: the throughput loss is linked to added checks before production.
- cognitive-load-and-platforms: the report's caveat that the gains "do not come without some drawbacks".

## Key points
- Survey base: the 2024 DORA report surveyed roughly 3,000 respondents; report released 22 October 2024 (article).
- Platform users: individual productivity +8%, team performance +10%, overall software delivery and operations performance +6% (article, quoting the report). Evidence: independent research (Google Cloud's DORA programme) reported by independent press.
- Throughput -8% and change stability -14% for platform users; the report calls the stability drop "a surprising result" (article).
- Lower stability in DORA terms means more rework from failed changes.

## Notable quotes
- "Internal developer platform users had 8% higher levels of individual productivity."
- "Throughput and change stability saw decreases of 8% and 14%, respectively, which was a surprising result."

## Could not verify
- Figures were read in the article, not in the report PDF itself; DORA's own 2024 report page (dora.dev/research/2024/dora-report/) states the direction of the effects but gives no numbers on the page.
