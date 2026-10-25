---
title: "MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework"
source_url: https://arxiv.org/abs/2308.00352
author: Sirui Hong, Mingchen Zhuge, Jiaqi Chen, ... Chenglin Wu, Jürgen Schmidhuber
publisher: arXiv (cs.AI, cs.MA)
published: 2023-08-01
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [process-artifacts-as-coordination, prd-agents, artifact-standardization]
relevance: high
---

## Relevance to the project
MetaGPT encodes a software company's standard operating procedure into agent roles that hand each other structured documents (PRD, system design, task list) instead of chatting. Its role ablation is one of the few quantified pieces of evidence that structured intermediate artifacts in a multi-agent pipeline improve output, and its PM role writing a PRD is a direct precedent for PM agents.

## Themes
- process-artifacts-as-coordination: agents publish structured documents to a shared message pool and subscribe only to what their role needs (method).
- prd-agents: the Product Manager agent writes a PRD with user stories and competitive analysis; Architect writes file lists, data structures, interfaces, sequence diagrams (method).
- artifact-standardization: authors argue free chat between LLMs causes unproductive exchanges and cascading hallucination, which standardised handoffs reduce (introduction; argued, not isolated experimentally).

## Key points
- Roles: Product Manager, Architect, Project Manager, Engineer, QA Engineer; sequential SOP workflow.
- Executable feedback: Engineer runs code and unit tests, debugs up to 3 retries; adds 4.2 points on HumanEval and 5.4 on MBPP.
- Pass@1: 85.9% HumanEval, 87.7% MBPP (as reported, v7).
- SoftwareDev: executability 3.75 vs ChatDev 2.25; human revisions 0.83 vs 2.5.
- Role ablation: Engineer alone executability 1.0 and about 10 revisions; full team 4.0 and about 2.5 revisions; cost $0.915 vs $1.385 per project.
- Limits: benchmarks are code; "executability" is a 1-4 rating; the ablation confounds role count with document handoffs (my reading).

## Could not verify
- Venue (commonly cited as ICLR 2024) not shown on the arXiv page.
