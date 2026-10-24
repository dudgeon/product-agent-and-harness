---
title: "How this PM streamlines 60k-page FDA submissions and saves millions with Claude, Streamlit, and clever AI workflows | Prerna Kaul"
source_url: https://www.lennysnewsletter.com/p/how-this-pm-streamlines-fda-submissions-prerna-kaul
author: Claire Vo (host), Prerna Kaul (product leader; formerly Gen AI PM at Moderna, now Panasonic Well)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-07-14
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [risk-review-as-classification, human-review-gates, cost-control-routing, evals-autonomy-trust, non-engineer-builders, prd-agents, artifact-standardization, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
One of the few sources in the library from a regulated life-sciences setting: a former Gen AI PM at Moderna demos the prototype of a tool that drafts parts of a ~60,000-page biologics licence submission (the FDA Common Technical Document) from clinical trial data, with automated PHI detection and redaction and per-operation cost tracing. It bears on the film's regulated-enterprise lead case in two ways: it shows the "structured, strictly formatted output plus compliance gate" shape of regulated documentation work, and it shows how weakly the impact claims are supported (synthetic data, "millions" saved without a figure). Also useful: cost transparency as a tactic for winning internal approval, a PRD-to-Jira add-on for PMs, and a product leader's view that PMs own the safety eval list and rollback trigger. The demo is a single-user prototype, not an agent harness.

## Themes
- risk-review-as-classification: PHI redaction framed as entity recognition over unstructured clinical notes; Claude picked a medical named-entity-recognition model and showed confidence scores (10:28, 16:03-17:34). Previously "months of effort to get right" per drug with bespoke ML, a scaling problem when Moderna aimed at ~50 drugs in trials and 15 to market in three to five years (17:49).
- artifact-standardization: the submission is "XML based" with fixed modules, so strict structured output was the first hard requirement (7:26); Claude looked up the CTD format and chose the module (15:05); export to text and the required XML (20:25).
- human-review-gates: the medical-writer step today is weeks of back-and-forth per module with ~20 specialists aligning stakeholders; she suggests shared AI projects as a better collaboration surface than comments on a shared document (18:53). The tool drafts; the episode does not describe who signs off.
- cost-control-routing: "trace and cost analysis" shows cost per operation, duration and token cost by step; transparency answers the stakeholder objection "this is going to be high cost. Can we find a simpler way that's not AI-based?" (22:14). Host's example: knowing PHI redaction costs, say, 15 cents per patient lets the organisation compare alternatives (23:32).
- evals-autonomy-trust: product leaders should supply "my 100 things I want to know that the model does well on when it comes to safety", monitor online as well as offline, and trigger rollback when it fails (41:16-42:49); "Compliance and privacy comes first" in regulated industries (41:16).
- non-engineer-builders: Streamlit UIs make her tools usable by non-technical colleagues, "a really, really big unlock" (12:18).
- prd-agents: she built a Google Docs add-on that converts PRDs into Jira format so PMs "don't necessarily like having to write requirements twice" (12:18). Her build process started with a PM-style pitch to Claude (problem, why it matters, sponsor, expected savings), which returned setup instructions, code and even a demo narrative (5:54-8:47).
- vendor-claims-vs-independent-evidence: impact is asserted, not measured: "We did. We did" save cost (24:58); the show notes' "4 to 6 months and 20 specialists, to just minutes" is not demonstrated in the episode, which runs on synthetic data.

## Key points
- Workflow demoed: generate synthetic participants and clinical notes, detect and redact PHI, generate a CTD synopsis with participant counts, ages and statistics, download as text or XML, view per-operation costs (14:04-24:25).
- She says the thinking was applied to Moderna's individualised cancer vaccine and the combined COVID/RSV vaccine submissions (24:58); the solution dates from 2023 and evolved over time (3:45).
- Chosen vendor for "safety and alignment" reputation (7:26). Model choice on ethics benchmarks is called a product leader's "priority zero" (41:16).
- Second workflow: a Claude project as a stakeholder "influence and communication coach", prompt built with the Anthropic console prompt generator, knowledge from public-domain books on persuasion, outputs a situation analysis, per-stakeholder pre-meetings, a minute-by-minute meeting plan and back-pocket questions (26:43-37:17).

## Notable quotes
- "Compliance and privacy comes first. But it's a bit more than privacy and compliance. It's the ethics overall" (41:16)
- "this is going to be high cost. Can we find a simpler way that's not AI-based?" (22:14, the objection cost transparency answers)

## Could not verify
- Full transcript read. The guest calls the document a "biological license agreement"; the FDA term is Biologics License Application (BLA). The auto-transcript garbles some names.
- No figure for cost or time saved, no accuracy figure for PHI redaction, and no description of human sign-off or validation in production. The "minutes" claim is from the show notes only. The demo used synthetic data.
- The host and guest attribute the project's sponsorship to the company's CEO; not checked.
