---
title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
source_url: https://arxiv.org/abs/2306.05685
author: Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, Ion Stoica
publisher: arXiv (NeurIPS 2023 Datasets and Benchmarks)
published: 2023-06-09
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [model-judge-biases, standard-form-spectrum, gate-judge-separation, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
The founding measurement of how far a model judge can stand in for a human one, and the first systematic list of its biases. For PM skills that put a model at a quality gate (dimension 2) and encode the standard as a rubric the model applies (dimension 3), this paper gives the baseline: a strong judge agrees with humans about as often as humans agree with each other, but only after position swapping, reasoning and reference answers are built into the judging procedure. It also shows that the form of the standard changes judge accuracy: a reference answer (an exemplar) cut math-grading failures far more than asking the judge to reason.

## Themes
- model-judge-biases: position bias (GPT-4 consistent on only 65% of swapped pairs; Claude-v1 23.8%), verbosity bias (a "repetitive list" attack fooled Claude-v1 and GPT-3.5 91.3% of the time, GPT-4 8.7%), self-enhancement (GPT-4 favoured its own answers about 10 points more than humans; Claude-v1 about 25) and weak math grading (Table 2-4, section 3.3).
- standard-form-spectrum: reference-guided grading (give the judge a correct exemplar) cut math-grading failures from 70% to 15%, against 30% for chain-of-thought alone (Table 4): an exemplar outperformed asking for judgment.
- gate-judge-separation: three judge formats, pairwise comparison, single-answer grading and reference-guided grading, with different failure profiles (section 3.1).
- evals-autonomy-trust: GPT-4 pairwise agreement with expert humans 85% on MT-Bench first turn vs human-human 81%; 87% on Chatbot Arena votes (section 4.2).

## Key points
- Biases (section 3.3): position bias, favouring the first answer in all three judges; verbosity bias; self-enhancement bias; limited capability grading math and reasoning even when the judge could solve the problem itself.
- Mitigations (section 3.4): swap positions and call it a tie if the verdict flips; few-shot judging raised GPT-4 consistency from 65.0% to 77.5% but made calls about 4x more expensive; chain-of-thought and reference-guided judging for math; a fine-tuned Vicuna-13B judge reached 65% position consistency and 85.5% non-tie agreement with humans (GPT-4: 87%).
- Agreement with humans (section 4.2): GPT-4 vs humans 85% (MT-Bench, non-tie), human vs human 81%; the authors argue this is "the same level" as human agreement.
- Released 3K expert votes and 30K crowd conversations.
- Limits (my reading): judges are compared on chat quality, not on long professional documents; the human raters are not domain experts in the PM sense; results are from 2023 models and the bias magnitudes will have moved, although every later survey still lists the same bias families.

## Notable quotes
- "strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans" (abstract).
