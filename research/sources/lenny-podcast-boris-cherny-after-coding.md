---
title: "Head of Claude Code: What happens after coding is solved | Boris Cherny"
source_url: https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens
author: Lenny Rachitsky (host), Boris Cherny (creator and head of Claude Code, Anthropic)
publisher: Lenny's Podcast
published: 2026-02-19
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [harness-over-model, non-engineer-builders, pm-persona-role-expansion, feedback-triage-agents, human-review-gates, status-update-agents, enablement-by-product, cost-control-routing, agent-led-intent-shaping, single-agent-many-skills, evals-autonomy-trust, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
The head of the most-used coding harness describes, first-hand, how his own team works once "coding is virtually solved": Claude reviews every pull request with a human layer after it, Claude reads the internal feedback channel and proposes fixes, Cowork runs his team's weekly status chasing, and roles overlap by about half. It is the clearest statement of the "minimal scaffolding, don't box the model in" harness philosophy, which bears directly on whether a PM meta-harness should encode workflows (work-structure, loop-source, harness-layering). It also names the next frontier as the roles adjacent to engineering (PM, design, data science), which is our target. Treat the productivity numbers as a vendor speaking about its own product.

## Themes
- harness-over-model (contested here): Cherny argues the opposite emphasis for scaffolding: "almost always you get better results if you just give the model tools, you give it a goal" (1:03:43); scaffolding gains of "10%, 20%" get "wiped out with the next model" (1:05:15). Build "for the model six months from now" (1:06:46).
- non-engineer-builders: on the Claude Code team "our product manager codes, our engineering manager codes, our designer codes, our finance guy codes, our data scientist codes" (40:58); a data scientist ran SQL analysis in the terminal and "the next week all of the data scientists were doing the same thing" (49:11). Designers mostly use the desktop app's code tab (46:32).
- pm-persona-role-expansion: "maybe a 50% overlap in those roles"; the PM does "more coordination or planning or forecasting" (42:46); predicts "everyone is going to be a product manager and everyone codes" and the engineer title replaced by "builder" (43:06).
- feedback-triage-agents / agent-led-intent-shaping: Claude "is looking at bug reports ... telemetry ... starting to come up with ideas for bug fixes, and things to ship" (17:54); in practice he points Claude or Cowork at the internal feedback Slack channel and it puts up PRs for him to approve (19:30).
- human-review-gates: "Claude reviews 100% of pull requests. There's still a layer of human review after it", except for throwaway prototypes (16:52). He still reads code: "I don't think we're at the point at where you can be totally hands-off" (16:52).
- status-update-agents: Cowork does "all of my project management for the team" (17:54); concretely, a team status spreadsheet with a row per engineer, and every Monday Cowork messages on Slack each engineer who hasn't filled in their status, from one prompt (1:22:08).
- enablement-by-product: latent demand as "the single-most important principle in product" (47:29); Cowork came from watching non-coding Claude Code use (MRI analysis, wedding-photo recovery) and "take Claude Code and put it in the desktop app" (52:14).
- cost-control-routing: don't optimise token cost early; some Anthropic engineers spend "hundreds of thousands a month in tokens" (27:44); use the most capable model because a cheaper one "takes more tokens in the end" (1:08:51).
- evals-autonomy-trust: three safety layers: interpretability, evals ("model is in a Petri dish"), then behaviour in the wild, hence early research-preview releases (54:30). Claude Code was used internally four or five months before release (54:30). Lenny's "50 non-technical uses" post was used by a PM as an eval for Cowork pre-launch: 48 of 50 passed (1:23:27).
- single-agent-many-skills: "It's the same Claude agent running everywhere" across terminal, desktop, iOS, Slack, GitHub (1:10:21); his own coding is roughly a third terminal, a third desktop, a third iOS (1:00:11).
- vendor-claims-vs-independent-evidence: "productivity per engineer has increased 200% in terms of pull requests" while the engineering team roughly 4x'd (20:50); he says he doesn't know the exact number. Measured in PRs, a vendor's own metric.

## Key points
- Origin: a one-person terminal prototype ("Claude CLI") that got two likes internally; DAU "went vertical" inside Anthropic; external release in February 2025 was not an immediate hit; inflections at Opus 4 (May 2025) and November 2025 (9:45-12:49, 52:14).
- Personal practice: 100% of his code written by Claude Code since November 2025; 10-30 PRs a day; about five agents running at once; Opus 4.6 runs "10, 20, 30 minutes unattended" (0:00, 16:23, 1:07:37).
- Team principles: under-fund projects so people are "forced to Claude-ify" (one engineer per project); go faster ("if you can do something today, you should just do it today"); "what's better than doing something? Having Claude do it" (24:03-25:54).
- Plan mode is "one sentence" injected into the prompt telling the model not to write code yet; he starts ~80% of tasks there, then auto-accepts edits (1:08:51).
- Cowork: built in about 10 days entirely with Claude Code, including a shipped virtual machine and guardrails for non-engineers; released as a rough research preview to learn about safety in the wild (52:14-56:05).
- Anthropic open-sourced a sandbox that "works with any agent, not just Claude Code" (58:48).
- Hiring: Anthropic screens even non-technical functions with technical interviews; designers largely code (45:37). This makes Anthropic an unrepresentative reference for a typical enterprise.
- Lenny's informal X polls: ~70% of engineers and PMs enjoy their job more since adopting AI, ~10% less; designers 55% more, 20% less (44:59). Unscientific poll.
- Revenue context from the host: Claude Code ~$2B revenue, Anthropic ~$15B (1:15:21); SemiAnalysis: 4% of public GitHub commits authored by Claude Code (5:35).

## Notable quotes
- "Coding is virtually solved." (0:22)
- "Don't try to give it a bunch of context upfront. Give it a tool, so, that it can get the context it needs." (1:03:43)
- "Claude reviews 100% of pull requests. There's still a layer of human review after it." (16:52)
- "Kat, our PM, does a little bit more coordination or planning or forecasting." (42:46)

## Could not verify
- Transcript read in full (Substack auto-transcription; some words garbled, e.g. "[inaudible]").
- 200% PR productivity, 4x team growth, 4% of GitHub commits, DAU doubling, revenue figures: speaker's or host's own numbers, no method stated. "200%" is measured in pull requests, which conflates volume with value.
- "Coding is solved" is stated for "the kinds of programming that I do"; no evidence offered for enterprise or regulated codebases.
- The 48/50 Cowork eval is an anecdote with no detail on the grading.
