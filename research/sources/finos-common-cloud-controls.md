---
title: "FINOS Common Cloud Controls (CCC)"
source_url: https://ccc.finos.org/
author: FINOS (Fintech Open Source Foundation)
publisher: ccc.finos.org
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [governance-as-code, agent-legible-platform, platform-onboarding-friction]
relevance: high
---

## Relevance to the project
The strongest regulated-industry example of banks codifying controls in a shared, machine-readable form: a cross-bank open standard of threats, controls and testable assessment requirements for cloud services, steered by Citi, Morgan Stanley, RBC, BlackRock, LSEG and others. It shows banks will publish control expectations as data when it cuts duplicated work, and that controls can be expressed as pipeline gates a requester (or agent) could pre-check.

## Themes
- governance-as-code: each control carries assessment requirements that can become scans, code analyses or behavioural checks, runnable as pipeline gates that block non-compliant resources (Verification section).
- agent-legible-platform: technology-agnostic Core Catalog of threats and controls that organisations import and extend with service-specific catalogs.
- platform-onboarding-friction: aim is a common framework instead of each bank's bespoke cloud-risk interpretation (FINOS blog estimates Tier 1 banks run 15,000-20,000 active controls; search result, not this page).

## Key points
- Steering committee lists Citi, LSEG, Morgan Stanley, Scott Logic, Red Hat, RBC, BlackRock.
- Site counts 450 capabilities, 223 threats, 206 controls; links Validators and Test Results pages.
- Originally proposed by Citi (announced Oct 2023); secondary sources say it uses OSCAL, which this page does not mention.

## Could not verify
- OSCAL usage and adoption inside specific banks; release version.
