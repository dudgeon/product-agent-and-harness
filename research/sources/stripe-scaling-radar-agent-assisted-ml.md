---
title: "Scaling Radar: Fighting fraud with agent-assisted machine learning"
source_url: https://stripe.dev/blog/scaling-radar-fighting-fraud-with-agent-assisted-machine-learning
author: Ryan Drapeau, Sai Samant (Stripe)
publisher: Stripe Dot Dev Blog
published: 2026-10-19
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [agent-factory-sdlc]
relevance: low
---

## Relevance to the project
Out of scope for knowledge-worker agents (ML engineering), skimmed to rule it in or out: Stripe built tools for agents to investigate missed fraud and run training experiments, contributing to an 8%+ recall gain on the Shield model. Shows the same "give agents tools over existing infra" pattern in data science.

## Themes
- agent-factory-sdlc: agents investigate missed fraud using model explanations and earlier investigations, then test changes to the model.

## Key points
- Training set from ~800M to 11B transactions; epoch 24h to 4.8h.

## Could not verify
- Only the first half (infrastructure) was read closely; the agent-tooling section was not read in detail.
