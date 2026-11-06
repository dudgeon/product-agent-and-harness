---
title: "UCF Mapping Report: Framework for Improving Critical Infrastructure Cybersecurity, Version 1.1 Draft 2"
source_url: https://www.nist.gov/document/2018-01-12-unifiedcomplianceframeworkucfpdf
author: Unified Compliance (UCF mapping team)
publisher: NIST (hosted)
published: 2018-01-12
retrieved: 2026-11-06
type: report
evidence: first-party
filed_by: design-requirements-agent
themes: [obligation-libraries-as-data, governance-as-code, requirements-partitions, rules-vs-judgment-encoding]
relevance: high
---

## Relevance to the project
A real artefact from the Unified Compliance Framework, the largest commercial library of mapped regulatory mandates, showing its data model and method end to end: an authority document is catalogued, split into citations, each citation into single mandates (tagged with primary and secondary verbs and nouns), and each mandate mapped to one common control in a taxonomy of impact zones. It also publishes the mapping team's open questions where the source text was ambiguous. This is the structured, authoritative data product a requirements agent would want to read obligations from, and the decomposition (one mandate per statement) is the same "singular" rule requirements quality guides apply.

## Themes
- obligation-libraries-as-data: the document has "176 citations mapped to 134 UCF Common Control IDs"; common controls sit in a hierarchy of Impact Zones (audits and risk management, HR, leadership, monitoring and measurement, continuity, operational management, physical, privacy, records management, system hardening, systems design and build, technical security, third party and supply chain) (pages 1 to 2).
- requirements-partitions: the impact-zone taxonomy is a partition by control domain built "through the lens of unification", independent of the source document's own structure (page 2).
- rules-vs-judgment-encoding: citations with several mandates are split so "only one mandate at a time can be mapped to a Common Control"; explanatory text is ignored; curly brackets add missing context to make a citation mappable (page 3).
- governance-as-code: mapping uses named entity recognition and part-of-speech tagging, then distance vectors to match mandates to controls, under a patented method (page 4).

## Key points
- Quality metrics per authority document: 22.8% of citations had multiple mandates; 7.1% of terms mapped to the document's glossary; 15.9% of mandates were called for by no other authority document ("lone wolf" mandates, harder to implement).
- Controls are counted as mandated, implied and implementation (134, 90 and 1,735 for this document): the library distinguishes what the source demands from what implementing it entails.
- The "Questions encountered during mapping" table records ambiguities (e.g. what "network integrity" means in PR.AC-5) and asks the issuer: an explicit open-question record, the same thing an agent should produce when an obligation is unclear.
- "Stub" citations (no mandate) are kept but unmapped.

## Notable quotes
- "only one mandate at a time can be mapped to a Common Control" (page 3)

## Could not verify
- Read as extracted PDF text (first five pages closely). UCF's own knowledge-base pages on compliance mapping returned 404. Library-wide scale figures (about 100,000 mandates, 10,000 controls, 1,000 authority documents) appear only in a third-party blog and are not confirmed.
