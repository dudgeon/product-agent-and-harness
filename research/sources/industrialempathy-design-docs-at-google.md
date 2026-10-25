---
title: Design Docs at Google
source_url: https://www.industrialempathy.com/posts/design-docs-at-google/
author: Malte Ubl
publisher: Industrial Empathy
published: 2020-07-06
retrieved: 2026-10-25
type: article
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [decision-rationale-records, process-artifacts-as-coordination, human-review-gates]
relevance: high
---

## Relevance to the project
A practitioner account of Google's design-doc culture: an informal doc whose value is the trade-off and alternatives sections and the early review, kept as organisational memory. It is a strong exemplar of an artifact that is both end-product (the design) and process (review record, rationale), and of a loose form: "Rule #1" is write in whatever form fits.

## Themes
- decision-rationale-records: "alternatives considered" is called one of the most important sections; the doc's focus is trade-offs (body).
- process-artifacts-as-coordination: purposes listed include catching issues early, consensus across the org, spreading senior engineers' knowledge, organisational memory (body).
- human-review-gates: lightweight review (send to list, comment) vs formal design review meetings with senior engineers; formal can slow progress (body).

## Key points
- Sections: context and scope; goals and non-goals (non-goals are plausible goals deliberately excluded); the design (overview then detail, system-context diagram, API sketches); alternatives considered; cross-cutting concerns (security, privacy, observability; privacy has its own dedicated doc and review).
- Length: 10-20 pages for large projects; "mini design doc" of 1-3 pages for small changes.
- Lifecycle: create and iterate; review (maybe several rounds); implement and amend; revisit a year or two later to learn what was right or wrong.
- When not to write: solution is unambiguous; doc would be an implementation manual without trade-offs.
- Decision aid: five questions (e.g. is the design uncertain, contentious); three or more yeses suggests writing one.
- Evidence: first-party description of practice; no outcome data.

## Notable quotes
- "Write them in whatever form makes the most sense for the particular project."
