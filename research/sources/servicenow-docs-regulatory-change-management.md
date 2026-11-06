---
title: "Using Regulatory Change Management (ServiceNow GRC documentation)"
source_url: https://www.servicenow.com/docs/r/Z61H6JNUJXKe8NNPQzK7MQ/GkAvjN08HpSXWEueqnL6gw
author: ServiceNow
publisher: ServiceNow documentation
published: unknown
retrieved: 2026-11-06
type: docs
evidence: first-party
filed_by: design-requirements-agent
themes: [obligation-libraries-as-data, governance-as-code, process-governance-load]
relevance: medium
---

## Relevance to the project
How a mainstream GRC platform handles the "regulation changed" side of the obligation library: regulatory alerts arrive from feeds (public regulator RSS, aggregators such as Thomson Reuters Regulatory Intelligence, LexisNexis), are triaged for applicability, impact-assessed by subject-matter experts, gap-analysed against the inventory of policies, citations and controls, and turned into action tasks (legal review, policy update, control revision, training). For a requirements agent in a bank, this is where the authoritative "what obligations exist and which controls satisfy them" data lives and how it is kept current; the agent reads it, it does not maintain it.

## Themes
- obligation-libraries-as-data: content providers are public RSS feeds, subscription aggregators (TRRI) and real-time regulatory-intelligence integrations; alert metadata comes from the provider and is not editable in the app (search-result summary of the alerts page; the main page lists the providers).
- governance-as-code: an applicable alert creates a regulatory change task; gap analysis compares "the current inventory of policies, citations, and controls" with new requirements; gaps are prioritised high, medium or low with owners and timelines.
- process-governance-load: roles are split (RCM manager approves action plans; RCM user coordinates; business users triage; SMEs, legal, audit, compliance, risk provide input); alerts close only after post-implementation review.

## Key points
- Release named on the page: Australia. Newer features are Workspace-only.
- Search-result summaries of other pages in the same docs set describe automated triage routing alerts to domain experts, a Smart Assessment engine for multi-stakeholder impact assessment, mapping events to GRC policies, processes and controls manually or with AI, and a 2025 "impacted areas" feature spanning controls, policies, control objectives and risks. These were not fetched.
- The data model (authority document, citation, policy statement, control) aligns with UCF, which ServiceNow GRC can import (seen in search results).

## Could not verify
- Read through WebFetch's model-summarised view of one page; the alerts, impacted-areas and UCF-integration pages were not fetched (two direct UCF integration URLs returned 404). No publication date is shown.
