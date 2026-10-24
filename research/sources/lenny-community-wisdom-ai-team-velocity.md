---
title: "Community Wisdom: Using AI to accelerate a team's velocity, interviewing backend engineers, tips for conducting willingness-to-pay interviews, when to pivot, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-using-ai-to-accelerate
author: Lenny's Newsletter community (digest edited by Kiyani)
publisher: Lenny's Newsletter
published: 2025-07-05
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [scoped-governance-containers, shared-persistent-sessions, org-context-grounding, tacit-knowledge-capture, spec-becomes-prototype-and-evals, prd-agents, enablement-by-product]
relevance: medium
---

## Relevance to the project
Only thread 1 ("Using AI to accelerate a team's velocity") bears on the project. It catches a mid-2025 snapshot of how PMs moved from single-player AI deliverables (PRDs, tickets, call summaries) to shared team spaces: one PM creates a Claude Project per larger feature initiative, loads PRDs, competitive work and user-session transcripts as its knowledge base, and shares it with CS, PMM and marketing, who then produce their own deliverables from it and upload them back. That is an early, organic version of the per-initiative shared context container our concepts propose (artifact-and-project-structure, session-persistence-sharing). Another member uses AI to extract stakeholder context before an offsite, a small tacit-knowledge-capture pattern. Community anecdotes.

## Themes
- scoped-governance-containers / shared-persistent-sessions: "creating a project per larger feature initiative, getting the knowledge base and instructions right, and sharing the project to folks in CS, PMM, Marketing, etc. really helps with things like handoffs and distributed knowledge" (thread 1, PM on a Claude team account).
- enablement-by-product: the same PM built "a project that's sole purpose is to help others make projects": it interviews the creator about objectives, outlines knowledge-base docs, and generates the instructions file; outcome "TBD" (thread 1). Buy-in came from "seeing concrete project examples for larger features" (thread 1). A former Smartsheet PM reports PMM "barfed on using anything and wanted to do it the old way" when pushed to use Gemini (thread 1).
- org-context-grounding: "It's a 'garbage in, garbage out' thing, but once you get comfortable with how to build and maintain the right context, I've found these shared team projects to be tremendously valuable" (thread 1).
- tacit-knowledge-capture: AI "context extraction" from stakeholders before an offsite: async structured prompts (what should this accomplish, who else cares, how would we know we're progressing, what processes should come out, which constraints matter), then AI finds "patterns and contradictions across all the responses"; a 3-day offsite took a day and a half (thread 1).
- spec-becomes-prototype-and-evals: a PM's PRDs became "much simpler, focusing only on the problem or the opportunity", then an LLM turns the PRD into a v0 prompt; multiple solutions are generated and the team discusses "on top of the actual screens rather than only the ideas" (thread 1).
- prd-agents: a custom GPT for user stories speeds ticket writing; another PM uses AI to improve document quality "rather than the speed of writing" for strategy docs and PRDs (thread 1).

## Key points
- The original question asks how to "ladder this up to the org level" and whether product ops teams use automation to speed innovation; replies stay at team level, with no org-level example (thread 1).
- LLM-generated Mermaid and Excalidraw diagrams replace manual box-dragging (thread 1).
- Thread 3 (designer delegation) has a tangential point: "have a definition of good" so critique is not personal; not filed as evidence.

## Could not verify
- Read the full digest; filed thread 1 only. Threads on pivoting, backend interviews, willingness-to-pay and designer delegation are out of scope.
- The offsite time saving is one member's pilot, self-reported.
