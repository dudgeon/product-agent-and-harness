---
title: Context Engineering for AI Agents Explained - a simple overview of the basics
source_url: https://departmentofproduct.substack.com/p/context-engineering-for-ai-agents
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-07-07
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [harness-over-model, org-context-grounding, memory-architecture]
relevance: low
---

## Relevance to the project
An early, basic explainer written the week "context engineering" took off (Lütke and Karpathy endorsements), covering four context types (memory, instructions, retrieval, tools), Cognition's two principles for sharing context between agents, observability with LangSmith, and a calendar-agent example. It supports the project's framing that agent failures are often context failures rather than model failures, but adds nothing beyond the first-party sources already filed ([Anthropic on context engineering](anthropic-effective-context-engineering.md), [Manus lessons](manus-context-engineering-lessons.md), [Cognition: Don't Build Multi-Agents](cognition-dont-build-multi-agents.md)). Downgraded from the triage guess of high: useful as the plain-language version for a PM audience, not as evidence.

## Themes
- harness-over-model: calendar example; when agents fail at such tasks, "they aren't necessarily model failures, but context failures"; relays Cursor's CEO attributing agent failures partly to missing context (second-hand).
- org-context-grounding: the richer calendar reply depends on contacts (who matters), calendar (fully booked), past email/Slack threads (tone) and send tools.
- memory-architecture: short-term vs long-term memory as one context type, with OpenAI, Gemini and AutoGen adding memory at the time.

## Key points
- **Definition:** building a system that gives the model all the relevant information and tools, in the right format, for the task; distinguished from prompt engineering, which crafts one instruction. Context engineering is dynamic per request.
- **Four context types:** memory, instructions/prompts, RAG, tools.
- **Multi-agent context (from Cognition):** every subagent should see the full context and decision history; actions carry implicit decisions, so agents acting without awareness of each other conflict. Compressed shared history is the recommended pattern.
- **Observability:** tools like LangSmith log exactly what context went into each call, which lets teams see how context choices change responses.
- **Further reading:** LangChain's "rise of context engineering", Lance Martin's context-engineering post, Phil Schmid.

## Notable quotes
- "Context engineering is the delicate art and science of filling the context window with just the right information for the next step" (Karpathy, as quoted)

## Could not verify
- Several diagrams (context types, prompt vs context comparison, feature examples) were images not in the text.
