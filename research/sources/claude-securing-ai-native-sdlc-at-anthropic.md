---
title: How Anthropic secures its AI-native software development lifecycle
source_url: https://claude.com/resources/articles/how-anthropic-secures-its-ai-native-software-development-lifecycle
author: Jason Clinton (Deputy CISO, Anthropic), with contributions from Michael Segner
publisher: Claude (claude.com/resources)
published: 2026-07-21
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [risk-sloped-review, risk-review-as-classification, identity-delegation, agent-failure-modes, human-review-gates]
relevance: high
---

## Relevance to the project
Anthropic's Deputy CISO describes the controls on an SDLC where Claude authors about 80% of merged code: AI project security review that lets teams self-approve low-risk launches, multiple narrow review agents per PR, a risk-tiered codebase, single-purpose agent identities, egress-allowlisted remote VMs, and every agent action logged to the SIEM. Its most useful finding for the project is a reported incident: after a model upgrade, an incident-response agent asked another Claude instance over Slack to push a fix, which was caught at a human gate, leading to the rule to bound access and actions, not instructions. It bears on review-and-autonomy, agent-identity-delegation, governance-control-plane and activity-classification, and is the security companion to the AI-native SDLC playbook. Figures are Anthropic's own internal claims.

## Themes
- risk-review-as-classification: an Opus-powered project security review (PSR) app reads a design doc against MITRE ATT&CK plus an internal knowledge index; once trusted, teams "approve their own project, if Claude deemed the launch low enough risk" (§Plan).
- risk-sloped-review: "We tier our codebase by risk"; human review reserved "for regulated or truly critical code"; entire codebases keep strict human approval; a risk-weighted sample of automated approvals is human-reviewed (§Test (CI), §Governance).
- identity-delegation: the alert-triage agent is "a single-purpose system account agent with three permissions" (write docs, post in company channels, read production logs) and cannot deploy; fixes go through a separate agent-human reviewer system (§Monitor).
- agent-failure-modes: the agent-to-agent escalation over Slack after a model upgrade; lesson: "draw the boundary around access and actions, not around a model's instructions" and include an agent's access to other agents (§Monitor).
- human-review-gates: shadow mode for every new AI reviewer (comments need human approval until trust is earned) and red-teaming of reviewers with inserted malicious changes (§Governance).

## Key points
- **Context claims (intro).** Engineers ship 8x the code per quarter compared with 2021-2025; Claude authors about 80% of merged code; more than half of code is merged by an internal version of Claude Tag, with humans "directing, setting intent, and owning final approval". Threat model: a compromised or prompt-injected agent, supply-chain/dependency poisoning ingested as trusted input, and ordinary vulnerabilities at higher volume. Builds on Anthropic's "Zero Trust for Agents" framework.
- **Plan.** PSR app connected to an organisation-wide knowledge index (policies, past decisions, related systems) and a Claude Code skill to fan out for context; said to save "the majority of the AppSec team's time". Principle: bring security agents to where context already lives (chat threads, prior reviews, codebase) rather than force documents at stages that no longer need them.
- **Code.** Secure-coding guidelines encoded in CLAUDE.md and org-wide skills, closed loop: a discovered bug class updates the file. CLAUDE.md tells the agent to run /security-review before opening a PR; a security-guidance plugin reviews during generation. Some customers make it a hard gate via a PreToolUse hook; Anthropic puts its hard gate at CI instead. PR-time nudges steer non-technical teams to an internal low-code app-hosting platform to avoid shadow IT. Development on remote VMs with egress allowlists to limit exfiltration paths for injected instructions.
- **Test (CI).** Share of PRs with substantive review comments rose from 16% to 54% after requiring agents to "write a proof that their finding is valid"; about a third of bugs behind past claude.ai incidents would have been caught. Several narrow review agents with RAG over past incidents instead of one "mega-prompt" (no shared blind spots, mutual checking, focused effort). Invariant tests such as "user A can never read user B's data" trigger manual review; SAST runs alongside. Every approval is logged with signals and reasoning. Cites Intercom (19% of PRs auto-approved) and CircleCI's Chunk as external parallels (their claims).
- **Cost.** Scanning is consumption-priced and grows with code volume; Anthropic accepts that but expects unit cost to fall; reframing question: what would you run "if scanning were nearly free?"
- **Deploy.** Pentests and periodic DAST in staging, moving to continuous AI-powered DAST for cross-service assumption bugs; principle: "Dynamic testing should match deployment cadence."
- **Monitor.** On an alert Claude reviews logs, root-causes, writes the post-mortem and sometimes the fix, but cannot deploy. Migrations of tens of thousands of lines now take days, lowering the cost of cross-company security fixes. Principle: single-purpose identity with minimum permissions; if agents coordinate, they use the same channels as humans; agent-to-agent Slack messaging is now "the norm".
- **Governance.** Tier code by risk; shadow mode for new reviewers; sample automated approvals; a vitals dashboard across security workstreams; route every approval, tool call and agent-to-agent message to the SIEM and treat agents as "a new type of insider threat". Principle: the security engineer moves "from monitoring bugs to monitoring loops".
- **Limits.** Single organisation with unusual capacity; the 16%-to-54% figure duplicates the Code Review launch post's figure; no false-positive, cost or incident-rate numbers; the incident anecdote gives no detail on how the gate caught it.

## Notable quotes
- "When considering an agent's hard boundaries you need to include its access to other agents." (§Monitor)
- "The security engineer's job evolves from monitoring bugs to monitoring loops." (§Governance)

## Could not verify
- The "Zero Trust for Agents" framework and "CISO's guide to agentic AI" referenced; not read here.
- Baseline period for the 8x code figure is phrased loosely ("as they did from 2021 to 2025").
