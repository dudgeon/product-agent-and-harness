---
title: "Building eval systems that improve your AI product (Lenny's Newsletter)"
source_url: https://www.lennysnewsletter.com/p/building-eval-systems-that-improve
author: Hamel Husain and Shreya Shankar (guest post in Lenny's Newsletter)
publisher: Lenny's Newsletter
published: 2025-09-09
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [evals-autonomy-trust, outcome-measurement-gap, human-review-gates, agent-failure-modes, spec-becomes-prototype-and-evals]
relevance: high
---

## Relevance to the project
The most practical method in the library for answering "how would we know a PM agent works": start from error analysis on about 100 real traces judged by one domain expert (often the PM), group critiques into fewer than ten failure modes, then build code checks for objective failures and LLM judges for subjective ones, validated against the expert's labels using true-positive and true-negative rates rather than accuracy. It also gives a way to localise agent failures (a transition failure matrix) and a CI-plus-production flywheel. The claim that people "are not very good at specifying their complete requirements for an AI up front" and discover criteria by reviewing outputs bears directly on intent shaping: criteria emerge from review. Bears on pm-agent-evaluation, review-and-autonomy and intent-shaping-and-spec. The authors sell a course on this method, so it is practitioner opinion, not measured results.

## Themes
- evals-autonomy-trust: trust in a metric comes from measuring the judge against a human-labelled set split train 10-20% / dev 40-45% / test 40-45%, and reporting TPR and TNR, not accuracy; a judge that always says "pass" is 99% accurate on a 99%-pass system (section "Measure what matters").
- outcome-measurement-gap: dashboards of off-the-shelf metrics (hallucination, toxicity) are ignored because they are "disconnected from real user problems"; use them only to sort traces for review (Phase 1, "A warning about off-the-shelf metrics").
- human-review-gates: a single "benevolent dictator" domain expert, often the PM, labels pass/fail with a detailed critique; LLM first-pass clustering is fine but "always have the human expert review" (Phase 1).
- agent-failure-modes: transition failure matrix: rows = last successful step, columns = step where failure occurred; reveals hotspots like executing generated SQL (section "Agentic workflows"). For multi-turn failures, first reproduce in a single turn to separate retrieval gaps from memory loss.
- spec-becomes-prototype-and-evals: "people are not very good at specifying their complete requirements for an AI up front"; criteria emerge while reviewing outputs, and judge alignment refines your own standard ("criteria drift") (Phase 1, Phase 2).

## Key points
- Phase 1, error analysis: ~100 randomly sampled interactions; open coding (free-form critique plus pass/fail, detailed enough for a new hire or a few-shot judge prompt); axial coding into under 10 failure modes; count them in a pivot table. Example (apartment-leasing assistant): conversation flow, handoff to human, rescheduling.
- Phase 2, suite: objective failures → code-based evaluators; subjective → LLM-as-judge giving binary pass/fail per failure mode. Binary over 1-5 Likert because "the distinction between a '3' and a '4' is subjective"; nuance goes in the critique.
- RAG: evaluate retriever (recall@k first) separately from generator (faithfulness, relevance); fix the retriever first.
- Phase 3: golden dataset in CI with a regression test for every significant bug (safety net for known failures); async LLM judges on sampled production traces (discovery engine); guardrails inline only if very low false-positive rate. New production failures feed back into error analysis and the golden set.
- Judge scores can be statistically corrected using known TPR/TNR to estimate the true failure rate.

## Notable quotes
- "Research shows that people are not very good at specifying their complete requirements for an AI up front." (Phase 1)
- "Effective evaluation systems are a process, not a dashboard" (closing section heading)

## Could not verify
- Full post read (open access). Figures and screenshots not visible in the text copy. The appendix on score correction and the linked FAQ were not read.
- Claims about adoption (2,000+ trained, 500+ companies, taught at major labs) are the post's own promotional framing.
