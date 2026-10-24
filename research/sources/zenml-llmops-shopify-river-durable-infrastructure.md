---
title: "Shopify: Building River: A Slack-Native AI Agent on Durable Infrastructure"
source_url: https://www.zenml.io/llmops-database/building-river-a-slack-native-ai-agent-on-durable-infrastructure
author: ZenML (LLMOps Database editorial, likely AI-assisted)
publisher: ZenML LLMOps Database
published: unknown (2026, after 2026-05-28)
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: competitive-teardown-shopify-river
themes: [shared-persistent-sessions, single-agent-many-skills, vendor-claims-vs-independent-evidence, harness-over-model]
relevance: medium
---

## Relevance to the project
A long structured summary of "Under the River" with a "Critical Assessment" section. **It mostly restates Shopify's claims.** Its value is (a) a clean digest of the Aquifer architecture (session / harness / sandbox; profiles; interactive, automation and job modes), (b) two data points not in Tobi's article: the **median session length of 19 minutes, median 50 tool calls**, and **7,000+ people (1,200 more than when initially announced)**, and (c) a list of what Shopify did *not* disclose.

## Themes
- `shared-persistent-sessions`: session = durable identity plus an append-only Postgres event log. The harness is disposable and lives outside the sandbox. Sandboxes are disposable, sometimes warm-started. "Session cells" (Go runtime + harness in one process group) exit when idle and restart on any host: "cattle, not pets, at the session level".
- `single-agent-many-skills`: River is one "profile". A profile is data (system prompt, skills, extensions, sandbox policy, model defaults), built with Nix and shipped as bundles. Other profiles include PR review and "Vanilla", the headless "pi" agent. Three modes: interactive (River), automation (PR review, woken by external systems), job (CI/batch, ephemeral).
- `vendor-claims-vs-independent-evidence`: it lists what is missing: model selection, prompts, cost, error rates, failure modes, quality control, hallucination handling, security beyond the sandbox, baselines for the 3,536 PRs, A/B testing, provider-outage handling.
- `harness-over-model`: "Decouple the brain from the hands", citing Anthropic's April 2026 "Scaling Managed Agents".

## Key points
- 30-day figures (from the `river_sessions` domain table): 59,918 sessions, 5,170 channels, 7,000+ people "(1,200 more than when initially announced)", 3,536 River-coauthored merged PRs. "Already wrong, in the upward direction."
- Median session 19 minutes, median 50 tool calls.
- World also contains skills, conventions, intent documents, runbooks, AGENTS.md and zone knowledge. After a solve, people leave "a pebble, a skill update, an AGENTS.md diff, sometimes a whole new shared skill."
- Shopify "mine this corpus" of public threads to feed River's skills, prompts and defaults, with no retraining.
- The post itself is "Co-authored by River".
- Three closing principles: decouple brain from hands ("You will not be able to retrofit it"), multiplayer by construction, next agent = profile not platform.

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- The 19-minute / 50-tool-call medians and the "+1,200 people" detail are attributed to Under the River. Those details are first-party via this summary; the coordinator holds the original.
- Authorship: no named author.
