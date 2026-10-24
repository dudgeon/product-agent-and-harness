---
title: Running an AI-native engineering org
source_url: https://claude.com/resources/articles/running-an-ai-native-engineering-org
author: Anthropic (unnamed engineering leader on the Claude Code team)
publisher: Claude (claude.com/resources)
published: 2026-06-03
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [pm-persona-role-expansion, spec-becomes-prototype-and-evals, risk-sloped-review, outcome-measurement-gap, agent-factory-sdlc]
relevance: high
---

## Relevance to the project
A Claude Code engineering leader describes which team norms broke once agentic coding became the default and what replaced them: just-in-time planning via prototypes and internal users instead of six-month roadmaps and design docs, "ask Claude, not the author" for context, Claude reviewing style, bugs and tests with humans kept for legal, security and product taste, and blurred roles where PMs code. This is first-party org-design evidence for the project's AI-native SDLC story and for where human review should sit. It is one team inside the vendor, with unusually strong dogfooding incentives, and gives no numbers beyond qualitative direction (onboarding faster, every commit Claude-assisted).

## Themes
- pm-persona-role-expansion: "Our PMs code a lot now"; engineers take on content and design; hiring indexes on creative builders with product sense and deep systems experts, less on raw throughput (Team makeup).
- spec-becomes-prototype-and-evals: planning shifted "away from design docs toward discussions in PRs or prototypes"; few product reviews; prototype, put internal users on it, act on feedback (Planning).
- risk-sloped-review: Claude handles style, linting, bugs and tests; humans review where expertise matters (legal risk tolerance, trust boundaries and security, PM/designer product sense and taste); the balance is to be re-evaluated per model (Code review).
- outcome-measurement-gap: suggested metrics are onboarding ramp time, PR cycle time and Claude-assisted commits, with the warning "don't confuse throughput with success" (How to know your new processes are sticking).
- agent-factory-sdlc: bottlenecks moved from writing code to verification, code review and security; a morning customer-feedback summary now runs automatically (intro; Context gathering).

## Key points
- **Before/after table:** planning (six-month roadmaps to JIT planning); context gathering (find the author to ask Claude first, then ask whether it can be automated); code review (humans review everything to Claude for style/bugs/tests, humans for domain expertise); team makeup (fixed roles to blurred roles).
- **Roadmap decay.** A six-month roadmap was out of date by month three because of the pace of change.
- **"Ask Claude, not the author."** Since all PRs are Claude-assisted, "who made this change?" no longer suffices; decompose the real need (regression owner, expert, decision context) and ask Claude.
- **Rollout model.** Three non-negotiable principles (relentless dogfooding by everyone including cross-functional partners, a flat team with managers starting as ICs, explicit permission to kill processes); everything else left to pods (triage, planning rituals, standups, which workflows get "Claudified" first).
- **Signals.** Engineers ship real code in their first week; the author has not seen a non-Claude-assisted commit in four months; CI and build systems may struggle with the extra code volume.
- **Starting move.** Pick the "noisiest" workflow and ask whether it still serves its purpose, then automate or drop it (anecdote of cancelling a status meeting).
- **Limits:** no quantitative results, no failure stories, no detail on how PM/designer review of taste is actually triggered; the author is unnamed on the page.

## Notable quotes
- "Verification, code review, and security took their place." (intro, on the new bottlenecks)
- "Don't confuse throughput with success." (How to know your new processes are sticking)

## Could not verify
- Author's name (no byline on the page; first-person account by a Claude Code engineering leader).
