---
title: "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning"
source_url: https://arxiv.org/abs/2507.19457
author: Lakshya A. Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J. Ryan, Meng Jiang, Christopher Potts, Koushik Sen, Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab
publisher: arXiv (ICLR 2026 oral)
published: 2025-07-25
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Eval-driven skill improvement done by a program: GEPA reads full trajectories (reasoning, tool calls, outputs), writes a natural-language diagnosis, proposes prompt edits and keeps a Pareto set of candidates scored against an eval. Its claim that language feedback is a richer learning signal than scalar reward is the research version of Warp's "the explanation of why is what makes feedback usable". It needs an eval metric, so it belongs to the eval-driven rung of the improvement loop, not the self-rewriting one.

## Themes
- skill-improvement-loops: samples trajectories, "reflects on them in natural language to diagnose problems, propose and test prompt updates" and combines lessons across a Pareto frontier; beats GRPO by 6% on average and up to 20% with up to 35x fewer rollouts; beats MIPROv2 by over 10% (abstract).
- evals-autonomy-trust: the optimiser is driven by a scored eval set; the quality of the resulting prompt is bounded by the eval (my reading).

## Key points
- Framed as sample-efficient alternative to RL for compound AI systems.
- +12% on AIME-2025 over MIPROv2 stated.
- Abstract-only read.
