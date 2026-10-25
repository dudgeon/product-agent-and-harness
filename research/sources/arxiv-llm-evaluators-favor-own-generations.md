---
title: "LLM Evaluators Recognize and Favor Their Own Generations"
source_url: https://arxiv.org/abs/2404.13076
author: Arjun Panickssery, Samuel R. Bowman, Shi Feng
publisher: arXiv (NeurIPS 2024)
published: 2024-04-15
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [model-judge-biases, gate-judge-separation]
relevance: medium
---

## Relevance to the project
The causal study behind the "use a different model to grade than to write" rule. Self-preference tracks self-recognition: models that can tell their own text apart favour it more, and fine-tuning recognition raised preference. For a PM harness this is the argument for separating the drafting agent from the judging agent (gate-judge separation) or at least swapping model families at the gate.

## Themes
- model-judge-biases: GPT-4 and Llama 2 rate their own outputs higher than humans do; a linear correlation between self-recognition capability and self-preference strength after fine-tuning; controlled experiments argue the link is causal (abstract).
- gate-judge-separation: implication (my reading) that the judge should not be the author's model.

## Key points
- Human annotators rated the compared outputs as equal in quality, so the preference is bias not signal.
- Models could distinguish their own outputs from other LLMs' and from humans'.
- No numbers on the abstract page.
