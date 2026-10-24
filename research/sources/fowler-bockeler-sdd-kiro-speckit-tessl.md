---
title: "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl"
source_url: https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
author: Birgitta Böckeler
publisher: martinfowler.com
published: 2025-10-15
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: user-story-mapping
themes: [prd-agents, artifact-standardization, docs-as-code-prd, agent-failure-modes]
relevance: high
---

## Relevance to the project
The best independent evidence on how consistent spec-in-repo practice is: definitions are in flux, tools differ in layout, and maintenance of specs after the task is vague. It also flags that it is unclear whether SDD is for developers or product people.

## Themes
- docs-as-code-prd: three levels (spec-first, spec-anchored, spec-as-source); all tools are spec-first, few commit to spec-anchored; spec-kit creates a branch per spec so specs behave like change requests.
- artifact-standardization: three different layouts (Kiro steering + per-feature folders; spec-kit constitution + numbered folders of ~8 files; Tessl `.tessl/framework` plus `*.spec.md`). Memory-bank files (AGENTS.md) distinguished from task specs.
- agent-failure-modes: spec-kit ignored research notes and duplicated existing classes; over-applied constitution; Tessl regeneration non-deterministic.
- prd-agents: unclear target user (developers, product people, or both); Kiro turned a small bug into 4 stories / 16 acceptance criteria.

## Key points
- Review burden: many repetitive markdown files were tedious to review; she would rather review code.
- Tension with iterative small steps; MDD (model-driven development) parallel as a warning for spec-as-source.
- Published date taken from search summary ('October 2025'); exact day not verified.

## Could not verify
- Exact publication date not verified (October 2025 per search snippet).
