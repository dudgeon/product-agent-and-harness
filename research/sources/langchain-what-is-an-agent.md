---
title: What is an AI agent?
source_url: https://www.langchain.com/blog/what-is-an-agent
author: Jess Ou (LangChain)
publisher: LangChain blog
published: 2026-07-31
retrieved: 2026-10-25
type: article
evidence: vendor-claim
filed_by: research-skill-rigidity-spectrum
themes: [work-structure-spectrum, agent-frameworks, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
LangChain's definition puts control flow at the centre: an agent is "a system that uses a large language model to decide the control flow of an application", and "Autonomy is a spectrum" with three separate things the model may control (each step's output, the next step, and which steps exist). Those three are a finer split of candidate dimension 1, and the post ties more model control to more required tooling (observability, evals, permissions).

## Themes
- work-structure-spectrum: progression from hand-written code, single LLM call, chain, router, state machine, to an autonomous agent that builds its own tools.
- evals-autonomy-trust: "the more control the model owns", the more robust observability, evals, memory, permissions and safe execution must be.

## Key points
- Definition (LangChain's own): the agent begins when the model chooses the next step, not only text.
- Three control questions: who decides the step's output, the next step, the available steps.
- Most production systems sit between fixed workflow and full autonomy.

## Could not verify
- The levels chart is an image; who decides each question at each level was not readable. Earlier Harrison Chase versions of this framing (2024) were not re-fetched.
