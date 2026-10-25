---
title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
source_url: https://arxiv.org/abs/2310.03714
author: Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, Christopher Potts
publisher: arXiv (ICLR 2024)
published: 2023-10-05
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
The programming-model statement that prompts should be compiled against a metric rather than hand-written: modules declare what they do, and an optimiser bootstraps demonstrations (exemplars) and instructions until the eval score rises. Two things transfer to PM skills: the stance that the eval, not the prose, is the durable artifact (which Anthropic's skill-creator article later echoes), and the result that bootstrapped exemplars beat expert-written ones, which bears on the exemplar rung of dimension 3.

## Themes
- skill-improvement-loops: pipelines as "text transformation graphs" whose modules "learn (by creating and collecting demonstrations)"; a compiler optimises to a metric; gains over standard few-shot prompting of over 25% (GPT-3.5) and 65% (llama2-13b-chat) (abstract).
- evals-autonomy-trust: versus pipelines with expert-created demonstrations, gains of 5-46% and 16-40%; compiled 770M T5 and llama2-13b programs competitive with expert-written GPT-3.5 chains (abstract).

## Key points
- Existing pipelines rely on "hard-coded prompt templates" found by trial and error; DSPy's position is to replace them with optimised modules.
- Requires a metric and a training set; the metric is the encoding of the standard.
- Abstract-only read.
