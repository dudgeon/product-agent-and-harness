---
title: "Quick: An internal hosting platform for the AI era"
source_url: https://shopify.engineering/quick
author: Daniel Beauchamp, Alex Pilon (Shopify)
publisher: Shopify Engineering blog
published: 2026-06-10
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [artifact-standardization, non-engineer-builders, org-learning-loop, skill-standards]
relevance: medium
---

## Relevance to the project

Quick is Shopify's internal hosting for agent-made HTML artifacts (dashboards, prototypes, tools): drop a folder, get a URL every employee can see. It is not River, but it is the artifact half of the same culture: open to all employees, no permissions and no site owners, and agent-ready via bundled skills. It bears on the artifacts dimension (where agent outputs live and how they are shared) and on the trust and privacy model (Shopify applies "open to everyone inside" to artifacts as well as sessions). River's Remote Dev streams simulator previews to a Quick site ([remote-dev note](shopify-engineering-remote-dev.md)).

## Themes

- **artifact-standardization**: one artifact form (a folder of static HTML plus a fixed client API: db, files, AI, data warehouse, websockets, identity); 50,000+ sites; "over half the company has created at least one" (intro).
- **non-engineer-builders**: launched July 2025; took off as AI let "people across every discipline" generate sites; usage "popped off" December 2025 (Adoption).
- **org-learning-loop**: sites import code from each other; shared JS libraries (comments, voice, analytics) became an internal ecosystem (An emergent ecosystem).
- **skill-standards**: "Quick comes out of the box with all the skills your agent needs"; `quick init` then any agent (Agents + Quick).

## Key points

- Architecture: each site is a folder in a Google Cloud Storage bucket, served by NGINX with wildcard subdomains via gcsfuse; whole server behind Identity-Aware Proxy, so every request is a verified employee; `quick deploy` wraps gcloud rsync.
- Shared backend: one CloudSQL + Node server gives every site a Firebase-like realtime db, file uploads, LLM calls via the Shopify AI proxy with server-held keys, BigQuery access, websockets, and an Identity API (name, title, team, Slack handle).
- **Trust model:** "All Quick sites are open to all employees. There's not even a concept of a 'site owner.'" Anyone can overwrite any site or take a subdomain. Safety rests on "the trusted walls of Shopify". The post does not discuss sensitive data in sites (e.g. a dashboard pulling restricted warehouse tables), which is the obvious risk.
- Product discipline: a small, fixed capability set; they say no to custom backends and cron.
- Mentions an internal designers' tool called "Artifact" for sharing work.

## Notable quotes

- "All Quick sites are open to all employees." (The Quick philosophy)

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify

- Whether the data-warehouse API applies the viewer's or the author's permissions (not stated). Whether River publishes to Quick directly beyond Remote Dev's Live Preview.
