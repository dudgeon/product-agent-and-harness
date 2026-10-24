---
title: "Governance posture: platform mapping"
source_url: https://handbook.gitlab.com/handbook/eta/ai/strategy/prompts-are-process/platform-mapping/
author: GitLab Enterprise Technology and AI (ETA)
publisher: GitLab Handbook
published: 2026-09-08
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [scoped-governance-containers, skills-marketplace, non-engineer-builders, org-learning-loop]
relevance: high
---

## Relevance to the project
A rare adopter-written (not vendor) account of how a large company maps one governance posture ("guided creation": anyone builds; promotion to a canonical shared version is owned and reviewed) onto two agent platforms, Claude (Chat, Cowork, Code) and Glean. It states plainly where each platform can and cannot enforce function scoping: Glean can scope agents to departments and IdP groups with Department Agent Moderators; Claude cannot (connectors and skill sharing are org-wide), so ownership, not tooling, holds the line; Claude Code's repo-scoped skills reviewed by merge request are "the tidiest expression". Directly relevant to how a regulated company would govern an intent-shaping agent and its skills across surfaces.

## Themes
- scoped-governance-containers: three scopes (function, repo, company-wide); Glean supports per-department scoping, Claude does not.
- skills-marketplace: company-wide AI marketplace resources must be self-contained.
- non-engineer-builders: Glean defaults let members create and share agents peer-to-peer but not publish company-wide.
- org-learning-loop: promotion from personal to canonical through an owner and review.

## Key points
- Glean controls: Default Member permissions (create on, share-with-teammate on, publish off, share-with-company off); Agent Moderator and Department Agent Moderator roles verify and brand agents; per-agent Viewer/Editor/Owner tiers plus document permissions.
- Claude: user-created skills and skill sharing toggles; share-with-organisation off; team plugins for scoped distribution; connectors org-wide on/off.
- Claude Code: skills in `.claude/skills/`, CODEOWNERS, git, merge request review; enforcement is technical.
- Open items: whether to define a "tighten" profile for sensitive or regulated surfaces.

## Notable quotes
- "Claude cannot do this today. Connectors are org-wide on or off and cannot be scoped per team, and skill-sharing is org-level."
- "Either way the principle leads and the platform follows"

## Could not verify
- Retrieved by curl and text extraction (verbatim). Claude admin behaviour described as of GitLab's writing (sources Mar-Apr 2026, page last modified 2026-09-08); may have changed.
