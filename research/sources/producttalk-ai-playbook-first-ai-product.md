---
title: "Building My First AI Product: 6 Lessons from My 90-Day Deep Dive"
source_url: https://www.producttalk.org/ai-playbook/
author: Teresa Torres
publisher: Product Talk
published: 2025-08-20
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
filed_note: re-check 2026-10-24
themes: [research-synthesis-agents, ai-synthesis-hallucination-risk, human-judgment-pm-jobs, non-engineer-builders]
relevance: high
---

## Relevance to the project
A first-hand, quantified test of AI interview synthesis against an expert (Torres), plus a candid build log of a discovery-focused AI product (her Interview Coach) by a non-engineer. The synthesis comparison is the best per-transcript evidence in the set for how much J1 synthesis can be handed to a model: useful additions, many misses. The evals routine is a concrete model for how a PM-agent product keeps quality from drifting.

## Themes
- **research-synthesis-agents**: Across two transcripts, Claude found 18 and 20 opportunities against her 15 and 19, surfaced 8 and 2 she missed, and missed 7 of hers each time (section 2).
- **ai-synthesis-hallucination-risk**: ChatGPT invented interview quotes and ignored guidelines; Claude also produced solutions labelled as opportunities and duplicates (section 2).
- **human-judgment-pm-jobs**: Her conclusion is that AI helps synthesis but cannot replace her doing it (section 2).
- **non-engineer-builders**: She built from browser projects to Replit to Zapier to AWS Step Functions, then evals in Jupyter and Claude Code (sections 3-4).

## Key points
- Problem choice (section 1): started from her own opportunity solution tree; two AI-shaped problems were slow interview snapshots and judging interview quality.
- Synthesis test (section 2): 15 transcripts run; detailed comparison reported for two. Rubric-based interview evaluation worked well in Claude, poorly in ChatGPT. Beta users were recent alumni, not current students.
- Architecture (section 3): chat UI caused rate-limit-draining follow-ups; one prompt across four rubric dimensions misapplied criteria; she split into a deterministic workflow of separate AI tasks delivered by email.
- Evals (section 4): golden datasets, code assertions, LLM-as-judge built from error analysis; one error (reusing excerpts across sections) fell from 81% of transcripts to 3% after a prompt change.
- Continuous investment (section 5): review about 60 traces every week or two, update the failure taxonomy, recalibrate judges against human labels.
- Data responsibility (section 6): students submitted real customer interviews with sensitive data; she relaunched with consent, 90-day retention, deletion, then partnered with Vistaly (SOC 2; she is an advisor) for compliance.

## Notable quotes
- "Claude is not ready to replace me when it comes to synthesizing interviews." (section 2)
- "Evals are how you know if your product is any good." (section 4)

## Could not verify
- Only two of the 15 transcript comparisons are reported in numbers. Vistaly is a commercial partner she advises; the article is not sponsored but the relationship is disclosed. Read via a fetch tool's rendering.
