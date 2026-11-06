---
title: "Microsoft Responsible AI Standard, v2: General Requirements"
source_url: https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf
author: Microsoft
publisher: Microsoft
published: 2022-06-21
retrieved: 2026-11-06
type: docs
evidence: first-party
filed_by: design-requirements-agent
themes: [governance-as-code, regulatory-drivers-of-process, launch-readiness-review, standard-form-spectrum]
relevance: medium
---

## Relevance to the project
Microsoft's internal AI policy, published as product development requirements: each principle becomes Goals (A1 to A5, T1 to T3, F1 to F3, reliability and safety, privacy and security, I1), each Goal says what systems it "Applies to", and each requirement carries an ID and tags (58 requirements in the external version). It is a public example of enterprise policy written in the form an obligation library needs: identifiable, scoped by applicability condition, and linked to the artefact (the Impact Assessment) where compliance is recorded. It is the policy behind the template filed as `microsoft-rai-impact-assessment-template`.

## Themes
- governance-as-code: requirement IDs (A1.1, A1.2, ...) with an "Applies to" scope and tags such as "Impact Assessment" (pages 4 to 5); the applicability scope is the hook a classifier needs.
- launch-readiness-review: A1.1 complete an Impact Assessment "early in the system's development, typically when defining the product vision and requirements"; A1.2 review it with reviewers and secure approvals "before development starts"; A1.3 update at least annually, when new intended uses are added, and before a new release stage.
- regulatory-drivers-of-process: the Standard fills a policy gap where "Laws and norms had not caught up" with AI risks, and is a living document to evolve with laws (About this release).
- standard-form-spectrum: goals are outcome statements ("Microsoft AI systems are assessed using Impact Assessments") decomposed into checkable requirements, an intermediate form between principle and rule.

## Key points
- A2 oversight of significant adverse impacts: check Restricted Uses and Sensitive Uses via the template's prompts; report sensitive uses to the Office of Responsible AI; annual re-review against both definitions.
- Goal list in this release: A1 impact assessment, A2 oversight of significant adverse impacts, A3 fit for purpose, A4 data governance and management, A5 human oversight and control; T1 system intelligibility for decision making, T2 communication to stakeholders, T3 disclosure of AI interaction; F1 quality of service, F2 allocation of resources and opportunities, F3 minimisation of stereotyping, demeaning and erasing outputs; reliability and safety, privacy and security goals; I1 accessibility standards compliance.
- Re-assessment triggers are explicit (annual, new intended use, release stage), which is the freshness rule an obligation record needs.

## Could not verify
- Read as extracted PDF text; only the index and accountability pages were read closely. The publication day is from Microsoft's June 2022 release; the PDF says only "June 2022". Whether Microsoft has since published a v3 was not checked.
