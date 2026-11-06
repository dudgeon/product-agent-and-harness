---
title: "Digital Regulatory Reporting Pilot Phase 1 Report"
source_url: https://www.fca.org.uk/publication/discussion/digital-regulatory-reporting-pilot-phase-1-report.pdf
author: Financial Conduct Authority and Bank of England (with pilot banks)
publisher: FCA
published: unknown
retrieved: 2026-11-06
type: report
evidence: first-party
filed_by: design-requirements-agent
themes: [obligation-libraries-as-data, governance-as-code, rules-vs-judgment-encoding]
relevance: high
---

## Relevance to the project
The UK regulators' own test of "regulation as code", run with six large banks in 2018, found that even rules intended to be unambiguous could not be converted into code without a human making further assumptions, that no method (direct human translation, a domain-specific language, semantic technology, NLP) had yet proven it could scale, and that the source documents are written to capture legal and policy intent across many interlinked PDFs. That is direct evidence for how a requirements agent should treat obligations: the interpretation step is the expensive, judgement-bearing part, it is best done once centrally and reused, and an agent that reads raw regulation must record its interpretation as a provisional claim for a named validator.

## Themes
- rules-vs-judgment-encoding: key finding 5.1: "there is no obvious solution to efficiently convert regulatory instructions" expressed in natural language into code; natural-language instructions "are not detailed enough to be translated into code", so a human must bridge the gap.
- obligation-libraries-as-data: reporting instructions "are often embedded across many legal documents and published in pdf form" and are hard to keep in sync with code when they change and come from several regulators (5.1).
- governance-as-code: the prototype interpreted instructions once and distributed the logic to all firms, which "may be significantly more efficient" than each firm translating separately; but outsourcing interpretation to a single body has significant consequences given the legal and financial stakes (5.2).

## Key points
- Background (section 2): instructions for one report can be spread across many interlinking regulations; wording may be unclear; firms must make judgements; international firms repeat the work per regime; many buy professional services to interpret requirements.
- Approaches tried: direct translation into code; a structured machine-readable language (DSL) usable by policy makers and lawyers; semantic technologies; NLP extraction of key terms.
- Use cases: UK mortgage reporting (product sales data) and the CET1 capital ratio, among Barclays, Credit Suisse, Lloyds, Nationwide, NatWest and Santander (FCA pilot updates page).
- Phase 2 (February to October 2019) addressed economic viability; ISDA's Digital Regulatory Reporting (filed as `isda-digital-regulatory-reporting`) is the production descendant of this idea in derivatives reporting.

## Notable quotes
- "not detailed enough to be translated into code" (section 5.1)

## Could not verify
- Read as extracted PDF text. The report carries no publication date in the text read; the pilot ran during 2018 and the Bank of England's summary page is dated 13 March 2019. The Phase 2 report and viability assessment were not read.
