---
title: Building an agentic harness that outlasts the model
source_url: https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model
author: Zack Deveau (Shopify Application Security)
publisher: Shopify Engineering blog
published: 2026-07-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [harness-over-model, cost-control-routing, agent-failure-modes, evals-autonomy-trust, one-job-per-agent]
relevance: medium
---

## Relevance to the project
This post is about **Dispatch**, Shopify AppSec's multi-agent vulnerability-scanning harness. It is not River or Aquifer, but it is part of the same AI-native engineering stack, and it is one of the few Shopify posts that publishes **costs per run** and an explicit **verifier-uses-a-different-model** rule. It is strong first-party evidence for "the harness, not the model, is the durable asset". River later carries remediation of these findings to merge; see the separate post "How River takes security work from a fix to merge" (2026-09-02, filed separately).

## Themes
- `harness-over-model`: newer security-tuned frontier models found more candidates, but in one audit all 30+ candidates were downgraded or false positives. "The models are getting better, but the most important piece of the system remains the harness." The durable advantages are a test oracle, partitioning, cross-model verification, and deterministic code owning credentials, Git and storage (§The harness outlasts the model).
- `cost-control-routing`: a full app scan costs **$50–$300** with public frontier models, and incremental diff scans **$5–$50**. Partitions sized at about 20–30% of the context window (§The results; §Keeping costs low).
- `agent-failure-modes`: "security generalist" agents chased unordered "potential" findings, filled their context or compacted, and produced non-deterministic, theoretical results (§Producing consistent and reliable results).
- `evals-autonomy-trust`: a finding counts only if a generated integration test proves exploitability (two-tenant fixtures, public stack, cross-tenant data). Otherwise it is rejected or downgraded. Benchmarks reintroduced past confirmed vulnerabilities to compare partitioned and unpartitioned scans.
- `one-job-per-agent`: category-specific Hunter agents per partition, sequential Verifiers, and per-finding fix-author agents.

## Key points
- **Dispatch** is "a thin Ruby client" orchestrator. Its stages are test bootstrap → architecture documentation → file cataloguing → partitioning (JSON artifact) → hunting (parallel, one Hunter per partition, with cross-repo code-search skills) → verification (sequential, **different model from hunting**) → post-processing (Ruby: dedupe, severity) → reporting → remediation (draft PRs with tests).
- State lives in a custom Rails backend. Follow-up runs scan only diffs and update persisted artifacts.
- **Results:** complete scans of 80+ apps including Shopify Core. Over about six weeks, thousands of scans produced 300+ findings, valued at more than $400,000 in bug-bounty equivalent, including two Critical.
- **Determinism:** "hand agents deterministic scripts inline, or author dedicated skills that call scripts", for example a skill enforcing JSON structure.
- Credentials: "Deterministic code that owns credentials, Git, and storage so the agents don't have to". This is the only credentials statement here.

## Notable quotes
- "A better hunter also produces more confident-sounding noise, and noise sent to a developer is worse than no finding at all."
- "You'll keep this part as new models come and go; this is where the innovation is."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- Which models were used (only "publicly available frontier models" and "security-tuned frontier models"), and whether Dispatch runs on Aquifer.
- The bug-bounty valuation method.
