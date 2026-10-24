---
title: "Inference hooks: inline data loss prevention for Claude Enterprise"
source_url: https://claude.com/resources/articles/claude-enterprise-inference-hooks
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-08-05
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [enterprise-admin-controls, agent-protocol-security, policy-enforcement-fail-open, agent-control-plane]
relevance: medium
---

## Relevance to the project
Inference hooks route every Claude Enterprise inference request, and every tool response (including MCP connectors, skills and plugins), through the organisation's own DLP server for an allow or deny verdict before the model sees it, across chat, Claude Code, Cowork and other Enterprise surfaces. For a PM harness in a regulated company this is the vendor-provided control point that compliance teams will ask for, and its configurable failure policy speaks directly to the fail-open versus fail-closed question. It is a short beta launch post with no latency, coverage or failure data.

## Themes
- enterprise-admin-controls: turned on once at org level; shadow mode (always allow), role-based exclusions, percentage-based rollouts ("Ways to use inference hooks").
- agent-protocol-security: tool responses from MCP connectors, skills and plugins are inspected before returning to the model, a check against injected or sensitive content arriving via tools ("How inference hooks works").
- policy-enforcement-fail-open: "Customize failure-policy tolerance, timeouts" lets each org choose what happens when the DLP server is slow or down; the post does not state the default ("Ways to use inference hooks").
- agent-control-plane: one enforcement layer across surfaces replaces per-product agents; previously native inline enforcement existed only via Claude Code's client-side hooks (intro).

## Key points
- **Mechanism.** Signed WebSocket from Claude to the customer's security server; prompt plus surrounding context sent before generation; Claude proceeds only after an allow verdict. The same check runs on tool-call responses.
- **Integration.** Open, webhook-based protocol with a published schema; named DLP vendors include Netskope, Palo Alto Networks, Proofpoint and Zscaler, or an in-house server. Security vendors are invited to build integrations.
- **Scope gap closed.** Before this, inline enforcement needed Claude Code client-side hooks; inference hooks are server-side and cover all Enterprise surfaces with one configuration.
- **Customer quote.** Bandwidth's VP of Information Security says it lets them "safely move faster on AI without giving up control" (vendor-curated).
- **Limits:** beta; it inspects inputs to the model (prompts and tool responses), and the post does not say whether model outputs or outbound tool-call arguments are inspected; no latency figures; failure-policy default unstated.

## Notable quotes
- "Your DLP server makes the call to block or allow, and Claude enforces that decision in real time." (intro)

## Could not verify
- Whether outbound tool-call parameters and model outputs are also checked, and the default failure policy (would need the linked documentation).
