---
title: How to Identify Opportunities for AI Automation - a Framework for Product Teams
source_url: https://departmentofproduct.substack.com/p/how-to-identify-opportunities-for
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-11-26
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [work-structure-spectrum, risk-sloped-review, human-review-gates, evals-autonomy-trust, agent-factory-sdlc]
relevance: high
---

## Relevance to the project
This is the source of DoP's "AI Automation Opportunity" framework: score each candidate task on three axes (safety, i.e. the cost of a wrong output; volume; verifiability) and plot them on a canvas. It is a ready-made, PM-friendly instance of the multi-axis option in the activity-classification dimension, narrower than Track 6's seven axes but already packaged for workshops, with a 1-3 scoring scale that maps to three outcomes (automate now / AI assistant / not ready). The middle "AI assistant" outcome is a useful bridge to review-and-autonomy: a mid score means "human in the loop", not "no". The existing [Stripe Kai note](departmentofproduct-stripe-kai.md) describes the canvas as "frequency vs volume"; this post shows the axes are safety, volume and verifiability.

## Themes
- work-structure-spectrum: classifies tasks by three properties rather than a single structured/unstructured axis; applies equally to internal process automation and user-facing features ("How to identify" and "new product features" sections).
- risk-sloped-review: safety (cost if wrong) is an explicit axis, colour-coded green/amber/red on the canvas; the author argues a high-risk, low-frequency task (drafting legal terms) fails even when verifiable because safety and volume outweigh verifiability.
- evals-autonomy-trust: verifiability as the main criterion, attributed to an OpenAI co-founder's argument (in context, about programming) that the more verifiable a task, the more automatable it is.
- human-review-gates: the five-step automation anatomy includes a logic step that routes the model's output (auto-approve vs send to a human).
- agent-factory-sdlc: opening examples of automation across the product loop: Figma Make Connectors reading a PRD from Notion or Linear to build a prototype ("context-driven prototyping", attributed to Linear's COO); Claude Code plus Playwright MCP doing SEO audits; Walmart's "Trend to Product" agent said to cut the design-to-store cycle by up to 18 weeks (all second-hand).

## Key points
- **Anatomy of an AI automation:** trigger; collect and prepare data; model interprets (classify, predict, generate, summarise); logic decides the path (e.g. auto-approve vs human); actions run in downstream tools and the result becomes data for next time. Can be deterministic or agentic.
- **The three dimensions:** Safety (cost of a wrong output; high to low risk), Volume (how often it happens), Verifiability (how easily you can tell it is right). Ideal candidates: low risk, high volume, easily verifiable.
- **Worked examples:** bug severity categorisation scores well on all three; drafting terms and conditions scores badly. For a consumer business (Instacart is the example), auto-building a cart from past orders is a good candidate; negotiating supplier pricing is not.
- **Canvas:** Y axis verifiability, X axis volume, colour for safety. The point is to surface discussion about awkward cases (verifiable and frequent but high risk).
- **Prompts provided (described, not reproduced):** one scores a task 1-3 on each axis with rubric anchors (e.g. "objective / some metrics / subjective" for verifiability), totals out of 9 and recommends one of three tiers; a second runs a pre-mortem with a success story and a failure post-mortem six months out, then asks for success factors, risks, mitigations, a go/no-go and 30-day warning metrics. The author suggests uploading engagement data so the model can judge volume.
- **Mini app:** a public Claude artifact for scoring and ranking opportunities in a workshop; a downloadable template and slide deck for subscribers. Not opened.
- **Closing stance:** pick "crisp, clear, value-adding" opportunities rather than all-in automation; cites Benedict Evans that it is too early to know how this plays out.

## Notable quotes
- "Just because you can automate something doesn't mean you should" (introduction)

## Could not verify
- The OpenAI co-founder is not named in the text; the verifiability argument matches Andrej Karpathy's public posts, but the embedded quote was an image and was not read.
- Walmart's 18-week figure and the Figma Make Connectors behaviour are relayed from press and a Figma demo; not checked.
- The framework is the author's; there is no evidence it predicts which automations succeed.
- Paywalled text summarised, not reproduced.
