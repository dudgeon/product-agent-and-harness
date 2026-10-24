---
title: "Accelerating Large-Scale Test Migration with LLMs"
source_url: https://airbnb.tech/infrastructure/accelerating-large-scale-test-migration-with-llms/
author: Charles Covey-Brandt (Airbnb)
publisher: The Airbnb Tech Blog (Medium and airbnb.tech)
published: 2025-03-13
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [harness-over-model, human-review-gates, org-context-grounding, agent-factory-sdlc]
relevance: medium
---

## Relevance to the project
Airbnb's best-known LLM engineering case: about 3,500 React test files moved from Enzyme to React Testing Library in six weeks against a 1.5-year manual estimate. The lesson is about the harness, not the model: a per-file state machine with validation gates, retry loops that feed errors back, and careful choice of context files. It is an early (2023 hackathon, 2024 build) example of the "validate, transform, validate" loop that Airbnb later turned into a general migration framework (see dx-airbnb-beyond-the-cli-airchat). It bears on how much structure an agent harness should impose on bulk code work.

## Themes
- harness-over-model: "simply brute force" retries with error feedback beat prompt tuning; choosing the right related files mattered more than prompt wording (sections "Retry loops", "Increasing the context").
- human-review-gates: each file passes Jest, lint and tsc gates before it is marked done; the last ~3% was finished by engineers starting from the failed AI output.
- org-context-grounding: prompts of 40k-100k tokens carried up to 50 related files, sibling tests from the same project and manual few-shot examples.
- agent-factory-sdlc: migration as a pipeline of stages that can be tracked, rerun and parallelised across hundreds of files.

## Key points
- Background: Airbnb adopted RTL for new tests in 2020; Enzyme (since 2015) no longer fit modern React. Deleting old tests would have cut coverage.
- Mid-2023 hackathon showed LLMs could convert hundreds of files in days. In 2024 the team built a scalable pipeline.
- Pipeline: each file moves through states (Enzyme refactor, fix Jest, fix lint and tsc, done). A failed check calls the LLM with the errors and latest file. Loop runner retries up to a set limit; most simple and medium files passed within 10 tries.
- First bulk run: 75% of files migrated in four hours (Airbnb claim, March 2025).
- About 900 failing files remained. Files were stamped with status comments; a `llm-bulk-migration` CLI reran files by path or step. A "sample, tune, sweep" loop over four days took completion to 97%.
- Some long-tail files were retried 50-100 times; the team judged that the ceiling for automation. Manual finish took about a week.
- Total: about six weeks of engineering plus API cost, against a 1.5-year manual estimate (Airbnb's own estimate).

## Notable quotes
- "retry steps multiple times until they passed or we reached a limit" (Retry Loops section)

## Could not verify
- The 1.5-year baseline is Airbnb's own estimate; the post gives no API cost figure. Pragmatic Engineer (pragmatic-engineer-migrations-with-ai) repeats the figures without independent check.
