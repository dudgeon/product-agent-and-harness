---
title: "Small Models, Massive Wins: Shopify's New AI Formula (Beyond the Pilot podcast)"
source_url: https://venturebeat.com/video/small-models-massive-wins-shopifys-new-ai-formula
author: Sam Witteveen (host), Farhan Thawar (guest, VP & Head of Engineering, Shopify)
publisher: VentureBeat, Beyond the Pilot podcast
published: unknown (companion article dated 2026-06-24)
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [cost-control-routing, harness-portability, org-learning-loop, identity-delegation, remote-agent-invocation, non-engineer-builders]
relevance: medium
---

## Relevance to the project
Shopify's head of engineering on the platform underneath all AI use (the LLM proxy, circuit breakers, the usage dashboard, distillation), with several direct statements about River: what it can see, that it **switches between models**, that it is **public-only**, and that it is **pull-only** ("you can talk to it, but it doesn't talk to you"). It is the best first-party source found on cost and model choice around River, and it gives the reason Shopify dropped its token leaderboard.

## Themes
- `cost-control-routing`: an internal LLM proxy buys tokens "in bulk from all the providers", reports usage and fails over automatically. "We don't have limits on our tokens, but we have circuit breakers in place": a ping on long-running, token-heavy tasks asks whether the spend was intended, and some users find forgotten background tasks this way.
- `harness-portability`: "once I buy the tokens, I don't care what harness you wanna use" (Claude Code, Codex, Cursor). "Our own agentic platform, like River, which again, switches between models."
- `org-learning-loop`: when an engineer corrects River in a thread, "any future query to River learns and will never have that mistake again". Other people helping River reframe problems was "an unintended consequence ... Putting River in public was intended."
- `identity-delegation`: "River can see Slack messages, it can query into our data warehouse, it can see our product management system." River works only in public, so "you can't go into a private channel and say, 'Hey, River, help me build.'"
- `remote-agent-invocation`: "River is an agent in that you can talk to it, but it doesn't talk to you." No proactive outreach.
- `non-engineer-builders`: Quick (transcribed "Qwik") hosts dragged-and-dropped HTML/JS. A "secure version of Qwik" can restrict readers ("I only want to have four people read this"). Anything going to merchants still needs a human engineer to take responsibility.

## Key points
- Describes River as "our agentic substrate across the company". The page calls it "River, Shopify's internal agentic substrate" and "a public-only Slack agent that queries their data warehouse, reads their PM system".
- River's token spend and River-submitted PRs are both "going up". No figures given.
- **Leaderboard removed:** "We don't have a leaderboard anymore. We have a usage dashboard." The aim is to highlight utility, not "who's in the top 10". "Any person in the company can see their spend in AI." When spend is high, leaders ask "What are you actually trying to do here?" This contrasts with the 2025 First Round piece, which described a Cursor-token leaderboard as "a cool proxy for value".
- **Distillation:** a Universal Distillation Platform turns frontier "teacher" models into smaller task models (2x–30x cheaper/faster in reported cases). "AI replaces tasks, not jobs."

## Notable quotes
- "River only works in public, which means you can't go into a private channel and say, 'Hey, River, help me build.'"
- "River is an agent in that you can talk to it, but it doesn't talk to you."
- "We don't have a leaderboard anymore. We have a usage dashboard."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- Episode date (no date on the page; the companion article is 2026-06-24), duration and timestamps.
- Whether "River ... switches between models" means automatic routing per turn or proxy failover only.
- The exact scope of "can see Slack messages": all public messages, or only the thread it is in.
