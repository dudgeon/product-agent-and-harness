---
title: "Uber's CISO on building an insider threat program for AI"
source_url: https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-10-13
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [agent-control-plane, agent-failure-modes, enterprise-admin-controls, org-context-grounding]
relevance: medium
---

## Relevance to the project
Uber's CISO argues agents need the same insider-threat programme companies run for staff: real-time telemetry in the harness, intervention before a risky tool call, and a cycle of discovering new agent behaviours and feeding safeguards back. Uber's stack (an LLM gateway as perimeter, its open-sourced AI Detection and Response tool in the harnesses, plus Anthropic's Enterprise Frontier Safeguards classifier output) is a concrete customer-owned control-plane layering. Bears on governance-control-plane and harness-layering; a customer Q&A on Anthropic's site, no incident or detection figures.

## Themes
- agent-control-plane: three layers: LLM gateway "which builds a perimeter and controls how AI is used", open-source ADR gathering real-time telemetry and acting in deployed agent harnesses, and Anthropic's classifier output as another data source (answer on fitting Enterprise Frontier Safeguards).
- agent-failure-modes: concern is accidental misuse and models "directed to act outside the constraints we expect"; "constraints create new behaviors" so detection must keep finding new ones.
- enterprise-admin-controls: Enterprise Frontier Safeguards described as safeguards in place while Uber's data stays inaccessible to Anthropic without permission, with Uber controlling the response after a trigger.
- org-context-grounding: threat modelling improved as models gather context themselves from code, design docs and Jira history; vision of one agent per service that knows its threat model and talks to other services' agents.

## Key points
- Priority one: real-time detection and intervention as close as possible to the person typing in a harness ("You probably don't want to do that").
- Priority two: watch trends in model behaviour, often with LLM help, and build safeguards back into the real-time platform.
- Argument for monitoring: employees already accept insider-threat retention and monitoring; frontier models introduce the same risk.
- Uber scale stated: 40 million trips and delivery orders a day.
- Limits: no specifics on what ADR detects, false-positive rates, or how intervention is surfaced; Enterprise Frontier Safeguards is an Anthropic product promoted on the page.

## Notable quotes
- "That insider threat program for models is going to be essential to rolling these systems out safely and securely." (Philip Martin, CISO, Uber)

## Could not verify
- The ADR open-source repository and the Enterprise Frontier Safeguards page were linked but not read.
