---
title: "LLM as a Broken Telephone: Iterative Generation Distorts Information"
source_url: https://arxiv.org/abs/2502.20258
author: Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, Guokan Shang
publisher: arXiv
published: unknown
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [relay-information-loss, agent-failure-modes]
relevance: medium
---

## Relevance to the project
Measured evidence that re-processing LLM output through a chain of LLM steps loses facts cumulatively, and that constrained prompts and low temperature slow the loss. It bears on model A (finish-to-start relay), where each stage rewrites the previous stage's artifact: the risk grows with the number of rewrites, not the number of reads.

## Themes
- relay-information-loss: "distortion accumulates over time, influenced by language choice and chain complexity" (abstract); factuality (FActScore) falls gradually across up to 100 translate-back iterations.
- agent-failure-modes: mixing models in a chain had mixed effects (worse for French chains, better for Thai); most complex multi-language chains declined fastest.

## Key points
- Setup: English to bridge language and back, up to 100 iterations, BookSum, ScriptBase-alpha and News2024 (150 docs each); Llama-3.1-8B, Mistral-7B, Gemma-2-9B; also a rephrasing task.
- Metrics: BLEU, ROUGE-1, chrF, METEOR, BERTScore; FActScore judged by Claude 3.5 Sonnet.
- Mitigations: "higher temperature settings lead to greater factual and semantic degradation"; "more constrained prompts" preserve relevance and factuality better; near-zero temperature stabilised factuality after the first few iterations.
- Limits: small models only (7-9B), similar datasets, translation as proxy for rewriting.
- Implication (my reading): a relay that re-reads a fixed artifact is safer than one that regenerates it each stage; schema-constrained artifacts are the analogue of "constrained prompts".

## Could not verify
- Retrieved via WebFetch of HTML v2 (revised 2025-09-15); publication venue not stated; v1 date taken from the arXiv ID.
