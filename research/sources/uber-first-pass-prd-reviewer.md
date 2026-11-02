---
title: "Lessons from Building a First-Pass AI PRD Reviewer at Uber"
source_url: https://www.uber.com/us/en/blog/first-pass-prd/
author: Lakshmi Ashok (Product Lead, Uber)
publisher: Uber Engineering Blog
published: 2026-05-12
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [prd-agents, agent-led-intent-shaping, human-review-gates, org-context-grounding, risk-sloped-review, outcome-measurement-gap]
relevance: high
---

## Relevance to the project
Uber's PRD Evaluator is a first-party example of an agent that shapes intent before human review: it gathers the PRD's linked docs, decks, meeting notes and prior experiments, classifies the change to set review depth, and returns a launch-readiness scorecard with a "start here" fix and write-ready replacement text. It sits before Uber's checkpoint process rather than replacing it. It is the closest Uber evidence on PRD/spec tooling, and pairs with the PRD/ERD tool Medisetty describes on the Pragmatic Engineer podcast. The post gives no evaluation numbers and does not name the platform it runs on.

## Themes
- prd-agents: scorecard with Ready / Ready with Caveats / Not Ready, per-dimension Looks Good / Needs Review, and for each gap: what is missing, replacement text, and evidence from linked docs or past experiments (Scorecard).
- agent-led-intent-shaping: dimensions are Opportunity and Hypothesis, Product Scope, User Experience and Impact, Metric and Data Rigor; actions such as "define a baseline, name a target, add a guardrail, narrow the first release" (Rubric).
- risk-sloped-review: PRDs are classified first: lighter (UX parity), moderate (incremental workflow or tooling migration), full (net-new), full with specialised scrutiny (policy, pricing, marketplace) (Step 2).
- org-context-grounding: builds a knowledge base around the PRD via AI search over linked and related artifacts, plus preloaded Uber principles, metric definitions and jobs to be done; "Context matters as much as language quality" (Step 1, Lessons).
- human-review-gates: "The evaluator doesn't aim to make final manual approval decisions or replace domain experts"; success is better human review conversations (Lessons).
- outcome-measurement-gap: only "dozens of PMs" in early use; no accuracy, time-saved or quality metrics reported.

## Key points
- Goal: raise the quality of what enters Uber's checkpoint and approval process, not change the process.
- Lessons: frameworks tied to real decision criteria beat generic critique; a few hard boundaries stop the tool calling a PRD ready when fundamentals are missing; prioritisation (what to fix first) is part of the product; flagging everything helps nobody.
- Figure 2 refers to "Six Dimension Scores" while the text names four dimensions; the other two are not given.

## Notable quotes
- "We didn't want a generic writing tool that simply rewarded polished prose."
- "A review tool that flags everything as important isn't helping."
- "Hard boundaries make output more honest."

## Could not verify
- Where it runs (Cortana persona, skill, doc add-on, standalone) and which models: not stated.
- Whether it is the same as the "PRD and ERD tool" mentioned on the Pragmatic Engineer podcast (chapter 47:54): not stated.
