---
title: "MADR: Markdown Architectural Decision Records"
source_url: https://adr.github.io/madr/
author: ADR GitHub organisation
publisher: adr.github.io
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [artifact-standardization, docs-as-code-prd]
relevance: high
---

## Relevance to the project
ADR/MADR is the one decision-record convention with real, long-lived adoption and a fixed file location, naming scheme and lifecycle status. It is the clearest precedent for a typed, versioned, in-repo document standard that a PM-side artifact (decision, PRD) could copy.

## Themes
- artifact-standardization: location `docs/decisions/`, name `NNNN-title-with-dashes.md`; frontmatter `status` (proposed, accepted, rejected, deprecated, superseded), `date`, `decision-makers`, `consulted`, `informed`.
- docs-as-code-prd: sections Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome (Consequences, Confirmation), Pros/Cons; versioned with code.

## Key points
- Large projects may group ADRs in category subfolders, making numbers unique only per category.

## Could not verify
- Adoption breadth not measured here.
