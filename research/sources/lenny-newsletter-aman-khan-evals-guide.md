---
title: "Beyond vibe checks: A PM's complete guide to evals"
source_url: https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete
author: Aman Khan (Director of Product, Arize AI), guest post in Lenny's Newsletter
publisher: Lenny's Newsletter
published: 2025-04-08
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [evals-autonomy-trust, spec-becomes-prototype-and-evals, outcome-measurement-gap, ai-synthesis-hallucination-risk]
relevance: medium
---

## Relevance to the project
A practical method a PM can use to define "good" for an agent: a four-part LLM-judge prompt, a 10-100 example human-labelled set, a 90% agreement target, then continuous evaluation in production. It is written for PMs building customer-facing AI products, not for judging PM agents, but the same loop is a candidate answer to pm-agent-evaluation (how we would know a PM agent works) and to review-and-autonomy (evals as an automated verifier before human spot checks). The author works for an eval-tooling vendor (Arize; contributor to the open-source Phoenix), disclosed in the post.

## Themes
- evals-autonomy-trust: evals are "regression tests or benchmarks" defining what good looks like for non-deterministic systems (section "What exactly are evals?"); production monitoring runs evals on live traffic and compares to real user outcomes ("Phase 4").
- spec-becomes-prototype-and-evals: writing the judge's goal and labels means "translating nuanced user expectations into precise criteria" (section "The eval formula", part 3): the eval as a written statement of intent.
- outcome-measurement-gap: eval scores can be "proxy leading metrics" tied to business outcomes, but only when validated against real user feedback ("Common mistakes").
- ai-synthesis-hallucination-risk: recommends hallucination detection (does output use provided context?) as the first eval to build ("What's next?").

## Key points
- **Three eval types ("Different eval approaches"):** human evals (thumbs, expert labels; sparse, weak and costly signal), code-based evals (cheap and fast; weak for open-ended tasks), LLM-as-judge (scalable, natural-language so PMs can write them; probabilistic, needs labelled examples to calibrate; panels of judges or confidence scores raise reliability).
- **Standard criteria:** hallucination, toxicity/tone, overall correctness; also code generation, summarization quality, retrieval relevance. Points to off-the-shelf evaluators in Phoenix and Ragas.
- **Four-part judge prompt ("The eval formula"):** role, context (the data to grade), goal (what success and failure look like), terminology and label definitions.
- **Workflow:** (1) collect real interactions and edge cases into a balanced dataset with 10-100 human labels, spreadsheets are fine at first; (2) write a first eval and aim for at least 90% agreement with human labels; (3) iterate on the eval prompt with few-shot good/bad examples, and use the dataset to compare agent changes such as a model swap; (4) run evals continuously in production and build dashboards.
- **Common mistakes:** over-complex evals give noisy signals and teams lose trust; not testing edge cases; not validating evals against real user feedback.
- Worked example throughout: a trip-planning agent that books San Diego instead of San Francisco.

## Notable quotes
- "Prompts may make headlines, but evals quietly decide whether your product thrives or dies" (intro).
- "If a human can grade something, so can an LLM" (section "LLM-based evals").

## Could not verify
- Paywalled post, read in full through a paid subscription. The embedded example prompt images were not visible in the text.
- The 90% agreement target and 10-100 example rule are the author's rules of thumb, not tested thresholds. Author has a commercial interest in eval tooling (disclosed).
