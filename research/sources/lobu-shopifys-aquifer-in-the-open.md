---
title: Shopify's Aquifer, in the Open
source_url: https://lobu.ai/blog/shopifys-aquifer-in-the-open/
author: Burak Emre Kabakcı
publisher: Lobu blog
published: 2026-05-29
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: competitive-teardown-shopify-river
themes: [memory-architecture, identity-delegation, shared-persistent-sessions]
relevance: low
---

## Relevance to the project
A vendor (Lobu, an open-source shared-memory agent platform) positioning itself against Aquifer. **It restates Under the River.** It is useful for two design contrasts: **extract structured events at write time** versus mining chat threads later, and a **credential-swapping proxy** so the worker "never holds a real secret". It also points out that Aquifer is single-tenant ("one company is the easy version").

## Themes
- `memory-architecture`: "We don't keep the chat. We keep what the chat was about." Every interaction becomes an embedded event in an append-only log, and "a new agent inherits the whole history". This contrasts with River's `river_sessions` table, "a log bolted onto one agent".
- `identity-delegation`: "A proxy sits in front of it and swaps placeholder tokens for the real ones only as a request leaves the box. The agent uses credentials it never sees and can never leak."
- `shared-persistent-sessions`: multi-tenant concerns (per-org memory, per-tenant credentials) that a single company "never has to solve".

## Key points
- Quotes Under the River: "the corpus is the compounding asset; the privacy of an agent thread is a disadvantage."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- Whether Aquifer itself uses a placeholder-swapping credentials proxy. adaptordie.io lists a "credentials proxy" among Aquifer's parts, so Under the River should be checked.
