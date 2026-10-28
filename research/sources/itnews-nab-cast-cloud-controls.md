---
title: "NAB uses CAST to keep its cloud apps in check"
source_url: https://www.itnews.com.au/news/nab-uses-cast-to-keep-its-cloud-apps-in-check-528857
author: Ry Crozier
publisher: iTnews
published: 2019-08-02
retrieved: 2026-10-28
type: article
evidence: first-party
filed_by: research-dependency-agent
themes: [governance-as-code, platform-onboarding-friction, risk-sloped-review, stale-records-mislead-agents]
relevance: medium
---

## Relevance to the project
National Australia Bank's infrastructure head described replacing change forms and the change board with automated approvals for cloud workloads: controls are defined programmatically ("Cloud Adoption Standards and Techniques", CAST), checked by code when a team launches an instance, tiered by stage from experiment to production, and every change is logged to ServiceNow, with the CMDB refreshed nightly. It is a first-party example of a regulated bank turning platform onboarding and change approval into a machine-checked contract, and of how automated logging fixed a records gap (many minor changes "had previously gone unrecorded").

## Themes
- governance-as-code: "So if you want to do a change, there's no form to fill in, there's no change board ... There are approvals that need to go through ... but they are all automated"; CAST lets the bank "programmatically define how we run our workloads in the cloud"; a Lambda function checks new instances against controls.
- platform-onboarding-friction: the old default "is no"; CAST changed the question to "Does it comply with CAST?"
- risk-sloped-review: controls tiered by stage: experiments need tagging and checks for bad behaviour but not multi-availability-zone resilience; by production all controls apply (tagging for purpose and owner, antivirus, code scanning, business continuity, multi-AZ).
- stale-records-mislead-agents: about 5,000 changes across 120 applications in one month (April 2019), many minor tweaks that had previously gone unrecorded; "100 percent" of activity now logged in ServiceNow; CMDB updated nightly with service maps.

## Key points
- Changes to packaged apps run through AWS Managed Services, triggered by API.
- Two-speed migration with a "migration factory" (Infosys, DXC) alongside AMS.

## Could not verify
- The scope of automation across NAB beyond cloud workloads, and how the regulator (APRA) viewed the change, are not reported.
