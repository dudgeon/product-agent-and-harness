---
title: "PaperBench: Evaluating AI's Ability to Replicate AI Research"
source_url: https://arxiv.org/abs/2504.01848
author: Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, Tejal Patwardhan (OpenAI)
publisher: arXiv / OpenAI
published: 2025-04-02
retrieved: 2026-10-25
type: paper
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [standard-form-spectrum, model-judge-biases, verification-capacity-gap]
relevance: medium
---

## Relevance to the project
A rubric for a long, open-ended piece of work (replicating a research paper) built as a weighted tree whose leaves are pass/fail statements. Partial credit flows up the tree, so an agent gets scored on progress rather than on the single hard outcome. That is a useful shape for PM artifacts, where "did the PRD succeed" is unknowable but "did it name the users, the metric, the non-goals" is checkable. The cost of encoding is stated plainly: each rubric took the paper's own author "multiple weeks", and the model judge reached macro F1 0.83 against human grading at about $66 per paper.

## Themes
- standard-form-spectrum: hierarchical rubric trees, 8,316 leaf nodes across 20 papers, leaves graded 1/0, parents a weighted average; weights set by the authors on importance relative to siblings, not difficulty; leaf types Code Development, Execution, Result Match (section 2.4).
- model-judge-biases: JudgeEval, human-graded leaves as ground truth; o3-mini SimpleJudge F1 0.83 (~$66/paper), o1 0.84 (~$830/paper), GPT-4o 0.73, GPT-4o-mini 0.59 (Table 3).
- verification-capacity-gap: rubric co-development "took multiple weeks per paper" and "many tens of hours of labor" (section 3.1, Appendix C); best agent replication score 21.0% (abstract).

## Key points
- Partial credit rationale: Result Match nodes are very hard, so Execution and Code Development nodes reward partial progress and make scores move incrementally.
- Code-Dev variant grades only code-development leaves, cutting judge cost about 85%, but correlates only weakly with the full benchmark (Pearson r 0.48 for o1).
- First-party: OpenAI grading agents including its own models; rubric construction and judge calibration are the transferable parts.
