---
title: "How we restructured Airtable's entire org for AI | Howie Liu (co-founder and CEO)"
source_url: https://www.lennysnewsletter.com/p/how-we-restructured-airtables-entire-org-for-ai
author: Lenny Rachitsky (host), Howie Liu (co-founder and CEO, Airtable)
publisher: Lenny's Podcast
published: 2025-08-31
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [pm-persona-role-expansion, spec-becomes-prototype-and-evals, evals-autonomy-trust, research-synthesis-agents, work-structure-spectrum, org-learning-loop, enablement-by-product]
relevance: medium
---

## Relevance to the project
A first-party account of a decade-old SaaS company reorganising product, engineering and design for AI: a "fast thinking" AI Platform group shipping near-weekly beside a "slow thinking" group for deliberate infrastructure bets. For the project it matters in three places: operating-model evidence for how an incumbent splits exploratory and deliberate work (work-structure, sequencing); a CEO's argument that prototypes replace decks and PRDs for AI features (intent-shaping-and-spec); and a useful counterpoint on evals, that for novel capabilities you should start with "vibes" and only write evals once the use-case cluster is known (pm-agent-evaluation). Downgraded from high: it is mostly about leadership and culture, with little on harness or PM workflow mechanics.

## Themes
- pm-persona-role-expansion: "as a PM, you need to start looking more like a hybrid PM prototyper, who has some good design sensibilities" (55:00); each of PM, eng, design must be "minimally good at the other two" (57:43); extends role collapse to marketing and sales (AEs must be SE-fluent) (1:09:25-1:12:06). Notes that at Stripe the DRI is sometimes the engineer rather than the PM (56:33).
- spec-becomes-prototype-and-evals: "prototypes over decks": in a deck or PRD, claims about the agent "are just words"; a functional prototype lets you try unrealistic, non-golden-path prompts and feel latency and reasoning exposure (48:49-50:24). He shares landing pages, deep research links and chat threads instead of memos (47:02).
- evals-autonomy-trust: contrarian take: for "a completely novel product experience ... you should actually not start with evals and you should start with vibes" (1:03:50); evals become useful once the form factor and use-case cluster have converged, e.g. a web-crawling list-building agent scoped to entity types (1:05:55).
- research-synthesis-agents: as Airtable's top inference-cost user, he runs map-reduce LLM passes over a year of sales-call transcripts for product, positioning and segmentation insights, spending "hundreds of dollars" per run and calling it trivial against consulting fees (14:03-15:47). Asserted, not demonstrated.
- work-structure-spectrum: fast-thinking (AI Platform, near-weekly "jaw-dropping" capability launches) versus slow-thinking (e.g. HyperDB, multi-hundred-million-record datastore) groups that complement each other: fast creates top-of-funnel, slow lets adoption grow into large deployments (21:38-23:33). Execution moved from "deterministic resourcing and timelines" to "experimentation and iteration-driven" (50:24).
- org-learning-loop / enablement-by-product: CEO leads by sharing his own experiments; tells staff they may cancel meetings for a day or a week to play with AI tools, "say that I told you to do it" (48:49).

## Key points
- Reorg history (19:01-22:07): from feature/surface teams (search, mobile) that think incrementally, to business-unit pillars (enterprise scale, teams/self-serve, AI, solutions, infra), to the current fast/slow split. About half the EPD org works on AI capabilities, with a weekly AI sprint check-in (18:29).
- Fast-thinking hires need autonomy and full-stack thinking about problem and "wow factor"; some acquired founders, many internal (23:52-26:38). Example design problem: Omni (Airtable's app-building agent) adding code generation for bespoke views, requiring decisions about what models can one-shot and where to put human approval, review and re-prompting (25:29).
- Agent strategy (32:20, 36:50-38:31): the agent became the default way to do everything in Airtable; the app is "almost like an artifact" the agent manipulates. Argument against pure vibe coding for business apps: reliability, data/security issues and "context collapse" as code grows; Airtable's no-code primitives act as a domain-specific language for the agent, and non-technical users can fall back to the GUI to inspect and edit. Relevant to artifact-and-project-structure (structured primitives as the agent's working surface).
- "Field agents" pod: agents that run inside customer apps (web research per row, document analysis, in future "generate a prototype of a feature from a PRD") (1:01:00).
- IC CEO: cut standing one-on-ones in favour of timely, insight-driven meetings; uses AI "multiple times an hour" (16:41, 1:09:16). Refounding test: if you can't execute your mission better with existing building blocks than from scratch, sell (35:10).

## Notable quotes
- "It's hard to taste the soup without participating in at least some part of creating the soup." (12:14)
- "In a deck or in a PRD ... those are just words. The real proof is in the pudding." (48:49)

## Could not verify
- Transcript read in full (Substack auto-transcription; some garbled names, e.g. "ICCO").
- Financial claims (over $100M free cash flow, ~$12B valuation) are from the show notes and the guest; not checked.
- No numbers are given on the fast group's size, output or results beyond "near-weekly" shipping and anecdotal user comments about velocity.
