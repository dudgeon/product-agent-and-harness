---
title: Claude Tag now supports personal connectors in channels
source_url: https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-09-24
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [identity-delegation, shared-persistent-sessions, public-by-default-agent-work, enterprise-admin-controls]
relevance: high
---

## Relevance to the project
Claude Tag, the Slack channel agent, can now use the requesting person's own connectors (their calendar, Drive, CRM accounts) for a request made in a shared channel, alongside the channel's admin-attached connectors that run under a service account. It is a concrete hybrid answer to "who is the agent acting as": channel and unattended work run under the agent's identity, person-initiated reads run on-behalf-of the requester, and each is logged under the matching account. A per-person review gate (review mode, or auto mode that holds sensitive content) controls what reaches the channel. It bears directly on agent-identity-delegation, session-persistence-sharing and trust-privacy-defaults, and refines the earlier channel-only identity model. Beta; Team plans first, Enterprise to follow.

## Themes
- identity-delegation: Claude reads the channel's GitHub through the channel connector and Priya's private doc "through Priya's Google Drive connector, separately from the channel's work"; actions via a personal connector appear in that tool's log "under your account", channel work under its service account (§Using personal connectors).
- shared-persistent-sessions: "Personal connectors don't run unattended": scheduled routines and anything Claude starts on its own use only channel connectors; shared connectors suit always-on work like #on-call triage (§Where the channel's own connectors still matter).
- public-by-default-agent-work: "Anything Claude posts is visible to everyone in the channel"; the requester chooses review mode (see the reply before it posts) or auto mode (posts unless Claude judges content sensitive) (intro, §Using personal connectors).
- enterprise-admin-controls: admins choose shared tools under an agent identity, personal connectors only (relying on existing role-based access), or tool by tool; Enterprise admins will be able to require review for everyone (intro).

## Key points
- **Motivation.** Organisations keep channel connector lists short because "they want access to follow the person, not the channel".
- **Flow.** First use of a personal connector prompts the user for consent; then it is used in that thread; users can disconnect any time; nothing to install.
- **Worked example.** In #checkout-migration (GitHub attached), a user asks Claude to check her Drive plan against merged PRs; Claude combines both and posts what's left.
- **Design guidance.** Shared connectors for unattended actions and anything the whole channel relies on; personal-only channels suit closely supervised work, such as drafting an RFP response from pricing data not provisioned to the channel.
- **Limits.** Auto mode depends on Claude's own judgement of what is "sensitive" (a model classifier as the privacy gate, with no stated accuracy); once posted, private-source content is visible to the whole channel; Enterprise mandatory review is future tense; rollout on Team first.

## Notable quotes
- "They want access to follow the person, not the channel." (intro)
- "Personal connectors don't run unattended." (§Where the channel's own connectors still matter)

## Could not verify
- Whether channel members without access to the source see a redacted or full answer beyond what the requester approves; the page implies full visibility of whatever posts.
