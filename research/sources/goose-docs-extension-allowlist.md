---
title: goose Extension Allowlist (docs)
source_url: https://goose-docs.ai/docs/guides/allowlist
author: goose maintainers (AAIF)
publisher: goose-docs.ai
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-block-product-practices
themes: [enterprise-admin-controls, skill-supply-chain-security, policy-enforcement-fail-open]
relevance: medium
---

## Relevance to the project
The upstream mechanism behind Block's internal "allowed list of MCP servers". It is thin: an environment variable pointing at a YAML file of allowed install commands, checked when an extension is installed. Enforcement depends on the device setting the variable (e.g. a custom distribution or MDM), so it is a client-side control, not an admin plane.

## Themes
- enterprise-admin-controls: `GOOSE_ALLOWLIST` = HTTPS URL of a YAML list of `id` + exact `command`; applies to Desktop and CLI; fetched when first needed, cached, refetched on restart.
- skill-supply-chain-security: best practice: exact command strings with full paths, HTTPS, restricted edit rights, monitor rejected installs.
- policy-enforcement-fail-open: "If this environment variable is not set, no allowlist restrictions are applied."

## Key points
- Matches only the install command; nothing in the page covers already-installed extensions, recipes that declare extensions, or runtime tool calls.

## Could not verify
- How Block sets the variable on managed laptops (presumably its internal build or MDM); not documented publicly.
