---
title: A practical guide to building agents (OpenAI), read via secondary summary
source_url: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
author: OpenAI (summary by Jeremy Weaver, ibl.ai)
publisher: OpenAI; summary at https://ibl.ai/blog/openai-a-practical-guide-to-building-agents.md
published: 2025-04
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [work-structure-spectrum, single-agent-many-skills, human-review-gates, agent-frameworks]
relevance: medium
---

## Relevance to the project
OpenAI's counterpart to Anthropic's guide. Its use-case test (messy decision logic, unstructured data, rule-based automation breaking on edge cases) is a usable "when does a task need an agent at all" screen, and its single-agent-first advice supports `single-agent-many-skills`. Read only through a third-party summary dated 2025-06-16 because the PDF could not be text-extracted.

## Themes
- work-structure-spectrum: build an agent where rules are hard to maintain, unstructured data must be parsed, or rule-based automation struggles with edge cases; otherwise use a single LLM call or conventional automation (per summary).
- single-agent-many-skills: start with a single agent in a loop; go multi-agent (manager + specialists, or peer handoffs) only when a single agent becomes a bottleneck (per summary).
- human-review-gates: high-risk actions go to manual review; humans can approve or roll back critical steps; guardrails in two layers (classifiers, tool safeguards) (per summary).

## Key points
- Publication month (April 2025) comes from a search result; the summary page is dated 2025-06-16.
- LangChain's Harrison Chase criticised this guide (see langchain note); that is vendor-vs-vendor, not independent evidence.

## Could not verify
- Exact wording of OpenAI's criteria, any failure-threshold triggers for human intervention, and the original date: the PDF returned binary only and no pypdf/pdftotext was available. Treat all points as secondary.
