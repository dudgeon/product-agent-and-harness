---
title: "CISO's guide to agentic AI"
source_url: https://claude.com/resources/articles/ciso-guide-to-agentic-ai
author: Jason Clinton (Deputy CISO, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-07-17
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [identity-delegation, enterprise-admin-controls, agent-protocol-security, human-review-gates, agent-control-plane]
relevance: medium
---

## Relevance to the project
Anthropic's Deputy CISO gives a four-question risk test for any agent (untrusted input, actions and on whose behalf, blast radius, observability) and an identity spectrum from service account to human credential, which is close to the vocabulary a regulated company would need to approve a PM agent. It also states seven concrete controls and how Cowork meets each, including the admission that Cowork activity was then not in the Compliance API or formal audit logs. The incident-response case (an agent upgraded to a new model began reaching another agent to fix production on its own) is a rare first-party account of emergent behaviour inside a bounded deployment. Bears on agent-identity-delegation, governance-control-plane and review-and-autonomy.

## Themes
- identity-delegation: "agentic identity spectrum": service account (single-purpose, no human identity, e.g. incident agent, Claude Tag) vs human credential (Cowork on a laptop); the middle, delegated identity in systems the person isn't watching, is where "accountability gets ambiguous" (section "The agentic identity spectrum").
- enterprise-admin-controls: seven controls, each stated as a generic requirement then as Cowork's implementation: IdP identity (SAML/OIDC, SCIM, custom roles), two-gate connector allowlist, per-tool per-action approval, sandbox without credentials, egress allowlist, OTel to SIEM, org-wide off switch (section "Case study: Claude Cowork").
- agent-protocol-security: prompt injection named as a main internal risk; egress allowlisting called "your strongest control against prompt injection"; connector tokens injected by a reverse proxy so the sandbox never holds them.
- human-review-gates: in the incident case, the only write-like action (a code change) still went to a PR a human reviewed; GRC lesson that accepting risk "is an act performed by humans with the authority to accept it".
- agent-control-plane: telemetry should be "a stream you can point somewhere, not a dashboard you have to visit"; per-tool OTel events with user identity.

## Key points
- Four questions: (1) what untrusted content does it ingest (if none, agent-specific risk "near zero", move quickly); (2) what actions, under whose identity; (3) blast radius as scope x severity; (4) observability: can you tell agent actions from user actions, does it land in the SIEM.
- Principle of least agency plus "admin-paced rollout" (small group, watch telemetry, expand) is Anthropic's stated default posture.
- Framing: a misaligned agent is "indistinguishable from an insider attack"; cites Ponemon 2026 (67 days average to contain an insider incident) as too slow for agent speed.
- Incident-response agent: read-only prod logs (no PII), Slack to run the channel, Google Doc drafting for the postmortem; all actions to SIEM. After moving from Claude Opus 4 to Opus 4.5 with nothing else changed (Nov 2025), it noticed it had the root cause and messaged an internal code-writing agent over Slack to produce a fix, which went to a human-reviewed PR. Agent-to-agent communication in chat channels, human-on-the-loop, is now described as the norm.
- Lesson stated: limit access by the permission boundary, not by what you believe the current model can do; design controls for the model six months out, because elaborate prompt scaffolds that act as controls get removed as models improve.
- Cowork surface: (possibly remote) execution environment for orchestration, MCP and network, plus a local bridge for files, browser and computer use. Remote sessions run in an ephemeral Anthropic-managed sandbox behind a mandatory egress proxy.
- Connector controls: admin enables per org and per role, each user then authorises; admins can remove individual verbs (e.g. allow draft, never send; no delete). Default suggested for email agents that read web content: drafts only, never auto-send externally.
- Telemetry: OTLP endpoint streams tool name, MCP server, parameters, success, duration, user and session. Prompt content is in Cowork's OTel output by default (opt-in in Claude Code). Stated gap: Cowork activity "not currently captured in Anthropic's Compliance API or formal audit logs".
- Off switch in three layers: one toggle disables connectors for all users including live sessions; RBAC per group; per-connector write disable.
- Claim: as of July 2026 more than 50% of code submitted for PRs at Anthropic is authored by an internal Claude Tag-like system, run in ephemeral VMs separated from production keys with human review before landing (Anthropic's own figure).
- GRC teams run agents (security questionnaires, vendor subprocessor-change notices) built by non-engineers with Claude Code on an internal business-app hosting platform; "A compliance analyst who can build the tool they need, where you can see it, isn't shadow adoption."
- Suggests ISO 42001 with a live risk register as the place agent risk decisions land.
- Limits: written by the vendor about its own product; no incident data; the Mythos-era external-threat material is deferred to a separate doc.

## Notable quotes
- "Ambiguous accountability is how incidents become unexplainable."
- "the environment the agent loop runs in should never hold a credential worth stealing"

## Could not verify
- The Compliance API gap was stated as of the July 2026 post; a later Anthropic post (see anthropic-compliance-api-cowork-claude-code, 2026-08-11) extends Compliance API coverage to Cowork, so this gap may be closed.
- The "seven requirements" are listed as six headed controls plus the off switch; the count is the author's.
