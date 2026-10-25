---
title: "Prometheus: Inducing Fine-grained Evaluation Capability in Language Models"
source_url: https://arxiv.org/abs/2310.08491
author: Seungone Kim, Jamin Shin, Yejin Cho, Joel Jang, Shayne Longpre, Hwaran Lee, Sangdoo Yun, Seongjin Shin, Sungdong Kim, James Thorne, Minjoon Seo
publisher: arXiv (ICLR 2024)
published: 2023-10-12
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [standard-form-spectrum, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Evidence that a model judge works best when handed both a fine-grained score rubric and a reference answer: the two forms of standard (rubric and exemplar) are complements, not alternatives. For PM skills it suggests the strongest encoding of "what a good PRD section looks like" is a rubric with score descriptors plus a worked exemplar, and that custom criteria (the team's own, such as "readable by a new hire") can be evaluated without a proprietary judge.

## Themes
- standard-form-spectrum: a 13B open evaluator trained on 1K fine-grained rubrics and 100K pieces of feedback performs best "when given a reference answer and a score rubric"; with 45 customised rubrics its Pearson correlation with human evaluators was 0.897 vs GPT-4 0.882 and ChatGPT 0.392 (abstract).
- evals-autonomy-trust: the stated motivation is that closed judges are unreliable for large-scale, custom-criteria evaluation (versioning, cost), so the standard must be owned and runnable by the team (abstract).

## Key points
- Feedback Collection: 1K score rubrics, 20K instructions, 100K responses with GPT-4-written feedback.
- Rubrics are user-defined, e.g. child-readability; the paper's claim is tailored evaluation at low cost.
- Across 1,222 custom rubrics on four benchmarks the correlation with GPT-4 showed similar trends; highest accuracy among open reward models on two human-preference benchmarks.
- Limit (my reading): correlations are with raters applying the same rubric; nothing here says the rubric captured what experts actually value.
