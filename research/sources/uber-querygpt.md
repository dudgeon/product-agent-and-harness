---
title: "QueryGPT – Natural Language to SQL Using Generative AI"
source_url: https://www.uber.com/us/en/blog/query-gpt/
author: Jeffrey Johnson, Callie Busch, Abhi Khune (Uber)
publisher: Uber Engineering Blog
published: 2024-09-19
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [metrics-review-agents, one-job-per-agent, org-context-grounding, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
QueryGPT is Uber's 2023-24 text-to-SQL tool and an early lesson that later shaped the context graph: similarity search over schemas failed, so Uber narrowed context with curated "workspaces" and split the job into intent, table and column-prune agents, letting the user confirm the tables. It is a dated example of grounding by domain scoping before a company-wide graph existed.

## Themes
- one-job-per-agent: intent agent maps a question to workspaces, table agent proposes tables for the user to confirm, column-prune agent trims schemas; "LLMs are excellent classifiers" (Architecture, Lessons).
- org-context-grounding: 12 system workspaces (Mobility, Ads, Core Services, etc.) plus user-made ones narrow the RAG search; schemas of 200+ columns hit 40-60K tokens (Architecture).
- evals-autonomy-trust: golden set from real logged questions; "vanilla" end-to-end vs "decoupled" (correct intent and tables given) runs; metrics include intent accuracy, table overlap, runs, returns rows, LLM-judged similarity (Evaluation).
- metrics-review-agents: ~1.2M interactive queries/month on Uber's data platform, ~36% from Operations (Problem).

## Key points
- Born at Generative AI Hackdays, May 2023; 20+ iterations.
- Limited release: ~300 daily active users; ~78% said it cut query-writing time; ~10 min to ~3 min per query estimate.
- Open problem: hallucinated tables and columns; planned validation agent and chat mode.

## Notable quotes
- "Picking a business domain allowed us to drastically narrow the search radius for RAG."

## Could not verify
- Current status (absorbed into Finch, Cortana or the context graph) is not stated anywhere on the blog.
