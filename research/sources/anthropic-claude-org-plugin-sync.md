---
title: Sync your organization's plugins from a repository (claude.com docs)
source_url: https://claude.com/docs/plugins/org-sync
author: Anthropic
publisher: claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skills-marketplace, org-learning-loop, harness-portability]
relevance: medium
---

## Relevance to the project
Documents the Git-backed private marketplace route for Claude/Cowork: an admin syncs a private GitHub/GitLab repo containing marketplace.json; plugins reach claude.ai, Cowork and Claude Code with availability set per plugin (available / installed by default / required). Same pattern as Ramp's Dojo (Git as source of truth) but productised.

## Themes
- skills-marketplace: sync on push to default branch via webhook; marketplace repo must be private or internal; plugin sources must be github/url/git-subdir or relative paths; members need no repo access.
- harness-portability: a plugin with a top-level `bin/` is rejected by claude.ai/Cowork, so one plugin package is not uniformly deployable across Claude surfaces.

## Key points
- GitLab sync is public beta, needs an access token per host.
- Rollout guidance page distinguishes claude.ai/Cowork members from Claude Code CLI developers.

## Could not verify
- Adoption or failure reports.
