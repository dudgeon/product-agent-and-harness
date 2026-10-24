---
title: "Spec Kit and spec-driven.md (GitHub)"
source_url: https://github.com/github/spec-kit
author: GitHub
publisher: GitHub
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [prd-agents, artifact-standardization, docs-as-code-prd]
relevance: high
---

## Relevance to the project
Spec Kit is the most visible open-source convention for putting a feature spec in the repo as numbered, templated markdown. It shows a de facto folder layout for agent-readable specs, but it targets developers' features, not PM artifacts such as research or roadmaps.

## Themes
- artifact-standardization: defines a per-feature folder (`specs/003-chat-system/`) with spec.md, plan.md, research.md, data-model.md, contracts/, quickstart.md, tasks.md plus `memory/constitution.md` (spec-driven.md).
- docs-as-code-prd: spec is declared the source of truth ('Specifications don't serve code' is the doc's own framing); lives in git, one branch per feature.
- prd-agents: templates force `[NEEDS CLARIFICATION: ...]` markers instead of guessing, a spec-quality convention.

## Key points
- README: Spec Kit is an open source toolkit giving AI coding agents structured processes, templates and documented outcomes; `specify init` takes an `--integration` option for the agent (repo page did not list supported agents).
- spec-driven.md: slash commands `/speckit.specify`, `/speckit.plan`, `/speckit.tasks` generate the files; feature numbers auto-assigned by scanning existing specs.
- Constitution: project-wide principles file consulted on every change; templates include checklists and pre-implementation gates.
- Extensions write to `.specify/bugs/` and `.specify/assessments/`.

## Could not verify
- README did not document per-agent support or the exact current file layout; layout above is from spec-driven.md, which may differ from the current release.
- Star counts and adoption figures seen only in secondary summaries; not recorded.
