---
title: "GraphQL Data Mocking at Scale with LLMs and @generateMock"
source_url: https://airbnb.tech/infrastructure/graphql-data-mocking-at-scale-with-llms-and-generatemock/
author: Michael Rebello (Airbnb)
publisher: The Airbnb Tech Blog (airbnb.tech)
published: 2025-11-04
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [org-context-grounding, prototyping-agents-limits, harness-over-model, compounding-context-repo]
relevance: medium
---

## Relevance to the project
A small but telling example of putting an LLM inside existing developer tooling rather than beside it. Engineers add a directive to a GraphQL query; the code generator (Niobe) sends schema, query, a snapshot of the linked design file, hints and a list of real image URLs to Gemini 2.5 Pro, then validates the result against the schema and retries on errors. It links the design artifact (a Figma-style design URL) directly to code-level test and prototype data, which is one of the few documented design-to-code handoffs at Airbnb.

## Themes
- org-context-grounding: context = query and dependencies, the pruned subset of the schema, schema doc comments, design snapshot from `designURL`, hints, platform, and a list of Airbnb-hosted images to stop invented URLs.
- prototyping-agents-limits: aimed at "high-quality demos, which are highly valued at Airbnb for early feedback"; `@respondWithMock` lets client engineers build UI before the server exists.
- harness-over-model: validation through `graphqlSync` and error-fed retries "self-heal" bad mocks; the author says this guarantee would not be possible with a tool outside the GraphQL infrastructure like ChatGPT.
- compounding-context-repo: mocks carry hashes of the query and arguments; when the query changes, the LLM gets the old mock plus a diff and is told to change only what changed; a pre-submit check keeps hashes current.

## Key points
- Pain points came from meetings with product engineers and internal surveys: hand-written mocks are slow, client work is blocked on server work, and mocks drift from queries.
- Model choice: Gemini 2.5 Pro for its 1M-token window and speed in internal tests (Airbnb claim).
- Output: JSON mock plus generated helper functions for demo apps, snapshot tests and unit tests on iOS, Android and Web.
- Adoption: over 700 mocks generated and merged in "the past few months" (Airbnb claim, Nov 2025). Backend support planned.

## Could not verify
- No time-saved measure; one anonymous engineer quote is the only outcome evidence.
