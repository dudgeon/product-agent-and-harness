---
title: "Can AI Guess What You Know? Performance Comparison of Large Language Models for Human Domain Knowledge Estimation From Communication Logs"
source_url: https://arxiv.org/abs/2605.22971
author: Ko Watanabe, Shoya Ishimaru
publisher: arXiv
published: 2026-05-21
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [tacit-knowledge-capture, ai-synthesis-hallucination-risk]
relevance: medium
---

## Relevance to the project

Tests whether passive mining of Slack can build a "who knows what" map, a precondition for an agent that knows whom to interview. Best-model error was about 21 points on a 0–100 scale against self-ratings, and more messages did not reliably help: feasible but rough, and privacy-sensitive.

## Themes

- **tacit-knowledge-capture**: 27,188 Slack messages from 43 users; seven models zero-shot; best MAE 21.13% (Gemini 2.5 Flash), GPT models "significantly larger discrepancies"; accuracy only weakly tied to message volume (abstract).
- **ai-synthesis-hallucination-risk**: authors stress "the need for privacy-preserving deployments and richer, structure-aware representations of human knowledge" (abstract).

## Key points

- Ground truth is self-reported skill from 27 participants, itself imperfect.

## Could not verify

- Full paper not read (prompts, per-domain errors, statistical tests).
