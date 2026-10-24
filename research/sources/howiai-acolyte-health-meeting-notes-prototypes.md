---
title: "How to turn meeting notes into prototypes that your sales team can immediately demo to customers | Anjan Panneer Selvam (Acolyte Health)"
source_url: https://www.lennysnewsletter.com/p/how-to-turn-meeting-notes-into-prototypes
author: Claire Vo (host), Anjan Panneer Selvam (CPTO, Acolyte Health)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-09-01
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [spec-becomes-prototype-and-evals, prd-agents, spec-edge-case-review, artifact-standardization, pm-persona-role-expansion, human-judgment-pm-jobs, prototyping-agents-limits]
relevance: medium
---

## Relevance to the project
A startup CPTO shows an end-to-end intent-shaping chain built from consumer tools: a wearable transcript of a stakeholder meeting, ChatGPT to normalise the brain dump into a prototyping prompt, Lovable for a working prototype, Perplexity deep research plus a "devil's advocate" pass for market analysis, Gamma for slides, then ChatPRD as a "gate" with a team-agreed PRD template before engineering. The prototypes then go into a "living product library" that sales and success demo to customers. It bears on intent-shaping-and-spec (prototype as the alignment object, PRD as the final gate to engineering) and artifact-and-project-structure (a shared library of prototypes as a managed artifact set). It is a stitched chain of separate tools with copy-paste between them, which illustrates the meta-harness gap. Acolyte is a health company, but nothing in the episode addresses regulation, PHI or compliance.

## Themes
- spec-becomes-prototype-and-evals: a journey-builder that once took "17, 18 page documents", sketches and Figma is prototyped in under 30 minutes; "nobody wants to spend time reading 17 pages ... they would rather see" (13:12-14:43). Host: for complex rule builders, the prototype as "source of truth" makes requirement testing natural (17:26).
- prd-agents: ChatPRD used "almost like a gate": it asks "have you thought through this?" before generating; template is a team-agreed "CPTO stack" PRD; it separated "future ideas and enhancements" from scope (25:25-26:58). Note ChatPRD is the host's product.
- spec-edge-case-review: AI "is bullish about everything", so he always adds a follow-up asking it to "play devil's advocate"; "there are more features that AI has helped me say no to" (23:38).
- artifact-standardization: the team PRD template was agreed with engineering ("a particular type of PRD that my team likes") so AI output lands in a known shape (25:25); the demo library uses pages close to the platform's design language (29:30).
- pm-persona-role-expansion: CPTO as one role because AI blurs product and technology (3:19); he builds demos without engineering ("I can almost do my entire product function without worrying the engineering team", 31:00).
- human-judgment-pm-jobs: host notes the PM still turns "I want a journey builder" into precise language ("single page canvas, user facing tool, map out personalized workflows") that AI can act on (6:27).
- prototyping-agents-limits: "at least three demos that did not work" for each one shown; iterating inside Lovable/v0 burned time, so he moved the thinking upstream to ChatGPT (45:51). Prototypes are explicitly not production code (41:55).

## Key points
- **Chain** (4:47-26:58): meeting (Limitless pendant transcript) -> ChatGPT normalises into a structured Lovable/v0 prompt -> Lovable prototype, adding details incrementally (e.g. naming React Flow) -> Perplexity deep research for market analysis, cut "to three minutes", plus devil's-advocate follow-up -> Gamma slides -> ChatPRD validation and PRD -> engineering. Each step is a manual paste; he hopes for integrations (28:41).
- **Living product library** (29:30-31:00): deployed microsites of prototypes that anyone, including the CEO, can demo safely because they are bounded ("no page ... is suddenly going to give a 404"). One stakeholder meeting led to a customer demo 30 minutes later. A shared, persistent artifact set that outlives the meeting.
- **Breaking deadlocks with engineering** (36:15-38:57): with no mobile developer, he built an Expo app in Rork to show feasibility, framed as "it's possible, what would production need?", not "I built it". Host flags the cultural risk of PMs showing CEOs and sales prototypes.
- **Prediction** (43:35): companies will spend more time up front with these tools and be "very sure of what they want" before building; support teams can train on prototypes before launch.

## Notable quotes
- "I use chat PRD almost like a gate ... Are you sure you want to do this? Are you sure you have everything?" (25:25)
- "The goal here is not to say something is easy. It's more so to are we all aligned and can be more fast." (41:55)

## Could not verify
- Transcript and show notes read in full. Timings ("30 minutes to two days ... into production", "three minutes" research) are the speaker's own; the demos were pre-built.
- Company size is not stated (host calls it "relatively small"). No evidence on whether prototypes shown to customers created commitments or how healthcare compliance is handled.
- The ChatPRD segment is the host promoting her own product with a guest who is a user; treat its benefits as vendor-adjacent.
