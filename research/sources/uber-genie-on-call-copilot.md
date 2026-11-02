---
title: "Genie: Uber's Gen AI On-Call Copilot"
source_url: https://www.uber.com/en-US/blog/genie-ubers-gen-ai-on-call-copilot/
author: Nicholas Marcott, Eduards Sidorovics, Paarth Chothani (Uber)
publisher: Uber Engineering Blog
published: 2024-10-10
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [agent-as-service-many-surfaces, org-context-grounding, context-trust-mechanisms, human-relay-removed, status-update-agents, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
Genie is Uber's first Slack-resident engineering assistant (launched September 2023): a RAG copilot added to support channels, answering from the wiki and internal Stack Overflow with cited sources and escalation to the human on-call. It is the obvious predecessor in shape to Cortana's channel-bound personas, but no Uber source found says Cortana grew out of Genie; Cortana's own origin story (Pragmatic Engineer, Oct 2026) is one engineer's assistant from December 2025. It also shows an early lesson the context graph later generalised: answer quality is capped by source-document quality.

## Themes
- agent-as-service-many-surfaces: Slack client calls a Knowledge Service; replies carry buttons to ask a follow-up, mark resolved, or reach human on-call; future plans to bring it into Michelangelo UI and IDEs (Serving, Future).
- human-relay-removed: Slack support channels got ~45,000 questions a month; Genie answers before the on-call engineer has to (Problem).
- org-context-grounding: answers only from retrieved "sub-contexts" with source URLs; sources pre-curated to those "widely available to most Uber engineers"; embeddings scoped to channels tied to specific wiki spaces (Architecture, Security).
- context-trust-mechanisms: each knowledge-base document scored by an LLM judge with suggestions to improve it, because poor documentation caps answer quality (Evaluation).
- evals-autonomy-trust: four feedback labels (Resolved, Helpful, Not Helpful, Not Relevant) to Kafka and Hive; LLM-as-judge eval pipeline in the Michelangelo UI (Feedback, Evaluation).
- status-update-agents: Q&A on internal help channels as an agent job; 154 channels.

## Key points
- Results (as of Oct 2024): 154 Slack channels, 70,000+ questions answered, 48.9% helpfulness rate, ~13,000 engineering hours saved since Sept 2023.
- Stack: Spark ETL from wiki and Stack Overflow APIs; LangChain chunking; OpenAI embeddings; Sia (in-house vector DB); cost tracked by a UUID passed through the Michelangelo Gateway into an audit log.
- RAG chosen over fine-tuning for time to market.

## Notable quotes
- "Since its launch in September of 2023, Genie has expanded its presence to 154 Slack channels"
- "Accurate information retrieval depends on the clarity and accuracy of the source documents."

## Could not verify
- Whether Cortana replaced, absorbed or runs beside Genie. No Uber blog post names Cortana at all (blog swept 2023 to 2026-11-02); secondary write-ups treat them as separate.
- Per-channel onboarding/configuration of Genie is not described.
