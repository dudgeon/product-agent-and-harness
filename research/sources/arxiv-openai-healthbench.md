---
title: "HealthBench: Evaluating Large Language Models Towards Improved Human Health"
source_url: https://arxiv.org/abs/2505.08775
author: Rahul K. Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, Joaquin Quiñonero-Candela, Foivos Tsimpourlas, Michael Sharman, Meghan Shah, Andrea Vallone, Alex Beutel, Johannes Heidecke, Karan Singhal (OpenAI)
publisher: arXiv / OpenAI
published: 2025-05-13
retrieved: 2026-10-25
type: paper
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [standard-form-spectrum, model-judge-biases, tacit-knowledge-capture, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
The largest worked example of encoding expert judgment as per-case rubrics graded by a model: 262 physicians wrote 48,562 criteria for 5,000 conversations, each criterion carrying a weight from -10 to +10, and a model grader checks each one. It is the strongest evidence that expert taste can be decomposed into weighted, checkable statements at scale, and also an honest measure of the ceiling: the model grader agreed with physicians about as well as physicians agreed with each other (both in the 55-75% range), so a rubric does not remove disagreement among experts, it exposes it. The "Consensus" subset, criteria kept only when a majority of reviewing physicians agreed they applied, is a model for how a PM team could separate contested from settled standards.

## Themes
- standard-form-spectrum: each conversation has its own physician-written rubric; criteria have nonzero point values from -10 to +10, negative for undesirable behaviour; score is points earned over maximum possible, per-example scores clipped to [0,1] (section 2).
- tacit-knowledge-capture: physicians from 262 practice settings in 60 countries and 26 specialties wrote the criteria; an expert panel's judgment is captured as text rather than left in heads (section 2).
- model-judge-biases: grader meta-evaluation on 60,896 physician-graded meta-examples; GPT-4.1 macro F1 0.709, o4-mini 0.692, o3 0.681; GPT-4.1 beat the average physician's F1 in five of seven themes; model-physician agreement similar to physician-physician agreement (section 4).
- evals-autonomy-trust: model scores GPT-3.5 Turbo 16%, GPT-4o 32%, o3 60%; HealthBench Hard top score 32% (OpenAI announcement page; the abstract).

## Key points
- Grading: model grader (GPT-4.1 by default) evaluates each criterion independently, full points if met, none if not; sums and normalises.
- HealthBench Consensus: 34 pre-written criteria assigned only when at least two physicians (a majority) judged them relevant; 3,671 examples with at least one positive consensus criterion.
- Seven themes (emergencies, clinical data, global health, and so on) and behavioural axes (accuracy, instruction following, communication).
- Vendor caveat: OpenAI benchmark grading OpenAI models; the physician set and rubric-writing process are first-party.
- My reading: the weights and negative criteria make this a rubric, not a checklist, but each criterion is still phrased as a checkable statement, which is what lets a model grade it reliably; the judgment was spent up front by the physicians, not at grading time.

## Could not verify
- The announcement page (openai.com/index/healthbench) returned 403; headline scores above are from the arXiv abstract and the body section read.
