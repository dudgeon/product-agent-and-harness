---
title: Make Rovo your research assistant – Deep research mode
source_url: https://support.atlassian.com/rovo/docs/using-rovo-deep-research/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [research-synthesis-agents, org-context-grounding, ai-synthesis-hallucination-risk, feedback-triage-agents]
relevance: medium
---

## Relevance to the project
Rovo Deep Research is Atlassian's "research the problem" agent: a planned, multi-step report over org knowledge and connected third-party sources, with citations. The support doc covers what it reads; the engineering blog says reports can be exported to Confluence and names "analyze customer feedback" as a use. For the map, the open question is whether the research output becomes a durable artifact other agents pick up (only "export to Confluence" is claimed).

## Themes
- `research-synthesis-agents`: "taking your prompt and converting it into a research plan, breaking it down into tasks ... provides you with a comprehensive report"; up to 15 minutes.
- `org-context-grounding`: "can access the same sources as typical conversation in Rovo Chat, including organizational knowledge, connected 3P sources, or context added to your prompt like a file, a smart link, or an @mention." (Deep Research reasoning)
- `ai-synthesis-hallucination-risk`: shows per-step reasoning and a Sources list "that you may independently review"; blog says inline citations were added after evaluations found "factual claims were occasionally difficult to verify."
- `feedback-triage-agents`: blog use case: "Analyze customer feedback to identify recurring pain points and feature requests, and summarize actionable insights."

## Key points
- **Documented:** start in Rovo Chat > Deep Research; files can be attached; keep window open; premium feature consuming Rovo credits.
- **Claimed, related post** ([How Rovo Deep Research works](https://www.atlassian.com/blog/atlassian-engineering/how-rovo-deep-research-works), William Li et al., 2025-08-05): starts by gathering foundational data from the Teamwork Graph; plan, parallel sub-task retrieval, reflection rounds, outline, parallel section writing, proofreader agent; "These reports can be effortlessly exported to your Confluence page with clear citations and sources"; models named: Atlassian-hosted Llama 3.2 8B, GPT-4o, GPT-4.1, Claude 3.7 Sonnet thinking (as of Aug 2025); LLM-as-judge evaluation on depth, accuracy, clarity.
- **Not documented in support doc:** the Confluence export (only the 2025 blog claims it).

## Could not verify
- Current export mechanism and whether exported pages keep citation links; current model mix.
