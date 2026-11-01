---
title: "spec-kit templates and commands (spec, plan, tasks, constitution, checklist; clarify, analyze, converge)"
source_url: https://github.com/github/spec-kit/tree/main/templates
author: GitHub
publisher: github.com
published: unknown
retrieved: 2026-11-01
type: docs
evidence: first-party
filed_by: research-sdd-ready-intent
themes: [sdd-input-contracts, agent-ready-intent, artifact-standardization, dependency-types-and-practices]
relevance: high
---

## Relevance to the project
The current templates are the exact input contract a Spec Kit project consumes: what a spec.md must contain, how requirements and success criteria are numbered, where constraints and external dependencies go, and how tasks express blocking. They replace the second-hand layout in the earlier notes ([spec-driven.md](github-spec-kit-spec-driven.md), [Spec Kit and spec-driven.md](github-spec-kit-sdd.md)) with the files themselves, and show that Spec Kit has no field for a dependency on another team, an open ask or a gate: the nearest are "Assumptions" and the tasks' "Blocking Prerequisites" phase.

## Themes
- sdd-input-contracts: spec-template.md has three mandatory sections (User Scenarios & Testing; Requirements; Success Criteria) plus Edge Cases, Key Entities and Assumptions; requirements are "**FR-001**: System MUST ..."; success criteria "**SC-001**", measurable and technology-agnostic; unclear items "[NEEDS CLARIFICATION: ...]", capped at three per spec by the specify command.
- agent-ready-intent: user stories carry a priority (P1, P2, P3), a "Why this priority", an "Independent Test" and Given/When/Then acceptance scenarios; the checklist command calls its checklists "Unit Tests for English", testing the requirements' completeness and clarity, not the code.
- artifact-standardization: specs live in `specs/NNN-name/` (or a directory set by `SPECIFY_FEATURE_DIRECTORY`), with the resolved path written to `.specify/feature.json`; extensions are declared in `.specify/extensions.yml` with before/after hooks per command.
- dependency-types-and-practices: tasks-template.md has "Phase 2: Foundational (Blocking Prerequisites)" ("MUST be complete before ANY user story"), inline "(depends on T012, T013)", `[P]` for parallel and `[US1]` for the story; a "Dependencies & Execution Order" section. The spec's Assumptions section is where "Dependency on existing system/service" goes ("Requires access to the existing user profile API").

## Key points
- plan-template.md: Summary; Technical Context (language, primary dependencies, storage, testing, target platform, project type, performance goals, **Constraints**, scale; each may be "NEEDS CLARIFICATION"); **Constitution Check** (a gate before research and again after design); Project Structure; Complexity Tracking (only to justify constitution violations).
- constitution-template.md: Core Principles (named, with "NON-NEGOTIABLE" as an example marker); two free sections whose examples are "Additional Constraints, Security Requirements, Performance Standards" and "Development Workflow, Review Process, Quality Gates"; Governance; a version, ratified and amended date line. The analyze command loads `/memory/constitution.md` and treats any conflict as CRITICAL.
- clarify command: an ambiguity and coverage scan over a fixed taxonomy (functional scope; domain and data; interaction and UX; non-functional quality attributes including "Compliance / regulatory constraints"; **integration and external dependencies** ("External services/APIs and failure modes"); edge cases; constraints and trade-offs; terminology; completion signals; placeholders), each marked Clear, Partial or Missing; at most five questions, chosen by impact times uncertainty.
- analyze command: read-only cross-check of spec, plan and tasks: coverage (requirements with at least one task), duplication, ambiguity, constitution alignment, with severities CRITICAL to LOW.
- converge command: assesses the codebase against spec, plan and tasks and appends unbuilt work as new tasks.
- taskstoissues is deprecated in favour of a bundled GitHub extension that turns tasks into dependency-ordered issues.

## Could not verify
- The templates move quickly; this reflects `main` on the retrieval date. Raw files fetched directly, so wording is verbatim where quoted.
- Whether the three-marker cap and the five-question cap are enforced by code or only by the prompt (they are written in the command prompts).
