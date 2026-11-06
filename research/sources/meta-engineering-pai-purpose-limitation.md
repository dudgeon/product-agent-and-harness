---
title: "How Meta enforces purpose limitation via Privacy Aware Infrastructure at scale"
source_url: https://engineering.fb.com/2024/08/27/security/privacy-aware-infrastructure-purpose-limitation-meta/
author: Wenlong Dong, Rituraj Kirti, Diana Marsala, Kendall Hopkins, Lucas Waye and others
publisher: Engineering at Meta
published: 2024-08-27
retrieved: 2026-11-06
type: article
evidence: first-party
filed_by: design-requirements-agent
themes: [governance-as-code, obligation-libraries-as-data, rules-vs-judgment-encoding]
relevance: medium
---

## Relevance to the project
Meta's engineering account of moving a privacy obligation (purpose limitation) from point checks in code to infrastructure: data assets carry labels with data-flow rules, "zones" check flows at runtime, and a requirement owner is guided through identifying assets, tracing lineage, remediating and then enforcing. It shows the downstream end of the chain a requirements agent starts: once an obligation is stated as a requirement with an owner, the platform can make it enforceable, and a single requirement can touch hundreds or thousands of engineers. That matters for the agent's handoff: a requirement sourced to a privacy obligation should name the platform control that enforces it where one exists.

## Themes
- governance-as-code: Policy Zones: annotations at table, column, row or cell level carry flow rules; zones run in logging mode, then enforcement mode where new disallowed flows are blocked even as code changes.
- obligation-libraries-as-data: the Policy Zone Manager guides "requirement owners" through four steps (identify assets, discover downstream flows via lineage, remediate, enforce and monitor); verifiers check annotation accuracy.
- rules-vs-judgment-encoding: point checking with if-statements and ACLs was "fragile" and needed exhaustive code audits; it did not scale to requirements spanning dozens of systems.

## Key points
- Lessons: build one end-to-end use case before generalising; build language libraries; invest early in efficiency (10x computational gains after simplifying policy representation); keep annotations simple and independent so requirements do not conflict; build tooling early.
- The post does not describe Meta's privacy review process itself; requirements arrive from privacy policy owners.

## Could not verify
- Read through WebFetch's model-summarised view. Meta's 2025 Policy Zones batch-processing post and its June 2026 "asset classification case study" were seen in search results only.
