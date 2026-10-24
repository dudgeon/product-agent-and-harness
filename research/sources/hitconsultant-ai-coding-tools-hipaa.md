---
title: What AI coding tools are HIPAA compliant? (HIT Consultant)
source_url: https://hitconsultant.net/2026/08/03/what-ai-coding-tools-hipaa-compliant-world/
author: Anand Chandrasekaran (Arya Health)
publisher: HIT Consultant
published: 2026-08-03
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A practitioner in a regulated industry (healthcare engineering) reading the vendors' terms side by side. Its core point for a regulated deployment: ZDR and HIPAA eligibility attach to specific contracts and surfaces, not to a product name, and cloud agents are the usual exclusion. It corroborates the first-party exclusions (Claude Code cloud sessions excluded under HIPAA/ZDR; Codex local-with-Work-Cloud not strict ZDR).

## Themes
- enterprise-admin-controls (proposed): "Codex cloud... is incompatible with ZDR"; ZDR effectively covers only the local CLI and IDE extension; ZDR requires enterprise approval rather than self-service; standard API endpoints retain inputs/outputs up to 30 days for abuse monitoring.
- enterprise-admin-controls: Claude Code ZDR is "explicitly tied to the Anthropic API via direct commercial contract"; "Claude Code bundled seats are not currently covered as part of Anthropic's HIPAA-ready offering"; ZDR does not apply via Bedrock or Vertex; code-execution sandboxes keep data up to 30 days and "are not ZDR-eligible".
- vendor-claims-vs-independent-evidence: "Every major provider retains data for at least some period under safety monitoring obligations"; ZDR and HIPAA are distinct and neither is automatic.

## Key points
- Recommends auditing every AI tool a development team uses. Does not cover GitHub Copilot.

## Could not verify
- The Claude Code bundled-seat claim may be out of date relative to Anthropic's HIPAA configuration for Claude Code local mode (see [Cowork admin](anthropic-cowork-team-enterprise-admin.md)); the Codex-cloud ZDR claim is not stated in this form on OpenAI's fetched pages (OpenAI says local-with-Work-Cloud is not strict ZDR). Model-summarised fetch.
