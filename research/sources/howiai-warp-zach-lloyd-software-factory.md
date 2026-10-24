---
title: "How Warp ships 2,000 PRs a month with AI factories | Zach Lloyd (CEO, Warp)"
source_url: https://www.lennysnewsletter.com/p/how-warp-ships-2000-prs-a-month-with
author: Claire Vo (host), Zach Lloyd (co-founder and CEO, Warp)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-09-21
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [agent-factory-sdlc, public-by-default-agent-work, human-review-gates, risk-sloped-review, evals-autonomy-trust, outcome-measurement-gap, cost-control-routing, remote-agent-invocation, org-learning-loop, human-judgment-pm-jobs]
relevance: high
---

## Relevance to the project
A concrete, demoed picture of a cloud "software factory" as a harness layer above coding agents: requests from Slack, Linear, GitHub or Sentry become a tracked issue, an implementation, a PR and a computer-use QA video, all in public threads, with every run recorded, scored by an LLM judge and fed to an observer agent that edits the factory definition. It is the clearest worked example in the library of the downstream half of the Helm story (coding agents out, shepherding and acceptance), and it gives a number for "the bottleneck moved": 35 minutes kickoff-to-PR vs 3.5 hours PR-to-first-human-review. It also offers a candidate metric for pm-agent-evaluation ("human interactions per PR"). Lloyd sells this product (Warp Factories), so treat all dashboard numbers as vendor claims about Warp's own use.

## Themes
- agent-factory-sdlc: the factory triages an input, opens a Linear issue, implements, opens a GitHub PR, then runs computer-use QA that records a video of the feature (5:52-7:25); triggers can be human (Slack tag of "Wilson"), external (Sentry crash reports), or start in Linear/GitHub (9:08).
- public-by-default-agent-work: "most work is starting in a public place" (4:19); multiple people join Slack threads, so builders are "no longer sort of working in this local silo" (7:25); Lloyd credits public work with spreading power-user habits across a power-law team (41:27).
- human-review-gates: all PRs still get human review (15:30); Warp dropped the two-person rule, so the prompter may review the agent's own code (15:30-16:01); "we don't have yet complete trust" (16:01).
- risk-sloped-review: Vo describes risk-scoring every PR and auto-stamping low-risk ones (her own "Merge Mommy" agent); Lloyd: "code review becomes an exercise in risk management" (16:18-17:01).
- evals-autonomy-trust: LLM-as-judge scores sampled agent runs on dimensions such as redundant tests, using a "medium smart" judge model to contain scoring cost (20:20-21:59); a second loop has an observer agent read 20-25 failed runs and propose changes to factory agent definitions (22:07); needs a real sample "otherwise it starts to overcorrect based on single things".
- outcome-measurement-gap: "human interactions per PR" (re-prompts in Slack, Linear comments, code review corrections) as a proxy for automation and throughput (12:37-14:41); Lloyd says "we're trying to figure out ... what is the right set of metrics".
- cost-control-routing: per-PR agent cost tracked centrally; model is "the biggest" lever, context management second (18:11); replay past real tasks under other model configs to build a cost-quality Pareto chart and feed a routing strategy (28:21-30:39).
- remote-agent-invocation: everything centralized in the cloud; work can be kicked off from any of Slack, Linear, GitHub (10:42).
- org-learning-loop: factory definition is code (repos, MCP servers, config, agents), so it can be versioned, replayed and edited by coding agents (23:44).
- human-judgment-pm-jobs: Warp keeps user interviews, watching users, and design jams "to make sure that we're tackling the right user stories" before building (41:27-42:58).

## Key points
- Two personas: the builder (contributes ideas; experience similar to a local coding agent, but in public) and the manager/CTO (wants velocity, improvement over time and cost visibility, impossible when "every builder has their own individual local setup") (4:19, 11:08).
- Dashboard numbers shown (Warp's own team): over 2,000 PRs in the last month; kickoff to PR 35 minutes; PR to first human review 3.5 hours (0:00, 14:41). Cost per PR rose with adoption, then dropped after model config changes (17:01-17:47).
- Factory = "an actual noun": repos + MCP servers + configuration + agents (code review agent, design agents, automations), all defined in code, which lets you freeze a factory state, rerun tasks against a changed definition, and let agents edit it (23:44).
- Quality for replay uses the same LLM-judge scoring; human or algorithmic judges possible but not built (30:55).
- Vo's recap: you need "session, tool call, MCP call, test failure, computer use level observability into every single coding session"; some teams copy every local coding session to S3 to run their own evals (26:03-27:40).
- CEO non-technical work: edits Figma slides via Figma MCP from Warp's coding agent by voice; Granola MCP mines four weeks of sales calls for the top 10 questions (top: buy vs build, then security, workflow, measurement, cost); a Google CLI scan of six months of email and calendar for cold leads into a Sheet; runs these in parallel tabs (32:09-40:18).
- Sponsor read cites a DX study of 500+ engineering orgs: AI tool spend up 28x in a year, innovation flat, review and validation friction offsetting gains (1:45). This is sponsor copy, not Lloyd's claim.

## Notable quotes
- "Kickoff to PR time, it's 35 minutes. But ... PR to first human review, it's three and a half hours." (Vo reading the dashboard, 0:00/14:41)
- "Code review becomes an exercise in risk management." (Lloyd, 17:01)
- "It doesn't matter how fast you build software, it still has to solve some user problem." (Lloyd, 42:58)

## Could not verify
- Full transcript read (Substack auto-transcription; "Cloud Code" = Claude Code, "Orb/more factories" = Warp Factories). Dashboard figures were shown on screen and read aloud; not independently verified and specific to Warp's own team.
- The observer agent's proposed change was shown as one example; how often its edits are accepted, and whether they improve scores, was not stated.
- Factory input is product requests already shaped enough to build ("simple enough and ambiguous enough"); how unclear intent is handled was not covered.
