---
title: "Spec-driven development: The AI engineering workflow at Notion | Ryan Nystrom (How I AI)"
source_url: https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering
author: Claire Vo (host), Ryan Nystrom (engineering tech lead manager, Notion AI)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-05-11
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [docs-as-code-prd, agent-ready-intent, remote-agent-invocation, status-update-agents, human-review-gates, single-agent-many-skills, org-context-grounding, harness-over-model]
relevance: high
---

## Relevance to the project
A first-party account of a spec checked into the repo as the handoff artifact to a coding agent, at a company that builds an agent platform. Notion keeps an `agent specs` folder of Markdown specs for Notion AI; a dictated "yap session" becomes a spec in the house format, the spec carries code pointers and a verification section, and Codex builds from it ("basically one-shotted"), then verifies by driving Notion AI through a purpose-built CLI. The spec is then the version-controlled source of truth: change the spec, not the code. Also shown: "Boxy", an internal VM fleet that lets anyone @mention Codex from a Notion comment and get a PR with screenshots in about 20 minutes, and a scheduled Notion custom agent that writes the daily standup pre-read. Bears on intent-shaping-and-spec (spec standard: code pointers plus verification), remote-invocation-route, artifact-and-project-structure and review-and-autonomy.

## Themes
- docs-as-code-prd: `agent specs` subfolder in the Notion repo holding Markdown specs; the spec "is now the sort of like source of truth for how this part of Notion AI works ... in plain English that can then be verified and implemented by agents"; its git history is a changelog of how the feature works (32:06-35:34).
- agent-ready-intent: what made one-shotting work was a spec "so comprehensive with code pointers" plus a verification section at the bottom; Claire notes "there is not code in the spec. There's just not all the code in the spec" (33:36, 35:34). The engineer's job becomes "the verification loop"; if verification is hazy, build the tool first (36:57).
- remote-agent-invocation: Boxy ("Software Factory"), VMs with Codex and Claude Code installed, invoked by mentioning Codex in a Notion task comment; 10:40 start, PR plus preview URL about 10 minutes later, with self-uploaded UI-verification screenshots; replies in the comment thread fix CI and type failures (25:07-29:22). Internal only; "we might ship some version".
- status-update-agents: a "hot potato" Notion custom agent runs at 9am, fans out sub-agents (map-reduce) over the project Slack channel, task database, merged PRs, yesterday's meeting transcript and a Honeycomb metric via MCP, fills the meeting template and posts to Slack (6:08-19:39). Read-only on shared task and project databases; edit only on the meetings database (18:02). Saves ~20 minutes a day and, more importantly, context switching (21:24).
- human-review-gates: review still happens on the agent PR ("I don't get this"), and he prompts the agent to defend its change under pushback because models are "a little sycophantic" (29:59, 45:31). Claire: specs no longer wait for a review meeting; debate the live, verified result instead (37:53).
- single-agent-many-skills: Notion rebuilt its agent harness after "tool and instruction fatigue" with a bloated system prompt, borrowing skills and progressive disclosure from coding agents (32:06).
- org-context-grounding: the pre-read works because the agent reads all project exhaust; Claire: it "pulls equal amounts of information out of everybody", surfacing quiet engineers' work (10:25-12:06).
- harness-over-model: fast CI is "on steroids" important with agents; Claire cites Stripe's 1,300 agent PRs a week as impossible with slow CI (42:45-44:27).

## Key points
- Context: Nystrom manages 6-7 engineers and still codes; running Project Afterburner to cut Notion's CI time to a quarter (4:36).
- Sub-agents in Notion AI exist but are "very expensive" and "finicky"; he used them anyway (16:32). He configured the agent's Honeycomb MCP query by giving the agent a screenshot (19:39).
- Spec workflow in full: Whisper dictation → Codex told "learn the format" from the spec library → spec → a couple of revisions → new Codex session "build it" → a couple of hours, a couple thousand lines → his own code review and manual play → done (33:36-35:08).
- He prefers Codex because it gets closer to one-shotting while he round-robins many agents, rather than iterating with a browser (40:03).
- Claire's recap: three use cases: never prep for a meeting; background agents from wherever you work; specs in the repo as the source of truth, and "when you update, update the specs, don't update the code" (38:00-39:23).

## Notable quotes
- "I didn't start with writing code ... I just started with an empty markdown document." (33:00)
- "I view our job as like engineers evolving into like systems thinkers and architects ... most importantly is like the verification loop." (36:57)
- "No more waiting for the meeting no more waiting for review." (Claire Vo, 37:53)

## Could not verify
- Transcript read in full. Boxy is internal tooling shown on screen; timings are the speaker's reading of timestamps.
- "One-shotted" is self-reported; no data on how many specs or how often the spec-first path works across the team.
- Whether product managers write or read these specs is not discussed; every author shown is an engineer.
