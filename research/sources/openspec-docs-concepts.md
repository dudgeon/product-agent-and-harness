---
title: "OpenSpec docs: Concepts, Writing Good Specs, Customization, Agent contract"
source_url: https://github.com/Fission-AI/OpenSpec/tree/main/docs
author: Fission AI
publisher: github.com
published: unknown
retrieved: 2026-11-01
type: docs
evidence: first-party
filed_by: research-sdd-ready-intent
themes: [sdd-input-contracts, agent-ready-intent, docs-as-code-prd, process-artifacts-as-coordination]
relevance: high
---

## Relevance to the project
OpenSpec's docs give the most explicit input contract of the lighter spec-driven tools: a living spec per capability made of "Requirement" blocks with one SHALL or MUST each and named GIVEN/WHEN/THEN scenarios, changed only through delta specs (ADDED, MODIFIED, REMOVED) inside a change folder. They also say outright that "external constraints (security, privacy, reliability, compatibility)" belong in the spec, and that project-wide context and per-artifact rules go in one config file. That config file is the obvious landing place for standing enterprise obligations, and the delta form matches how the intent record changes requirements over time.

## Themes
- sdd-input-contracts: "One statement, one SHALL/MUST"; "Observable"; SHOULD only "when you truly mean unless there's a good reason not to"; each scenario a concrete GIVEN/WHEN/THEN "that could become an automated test" (Writing Good Specs).
- agent-ready-intent: "A spec is a behavior contract, not an implementation plan"; good content includes "Observable behavior", "Inputs, outputs, and error conditions", "External constraints (security, privacy, reliability, compatibility)"; avoid class names, library choices and step-by-step plans (Concepts, What a Spec Is).
- docs-as-code-prd: canonical specs in `openspec/specs/<capability>/spec.md` (Purpose, Requirements); changes in `openspec/changes/<name>/` with proposal.md, design.md, tasks.md, `.openspec.yaml` and `specs/` deltas; archive merges deltas into the canonical specs (Concepts).
- process-artifacts-as-coordination: `openspec/config.yaml` holds `context:` (project facts, conventions, constraints, injected as "a required prompt-level input") and `rules:` per artifact (for example "Include rollback plan", "Identify affected teams" for proposals) (Customization; Agent contract).

## Key points
- Progressive rigour: "Lite spec (default)" against a "Full spec (for higher risk)" for cross-team or cross-repo changes, API or contract changes, migrations, security or privacy concerns.
- Custom schemas in `openspec/schemas/<name>/schema.yaml` can change the artifact set and templates; `.openspec.yaml` allows `x-*` keys of one's own on a change.
- The agent contract documents `openspec validate --json` and an `instructions apply` payload whose `state` is `blocked`, `ready` or `all_done`; "blocked" means required artifacts are missing, not that an outside party has not answered.
- Tasks are numbered checkbox groups ("1.1", "1.2") with no dependency or owner field.
- "OpenSpec doesn't touch git": committing, branching and review are the team's own (Team workflow).

## Could not verify
- Raw Markdown fetched directly from `main` on the retrieval date; quotes are verbatim. Docs undated.
