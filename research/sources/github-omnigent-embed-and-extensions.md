---
title: "Omnigent's embed build and extensions (omnigent-ai/omnigent #9514 and docs/extending/extensions.md)"
source_url: https://github.com/omnigent-ai/omnigent/blob/main/docs/extending/extensions.md
author: Omnigent maintainers
publisher: GitHub
published: 2026-10-08
retrieved: 2026-11-11
type: docs
evidence: first-party
filed_by: film-omnigent-canvas-coach
themes: [meta-harness, build-vs-buy]
relevance: medium
---

## Relevance to the project
Shows the two mechanisms by which a company could make Omnigent its own internal agent surface: embedding its web UI in a host application, and installing extensions that add pages to it. This is the basis for the concept film's line that a company can customise Omnigent, and for the claim that a team doing so could add a product coach and its templates. It does not show that any named company has done this.

## Themes
- [[meta-harness]]: operator-installed extensions contribute "namespaced browser pages and links in the primary sidebar" (extensions.md, V1 contribution points).
- [[build-vs-buy]]: the web UI has an embed build (`npm run build:embed`) and a host integration API; #9514 adds an optional host-provided HTML preview frame "so embedders can supply an isolated document renderer while retaining Omnigent's comment bridge".

## Key points
- **Extensions (V1):** Python distributions installed by an administrator; they add pages under `/extensions/{extension_id}/{route}` and sidebar links. The browser part runs in an opaque-origin sandboxed iframe with no network egress and a permission-checked SDK. Arbitrary React components, runner tools and user-installed marketplace packages are not supported in V1.
- **Embedding:** #9514 (merged 2026-10-08) is an "additive embed integration API"; the code distinguishes an embedded host from standalone (`useIsEmbedded`, `getEmbedRoot` in the viewer source).
- Omnigent is Apache-2.0, so a fork is also open to a company ([github-omnigent-repo](github-omnigent-repo.md)); Databricks itself runs a hosted variant ([databricks-docs-omnigent-on-databricks](databricks-docs-omnigent-on-databricks.md)).

## Could not verify
- A public source naming a company that customises Omnigent as an internal agent surface: a web search on 2026-11-11 found none. Geoff has first-hand knowledge of at least one company doing so (told to the film worker, 2026-11-11; not named here), which is what the concept film's line rests on.
