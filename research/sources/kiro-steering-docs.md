---
title: Steering (Kiro docs)
source_url: https://kiro.dev/docs/steering/
author: Kiro (AWS)
publisher: kiro.dev
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [org-context-grounding, process-artifacts-as-coordination, docs-as-code-prd]
relevance: medium
---

## Relevance to the project
Steering files are Kiro's standing-context layer beside its per-feature specs: product.md, tech.md and structure.md, with inclusion modes that decide when each loads. They are the IDE-vendor version of CLAUDE.md and Spec Kit's constitution, and show a split between always-on standards and conditionally loaded guidance that a PM skill library would also need.

## Themes
- org-context-grounding: product.md (purpose, users, goals), tech.md (stack, constraints), structure.md (organisation, naming, architecture) included in every interaction by default (body).
- process-artifacts-as-coordination: global steering in ~/.kiro/steering can be distributed by MDM or Group Policy, or pulled from a central repo, so a team shares one standard (body).
- docs-as-code-prd: workspace steering in .kiro/steering/ overrides global on conflict (body).

## Key points
- Inclusion modes in front matter: always (default), fileMatch (glob), manual (#filename or slash command), auto (loaded when the request matches a description).
- Supports AGENTS.md at workspace root, in subdirectories and in ~/.kiro/steering; AGENTS.md always loads, no inclusion modes.
- Custom agents do not get steering automatically; add the steering path to the agent's resources.
- Kiro Web cannot read local global steering; upload via Configuration Sync.
- My judgment: inclusion modes are a deterministic routing rule over advisory content, i.e. the gate is fixed but the content is still a model-read instruction.

## Could not verify
- Retrieved via WebFetch, a model-summarised view.
