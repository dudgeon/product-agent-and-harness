---
title: How Anthropic enables self-service data analytics with Claude
source_url: https://claude.com/resources/articles/how-anthropic-enables-self-service-data-analytics-with-claude
author: Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry (Data Science and Data Engineering, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-06-03
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [metrics-review-agents, org-context-grounding, evals-autonomy-trust, compounding-context-repo, org-learning-loop]
relevance: high
---

## Relevance to the project
The most detailed first-party account so far of an analyst-facing agent in production: Anthropic's data team says analytics accuracy is a context-and-verification problem, not a code-generation one, and describes the stack (canonical datasets, semantic layer, pairwise skills, offline evals, provenance footers, correction harvesting) that it credits with moving eval accuracy from 21% without skills to above 95% with them. It gives the project a concrete pattern for analyst and PM metrics agents, a model for keeping skills from rotting (skill docs colocated with the data models and updated in the same PR), and an honest list of what did not work and what remains unsolved (silent plausible-but-wrong answers). It also bears on the "one agent or many scoped ones" question for access control. All numbers are Anthropic's own internal measurements, not independently checked.

## Themes
- metrics-review-agents: Anthropic states 95% of business analytics queries are automated via Claude at ~95% aggregate accuracy, freeing data scientists for causal modelling and forecasting (intro).
- org-context-grounding: four "sources of truth" in descending trust (semantic layer, lineage, query corpus, business context via a company knowledge graph of docs, roadmaps, decision logs and org structure) (Sources of truth).
- evals-autonomy-trust: offline Q/A evals pinned to snapshot dates, results stored as telemetry (skill version, git SHA, model ID), per-domain launch gate at ~90%, ablation per PR (Validation).
- compounding-context-repo: skill markdown colocated with transformation models; a review hook flags reporting-model changes that do not touch a skill file; ~90% of data-model PRs include a skill change (Skills, "maintenance").
- org-learning-loop: a scheduled agent scans stakeholder channels for correction language every few hours, drafts a one-line reference-doc fix and opens a PR to the domain owner; corrections also become evals (Online validation, "Active correction harvesting").

## Key points
- **Framing ("Data is not software").** Unlike code, analytics usually has one correct answer from one correct source and no deterministic proof; the hard part is mapping a question to the right governed entity, after which SQL is "trivial".
- **Three failure modes:** concept-to-entity ambiguity (e.g. what counts as "active"), data staleness, and retrieval failure (the right doc exists but is not found). Each stack layer is assigned to one or more of these.
- **Data foundations.** Fewer, governed canonical datasets with near-duplicates deprecated; standards enforced by tooling, CI and mandate; all data code (models, semantic layer, docs, dashboard definitions) in one repo; metadata maintained as rigorously as transforms.
- **Semantic layer first, by skill instruction.** A tried-and-failed idea: having an LLM auto-generate metric definitions from raw tables and logs was net-negative on evals versus a smaller human-curated layer; recommendation is Claude drafts docs, a human owns the definition.
- **Query corpus null result.** Giving the agent grep access to thousands of prior SQL files moved accuracy by under one point; the answer was present ~80% of the time but the agent did not use it. The team concluded the bottleneck was structure, not access, and distilled the corpus into per-domain reference docs instead.
- **Pairwise skills.** A thin knowledge skill routes (semantic layer first, else ~30 domain reference files); a runbook skill encodes the senior-analyst process (clarify, find sources, query, adversarial sub-agent review) plus a dozen reusable analysis patterns (retention, funnel, rate decomposition). Appendix gives the skill skeleton: IF/THEN/DO NOT trigger description, out-of-scope escalation to owning teams, PII rule (return SQL rather than results for restricted data), mandatory adversarial SQL review, provenance footer.
- **Skill rot is real.** Offline accuracy drifted from ~95% to ~65% in a month before maintenance was treated as engineering work.
- **Same skill on every surface.** On merge, skills sync to a plugin marketplace (IDE users), cloud-storage blobs (hosted apps) and MCP resources (Slack, dashboards, standalone agents); no hardcoded paths.
- **Costs of accuracy.** Adversarial review raised eval accuracy 6% at 32% more tokens and 72% higher latency; swapping the reviewer to a cheaper model lost most of the gain for no real speed-up. Over-refining docs gave three consecutive net-negative iterations.
- **Online validation.** Provenance footer (source tier, freshness, owner); data-quality checks; passive monitoring of semantic-layer share and correction-language share, reviewed weekly.
- **Unsolved.** Silent failures (plausible wrong answers used without objection) are mitigated only by the footer, human sign-off on anything leadership-bound and daily KPI sanity evals; the authors say they lack a robust solution.
- **Starting point and trade-offs.** A few canonical datasets, a few dozen evals and a thin knowledge skill capture most of the upside. Open choices named: build for today's model gaps vs wait for models; audience technicality; spend for accuracy; and data-access posture, which "determines whether you're building one agent or many scoped ones".
- **Limits:** single company with an unusually strong data team; accuracy figures are internal evals, and how "~95% accuracy in aggregate" for live queries is measured is not fully explained.

## Notable quotes
- "Pointing Claude at a warehouse and letting the agents execute can create a false sense of precision." (intro)
- "Treat the query history as raw material for curation, not as a source of truth the agent reads directly." (Sources of truth)

## Could not verify
- How the headline "95% of queries automated, ~95% accuracy" is measured in production versus on the offline eval set.
