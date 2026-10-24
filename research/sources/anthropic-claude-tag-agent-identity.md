---
title: "Claude Tag: agent identity (concepts)"
source_url: https://www.claude.com/docs/claude-tag/concepts/agent-identity
author: Anthropic
publisher: claude.com docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, remote-agent-invocation, human-review-gates]
relevance: high
---
## Relevance to the project
Documents the org-managed Slack agent identity model: in shared channels the agent acts as a service account with admin-defined access bundles, not as the person who tagged it. This is the clearest vendor statement of one resolution of the 'who is the agent acting as' question, and the opposite of Cursor's creator-identity model and Codex's requester-identity model.

## Themes
- shared-persistent-sessions: channel sessions use connectors, repos and plugins an admin applied to the channel/workspace/org, and 'everyone in the channel gets the same capability, regardless of who asks'
- human-review-gates: audit attribution differs by context: channel actions appear under service accounts; DM actions under the user (PRs still authored by the GitHub App); personal-connector work in a channel is recorded under the approving user

## Key points
- Credentials live in a store and are attached at a network proxy so the model and sandbox never see them; outbound traffic is allowed only by credential rule, allowed domain or environment setting.
- Public beta; proxy handles only HTTP/HTTPS (no SSH or DB wire protocols). Replaces the earlier per-user-linked Claude in Slack.
- Sessions can run in a self-hosted environment but Access bundles are not yet supported there (per self-hosted docs).
