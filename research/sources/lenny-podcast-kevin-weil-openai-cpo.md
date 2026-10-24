---
title: "OpenAI's CPO on how AI changes must-have skills, moats, coding, startup playbooks, more | Kevin Weil (CPO at OpenAI, ex-Instagram, Twitter)"
source_url: https://www.lennysnewsletter.com/p/kevin-weil-open-ai
author: Lenny Rachitsky (host), Kevin Weil (CPO, OpenAI)
publisher: Lenny's Podcast
published: 2025-04-10
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [spec-becomes-prototype-and-evals, evals-autonomy-trust, pm-job-stable-methods-change, pm-persona-role-expansion, human-judgment-pm-jobs, one-job-per-agent, cost-control-routing, human-review-gates, org-context-grounding]
relevance: medium
---

## Relevance to the project
An early (April 2025) first-party account from a frontier-lab CPO of how AI changes product work: evals as a core PM skill and as the thing that decides what product you can build, vibe-coded prototypes replacing Figma, a deliberately PM-light org, and "ensembles" of specialised model calls as the internal architecture. It bears on intent-shaping-and-spec (evals and prototypes as the handoff), pm-agent-evaluation and work-structure (one job per model call). It is also an honest admission that even at OpenAI the PM day job was still "recognisable" in 2025, which dates the "everything has changed" framing. Downgraded from high to medium: much of the episode is consumer AI, Libra and parenting; the PM-relevant content is about 20 minutes.

## Themes
- spec-becomes-prototype-and-evals: for Deep Research, evals were designed alongside the product from "hero use cases" (question plus amazing answer), then the model was hill-climbed on them (21:00-22:35); "instead of showing stuff in Figma, we should be showing prototypes that people are vibe coding over the course of 30 minutes" (54:30).
- evals-autonomy-trust: whether a model is right 60%, 95% or 99.5% of the time decides what product you build (17:50, 20:20); AI products are capped by how good the evals are; custom evals measure company-specific fine-tunes (22:48-24:22).
- pm-job-stable-methods-change: "if I were to just teleport my five-year-old self ... into my day job, I would recognize it still" (53:52). Uses so far: ChatGPT for summarising docs, custom GPTs that write product specs, models that help write evals.
- pm-persona-role-expansion: predicts "quasi researcher machine learning engineer types" on every product team because fine-tuning becomes core workflow (57:36); the chief people officer vibe-coded an internal tool in Windsurf (54:50).
- human-judgment-pm-jobs: the PM's distinctive job is to be decisive when ambiguity stalls a group, "make sure that we get a call made" (51:40); high agency and comfort with ambiguity are the hiring bar, which makes junior PMs hard to place (49:54).
- one-job-per-agent: OpenAI internally breaks a problem into specific tasks; "10 different problems ... 20 different model calls", some fine-tuned, some chosen for latency or cost, each with its own prompt (59:29). A company is "an ensemble of models" fine-tuned by experience (1:01:24).
- cost-control-routing: o-series models where reasoning matters and latency doesn't; 4o-mini for quick cheap checks (1:01:24).
- human-review-gates: support automation answers when confident, otherwise drafts an answer for a human, and the human's correction becomes fine-tuning data; 30-40 support staff for 400M+ weekly users (1:01:24).
- org-context-grounding: "most of the world's data, knowledge, process is not public"; models need the equivalent of two weeks' onboarding with company data (22:48).

## Key points
- **Model maximalism** (30:03): don't build much scaffolding around current model limits, because in two months a better model will remove them; build products that "just barely" work at the edge of capability. Exception: errors "you just don't want to make" do get scaffolding. This argues against heavy harness investment, which is a useful counterpoint to the harness-over-model theme.
- **Planning** (26:53): quarterly roadmaps and a year strategy exist but are expected to be thrown out halfway; the value is the moment of reflection and dependency checking ("plans are useless, planning is helpful"). Strongly bottom-up, subject to directional alignment.
- **Reviews** (30:03): product reviews only for the biggest projects; no launch should wait on a review with Weil or Altman. "Iterative deployment": ship and learn in public.
- **Research plus product as one team** (45:49): treating research and product separately makes OpenAI "an API consumer of our own models"; now every product starts as a joint eng-product-design-research team, with evals and fine-tuning as the loop.
- **PM-light org** (48:11): about 25 PMs at the time. "Too many PMs ... will fill the world with decks and ideas versus execution." A PM with slightly too many engineers can't micromanage.
- **Waiting UX** (36:14-40:57): design for 20-second waits the way a human would answer (brief updates, summarised chain of thought rather than all of it), reasoning about AI products by human analogy.
- **Chat as interface** (41:30-43:51): chat is the right baseline because it is unstructured and maximises bandwidth; prescribed UIs suit high-volume narrow cases, but chat stays the catch-all. Bears on the agent-interface dimension.
- **Prompting** (1:27:00): wants prompt engineering to stop mattering; meanwhile, few-shot examples are "poor man's fine-tuning".

## Notable quotes
- "If the model's 60% right on something, you're going to need to build your product totally differently." (20:20)
- "I would recognize it still. And I think we should be in a world ... where I almost wouldn't recognize it." (53:52)
- "Too many PMs causes problems. We'll fill the world with decks and ideas versus execution." (48:11)

## Could not verify
- Transcript read in full (Substack auto-transcription). Numbers (25 PMs, 30-40 support staff, 400M weekly users, 3M API developers) are the speaker's own, spoken as estimates.
- Recorded March 2025; model names and the pace claims (new o-series model every 3-4 months) are dated.
- "GPTs that write product specs" is mentioned in passing; no detail on how specs are produced or reviewed.
