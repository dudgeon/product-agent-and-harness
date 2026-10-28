---
title: "Infosys insurance customer case study (Backstage developer portal)"
source_url: https://www.cncf.io/case-studies/infosysinsurancecustomer/
author: Cloud Native Computing Foundation (implementer: Infosys)
publisher: CNCF
published: 2024-08-27
retrieved: 2026-10-28
type: article
evidence: vendor-claim
filed_by: research-dependency-agent
themes: [platform-onboarding-friction, dependency-value-evidence, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
The only named-sector (insurance) developer-portal case with figures found: an unnamed US insurance, retirement and annuity company whose Backstage portal, integrated with its CMDB, source control, CI, security scanners and identity, is credited with 40% faster onboarding of new developers, 35% higher deployment frequency and 20% shorter lead time. The implementer wrote it, the client is anonymous, and no baseline or method is given, so it is a vendor claim, but it shows what a regulated firm wires into a portal (the CMDB among them).

## Themes
- platform-onboarding-friction: "Onboarding time for new developers reduced by 40%" (Impact). Vendor claim, no method.
- dependency-value-evidence: "Deployment frequency (DF) increased by 35%"; "Time from code commit to production is faster by 20%"; "products got to market faster by 25-30%" (Impact).
- vendor-claims-vs-independent-evidence: implementer-authored, anonymous client, no baseline period or measurement method.

## Key points
- Problem stated as siloed teams and reluctance to share resources.
- Infosys compared OpsLevel, Cortex and Backstage and chose Backstage (v1.11.0) with a software catalog, self-service scaffolder templates and 20+ custom plugins.
- Integrations: Bitbucket, Swagger, Jenkins, AppDynamics, CMDB, SonarQube, Fortify, Twistlock, Kibana, AWS S3, Okta; environments Dev, QA, Model and Prod on AWS.
