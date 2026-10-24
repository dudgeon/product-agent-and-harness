---
title: "Money Forward builds an AI-native engineering organization with Claude Code"
source_url: https://claude.com/customers/money-forward
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [agent-factory-sdlc, enablement-by-product, vendor-claims-vs-independent-evidence, human-review-gates]
relevance: medium
---

## Relevance to the project
A Japanese fintech (17M+ users, 400,000 businesses) describes a trial-led, bottom-up Claude Code rollout run by an internal productivity research group (MEPAR) and an ambition to extend Claude Code from engineering into product discovery, testing and SRE, which is a regulated-industry example of the agent-across-the-SDLC path. It is mainly engineering, not PM, evidence. All figures (80% adoption, 7 hours/week saved from an early-adopter survey, 90%+ code acceptance, API endpoint work 2 days to 5 hours) are the customer's unaudited claims on an Anthropic page. One claim cuts against review practice elsewhere: high acceptance is framed as engineers integrating output "without extensive review".

## Themes
- agent-factory-sdlc: plan to extend Claude Code "from product discovery and test generation to SRE operations"; CTO's vision of Claude across planning, implementation, testing and operations ("Looking ahead").
- enablement-by-product: small trials with a public channel any employee could follow; 200+ engineers outside the trial asked for access; the trial channel became the official one ("Choosing Claude through rigorous evaluation").
- vendor-claims-vs-independent-evidence: 7 hours/week saved comes from "an internal survey for early adopters", not measurement; customer case on Anthropic's site.
- human-review-gates: Claude Code PR review against an internal style-guide template lets developers fix issues before human review; separately, "code acceptance rate exceeds 90%" is presented as trust "to integrate it without extensive review" ("The outcome").

## Key points
- **Selection process:** MEPAR (Money Forward Engineering Productivity AI Research) ran side-by-side trials with small groups and only rolled out tools with strong feedback; PR-review integration built from an internal template based on the style guide.
- **Why it won (customer's account):** earlier tools understood one project in one IDE; Claude Code navigated multiple languages and repositories; CLI works across WebStorm, JetBrains, RubyMine and VS Code.
- **Rollout:** organisation-wide in July, training workshop with Anthropic in August (year not stated).
- **Uses:** full features, large refactors, PR review automation, a `/onboarding` command that sets up frontend, backend and end-to-end repos (onboarding a week to a day, per a staff engineer), Sherlock (incident investigation by searching logs and past cases), Lumos (agent that fixes Kubernetes issues and opens a PR within five minutes).
- **Role shift claim:** on the Public API initiative Claude Code generated about 80% of implementation code and developers "shifted from writing code to directing it".
- **Solo build:** one staff engineer built the company's MCP server in three months with Claude Code as "my only colleague".
- **Limits:** no quality, incident or defect data; adoption and time-saved figures are self-reported; PM involvement is only an aspiration ("product discovery").

## Notable quotes
- "Developer productivity is therefore a business strategy..." (Tran Ba Vinh Son, Group Company CTO and Manager of MEPAR)

## Could not verify
- Publication date and rollout year; how "code acceptance rate" is defined.
