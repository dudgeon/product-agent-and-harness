---
title: "Jev for beginners: how to use it and what to build"
source_url: https://www.lennysnewsletter.com/p/jev-for-beginners-how-to-use-it-and
author: Claire Vo (host; founder of ChatPRD)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-09-28
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [feedback-triage-agents, research-synthesis-agents, cost-control-routing, risk-review-as-classification, metrics-review-agents, outcome-measurement-gap]
relevance: medium
---

## Relevance to the project
Vo shows a cheap "decision model" (Jev, from TypeSafe AI) that returns typed values (a choice, a score, a probability) instead of text, and pairs it with larger models in a pipeline: the small model tags, clusters and filters at volume, a "brainy" model analyses the clusters, a generator writes. Her biggest example is ChatPRD's product insights graph: about 1,100 signals (PRs, support tickets, meeting notes, Linear tickets) and over 200,000 classifications and pairwise groupings for roughly $4 on the classification side, showing the gap between what customers ask for and what the team is working on. That is direct evidence for feedback and research synthesis at scale and for model routing inside a harness. It also shows a measurement idea: classify your own agent sessions and PRs to see where effort actually goes. Bears on context-and-memory, governance-control-plane (cost) and pm-agent-evaluation.

## Themes
- feedback-triage-agents / research-synthesis-agents: ChatPRD insights graph, ~1,100 raw signals from PRs, support tickets, Granola conversations and Linear tickets; extract labels, assign with Jev, analyse clusters with a larger model; output is trends over time and the gap between "what are customers telling us they want" and "what are we actually working on" (14:30-16:53).
- cost-control-routing: three tiers: Jev for classification, clustering and mapping; a reasoning model ("Astra") for analysis and insight; a generation model for writing (15:22). Jev pricing: 4 cents per million input tokens, no output charge (3:06). Vo says prior frontier-only attempts cost "thousands ... if not tens of thousands of dollars" (13:44).
- metrics-review-agents / outcome-measurement-gap: 1,700 ChatPRD PRs categorised by pairwise relatedness then labelled by Gemini Flash-Lite, for 9 cents in about two minutes; ~30% of PRs were platform security and infrastructure (9:11-10:43). She pitches this to CTOs and CPOs who are asked "what percentage of work is going on to what initiatives".
- risk-review-as-classification: score primitive for bug severity (cosmetic, broken, blocking) and routing ("smart if statements") (4:36-6:09).

## Key points
- Primitives: choice (pick from a list), score (e.g. 1-5 severity), and a probability-of-yes value (6:09).
- Pattern: "Jev alone is okay. Jev with an LLM buddy is super powerful": tag, cluster and filter a large corpus, then apply precise model actions only to the clusters that matter (12:14-13:44).
- Meta-analysis of her local Claude Code and Codex sessions: in January almost all her sessions were engineering; by September under ~40% were, with more agent work, media publishing and client delivery (11:12-12:14).
- Gmail triage: score deletability from subject and snippet, then have another model work the remaining clusters (12:14).
- Audience dashboard: ~4,500 YouTube comments classified by sentiment and "contains an episode idea" (58 found), with live search; real-time performance needed batching and scoring architecture, not just "slap Jev in the middle" (18:24-21:29).
- Vo says ChatPRD's insights feature became "more margin accretive" because of the routing (16:53).

## Notable quotes
- "Jev alone is okay. Jev with an LLM buddy is super powerful." (12:14)

## Could not verify
- Full transcript read (short episode, single speaker labelled SPEAKER_00).
- All cost and accuracy figures are Vo's own; she asserts the PR categorisation "is accurate" without a stated check. No evaluation of classification quality is shown.
- Jev was "currently free" on Vercel's AI gateway at recording, so real costs are list-price estimates.
- Model names (Jev, Astra, Soul, Luna) are products of the time; their capabilities are not independently checked here.
