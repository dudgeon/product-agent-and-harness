---
title: "Announcing TechDocs: Spotify's docs-like-code plugin for Backstage"
source_url: https://backstage.io/blog/2020/09/08/announcing-tech-docs
author: Gary Niemen (Spotify)
publisher: Backstage blog
published: 2020-09-08
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [docs-as-code-prd, legible-org-for-agents, org-context-grounding, compounding-context-repo]
relevance: medium
---

## Relevance to the project
Explains why Spotify put technical docs next to code and surfaced them in Backstage: in an internal productivity survey, engineers ranked "difficulty finding technical information" as their third-biggest problem, with docs scattered across Confluence, Google Docs, READMEs and custom sites. TechDocs ties one doc site to one catalog component and owner. For the project it is the engineering-side answer to "where are things recorded and found", and the base that later AI context layers at Spotify sit on. It covers engineering docs only, not product briefs.

## Themes
- docs-as-code-prd: Markdown in the repo, built by CI with MkDocs, rendered centrally in Backstage.
- legible-org-for-agents: standard model is one component, one repo, one doc site, shown on the catalog's Docs tab with owner, support channel and open issues.
- org-context-grounding: search across all doc sites via Elasticsearch; a docs home page lists key and most-used docs.
- compounding-context-repo: trust signals (last updated, top contributors, owning team, open issues); owners get a Manage page listing their docs, issue counts and last-updated dates.

## Key points
- TechDocs was Spotify's most-used Backstage plugin, ~20% of Backstage traffic among 130+ plugins (Spotify, Sep 2020).
- Goal: help engineers "go from stuck to unstuck, and fast".
- Golden Path tutorials span many teams; their ownership uses GitHub CODEOWNERS.
- Ideas then under consideration: "Did this help?" feedback and a trust score.
- No mention of RFCs, ADRs or product documents.

## Could not verify
- Read via WebFetch summary. Current figures (5,000+ doc sites, ~10,000 daily hits) appear on newer Backstage pages, not this post, and were not checked.
