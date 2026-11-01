---
title: "Faithful, Not Corrective: Model Capability Governs Message-Format Effects in Multi-Hop Agent Relays"
source_url: https://arxiv.org/abs/2607.09678
author: Sicheng Zeng
publisher: arXiv (cs.AI)
published: 2026-06-12
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [relay-information-loss, process-artifacts-as-coordination]
relevance: medium
---

## Relevance to the project
A counterweight to "telephone game" claims: with a strong relay model, briefs of twelve facts survived six hops nearly losslessly in every format (hop-6 recall at least 0.973), with residual loss at the first encoding step; with a weak 1.5B relay, format choice mattered a lot. Every format carried an injected error faithfully. For the modules this says a strong-model relay copies well but does not catch mistakes: structure "buys a faithful, error-localizing channel, not an error-correcting code", so verification has to be added, not assumed.

## Themes
- relay-information-loss: strong relay nearly lossless; weak relay across-format dispersion grew 8.7x; injected errors persisted 83-100% in every format.
- process-artifacts-as-coordination: formats tested: free natural language, precision-instructed language, JSON, triples, key-value.

## Key points
- Cognitive load raised generation cost 24-53% with fidelity within ±1.8 points.
- Single-author preprint; v2 2026-09-17.

## Could not verify
- Full paper not read (abstract only).
