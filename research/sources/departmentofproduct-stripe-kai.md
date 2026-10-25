---
title: How Stripe Built a new Internal AI Knowledge Platform that their PMs use "all day long"
source_url: https://departmentofproduct.substack.com/p/how-stripe-built-a-new-internal-ai
author: Rich Holmes
publisher: Department of Product (Substack, "DoP Deep", paid)
published: 2026-08-04
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [agent-as-service-many-surfaces, skills-marketplace, task-context-isolation, non-engineer-builders, enablement-by-product, tacit-knowledge-capture, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A PM-audience deep dive on Kai, read in full on 2026-10-24 through a paid subscription. Its facts all come from Stripe's own Kai post (no new Stripe data or interviews), but it adds three things. First, a builder's playbook for PMs: start with one repeatable domain and the surface people already use; separate "where skills get built" from "what runs the agent"; design combination guardrails beyond access permissions; make domain owners the QA. Second, an analogy table of combination guardrails for other domains. Third, a linked list of 15 internal AI tools for non-engineers at peer companies, filed as [its own note](departmentofproduct-internal-ai-tools-for-non-engineers.md). Useful for the strategy's "how to start" framing and for the trust/privacy dimension. It is not evidence of outcomes.

## Themes
- agent-as-service-many-surfaces: the Chrome extension covers "external, browser-based tools that Stripe doesn't control the codebase of, so embedding via API isn't an option, but a browser-level extension still is"; "By making the API the core product and treating every surface as a thin layer on top, Stripe could add new surfaces without touching the underlying logic."
- skills-marketplace: compares Agent Studio to Ramp's Dojo; reports that the earlier 4,000-agent builder's quality "varied wildly", so Stripe "had to build quality signals directly into the agents".
- task-context-isolation: explains why the two-customer rule matters (confidentiality commitments; competitive leakage between rival merchants on the same processor). Proposes analogous combination guardrails: recruiting (two candidates side by side), healthcare (two patients summarised together), HR (performance plus compensation in one output). Argues these must be "enforced at the infrastructure or session level rather than left to individual skill or feature owners".
- enablement-by-product: "Start with one domain and one surface": choose the most repeatable job (the article says Stripe started with sales reps researching accounts before a call) and build in the tool they already use.
- tacit-knowledge-capture: domain owners as QA: "puts the people who know the most about a specific domain in charge of deciding whether or not an agent is performing well".
- vendor-claims-vs-independent-evidence: restates the 83% weekly figure and sales uplift without questioning them. It attributes 83% to the owner-as-QA choice ("As a result"), which is the author's inference.

## Key points
- Six use-case cards, taken from Stripe's post: Sales Research, Data Analysis (5,000+ daily sessions), Finance Modelling, Incident Triage, Compliance Review, and Workflow Automation (Asana + Slack + Jira digests).
- Three-layer architecture diagram: surface-agnostic APIs (web app, Slack, Chrome extension, embedded in internal tools), then AgentStudio, then the execution environment (harness, sandbox, workflow orchestration, access control). Labels: "Shared with product-facing agents", "Built on LangChain deepagents + K8s".
- Agent Studio screenshot (from Stripe): a skills grid with owners and usage counts.
- Sample prompts: (1) score candidate tasks on repeatability, clarity of where people already work, ease of telling whether it works, and value; (2) a guardrail-discovery prompt that looks at *combinations* of individually accessible data, each defined by rule, harm and detection, then ranked by likelihood and severity.
- Links to an "AI Automation Opportunity Canvas" (DoP's own framework: tasks scored on safety, volume and verifiability; see [departmentofproduct-ai-automation-opportunities](departmentofproduct-ai-automation-opportunities.md); corrected 2026-10-24, the earlier note said "frequency vs volume") and to a DoP piece on Ramp's Dojo.

## Notable quotes
- "Unlike code which can often be easily rejected for bad syntax or not following coding conventions, knowledge systems like this have to have human agreed rules baked into them."

## Could not verify
- "Stripe started with sales reps researching accounts" is the author's reading; Stripe's post and podcast say the pilot was with GTM, not specifically account research.
- Retrieved through a paid subscription; the paywalled text is summarised, not reproduced.
