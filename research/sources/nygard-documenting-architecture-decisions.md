---
title: Documenting Architecture Decisions
source_url: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
author: Michael Nygard
publisher: Cognitect blog
published: 2011-11-15
retrieved: 2026-10-25
type: article
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [decision-rationale-records, process-artifacts-as-coordination]
relevance: high
---

## Relevance to the project
The origin of the ADR: a short, numbered, immutable record of one decision kept in the repo. It is the canonical process artifact for keeping rationale across rotating contributors, which is the multi-party problem agents now inherit. Its supersede-never-edit rule is what recent agent-practice posts rediscover.

## Themes
- decision-rationale-records: format is title, context, decision, status, consequences; statuses proposed, accepted, deprecated, superseded (body).
- process-artifacts-as-coordination: written so newcomers neither blindly accept nor blindly reverse past decisions (body, problem statement).

## Key points
- Problem: people joining later cannot see why a choice was made, so they accept it blindly (stagnation) or reverse it blindly (breakage).
- Large specs go stale and are unread; small modular records are more likely to be maintained.
- Context in neutral language; decision in active voice ("We will..."); consequences list all effects, good and bad.
- Numbers are sequential and never reused; a reversed decision stays, marked superseded.
- Stored in the repo at doc/arch/adr-NNN.md in lightweight markup.
- Experience: used since August on several projects with six to ten developers rotating through; all said the context helped (anecdote, one author, no measures).

## Notable quotes
- Reversed decisions: "we will keep the old one around, but mark it as superseded".
