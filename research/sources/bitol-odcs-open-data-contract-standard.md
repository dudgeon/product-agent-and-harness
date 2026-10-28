---
title: "Open Data Contract Standard (ODCS)"
source_url: https://bitol-io.github.io/open-data-contract-standard/latest/
author: Bitol project (Linux Foundation AI & Data)
publisher: bitol-io.github.io
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-legible-platform, onboarding-as-code, decision-rights-for-agents]
relevance: high
---

## Relevance to the project
ODCS is the one widely used open standard where a provider's contract carries not only schema, quality and SLA but also who approves access: its Roles section lists the IAM role a consumer needs plus first- and second-level approvers. That is very close to the "intake contract" the dependency agent would read for a data platform: what you get, what quality and SLA it promises, who supports it, and who signs off access. Approvers are names in YAML, so they go stale unless synced from an identity or catalog system.

## Themes
- agent-legible-platform: contract sections: Fundamentals, Schema, Data Quality, Support & Communication Channels, Pricing, Team, Roles, SLA, Infrastructures & Servers, Authoritative Definitions, Tags, Custom properties (index).
- decision-rights-for-agents: Roles section: `role` (IAM role giving access), `access` (read/write), `firstLevelApprovers`, `secondLevelApprovers`, `description` (Roles page).
- onboarding-as-code: the contract is YAML and "platform agnostic", so a request can be checked against it before submission (Principles).

## Key points
- Since v3.1.0 each section has its own reference page.
- Approvers are free-text names, not identity references, in the example (one entry: `secondLevelApprovers: 'mickey'`).

## Notable quotes
- The Roles section "lists the roles that a consumer may need to access the dataset."

## Could not verify
- Current version number and Linux Foundation stewardship are not stated on the page read.
