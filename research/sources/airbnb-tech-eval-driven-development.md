---
title: "Eval-driven development: Lessons from evaluating GenAI at scale"
source_url: https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale/
author: Rohit Girme, Dan Miller, Mia Zhao, Lifan Yang, Clint Kelly (Airbnb)
publisher: The Airbnb Tech Blog (airbnb.tech)
published: 2026-07-30
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [evals-autonomy-trust, spec-becomes-prototype-and-evals, human-review-gates, human-judgment-pm-jobs, ai-synthesis-hallucination-risk]
relevance: high
---

## Relevance to the project
Airbnb's house guide to evaluating LLM features (review highlights, AI customer support, smart messaging). It makes evaluation a product activity, not just an ML one: the PM or subject expert labels the golden set, a named human "decision-maker" settles what good means, and a weekly PM review of flagged production outputs feeds new evals. This is direct evidence that in an AI-feature team the PM's intent is expressed as eval criteria and golden examples, which matters for how a harness should capture and carry intent.

## Themes
- evals-autonomy-trust: three layers in order: programmatic checks, LLM-as-judge ("virtual judges"), human evaluation (section 2). Keep 3-5 well-calibrated judges, one per dimension; calibrate to high-80s/90s% agreement on a 50-100 example golden set that must include bad examples (2.2.1).
- spec-becomes-prototype-and-evals: "eval-driven development" as the GenAI version of TDD; it "forces stakeholders to externalize what 'good' means, which shapes the product roadmap" (1.2).
- human-review-gates: production monitoring samples 5% of de-identified live traffic daily, runs checks and judges, and surfaces flagged outputs to humans; weekly PM review closes the loop (section 4, step 4).
- human-judgment-pm-jobs: "Appoint a decision-maker" (a human) for disputed correctness; the product partner regularly answers "Is X better or worse than Y?" (1.2).
- ai-synthesis-hallucination-risk: walkthrough finds 15 of 100 support-policy answers invented policy details; faithfulness judge started at 78% agreement with the PM, reached 88% after rubric fixes (section 4, step 3).

## Key points
- "The one rule": run a prototype through about 100 examples (synthetic is fine), read outputs and traces, categorise mistakes, then build evals (1.1).
- Expect evaluation to take a meaningful share of total project effort (1).
- Start with 20-100 rows labelled by subject experts; move to scaled annotators only when the rubric is solid; if experts disagree, stop and resolve that first (2.4).
- Agent evaluation: judge the trajectory, not only the final answer; reconstruct traces from spans and check sub-agents and tool calls (section 3).
- Iteration method: fix model and vary prompt, then fix prompt and vary model, then vary serving config (note in section 4).
- Privacy: sampled traffic is de-identified and purpose-limited to safety and quality.
- An infrastructure team provides shared tooling; each product team keeps its own criteria.

## Notable quotes
- "The teams that succeed with AI aren't the ones with the best models, they're the ones with the best communication and clearest product vision." (Key takeaways)

## Could not verify
- The walkthrough is described as fictionalised and simplified; no real production metrics are given.
