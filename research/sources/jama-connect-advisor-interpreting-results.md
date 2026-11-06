---
title: "Jama Connect Advisor: Interpreting the results"
source_url: https://help.jamasoftware.com/ah/en/jama-connect-advisor-/interpreting-the-results.html
author: Jama Software
publisher: Jama Software help
published: unknown
retrieved: 2026-11-06
type: docs
evidence: first-party
filed_by: design-requirements-agent
themes: [rules-vs-judgment-encoding, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
The product help for Jama's NLP requirements-quality add-on shows what commercial requirements-quality tooling actually outputs: per-requirement analysis in two parts, INCOSE rules (a percentage score per rule, colour-banded, with suggested changes) and EARS notation (syntax guidance and suggested rewrites). It is the existing statement-level quality check a requirements agent in an engineering-heavy enterprise might call rather than rebuild; it says nothing about completeness of a set or about obligations.

## Themes
- rules-vs-judgment-encoding: score bands: 81 to 100% "High quality with a few suggested improvements", 61 to 80% medium, 0 to 60% low; per-rule feedback with suggested changes.
- vendor-claims-vs-independent-evidence: the page does not say how scores are computed or which rules are checked; a Jama webinar recap (search result) claims a "core subset" of the 40-odd INCOSE rules plus 49 requirement attributes.

## Key points
- Comparable tools: IBM Engineering Requirements Quality Assistant scores each requirement 1 to 100 using Watson NLP trained on INCOSE-consistent indicators (English, text-only; IBM's SaaS was discontinued and a partner now offers it); QRA's QVscribe markets "deterministic evaluation" against INCOSE rules. Both seen through search results only.

## Could not verify
- Read through WebFetch's model-summarised view. No independent accuracy evaluation of Jama Connect Advisor, IBM RQA or QVscribe was found.
