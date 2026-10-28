# Themes: research-shared-persistent-agents

Written only by the task research-shared-persistent-agents (2026-10-26). Bullets from the catalogue of agent-to-agent and agent-to-human interactions that shared, persistent agents make possible ([synthesis](../../tasks/research-shared-persistent-agents/01-synthesis.md)). One new slug (human-relay-removed) carries a description; existing slugs reuse the register heading.

## human-relay-removed: The session or channel replaces the person as relay
On a desktop the person is the bus between the agent and everyone else: they paste context in, copy output out, brief the teammate, carry the plan to the next tool and start the morning's work. Shared, persistent designs make the session, the thread or the plan the handoff object, so the relay disappears. It matters because most of the claimed speed of shared agents comes from this one removal, not from a better model.
- [Buzz: a workspace for people and agents](sources/block-eng-buzz.md): early AI use had people copying agent output into Slack and back, "making individuals faster and teams slower"; "a project becomes a conversation with code in it" (research-shared-persistent-agents)
- [We Built Every Employee at Ramp Their Own AI Coworker](sources/x-sebgoddijn-glass-article.md): a support agent hands a ticket session to an engineer instead of re-explaining it (research-shared-persistent-agents)
- [Why we built our background agent (Ramp Inspect)](sources/ramp-builders-why-we-built-background-agent.md): "every session is multiplayer. Send your session to any colleague"; prompts attributed per person (research-shared-persistent-agents)
- [Inside Stripe: how it ships fast (Orbit)](sources/youtube-notmybusiness-inside-stripe-ships-fast.md): one button hands a reviewed seven-step plan, a devbox and instructions to a Minion; engineers run three to seven projects in parallel (first-party marketing) (research-shared-persistent-agents)
- [Claude Code projects, redesigned](sources/claude-code-projects-redesigned.md): a coordinator chat scopes, delegates to parallel cloud threads and assembles, over shared project memory; single owner (research-shared-persistent-agents)
- [Ramp office hours with Anthropic](sources/claude-customers-ramp-office-hours.md): "more Inspect sessions are coming from automations than humans" (Ramp's CTO, no numbers) (research-shared-persistent-agents)

## shared-persistent-sessions: Shared, persistent, multi-user agent sessions
- [Under the River](sources/shopify-engineering-under-the-river.md): the "good thread": one person asks, River posts partial findings, "a second human drops in with a constraint or a redirect", the thread is searchable for the next person; "every engineer's laptop agent is a private artifact that dies with the session" (research-shared-persistent-agents)
- [River floods Shopify (chart)](sources/x-tobi-river-floods-shopify-chart.md): the only published multiplayer metric: "wrote in the same thread" links 61,680 (Mar 2026) to 171,853 (Sep 2026); volume, not outcome (research-shared-persistent-agents)
- [Claude Code on the web (cloud sessions)](sources/anthropic-claude-code-cloud-sessions.md): the vendor product shares a snapshot, "their view doesn't update in real time"; handoff to the terminal is a one-way fork (research-shared-persistent-agents)
- [Coding is no longer the constraint (Spotify)](sources/spotify-engineering-coding-no-longer-constraint.md): Honk v2 adds multiplayer sessions and team projects; access model not given (research-shared-persistent-agents)
- [Open-Inspect](sources/github-open-inspect-background-agents.md): a per-session Durable Object with presence and attributed prompts; team-visibility enforcement defaults to "shadow"; credentials cached in snapshots (research-shared-persistent-agents)
- [Scaling Managed Agents](sources/anthropic-engineering-scaling-managed-agents.md): the session as a durable event log outside harness and sandbox; a crashed harness resumes with the session id, so the session outlives its runtime (research-shared-persistent-agents)
- [Claude Tag CI/CD first responder](sources/claude-tag-ci-cd-first-responder.md): several engineers steer one investigation "in multi-player mode" in the on-call channel (research-shared-persistent-agents)
- [Multi-User Large Language Model Agents](sources/arxiv-multi-user-llm-agents.md): one agent serving several users loses priority stability under conflict (Haiku 4.5 0.86 to 0.62) and leaks more over turns; simulated, not field (research-shared-persistent-agents)
- [Multiplayer AI Manifesto](sources/fullstack-multiplayer-ai-manifesto.md): argues teammates should join one live session with shared context; concedes no platform does it yet (vendor) (research-shared-persistent-agents)
- [Scheduled tasks (Codex automations docs)](sources/openai-codex-scheduled-tasks-docs.md): thread-scoped tasks return to the same chat with context; results land in a "Scheduled" inbox (research-shared-persistent-agents)

## org-learning-loop: One person's win becomes everyone's baseline
- [Introducing Glass: learn things once](sources/x-eglyman-introducing-glass-learn-things-once.md): 323 employees, 6,500+ edits to what Glass knows; Finance's "UK customers" correction (vendor claim, counts only) (research-shared-persistent-agents)
- [Learning on the Shop floor](sources/x-tobi-learning-on-the-shop-floor.md): merge rate 36% to 77% in two months credited to people writing down what River should have known; one team's skill "reused by twelve other teams" (CEO claim, merge rate undefined) (research-shared-persistent-agents)
- [How Anthropic employees use Claude Tag](sources/claude-how-anthropic-uses-claude-tag.md): a counsel's correction becomes a channel's standing instruction; a Friday routine proposes instruction updates for approval: the curate step (research-shared-persistent-agents)
- [Claude Tag CI/CD first responder](sources/claude-tag-ci-cd-first-responder.md): every resolved incident appended to lessons.md and read first next time; recurring patterns promoted into the skill (research-shared-persistent-agents)
- [Managed Agents: dreaming, outcomes, orchestration](sources/claude-managed-agents-dreaming-outcomes.md): dreaming "pulls shared learnings across agents" with optional human review; Harvey's "6x" has no baseline (research-shared-persistent-agents)
- [Vedder: Spotify's context layer](sources/spotify-engineering-vedder-context-layer.md): counter-evidence for mined corrections: curators rejected 87.5% of generated examples as noise (research-shared-persistent-agents)
- [Bugbot now self-improves with learned rules](sources/cursor-bugbot-learning.md): PR reactions, replies and human review comments become candidate rules, auto-promoted or disabled; 44k+ rules across 110k+ repos (vendor) (research-shared-persistent-agents)
- [Agent Workflow Memory](sources/arxiv-wang-agent-workflow-memory.md): workflows induced from past trajectories lift relative success 24.6% (Mind2Web) and 51.1% (WebArena) (research-shared-persistent-agents)

## identity-delegation: Identity and delegation (on-behalf-of)
- [Agent identity: the access model behind Claude Tag](sources/claude-agent-identity-access-model.md): the two cases "act as the user" cannot cover: the task runs after the requester logs off, and several people steer one agent; "what can this agent do in this compartment?" (research-shared-persistent-agents)
- [Personal connectors for Claude Tag](sources/claude-tag-personal-connectors.md): the hybrid: unattended work under the channel identity, person-initiated reads on the requester's own connectors, each logged under the matching account; "personal connectors don't run unattended" (research-shared-persistent-agents)
- [Why we built our background agent (Ramp Inspect)](sources/ramp-builders-why-we-built-background-agent.md): PRs open with the requester's GitHub token so nobody approves their own agent's work: separation of duties by identity (research-shared-persistent-agents)
- [Buzz: a workspace for people and agents](sources/block-eng-buzz.md): each agent has its own keypair and an owner-signed, scoped authorisation; revoking the agent does not touch the human identity (research-shared-persistent-agents)
- [Cursor forum: Team Followups act on behalf of the creator](sources/cursor-forum-team-followups-act-on-behalf.md): a teammate's follow-up runs on the creator's OAuth tokens, "documented and intentional" per staff (research-shared-persistent-agents)
- [Claude Code scheduled tasks](sources/anthropic-claude-code-scheduled-tasks.md): tasks "belong to your individual claude.ai account", are not shared with teammates, and act as the creating user (research-shared-persistent-agents)
- [Agent identity (Ramp for Agents developer guide)](sources/ramp-agents-identity-guide.md): on-behalf-of agents run as the OAuth user; standalone agents get their own credentials and an accountable owner (early access) (research-shared-persistent-agents)
- [GitHub MCP Exploited](sources/invariantlabs-github-mcp-toxic-agent-flow.md): a public issue hijacks an agent into leaking private repos using its user's authority; mitigation is one repo per session (research-shared-persistent-agents)
- [Scheduled tasks (Codex automations docs)](sources/openai-codex-scheduled-tasks-docs.md): Team Tasks run in the cloud through a team service account (research-shared-persistent-agents)

## public-by-default-agent-work: Public-by-default agent work and its costs
- [River's reaction to the Shop floor post](sources/x-tobi-river-reaction-to-shop-floor-post.md): "Some questions that would have been asked in a DM just don't get asked"; public-only as "an honesty pressure"; written by the agent (research-shared-persistent-agents)
- [The transparency paradox (Bernstein, ASQ 2012)](sources/asq-bernstein-transparency-paradox.md): broad visibility bred hiding and a "show" for observers; privacy zones raised defect-free output 10-15% for five months; one factory, 2009 (independent) (research-shared-persistent-agents)
- [Building effective human-agent teams (Slack CPO)](sources/claude-slack-human-agent-teams.md): "Agents can only learn from what they can see"; "a private channel is a blind spot"; psychological safety, not secrecy, sends work to DMs (research-shared-persistent-agents)
- [Tenable on the Claude Tag access model](sources/tenable-claude-tag-slack-access-model.md): channel membership becomes the IAM boundary; new members see prior scrollback (independent) (research-shared-persistent-agents)
- [How I AI: Stripe Minions (Kaliski)](sources/howiai-stripe-minions-kaliski.md): a public "robots" channel 76 people follow; "we pair prompt"; open-by-default chosen per person for coding runs while Kai sessions stay private (research-shared-persistent-agents)
- [Shopify River and agent context (Magica)](sources/magica-shopify-river-agent-context-cost.md): no like-for-like comparison of shared versus private agents has been published (research-shared-persistent-agents)
- [Don't Disturb Me](sources/arxiv-wessel-dont-disturb-me-bots.md): noise is the central harm of bots in PRs; information overload disrupts communication and workflow (independent, 2021) (research-shared-persistent-agents)
- [Meta-Analysis of Digital Surveillance of Workers](sources/msr-ravid-digital-surveillance-meta-analysis.md): monitoring is stressful whatever its form; only transparent, purposeful, less invasive monitoring improves attitudes (independent) (research-shared-persistent-agents)

## remote-agent-invocation: Remote agent invocation
- [Remote Dev (Shopify)](sources/shopify-engineering-remote-dev.md): overnight bug fixes on a pool of warm remote Macs; tasks start from Slack; River records before-and-after video to prove its work (research-shared-persistent-agents)
- [How River takes security work from fix to merge](sources/shopify-engineering-river-vulnerability-remediation.md): River reads a ledger and opens four threads for 35 findings within a minute, then runs check back; draft-only under human merge authority (research-shared-persistent-agents)
- [Cowork on web and mobile](sources/claude-cowork-web-mobile-handoff.md): scheduled tasks "run with no device online"; when Claude reaches "a call only you can make, it asks" on the phone (research-shared-persistent-agents)
- [Claude Tag CI/CD first responder](sources/claude-tag-ci-cd-first-responder.md): a daily "ci-weather" report compiled unattended from incident channels, build metrics and deploy lag; median 14 minutes to first evidence-grounded analysis (unverified) (research-shared-persistent-agents)
- [Beyond the CLI: Airbnb's AirChat](sources/dx-airbnb-beyond-the-cli-airchat.md): AirChat Remote takes triggers from Slack, on-call channels and failing PRs (research-shared-persistent-agents)
- [Build agents that run automatically (Cursor Automations)](sources/cursor-blog-automations.md): schedule, Slack, Linear, GitHub, PagerDuty and webhook triggers; each run in a fresh sandbox with a memory tool (vendor) (research-shared-persistent-agents)
- [Seer: hand off to a coding agent](sources/sentry-seer-coding-agent-handoff.md): Seer passes root cause and solution as a structured prompt to Cursor, Claude Code or Copilot; stopping point configurable (research-shared-persistent-agents)

## human-review-gates: Human review gates on agent output
- [Code Review for Claude Code, GA](sources/claude-code-review-ga.md): parallel find, verify, rank agents on every PR; "won't approve PRs"; substantive comments on 16% to 54% of PRs; under 1% marked incorrect; $15-25 per review (first-party) (research-shared-persistent-agents)
- [Honk part 3: feedback loops](sources/spotify-engineering-honk-part-3-feedback-loops.md): an LLM judge compares the diff with the original prompt and vetoes about a quarter of unattended sessions, mostly scope creep (research-shared-persistent-agents)
- [Intercom: AI approving pull requests](sources/intercom-ai-approving-pull-requests.md): about 19% of PRs auto-approved by risk and size; the shipping engineer stays accountable; revert rates self-reported (research-shared-persistent-agents)
- [Configuring agents in Buzz](sources/block-eng-configuring-agents-in-buzz.md): a reviewer agent deliberately from a different model family; "respond-to" sets who may direct an agent (research-shared-persistent-agents)
- [How River takes security work from fix to merge](sources/shopify-engineering-river-vulnerability-remediation.md): "hand off the decision, not the investigation": the current head, what it tried, evidence, and "the smallest question that an owner has to answer" (research-shared-persistent-agents)
- [Automated Code Review In Practice](sources/arxiv-cihan-automated-code-review-in-practice.md): 73.8% of LLM review comments resolved, but PR closure time rose from 5h52m to 8h20m (independent) (research-shared-persistent-agents)
- [AGENTOPS01-BP02 handoff and escalation (AWS)](sources/aws-agentic-lens-handoff-escalation.md): separate agent-to-human triggers (confidence, stakes, retries) from routing; mixing them causes fatigue or risk (research-shared-persistent-agents)
- [Seer: hand off to a coding agent](sources/sentry-seer-coding-agent-handoff.md): "Seer never merges on its own"; start at "Stop after Solution" to build trust (research-shared-persistent-agents)

## verification-capacity-gap: Verification capacity is the new limit
- [The Knowledge Project: Tobi Lütke on AI agents](sources/fs-knowledge-project-tobi-lutke-ai-agents.md): "slop grenades": unread agent PRs pushed onto colleagues to review (research-shared-persistent-agents)
- [Inside Shopify's AI-first engineering playbook (BVP)](sources/bvp-inside-shopifys-ai-first-engineering-playbook.md): "We still require a human PR reviewer, which is now becoming a big bottleneck" (research-shared-persistent-agents)
- [Why do multi-agent LLM systems fail? (MAST)](sources/arxiv-why-multi-agent-llm-systems-fail.md): 1,642 traces: about 32% inter-agent misalignment, 24% verification failures; a verification step +15.6% task success (independent) (research-shared-persistent-agents)
- [The AI Productivity Paradox Report 2025](sources/faros-ai-productivity-paradox-2025.md): 98% more PRs merged and 91% longer review time on high-AI teams; no company-level gain (vendor telemetry, 10,000 developers) (research-shared-persistent-agents)
- [Rise of the Overnight Agents](sources/greptile-rise-of-overnight-agents.md): fully agent-authored merged PRs rose from 0.86% to 27.6% (Feb 2025 to Apr 2026); reverts per 1,000 PRs lower than human for Codex and Claude, higher for Cursor background agents and Devin (vendor) (research-shared-persistent-agents)
- [On the Use of Agentic Coding](sources/arxiv-watanabe-agentic-coding-prs.md): 83.8% of 567 Claude Code PRs merged; 45.1% of those needed human revision, mostly for project standards (independent) (research-shared-persistent-agents)

## skill-improvement-loops: How skills and agent instructions get better
- [How Intercom uses Claude Code today](sources/ideas-fin-how-we-use-claude-code-today.md): a SessionEnd hook classifies each transcript's gaps (missing skill, missing tool, repeated failure, wrong info) and opens a pre-filled GitHub issue: traces to standards (research-shared-persistent-agents)
- [How I AI: Stripe Kai (Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): telemetry sorts about 2,000 skills into about 50 used daily, 100-150 by sub-org and a long tail; a pipeline says which to promote into the default context (research-shared-persistent-agents)
- [Remote Dev (Shopify)](sources/shopify-engineering-remote-dev.md): the "Jev" classifier tags every mobile River conversation by outcome and feeds failures to an LLM that proposes improvements (research-shared-persistent-agents)
- [The Knowledge Project: Tobi Lütke on AI agents](sources/fs-knowledge-project-tobi-lutke-ai-agents.md): River's repeated failure to pick unit tests became an ML test-selection model, saving about 30 minutes per task; nightly "dreaming" rewrites skill files (research-shared-persistent-agents)
- [Building Laminar](sources/ramp-builders-building-laminar.md): a bespoke session-debug UI because "building great agents requires you to read the traces" (research-shared-persistent-agents)
- [Automating SKILL.md Generation via Interaction Trajectory Mining](sources/arxiv-hao-skillmd-trajectory-mining.md): mined skills are readable but don't transfer; "readability does not imply transfer" (research-shared-persistent-agents)
- [Bugbot now self-improves with learned rules](sources/cursor-bugbot-learning.md): online rule promotion from live review feedback replaced offline-only experiments (research-shared-persistent-agents)

## agent-stewardship: Every deployed agent needs a human steward
- [Building effective human-agent teams (Slack CPO)](sources/claude-slack-human-agent-teams.md): retire an agent if people cannot say what it is for; a session that outlives its creator needs a named owner (research-shared-persistent-agents)
- [Agent identity: the access model behind Claude Tag](sources/claude-agent-identity-access-model.md): revoking the agent's identity ends access everywhere, "easier than auditing actions across user accounts" (research-shared-persistent-agents)
- [Owners, sponsors, and managers (Entra Agent ID)](sources/microsoft-entra-agent-owners-sponsors.md): a business sponsor is mandatory per agent, groups allowed, succession on departure required; Microsoft sources conflict on the default transfer (research-shared-persistent-agents)
- [Agent identity (Ramp)](sources/ramp-agents-identity-guide.md): standalone agents must have an active human owner in the business (research-shared-persistent-agents)

## risk-sloped-review: Human review sloped to risk
- [Build agents that run automatically (Cursor Automations)](sources/cursor-blog-automations.md): "agentic codeowners" auto-approves low-risk PRs and routes higher-risk ones to two reviewers chosen by contribution history (vendor) (research-shared-persistent-agents)

## agent-failure-modes: Recurring agent failure modes in PM work
- [AGENTOPS01-BP02 (AWS)](sources/aws-agentic-lens-handoff-escalation.md): agent-to-agent deadlocks are silent; "a deadlock that requires a human to notice lasts until someone notices" (research-shared-persistent-agents)
- [Rise of the Overnight Agents](sources/greptile-rise-of-overnight-agents.md): failure types differ by agent (Cursor background agents n+1 at 3.45x human, Claude IDOR at 1.75x) (vendor) (research-shared-persistent-agents)

## cost-control-routing: Cost metering and model routing built into the harness
- [The Coding Agent Economy](sources/requesty-coding-agent-economy.md): Claude Code mean $108, median $23, P95 $291 per active user per month; spend is tail-driven (vendor) (research-shared-persistent-agents)

## vendor-claims-vs-independent-evidence: Vendor claims dominate; independent evidence is scarce
- [Bugbot now self-improves with learned rules](sources/cursor-bugbot-learning.md): the competitor resolution-rate table was run by Cursor's own LLM judge; contrast the independent 73.8% resolved with slower closure (research-shared-persistent-agents)

