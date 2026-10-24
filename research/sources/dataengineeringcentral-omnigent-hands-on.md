---
title: "Omnigent. Too afraid to ask what a meta-harness for Agents is?"
source_url: https://dataengineeringcentral.substack.com/p/omnigent-too-afraid-to-ask-what-a
author: Daniel Beach
publisher: Data Engineering Central (Substack)
published: 2026-08-31
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, shared-persistent-sessions, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
The only first-person, hands-on account of Omnigent found by a writer with no disclosed Databricks affiliation (the post is sponsored by Delta Lake, a Databricks-originated project, so not fully neutral). It shows what a short trial actually surfaces: policies are the most valued feature, the single-user local path works, and the shared-server path broke on setup. It bears directly on what an Omnigent trial for a regulated setting should test (server deploy, policy scope, audit), since the author never got that far.

## Themes
- [[meta-harness]]: install by one-line curl, `omnigent setup` detected Claude Code and GitHub Copilot (Copilot needed a separate token); `omnigent claude` ran Claude Code inside tmux with a local web UI on port 6767 (install section).
- [[shared-persistent-sessions]]: the collaboration path (Railway deploy for phone/remote access) repeatedly failed health checks; logs showed a missing `DATABASE_URL` that the guide does not mention; adding a localhost Postgres URL did not fix it and he stopped (collaboration section).
- [[vendor-claims-vs-independent-evidence]]: a single short trial; the author says he barely scratched the surface. No measurement of policy effectiveness or cross-vendor review quality.

## Key points
- Policies: he asked the agent in plain language (via the web UI) to require approval before git commit, push and bash; the agent then asked permission when committing a README change. He found the policies session-scoped and needing more specificity than expected. Policies were his favourite feature.
- Polly (built-in coding orchestrator): asked for a plan for a Rust-based Python library over DataFusion/Arrow writing Delta Lake to S3; watched several agents work in the web UI; says it "worked". He expects multi-agent routing to improve results but did not measure it.
- Uneasy about phone-based agent access.
- Reader comment (State of Play): AI changes already bottleneck at review, so a second AI reviewer may add to the queue rather than shorten it. Not answered.

## Notable quotes
- "The policies were probably my favorite part of Omnigent."

## Could not verify
- Which Omnigent version he used (not stated in the summarised text); text was read through a summarising fetch.
