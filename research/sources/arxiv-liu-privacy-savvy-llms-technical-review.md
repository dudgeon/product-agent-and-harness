---
title: "How Privacy-Savvy Are Large Language Models? A Case Study on Compliance and Privacy Technical Review"
source_url: https://arxiv.org/abs/2409.02375
author: Yang Liu, Xichou Zhu and others (ByteDance Privacy and Data Protection Office)
publisher: arXiv
published: 2025-02-14
retrieved: 2026-11-06
type: paper
evidence: independent
filed_by: design-requirements-agent
themes: [risk-review-as-classification, elicitation-agent-evidence, launch-readiness-review]
relevance: medium
---

## Relevance to the project
A large platform company's privacy office describes its Privacy Technical Review (PTR), a technical assessment that checks products against privacy rules before and shortly after launch by reviewing requirement documents, technical designs, code and traffic, and measures how well LLMs do three sub-tasks: extracting personal-data types, detecting ten legal key points (storage region, retention, user rights, SDK use and others), and answering questions over agreement text. LLMs were near-perfect at extraction (F1 about 99) and roughly equal to a tuned domain model at key-point detection (about 94 to 95), but weaker on precise question answering. For a requirements agent, this is measured evidence that obligation screening from documents (does this feature touch personal data, retention, cross-border storage) is within reach, while exact answers still need checking.

## Themes
- risk-review-as-classification: key-point detection is binary classification over ten legal aspects; GPT-4 F1 94.8, GPT-4o 94.5, a domain-tuned BERT (ComBERT) 94.0.
- elicitation-agent-evidence: personal-information extraction F1: GPT-4o 99.6, Gemini 1.5 Flash 99.8, versus ComBERT 91.8; extractive QA F1 about 68 to 74 with low exact-match (GPT-4 EM 40.5 versus ComBERT 54.9).
- launch-readiness-review: PTR covers the whole development lifecycle and includes "gray" and full launch stages; requirement documents are the first input reviewed.

## Key points
- The authors conclude "significant gaps persist" in LLMs' ability to comply with evolving legal standards.
- Datasets are from ComBERT's release (about 8,800 sentences for extraction; about 2,300 QA passages), mostly privacy policies and agreements, not PRDs.

## Could not verify
- Read through WebFetch's model-summarised view of HTML v4; the summary flagged several inconsistencies between the paper's text and tables. No peer-reviewed venue listed; first version September 2024.
