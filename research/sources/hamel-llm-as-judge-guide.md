---
title: "Using LLM-as-a-Judge For Evaluation: A Complete Guide"
source_url: https://hamel.dev/blog/posts/llm-judge/
author: Hamel Husain
publisher: hamel.dev
published: 2024-10-29
retrieved: 2026-10-25
type: article
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [evals-autonomy-trust, tacit-knowledge-capture, rules-vs-judgment-encoding]
relevance: high
---

## Relevance to the project
Husain's "critique shadowing" method is the most practical public account of how to turn an expert's taste into something a model can apply: one principal domain expert makes binary pass/fail calls with written critiques; the critiques become few-shot examples in the judge prompt; iterate until agreement is high. His key finding for the rigidity question is that criteria cannot be fully specified in advance ("criteria drift"): experts discover their standard while grading. For PM skills that means rubrics should be grown from graded examples, not written up front. Page modified 2026-09-01.

## Themes
- evals-autonomy-trust: binary pass/fail over 1-5 scales because nobody knows what separates a 3 from a 4 and scale scores often fail to track expert judgment; Honeycomb case reached over 90% agreement with the expert in three rounds; report true positive and true negative rates separately.
- tacit-knowledge-capture: critiques must be detailed enough for a new employee; "Being too terse is a common mistake"; the expert, not a developer proxy, defines success.
- rules-vs-judgment-encoding: citing Shankar et al., people define criteria while grading; the Honeycomb expert: "I wasn't being consistent about how I judged certain edge cases"; the judge is a way to "trick people into carefully looking at their data".

## Key points
- Standard form: exemplars with reasons (critiques) beat abstract rubrics; examples should carry the same context the judge will see (user metadata, system state) and be diverse; choose them dynamically where possible.
- Human clarification of the standard is often worth more than the judge itself (author's view).
- Existing notes on Hamel's error analysis: howiai-hamel-husain-error-analysis, lenny-podcast-hamel-shreya-evals.

## Could not verify
- The Shankar et al. paper (likely "Who Validates the Validators?") not read here.
