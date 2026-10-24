---
title: "Tobi Lütke: AI Agents, Better Decisions, and the Future of Work"
source_url: https://fs.blog/knowledge-project-podcast/tobi-lutke-3/
author: Shane Parrish (host), Tobi Lütke (guest)
publisher: The Knowledge Project (Farnam Street); also on YouTube (https://www.youtube.com/watch?v=G9P9D9hptq8)
published: 2026-09-10
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [org-learning-loop, memory-architecture, legible-org-for-agents, human-review-gates, agent-failure-modes, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
Shopify's CEO describes River at length, about four months after "Learning on the Shop floor" and "Under the River". It is the only first-party source that explains River's **memory design** (per-person and per-channel memory, plus nightly "dreaming" that rewrites skill files), its **persona** (a named, sarcastic "she" with a "soul" markdown file), and a **much larger PR-share claim** ("up to about 50%" of PRs come out of chat conversations). He also names the main failure mode, "slop grenades", meaning unread agent PRs pushed onto reviewers. It bears on the teardown's questions about memory and skills, the public-by-default rationale, metric inflation, and review load.

## Themes
- `org-learning-loop`: River was forced into open channels to recreate office "osmosis learning" and make "reflexive reaching for AI" observable. Tobi calls it "a late choice in the process, but one of my favorite calls" (transcript, River section, after 07:18).
- `memory-architecture`: "dreaming": "periodically at night or in off hours" River reviews the day's conversations, asks what went well or badly with its skills, and writes the results to "text files, skill files and instructions". At session start, memory "dedicated to the person that's asked the question" is injected, plus "the channel memory".
- `legible-org-for-agents`: where River struggles, that is treated as a tooling discovery. The example: River repeatedly failed to pick the right subset of unit tests, so Shopify trained an ML model to predict which tests to run and told River to "just run this thing", which saved about "30 minutes at the end of every task". "If you make your system easy for agents to be legible, it also ends up being easier for people."
- `human-review-gates` / `agent-failure-modes`: "slop grenades": "You just tell the AI to go nuts. It makes a pull request. You just say, 'Yep, that's good.' You don't really read it, and now it has to be reviewed by your colleagues." Long AI-inflated emails are the same failure.
- `vendor-claims-vs-independent-evidence`: "up to about 50% of pull requests ... are created now not by engineers ... but out of conversations in our common company chat". This is a founder estimate with no method given, and it conflicts with Shopify's published "one in eight merged PRs coauthored" (May 2026).

## Key points
- **Scale and surface (River section):** River "lives in Slack". "We have 7,000 people there ... There's 10,000 different channels." You invite River to a channel, and "River has access to all the code, all the systems, all the tools. It's all sandboxed and secure." She can answer normal questions about the company or propose PRs.
- **PR share:** "a very large percentage, I want to say it's probably up to about 50% of pull requests in Shopify ... are created now ... out of conversations in our common company chat." Note the wording: *created out of conversations*, not "authored by River" or "merged". Secondary outlets (Podcast Alpha, Shopifreaks, Taskade) turned this into "River writes half of Shopify's PRs".
- **Persona:** River has "a real name", "a profile picture", is "prompted to be allowed to be somewhat sarcastic", and may say a request is "stupid", including to Tobi. This is a deliberate bet against "neutered" assistants ("risk the Sydney scenario, but take a lot of upside"). Agents "have a soul in form of a markdown file."
- **Public-by-default rationale:** Shopify is remote-first, and the office's "osmosis learning" (mixed junior/senior pods) was lost. Forcing River into open channels makes AI use "really, really easy for people to observe". A typical pattern: a long human conversation, then "Hey River, can you summarize this, create a ticket ... make a diagram ... research papers ... create a prototype", and "an hour or so later, that is there."
- **Memory (contradiction inside the interview):** he first says "she has memories by channel", then "it is a memory system per person". The detailed explanation reconciles the two: per-person crystallised memory is injected at session start, "and then depending on which channel it's in, it's also the channel memory."
- **Dreaming:** an off-hours self-reflection job over the day's conversations and skill use, producing edited skill files and instructions, not weights ("the result is text files").
- **Surfaces beyond Slack:** "River has the ability, although not really utilized, to join Google Meets. You can send an invitation, and River will show up." There is talk of a 3D avatar.
- **Model choice (Tobi's personal agent, not River):** his "AI chief of staff" (an OpenClaw-style system) runs a "council" of sub-agents across Grok, ChatGPT, Opus and Kimi, with a randomised synthesiser and a final read by "Fable". It costs "15, 20 bucks on tokens" per run. He randomises his main chat model daily ("GPT Sol or ... Opus 5"; adds Meta "Muse 1.2"). Nothing is said about which models River uses.
- **Lineage:** credits Peter Steinberger's OpenClaw with discovering "stable patterns by which we can now build Rivers and build Sidekicks", meaning file systems and soul files that agents are "pre-trained to use".
- **Not covered:** identity and credentials, private-channel or HR handling, cost per session, evals.

## Notable quotes
- "This is a AI called River. She has a real name. She has a profile picture."
- "You invite River, you tell River something, and River has access to all the code, all the systems, all the tools. It's all sandboxed and secure."
- "So this was a late choice in the process, but one of my favorite calls."
- "Machines can't take responsibility." (said in the context of human-in-the-loop decision surfaces)
- "Internally, we have come to call these things that people are lobbing 'slop grenades' at each other."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- The members-only extended cut was not available, and the transcript carries a "may contain errors" warning.
- "Up to about 50%" has no definition (opened, merged or coauthored PRs?), no date range and no denominator. It cannot be reconciled with the May 2026 "1 in 8 merged PRs coauthored" figure from these sources alone.
- "Access to all the code, all the systems, all the tools": the permission model behind it (whose identity River acts as) is not described.
