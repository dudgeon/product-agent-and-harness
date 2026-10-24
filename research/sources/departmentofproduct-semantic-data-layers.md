---
title: Why Semantic Data Layers matter to product teams
source_url: https://departmentofproduct.substack.com/p/why-semantic-data-layers-matter-to
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-06-17
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [metrics-review-agents, org-context-grounding, legible-org-for-agents, single-agent-many-skills, tacit-knowledge-capture, ai-synthesis-hallucination-risk]
relevance: medium
---

## Relevance to the project
Argues that the hard part of self-serve analytics agents is knowing what a question means, not writing SQL, and that a governed semantic layer (one canonical, owned definition per metric) is the fix. Its anchor case is Anthropic's data team, relayed second-hand: about 95% of data requests automated, and eval accuracy on analytics questions raised from about 21% to above 95% after adding a semantic layer and two skills. For the project it is evidence for the context-and-memory and metrics-review dimensions: an analytics agent for PMs depends on organisation-owned definitions, and the skill design (a thin router skill plus an analyst-workflow skill with adversarial review) is a concrete pattern. The Anthropic primary is not yet filed and should be before the numbers are used.

## Themes
- metrics-review-agents: Anthropic's self-service reporting system, said to automate about 95% of data requests; accuracy on its evals rose from about 21% to consistently above 95%, around 99% in some domains (introduction; "Why it matters now").
- single-agent-many-skills: two skills in Anthropic's setup: a knowledge skill that only routes (check the semantic layer first, then domain reference files) and an analyst skill encoding a senior analyst's workflow (clarify the question, fetch sources via the router, run the query, then an adversarial review step before the answer counts) ("Speeding up product discovery").
- tacit-knowledge-capture: Anthropic tried letting the LLM write metric definitions and it failed; the rule became "AI drafts the documentation, a human owns the definition", with a named owner per definition so it does not drift ("Standardising definitions").
- legible-org-for-agents: the semantic layer as the place the organisation's vocabulary (activation, feature adoption, new user, customer PII) is made explicit, versioned and queryable by agents and BI tools alike.
- org-context-grounding: a discovery-research pipeline sketch: centralise research as markdown, embed into a vector index tagged by product area/date/segment, build governed views over common metrics, and use the 20-30 most-asked discovery questions as both build target and eval set (80% accuracy before wider rollout).
- ai-synthesis-hallucination-risk: Uber's File Semantic Analyzer (second-hand): files from Drive and shares are OCR'd, chunked, classified by meaning, routed by a rules engine, with high-stakes cases sent to a human; claimed 97% fewer false positives and about four person-years saved annually across about 150,000 files.

## Key points
- **Definition:** a translation layer between raw warehouse tables and anything querying them; turns columns into named, governed business concepts so "monthly active users" returns one number wherever asked.
- **Why now:** precise definitions are what let non-technical staff and agents self-serve; vendors (Microsoft, Databricks, SAP) are reported to be fighting to own this layer (citing The Information).
- **Anatomy:** raw tables at the bottom; metric and dimension definitions (usually YAML via dbt, Cube, Metriql or LookML) in the middle; consumers (BI, agents, analysts) on top. Questions that map to a defined metric compile to SQL automatically.
- **How to start (author's advice):** pick the five most-argued metrics; write inclusions and exclusions (exclusions are where disagreement lives); encode as a governed view, not a doc; delete the near-duplicate alternatives; give each an owner.
- **In-product search:** semantic search lets users describe what they want without exact terms (GitHub Copilot semantic code search as the example).
- **Visualising the model:** a prompt to have Claude build an interactive 3D view of raw sources and governed metrics with their dependencies, for explaining the model to non-technical stakeholders (described, not reproduced).

## Notable quotes
- "generate documentation with AI, but have a human own the definition" (author's paraphrase of Anthropic's rule)

## Could not verify
- The Anthropic data-team post (the source of the 95%, 21% and 99% figures and the two skills) was not linked in the retrieved text and is not filed; the quoted "biggest challenge" passage was an image.
- Uber's FSA figures are company-reported, relayed second-hand.
- Paywalled text summarised, not reproduced.
