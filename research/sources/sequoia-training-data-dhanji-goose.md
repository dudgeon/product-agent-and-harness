---
title: "Block CTO Dhanji Prasanna: Building the AI-First Enterprise with Goose, their Open Source Agent"
source_url: https://www.sequoiacap.com/podcast/training-data-dhanji-prasanna/
author: Sonya Huang and Roelof Botha (hosts) with Dhanji Prasanna (Block CTO)
publisher: Sequoia Capital (Training Data podcast)
published: 2025-09-30
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-block-product-practices
themes: [leadership-permission-mandate, non-engineer-builders, outcome-measurement-gap, build-vs-buy, ai-flattened-org]
relevance: medium
---

## Relevance to the project
Block's CTO explains how the AI programme started (a "manifesto" email to Dorsey asking for central AI investment), why Block unwound its GM/business-unit structure into functions, and the single metric Block tracked: "manual hours saved by goose", targeting 25% by end of 2025. It complements the paywalled Lenny's episode ([lenny-podcast-block-dhanji-goose](lenny-podcast-block-dhanji-goose.md)) with a free transcript. PM work is not discussed; the relevance is the operating-model and measurement story that preceded the 2026 cut. Goose internals and governance are left to sibling notes.

## Themes
- leadership-permission-mandate: before becoming CTO, Prasanna emailed Dorsey that Block must "invest in AI, and we need to do it centrally", saying Block was "well behind the eight ball"; Dorsey flew to Sydney for two days to discuss it ("Who's driving the AI agenda at Block?").
- ai-flattened-org (reorg): start was about eight funded "special projects" with two to five engineers each; then "progressively we started to unwind our GM structure", which he says was holding back value. He was Cash App head of engineering (about 10 to 200+ engineers) during the earlier move from functional to GM structure; Botha frames both moves as fitting their era.
- outcome-measurement-gap: the metric "is very simply manual hours saved by goose", tracked weekly from zero toward a 25% year-end target; "engineers report eight to ten hours per week" (self-report) ("Goal metric for AI impact"). Code share: most engaged engineers generate "about 30 to 40 percent" of code in legacy codebases; AI-first teams are "pretty much all entirely vibe coded".
- non-engineer-builders: "We never expected sort of our sales guy or our financial person to be writing software dashboards for themselves." Hence two goose UIs (CLI for engineers, desktop for others).
- build-vs-buy: Block tried "Here's every single AI tool there is" with "mixed success"; goose is used "by the majority of the company" alongside other licensed tools, and must compete with them.

## Key points
- Block treats its own capabilities (payments, bitcoin, issue tracking, pull requests) as building blocks with an agent layer on top; said to be an insight from about end of 2024.
- goose builds goose: "every PR that's open is written by goose"; aim is for each release to rewrite itself from scratch.
- Remote-first lets Block hire in Sydney, Sweden and elsewhere; trade-off is velocity and serendipity.
- Block trains small language models for customer service and risk; does not train LLMs. Prefers open-weight models (Qwen named).
- Design and engineering kept "on a pedestal" since the first Square reader.

## Notable quotes
- "we need to invest in AI, and we need to do it centrally" (Prasanna, on the email to Dorsey)
- "progressively we started to unwind our GM structure" (Prasanna)

## Could not verify
- Release date 2025-09-30 from podcast directories (Podbay/Amazon listing); the Sequoia page shows no date. Transcript untimestamped; references are by chapter heading.
- Hours-saved and code-share figures are self-reported with no method; whether the 25% target was hit by end of 2025 is not reported here.
