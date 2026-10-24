---
title: "CISO Briefing: Agent Context Poisoning: SKILL.md and the New AI Supply Chain Attack Surface"
source_url: https://labs.cloudsecurityalliance.org/research/briefing-csa-research-note-skill-md-agent-context-poisoning/
author: Cloud Security Alliance (AI Safety Initiative)
publisher: CSA Labs
published: 2026-05-06
retrieved: 2026-10-24
type: report
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-supply-chain-security, skills-marketplace]
relevance: medium
---

## Relevance to the project
Neutral-body governance view: skills, CLAUDE.md and AGENTS.md should be treated as untrusted third-party code; scanners that look for binaries miss natural-language payloads. Gives a checklist (internal registry with signing and audit logging, content-hash verification, Unicode tag stripping) that maps onto a private marketplace design.

## Themes
- skill-supply-chain-security: poisoned instructions in skill bodies; invisible Unicode Tag characters (patched in Claude Code 2026-02-10); repository `.claude/settings.json` hooks; two Claude Code CVEs cited (CVE-2025-59536, CVE-2026-21852).
- skills-marketplace: recommends "an internal skill registry with signing and audit logging".

## Key points
- Recycles the Snyk 36.82% / 13.4% / 76 figures and the 341-skill ClawHavoc campaign; not new measurement.

## Could not verify
- CVE details and patch versions not independently checked.
