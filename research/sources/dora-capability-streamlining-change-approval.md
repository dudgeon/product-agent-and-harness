---
title: "Capabilities: Streamlining change approval"
source_url: https://dora.dev/capabilities/streamlining-change-approval/
author: DORA
publisher: DORA / Google Cloud
published: 2025-10-30
retrieved: 2026-10-28
type: docs
evidence: independent
filed_by: research-dependency-agent
themes: [process-governance-load, risk-sloped-review, governance-as-code, coordination-cost-and-waiting]
relevance: medium
---

## Relevance to the project
DORA's living capability guide turns its change-approval research into practice: peer review in the development platform for segregation of duties, continuous risk analysis to flag only high-risk changes for extra scrutiny, and the CAB recast from gatekeeper to coordinator. Its suggested measures (time spent waiting for approval, share of changes needing external approval by risk level, team confidence in the process) are exactly the instrumentation a dependency agent could collect. The page carries no figures of its own; it cites the 2019 report.

## Themes
- process-governance-load: external approval (a CAB or senior manager) hurts delivery performance; centralised CABs "add delay and error" because approvers are far from the change (Overview).
- risk-sloped-review: "Analyze risk continuously to flag high-risk changes for extra scrutiny"; pitfall: "Treating all changes equally" (Recommended practices; Common pitfalls).
- governance-as-code: shift validations into the development platform and implement security controls at platform and infrastructure layers rather than manual review (Recommended practices).
- coordination-cost-and-waiting: suggested metrics include "time changes spend waiting for external or local approval" and the proportion of changes requiring external approval by risk profile (Measuring).

## Key points
- CAB keeps a role: coordinating between teams, process improvement, high-level trade-offs such as time-to-market versus business risk.
- Pitfall: responding to production problems by adding process, which increases lead times and batch sizes.
- Recommends making the regular change process fast enough to handle emergency changes, removing the need for a separate emergency path.
- Recommends communicating the approval process clearly and helping teams navigate it, which the research links to higher performance.
