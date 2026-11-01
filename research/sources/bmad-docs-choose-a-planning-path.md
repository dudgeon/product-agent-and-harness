---
title: "Choose a Planning Path (BMad Method docs)"
source_url: https://docs.bmad-method.org/plan/choose-a-planning-path/
author: BMad Code
publisher: docs.bmad-method.org
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, relay-information-loss, work-structure-spectrum]
relevance: high
---

## Relevance to the project
BMAD is the most elaborated role-to-role document relay in the open (analysis skills, PRD, UX, architecture, a product-owner agent "Sofia" that slices epics into tickets, then one Build per story). This page states plainly that dividing work loses information and that the durable documents exist "so later sessions can still see the whole". It is a first-party account of model A as a method, with the person choosing the path.

## Themes
- process-artifacts-as-coordination: each artifact has a producing skill: product brief / PRFAQ, PRD (`bmad-prd`), UX files, `architecture-<slug>.md`, epic and story requirements and `tickets.toml` (Sofia), build plans (`bmad-build`, one per story).
- relay-information-loss: "Dividing work can lose information: a requirement weakens, a constraint disappears"; "Hand her a pile of raw documents several times that size and she silently loses the parts that mattered; condense them first."
- work-structure-spectrum: "The answer turns on one question: is the intent already well defined?" Sizes: trivial, one session, epic (several Build sessions), project (about 20+ sessions).

## Key points
- Who decides the next step: in an installed project, `bmad` (the help skill) recommends the next skill; the person runs it. For epics, Sofia orders stories; you run Build once per story; stories with `refine = true` get refined first; epics close with `bmad-retrospective`.
- "The breakdown is an execution plan, not a promise that nothing will change."
- Version context: the README says v6.12 is stable and V7 is in preview (installable as a Claude Code or Codex plugin, target mid-November 2026); these docs read like the newer generation (Sofia, tickets.toml), not the v4 SM/Dev/QA cycle (see bmad-v4-knowledge-base).

## Could not verify
- Which version these docs describe exactly; page undated. Retrieved via WebFetch (model-summarised).
