# Research plan: taxonomy of agent runtime patterns

Date: 2026-10-24. Task: research-agent-runtime-patterns-taxonomy. Status: draft.

## Goal

A research-grounded taxonomy of agent runtime patterns for coding and knowledge work, to inform three aims: (1) make users' work less dependent on one harness (today mostly Claude Code); (2) package complex, standardized skills/subagents; (3) move sessions from local/private/ephemeral to deployed/shared/persistent. Building our own harness is **one option among the patterns, not a premise**.

## What existing research already covers (and gaps)

Read: the project brief, research/README.md, INDEX.md and THEMES.md (about 130 source notes), the Ramp Glass teardown, the PM-agents brief and the prior-work note.

Covered, build on it and do not redo:
- **Ramp Glass** (a first-party-built harness on the Claude Agent SDK): MCP proxy, Dojo skills marketplace on Git, memory pipeline, cost router, shared sessions, scheduled tasks. Themes: `harness-over-model`, `skills-marketplace`, `memory-architecture`, `cost-control-routing`, `single-agent-many-skills`, `build-vs-buy`. All Ramp's own account, no independent verification.
- Ramp's Inspect (Modal-sandboxed, multiplayer coding agent), Block's Goose, Intercom's Claude Code rollout, Anthropic Cowork plugins (mentioned, in PM context), Notion custom agents.
- PM-agent jobs and where they worked (`one-job-per-agent`, `org-context-grounding`, `human-review-gates`, `prd-agents`, `agent-failure-modes`).

