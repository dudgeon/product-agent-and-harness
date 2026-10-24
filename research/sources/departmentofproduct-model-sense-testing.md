---
title: How to test a new AI Model to get up to speed with its capabilities quickly
source_url: https://departmentofproduct.substack.com/p/how-to-test-a-new-ai-model-to-get
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-12-16
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [evals-autonomy-trust, harness-over-model, vendor-claims-vs-independent-evidence, outcome-measurement-gap]
relevance: medium
---

## Relevance to the project
Argues that "model sense" (a hands-on feel for what each new model can and cannot do) is becoming a core PM skill, and gives a practical routine: a personal logbook with a reusable prompt library, a changelog tracker comparing official claims with observed performance, and a small domain eval suite rerun at every release. For the project it is a lightweight, PM-owned version of re-testing the harness at each model release, and it names "scaffolding" (retrieval, human-in-the-loop escalation, domain checks) as the thing that closes model gaps, which matches the harness-over-model theme. It is about evaluating models for product features, not PM agents, and the ideas are attributed second-hand to Google's Madhu Guru and Box's Aaron Levie.

## Themes
- evals-autonomy-trust: the "Model Sense Notebook" holds five logs: model tests, prompt library, frontier-opportunity tracker, changelog (claims vs reality), and an evaluation suite of domain tests rerun to track reliability (setup section). Points to Braintrust as a cross-functional eval tool PMs can use.
- harness-over-model: defines scaffolding as the infrastructure, logic and guardrails "you build around an AI model to make it actually work reliably in production", and says knowing which features need it is the skill (scaffolding section).
- vendor-claims-vs-independent-evidence: benchmarks "are often presented in a way that flatters the model"; only hands-on tests give a real sense.
- outcome-measurement-gap: an anecdote of Claude reading "this year" as 2024 in a Google Analytics task, caught only by checking the numbers by hand (data section).

## Key points
- Tests by area: a fixed generative prompt over time (Simon Willison's pelican-on-a-bicycle, with a harder variant); coding for non-engineers (simple observable pages, walking through a known past bug and comparing reasoning, sitting with engineers; SWE-bench explained); prototyping with a structured template, compared across Gemini 3 and Claude Opus 4.5, then a model-as-senior-designer critique; data analysis (trends, pivots, outliers, SQL); API basics (temperature, tokens) and probing guardrails with adversarial prompts.
- "Frontier zone": build internal prototypes on capabilities that are "kinda possible" now and expected to be reliable in about six months, using low benchmark areas (e.g. computer use) as the pointer; do not ship until reliable.
- A downloadable Notion-style notebook template.

## Could not verify
- The Madhu Guru and Aaron Levie remarks (shown as images; not linked in the text).
