---
title: "AI SLOPCAST #9: Lehrwerkstatt and Agent's Dead Silence"
source_url: https://oleg.guru/aislopcast/en/009-shopify-river-lehrwerkstatt/
author: Oleg Chirukhin
publisher: AI Slopcast (oleg.guru); video in Russian on YouTube and VK
published: 2026-05-14
retrieved: 2026-10-24
type: podcast
evidence: independent
filed_by: competitive-teardown-shopify-river
themes: [org-learning-loop, vendor-claims-vs-independent-evidence, agent-failure-modes, human-review-gates]
relevance: medium
---

## Relevance to the project
The most pointed **critique** found. The author accepts the learning mechanism but names three omissions: curated metrics with no negatives, **surveillance built into the architecture** (every gap and mistake broadcast and archived, "a treasure trove" for HR), and a **junior pipeline** problem (no junior hiring plus public learning only for existing staff). It bears directly on the teardown's "chilling effects / privacy of public-by-default" question. The numbers come second-hand from ZenML, and there are some factual slips (see below).

## Themes
- `org-learning-loop`: three mechanisms behind the no-DM rule: incidental learning by scrolling (short horizon), diffusion of technique as folklore (medium), and collective debugging that accumulates fixes (long; "almost certainly what accounts for that climbing merge rate"). Agents make visibility cheap because "the agent doesn't mind being watched".
- `vendor-claims-vs-independent-evidence`: "the numbers are, almost certainly, a curated selection". Missing: bugs in River code, incidents, tech debt, and **review load on senior engineers**.
- `agent-failure-modes`: thinking out loud with an agent is "a deeply intimate part of engineering work". With River "it is broadcast to the entire company — and archived for years ... You can track who gets stuck on easy problems." "Companies that copy River's design will inherit ... the most fine-grained employee-surveillance system anyone has ever built."
- `human-review-gates`: "if River is opening one out of every eight, somebody is reading them ... the senior engineers, whose time is not free."

## Key points
- A 77% merge rate is "roughly, the bar for a junior engineer". Tobi's (reported) plan to hold headcount at 7,500–8,000 for five years means "no new juniors", so "where ... is the next cohort of senior engineers going to come from?" The "context engineer" role is open only to the already experienced.
- Small teams: publish every agent action to one team channel; "No private Cursor sessions. No off-the-books Claude Code."
- Prediction: open-source communities will set agent best practice because publicness is native to them.
- Cites a 20VC appearance (early May 2026) and BigGo Finance for the headcount and "context engineer" remarks. Neither was verified.

## Notable quotes
- "The capability is wired into the architecture, and the precedent has been set."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- **Factual slips:** it calls Tobi's piece a "personal blog" post (it was an X article). It says the merge-rate gain had "No new prompt", whereas Tobi attributes it to people writing skills and instructions. It says River "opens roughly one out of every eight pull requests merged", repeating the ZenML conflation.
- The 7,500–8,000 headcount plan (via BigGo Finance / 20VC) was not checked.
