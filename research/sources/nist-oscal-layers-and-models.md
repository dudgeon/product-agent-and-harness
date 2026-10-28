---
title: "OSCAL: the Open Security Controls Assessment Language (layers and models)"
source_url: https://pages.nist.gov/OSCAL/learn/concepts/layer/
author: NIST
publisher: pages.nist.gov
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [governance-as-code, agent-legible-platform, decision-rationale-records]
relevance: high
---

## Relevance to the project
OSCAL is the standards-body format for making controls, system security plans and assessment results machine-readable. In regulated orgs it is the most mature candidate for "what this platform checks, and the evidence that it did", which is exactly the part of a platform's onboarding a dependency agent cannot see today. It is used for authorisation packages (FedRAMP, FINOS CCC), not yet for per-request onboarding.

## Themes
- governance-as-code: three layers: Control (Catalog, Profile, Control Mapping), Implementation (Component Definition, System Security Plan), Assessment (Assessment Plan, Assessment Results, POA&M); all released (layer page).
- agent-legible-platform: a Component Definition describes how a component (e.g. a platform service) implements controls, which a consumer can inherit; formats XML, JSON, YAML (OSCAL home).
- decision-rationale-records: Assessment Results and POA&M record findings and remediation commitments as data.

## Key points
- NIST home page frames OSCAL as replacing Word/Excel security plans and says automation "dramatically reduces audit durations from months to minutes" (NIST claim, no evidence on page).
- Control Mapping model is at v1.2.0 per the link on the page.

## Notable quotes
- "Each lower layer in the stack provides information structures that are referenced and used by each higher layer."
