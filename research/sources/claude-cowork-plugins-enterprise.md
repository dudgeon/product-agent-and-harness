---
title: Cowork and plugins for teams across the enterprise
source_url: https://claude.com/resources/articles/cowork-plugins-across-enterprise
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-02-24
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [skills-marketplace, enterprise-admin-controls, harness-portability, single-agent-many-skills, enablement-by-product]
relevance: medium
---

## Relevance to the project
Anthropic's launch of private plugin marketplaces for Cowork: admins build or template plugins (skills, commands, connectors), distribute them through org-specific marketplaces with per-user provisioning and auto-install, and track usage and cost through OpenTelemetry. It is the vendor's packaged answer to capability distribution for non-engineers, and it states plugins are portable file systems that also run on anything built on the Claude Agent SDK. Launch post only: no adoption or outcome data.

## Themes
- skills-marketplace: org-specific marketplaces, private GitHub repos as plugin sources (private beta), per-user provisioning and auto-install ("Upgrading the plugin experience").
- enterprise-admin-controls: unified "Customize" menu for plugins, skills and connectors; admin control over which connectors are bundled; OpenTelemetry for usage, cost and tool activity ("Upgrading the plugin experience").
- harness-portability: "Plugins are simple, portable file systems that you own. They work across Cowork and anything built on the Claude Agent SDK" ("New connectors and plugins"); portability stops at Anthropic's stack.
- single-agent-many-skills: "Plugins turn Claude into specialized agents for every role and department": one agent specialised per role by plugin, not separate agents (intro).
- enablement-by-product: Claude guides admins through plugin setup by asking questions; slash commands open structured forms so a workflow "feels as intuitive as filling out a brief" ("Upgrading the plugin experience").

## Key points
- New role plugin templates include HR, Design (critique frameworks, UX copy, accessibility audits, research plans), Engineering, Operations, brand voice (Tribe AI), and several finance plugins (financial analysis, investment banking, equity research, private equity, wealth management). No product-management plugin in this release list.
- New connectors: Google Workspace, Docusign, Apollo, Clay, Outreach, Similarweb, MSCI, LegalZoom, FactSet, WordPress, Harvey; partner-built plugins from Slack, LSEG, S&P Global and others.
- Company branding in Cowork; cross-app work between Excel and PowerPoint add-ins (research preview).
- The demo company is fictional; the legal team in it uses Thomson Reuters CoCounsel built on the Agent SDK.
- **Limits:** no review, signing or security-scan step for private-marketplace plugins is described; nothing on versioning or eval-gating.
