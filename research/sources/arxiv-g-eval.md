---
title: "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment"
source_url: https://arxiv.org/abs/2303.16634
author: Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, Chenguang Zhu
publisher: arXiv (EMNLP 2023)
published: 2023-03-29
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [standard-form-spectrum, model-judge-biases, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
The paper that made "give the model a criterion, let it write its own evaluation steps, then fill in a score" the default rubric-grading recipe. It sits in the middle of dimension 3: the human supplies a short criterion (coherence, consistency) and the model expands it into a checklist-like procedure. Its own stated limit, that model evaluators lean toward model-written text, is the first version of the self-preference warning that matters when a PM skill grades drafts the same model wrote.

## Themes
- standard-form-spectrum: a one-line criterion plus auto-generated evaluation steps (a form-filling paradigm) replaces a hand-written rubric; Spearman correlation with humans on summarisation 0.514, which the authors call a large margin over prior metrics (abstract).
- model-judge-biases: the authors flag "bias towards the LLM-generated texts" as a potential issue with LLM evaluators (abstract).

## Key points
- Method: chain-of-thought plus form-filling; the model is given the task description and criterion and generates the intermediate evaluation steps itself.
- Result: with GPT-4, 0.514 Spearman with human judgements on summarisation; the abstract names no other numbers.
- Limitation stated by the authors: evaluators may prefer model-written over human-written text.
- Read from the arXiv abstract page; body details (probability-weighted scoring) not confirmed here.

## Could not verify
- The probability-weighted scoring detail and the SummEval dataset name are not on the abstract page.
