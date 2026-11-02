---
title: "Enhanced Agentic-RAG: What If Chatbots Could Deliver Near-Human Precision?"
source_url: https://www.uber.com/us/en/blog/enhanced-agentic-rag/
author: Arnab Chakraborty, Christopher Settles, Adi Raghavendra (Uber)
publisher: Uber Engineering Blog
published: 2025-05-29
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [org-context-grounding, evals-autonomy-trust, one-job-per-agent, context-trust-mechanisms]
relevance: medium
---

## Relevance to the project
Uber's 2025 rebuild of Genie for security and privacy help channels shows the step from plain RAG to a pipeline of narrow agents (query optimiser, source identifier, post-processor) on LangFx and LangGraph, with an SME-curated golden set and LLM-as-judge scoring. It shows Genie becoming a configurable "Michelangelo Genie framework" for other domain teams, which is the nearest blog evidence of a reusable, per-domain assistant before Cortana's personas. Numbers are relative improvements only.

## Themes
- org-context-grounding: moved policy docs from PDF to Google Docs for structure and built-in access control; LLM converts tables to markdown; summaries, FAQs and keywords added as metadata; access-control metadata indexed (Document processing).
- one-job-per-agent: Query Optimizer, Source Identifier and Post-Processor agents each do one step; vector and BM25 retrieval unioned (Architecture).
- evals-autonomy-trust: 100+ SME-curated golden queries over 40+ policy documents; LLM-as-judge 0-5 scoring; batch evaluation cut experiment turnaround from weeks to minutes (Evaluation).
- context-trust-mechanisms: "Google Docs offer built-in access control, crucial for security-sensitive applications."

## Key points
- Outcome: acceptable answers up a relative 27%, incorrect advice down a relative 60%.
- Components built on Langfx (Uber's LangChain-based service in Michelangelo), orchestration in LangGraph; flow is still sequential.
- Rolled out to multiple security and privacy help channels; components are configurable in the "Michelangelo Genie framework" for other teams.
- Next: multimodal content, chain-of-RAG for multi-hop questions, a self-critique agent, and exposing capabilities as tools agents can select.

## Notable quotes
- "increasing the percentage of acceptable answers by a relative 27% and reducing incorrect advice by a relative 60%"
- "reduced experiment evaluation time from weeks to minutes"

## Could not verify
- Absolute accuracy and channel counts are not given. No mention of Cortana, personas (only "policy details can vary by persona") or skills.
