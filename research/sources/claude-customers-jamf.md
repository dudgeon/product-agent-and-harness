---
title: "How Jamf's engineering team turns structured workflows into interactive tools with Cowork"
source_url: https://claude.com/customers/jamf-qa
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [risk-sloped-review, non-engineer-builders, enablement-by-product, skills-marketplace, metrics-review-agents]
relevance: medium
---

## Relevance to the project
Jamf's rollout pairs a risk-tiered governance model ("One Framework, Three Roads": Express, Toll Road, Off-Road) with Cowork skills that turn structured, checklist-shaped work into guided conversational tools, which is a concrete template for how a company could govern and seed a product agent. The case study and Q&A are Anthropic customer pages, so the adoption figures (89% active usage in eight weeks, 285 use cases, ~838 hours/month saved in HR) are the customer's own unaudited claims. The Q&A also shows a plugin used as a data-routing guardrail (warehouse first, live API only when real-time is needed) and an ambition for shared read/write across users, both relevant to how a harness mediates data access and collaboration.

## Themes
- risk-sloped-review: "One Framework, Three Roads": Express (approved tools, no approval), Toll Road (custom Skills, MCP connectors; documentation plus department-level review), Off-Road (custom API builds; architecture and security sign-off) (case study, "The solution").
- non-engineer-builders: non-technical HR staff built many of HR's 21 use cases; a Facilities Director built a location dashboard alone; Q&A says broadest Cowork adoption is not from engineers (Q&A, "Has adoption spread").
- enablement-by-product: 208 employees creating and sharing reusable Skills; 60% of the 15-person Enterprise Transformation team's licensed users are Skills creators (case study, "The outcome").
- skills-marketplace: skills are "reusable by default"; the 285-use-case library is used as a pipeline to pick workflows for deeper API integration (Q&A; case study).
- metrics-review-agents: an AI Department Scorecard built in ~8 hours from Okta, LMS, usage reports and Jira into a self-contained HTML dashboard, reviewed weekly by 16 department leaders (case study).

## Key points
- **Two-lane architecture (case study):** Claude Enterprise (bought via AWS Marketplace) for governed employee knowledge work; Claude on Amazon Bedrock for developer-controlled API automation "that don't need a human at every step", chosen to reuse existing procurement and SOC 2/ISO-27001 controls and usage-based pricing.
- **Governance as self-sorting tiers:** one set of principles (data security, acceptable use, documentation) with three review paths by complexity, so nobody has to ask which process applies.
- **Skill as app (Q&A):** a performance self-evaluation skill asks name, level and role type, builds a personalised competency checklist, probes for concrete examples, pulls recently closed Jira tickets as memory aids, runs 60-90 minutes with a visible checklist, and exports a file to paste back into the spreadsheet plus a level assessment and development plan. Built in under 45 minutes, per the engineer; tested by prompting it to sample questions rather than run the full set.
- **Interactive primitives named:** visible task checklist, the ask-question pause for input, and MCP calls shown alongside ("almost like a heads-up display"). Advice: pick "a workflow that's annoying, structured, and repeatable".
- **Vendor review skill:** a 12-question review where the skill researches the vendor, drafts answers, then walks the reviewer through each for approval (human approves each answer).
- **Plugin as data guardrail:** a plugin bundles skills and MCPs and can set routing rules: warehouse first for historical/aggregated data, live API only for real-time needs, so the skill user never chooses the source. Described as being explored, not shipped.
- **Next step named:** shared read/write between users: a guided ideation template that writes to a persistence layer and uses similarity search to connect people working on related ideas. Most current use is read-heavy.
- **Adoption claims (case study):** 89% active usage in eight weeks; 1,000 licenses assigned in four weeks, 200+ waitlist, expanding to 2,000; Marketing has 62.5% of submitted use cases in production; a policy comms package drafted in ~4 hours vs 2-3 days, review rounds 3 to 1. HR hours figure is an estimate from 21 use cases.
- **Change management:** a "Work on What Matters" campaign that avoids "efficiency"/"optimize" wording and a four-persona readiness framework; communications drafting is the most common skeptic-conversion trigger.
- **Limits:** no quality or error data on skill outputs; the evaluation skill's quality is described anecdotally; no account of failures or governance incidents.
- **Inconsistency:** Nick Benyo is titled "Software Engineer" in the Q&A and "Principal Solutions Architect" in the case study.

## Companion pages
- https://claude.com/customers/jamf (case study: "How Jamf reached 89% active usage in eight weeks with Claude Enterprise in AWS Marketplace")

## Notable quotes
- "The human is still making the decisions. Cowork just makes sure the process doesn't stall or come back with the wrong data." (Nick Benyo, Q&A)
- "It stopped feeling like a chatbot and started feeling like a lightweight app framework." (Nick Benyo, Q&A)

## Could not verify
- Publication dates of both pages.
- How "active usage" and hours saved were measured.
