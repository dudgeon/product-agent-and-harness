---
title: "How Airbnb achieved metric consistency at scale (Part I: Introducing Minerva)"
source_url: https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70
author: Robert Chang and Minerva team (Airbnb)
publisher: The Airbnb Tech Blog (Medium)
published: 2021-04-30
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [certified-metrics-layer, org-context-grounding, legible-org-for-agents, metrics-review-agents, docs-as-code-prd]
relevance: high
---

## Relevance to the project
Minerva is Airbnb's single source of truth for metrics across analytics, executive reporting and A/B testing: metrics and dimensions defined once in a GitHub repo, code-reviewed, catalogued in Dataportal with owners and certification. For the project it is the model of a governed context layer that a metrics or experiment-reading agent would need to sit on; it also shows that disagreeing numbers ("Data Science and Finance would sometimes provide diverging answers" to the CEO) were the trigger. The measurement layer is the part of Airbnb's process that is most structured and most machine-readable.

## Themes
- certified-metrics-layer: "more than 12,000 metrics and 4,000 dimensions in Minerva, with more than 200 data producers" (Airbnb, April 2021); "define metrics once, use them everywhere".
- docs-as-code-prd: metric definitions live "in a centralized Github repository that can be viewed and updated by anyone at the company"; changes go through "code review, static validation, and test runs"; definitions are version-controlled with automatic backfills.
- org-context-grounding / legible-org-for-agents: Dataportal indexes Minerva metrics with "certification status, ownership, and popularity"; Metric Explorer shows owners, landing time and descriptions.
- metrics-review-agents: XRF (eXecutive Reporting Framework) turns chosen Minerva metrics into report-ready time series for weekly, monthly and quarterly business reviews.

## Key points
- History: around 2010 one analyst, his laptop the warehouse; then Airflow (built at Airbnb), `core_data` tables, the experimentation platform, Dataportal (data catalog), Superset, and Data University for non-data staff.
- Pain: derived tables proliferated, lineage impossible, fixes didn't propagate; leaders got different numbers for simple questions; trust "degraded".
- Fix: multi-year warehouse rebuild with certified, normalised tables, then Minerva on top (Airflow, Hive, Spark, Presto, Druid) covering the full metric life cycle including cost attribution, GDPR deletion, access control, auto-deprecation and usage-based retention.
- ERF integration: ERF's own "metrics repo" was replaced so all A/B test base events come from Minerva, aligning experiment results with top-line metrics.
- Python and R clients expose the same numbers in notebooks.
- COVID: a Minerva-based executive dashboard was wireframed and live "in just under a few days", got 11,000+ views from 1,500 viewers, the most viewed Superset dashboard of 2020; insights (local travel, longer stays) led to product page redesigns.

## Could not verify
- Parts II and III of the series (architecture, API, lessons) were not read. Current (2026) status of Minerva is not stated in any source found.
