---
title: "Agentic Commerce Protocol and building the Economic Infrastructure for AI — with Emily Glassberg Sands, Head of Data & AI at Stripe"
source_url: https://www.latent.space/p/stripe
author: Alessio Fanelli and swyx (hosts), Emily Glassberg Sands (Stripe)
publisher: Latent Space
published: 2025-10-30
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [build-vs-buy, skills-marketplace, org-learning-loop, org-context-grounding, metrics-review-agents, outcome-measurement-gap, cost-control-routing, human-judgment-pm-jobs, harness-portability]
relevance: medium
---

## Relevance to the project
The pre-Kai baseline from Stripe's head of Data & AI (Oct 2025): GoLLM (internal ChatGPT-style UI) with shareable "presets" (hundreds overnight), then LLM Proxy for production use, a LibreChat-based replacement wired to **Toolshed** (central MCP server that teams like Salesforce extend themselves), and **Hubert**, a text-to-SQL assistant on the Hubble data catalog (~900 weekly users) whose worst failure was data discovery. It shows Stripe's sequential build-then-buy stance and its honest "I have a really hard time understanding impact". Bears on build-vs-buy (loop-source), capability-distribution-trust, org-context-grounding and pm-agent-evaluation.

## Themes
- build-vs-buy: "not an either or ... some of that and is sequential": built GoLLM when no enterprise-safe provider existed, later replaced it with open-source LibreChat; warns against hill-climbing a home-grown tool out of sunk cost (01:11:40). "Spotlight program": RFPs to buy (evals RFP, 2 dozen applicants, Braintrust chosen).
- skills-marketplace / org-learning-loop: GoLLM "presets" = prompt saving and sharing; "hundreds of presets ... overnight" (00:49:45).
- harness-portability: Toolshed is managed centrally but "anybody can ... the Salesforce team can add Salesforce ... we don't want to be blocked on some central team" (01:00:43).
- org-context-grounding / metrics-review-agents: Hubert did worst at data discovery; fix was deprecating low-quality tables, owner-written docs for canonical datasets ("brute-forcing it with humans"), and org-position persona context to bias table choice (01:05:11). Hubert deliberately targeted at technical domain users who can validate answers.
- outcome-measurement-gap: "I have a really hard time understanding impact. Like I don't quite know what statistic to look at"; coding-model cost "pretty non-trivial"; argues for 2-3 year ROI not in-year (00:53-01:04).
- human-judgment-pm-jobs: "LLM was used in the generation of this content. Please cite the LLM" as a non-negotiable norm; prefers a prototype to a doc (00:57-00:59).

## Key points
- 8,500 Stripes/day used LLM tools (of ~10,000); 65-70% of engineers used AI coding assistants daily.
- A pan-European local payment method integration built with an LLM in two weeks (vs ~two months): the precursor of the payment-method factory.
- Experimental Projects team: "embedded projects" (EP people plus the owning team) more often reach "escape velocity".

## Could not verify
- Publication year inferred (page shows "Oct 30"; content is the ACP launch period, autumn 2025). The transcript is the publisher's; small transcription errors likely.
