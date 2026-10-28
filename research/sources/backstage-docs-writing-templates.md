---
title: "Writing Templates (Backstage Software Templates)"
source_url: https://backstage.io/docs/features/software-templates/writing-templates
author: Backstage project (CNCF)
publisher: backstage.io
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [onboarding-as-code, agent-legible-platform]
relevance: high
---

## Relevance to the project
Backstage Scaffolder templates are the most widespread "intake as a schema" in platform engineering: each template's inputs are JSON Schema (rendered with react-jsonschema-form), so a platform's golden-path request form is already machine-readable and could be read and filled by an agent. What the template format lacks is approval: templates run steps; any human sign-off has to be built into a step or happen in the PR the template opens.

## Themes
- onboarding-as-code: "Each `Step` is `JSONSchema` with some extra goodies for styling"; steps are a series of actions with `id`, `if`, `each`, `action`, `input`, and outputs referenced as `steps.$id.output.*` (Parameters, Steps).
- agent-legible-platform: catalog-aware fields (`OwnerPicker` filtered by `catalogFilter`, `RepoUrlPicker` limited by `allowedHosts`/`allowedOwners`) tie the intake to the ownership graph (Custom fields).

## Key points
- Secrets marked with `ui:field: Secret` are referenced as `${{ secrets.key }}` and may be passed programmatically "via CI/CD pipelines or API calls"; a missing required secret returns 400.
- `output.links` / `output.text` return results (e.g. repo URL, catalog entity) to the requester.
- No approval, SLA or reviewer construct exists in the template format on this page.

## Could not verify
- Scaffolder permission rules ("Authorizing scaffolder tasks") were linked but not read.
