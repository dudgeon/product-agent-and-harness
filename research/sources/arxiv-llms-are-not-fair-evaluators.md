---
title: "Large Language Models are not Fair Evaluators"
source_url: https://arxiv.org/abs/2305.17926
author: Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Qi Liu, Tianyu Liu, Zhifang Sui
publisher: arXiv (ACL 2024)
published: 2023-05-29
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [model-judge-biases, human-review-gates]
relevance: medium
---

## Relevance to the project
Shows how badly position bias can swing a pairwise model verdict (a weaker model "beat" ChatGPT on 66 of 80 queries just by going first) and proposes a human-in-the-loop calibration rule that is reusable for PM review: measure how unstable the judge's verdict is across orderings and escalate the unstable cases to a person. That is a concrete mechanism for sloping human review to judge uncertainty.

## Themes
- model-judge-biases: swapping candidate order let Vicuna-13B beat ChatGPT on 66 of 80 queries with ChatGPT as judge; the ranking "can be easily hacked" (abstract).
- human-review-gates: Human-in-the-Loop Calibration uses a "balanced position diversity entropy" to find examples where the judge disagrees with itself across orderings and asks a human only there (section 4).

## Key points
- Three calibrations: Multiple Evidence Calibration (generate several evidence passages before rating), Balanced Position Calibration (aggregate across orders), Human-in-the-Loop Calibration (entropy-triggered escalation).
- Manual win/tie/lose annotation of ChatGPT vs Vicuna-13B on the Vicuna benchmark as ground truth.