Gaps (this task's tracks):
- No source yet on meta-harnesses, harness-agnostic layers, A2A, remote-agent MCP servers, managed/cloud agents, agent frameworks, open skill standards, or multi-user persistent sessions as an infrastructure pattern.
- Little independent evidence anywhere; the Ramp material is first-party.
- The structured vs unstructured work distinction is a working hypothesis, not yet researched.

## Preliminary findings (from two quick searches, to be verified by the tracks)

- "Ormnigent" is very likely **Omnigent**: Databricks' open-source (Apache 2.0, alpha) "meta harness" that sits above Claude Code, Codex, Pi or custom agents. It offers a uniform session API in sandboxes, policies (e.g. spend caps) and shared live sessions. Source: [Databricks blog](https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents) (vendor claim; not yet read in full).
- **Confirmed (2026-10-24):** Ormnigent = Databricks' Omnigent; the Cloudflare offering is **Cloudflare OS** (https://blog.cloudflare.com/cloudflare-os, 2026-08-05): open-source, deploy-in-your-own-account per-employee agent workspace (persistent workspaces/sessions, Access + typed bindings + 'Gatekeepers', Dynamic Workers apps, AI Gateway cost caps, shared skills library; browser-based, does not mention Claude Code/Codex). Related: 'How we use AI with Cloudflare OS', github.com/cloudflare/cloudflare-os. Cloudflare Agents Week, 2026-04-14 to 04-20**, an "agent cloud" (Sandboxes GA, Artifacts Git storage, Workflows v2, Mesh, Managed OAuth for Access). Secondary coverage only so far; the plan may mean a newer offering. Track 1 must identify it.

## What we already have (per track: start here, fill gaps, don't redo)

Existing material: `research/INDEX.md`, `research/THEMES.md`, `research/sources/` (Ramp Glass, intent-factory, PM-agent notes); `tasks/competitive-teardown-ramp-glass/00-teardown-summary.md`; `tasks/research-pm-agents-jobs-to-be-done/` (00-brief, 01-jobs-to-be-done-map, 02-commercial-pm-agents, 03-in-practice-cases-and-failures); `tasks/research-product-agent-and-harness/00-prior-work-found.md`; Geoff's two artifacts `sources/geoff-building-accelerating-intent-factory.md` and `sources/geoff-intent-shaping-well-managed-environment.md`. Reuse existing theme slugs.

| Track | Starts from (themes / findings) | Gap to fill |
|---|---|---|
| 1 Meta-harnesses | `harness-over-model`, `build-vs-buy`, `cost-control-routing`; Glass's MCP proxy and shared sessions; Goose (low-relevance note) | Omnigent, Cloudflare OS, others; independent evidence |
| 2 Frameworks | `build-vs-buy`, `single-agent-many-skills`; Glass is built on the Claude Agent SDK; Ramp's applied-AI service (LLM proxy) | What frameworks provide vs leave out; evidence beyond Ramp's own account |
| 3 Remote agents | `one-job-per-agent`; Ramp Inspect/Policy Agent; Jira-agent-to-coding-agent flow (Atlassian) | MCP-agent, A2A, managed/cloud agents; real adoption |
| 4 Skills/plugins | `skills-marketplace` (Dojo), `org-learning-loop`, Cowork PM plugin notes | Open standards, portability, security, how much complexity a skill can carry |
| 5 Shared sessions | `memory-architecture`, `compounding-context-repo`, `org-context-grounding`; Glass multiplayer/scheduled tasks (laptop-dependence limit noted) | Infrastructure for deployed/persistent sessions; failures |
| 6 Work structure | PM jobs map (10 jobs x suitability), `human-judgment-pm-jobs`, `human-review-gates`, `evals-autonomy-trust`, `risk-sloped-review`, `one-job-per-agent` vs `single-agent-many-skills` | Test the structured/unstructured hypothesis beyond PM work |

The synthesis must also connect each pattern to those themes, the PM jobs, and the Glass design choices (teardown summary list 1-9).

## Draft axes of the taxonomy

1. **Where the runtime lives**: local process / local sandbox / user-owned remote (SSH, devbox) / vendor cloud / org-deployed service / edge.
2. **Who owns the harness (the loop)**: vendor product (Claude Code, Codex) / vendor SDK embedded in own product (Agent SDK, Glass) / framework-built (own harness) / meta-harness wrapping others / none (workflow engine).
3. **Harness coupling**: tied to one harness / portable across harnesses via open formats (skills, MCP, AGENTS.md) / harness-agnostic orchestration layer.
4. **Packaging of capability**: prompt / skill / plugin / subagent definition / MCP server / deployed agent behind a protocol (A2A, MCP-as-agent) / marketplace distribution and versioning.
5. **Invocation relation**: in-process subagent / spawned child session / remote call to a deployed agent / peer delegation / human-triggered handoff / scheduled or event-triggered.
6. **Session locality, sharing, persistence**: ephemeral-private / resumable-private / shared-live (multiplayer) / persistent-deployed (long-running, event-driven) / org memory.
7. **Governance and control plane**: permissions, policy, cost caps, audit, identity (on-behalf-of auth), evals.
8. **Work structure served**: unstructured (planning, ideation, exploration) vs semi-structured vs task-specific workflow (e.g. PRD review). Cross-cut: how each pattern serves each.

Pattern classes expected (hypotheses to confirm or discard): (A) general harness + skills/subagents; (B) own harness on a framework/SDK; (C) meta-harness; (D) harness calling deployed task agents (MCP/A2A); (E) cloud/background agents (managed sessions); (F) shared persistent workspace/session; (G) workflow-engine-embedded agents; (H) portable skill/plugin ecosystems as the distribution layer.

## Research tracks

Each track: read-only web research, one source note per primary source in `research/sources/`, INDEX line, THEMES evidence (reuse slugs; add `meta-harness`, `harness-portability`, `remote-agent-invocation`, `shared-persistent-sessions`, `skill-standards`, `agent-frameworks`, `work-structure-spectrum` as needed), vendor claims separated from independent evidence, dates noted.

1. **Meta-harnesses and harness-agnostic layers.** Scope: Omnigent (Databricks), Cloudflare's agent-cloud/harness offerings (identify the "new offering"), and others (e.g. orchestrators and multi-agent CLIs wrapping Claude Code/Codex, ACP/Agent Client Protocol, conductor-type tools, OpenCode/Goose-like open harnesses, Vercel/Modal/E2B-style session runtimes). Seeds: Databricks blog + GitHub repo, Cloudflare Agents Week posts, Zed ACP, Goose docs.
2. **Frameworks for building your own harness.** Scope: Claude Agent SDK, OpenAI Agents SDK / Codex SDK, LangGraph, Google ADK, Vercel AI SDK, Pydantic AI, Mastra, Microsoft Agent Framework; what a harness includes (loop, tools, context, permissions, memory, sandbox); build-vs-buy evidence beyond Ramp. Seeds: framework docs, Anthropic "effective agents / harness" engineering posts, independent comparisons.
3. **Calling deployed remote agents from Claude Code/Codex.** Scope: MCP servers that are agents, A2A protocol (Linux Foundation), Claude Agent SDK / Managed Agents, Claude Code on the web/background agents, Codex cloud, Cursor/Devin/Copilot background agents, subagents-as-a-service; auth on-behalf-of, streaming and long-running tasks. Seeds: A2A spec, MCP spec (tasks, elicitation), Anthropic and OpenAI docs.
4. **Portable skills, subagents and plugin ecosystems.** Scope: Agent Skills open standard, AGENTS.md, Claude Code plugins/marketplaces, Cowork plugins, Codex/Copilot/Cursor equivalents, enterprise skill registries, versioning, security of third-party skills. Seeds: agentskills.io, Anthropic skills docs, plugin marketplace docs, security analyses.
5. **Deployed, shared, multi-user, persistent sessions.** Scope: multiplayer/shared sessions (Glass, Inspect, Omnigent), cloud workspaces, long-running/event-driven agents, durable execution (Temporal, Cloudflare Durable Objects, Workflows), team memory, session handoff, scheduled agents, collaboration UIs (Notion agents, Slack-native agents). Seeds: Ramp sources (already filed), Cloudflare Agents SDK, Temporal/agents write-ups, Devin/Cursor team features.
6. **Classes of user activity and fit.** Scope: evidence on unstructured exploration vs structured workflows: when flexible general harnesses win, when task-specific agents/workflows win (Anthropic "workflows vs agents", Cagan/Torres on product work, research on agent reliability, "one job per agent"), PRD-review-type standardization. Seeds: Anthropic "Building effective agents", existing PM-agents brief, practitioner write-ups.
7. (Optional, only if tracks 1-6 leave a gap) **Governance and control plane**: policy, cost, identity, audit across harnesses. Folded into tracks 1 and 5 by default.

## Process

1. This plan, then a check-in (tracks, the Omnigent/Cloudflare question).
2. Fan out six parallel subagents, one per track, each briefed with the filing rule.
4. Before synthesis, re-read research/ and tasks/*/ (PM-agents research is still running) and give the Fable synthesis subagent everything.
5. Synthesis written to `01-synthesis.md` (executive summary, taxonomy, theme/concept/pattern map, fit for unstructured vs task-specific work, open questions); reviewed against this plan.

## Options by dimension (added 2026-10-24)

The project deliverable is a menu of options and key questions, not a single recommended pattern. The taxonomy axes above are the provisional dimensions in [options/DIMENSIONS.md](../../options/DIMENSIONS.md) (harness-ownership, runtime-location, capability-packaging, session-persistence-sharing, work-structure, governance-control-plane). Each track appends options (examples, gives/costs, maturity, evidence-linked source note marked vendor claim / independent / first-party) and concrete key questions (with what could answer each) to the relevant dimension, and proposes new dimensions in its report. The synthesis is organised by dimension, with cross-cutting questions and a "what further work would cover" view.

Update 2026-10-24: dimensions also include USER and PRODUCT choices (which users we serve, which jobs to automate first, target outcome/value, how adoption happens), not only runtime/architecture. Where findings bear on these (e.g. unstructured vs task-specific work, who the user is), add them as dimensions. Key questions stay unranked.
