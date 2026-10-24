---
title: "CASTLE: training natural language search before the first real query"
source_url: https://airbnb.tech/ai-ml/castle-training-natural-language-search-before-the-first-real-query/
author: Wendy Ran Wei and 11 co-authors (Airbnb)
publisher: The Airbnb Tech Blog (airbnb.tech)
published: 2026-10-13
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [synthetic-users-limits, evals-autonomy-trust, research-synthesis-agents]
relevance: low
---

## Relevance to the project
Shows how Airbnb built its AI (natural-language) search before it had real queries: synthetic queries and labels derived from real booking choices, seeded with about 500 queries gathered in targeted user research. Relevant as a concrete link from user research to model training data, and as a careful case of when synthetic data can stand in for users (grounded in real behaviour) and when it cannot.

## Themes
- synthetic-users-limits: plain LLM query generation drifts far from how guests really search (KL divergence 9.33-26.2 for prior methods); grounding in booked-vs-viewed listing pairs got 1.01 (Airbnb claim); real guests search in short 4-8 word phrases, not long sentences.
- evals-autonomy-trust: three subject experts reviewed 200 sampled triplets and agreed with the generated labels 91-93% of the time; a Virtual Judge labels long-tail pairs where no booking signal exists.
- research-synthesis-agents: about 500 seed queries "collected from targeted user research" ground the generated language, a direct research-to-training handoff.

## Key points
- Method: a guest booking one listing over viewed alternatives gives a (positive, negative) pair; the LLM writes a query the positive satisfies and the negative does not, so the label is right by construction.
- Prompt variants: templates, few-shot from seed queries, attribute-grounded; a variety mechanism prevents "query collapse".
- Paper accepted at CIKM 2026. Next: multi-turn conversational search.
- Context: Chesky said AI search went into testing on a small share of traffic in 2026 (airbnb-earnings-q4-2025, airbnb-earnings-q2-2026).

## Could not verify
- No online (A/B) results for the search product itself are given.
