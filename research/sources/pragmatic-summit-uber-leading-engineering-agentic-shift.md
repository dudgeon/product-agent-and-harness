---
title: "Uber: Leading engineering through an agentic shift - The Pragmatic Summit"
source_url: https://www.youtube.com/watch?v=i1tZN41VKcE
author: Anshu Chada (head of Developer Platform, Uber) and Ty Smith (Principal Engineer, Uber)
publisher: The Pragmatic Engineer (YouTube; Pragmatic Summit)
published: 2026-03-10
retrieved: 2026-11-02
type: video
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [agent-control-plane, remote-agent-invocation, agent-as-service-many-surfaces, verification-capacity-gap, risk-sloped-review, human-review-gates, harness-portability, build-vs-buy, cost-control-routing, outcome-measurement-gap, leadership-permission-mandate, enablement-by-product]
relevance: high
---

## Relevance to the project
Uber's March 2026 snapshot of its developer-platform agent stack, six months before the software-factory talk, and it has no Cortana in it: the front door then was Minion (background agent) reached from web, Slack, CLI, PRs and an API, with a prompt improver and prompt templates. It shows the pieces Cortana later packaged (MCP gateway, no-code Agent Builder with a registry, AIFX CLI) and the review-side tools built to absorb agent output (Code Inbox, uReview, Autocover). It also gives Uber's own admission that the measures are activity, not outcomes, and that cost rose 6x since 2024. Bears on the teardown's lineage question (Cortana postdates this talk) and on review capacity as the binding constraint.

## Themes
- remote-agent-invocation: Minion is reachable through a web UI, Slack, GitHub PRs in review, the CLI, and an API "so that it can start to be connected to by other workflows" (14:55-15:40).
- agent-as-service-many-surfaces: one background-agent service behind several panes of glass; Slack pings at start and on completion with links to PR and artifacts (17:40).
- agent-control-plane: central MCP gateway built by a cross-company tiger team proxies internal and external MCPs with authorization, telemetry, logging, a registry and a sandbox (09:50-10:30).
- verification-capacity-gap: developers now spend more time in planning and review "because there's so much more code being generated" (18:50); review slowdown lets more bugs in.
- risk-sloped-review: Code Inbox estimates a change's risk from surface area and blast radius and flags it so reviewers add scrutiny (20:55-21:30).
- human-review-gates: uReview runs generators then a review grader to keep only high-confidence comments; Autocover pairs a generator with a separate critic, later split out as a standalone test validator (22:00-25:45).
- harness-portability: Minion runs on "state-of-the-art agents, CLIs, and SDKs" and the user picks the agent per task (Claude Code shown); abstraction layers let Uber swap model or technology (14:20, 16:50, 30:50).
- build-vs-buy: built Minion on its own CI infrastructure because vendors' background agents run on "other people's infrastructure"; expects its own tools to be replaced and accepts that (14:00, 31:30).
- cost-control-routing: costs up "at least 6x" since 2024; infrastructure picks a strong model for the plan and cheaper models for execution (36:40-37:30).
- outcome-measurement-gap: "these are activity metrics... not necessarily business outcomes"; plan to instrument time from first design to experiment launch (35:00-36:00).
- leadership-permission-mandate: top-down directives "had some impact"; sharing wins peer to peer worked better; four VPs landed code in a 24-minute demo session (32:50-34:00).

## Key points
- Framing (00:00-07:00): Uber moved from "pair programming" (Copilot-era, 10-15% velocity bump) to "peer programming": developers as their own tech leads directing async agents. When agentic workflows opened, 70% of submitted workflows were toil (upgrades, migrations, bug fixes), because start and end states are clear and accuracy is higher.
- Stack (08:00-12:30): Michelangelo model gateway (frontier and internal models); context sources (code, docs, Jira, Slack); industry agent clients; specialized agents; enablement on top. Michelangelo also offers agent building via SDKs and no-code agent builders with visualization, telemetry, tracing and a registry usable by "engineers or non-engineering alike". AIFX CLI provisions, configures and updates agent clients (Claude Code, Codex, Cursor), installs MCPs from the registry, ships standard configs, and connects to background-task infrastructure.
- Minion (14:00-19:00): background agent platform on Uber's CI platform with monorepos checked out, network access, and MCP access via AIFX; per-monorepo defaults; prompt templates with placeholders; choice of monorepo, branch or follow-up on an existing PR/diff; choice of agent; output as GitHub PR (dual mode with Phabricator during migration). A "prompt improver" flags low-quality prompts (red icon) and proposes edits. Demo: user bug report in, PR out after 7 minutes; the Minion bot co-authors with the requester; PR carries linked Jira, test plan and which agent ran.
- Code Inbox (19:00-21:30): unified PR inbox showing only actionable items; smart reviewer assignment from ownership, compliance, history, time zone and calendar; SLOs with reassignment and escalation; batched, focus-time-aware Slack notifications; plugs into teams' existing review-queue channels.
- uReview (21:30-24:30): preprocessor, plugin generators (defect bots, best practices, MCP-sourced context, external bots via API), grader, dedup, categorization; per-layer model choice from evals.
- Autocover (24:30-25:45): custom agent on internal LangFX SDK (built on LangChain); ~5,000 tests generated and merged per month; "almost a 3x rate of quality" vs a generic agent.
- Auto-migrate and Shepherd (25:45-29:30): four areas (problem identification, code transformer agentic or OpenRewrite, validation, campaign management). Shepherd is a web UI; migrations defined in YAML as a prompt or a script; it generates, refreshes and routes PRs and integrates with Code Inbox and Minion. Example: Java 21 upgrade.
- Non-technical (29:30-38:00): need to revisit build/buy often; adoption "slower than I've expected"; NPS and self-reported satisfaction at record highs; CFO asks for revenue impact; 2026 added JetBrains AI and Warp, each with its own cost model.

## Notable quotes
- "we imagine developers acting as their own tech leads" (Chada, 05:00)
- "the cost of AI is too damn high" (Chada, 36:50)
- "engineers trust other engineers as opposed to directors like me" (Chada, 34:30)

## Could not verify
- No mention of Cortana, a context graph, personas or a skills marketplace; consistent with Cortana starting later. The updated adoption figures (84% agentic users, 65-72% AI-generated IDE code, Claude Code 32% to 63% Dec-Feb) are in the video description dated 11 March, not the talk.
- Transcript is YouTube auto-captions; names such as "Thai" for Ty and "Cloud Code" are caption errors.
