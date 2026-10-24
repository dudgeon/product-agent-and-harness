---
title: "What happens after coding is solved? | Fiona Fung (Manager of the Claude Code and Cowork Teams)"
source_url: https://www.lennysnewsletter.com/p/building-the-most-ai-pilled-engineering
author: Lenny Rachitsky (host), Fiona Fung (leads the Claude Code and Cowork teams, Anthropic)
publisher: Lenny's Podcast
published: 2026-06-21
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [human-review-gates, evals-autonomy-trust, docs-as-code-prd, pm-persona-role-expansion, feedback-triage-agents, status-update-agents, outcome-measurement-gap, org-learning-loop, agent-ready-intent, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
The manager of Anthropic's Claude Code and Cowork teams says, first-hand, that once code throughput rose (8x per engineer per quarter, an Anthropic figure) the bottleneck became verification: "how do we know this works as intended?" That is the downstream half of the story's "bottleneck moved" claim, and her remedy is upstream: check "a statement of what good looks like" (specs, a content-design skill) into the repo so automated review can test against it. She also describes PMs and designers checking in code, monthly just-in-time planning replacing six-month roadmaps, and manager "routines" that turn feedback channels into overnight PRs. It bears on review-and-autonomy, intent-shaping-and-spec (the spec as the thing verification checks against), pm-agent-evaluation and target-user. It is a vendor insider describing her own team, which is the most AI-saturated setting there is, so treat it as an upper bound, not a typical enterprise.

## Themes
- human-review-gates: human code review "was a really really big bottleneck" until Claude code review arrived; humans still review areas that "need deep subject matter expertise" (14:54). Open question from her talk: "How far do you push fully automated reviews?" (1:09:13).
- evals-autonomy-trust: "bad vs sad" framework: bad = unrecoverable (e.g. CLI crash, lost work), sad = recoverable pain (flicker); each team defines its own bad/sad and goals (44:46-47:07). A swear-word dashboard tracks user frustration that evals miss (47:39). Verifying "that the experience is what you wanted it to be" is "still a hard one to crack" (1:10:44).
- docs-as-code-prd / agent-ready-intent: "if you have specs, check those into the repo and then make sure the spec also keeps up to date with the code"; any "statement of what good looks like" in the repo lets code review check against it; content design now has a skill in the repo (15:00). Lenny calls it the evolution of TDD (15:52).
- pm-persona-role-expansion: "designers, PMs, everybody on the Claude Code team checks in code" (8:16); PMs "no longer bottlenecked ... waiting on engineering bandwidth" and have shipped features when no engineer was free (1:00:23); next roles to change are design and data science (1:01:00). Hiring two profiles: creative builders with product sense, and deep systems experts (17:18).
- feedback-triage-agents / status-update-agents: her morning ritual of reading feedback channels is now a Claude "routine" that finds themes and opens PRs she reviews on waking (12:39, 36:20). A Claude Code remote session enlisted in all repos, Slack and metrics is used for monthly look-backs with reports (10:03).
- outcome-measurement-gap: lines of code, "significant" lines and time-to-land-PR all fail as productivity measures; "don't mistake motion for progress"; measure the outcome instead, plus listening tours with senior engineers (40:28-43:31).
- org-learning-loop: "pairwise programming lunches" because working with agents became "a lonely experience" and everyone uses Claude Code differently (55:38, 57:53); hackathons.
- vendor-claims-vs-independent-evidence: the 8x figure is Anthropic's own (tweet, 2021-2025 baseline), from the tool's maker.

## Key points
- **Throughput:** Anthropic engineers ship on average 8x as much code per quarter as in 2021-2025; flat for years, then a sharp rise this year (0:00, 2:41; Anthropic tweet linked in show notes). "Most commits are Claude assisted" (1:02:20).
- **Shift to verification:** in the CD-shipping era planning was heavy because engineering time was scarce; now "coding is no longer the bottleneck", so the question is verification of high-throughput, multi-discipline commits (8:16).
- **Async agent management:** "we're shifting more towards async"; a routine "generates ... these prompts for me" and spawns agents, so "the level of abstraction keeps pulling up"; eventually "go for it" autonomy where verification is good (35:37-38:00).
- **Unsolved:** context-switching load from many async agents; she now blocks focus time to catch up on async work (1:11:11-1:12:42). Growing the next generation of engineers without hand-coding years (1:13:19).
- **Planning:** a "super lightweight" six-month roadmap was barely referenced after three months; now monthly "JIT planning" on a short spreadsheet with weekly check-ins and six-monthly themes; looking to automate even the spreadsheet (1:23:00-1:26:48). Team value: explicit permission to kill processes that no longer serve.
- **Managers start as ICs** to learn the codebase and build rapport; she ships PRs herself to stay in the product (50:01-54:38). Claude was her "onboarding buddy" for the codebase.
- **Latent demand:** Cowork came from non-coders using Claude Code (analysing MRIs, recovering photos); Claude for Small Business from her onboarding small-business friends (32:43-34:57).
- **Agency with accountability:** high agency paired with high accountability and a stated hypothesis (38:48).

## Notable quotes
- "Coding is no longer the bottleneck." (0:00, Lenny quoting the theme; Fung at 8:16)
- "Any time you have a statement of what good looks like. Get that into the repo and then code review can make sure it's still matching." (15:00)
- "How do we know this works as intended?" (show-notes takeaway, paraphrasing 8:16 and 1:10:44)
- "I haven't cracked it yet." (on context switching, 1:12:42)

## Could not verify
- Transcript read in full (Substack auto-transcription; speakers labelled SPEAKER_00/01, "ClockCo"/"Cloud Code" = Claude Code).
- 8x is Anthropic's own metric with no published method; the swear dashboard, bad/sad framework and routines were described, not demonstrated.
- The "bottleneck shifted to how do we know this works" line is Lenny's takeaway wording; Fung's own words are close (8:16, 1:10:44).
