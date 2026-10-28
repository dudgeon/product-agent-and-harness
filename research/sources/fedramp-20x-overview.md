---
title: "FedRAMP 20x"
source_url: https://www.fedramp.gov/20x/
author: FedRAMP (US GSA)
publisher: fedramp.gov
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [governance-as-code, platform-onboarding-friction, agent-legible-platform]
relevance: high
---

## Relevance to the project
FedRAMP 20x is the largest public example of a regulator replacing document-based authorisation with machine-readable, automatically validated security indicators and continuous reporting. It is the government analogue of the dependency agent's destination: the provider publishes structured evidence, validation runs as code, and assessors review the validation code rather than narratives. Its own lessons (KSIs as a presentation confused people) are a caution that machine-readable is not automatically legible.

## Themes
- governance-as-code: providers' security status "should be validated automatically whenever possible"; Phase 2 lessons cite consistent machine-readable schemas, validations that fit existing provider tools, and assessor review of validation code (Goals, Phase 2 lessons).
- platform-onboarding-friction: replaces static yearly manual assessments; "Security should be continuously enforced, monitored, and reported—not staged for a point-in-time audit."
- agent-legible-platform: Key Security Indicators (KSIs) were the Phase 1 proof of concept for automated validation; Phase 2 found presenting requirements as KSIs "confusing".

## Key points
- Phase 1 (Apr-Sep 2025, Low): 26 complete packages, 13 reviews, first pilot authorisations late July 2025.
- Phase 2 (18 Nov 2025-Mar 2026, Moderate): 14 qualifying submissions; first cohort authorised 6 Mar 2026; six more by 27 Apr 2026.
- Phase 3 active: Consolidated Rules for 2026 planned June 2026; submission pipeline Jul-Sep 2026. Phase 5: no new Rev5 certifications after 11 Jun 2027.
- Certification classes A (pilot), B (Low), C (Moderate), D (High, Phase 4).
- Core principle on the page: "Continuous evidence of what is happening is stronger than a policy saying it should happen"; Phase 1 lesson that KSIs "can demonstrate security posture in near real time", and participants no longer rushed to finish paperwork before an audit (re-read 2026-10-28).

## Could not verify
- Whether OSCAL is mandatory for 20x packages (the page does not mention OSCAL; secondary sources say OSCAL outputs are required from Sep 2026).
