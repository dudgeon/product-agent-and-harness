---
title: "Migrating the payments network, twice"
source_url: https://americanexpress.io/migrating-the-payments-network-twice/
author: American Express engineering
publisher: americanexpress.io
published: 2026-03-12
retrieved: 2026-11-22
type: article
evidence: first-party
filed_by: research-future-of-product
themes: [evals-autonomy-trust, deterministic-scaffold-model-nodes]
relevance: medium
---

## Relevance to the project
A first-party account of replacing a card authorisation platform with shadow traffic then canary routing at 1%, 5%, 10%. It shows how simulation fidelity is actually obtained in payments: replaying live traffic to a production instance of the new system finds logic discrepancies, but performance and environment differences were found by load and resilience tests, and the last check was live canary with rollback.

## Themes
- evals-autonomy-trust: validation ladder in payments: connection migration, shadow traffic, canary; rollback as a first-class capability; shadow traffic retained for ongoing validation

## Key points
- Stage 1 forwarded all traffic unparsed to legacy; stage 2 replayed a copy of live traffic to a dedicated production instance of the new platform; stage 3 routed 1%, 5% then 10% of live traffic with automatic revert on anomaly.
- Shadow traffic surfaced unknown discrepancies between legacy and new logic but did not replace unit and functional testing.
- Second migration rebuilt the Kubernetes environment as infrastructure-as-code from exported production config; load and failure tests compared to a baseline.
- Lessons: traffic control, rollback, observability, patience; no latency, defect or timeline figures given.

## Could not verify
- Almost no quantitative results published; what shadow traffic caught versus missed is partly inferred from structure.
