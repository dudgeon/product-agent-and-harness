---
title: "Building AI product sense, part 2"
source_url: https://www.lennysnewsletter.com/p/building-ai-product-sense-part-2
author: Marily Nika (guest author; former AI PM at Google and Meta, AI PM educator), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2026-02-10
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [ai-synthesis-hallucination-risk, agent-failure-modes, evals-autonomy-trust, human-judgment-pm-jobs, cost-control-routing, pm-job-stable-methods-change]
relevance: medium
---

## Relevance to the project
A guest post on "AI product sense" for PMs building AI features. Its worked examples are PM jobs we'd want an agent to do (extracting decisions from a Slack thread, summarising a PRD for a VP, grouping 40 bugs into a roadmap), and it shows where models fail on them: "when confronted with mess, they confidently invent structure", inventing a roadmap, assigning the wrong owners and turning offhand comments into commitments. The proposed fixes (ask instead of guess, refuse to invent owners, offer scope choices on long context, light output structure) are guardrails a PM harness would need for synthesis and status jobs. It also gives a quality-bar vocabulary (acceptable, delight and do-not-ship bars plus a cost envelope) usable for pm-agent-evaluation, and notes Meta's new "Product Sense with AI" PM interview. Evidence is the author's practice; she sells courses.

## Themes
- ai-synthesis-hallucination-risk: asked to extract "strategic product decisions" from a messy seven-line Slack thread, the model "confidently hallucinated a roadmap, assigned the wrong owners, and turned offhand comments into commitments" (Ritual 1). A startup's Slack-summary feature began assigning owners for action items "when no one had actually agreed to anything yet" (Design guardrails).
- agent-failure-modes: "semantic fragility" on ambiguous asks such as "Summarize this PRD for the VP of Product" (over-summarising, latching on one detail, dropping caveats, wrong audience) (Ritual 2); running the same "top 5 decisions" prompt repeatedly yields different decisions each time (Ritual 4).
- evals-autonomy-trust: minimum viable quality (MVQ) with three bars (acceptable, delight, do-not-ship) set by strategic context; delight measured by behaviour (fewer retries and "No, I meant..." corrections); rule of thumb: 8-9 of 10 without retry feels magical, 1 in 5 needing retry erodes trust (Define MVQ). "If a user saw the worst version of these 10 outputs, would they still trust the product?" (Ritual 4).
- human-judgment-pm-jobs / pm-job-stable-methods-change: Meta added a "Product Sense with AI" interview, "the first major change to its PM loop in over five years", judging how candidates notice when the model is guessing and decide under uncertainty, not prompting skill (intro).
- cost-control-routing: estimate a cost envelope early; worked example of AI meeting notes at about $0.02 per 30-minute transcript, $0.40 per user-month average, $2 for heavy users, $0.25-0.30 with caching and a smaller model for low-stakes meetings (Estimating the cost envelope).

## Key points
- Weekly ritual under 15 minutes: ask the model to do something obviously wrong, something ambiguous, something unexpectedly hard; compare bad and good outputs and turn the gap into a product requirement (Map the failure modes).
- Four guardrail patterns: ask when unsure; offer a choice when context is too long; say so when there is no structure ("I didn't see any decisions here"); add light structure when outputs vary (Ritual 4).
- The fix for the owner-assignment bug was a one-line system-prompt rule, "not a different underlying model" (Design guardrails).
- "AI product sense" means different things to different PMs (model knowledge, evaluation, prompting, safety, cost); the author defines it as translating probabilistic behaviour into a reliable experience (conclusion).

## Notable quotes
- "When confronted with mess, they confidently invent structure" (Ritual 1).
- "It looks authoritative, clean, structured. And it's completely wrong" (Ritual 1).

## Could not verify
- Post read in full; several tables (ambiguous prompts, five strategic context factors, guardrail examples) were images or did not survive text extraction.
- Examples are single runs on unnamed models (NotebookLM named for one); no failure rates measured. Cost figures are illustrative.
- Meta interview change is stated by the author without a link in the text.
