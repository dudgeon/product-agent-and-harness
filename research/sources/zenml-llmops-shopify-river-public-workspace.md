---
title: "Shopify: Building a Public AI Agent Workspace for Organizational Learning"
source_url: https://www.zenml.io/llmops-database/building-a-public-ai-agent-workspace-for-organizational-learning
author: ZenML (LLMOps Database editorial, likely AI-assisted)
publisher: ZenML LLMOps Database
published: unknown (2026, after 2026-05-09)
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: competitive-teardown-shopify-river
themes: [org-learning-loop, vendor-claims-vs-independent-evidence, identity-delegation]
relevance: low
---

## Relevance to the project
A structured summary of Tobi's "Learning on the Shop floor". **It restates Shopify's claims**, and it was the source most secondary outlets (e.g. AI Slopcast) used for the numbers. Its useful part is the critical-assessment list, including **psychological safety** and **missing security/permission model**. It also contains a conflation error worth knowing about.

## Themes
- `org-learning-loop`: the Lehrwerkstatt framing. A checkout data-warehouse skill was reused by "twelve other teams". Channels "pre-load the zones, skills, and instructions". Memory is "constantly learning and un-learning". The merge rate went from 36% to 77% over two months, attributed to people writing down what River should have known.
- `vendor-claims-vs-independent-evidence`: "Selective Reporting", "Code Quality" (the 23% unmerged are not discussed), "Attribution" (performance metrics distorted by an AI author), "Model Dependencies" (models not disclosed).
- `identity-delegation`: "there must be boundaries around what code or data River can access. The security model and permission system aren't described."

## Key points
- Restated figures: 5,938 employees, 4,450 channels (30 days), 1,870 PRs opened in a week, about 1 in 8 merged PRs authored by River, merge rate 36%→77% over two months. Tobi's channel is named here as "#tobi-working-with-river" (100+ people). AI Slopcast and AI Enabled PM say "#tobi_river".
- **Error:** it says River "opened 1,870 pull requests in just one week ... representing approximately one in eight merged pull requests". That conflates PRs opened with the merged-PR share; Tobi gave them as separate facts.
- Psychological safety concern: "Asking for help feels different when the whole company can see the question" (quoting Tobi), with a note that effects on different personality types and seniority levels are unexplored.
- Production gaps listed: concurrency and rate limits, cost, uptime/SLOs, access control.

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- The exact channel name (#tobi_river vs #tobi-working-with-river). Check against Tobi's original.
