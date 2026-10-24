---
title: "Specs (Kiro docs)"
source_url: https://kiro.dev/docs/specs/
author: Amazon / Kiro
publisher: kiro.dev
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [prd-agents, artifact-standardization, docs-as-code-prd]
relevance: medium
---

## Relevance to the project
Kiro is the IDE-vendor version of spec-driven development: a three-file spec per feature (requirements, design, tasks). It is a second independent convention alongside Spec Kit, which shows the file set is not standardised across tools.

## Themes
- artifact-standardization: three-file spec per feature with three phases (requirements/bug analysis, design, tasks); Spec Kit uses a different file set for the same job.
- docs-as-code-prd: specs are plain markdown files the agent keeps updated (task status); storage path not stated on the page fetched.

## Key points
- requirements.md holds user stories and acceptance criteria; bugfix.md captures current, expected and unchanged behaviour.
- design.md: architecture, sequence diagrams, data flow, error handling, testing strategy.
- tasks.md: discrete tasks whose status Kiro updates; independent tasks grouped into concurrent waves.

## Could not verify
- Page did not state where spec files are stored, EARS notation, or steering file contents (the Böckeler article says Kiro uses a steering folder with product/tech/structure files and GIVEN/WHEN/THEN criteria; second-hand here).
- The /docs/specs/concepts/ URL returned 404.
