---
title: Graders (OpenAI API docs)
source_url: https://developers.openai.com/api/docs/guides/graders
author: OpenAI
publisher: OpenAI developer docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [gate-judge-separation, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
A vendor's typology of checks from fully deterministic (string equality) through fuzzy metrics and custom code to model judges, with the rule "use an LLM judge when code falls short". It also warns about grader hacking, a risk for any PM skill that self-scores against a rubric.

## Themes
- gate-judge-separation: string check (0/1, `eq`/`like`), text similarity (BLEU, ROUGE, cosine, fuzzy), Python `grade()` functions, score-model graders returning a score in a range with reasoning steps; multigraders combine them with a formula.
- evals-autonomy-trust: calibrate model graders against expert-graded answers; check the grader ranks answers in the same order as experts; add edge cases over time.

## Key points
- Guidance: string checks for "straightforward pass or fail answers"; similarity for open-ended closeness; Python for custom logic; LLM judge "when code falls short"; combine when correctness depends on several conditions (exact email match plus tolerant name match).
- Prefer smooth scores to pass/fail for optimisation; watch for "grader hacking" (high model-grader score, poor expert review); balance skewed datasets.
- Context is reinforcement fine-tuning and evals, not runtime gates; the typology transfers.

## Could not verify
- The page did not describe a label-model grader in the retrieved text; page undated.

## Added by research-skill-rigidity-spectrum (2026-10-25)
- Form of the standard inside a model grader: OpenAI's advice is a rubric embedded in the grader prompt with "detailed, step-by-step instructions" and many examples, a numeric `range` and a `pass_threshold` (worked example: exact match 1, partial 0.5, else 0), with reasoning `steps` returned alongside the score. The reliability advice (validate against expert-graded examples; prefer smooth scores to pass/fail; run multiple samples through the judge to check stability) matches the judge-bias literature (arxiv-zheng-judging-llm-as-a-judge). Note the page says graders in evals and fine-tuning are being deprecated. Theme: standard-form-spectrum.
