---
title: "Automating the Detection of Requirement Dependencies Using Large Language Models"
source_url: https://arxiv.org/abs/2602.22456
author: Ikram Darif, Feifei Niu, Manel Abdellatif, Lionel C. Briand, Ramesh S, Arun Adiththan (University of Ottawa, ÉTS Montreal, General Motors)
publisher: arXiv
published: 2026-02-25
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [dependency-detection-automation, ai-synthesis-hallucination-risk, human-review-gates]
relevance: high
---
## Relevance to the project
The clearest 2026 evidence on LLMs finding dependencies in specification text: LEREDD (few-shot in-context learning plus retrieval over the spec) labels requirement pairs as Requires, Implements, Conflicts, Details, Is similar or no dependency, reaching about 86-87% overall F1/accuracy on 813 hand-labelled automotive requirement pairs. Two findings matter for a dependency agent: zero-shot models "typically over-predict dependencies" (false blocked-by links), and fine-grained dependency types are much harder than "is there a dependency at all". Even human annotators only agreed moderately (kappa 0.43).

## Themes
- dependency-detection-automation: zero-shot GPT-5.4 overall F1 0.78, but only 0.29 average F1 on specific dependency types; LEREDD with six retrieved examples per type reaches Requires F1 0.86 in the pilot, about 86% F1 and 87% accuracy overall, with only a 2.27% drop when moved to a new system (RQ1-RQ5).
- ai-synthesis-hallucination-risk: "zero-shot models typically over-predict dependencies" (RQ1 answer); the model returns a rationale and confidence score, and predictions with confidence 4 or lower are re-labelled no-dependency as the main filter against unreliable claims.
- human-review-gates: two annotators reached only Cohen's kappa 0.43 before consensus, so "ground truth" for dependencies is itself a judgment call; rationales are offered as the reviewer's aid.

## Key points
- Data: three automotive SRS documents (40, 25 and 50 requirements) from a university course; class imbalance is severe (620 no-dependency vs 116 Requires, 37 Implements, 18 Details, 15 Conflicts, 7 Is similar), so minority-class F1 is unstable.
- Retrieval over the spec (RAG) added little over few-shot examples within a dataset.
- Baselines: TF-IDF/LSA retrieval and fine-tuned BERT; LEREDD reports large relative gains on Requires.
- Small, clean, single-domain specs: far from the cross-team, cross-system dependencies of a regulated enterprise.

## Could not verify
- The threats-to-validity section (the page was truncated) and a peer-reviewed venue.
