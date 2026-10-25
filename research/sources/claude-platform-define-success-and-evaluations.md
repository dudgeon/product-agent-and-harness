---
title: "Define success criteria and build evaluations"
source_url: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
author: Anthropic
publisher: Claude Developer Platform docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [standard-form-spectrum, gate-judge-separation, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Anthropic's grading ladder and rubric tips in one page: code-based grading is "fastest and most reliable" but "lacks nuance"; human grading is "most flexible and high quality, but slow and expensive. Avoid if possible"; LLM grading is "fast and flexible ... Test to ensure reliability first, then scale". The rubric advice is specific enough to copy: write rubric lines that are checkable ("The answer should always mention 'Acme Inc.' in the first sentence. If it does not, the answer is automatically graded as 'incorrect'"), expect several rubrics per criterion, and let the grader reason before scoring. It also states the design principle "prioritize volume over quality": more automated checks with slightly lower signal beat fewer hand-graded ones.

## Themes
- gate-judge-separation: three grading methods ranked code, human, LLM, with the trade-offs quoted above; worked examples use exact match, cosine similarity, ROUGE-L, an LLM Likert scale for tone, and an LLM binary yes/no for PHI (Grading evals).
- standard-form-spectrum: rubric lines written as checkable statements with a stated consequence; "A given use case ... might require several rubrics for holistic evaluation"; grader outputs 'correct'/'incorrect' or a 1-5 score (Tips for LLM-based grading).
- evals-autonomy-trust: "More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals" (Eval design principles); use a different model to grade than to generate (Likert example).

## Key points
- Success criteria should be specific, measurable, achievable, relevant; even safety can be quantified ("Less than 0.1% of outputs out of 10,000 trials flagged for toxicity").
- Task-specific evals mirroring the real distribution, with edge cases.
- Encourage reasoning: use a grader with thinking on so it reasons before scoring.
