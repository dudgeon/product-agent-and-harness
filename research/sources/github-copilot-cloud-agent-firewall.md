---
title: Customizing or disabling the firewall for GitHub Copilot cloud agent
source_url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall
author: GitHub
publisher: GitHub Docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, agent-failure-modes]
relevance: medium
---

## Relevance to the project
The egress control for Copilot cloud agent and code review, now with organisation-level enforcement. It is unusually candid about limits (Bash-tool processes only; not MCP servers or setup steps; bypassable), which matters when a regulated owner asks whether a cloud agent can exfiltrate. Builds on [Copilot risks](github-copilot-cloud-agent-risks.md).

## Themes
- enterprise-admin-controls (proposed): organisation owners configure firewall settings for cloud agent and code review; repo admins can change them only when the org setting is "Let repositories decide"; org custom allowlist rules apply to all repos and cannot be deleted by repos; "Allow repository custom rules" can be disabled.
- agent-failure-modes: "The firewall only applies to processes started by the agent via its Bash tool." It "does not apply directly to Model Context Protocol (MCP) server processes" or setup steps. "Sophisticated attacks may bypass the firewall, potentially allowing unauthorized network access and data exfiltration"; it "should not be considered a comprehensive security solution."

## Key points
- On by default; recommended allowlist on by default (OS and language package registries, container registries, CAs, Playwright browser hosts).
- Disabling allows any host, "increasing risks of exfiltration".
- No mention of self-hosted or larger runners.

## Could not verify
- Whether partner agents (Claude, Codex) on GitHub get the same firewall (the third-party page says "same security protections, mitigations, and limitations"). Undated; model-summarised fetch.
