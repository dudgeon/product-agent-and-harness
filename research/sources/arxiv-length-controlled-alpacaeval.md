---
title: "Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators"
source_url: https://arxiv.org/abs/2404.04475
author: Yann Dubois, Balázs Galambosi, Percy Liang, Tatsunori B. Hashimoto
publisher: arXiv (COLM 2024)
published: 2024-04-06
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [model-judge-biases]
relevance: low
---

## Relevance to the project
The standard fix for verbosity bias: model a judge's preference as a function of length difference and read off the counterfactual verdict at equal length. Relevant because PM drafts graded by a model will otherwise drift longer; the fix is statistical, applied after judging, not a prompt instruction.

## Themes
- model-judge-biases: auto-annotators are documented to prefer longer outputs; a regression that zeroes the length difference raised Spearman correlation with Chatbot Arena from 0.94 to 0.98 and improved robustness to verbosity manipulation (abstract).

## Key points
- Generalised linear model on length difference plus other features; the counterfactual is "what would preferences be if both outputs had the same length".
- No robustness figures on the abstract page.
