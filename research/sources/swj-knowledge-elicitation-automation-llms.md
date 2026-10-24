---
title: Investigating Knowledge Elicitation Automation with Large Language Models
source_url: https://www.semantic-web-journal.net/content/investigating-knowledge-elicitation-automation-large-language-models
author: Sherida van den Bent, Romana Pernisch, Stefan Schlobach
publisher: Semantic Web Journal (submission, rejected)
published: 2025-01-05
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [tacit-knowledge-capture, ai-synthesis-hallucination-risk]
relevance: low
---

## Relevance to the project

One of the few head-to-head comparisons of LLM-led versus human-led knowledge elicitation from experts, turning interviews into a structured ontology. Its direction (AI interviews efficient, AI structuring lossy) matches other evidence, but the study was rejected by reviewers for its tiny sample, so treat it as a weak signal only.

## Themes

- **tacit-knowledge-capture**: authors report "AI-led interviews are more time-efficient and structured" but human-led ontology generation performed better; AI ontologies "missed much data" (abstract).
- **ai-synthesis-hallucination-risk**: reviewers note AI ontologies contained hallucinated data and inconsistent structures across runs (reviews 2–3).

## Key points

- ChatGPT v4 ran interviews; pipelines mixed human and AI at interview, transcription and ontology stages; scored with OQuaRE metrics against a hand-built base-truth ontology.
- Conclusion: LLM as interviewer, human knowledge engineer as structurer.
- Reviews (Jun–Oct 2025): one major revision, two rejects; only two human experts; one niche domain (a tabletop role-playing game); single LLM.

## Notable quotes

- Reviewer: "With only two human experts interviewed, how are the results statistically significant?"

## Could not verify

- No time or metric numbers are on the page; the full PDF was not read.
