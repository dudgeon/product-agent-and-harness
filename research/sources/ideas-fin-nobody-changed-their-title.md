---
title: "Nobody changed their title. Everybody changed their job."
source_url: https://ideas.fin.ai/p/nobody-changed-their-title-everybody
author: Karen Church (Lead, Research & Data Science (RAD), Intercom / Fin)
publisher: Fin Ideas (Intercom Substack, ideas.fin.ai)
published: 2026-07-07
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [research-synthesis-agents, feedback-triage-agents, org-context-grounding, pm-persona-role-expansion, ai-synthesis-hallucination-risk]
relevance: high
---

## Relevance to the project
The best first-party evidence for Intercom's "talk to customers" and "research the problem" rows: a 40-person research and data science team where researchers pull their own data, synthesise hundreds of sales calls and win/loss records in one session, start from existing evidence before new research, and turn 60+ customer interviews into a queryable skill. Named internal tools: Claude4Data and Cockpit (which clusters customer feedback with an LLM job). It does not describe how findings are handed to PMs, and does not name Fin conversation data as a research input.

## Themes
- research-synthesis-agents: one researcher synthesised hundreds of sales calls, win/loss records and interviews in a single session, work that previously took weeks or didn't happen; a 60+ customer interview study became a searchable repository with a queryable skill.
- feedback-triage-agents: Cockpit's feedback tool consolidates fragmented customer feedback and uses an LLM job to cluster and summarise it; built in about a month by a data scientist without an engineering background.
- org-context-grounding: a shared semantic layer is being built so AI skills define metrics consistently; "Creating shared, verified infrastructure for our AI tools is essential to their accuracy."
- pm-persona-role-expansion: "SQL used to be the majority of the job, and now it's near zero"; data scientists build pipelines and make product changes directly rather than handing off to engineering.
- ai-synthesis-hallucination-risk: researchers spend more time verifying AI-generated findings; deep focused analysis harder to protect.

## Key points
- Research inputs named: churn surveys, product satisfaction scores, win/loss records, sales-call transcripts (Gong), Salesforce notes, emails, Slack threads, customer feedback.
- "Starting from evidence that already exists, rather than running something new, used to be the fallback option." Now often the first step.
- Customer discovery itself was not made faster.
- Outputs: HTML reports replacing Tableau dashboards; customer ROI deck agent (450+ decks, 100+/month); daily win/loss and live-deal system feeding a fortnightly leadership deal briefing.

## Could not verify
- Hand-off from research to PMs/product teams; whether Fin conversation data (Insights, Topics, CX score) feeds Intercom's own roadmap; survey method behind the "what changed" claims.
