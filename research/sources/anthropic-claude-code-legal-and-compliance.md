---
title: Claude Code docs: Legal and compliance
source_url: https://code.claude.com/docs/en/legal-and-compliance
author: Anthropic
publisher: Claude Code docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-portability, meta-harness, identity-delegation]
relevance: high
---

## Relevance to the project
Anthropic's own rule for wrapping Claude Code, which any meta-harness (Omnigent, Warp Oz, Conductor) and any internal hosted layer must follow. It permits a platform to host the unmodified Claude Code binary with each end user signing in with their own subscription or key, but forbids third parties from collecting, storing or intermediating Claude.ai credentials or routing requests through subscription credentials on users' behalf. For a company-internal tool, the sanctioned path is the organisation's own API keys or Team/Enterprise plans and a commercial agreement. No Anthropic statement about Omnigent specifically was found.

## Themes
- [[harness-portability]]: "preinstalling or running Claude Code in your products or services (e.g. in hosted sandboxes or other agent infrastructure) requires agreeing to our Commercial Terms" with conditions: binary unmodified, no removal of built-in auth methods, no paying for, reselling or intermediating Claude usage; each end user authenticates with their own key, plan credentials or 3P provider credential (section "Can customers offer Claude Code in their products?").
- [[meta-harness]]: OAuth is "intended exclusively for purchasers of Claude Free, Pro, Max, Team, and Enterprise subscription plans" for ordinary use of Claude Code and native Anthropic apps; developers building products, including on the Agent SDK, should use API keys (section "Authentication and credential use").
- [[identity-delegation]]: "developers may not collect, store, or intermediate Claude.ai credentials or session tokens — sign-in to a Claude account must complete through Anthropic's own flow." Customers may provision their own API keys in secrets managers or machine images for their own authorised users, billed to the key owner.

## Key points
- Allowed: an end user signing in to the unmodified Claude Code binary with their own subscription, including where a platform hosts Claude Code.
- Not allowed (as written): third-party apps offering Claude.ai login, routing requests through Free/Pro/Max credentials for users, storing or intermediating session tokens.
- "Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK."
- Anthropic "may" enforce "without prior notice".
- HIPAA configuration excludes cloud sessions, Remote Control and Claude Code routed through a third-party cloud provider or a gateway; ZDR not available for all organisations. Relevant if a regulated deployment routes Claude Code through a meta-harness or gateway.
- Context (secondary press, not filed): Anthropic blocked subscription OAuth outside its own products from early 2026 and revised terms around 2026-02-19/20; OpenAI took the opposite line (Sign in with ChatGPT for third-party tools, September 2026, per The New Stack).

## Could not verify
- Page publish/update date not shown.
- How Omnigent's README subscription path ("via the official claude / codex CLIs") and the proposed token broker in issue #11493 are judged by Anthropic; no Anthropic or OpenAI statement on Omnigent found.
