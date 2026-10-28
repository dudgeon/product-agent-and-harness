---
title: "Onboarding to the National Record Locator (NRL) v3.0"
source_url: https://digital.nhs.uk/services/national-record-locator/nrl-onboarding-guidance
author: NHS England
publisher: NHS England Digital
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [platform-onboarding-friction, process-governance-load, process-artifacts-as-coordination, legible-org-for-agents]
relevance: high
---

## Relevance to the project
A public, stage-gated onboarding process for a national health-data platform, and one of the few places a regulated platform's full intake is written down: prerequisites (organisation code, Data Security and Protection Toolkit, a defined use case), eligibility and credentials, clinical-safety and non-functional assurance (DCB0129/DCB0160 hazard logs), technical conformance testing in sandbox and integration environments, then a signed connection agreement before production credentials. Each stage gates access to the next environment, and timings are explicitly undefined. It is close to the "machine-readable onboarding contract" the dependency agent would want, but written for people, with each gate reviewed by hand.

## Themes
- platform-onboarding-friction: "You cannot proceed to DOS Stage 1 without these prerequisites in place"; "Timelines vary depending on the complexity of your integration and the completeness of submitted evidence" (Stage 0; Timings).
- process-governance-load: Stage 2 requires clinical risk management documents (DCB0129/DCB0160), a hazard log, information-governance confirmation and security architecture where required; "NHS England will review submitted evidence and may request clarification or updates".
- process-artifacts-as-coordination: stage outputs are artefacts (app ID and non-production credentials, test evidence, conformance certificate, signed connection agreement).
- legible-org-for-agents: the stage structure, inputs and environment gating are explicit enough to encode; the review steps are not.

## Key points
- Stages via NHS England's Digital Onboarding Service: 0 prerequisites; 1 set-up and eligibility (use case validated, contacts named, developer-portal access, non-production credentials); 2 non-functional and clinical-safety assurance; 3 technical conformance and testing ("You will not progress until evidence is accepted"); 4 legal agreement and production access, with a production smoke test.
- Path to live: Sandbox, Integration (INT), Production; "Access to each environment is controlled and dependent on the successful completion of prior stages."
- Dependent services (Spine Secure Proxy, National Document Repository) need "separate onboarding and approval, where applicable": onboarding to one platform triggers onboarding to others.
- The NHS login integration plan (separate NHS page, seen via search only) estimates its own onboarding at about 3 to 4 months.

## Could not verify
- Page read via a mirror of the NHS England site (nhsd-proxy.openprescribing.net) because digital.nhs.uk returned 403; the NHS login "3 to 4 months" figure was seen only in a search summary.
