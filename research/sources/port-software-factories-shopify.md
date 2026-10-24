---
title: Inside Shopify's software factory
source_url: https://software-factories.port.io/shopify
author: Port (Inside the Software Factory research index)
publisher: Port (software-factories.port.io)
published: 2026-09-08 (page "Updated" date)
retrieved: 2026-10-24
type: report
evidence: independent
filed_by: competitive-teardown-shopify-river
themes: [vendor-claims-vs-independent-evidence, cost-control-routing, shared-persistent-sessions, agent-factory-sdlc, outcome-measurement-gap]
relevance: medium
---

## Relevance to the project
The best secondary synthesis found. It joins River/Aquifer, Dispatch, Roast/Boba, the LLM proxy, UDP distillation and Quick into one picture, cites 10 sources, and ends with an explicit **"Gaps in the record"** list. **Most content restates Shopify and press claims.** Its original contribution is the source-critical framing. Port is a developer-portal vendor, so the page is also marketing for its "software factory" taxonomy.

## Themes
- `vendor-claims-vs-independent-evidence`: "1 in 8" and Dispatch's $400k are self-reported, with "no stated definition of 'coauthored' or 'verified finding'". The richest operational detail comes from "press interviews and a VC firm's content arm", not the engineering blog. The April 2025 memo is "a mandate, not a mechanism". "No source states a single unifying motivation connecting the memo to the engineering systems."
- `cost-control-routing`: one LLM proxy for all tools, with bulk purchasing, failover, **PII masking and prompt-injection detection** (its sources 5–7). No per-team cap, but spend alerts ("10-hour mark" in one account, "$250-a-day" in another).
- `shared-persistent-sessions`: a restatement of Aquifer's session / harness / sandbox split and "session cells".
- `agent-factory-sdlc`: maturity rated "L4 · AI-native of 5". Patterns tagged: background-agent, adversarial-verification, multi-provider, spend-control, shared-agent-context, mcp-gateway, enforcement-over-instruction, adoption-by-mandate.
- `outcome-measurement-gap`: Shopify "does not track AI-authored lines of code or PR counts as a success metric". It tracks reversion rate and weekly demos.

## Key points
- People named: Farhan Thawar, Javier Moreno, Burke Libbey, Zack Deveau, Obie Fernandez.
- Headcount about 7,600 (10-K, 2025-12-31). Revenue $11.56bn, GMV $378.4bn (FY2025).
- Hiring: director-level-plus candidates do live coding with AI allowed. "If they don't use a copilot, they usually get creamed" (Thawar, Pragmatic Engineer, 2025-07-02).
- Stack list: River (coding agent), Aquifer (hosting), World (monorepo), Dispatch (security), Roast/Boba (workflow), internal LLM proxy.
- Warns that Quick adoption (50,000+ sites) is often mis-cited as engineering evidence, and that the merchant-facing "Shopify AI Toolkit" is conflated with internal practice.
- "No source lays out a roadmap."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- The PII-masking and prompt-injection-detection claims for the proxy are attributed to Bessemer, VentureBeat and Pragmatic Engineer. They were not in the Bessemer text read for this teardown, so they probably come from the Pragmatic Engineer 2025 episode, which was not read.
