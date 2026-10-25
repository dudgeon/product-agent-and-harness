---
title: OpenSpec (Fission-AI/OpenSpec README)
source_url: https://github.com/Fission-AI/OpenSpec
author: Fission AI
publisher: GitHub
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [docs-as-code-prd, process-artifacts-as-coordination, agent-ready-intent]
relevance: medium
---

## Relevance to the project
OpenSpec is the lightweight rival to Spec Kit and Kiro: each change gets its own folder of process artifacts (proposal, spec deltas, design, tasks) that is archived into the living spec once shipped. It shows a spec-driven toolchain that treats the change proposal, not the full spec, as the unit of review, which matters for how a PM agent would stage review in a multi-party repo.

## Themes
- docs-as-code-prd: per-change folder `openspec/changes/<name>/` with proposal.md, specs/, design.md, tasks.md (README).
- process-artifacts-as-coordination: `/opsx:archive` moves the change to `changes/archive/<date>-<name>/` and updates the canonical specs, so the change record and the end-product spec are separate artifacts (README).
- agent-ready-intent: requirements in Markdown with SHALL and WHEN/THEN scenarios, headed as "ADDED Requirements" (delta form) (README).

## Key points
- Default commands: `/opsx:explore` (thinking partner before committing), `/opsx:propose`, `/opsx:apply`, `/opsx:archive`; expanded profile adds new, continue, ff (fast-forward), verify, bulk-archive, onboard.
- Human gate is stated as review of the plan before code: "Your AI writes these; you review the plan before any code is written."
- The README does not describe what the CLI validates; deterministic enforcement is not documented on this page.
- Self-positioning: Spec Kit is "thorough but heavyweight" with rigid phase gates; Kiro locks you into its IDE. OpenSpec claims to be lighter and tool-agnostic (vendor-claim).
- About 72.9k stars and 5.0k forks at retrieval.

## Could not verify
- Whether the CLI validates spec delta structure (a `validate` command may exist; not shown on the README as fetched).
- Retrieved via WebFetch, a model-summarised view.
