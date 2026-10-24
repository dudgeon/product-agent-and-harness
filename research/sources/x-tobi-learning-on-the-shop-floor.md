---
title: Learning on the Shop floor
source_url: https://x.com/tobi/article/2053121182044451016
author: Tobi Lütke (CEO, Shopify)
publisher: X (@tobi), article; post https://x.com/tobi/status/2053121182044451016
published: 2026-05-09
retrieved: 2026-10-24
type: x-post
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [org-learning-loop, shared-persistent-sessions, enablement-by-product, compounding-context-repo, evals-autonomy-trust, vendor-claims-vs-independent-evidence, public-by-default-agent-work]
relevance: high
---

## Relevance to the project

Tobi Lütke's founding essay on River: why Shopify's agent lives only in public Slack channels and refuses DMs, and his claim that this turned the company into a "Lehrwerkstatt" (teaching workshop) where people learn by watching others work with the agent. It is the clearest first-party argument for a public-by-default trust model and a chat-native interface, and the source of the 36%→77% merge-rate claim. ~2.8M views, 4.5K likes by 2026-10-24 (fxtwitter API), so it has shaped how the industry talks about shared agent sessions.

## Themes

- **org-learning-loop**: Public-only River makes "osmosis learning" happen: a support engineer copies a backend engineer's log-query technique the next day; new hires scroll #river to see how seniors scope requests; one team's checkout-warehouse skill "gets reused by twelve other teams" (sections 1-2).
- **shared-persistent-sessions**: River declines DMs and suggests a public channel; Tobi works in #tobi_river where 100+ people react, add context, "pick up the torch", help with reviews (section 1).
- **enablement-by-product**: learning "does not require a curriculum, a training plan, or a manager. It just requires everyone's work to be visible" (section 1).
- **compounding-context-repo**: channels pre-load zones, skills and instructions written by the team closest to the work; River has a memory "constantly learning and un-learning" (section 2).
- **evals-autonomy-trust**: merge rate 36%→77% in two months without retraining or switching models, attributed to people writing down what River should have known (section 2). Measurement undefined.
- **vendor-claims-vs-independent-evidence**: all numbers self-reported by the CEO, no method.

## Key points

- **Origin frame:** Tobi's apprenticeship at a Siemens subsidiary at 16, learning by watching (opening).
- **What River is:** an agent in Shopify's Slack, mentioned like a teammate; reads/writes code, runs tests, opens PRs, queries the data warehouse, reads production traces. River is referred to as "she".
- **Numbers (30 days to ~2026-05-09):** 5,938 employees across 4,450 channels; 1,870 PRs opened in the last week in the main monorepo; "about one in eight pull requests merged into our codebase last week was authored by River, reviewed by us".
- **The constraint:** contrasted with ChatGPT/Claude ("a private window") and Cursor ("between you and the IDE"). River "does not respond to direct messages", politely declines and suggests a public channel. Personal channels (#tobi_river) became a pattern.
- **Admits friction:** "This was odd at first... Asking for help feels different when the whole company can see the question." The learning effect was "hoped for but did not fully predict"; he calls it a "somewhat accidental" discovery.
- **AI-deskilling argument:** the risk is not AI doing work but "AI does the work and we never learn from it"; private windows lock everyone else out of the apprenticeship.
- **Merge rate:** 36%→77% over two months; credited to people noticing where River got stuck and writing it down; "The agent gets better at being Shopify."
- **"The company moves at the speed of its slowest secret":** organisational speed is set by its lowest-bandwidth channel; meetings, email and private DMs are slow for the organisation; public conversation with an agent is "fast, searchable, teachable, and it compounds".
- **Closing:** references his 2018 piece on human excellence and chess; "apprentice and the master" model.
- **Not covered:** sensitive or regulated work, HR/legal topics, what happens to people who need privacy, how permissions work, cost.

## Notable quotes

- "She only works in the open." (section 1 intro)
- "If every interaction with an agent happens in a private window, the only person who learns anything is the person at the keyboard." (section 2)
- "The company moves at the speed of its slowest secret" (section 3 heading)

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify

- How "merge rate" is defined (share of River-opened PRs that merge?) and over what base.
- Whether River's no-DM rule has exceptions (e.g. private channels, HR, security incidents). See [x-tobi-river-reaction-to-shop-floor-post](x-tobi-river-reaction-to-shop-floor-post.md) for the cost River itself names.
