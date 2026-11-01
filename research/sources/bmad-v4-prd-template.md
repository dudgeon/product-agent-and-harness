---
title: "BMAD-METHOD prd-tmpl.yaml (v4.44.3)"
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/v4.44.3/bmad-core/templates/prd-tmpl.yaml
author: BMad Code
publisher: github.com
published: unknown
retrieved: 2026-11-01
type: docs
evidence: first-party
filed_by: research-sdd-ready-intent
themes: [sdd-input-contracts, artifact-standardization]
relevance: medium
---

## Relevance to the project
BMAD's PRD template is the one spec-driven input that keeps functional and non-functional requirements as two numbered lists (FR1..., NFR1...), which is the nearest of the tools to the project's attribute axis and the easiest to map a faceted requirement record onto. Its epic and story sections then carry numbered acceptance criteria that are told to include "any critical non-functional requirements from the PRD", so the NFRs reach the build unit.

## Themes
- sdd-input-contracts: section `requirements` with child `functional` (prefix FR: "Each Requirement will be a bullet markdown and an identifier sequence starting with FR") and `non-functional` (prefix NFR); example "NFR1: AWS service usage must aim to stay within free-tier limits where feasible."
- artifact-standardization: other sections are Goals and Background Context (with a change log), User Interface Design Goals (accessibility level "None | WCAG AA | WCAG AAA | Custom"), Technical Assumptions (repository structure, service architecture, testing requirements), Epic List and Epic Details with stories.

## Key points
- The template is YAML that drives an elicitation dialogue; output is Markdown.
- This is the v4 generation; newer BMAD (V6 stable, V7 in preview) uses a `bmad-prd` skill and a ticket tree with plan files whose status can be `blocked` with a reason ([autonomous loops](bmad-docs-autonomous-development-loops.md); [plan inside an organization](bmad-docs-plan-inside-an-organization.md)).

## Could not verify
- Whether the current-generation PRD skill keeps the FR/NFR split; community templates for the newer versions suggest it does, but the upstream file was not located. Raw YAML fetched directly; quotes verbatim.
