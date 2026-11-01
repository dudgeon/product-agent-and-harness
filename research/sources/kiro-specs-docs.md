---
title: "Specs (Kiro docs)"
source_url: https://kiro.dev/docs/specs/
author: Amazon / Kiro
publisher: kiro.dev
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [prd-agents, artifact-standardization, docs-as-code-prd, sdd-input-contracts]
relevance: medium
---

## Relevance to the project
Kiro is the IDE-vendor version of spec-driven development: a three-file spec per feature (requirements, design, tasks). It is a second independent convention alongside Spec Kit, which shows the file set is not standardised across tools.

## Themes
- artifact-standardization: three-file spec per feature with three phases (requirements/bug analysis, design, tasks); Spec Kit uses a different file set for the same job.
- docs-as-code-prd: specs are plain markdown files the agent keeps updated (task status); storage path not stated on the page fetched.

## Key points
- requirements.md holds user stories and acceptance criteria; bugfix.md captures current, expected and unchanged behaviour.
- design.md: architecture, sequence diagrams, data flow, error handling, testing strategy.
- tasks.md: discrete tasks whose status Kiro updates; independent tasks grouped into concurrent waves.

## Could not verify
- Page did not state where spec files are stored, EARS notation, or steering file contents (the Böckeler article says Kiro uses a steering folder with product/tech/structure files and GIVEN/WHEN/THEN criteria; second-hand here).
- The /docs/specs/concepts/ URL returned 404.

## Added by research-sdd-ready-intent (2026-11-01)
Further Kiro docs pages read (all first-party, model-summarised fetches): [feature specs](https://kiro.dev/docs/specs/feature-specs/), [requirements-first](https://kiro.dev/docs/specs/feature-specs/requirements-first/), [best practices](https://kiro.dev/docs/specs/best-practices/), [analyze requirements](https://kiro.dev/docs/specs/analyze-requirements/), [correctness](https://kiro.dev/docs/specs/correctness/).
- sdd-input-contracts: requirements.md holds requirements in EARS notation, "WHEN [condition/event] THE SYSTEM SHALL [expected behavior]" (feature specs); organised by feature heading and sub-heading, with user stories, acceptance criteria, functional requirements and edge cases (requirements-first). The notation's source is [EARS](alistairmavin-ears.md).
- Location: the best-practices page shows `.kiro/specs/<feature>/` and says to "Store specs directly in your project repository alongside the code they describe"; across teams it suggests "a central specs repository" linked by Git submodules, package references or symbolic links, with a cross-repository review process.
- Import: requirements that "already exist in another system (such as JIRA, Confluence, or Word documents)" can be pulled in over MCP or pasted into a file, then turned into a spec in a spec chat (best practices).
- Workflows: requirements-first, design-first, and Quick Spec (all three phases without approval gates). Each phase is confirmed by a person before the next is generated; editing requirements.md and asking Kiro updates design and tasks.
- tasks.md: discrete tasks with expected outcomes, dependencies between tasks, and optional vs required marking; "Run all Tasks" runs only incomplete required tasks. No owner, external-party or blocked field documented.
- No dedicated non-functional section: design-first is recommended when the system "must meet strict non-functional requirements (latency, throughput, compliance)"; the design review checklist includes "Non-functional requirements are addressed".
- Analyze Requirements (optional, before design): looks for logical inconsistencies, ambiguities, conflicting constraints (functional vs non-functional), unstated assumptions and missing edge cases; model reasoning, not stated as deterministic.
- Correctness properties: Kiro extracts universal properties from EARS requirements during design and runs property-based tests against the implementation, with a traceable link from property to requirement and task; optional by default; "evidence of correctness, not a proof".
