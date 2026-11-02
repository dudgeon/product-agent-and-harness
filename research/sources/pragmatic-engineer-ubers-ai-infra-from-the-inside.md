---
title: "Uber's AI infra, from the inside"
source_url: https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside
author: Gergely Orosz with Uday Kiran Medisetty (Distinguished Engineer, Uber)
publisher: The Pragmatic Engineer (podcast; also on YouTube as MDUYSMJmi8A)
published: 2026-10-14
retrieved: 2026-11-02
type: podcast
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [org-context-grounding, legible-org-for-agents, agent-as-service-many-surfaces, harness-portability, cost-control-routing, skills-marketplace, skill-improvement-loops, docs-as-code-prd, opportunity-to-code-chain, remote-agent-invocation, handoff-context-transfer, identity-delegation, risk-sloped-review, human-review-gates, outcome-measurement-gap, agent-legible-platform, sdd-input-contracts]
relevance: high
---

## Relevance to the project
The fullest first-party account of where Cortana came from and how it sits in Uber's lifecycle: it began "back in December" (2025) as one engineer's AI assistant on web and Slack that answered questions from any codebase, and its traces led Uber to build the context graph, which is now Cortana's "default grounding". Medisetty also describes a PRD/ERD tool (a single place for product and engineering design docs, launch, experiment and production-readiness reviews, with status, owners and Jira/Linear links, all fed into the graph, called a "source of truth system for both humans and agents to know the specs for every project"), and Minion taking a plan or Slack thread to PRs. That makes Uber a direct case for the shaping and dependency workstream: specs held in one tracked tool, linked to execution, and read by agents. Cortana carries forward the user's existing permissions. Interview format; the numbers are Medisetty's.

## Themes
- org-context-grounding: Cortana traces showed people asking research, query, data-source, ownership and RCA questions, and that models spent many turns getting grounded across siloed systems (37:45-38:36); the graph is now the assistant's "default grounding", so it first works out the domain and services, then reads deeper (39:25-39:43).
- legible-org-for-agents: 100+ node types and 130+ edge types, live; people, PRs, assets, design docs, features, on-call events, config changes and incidents all linked (38:46-40:43); built with help from the production graph team (41:53).
- agent-as-service-many-surfaces: Cortana "omnipresent in Slack, Web, CLI"; even "someone in Ops in some country" can ask how something is built, who works on it and its history (42:11-42:49); "execute any skill anyone has built" (42:58).
- identity-delegation: "we carry forward all of the existing user permissions, so then if I'm only able to access the stuff that I had access to" (43:07-43:23).
- harness-portability: AIFX (AI Foundations) wraps Claude Code, Codex and OpenCode so settings, skills, tools and plugins move with the engineer; pre-installed on DevPods; centrally managed settings synced across environments (24:00-25:12).
- cost-control-routing: spend tiers per user with manager approval to step up, a separate tier for background coding agents, a status line showing spend across harnesses, and a CostCheck plugin with personalised tips (25:34-28:20).
- skills-marketplace: a skills monorepo with central and team skills, one quality gate, portable across harnesses; persona-based default skills (24:34, 33:43-34:22); "around probably 30,000 skill executions per day" in recent weeks (35:24).
- skill-improvement-loops: in flight: collect harness traces and generate improvement patches for skills (35:03).
- docs-as-code-prd: PRD and ERD tool holds product and engineering design docs, launch reviews, experiment reviews and production-readiness reviews with status, owners, and Jira or Linear links; all fed into the graph (46:48-48:28). Later named as "the U-Plan tool" (1:24:05).
- sdd-input-contracts: "source of truth system for both humans and agents to know the specs for every project" (48:28); planning up front matters because of product and country heterogeneity and corner cases (48:42-49:00).
- opportunity-to-code-chain: "Once we have the plan, then the next thing is how do you convert that into, decompose that and execute" via Minion (49:38).
- remote-agent-invocation: Minion is used from web or Slack, with plan mode or one-shot; "@minion, follow this thread ... create a PR" takes the Slack thread as context (50:20-51:49); on-call asks Minion for a root cause in support channels (52:04).
- handoff-context-transfer: DebugAssist RCA handed to Minion, which attaches the PR to the Jira task holding the RCA; corrections become data to improve both (1:18:29-1:19:17).
- risk-sloped-review: Code Inbox routes PRs and adds risk score and blast radius; a "green lane" for auto-landing low-risk PRs is a future option only after backtesting; every PR still needs an engineer's review (56:35-59:22).
- outcome-measurement-gap: Uber moved from diff velocity to feature velocity, tagging PRs by type and complexity; uses AI to cluster and back-fill missing links from product design doc to engineering design doc to task so it can measure P50 feature time and find whether the bottleneck is in the PRD, launch or rollout phase (1:22:33-1:25:01).
- agent-legible-platform: MCP specs auto-generated from the Thrift/Protobuf IDL registry, with LLM-optimised descriptions (29:19-30:46); "All the things that we built to make life easier for engineers: it makes it easier for our agents as well" (show notes).

## Key points
- Model gateway: built on Michelangelo from late 2023; one OpenAI- or Anthropic-compatible API; first middleware was AI Guard (five fine-tuned models from the security team, on every request and response); every model request at Uber goes through it (18:36-23:42).
- MCP gateway: started around April 2025; built by the API gateway team; vendor tools (Google, Slack) exposed through it; recently every MCP also projected as a CLI; skills rewritten to the CLI pattern for token efficiency (28:31-37:11).
- Cortana origin and growth: built by one engineer in December; now plugs in the context graph, tools and skills; can produce a "360 degree health report" for an asset from logs, monitoring and dependencies (37:45-43:23).
- Minion: background coding agent; "around 15% of all of the production PRs go through Minion right now"; latest iteration is a v2; runs on a mega DevPod with all repos; began with maintenance tasks and is widening as self-validation tools are added (49:38-51:26).
- DevPods: warm Kubernetes pods cloned from prebuilt images with Bazel caches; a Minion flavour holds all repositories (52:17-53:52).
- Validation: `aifx validate` runs lint, coverage, build and template rules before a PR; Slate per-branch environments let agents test end to end; self-healing CI; CI jobs more than doubled in a year, prompting an internal "code red" (54:15-1:02:33; show notes).
- Customer support policy example: runbooks turned into agent-followable policies, with agents generating V0 policies, configuration and synthetic evals, under human verification steps (1:27:34-1:29:26).
- Engineer's job: "how do you build the right context for the agents to produce reliable output"; give the "right specs right constraints"; multitask; verify (1:25:42-1:27:06).

## Notable quotes
- "one of the engineers built an AI assistant that you can go to, we call it Cortana" (37:45)
- "a source of truth system for both humans and agents to know the specs for every project" (48:28)
- "we carry forward all of the existing user permissions" (43:20)

## Could not verify
- The transcript is the publisher's auto-generated one (read in a signed-in browser session); names are garbled in places ("U-Plan" may be "uPlan"; "Mahini and v2" is probably "Minion v2"). The year of "back in December" is inferred as 2025 from the episode date.
- Whether the PRD/ERD tool has its own agent, or whether Cortana drafts PRDs into it, is not stated; the talk demo shows Cortana drafting requirements, but not where they are saved.
- Episode figures (15% of production PRs via Minion; 30,000 skill executions a day) differ from the AI Engineer talk (70% of PRs by local or cloud agents; 20,000 skill executions a day); they measure different things at different dates.
