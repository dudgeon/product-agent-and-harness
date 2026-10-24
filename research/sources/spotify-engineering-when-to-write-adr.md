---
title: "When Should I Write an Architecture Decision Record"
source_url: https://engineering.atspotify.com/2020/04/when-should-i-write-an-architecture-decision-record
author: Josef Blake (Spotify)
publisher: Spotify Engineering
published: 2020-04-14
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [decision-rationale-records, docs-as-code-prd, compounding-context-repo, tacit-knowledge-capture]
relevance: medium
---

## Relevance to the project
Shows how one Spotify team (the Creator team) records engineering decisions: RFCs to debate big changes, then ADRs to record the outcome, with ADRs also used to backfill undocumented standards found in code review. The stated payoffs are onboarding, ownership handover after reorgs, and cross-office alignment. For the project it is a concrete case of decision rationale being kept as a durable artifact so context survives team changes, though only "a handful of teams" did this in 2020.

## Themes
- decision-rationale-records (proposed): flow is RFC for a big change, then ADR once the RFC concludes; small decisions go straight to an ADR ("Proposing large changes", "Proposing small/no changes").
- compounding-context-repo: when systems move between teams after reorgs, "a lot of context/knowledge was lost"; new owners now read the ADRs ("Ownership Handover").
- tacit-knowledge-capture: backfill an ADR when review reveals an implicit standard nobody wrote down ("Backfilling decisions").
- docs-as-code-prd: ADRs let Stockholm teams adopt a React Hooks decision written by New York engineers ("Alignment").

## Key points
- "At Spotify, a handful of teams use ADRs" (intro, April 2020).
- Decisions arise from RFCs or biweekly engineering meetings; Spotify also has system design reviews and architecture reviews.
- Rule of thumb: write an ADR "almost always".
- Example: 2019 decision to adopt React Hooks after a small experiment; consequence: no new class components.

## Could not verify
- Full post read. How widespread ADRs or RFCs are at Spotify in 2025-2026 is not stated here; where ADRs are stored (repo, TechDocs) is not stated.
