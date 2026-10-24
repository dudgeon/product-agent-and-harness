---
title: "Agent identity: a new access model for autonomous, team-wide AI"
source_url: https://claude.com/resources/articles/agent-identity-access-model
author: Noah Zweben (member of technical staff, Claude Code team, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-06-24
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [identity-delegation, scoped-governance-containers, enterprise-admin-controls, shared-persistent-sessions, agent-protocol-security]
relevance: high
---

## Relevance to the project
Anthropic's explanation of why a multiplayer, long-running agent cannot "act as the user" and instead holds its own accounts per channel: the question becomes "what can this agent do in this compartment?" rather than "what can this user do?". It is the rationale piece behind the Claude Tag identity docs already filed, and it states the trade-off openly: a channel member without repo access can have the agent read that repo if the channel profile allows it. Planned just-in-time grants and a user-permission overlay show where the model is heading. First-party design argument, no deployment data.

## Themes
- identity-delegation: two reasons act-as-user breaks: autonomy (tasks run after the requester logs off) and multiple people steering a channel (section "Why 'act as the user' breaks down").
- scoped-governance-containers: distinct identity per private channel, shared workspace identity for public channels; memory and access stay inside boundaries (section "How identity boundaries work").
- enterprise-admin-controls: workspace baseline profile inherited by channels, channel overrides; repo access, connectors, skills/plugins, standing instructions; RBAC on who can invoke; per-channel disable (sections "Inheriting permissions", "Broad default access").
- shared-persistent-sessions: DMs run as the user's own claude.ai account and connectors, channels run as the agent (section "Direct messages").
- agent-protocol-security: credentials stored separately and injected at the network boundary; non-allowed hosts blocked; every routine, memory write and network call audited (section "Security and audit").

## Key points
- Claude posts as the Claude app, opens PRs as the Claude GitHub App, queries the warehouse under an admin-provisioned service account; no personal credentials in channels, so a channel "can never become a side door" into someone's private docs.
- Same service can be connected at different permission levels per channel (read-only warehouse in general, write in the data team's channel).
- Revoking the identity ends access everywhere, said to be easier than auditing actions across user accounts.
- Anthropic recommends generous access at the start, then paring back: start with a baseline profile in a few channels, read the audit trail, extend "one deliberate grant at a time". This default favours breadth; a regulated org may want the opposite order.
- Admins can scope a channel to its least-privileged member; actions land in each connected system's own logs.
- Cites agent task length "doubling roughly every four months" as motivation (no source given).
- **Roadmap (not shipped)**: just-in-time credential grants for single sensitive actions; identity-aware overlay requiring both channel profile and requesting user's permissions.

## Notable quotes
- "Agent identity replaces the question 'what can this user do?' with 'what can this agent do in this compartment?'"

## Could not verify
- Whether JIT grants or the user-permission overlay have shipped since publication.
- Related filed sources: [Claude Tag agent identity docs](anthropic-claude-tag-agent-identity.md), [Tenable on the Claude Tag access model](tenable-claude-tag-slack-access-model.md).
