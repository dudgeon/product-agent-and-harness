---
title: "CMDB Health KPIs and metrics"
source_url: https://www.servicenow.com/docs/bundle/zurich-servicenow-platform/page/product/configuration-management/reference/r_CMDBHealthMetrics.html
author: ServiceNow
publisher: ServiceNow product documentation (Zurich release)
published: 2025-07-31
retrieved: 2026-10-28
type: docs
evidence: vendor-claim
filed_by: research-dependency-agent
themes: [stale-records-mislead-agents, dependency-types-and-practices, legible-org-for-agents]
relevance: high
---

## Relevance to the project
ServiceNow's configuration management database (CMDB), the system of record for configuration items and their relationships in most large banks, insurers and healthcare organisations, ships with built-in metrics for its own decay: completeness, compliance and correctness, where correctness counts orphaned, duplicate and stale items and relationships. That the vendor builds staleness scoring into the product, with a default of 60 days without update, is first-hand evidence that the enterprise dependency record goes stale by default and that someone must govern it. A dependency agent reading a CMDB should read these health scores too.

## Themes
- stale-records-mislead-agents: Staleness counts configuration items (CIs) not updated within a rule's Effective Duration; the base system rule "sets the Effective Duration time to 60 days" (§Correctness). Stale relationships are those where "the parent CI or the child CI is a stale CI" (§Relationships).
- dependency-types-and-practices: the CMDB records system dependencies as typed parent-child relationships; health metrics flag duplicate relationships and orphan relationships "missing either a parent CI, a child CI, or both" (§Relationships).
- legible-org-for-agents: Compliance compares "actual values of specified fields, against expected values defined in template and scripted audits", but "Audit must be activated for the compliance KPI to show results" (§Compliance).

## Key points
- Completeness: percentage of CIs with mandatory fields unpopulated (Required) and recommended fields unpopulated (Recommended; none recommended out of the box).
- Correctness: Orphan ("unintentionally left in the CMDB when it is no longer needed"), Staleness, Duplicate (via identification rules; only independent CIs evaluated).
- Overall health is a weighted blend of the three KPIs (per ServiceNow community and docs summaries seen in search; weights not read here).
