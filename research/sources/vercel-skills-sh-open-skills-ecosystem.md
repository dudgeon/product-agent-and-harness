---
title: Introducing skills, the open agent skills ecosystem (Vercel)
source_url: https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem
author: Vercel
publisher: vercel.com
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skills-marketplace, harness-portability, skill-supply-chain-security]
relevance: medium
---

## Relevance to the project
A cross-harness installer and directory: `npx skills add <owner/repo>` copies a skill into each agent's native skills folder (project or global with `-g`), and skills.sh ranks skills by installs. It is the "npm for skills" layer; one of the two registries scanned in Snyk's ToxicSkills audit.

## Themes
- skills-marketplace: installer translates one repo into per-agent directories; claims 18+ agents in Vercel docs, 40-70+ in the CLI README (counts disagree).
- harness-portability: compatibility caveat that hooks and some features are agent-specific.

## Could not verify
- Only search-result summaries read; install semantics, pinning and update behaviour unchecked.
