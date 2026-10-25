---
title: How to develop a Headless Product Strategy
source_url: https://departmentofproduct.substack.com/p/how-to-develop-a-headless-product
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-09-15
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [pm-tool-connectivity, agent-as-service-many-surfaces, cost-control-routing, identity-delegation, skill-standards, evals-autonomy-trust, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
About making your own product usable by outside agents (MCP, CLI, skills, agent auth, agentic payments), not about agents for PM work, so it bears on the project only indirectly. Two indirect uses: it shows the PM tools a harness would reach (Linear, Notion, Atlassian-style trackers) are being rebuilt for agent callers, with Linear's CEO reported as saying agent-created issues now outnumber human ones; and its tool-design lessons (small discoverable surfaces, a single "code mode" tool, golden-dataset evals of an MCP server) apply to any MCP layer a PM harness would depend on. Company facts are second-hand from vendor posts and talks.

## Themes
- pm-tool-connectivity: Linear's CEO says agent-created issues via MCP outnumber human-authored ones; PostHog reports a 50x rise in headless MCP requests in six months; Replit made its agent callable from Claude, ChatGPT and Slack (intro, step 1). All vendor statements relayed.
- agent-as-service-many-surfaces: "treat your capabilities, data and logic as the product, and the UI as one of many consumption paths"; Salesforce's headless split lets the same rules run in Slack, WhatsApp, mobile or a custom UI (step 1).
- cost-control-routing: Rippling says wrapping existing APIs as MCP tools inflates the AI bill; its single code-mode tool, where the agent writes a short program in a sandbox, is claimed 98% cheaper than chained tool calls and can compute fields no API returns (step 2). Vendor claim.
- identity-delegation: WorkOS Agent Auth caps a delegated session at the intersection of user permissions and an agent ceiling, with step-up auth pausing sensitive tool calls; cites a UK AI Security Institute evaluation where agents defeated CAPTCHA and signup defences unprompted (step 4).
- skill-standards: distinguishes a tool (something an agent calls, with a schema, that can fail) from a skill (something an agent reads, telling it how to use tools well); Webflow ships skills for Codex and ChatGPT (step 3).
- evals-autonomy-trust: Rippling tested its MCP against 50+ golden cases (prompt, reference answer, stubbed data, expected call sequence), judged on right functions, right path, call success and final answer (step 5).

## Key points
- **Five steps:** separate value from interface and pick high-value use cases; expose it in an agent-usable shape (APIs, MCP, CLI; the post focuses on MCP); package expertise as skills; build identity, permissions and payment rails; dogfood agent access internally before shipping.
- **Diagnostics for step 1:** find decisions enforced only by the UI, trace one transaction by hand, and mine API logs for customers already automating or scraping (an approach attributed to Ramp's CPO).
- **Pricing:** if work moves from logged-in people to agents, per-seat pricing may stop fitting; ask whether customers paid for the screen or the outcome.
- **Payments:** Stripe's agentic payments (Machine Payments Protocol, Link via agents, single-use cards); a Stripe PM is quoted as more bullish on B2B than consumer agent payments.
- **Future:** Meta's Muse agent reportedly used 10x the tokens Meta predicted; the author doubts everyone will collapse into one app, because people enjoy using some software.
- Includes prompts for finding logic trapped in the UI and a downloadable list of 30+ recent MCP launches (not retrieved).

## Notable quotes
- "A skill is something an agent reads." (step 3)

## Could not verify
- Linear, PostHog, Rippling, Replit, Salesforce and Meta figures are relayed from screenshots and talks; none of the primaries were read.
- Retrieved through a paid subscription; summarised, not reproduced.
