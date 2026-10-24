---
title: Using the Ops Expert agent (formerly Rovo Ops)
source_url: https://support.atlassian.com/rovo/docs/using-ops-guide/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [agent-factory-sdlc, org-context-grounding, compounding-context-repo, opportunity-to-code-chain, cost-control-routing]
relevance: medium
---

## Relevance to the project
Ops Expert is Atlassian's "operate and learn" agent: it triages alerts and incidents with history from Confluence runbooks, past Jira and JSM incidents and Slack, drafts post-incident reviews as a Jira work item or Confluence page, and creates Jira work items for PIR action items. That last step is the documented loop from operations back into the backlog. The page also documents how Teamwork Graph context is billed, including when third-party agents read it over MCP or the CLI.

## Themes
- `agent-factory-sdlc`: "create post-incident review reports (PIR) in a Jira work item or on a Confluence page." (Create PIR)
- `opportunity-to-code-chain`: suggested follow-ups after a PIR: "Create a Confluence page for this PIR" and "Create Jira tickets for action items in this PIR"; "Suggest problem ticket" when an incident recurs.
- `org-context-grounding`: sources include "Confluence (related articles, runbooks, post-mortem reports), Jira (past work items), Jira Service Management (past incidents and alerts), Microsoft Sharepoint docs, Google docs, and historical chats from Slack." (Triage incidents)
- `compounding-context-repo`: "For a previous incident, Ops Expert provides a concise summary of the details captured in a shared Post-Incident Review"; PIRs as "living documents that guide the resolution of similar incidents."
- `cost-control-routing`: credits for Intelligence and for Context ("when an enriched context is retrieved from the Teamwork Graph (TWG) via API calls ... when you use third-party AI tools, such as Claude or ChatGPT, with Atlassian data via the Teamwork Graph CLI or the Atlassian Rovo MCP server"); allowances apply from December 3, 2026.

## Key points
- **Documented:** `/create-pir` in Rovo Chat creates a PIR work item, links the Primary incident, pre-fills a summary and timeline; "Chat with Ops Expert" from the JSM incident view; PIR from a Slack channel's history via JSM's Slack integration.
- **Documented tools:** Find alerts (natural language to AQL), Create PIR, Find similar incidents, Suggest related people, Summarize incident, Find incidents, Find cause of incident, Suggest problem ticket, Suggest incident fields; MCP: New Relic tools (e.g. "What is the deployment impact of this alert?").
- **Vendor-claim, related page** ([Incident management and AIOps guide](https://www.atlassian.com/collections/service/guides/incident-management-aiops), 2026-09-08): "When an incident closes, Rovo Ops automatically drafts the post-incident review from the incident record, alert data, and the swarm channel"; six automation templates including "when an incident closes, automatically create a PIR"; AI alert grouping with "Per-organization machine learning models"; root-cause investigation draws on "commits, pull requests, deployments, and feature flags"; MCP to New Relic and Dynatrace; Premium and Enterprise; customer result "75% less alert noise" (unnamed customer).
- **Not documented:** whether PIR action items carry a link back to the PR or deployment that caused the incident.

## Could not verify
- Alert grouping support doc; the named customer for the 75% figure.
