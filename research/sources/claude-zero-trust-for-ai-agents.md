---
title: Zero Trust for AI agents
source_url: https://claude.com/resources/articles/zero-trust-for-ai-agents
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-05-27
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-protocol-security, identity-delegation, enterprise-admin-controls, policy-enforcement-fail-open, memory-architecture]
relevance: medium
---

## Relevance to the project
Anthropic's tiered Zero Trust framework for enterprise agents gives a regulated organisation a ready-made control checklist (identity, scoped privilege, sandboxing, tracing, memory integrity, governance) against which any PM-agent harness option can be graded. It matters for the agent-identity, governance-control-plane and trust defaults dimensions: it sets per-agent cryptographic identity, short-lived tokens and deny-by-default as the entry floor, not an aspiration. It is a security guide, not a PM source, and every "pro-tip" maps controls back to Claude Code features, so it doubles as product positioning.

## Themes
- agent-protocol-security: Ch 04 catalogues tool poisoning, MCP rug pulls, tool-chaining exfiltration and loop amplification; Ch 06 Phase 2 advises self-hosting and signing verified MCP servers.
- identity-delegation: Ch 04 names "unscoped privilege inheritance" (manager agent passes full access to workers) and the confused-deputy problem; Ch 06 Phase 6 requires per-agent credentials and authorization checks at each hop of a multi-agent workflow.
- enterprise-admin-controls: Ch 05 governance tier table (acceptable-use policy, cross-functional AI committee, then automated policy checks in pipelines); Claude Code managed settings and `allowManagedPermissionRulesOnly` cited.
- policy-enforcement-fail-open: Ch 02 "impossible, not tedious" test: friction controls (rate limits, extra hops, SMS MFA) fail against patient agentic attackers; Ch 05 cites fail-closed matching for unrecognised commands.
- memory-architecture: Ch 06 Phase 7 memory isolation, hash-based context integrity checks at every retrieval, source tagging, TTLs and versioned memory rollback.

## Key points
- Packaging: a short launch article (2026-05-27) fronts a nine-part guide (about 69 minutes of reading) at claude.com/resources/guides/zero-trust-for-ai-agents. Ch 01 positions it as "Anthropic's current thinking", not legal, compliance or security assurance.
- Tier names are inconsistent: the launch article lists "Foundation, Advanced, and Optimized"; the guide's tier tables (Ch 05) use Foundation, Enterprise and Advanced. This note follows the guide.
- Ch 03 defines blast radius and adopts OWASP's "least agency" (restrict what each tool can do, how often and where; e.g. email summariser with no send/delete). Lists Zero Trust guidance from the US (CISA, NSA ZIGs, NIST SP 800-207), UK (NCSC) and Australia; states US federal agencies must adopt Zero Trust by 2027.
- Ch 05 raised floor: Foundation now requires cryptographically rooted agent IDs, IdP-issued tokens with lifetimes in minutes (static API keys "no longer a legitimate entry point"), RBAC deny-by-default, identity-based isolation (network segmentation only a backstop), action logs with request IDs, version-controlled agent configs, documented rollback, and model-drafted first-pass alert triage.
- Ch 05 Enterprise adds X.509 certs and mTLS, ABAC, dynamic privilege elevation, per-agent sandboxes (gVisor named; "table stakes" for any agent handling untrusted input), immutable audit logs, OpenTelemetry tracing across agents, signed configs, automated rollback, a cross-functional AI governance committee. Advanced adds hardware-backed identity and attestation, JIT/JEA access, continuous authorization, confidential computing, full provenance chains with decision replay, and human-in-the-loop approval for high-risk actions (placed under output filtering).
- Ch 06 eight-phase workflow: requirements; supply chain (AI-BOM, OpenSSF Scorecard, reachability analysis, "AI vendoring" small unmaintained dependencies by having a model reimplement them); agent boundaries (written approved/prohibited actions, escalation triggers, scope limits, blast radius); prompt-injection defences; tool allow-listing enforced both inside and outside the agent; credentials; memory; measurement.
- Ch 06 compartmentalisation tip: split an agent into several only if each gets its own identity and credentials; shared credentials defeat the split.
- Ch 06 notes Claude Code sub-agents can inherit up to the parent's permissions and look identical from outside; the distinction is visible only in OpenTelemetry or local JSONL transcripts. This is a candid limit for anyone relying on per-subagent attribution.
- Ch 05/07 rule: "automate the bookkeeping around incidents, not the decisions": models gather evidence and draft write-ups; humans make containment, disclosure and customer-comms calls. Start agentic triage on one noisy alert rule and measure agreement with a human for two weeks.
- Ch 06 Phase 8 metrics: dwell time and alert coverage first; target detection within an hour for critical systems; explainability (trace any action to its triggering input) is "not optional" in regulated industries.
- Third-party figures are cited, not Anthropic's own: Spotlighting cuts indirect injection success from over 50% to under 2% (Microsoft); constitutional classifiers blocked 95% of jailbreaks in Anthropic testing; 250 poisoned documents can backdoor 600M-13B parameter models (Anthropic research).
- Missing: no PM- or knowledge-work-specific agent examples; no cost or effort estimates per tier; no evidence any customer implemented the tiers.

## Notable quotes
- "does this make the attack impossible, or just tedious?" (Ch 02)
- "automate the bookkeeping around incidents, not the decisions" (Ch 05)

## Companion pages
- https://claude.com/resources/guides/zero-trust-for-ai-agents (landing)
- .../building-for-the-next-threat-landscape (Ch 01)
- .../the-principles-behind-zero-trust (Ch 02)
- .../security-considerations-for-autonomous-systems (Ch 03)
- .../current-threats-to-agentic-systems (Ch 04)
- .../applying-zero-trust-to-agentic-ai-services (Ch 05)
- .../agent-implementation-workflow (Ch 06)
- .../defensive-operations-at-the-speed-of-autonomous-threats (Ch 07)
- .../from-principles-to-practice (Ch 08)

## Could not verify
- Guide chapters show no publication date; the date above is the launch article's. Which tier naming is current.
