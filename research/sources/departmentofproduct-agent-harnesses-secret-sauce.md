---
title: Are Agent Harnesses the new "secret sauce" for Product Teams?
source_url: https://departmentofproduct.substack.com/p/are-agent-harnesses-the-new-secret
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-04-29
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [harness-over-model, build-vs-buy, human-review-gates, risk-sloped-review, work-structure-spectrum, pm-tool-connectivity, meta-harness, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
A PM-audience explainer that frames the agent harness as the place product teams now differentiate ("agentic moats"), built around Square's head of product calling Managerbot's harness the "secret sauce". It distils five harness principles (brain/hands/session split, fixed rules mixed with AI steps, designed human approval, tool curation and progressive disclosure, self-improving harnesses), each pinned to a company case. Every company fact is second-hand from vendor posts, press and one VentureBeat interview; there is no new data. Its value for the strategy is the plain-language framing and one sharp design question for PMs: "which decisions belong to the model, and which belong to the system?", answered by reversibility. Bears on loop-source, review-and-autonomy and governance-control-plane.

## Themes
- harness-over-model: opens with Anthropic's harness-design experiments (solo agent 20 min/$9 with a broken game vs a three-agent harness 6 h/$200 that worked) and draws the lesson that "the right harness for last year's model may be over-engineered for this year's" (section "Anthropic's engineer demonstrates..."). Second-hand from [Anthropic's post](anthropic-harness-design-long-running-apps.md).
- build-vs-buy: harness design as the new differentiator; Square's head of product names context management and progressive tool disclosure "at the harness layer" as the secret sauce; Jack Dorsey is reported as wanting the harness to become infrastructure for organisational intelligence (intro). Second-hand from VentureBeat.
- human-review-gates: Managerbot never executes an action (shift change, campaign, reorder) without the seller's explicit approval; the post says approval is wired into the loop rather than bolted on, and ties it to Block's regulatory history and lessons carried over from the Cash App bot (principle 3).
- risk-sloped-review: proposes splitting actions by reversibility: easy-to-undo actions (draft email, schedule proposal, summary) in the agent's free zone; hard-to-undo ones (payments, production publish, financial records) in a hardcoded layer the model cannot bypass (principle 2).
- work-structure-spectrum: Stripe Minions "blueprints" mix open-ended agent steps with mandatory fixed steps (lint, security scan, commit format); GitHub Copilot coding agent runs CodeQL, secret scanning and dependency review before a human sees the PR (principle 2). Second-hand from [Stripe Minions part 2](stripe-minions-part-2.md) and [GitHub Copilot cloud agent docs](github-copilot-cloud-agent.md).
- pm-tool-connectivity: progressive tool disclosure at Square (sellers touch hundreds of tools; expose only those relevant to the task); Stripe's Toolshed MCP server with about 500 tools, each agent given a curated subset; Intercom Fin's MCP connectors to Shopify, Salesforce, Stripe and Jira (principle 4).
- meta-harness: describes the Stanford "Meta-Harness" optimiser (an agent rewrites harness code from logged traces; reported first among Claude Haiku 4.5 agents on TerminalBench-2, second overall on Opus 4.6) under the label "self-improving harnesses", and calls it not production-ready (principle 5). This is the optimiser sense of the term, not the layer-above-harnesses sense. Primary: [Meta-Harness paper](arxiv-meta-harness-optimization.md).
- vendor-claims-vs-independent-evidence: all case facts restated from company announcements and one interview; no outcome data for Managerbot; the 20+ example table at the end is an image not checked here.

## Key points
- **What a harness is (section 1):** scaffolding around a model that chunks big tasks, manages memory and context, coordinates several agents (generator and evaluator), provides tools, and keeps long sessions on track. Argued to matter for both internal tools and user-facing features.
- **Principle 1, brain / hands / session decoupling:** keep the model stateless, spin tool sandboxes up and down on demand, and keep the session log in its own durable store, so a container crash loses nothing, many agents can run in parallel and credentials stay out of the sandbox. The post says OpenAI shipped the same split in its April 2026 Agents SDK update. Primary for the pattern: [Anthropic, Scaling Managed Agents](anthropic-engineering-scaling-managed-agents.md); OpenAI side: [Agents SDK docs](openai-agents-sdk-docs.md).
- **Principle 2, mix AI steps with fixed rules:** Stripe Minions (over 1,300 PRs merged a week, no human-written code, per Stripe) gets quality from blueprints, not from model capability. The reversibility test decides what goes in the fixed layer.
- **Principle 3, human-in-the-loop as a designed interface:** Managerbot monitors inventory, sales velocity, shift cover and customer patterns, then proposes actions the seller must approve. Mentions Block's $80m state regulator fine in early 2025 over Cash App compliance as context (the post's own inference that this motivates the design).
- **Principle 4, build the harness around tools:** tool selection decides what feedback loops are possible (Playwright let Anthropic's evaluator click through the app); tool management "becomes its own discipline" at scale.
- **Principle 5, self-improving harnesses:** a coding agent reads a filesystem of past runs (code, score, full trace) and proposes the next harness version; the loop repeats. Called "dangerous territory" but likely to be tried by large companies.
- **Further reading:** Anthropic harness design, Claude Managed Agents, Addy Osmani on agent harness engineering, VentureBeat on Managerbot.

## Notable quotes
- "which decisions belong to the model, and which belong to the system?" (principle 2)
- "the right harness for last year's model may be over-engineered for this year's" (Anthropic section)

## Could not verify
- The Square head of product quote and the Dorsey "organisational intelligence" line come via VentureBeat (footnote 1); the VentureBeat article is not filed and was not read here.
- The OpenAI April 2026 Agents SDK claim was not checked against OpenAI's changelog.
- The closing table of 20+ real-world examples (Spotify, Slack, Microsoft and others) is an image and was not available in the text.
- Retrieved through a paid subscription; summarised, not reproduced.
