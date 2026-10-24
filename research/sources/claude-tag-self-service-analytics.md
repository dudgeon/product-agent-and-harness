---
title: "Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions"
source_url: https://claude.com/resources/articles/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
author: Clement Peng and Lily Zhao (Anthropic Data Science and Data Engineering)
publisher: Claude (claude.com/resources)
published: 2026-08-13
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [metrics-review-agents, identity-delegation, org-context-grounding, public-by-default-agent-work, ai-synthesis-hallucination-risk]
relevance: medium
---

## Relevance to the project
Anthropic's data team describes running a shared Slack analytics agent on governed definitions, the closest first-party pattern for an analyst-facing agent in this project. The useful parts are the controls: skills treated as served content re-read every conversation so definitions never go stale, a service account scoped to governed tables with PII columns invisible, channel membership treated as an access grant, every query labelled for audit, and per-answer telemetry (skill versions, thumbs-down, data-quality warnings). It also names the core risk plainly: a Slack consumer sees one number without the context to sniff-test it. Anthropic describing its own practice; the ~95% accuracy and 75% figures are its own, unaudited.

## Themes
- metrics-review-agents: loops for weekly standup readouts, experiment monitoring several times a day, KPI anomaly explanations and pipeline failure triage (section "Claude Tag handles repetitive tasks").
- identity-delegation: queries run as a service account, not the asker; "everyone who can mention the bot has the bot's data access", no per-user row-level security (section "Permission the service account deliberately").
- org-context-grounding: wiring Claude Tag to an internal knowledge index (incidents, flags, release notes) to explain why a metric moved (section "Connect to business context").
- public-by-default-agent-work: keep the agent in shared channels and work in threads, not DMs, so threads are a reviewable record (section "Claude Tag threads become the new meeting").
- ai-synthesis-hallucination-risk: stale skill gives "last Tuesday's wrong answer with full confidence" to a consumer cut off from context (section "Refresh skills").

## Key points
- **Foundation from a prior post**: governed semantic layer, skill files encoding analytical conventions, eval suite; ~95% accuracy claimed there (not re-shown here).
- **Skill freshness**: runtime mounts the data repo's skills/ directory and re-reads it every conversation; alternative is skills-over-MCP; verify freshness against an SLA.
- **Runbook skills beyond a "knowledge skill"**: forecasting (including when to refuse), cohorts/retention, funnels, charting, analytical writing (TL;DR, number, mechanism, caveat, calibrated hedging).
- **Five permission controls**: governed-only scope (agent says so when data is outside it); column-level PII classification (Claude flags candidates, human labels, lineage propagates) with no PII clearance; connection path and auth documented in the skill so it fails cleanly; data team owns the channel list; query labels for surface, conversation and requester (audit and cost, not enforcement).
- **Telemetry**: structured event per question; two views, adoption (share routed through governed layer) and correctness (thumbs-down and correction rate by domain); adoption dips usually mean skill drift or an uncovered question class.
- **Proactive mode**: in one data channel Claude Tag answered >75% of questions within a minute or two unprompted over a month; triage loop decides answer, investigate or bring in a human. Example of agent drafting a PR, data scientist approving, Claude merging.
- **Rollout order**: permissions, distribution, telemetry, knowledge index, analytics skills last.
- Limits: examples are "fictional recreations"; no accuracy data from the Slack deployment itself beyond thumbs-down proxy; Claude Tag was in public beta.

## Notable quotes
- "Treat Claude's channel membership as an access grant."
- "A data analytics agent in Slack is a shared read replica of your governed warehouse."

## Could not verify
- The ~95% accuracy figure (comes from the earlier post, not filed here) and the >75% answer rate's quality.
