---
title: Even with a 30GB monolithic repository, the development environment doesn't slow down — How Shopify powers "World"
source_url: https://flagship.inc/en/columns/ai-first-series-2-shopify-tectonix-nix
author: Flagship Inc. (column; AI-First series part 2)
publisher: flagship.inc
published: 2026-07-22
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: competitive-teardown-shopify-river
themes: [legible-org-for-agents, shared-persistent-sessions]
relevance: low
---

## Relevance to the project
A Japanese Shopify agency's column series on Shopify's AI-first infrastructure. **It restates Under the River** plus public Nix and Tectonix talks. It adds context that World is **30GB+**, describes Tectonix's lazy-tree / forked Nix evaluator, CI policy (Semgrep, OPA), and Shopify's **2026 acquisition of Garnix** (Nix CI). Part 1 (https://flagship.inc/en/columns/ai-first-series-1-shopify-world-monorepo, same date) restates the River numbers and argues multi-client agencies must keep per-project "worlds" for confidentiality. It was not filed separately.

## Themes
- `legible-org-for-agents`: reproducibility means "build errors encountered by AI are narrowed down to 'pure code errors' only".
- `shared-persistent-sessions`: Aquifer's session (Postgres append-only), disposable harness, and sandbox "hardened with Nix and completely separated from the Harness". The blast radius is confined to the sandbox.

## Key points
- Tectonix = git sparse-checkout + NixOS module system + custom extensions. A forked Nix evaluator ("tecnix") with lazy-tree reads from the Git object DB. Developers edit only per-zone `zone.nix` files.
- Production still deploys as microservices. "Development is unified, but deployments remain separate."
- An earlier Nix attempt around 2019 failed on the learning curve. Practical snags included Nix's read-only filesystem crashing tools (Cloudflare tunnel, EROFS).
- Garnix's "call-by-hash" builds production from the merged commit hash.

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- The Garnix acquisition and the 30GB figure were not checked against first-party sources.
- The underlying talks were not reviewed: SCALE 23x "Tectonix: The bedrock of Shopify's Monorepo" and NixCon 2025 "Nix-based development environments at Shopify (reprise)".
