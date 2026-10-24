---
title: "Gustav Söderström - How Spotify Thinks [Invest Like the Best, EP.424]"
source_url: https://colossus.com/episode/how-spotify-thinks/
author: Patrick O'Shaughnessy (host), Gustav Söderström (co-president, CPO and CTO, Spotify)
publisher: Invest Like the Best (Colossus)
published: 2025-05-20
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [bets-and-planning-cadence, autonomy-alignment-placement, decision-rationale-records, non-engineer-builders, legible-org-for-agents, prototyping-agents-limits]
relevance: high
---

## Relevance to the project
The most detailed recent first-party account of how Spotify decides what to build: about 14 VPs pitch bets every six months "as if we were a VC and they were a startup", the two co-presidents produce one global stack rank (44 bets this cycle; usually 30-50), and teams staff from the top down. It is preceded by a prototyping phase and run week to week by a three-hour Tuesday "E-Team". He also says non-developers now use Cursor with MCP-wrapped internal services, and that his "biggest job to enable AI" is exposing data through APIs. This bears directly on where intent is set, how it is recorded, and what agents need to see.

## Themes
- bets-and-planning-cadence (proposed): six-month bets cycle; ~14 VPs pitch; co-presidents (Söderström and Norström) stack-rank; 44 bets this cycle, 30-50 typical, roughly 30 committed; teams resource from the top down using their own people first, then limited cross-org moves (~16:26-23:20, ~26:50-32:08). Six months because a year is too slow and a quarter has too much planning overhead.
- autonomy-alignment-placement (proposed): bottom-up ideas from VPs plus top-down synchronisation; company is "completely synchronized for good and bad"; "good at doing global changes" but slower at trying things (~26:50).
- decision-rationale-records (proposed): E-Team (execution team) meets three hours every Tuesday; aim that nobody is blocked more than ~2.5 days; no "take it offline"; VPs may not bring direct reports, so they must know details themselves (~23:20). Longer-range questions go to small expert focus groups that report back.
- prototyping-agents-limits: in the six months before a cycle, teams prototype what Spotify could look like in Figma and increasingly with generative AI tools, to surface conflicts between bets before commitment (~16:26).
- non-engineer-builders: PMs and designers use Cursor; screenshot a screen, have Cursor build a clickable prototype, then connect it to live services via MCP (~32:08-36:29).
- legible-org-for-agents: the bottleneck is "old school engineering": exposing years of play history and other data via real-time APIs so AI tools can use them (~32:08).

## Key points
- Org (~26:50): platform org (cloud, dev tools, security), experience org (consumer app across devices), personalization org (AI, recommendations, balancing content types), plus business verticals (music, podcasts, books).
- Strategy tools (~15:39-16:26): Hamilton Helmer's 7 Powers as shared vocabulary; Socratic debate sessions with his leadership team, extended to the VP and director layer; "discussion is cheap" so debate before committing resources; wants an explanation for why something works, even after a positive A/B test.
- Planning is "the main risk"; Spotify built its own planning tooling because outside tools fell short (~26:50-32:08).
- AI productivity (~05:55, ~38:31): coding is a small share of developer time; expects bigger gains in refactoring, automated review, communication, planning, prototyping; cites studies of ~7% developer speedup as current reality (May 2025), expects more once workflows change. Warns against overfitting to current tools; prompt and prototype sharing is informal and "hacky" (~36:29-40:05).
- Expects specialised AI interfaces per function (licensing, product) trained on company data.

## Notable quotes
- "as if we were a VC and they were a startup" (~16:26, on VP bet pitches)
- "You have to be on top of it enough to explain it yourself" (~23:20, on E-Team)

## Could not verify
- The Colossus transcript is behind a login. Content was read through a third-party AI transcript page (pod.wave.co) via WebFetch summaries, not verbatim; timestamps are that page's segment markers. Treat numbers (14 VPs, 44 bets, 2.5 days) as the guest's claims reported via a machine transcript.
- The final ~20% of the transcript (after ~40:00: free tier, music industry, podcasts, audiobooks) was not read.
