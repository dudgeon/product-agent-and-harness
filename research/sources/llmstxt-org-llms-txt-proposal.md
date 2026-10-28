---
title: "The /llms.txt file"
source_url: https://llmstxt.org/
author: Jeremy Howard (Answer.AI)
publisher: llmstxt.org
published: 2024-09-03
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-legible-platform, legible-org-for-agents]
relevance: medium
---

## Relevance to the project
llms.txt is the simplest published convention for a site (or any path under it) to describe itself to agents: a small Markdown index with links to clean Markdown versions of pages. It is a model for a platform's "front page for agents", but it carries only navigation and prose, not ownership, intake, checks or SLAs. Its reception (see `ppcland-llms-txt-adoption-zero-requests`) shows that publishing a file is not the same as agents using it.

## Themes
- agent-legible-platform: fixed Markdown structure: required H1 name, optional blockquote summary, optional prose, H2 sections of link lists; an "Optional" H2 marks links an agent may skip for shorter context (Format section).
- legible-org-for-agents: can sit at the root or at any subpath covering pages under it; companion convention of `page.md` / `page.html.md` clean-Markdown versions, discoverable via `rel="alternate" type="text/markdown"` or `rel="describedby"` (v2 additions).

## Key points
- Proposed 3 Sep 2024; page now describes a v2 (modified Aug 2026).
- Claims "thousands of sites" publish one; lists generators in Mintlify, GitBook, Yoast, Docusaurus, VitePress, Drupal and an MCP server; cites Lighthouse auditing for the file (self-reported).
- No schema for ownership, contacts, versioning or freshness; no signing or verification.

## Notable quotes
- "The file itself stays small enough to fit in context."

## Could not verify
- The adoption claim and the Lighthouse integration were not checked independently.
