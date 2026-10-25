---
title: "How healthcare organizations use Claude Tag"
source_url: https://claude.com/resources/articles/how-healthcare-organizations-use-claude-tag
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-09-14
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [scoped-governance-containers, risk-sloped-review, shared-persistent-sessions, tacit-knowledge-capture, identity-delegation]
relevance: medium
---

## Relevance to the project
Three healthcare companies run Claude Tag, the shared Slack agent, only in channels and with connectors that never touch patient data, because Tag is not yet covered by Anthropic's BAA; the per-channel scoping that makes this possible is a concrete regulated-industry pattern for the strategy's governance and trust-default options. The Tennr example is the sharpest data point: autonomy is set per channel, so the agent ships code without PR review in a low-risk internal-tool channel but only gathers information in product and engineering channels. Customer stories published by Anthropic, with a promotional credit offer attached; outcome figures are the customers' claims.

## Themes
- scoped-governance-containers: Tag can be off by default, enabled only in approved channels, DMs disabled, connectors scoped per channel; "access bundles" give a channel its codebase and tracker while EHR and clinical systems stay unreachable (intro bullets).
- risk-sloped-review: Tennr lets Claude "fix problems, modify code, skip PR reviews, and ship" in its offer-tool channel but not in Product or Eng channels; "real autonomy where it's low risk without granting it everywhere" (Tennr section).
- shared-persistent-sessions: channel memory lets Tag recognise a new complaint as a known issue and recall investigations from weeks earlier; teams work in open threads so everyone can review and pick up context (Insight Health section; "Getting started").
- tacit-knowledge-capture: Medallion's undocumented payer rules move from a few domain experts into a channel where Tag answers from past expert responses and tags an expert when not confident, whose answer then informs future ones (Medallion section).
- identity-delegation: Insight Health pairs Tag (sees codebase and Linear) with its own Agent SDK agent Zeus on a BAA-covered API org that queries production data and masks PHI before Slack; deliberately different access per agent (Insight Health section).

## Key points
- Tag's access model as described: sees what a workspace member sees; can read and keyword-search public channels; no access to private channels it is not invited to.
- Insight Health (referral-document AI for 1,100+ practices): two agents investigate production alerts in-thread, open a draft PR, watch tests; an engineer reviews and merges. Customer claims 97% of alerts in its critical channel closed without an engineer stepping in. CTO credits visible agent reasoning in the channel with building trust.
- Tennr: an internal offer portal built in Claude Code has Tag as "primary maintainer"; recruiters, People and RevOps request changes in plain English and Claude ships and deploys; customer reports 15+ tickets in about a month, a same-day lockdown of an exposed API, and Claude posting an unprompted incident notice about a comp-display bug. Conventions (emoji status legend, ticket format) were taught in-channel and adopted.
- Medallion: policy-level questions only (not individual patients or providers); expert oversight and corrections; every exchange auditable in a company-visible channel; downstream systems validate actions independently.
- Recommended start: one alert or support-engineering channel, connect GitHub, two weeks before widening the allowlist.
- Commercial context: Tag is in beta; article advertises a $25,000 Enterprise credit for linking GitHub (expires 2026-10-01).
- Limits: no PHI use cases at all, by design; the Tennr no-review posture is one company's choice and the comp-display bug shows it can reach candidates; no error rates beyond the 97% claim.

## Notable quotes
- "Being able to draw those lines channel by channel meant we could give Claude real autonomy where it's low risk without granting it everywhere." (Abe Griffiths, VP Business Operations and Strategy, Tennr)
- "When it isn't confident, it tags in the right expert, and their response becomes the basis for future answers on related topics." (Armaan Sarkar, CTO, Medallion)

## Could not verify
- The 97% closure figure (definition of "closed" and period not given) and Tennr's ticket counts.
- Linked healthcare best-practices and security docs were not fetched.
