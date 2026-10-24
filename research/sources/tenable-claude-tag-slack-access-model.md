---
title: "Claude Tag Slack access model (Tenable Research)"
source_url: https://www.tenable.com/blog/claude-tag-slack-access-model
author: Chen Doytshman (Tenable Research)
publisher: Tenable blog
published: 2026-07-15
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, human-review-gates]
relevance: high
---
## Relevance to the project
A security vendor's analysis of a shared Slack agent: channel membership becomes an IAM boundary because everyone in the channel can direct an agent that holds shared credentials. Directly informs access-control and permission-leakage design for any shared-agent surface. Tenable sells security products, so it is independent of Anthropic but not disinterested; Tenable reported the issue to Anthropic via HackerOne 2026-06-30 to 07-02.

## Themes
- shared-persistent-sessions: service-identity pattern means 'anyone in a channel with the bundle can direct Claude within its scope'; public-channel join policy effectively governs access to bundle credentials; new members also see prior scrollback
- human-review-gates: recommends auditing bundles, scoping to minimum, keeping elevated bundles in private channels, and logging/approving channel invites

## Key points
- Other OAuth connectors (e.g. Google Drive) reuse the credential of the admin who connected them; GitHub bundles use an app token limited to a repo allowlist.
- Tenable's framing: not per-user delegation; resembles deploy bots. Interpretations of 'confused deputy' are the reader's, not the article's own terms (checked by the retrieving agent).
- Anthropic confirmed only that admin-experience feedback was passed to product.

## Could not verify
- Full article was read via summarisation; exact wording not checked.
