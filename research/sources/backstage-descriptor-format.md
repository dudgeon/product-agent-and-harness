---
title: "Descriptor Format of Catalog Entities (Backstage)"
source_url: https://backstage.io/docs/features/software-catalog/descriptor-format
author: Backstage / Spotify (CNCF)
publisher: backstage.io
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [artifact-standardization, legible-org-for-agents]
relevance: high
---

## Relevance to the project
Backstage is the strongest existing example of a repo-resident manifest that makes entities, owners and relations discoverable across an organisation. A PM equivalent (project, initiative, artifact with owner, lifecycle) could reuse this envelope.

## Themes
- artifact-standardization: Kubernetes-style envelope (`apiVersion`, `kind`, `metadata` name/title/description/tags/links/labels/annotations, `spec`); relations are generated, not hand-written.
- artifact-standardization: required fields include `spec.owner` and `spec.lifecycle` (experimental, production, deprecated, extensible); System groups components, Domain groups systems (a built-in grouping hierarchy).
- legible-org-for-agents: annotations link entities to external systems; owner field is for display, not authorization.

## Key points
- Entities are files in repos discovered by the catalog; the same structure serves JSON via API.

## Could not verify
- No PM-specific kinds exist; applicability to product artifacts is an inference.
