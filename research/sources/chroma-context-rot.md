---
title: "Context Rot: How Increasing Input Tokens Impacts LLM Performance"
source_url: https://www.trychroma.com/research/context-rot
author: Kelly Hong, Anton Troynikov, Jeff Huber (Chroma)
publisher: Chroma research
published: 2025-07-14
retrieved: 2026-10-31
type: report
evidence: independent
filed_by: research-agent-handoff-models
themes: [through-line-context-budget, agent-failure-modes]
relevance: medium
---

## Relevance to the project
The most-cited independent measurement of why a single long-running through-line session degrades: across 18 models, reliability falls as input grows, even on simple tasks, and models did much better on a focused ~300-token prompt than on a full ~113k-token chat history. It is the empirical basis for vendors' compaction, subagents and memory files, and it argues against model B in its naive form (one ever-growing conversation) while supporting model B with records the session re-reads. Chroma sells a retrieval database, but the report is a benchmark study rather than a product claim, so it is labelled independent with that caveat.

## Themes
- through-line-context-budget: LongMemEval: "Models performed much better on short, focused prompts (about 300 tokens) than on full chat histories (about 113k tokens)"; the Claude family showed the largest gap, mostly abstentions under ambiguity.
- agent-failure-modes: one distractor lowers accuracy and four lower it further; performance drops faster when the question and the relevant text share fewer words or meanings.

## Key points
- Models: Claude Opus 4, Sonnet 4, 3.7, 3.5, Haiku 3.5; o3, GPT-4.1 family, GPT-4o, GPT-4 Turbo, GPT-3.5 Turbo; Gemini 2.5 Pro and Flash, 2.0 Flash; Qwen3 235B, 32B, 8B.
- Shuffled haystacks scored better than coherent essays; repeated-words task degraded with length.
- Implication drawn by the authors: needle-in-a-haystack benchmarks overstate real-world reliability; where and how information is placed matters ("context engineering").

## Could not verify
- Results predate 2026 models with 1M windows; no newer replication was read.
