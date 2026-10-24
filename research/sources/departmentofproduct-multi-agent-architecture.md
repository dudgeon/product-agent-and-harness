---
title: Multi Agent Architecture explained
source_url: https://departmentofproduct.substack.com/p/multi-agent-architecture-explained
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-05-19
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [one-job-per-agent, single-agent-many-skills, agent-frameworks, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
A May 2025 primer on multi-agent patterns for product teams: single agent, network, supervisor, hierarchical and custom, with framework pointers (AutoGen, LangGraph, A2A). It is the "many specialised agents" side of the debate written before the counter-arguments filed here ([Cognition, Don't Build Multi-Agents](cognition-dont-build-multi-agents.md), June 2025) and before AutoGen was archived ([AutoGen archive notice](github-microsoft-autogen-archive-notice.md)), so it is mainly useful as a dated snapshot of the vocabulary PMs met. Company examples are second-hand from AWS docs, a WSJ interview and Microsoft's Work Trend Index.

## Themes
- one-job-per-agent: the case for multiple agents is that a single agent "can become overwhelmed with too many tools, too much context"; benefits claimed are modularity, specialisation and control ("What exactly is multi agent AI architecture?").
- single-agent-many-skills: the post treats the single agent as fine for simple cases only. That conflicts with the later filed view that one agent with many skills, with context kept in one thread, is often better ([Cognition](cognition-dont-build-multi-agents.md)).
- agent-frameworks: AutoGen, LangGraph and A2A named as the technologies; Amazon Bedrock's console toggle to make one agent a supervisor ("Supervisor"; "Terminology and technologies").
- vendor-claims-vs-independent-evidence: Accenture says 10-15% of its clients use multi-agent systems, expected to pass 30% in 18-25 months, and that it runs 15 agents under 3 "super agents" (WSJ, second-hand).

## Key points
- Network pattern: no central controller; resilient but resource-heavy and hard to supervise. Illustrated with a study where an AI "conversational surrogate" relayed ideas between groups of 200+ people.
- Supervisor pattern: one agent assigns, monitors and aggregates; Microsoft's three-phase picture (assistant, humans overseeing agents, agent teams with occasional check-ins); Bedrock example of a content agent plus an engagement-predictor agent under a supervisor.
- Hierarchical pattern: supervisors of supervisors once one supervisor becomes the bottleneck; AWS drug-discovery example with molecular, literature and repositioning teams working in parallel.
- Custom: mixes of the above; closes by saying product teams will need to govern what agents do and how much oversight they get (pointing to Salesforce guidance).

## Could not verify
- The architecture diagrams were images not visible in the text copy. None of the cited sources were opened.
- Paywalled; summarised, not reproduced.
