---
title: "Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains"
source_url: https://arxiv.org/abs/2507.17746
author: Anisha Gunjal, Anthony Wang, Elaine Lau, Vaskar Nath, Yunzhong He, Bing Liu, Sean Hendryx (Scale AI)
publisher: arXiv
published: 2025-07-23
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [standard-form-spectrum, model-judge-biases, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
The clearest statement of what a good rubric is for a model judge, from a group that used rubrics as the training signal for medicine and science answers. Its four design rules (grounded in expert guidance, comprehensive including pitfalls, importance-weighted, each item self-contained) are directly usable as a spec for PM review rubrics. Two findings cut against intuition: rubrics written with a reference answer beat rubrics written without one (so exemplars feed rubrics), and letting the judge read the whole rubric and give one holistic score beat a fixed weighted sum of per-item checks, because hand weights were "brittle".

## Themes
- standard-form-spectrum: checklist-style rubrics with 7-20 self-contained items per prompt, each tagged Essential, Important, Optional or Pitfall; explicit weights 1.0/0.7/0.3/0.9 vs an implicit holistic 1-10 judgment over the same items; implicit won (sections 2.2, 3.2, 4).
- standard-form-spectrum: rubrics generated with reference answers scored 35.9% on HealthBench-1k vs 32.0% without, so "expert signal matters" for writing rubrics (section 4).
- model-judge-biases: structured rubric rewards gave better alignment for smaller judges and reduced variance across judge sizes vs direct Likert scoring (abstract).
- evals-autonomy-trust: relative gains over Likert LLM-judge rewards of up to 31% on HealthBench and 7% on GPQA-Diamond (abstract).

## Key points
- Four rubric desiderata (section 3.1): grounded in expert guidance; comprehensive coverage across accuracy, coherence, completeness, style, safety, including negative pitfall items; criterion importance weighting; self-contained, independently actionable items.
- Generation (section 3.2): an LLM writes rubrics from reference answers standing in for expert supervision (GPT-4o for medicine, o3-mini for science).
- Aggregation (section 2.2): explicit normalised weighted sum vs implicit single judgment; the paper reports RaR-Implicit strongest overall and warns fixed weighted sums "can be brittle".
- HealthBench-1k (Table 1): Reference-Likert 31.7%, RaR-Implicit-Synthetic 35.9%, RaR-Implicit-Human 34.8%.
- Limits named (section 9): medicine and science only; dialogue, tool use and agentic tasks untested; only two aggregation schemes; off-the-shelf judges.
- My reading: the split between explicit checklists and holistic rubric judgment is exactly the checklist-vs-rubric question; here the rubric-as-context-for-judgment form won, but the items themselves were still written as checkable statements.
