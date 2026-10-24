---
title: Agent internet access (Codex Cloud docs)
source_url: https://learn.chatgpt.com/docs/cloud/internet-access
author: OpenAI
publisher: learn.chatgpt.com (also at developers.openai.com/codex/cloud/agent-internet)
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, remote-agent-invocation, agent-failure-modes]
relevance: medium
---

## Relevance to the project
The network policy for Codex cloud tasks: off by default in the agent phase, per-environment allowlists and an HTTP-method restriction that is unusual among vendors. It also states that workspace-level Agent Security network requirements and the environment's own setting apply separately, and that a full-sandbox escalation can bypass the managed command proxy. For a regulated deployment of background agents this is the egress control that would have to be configured and evidenced.

## Themes
- enterprise-admin-controls (proposed): "An allowed domain in Agent Security does not override a restriction in the Cloud environment's internet settings"; managed policy may allow full sandbox escalation that bypasses the command proxy, so set enforced approval and sandbox requirements and test escalated commands.
- agent-failure-modes: named risks are prompt injection from untrusted content (example: an issue that tells the agent to POST the last commit to an attacker), code or secret exfiltration, malware or vulnerable dependencies, licence-restricted content.
- remote-agent-invocation: setup scripts run with internet access; agent phase is off unless enabled per environment.

## Key points
- "By default, Codex blocks internet access during the agent phase." "Setup scripts still run with internet access so you can install dependencies."
- Modes: Off, or On with presets None, Common dependencies (71 domains: github.com, npmjs.com, pypi.org, crates.io and similar) or All (unrestricted), plus custom domains.
- Methods: limit to GET, HEAD, OPTIONS; "Requests using other methods (POST, PUT, PATCH, DELETE, and others) are blocked."
- The page now labels this Codex Cloud (Legacy) and points to a newer "Connect to services" section; ChatGPT Work Cloud has separate permissions and does not inherit these requirements.

## Could not verify
- "Connect to services" (current Codex Cloud) not read. WorkOS (independent) says there is no documented way to restrict setup-phase egress and no documented blocked-egress log ([WorkOS](workos-agent-sandbox-egress-defaults.md)). A single community forum report of a hardcoded allowlist still applying under "unrestricted" was seen in search only, not read.
