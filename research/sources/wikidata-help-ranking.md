---
title: "Help:Ranking"
source_url: https://www.wikidata.org/wiki/Help:Ranking
author: Wikidata contributors
publisher: Wikidata
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms]
relevance: high
---

## Relevance to the project
Wikidata separates two things the project's store also needs to separate: where a value came from (references) and which value should be used (rank). Conflicting values can sit side by side, one marked preferred, a wrong one marked deprecated rather than deleted so nobody re-adds it, and queries read only the best-ranked value. It bears on provenance, consistency and fitness to drive rules: a gate rule should read the "best rank" value, while the history of contested values stays visible.

## Themes
- context-trust-mechanisms: three ranks (preferred, normal, deprecated); the query service's "best" (truthy) value is the preferred one if any, else normal; deprecated statements are never used in templates or queries unless asked for; "References merely state where a data value comes from" (sections on each rank and on references).

## Key points
- Preferred marks the value(s) that "best represent consensus", ideally sourced or qualified (preferred rank section).
- Deprecated is for statements "known to include errors" or outdated knowledge. Correct historical values are not deprecated but given start and end qualifiers (deprecated rank section). The distinction matters for lead times and owners: a superseded owner is history (end-dated), a wrong owner is deprecated.
- Keeping the deprecated statement prevents others re-adding it and records how understanding changed (deprecated rank section). Useful against agents that re-scrape a stale wiki and re-write the old value.
- Every statement, deprecated ones included, must be verifiable: a source must make the claim, true or not (references section). Provenance and correctness are independent axes.
