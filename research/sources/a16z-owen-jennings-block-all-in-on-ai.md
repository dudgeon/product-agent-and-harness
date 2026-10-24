---
title: "What Happens When a Public Company Goes All In on AI"
source_url: https://a16z.com/podcast/what-happens-when-a-public-company-goes-all-in-on-ai/
author: David Haber (a16z) with Owen Jennings (executive officer and business lead, Block)
publisher: a16z podcast
published: 2026-04-01
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-block-product-practices
themes: [pm-persona-role-expansion, ai-flattened-org, non-engineer-builders, human-review-gates, agent-factory-sdlc, outcome-measurement-gap, leadership-permission-mandate, compounding-context-repo, opportunity-to-code-chain, legible-org-for-agents, pm-job-stable-methods-change]
relevance: high
---

## Relevance to the project
The most concrete first-party account of what Block's product organisation looks like after the February 2026 cut, from the executive product reports to. Jennings says "All of our product managers are shipping PRs", feature teams of about 14 became squads of one to six, product has "two layers, maybe three", meetings fell 70-80%, and an internal agent (Builder Bot) takes many features to 85-90% before a human finishes them. He also predicts fewer PMs per roadmap, while expecting more PMs overall via Jevons. Directly relevant to persona design (PM as agent supervisor) and to where human review sits.

## Themes
- pm-persona-role-expansion: "for a given product or for a given roadmap, you're going to need fewer engineers, fewer designers, fewer PMs. I think that's very, very clear after December" [about 11:13]; but not necessarily fewer in the world: "the classic Jevons paradox thing". "All of our designers are... shipping PRs. All of our product managers are shipping PRs." [12:55]
- ai-flattened-org: old shape was "eight server engineers, four client engineers, a PM, and a designer" working linearly through a roadmap; now "squads of like one to six people" that cycle between products [12:55]. Development layers cut "by, I don't know, 50 or 60%"; product has two or three layers [12:55]. Example: "a squad of three people instead of a feature team of 14" [06:43].
- agent-factory-sdlc / human-review-gates: Builder Bot "is just autonomously merging PRs"; some complex features reach 100%, "more often than not" 85-90%, then "a human who has a lot of context" finishes [12:55]. Human in the loop is "critical" now for partners and regulators but he expects that to fall [12:55].
- non-engineer-builders: PMs and growth/marketing staff also run agents in parallel; his own work is checking "10 or 20 agents" and committing the markdown output to GitHub as "source of truth" [09:18]. G2, an internal "agentic operating system", lets "anyone... automate any deterministic workflow" [11:13].
- compounding-context-repo: a company as "a markdown file of who you are" (values, metrics, what you care about) fed by proprietary signal and iterated by agents; humans may become "more like editors" [23:22].
- outcome-measurement-gap: claims are throughput and cost: "couple months to build a feature. Now it takes maybe a week or two" [23:22]; Moneybot team went from about 15 people to four "plus $2,000 on the tokens" [09:18]. No customer-outcome measure.
- leadership-permission-mandate: "unlimited access to tokens and you can use fast mode on Claude Code"; the cut is "a massive forcing function" for workflow change [09:18]. Weekly one-to-two-hour all-hands with Dorsey every Monday [06:43].

## Key points
- Timeline: goose launched early 2024; "late November, first week of December" 2025 a "binary change" (he names Opus 4.6 and Codex 5.3) made tools capable on complex existing codebases; Q1 2026 spent by the exec team working out implications; cut "slightly greater than 40%" [03:13].
- Cuts were "way larger on the development side"; outbound sales, account management, regulatory and compliance teams were left largely intact ("we basically did not touch our compliance team") [05:49, 06:43].
- Principles for the cut: reliability first (an outage is "P00"), regulatory trust, durable growth; org rebuilt "from scratch" [06:43].
- 18 months earlier Block moved from business units to functions; product rolls up to Jennings, engineering and design to their heads [17:02].
- Gross profit per FTE: middle of the pack 2019-2024, "second quintile" in 2025 behind Nvidia and Meta, per Jennings [05:49].
- Generated interfaces in Moneybot/Managerbot are "potentially a nightmare from a QA perspective" [20:13].
- He disputes the "cruft and bloat" narrative: "we're not writing code by hand anymore. That's over, that's done." [05:49]

