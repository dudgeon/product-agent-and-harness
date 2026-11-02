---
title: "Scaling AI in Legal: Building Uber's Redlining Agent"
source_url: https://www.uber.com/us/en/blog/building-ubers-redlining-agent/
author: Austin Greco, Meghana Somasundara, Frank Tenente (Uber)
publisher: Uber Engineering Blog
published: 2026-10-08
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [human-review-gates, deterministic-scaffold-model-nodes, skill-improvement-loops, tacit-knowledge-capture, agent-as-service-many-surfaces]
relevance: medium
---

## Relevance to the project
Uber Legal's Redlining Agent is a non-engineering agent built into Word (where lawyers work) rather than into a shared assistant, with every suggestion accepted, rejected or modified by a lawyer, and lawyer feedback stored as retrieval examples. It shows Uber's non-engineering agents being built as standalone apps on the GenAI Gateway rather than as Cortana personas, and names a move toward agent harnesses (Claude Code, OpenCode) with skills as the next step.

## Themes
- human-review-gates: lawyers decide every suggestion before it reaches the counterparty (Summary).
- deterministic-scaffold-model-nodes: a deterministic rules engine is the hard guardrail; the feedback loop handles negotiable nuance (Iteration 4).
- skill-improvement-loops: lawyer decisions, edited text and comments become retrieval examples, with time decay (365-day half-life) (Iteration 2).
- tacit-knowledge-capture: record the lawyer's reasoning and final edits, not just the decision; SMEs own prompt content that shapes tone (Lessons).
- agent-as-service-many-surfaces: "Lawyers live in Word, so asking them to copy-paste between tools would kill adoption."

## Key points
- Built early 2024 to 2025; React task pane in Word, Python LangGraph back end, OpenSearch vector stores for rules and feedback, Redis for session state; models via GenAI Gateway.
- Claimed results: 20%+ reduction in average contract review time; 91% accuracy on AI decisions; LLM-as-judge for document quality and rule adherence.
- Future: agentic harnesses with skills, legal ontologies, knowledge graphs.

## Notable quotes
- "Lawyers live in Word, so asking them to copy-paste between tools would kill adoption."

## Could not verify
- Cortana, Slack and the MCP Gateway are not part of the design; how "91% accuracy" is measured is not detailed.
