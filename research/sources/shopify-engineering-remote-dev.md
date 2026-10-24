---
title: We gave AI agents a mobile dev environment
source_url: https://shopify.engineering/remote-dev
author: Michael Garfinkle, Mauricio de Meirelles, David Cortes (Shopify)
publisher: Shopify Engineering blog
published: 2026-10-22
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [shared-persistent-sessions, remote-agent-invocation, org-learning-loop, enablement-by-product, non-engineer-builders, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
This is the most recent first-party River post. It shows how Shopify extends River into a new domain (iOS and Android) with a per-session remote environment, a skill, and a feedback-mining classifier, and it reports an adoption metric for that domain: River's share of merged mobile PRs rose from **6% to 61%**. It is useful evidence on how a profile and skill plus an environment extend one agent across domains, on internal marketing as adoption work, and on mining public threads to improve the agent.

## Themes
- `shared-persistent-sessions`: "Each River session gets its own environment". There is a pool of warm Macs, each with an attached Android emulator VM, claimed per session and destroyed afterwards (§What we built; §How we built it).
- `remote-agent-invocation`: tasks start "directly from Slack". There are also automated workflows "that run without anyone having to start a task manually", for example overnight bug pick-up, fix and PR (§Works in the background).
- `org-learning-loop`: "multiplayer by default". They "see where people get stuck, where guidance goes wrong, where access to tools gets rejected." **Jev**, "a really fast, really cheap classifier model", tags all mobile River conversations, rates outcomes, and feeds failures to an LLM that proposes improvements, run "iteratively, using River" (§Building in public).
- `enablement-by-product`: adoption needed "storytelling and internal ads": a River persona character and an AI-generated parody of Apple's "Mac vs PC" ad. Early bad experiences ("This is not for me, I'll go back to coding locally") had to be overcome (§Helping people use it).
- `non-engineer-builders`: "a web developer can fix a bug, a designer can iterate on a UI, and a PM can test a feature, all through Slack". Live Preview streams the simulator or emulator to a Quick site for anyone with the link.
- `evals-autonomy-trust`: "It proves its work": River reproduces a bug, records it, fixes it, then records before/after screenshots or video, and even generates narrated explainer videos.

## Key points
- **Problem:** parallel agentic mobile workflows maxed out laptops (3–4 workflows) and stopped when a lid closed. "River ran on Linux: it could edit Swift, but building and testing the iOS app" needed Macs.
- **Architecture:** a fleet of remote Macs reached over SSH. Android runs on a separate Linux VM with nested virtualization, because macOS lacks it. The warm pool has main checked out, tools installed, apps built and caches warm; idle Macs are periodically refreshed on a staggered rotation. Time from request to a running device went from over 30 minutes to "just a few minutes". The agent keeps its own checkout (local or cloud) and syncs changes to the Mac.
- **Skill, not just infra:** River "always stated that an iOS build cannot run on Linux". A skill taught it to use the remote Mac. Tooling included a CLI wrapping the SSH flags and tmux panes River can watch in real time, instead of sleeps and timeouts. It took several iterations.
- **Delegated task types:** rebasing, resolving merge conflicts, checking CI failures, addressing PR feedback, triaging crashes, reviewing code, and overnight automated bug fixes.
- **Adoption metric:** "River initially created only 6% of merged mobile pull requests ... evolving to 61% of merged mobile pull requests". The time window is not stated in text (a chart in the post). Gains are attributed to Remote Dev plus internal campaigns.
- **Next:** health-monitoring workflows that auto-open crash-fix PRs, and multi-agent parallel bug bashes simulating merchants.
- **Mentions:** links back to Tobi's "Learning on the Shop floor" ("Earlier this year, Tobi shared how this was already shifting Shopify's culture").

## Notable quotes
- "Our ability to delegate work had outgrown our ability to run it."
- "We can see where people get stuck, where guidance goes wrong, where access to tools gets rejected. All of it."
- "River initially created only 6% of merged mobile pull requests."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- The 6%→61% chart's date range, and whether "created" means authored or coauthored.
- How "access to tools gets rejected" is enforced (the permission model) is not described.
- Whether Jev is an internal model or a distilled one is not stated here. AI Enabled PM wrote a separate piece on Jev (2026-09-24), which was not read.
