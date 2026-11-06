---
title: "INCOSE Guide to Writing Requirements (Jama Software requirements management guide)"
source_url: https://www.jamasoftware.com/requirements-management-guide/writing-requirements/incose-requirements-writing-guide/
author: Mario Maldari
publisher: Jama Software
published: 2026-08-20
retrieved: 2026-11-06
type: article
evidence: vendor-claim
filed_by: design-requirements-agent
themes: [rules-vs-judgment-encoding, requirements-partitions, spec-edge-case-review]
relevance: medium
---

## Relevance to the project
A requirements-tool vendor's summary of the INCOSE Guide to Writing Requirements (version 4, 2023), the most widely used rulebook for individual requirement statements and sets. It gives the numbering an agent's deterministic check step could cite (C1 to C15 characteristics, about 42 rules) and, usefully, says which rules natural-language processing can check (vague terms, escape clauses, passive voice, combinators) and which characteristics still need an engineer (necessary, correct). That split maps onto the intent-shaping brief's design: mechanical quality checks as fail-closed gates, necessity and correctness as validator questions.

## Themes
- rules-vs-judgment-encoding: NLP can check R7 (no vague quantifiers or subjective adjectives), R8 (no escape clauses), R2 (active voice) and R19 (no combinators); judgement-based characteristics such as Necessary and Correct "still require an engineer".
- requirements-partitions: characteristics split into individual-statement ones (C1 necessary, C2 appropriate, C3 unambiguous, C4 complete, C5 singular, C6 feasible, C7 verifiable) and set-level ones (C10 complete, C11 consistent, C12 feasible, C15 correct); traceability has no characteristic of its own.
- spec-edge-case-review: set-level completeness (C10) is a property of the whole set, which is what an obligation screen adds to a feature's own requirements.

## Key points
- Rules named: R1 consistent structure against an agreed statement pattern; R2 active voice; R4 defined terms; R7 no vague terms; R8 no escape clauses; R16 restricted negation; R18 one requirement per statement; R19 no combinators; R31 implementation detail only with documented rationale; R34 measurable performance targets; R36 consistent terms and units; R40 decimal format (new in v4).
- The page is marketing for Jama Connect Advisor, which scores requirements against a subset of these rules and EARS (filed as `jama-connect-advisor-interpreting-results`).

## Could not verify
- The INCOSE guide itself (INCOSE-TP-2010-006-04, July 2023) could not be retrieved: the INCOSE-hosted PDF returned an HTML page instead of the document. Rule names above are the vendor's summary and may paraphrase INCOSE's wording. Read through WebFetch's model-summarised view.
