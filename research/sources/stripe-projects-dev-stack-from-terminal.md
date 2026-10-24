---
title: "Production-ready dev stack from the terminal (Stripe Projects)"
source_url: https://stripe.dev/blog/production-ready-dev-stack-from-terminal
author: Rami Banna (Stripe)
publisher: Stripe Dot Dev Blog
published: 2026-03-26
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [identity-delegation]
relevance: low
---

## Relevance to the project
External product (Stripe CLI plugin that provisions hosting, databases, auth and analytics across partner providers and syncs "agent-ready credentials"). Filed because Geoff's doc cites it for the PM who built it in 7 weeks with internal AI tools (that story is in the Not My Business video, not this post). Minor relevance: a "project" manifest that writes coding-agent skills into the repo and gives agents deterministic, auditable provisioning and scoped payment tokens.

## Themes
- identity-delegation: credentials synced to env "in a format that works for humans and agents"; paid upgrades via a scoped Shared Payment Token so underlying payment credentials aren't copied around.

## Key points
- `stripe projects init` writes `.projects` config, a blank `.env`, and "relevant agent skills" into the project directory.

## Could not verify
- The post says nothing about how the product was built internally.
