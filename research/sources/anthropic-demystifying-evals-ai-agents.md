---
title: Demystifying evals for AI agents
source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
author: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe (Anthropic)
publisher: Anthropic Engineering
published: 2026-01-09
retrieved: 2026-10-25
type: article
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [gate-judge-separation, evals-autonomy-trust, human-review-gates]
relevance: high
---

## Relevance to the project
The most direct vendor statement on the gate-type dimension: three grader kinds (code, model, human) with stated strengths and weaknesses and an ordering rule: deterministic where possible, model where necessary, human sparingly for validation and calibration. It also argues against rigid path checks ("grade what the agent produced, not the path it took"), which is a caution against encoding PM skills as mandatory step sequences when only the artifact matters.

## Themes
- gate-judge-separation: code graders fast, cheap, objective, reproducible but brittle and blind to nuance; model graders flexible and nuanced but non-deterministic, costlier, need calibration; human graders gold standard but slow, costly, scarce.
- human-review-gates: humans calibrate model graders; use human grading "sparingly".
- evals-autonomy-trust: capability evals start at low pass rates; regression evals near 100%; capability evals "graduate" into regression suites.

## Key points
- Ordering rule: deterministic graders where possible, LLM graders where necessary or more flexible, human graders sparingly for validation. Scoring can be weighted, binary or hybrid.
- Coding evals: unit tests plus an LLM rubric for code quality; conversational evals mostly model-graded.
- Outcome vs transcript: avoid rigidly checking step sequences, since agents find valid unanticipated paths; transcripts still used to diagnose failures.
- Rubric advice: structured rubrics; one isolated LLM judge per dimension rather than one judge for all; give the judge an "Unknown" way out; calibrate with experts.

## Notable quotes
- "it's often better to grade what the agent produced, not the path it took"

## Could not verify
- Read via summary fetch; examples beyond those above not recorded.
