---
title: "How this Yelp AI PM works backward from \"golden conversations\" to create high-quality prototypes using Claude Artifacts and Magic Patterns | Priya Badger"
source_url: https://www.lennysnewsletter.com/p/how-this-yelp-ai-pm-works-backward
author: Claire Vo (host), Priya Badger (product manager, Yelp)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-10-20
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [spec-becomes-prototype-and-evals, prototyping-agents-limits, human-judgment-pm-jobs, prd-agents]
relevance: medium
---

## Relevance to the project
A concrete first-party intent-shaping workflow for an AI feature: Yelp's "standard LLM-powered playbook" starts with "golden conversations" (example dialogues) instead of a PRD or wireframe, uses them as the seed of evals, then has Claude derive a system prompt and an Artifact prototype that calls the model live. It is evidence for the "spec becomes prototype plus evals" pattern from an ordinary large consumer company, and shows the example artifact (not prose) as the shared object across PM, design and engineering. Bears on intent-shaping-and-spec and pm-agent-evaluation. Single-PM demo; the live demo partly failed.

## Themes
- spec-becomes-prototype-and-evals: "a lot of people talk about like evals are the new PRD ... this is like the very early step of getting to the eval process" (13:48); golden conversations reveal criteria (did it recognise the image, is it concise, does it flow), later formalised as a rubric. Host: "you really are using example conversations and just reference designs as your PRD here" (17:13).
- prototyping-agents-limits: Claude Artifacts can call the model without API keys, so the prototype exercises real responses; a reply that reads fine in a doc "feels really long" in a mobile chat bubble (17:45-19:19). The Magic Patterns variant demo failed with a React version error (30:42); long sessions "go haywire" as context fills, so fork or summarise into a new chat (39:11).
- human-judgment-pm-jobs: "the core of the PM job and the earliest part of the workflow hasn't really changed": understanding the user problem and prioritising; AI helps in solution exploration after that (24:34).
- prd-agents: Claude translates refined example conversations into system instructions, which she reads to learn how examples become prompts (17:45).

## Key points
- **Workflow** (6:17-19:19): (1) prompt Claude for a full sample conversation with output format constraints ("assistant:/user:" labels); (2) upload real photos across many service categories (cracked porch, oven error code, wasp nest, bathroom) to generate a batch of conversations, because patterns show up across many examples; (3) give feedback once ("be more opinionated", "don't ask about budget") and have all conversations rewritten; (4) ask for an Artifact app with a chat UI, a system prompt derived from the conversations, photo analysis and screenshots of the current Yelp Assistant as visual reference.
- **Team practice** (8:51, 21:37): golden conversations are "part of our standard LLM-powered playbook at Yelp"; design, product and engineering write conversations together and critique each other's. The prototype still goes through the "usual design and engineering processes".
- **UI exploration** (21:37-29:00): Magic Patterns rebuilds the existing assistant from screenshots; "Inspiration mode" generates four differentiated variants; forks run variants separately. Replaces "really hacky Figma mock-ups"; designers use Magic Patterns or Figma Make and trade links.
- **Before or without a PRD** (27:05): prototyping tools help "even earlier", when the problem is understood but the solution isn't.
- Side use: a Claude Project that turns a week of an internal Slack channel export into a newsletter in a fixed format, with names replaced for privacy (34:00).

## Notable quotes
- "We start with golden conversations. What's the experience that you're trying to drive?" (8:51)
- "Sometimes we come in and we feel like we need to have a whole PRD before we can start prototyping." (27:05)

## Could not verify
- Transcript read in full (auto-transcription with errors, e.g. "alum powered playbook" for LLM-powered). Show notes read in full.
- How golden conversations become production evals at Yelp, and how widely the playbook is used, is not described.
