---
title: "When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings"
source_url: https://arxiv.org/abs/2407.04503
author: Jérémy Perez, Grgur Kovač, Corentin Léger, Cédric Colas, Gaia Molinaro, Maxime Derex, Pierre-Yves Oudeyer, Clément Moulin-Frier
publisher: arXiv (ICLR 2025 poster)
published: 2024-07-05
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [relay-information-loss]
relevance: low
---

## Relevance to the project
Peer-reviewed (ICLR 2025) transmission-chain study: passing text through successive LLM agents drifts it toward "attractor" states, more so under open-ended instructions. For a multi-stage relay of product artifacts, it suggests drift is not random noise but a pull toward the model's defaults, which matters when enterprise obligations are the unusual, non-default content.

## Themes
- relay-information-loss: "Small biases, negligible at the single output level, risk being amplified in iterated interactions" (abstract); open-ended instructions (take inspiration, continue) produce stronger attraction than rephrase.

## Key points
- Transmission-chain design from cultural evolution research; tracks toxicity, positivity, difficulty, length across chains; varies initial text, instruction, model, size.
- Finding: more open-ended instructions give stronger attractor effects; toxicity is a stronger attractor than length.
- My reading: in a relay, tightly scoped "transform this into that schema" steps should drift less than "draft the next document from this one".

## Could not verify
- Only the abstract page was read (v4, 2026-01-29); effect sizes not checked.
