---
title: "ISDA Digital Regulatory Reporting"
source_url: https://www.isda.org/isda-digital-regulatory-reporting/
author: International Swaps and Derivatives Association
publisher: ISDA
published: unknown
retrieved: 2026-11-06
type: docs
evidence: first-party
filed_by: design-requirements-agent
themes: [obligation-libraries-as-data, governance-as-code, compounding-context-repo]
relevance: medium
---

## Relevance to the project
The one production-scale example of regulation as machine-executable code in finance: an industry committee agrees a single interpretation of each reporting rule set, which is coded against the open Common Domain Model and run by firms to produce regulator-ready reports, live since December 2022 across 14 regimes in nine jurisdictions. It shows that the obligation-as-data destination is reachable where the domain has a shared data model and an industry body willing to own the interpretation, and that the interpretation (not the code) is the asset. It also now ships a "Tracer Agent" that explains why any report field has its value, an example of an agent reading a governed interpretation rather than raw regulation.

## Themes
- obligation-libraries-as-data: an industry-agreed "golden-source interpretation" of each rule set is converted into code using the Common Domain Model; outputs are ISO 20022 (and DTCC Harmonized XML for Canada).
- governance-as-code: rule interpretations are reviewed and agreed by an industry committee; firms can use DRR to report directly or to validate their own logic.
- compounding-context-repo: interpretation is done once and shared across firms (contributors named include BNP Paribas, Goldman Sachs, Société Générale, Standard Chartered, LSEG, Natixis; JPMorganChase uses it as a primary reporting mechanism).

## Key points
- Coverage: Australia, Canada, EU (EMIR, MiFIR, SFTR), Hong Kong, Japan, Singapore, Switzerland, UK (UK EMIR, UK MiFIR, UK SFTR), US (CFTC and SEC); some in progress.
- Timeline: first launch 5 December 2022 (CFTC rewrite); Japan, EU EMIR, UK EMIR, Australia and Singapore in 2024; Canada and Hong Kong in 2025; Ontario updates expected 2026 to 2027.
- DRR Tracer Agent (built with Gentek) traces why a field is reported as it is; South Africa's trade repository plans to publish its rules as DRR code before reporting starts.

## Could not verify
- Read through WebFetch's model-summarised view; the page does not mention the Rune DSL or FINOS licensing, and gives no adoption count.
