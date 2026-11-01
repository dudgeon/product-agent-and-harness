---
title: "Use Certification to Help Users Find Trusted Data"
source_url: https://help.tableau.com/current/server/en-us/datasource_certified.htm
author: Tableau (Salesforce)
publisher: Tableau Server help
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms, certified-metrics-layer]
relevance: medium
---

## Relevance to the project
A widely deployed tiered label for trusted data: a project leader or admin certifies a data source, it gets a badge, a note naming who certified it and why, and higher search ranking. It bears on the tiered-provenance-label and central-curator mechanisms: certification is a two-tier label (certified or not) granted by a role, its meaning is left to each organisation to define, and the product has no expiry or re-certification. A certified badge that never expires is the failure mode the project needs to avoid.

## Themes
- context-trust-mechanisms: "Certified data sources rank higher in search results and are added to recommended data sources"; the badge tooltip shows who certified the asset and an optional note on status and intended use (sections on certification effects and certification notes).
- certified-metrics-layer: certification "of the data that complies with your organization's data standards" marks which sources are trusted and recommended, for projects with similarly named or poorly described content (opening section).

## Key points
- Who can certify: server or site admins, or project owners and project leaders for that project; databases and tables need Tableau Catalog and the Set permissions capability (section "Who can certify").
- Best practice is organisational, not technical: define certification criteria, document and share them, per project or globally; "the key is that everyone understands what certification means" (best practices section). Admins can relabel the certification description.
- The help page says nothing about certification expiry or periodic re-certification (checked across the page). Certification persists until someone removes it.
- Certification also changes ranking: the label is not just informational; it steers what users and, by extension, agents pick up first.