## Notable quotes
- "All of our product managers are shipping PRs." [12:55]
- "Maybe the humans are more like editors." [23:22]

## Could not verify
- Transcript read via a third-party transcription (pod.wave.co), not the a16z page, which has video only; timestamps are that site's and approximate. Host name is auto-transcribed as "Haper".
- Model names "Opus 4.6" and "Codex 5.3" are as spoken. No data on PM headcount before/after or how PM PRs are reviewed.
- A separate claim (The Information on X, reported via Digg) that Jennings said Square shipped about 3x as many features in H1 2026 as a year earlier was not read at source.

## Second reading (2026-10-24, research-block-product-practices, PM-practice pass)
A second subagent read the same source for PM practice; its notes, merged here from a duplicate note:

### Relevance to the project
Block's business lead (product operations and support across Square, Cash App and Afterpay) states that "all of our product managers are shipping PRs", that PMs and growth marketers now run many background agents in parallel, and that Builderbot builds most features to 85-90% with a human finishing the rest. He sketches the end state as a company "markdown file" of values, metrics and non-goals fed to an agent loop, with humans "more like editors". This is the clearest Block statement of the PM's changed job and of an intent artifact that drives agents, though it is an executive's claim without method.

### Themes
- pm-persona-role-expansion / non-engineer-builders: "All of our designers are are shipping PRs. All of our product managers are shipping PRs. That's not that interesting anymore." (section "Development and Automation Processes").
- agent-factory-sdlc: workflow shift from sequential PR-review-change to "I have 14 agents who are building PRs on my behalf"; "it's not just ... software development ... it's for PMs too it's for growth marketers too" ("eight instances of goose up") (restructuring section).
- human-review-gates: Builderbot "autonomously merging PRs" and building some features to 100%, more often to "85 or 90%", then "a human who has a lot of context" does the final 10% ("Development and Automation Processes").
- legible-org-for-agents / opportunity-to-code-chain: "a markdown file of like who you are", values, "metrics we're trying to optimize for", what "we don't care about", plus a feedback loop with the company's data signal and a tool like Builderbot or Claude Code; feature cycle from "a couple months" to "a week or two"; future "hundreds, thousands of times a day ... Maybe the humans are more like editors" ("Data, Insights, and Iteration Loop").
- pm-job-stable-methods-change: "for a given roadmap, you're going to need fewer engineers, fewer designers, fewer PMs", but not necessarily fewer in the world.

### Key points
- Old team shape: "eight server engineers, four client engineers, a PM, a designer", working linearly through a roadmap; now squads of one to six that rotate across products for a few cycles; "a squad of three people instead of a feature team of 14".
- Development-side management layers cut by "50 or 60%"; product side has two or three layers.
- December 2025 model releases are cited as the turning point: "a designer and an engineer who was on the tools" became "10 20 100x more productive" (speaker estimate).
- Outside development, any deterministic queue work is being automated; chatbots and AI phone support handle "a majority" of support inquiries; product, risk and compliance operations decisioning next.
- Proactive intelligence (Moneybot, Managerbot) is where product value is going; generated, per-user interfaces are "potentially a nightmare from like a QA perspective".

### Notable quotes
- "Maybe the humans are more like editors." (closing section)
- "if your answer to that is ... I don't know, then ... you maybe could get vibe coded away." (closing section, on moats)

### Could not verify
- a16z's page has no transcript; I read the transcript reproduced on Ernest Chiang's write-up (https://www.ernestchiang.com/en/posts/2026/coexisting-with-ai-three-restructuring-principles-from-block/, 2026-04-05), which embeds the video (YouTube krdrkl38nRw). No timestamps, so section headings from that transcript are used. Auto-transcription errors ("Opus 46", "codeex 53").
- "All PMs ship PRs" is unquantified and unverified; what PM PRs contain (prototypes, copy, config, features) is not said. Whether the "markdown file for Block" exists is ambiguous.
