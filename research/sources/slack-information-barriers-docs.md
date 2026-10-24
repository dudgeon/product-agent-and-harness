---
title: Create information barriers in Slack
source_url: https://slack.com/help/articles/360056171734
author: Slack
publisher: Slack Help Center
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [identity-delegation, shared-persistent-sessions, public-by-default-agent-work]
relevance: medium
---

## Relevance to the project

Regulated firms (e.g. banks separating trading from investment banking) already need walls inside the chat tool. Slack's information barriers block DMs and huddles between identity-provider groups but, per Slack, do not stop barred members interacting in shared public or private channels. A Slack-native, public-by-default agent like River therefore inherits the chat tool's visibility model, and Slack's own barrier feature would not by itself keep agent threads in public channels from crossing a wall. Bears on the agent-interface and trust/privacy dimensions for regulated settings.

## Themes

- **identity-delegation**: barriers are defined between IdP groups; Enterprise Grid only; enabled via Slack support; admin API (admin.barriers.create/list/delete) (help article; api.slack.com/enterprise).
- **shared-persistent-sessions**: members on either side of a barrier "will still be able to interact in public and private channels" they share; existing DMs become read-only (help article).

## Key points

- Default: any Enterprise Grid member can DM or huddle with any other member.
- Barriers apply to DMs and huddles between configured IdP groups; channel co-membership still allows interaction.
- Enterprise Grid marketed for regulated industries (HIPAA, FINRA cited in 2017-2020 press, e.g. SiliconANGLE 2020-08-11).

## Could not verify

- Read through a search-tool summary of the help article (localised URL), not the live English page; current wording may differ.
