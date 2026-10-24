# Track 5: Deployed, shared, multi-user, persistent sessions

Date: 2026-10-24. Filed by research-agent-runtime-patterns-taxonomy. Plan: [00-research-plan.md](00-research-plan.md). 26 new source notes, listed at the end. Omnigent and Cloudflare OS are Track 1's; only cross-referenced here. Evidence is labelled **first-party** (vendor's own docs or engineering post), **vendor claim** (promotional or about a customer), **independent**, **anecdote** (forum, blog, second-hand).

## 1. Summary

- "Persistent and shared" is not one pattern. The products in the field split on five separable decisions: where the session runs, what makes it durable, who the agent acts as, how people join it, and how work is handed on. Each has more than one live answer (see section 3).
- Almost every account of **teams running shared agents at scale is first-party** (Ramp Inspect, Stripe Minions). Independent evidence found is mainly about **failures and design critiques**: Answer.AI on Devin (3 of 20 tasks succeeded, Jan 2025), Tenable on Claude Tag's access model, Wavect on Inspect, Cursor forum threads, press on Replit and Kiro. Absence of independent success reports is itself a finding, not proof they do not exist.
- The sharpest design divergence is **identity**: Cursor runs a shared agent with the creator's tokens (teammates can steer it; staff call this intended), Codex runs as the requester, Claude Tag as a service account with channel-scoped access bundles, Copilot as agent-with-human-co-author under a separate approver. Each has a documented or reported leakage mode.
- **Handoff is asymmetric** in every shipped product examined (Claude: cloud to terminal only, as a fork; Cursor: local to cloud works, cloud-origin to local often does not). Sessions expire; transcripts are deleted by default locally (30 days in Claude Code) and held vendor-side in cloud.
- **Scheduled/event-driven** cloud agents exist as vendor products but are **personal, not team-shared** in Claude's case; Glass's laptop-as-server schedule is the weakest variant. Durable execution tooling (Temporal, Cloudflare, LangGraph, Inngest) is mature as infrastructure, but an independent comparison warns model calls outside step boundaries are re-paid and durability does not give idempotency.

## 2. Evidence by pattern

| Pattern | Examples | Evidence | Source notes |
|---|---|---|---|
| Vendor cloud session, single owner, share-by-link | Claude Code on the web, Codex cloud, Warp Oz | first-party docs | [claude cloud](../../research/sources/anthropic-claude-code-cloud-sessions.md), [codex](../../research/sources/openai-codex-cloud-slack.md), [warp](../../research/sources/warp-oz-cloud-agents.md) |
| Live multiplayer on per-session control plane | Ramp Inspect, Open-Inspect | vendor claim, first-party README, independent critique | [modal](../../research/sources/modal-ramp-inspect-background-agent.md), [open-inspect](../../research/sources/github-open-inspect-background-agents.md), [wavect](../../research/sources/wavect-ramp-inspect-architecture.md) |
| Durable session log, disposable harness | Claude Managed Agents | first-party | [post](../../research/sources/anthropic-engineering-scaling-managed-agents.md) |
| One-shot isolated runs, human at the PR | Stripe Minions | first-party | [stripe](../../research/sources/stripe-minions-part-2.md) |
| Scheduled / API / webhook triggered | Claude scheduled tasks, Warp, Cloudflare alarms | first-party | [routines](../../research/sources/anthropic-claude-code-scheduled-tasks.md), [cloudflare](../../research/sources/cloudflare-agents-long-running-agents.md) |
| Customer-hosted runners, vendor control plane | Claude self-hosted (beta) | first-party | [self-hosted](../../research/sources/anthropic-self-hosted-environments.md) |
| Chat-native shared agents | Claude Tag, Codex in Slack, Cursor, Devin | first-party + independent + anecdote | [tag](../../research/sources/anthropic-claude-tag-agent-identity.md), [tenable](../../research/sources/tenable-claude-tag-slack-access-model.md), [cursor](../../research/sources/cursor-forum-team-followups-act-on-behalf.md) |
| Durable execution under agents | Temporal, Inngest, DBOS, LangGraph, Durable Objects | vendor claim, first-party, independent | [temporal](../../research/sources/temporal-openai-agents-sdk-integration.md), [langgraph](../../research/sources/langchain-langgraph-persistence.md), [hackernoon](../../research/sources/hackernoon-durable-execution-compared.md) |

## 3. Patterns on the plan's axes

**Axis 1, where the runtime lives.** Vendor cloud VM (Claude, Codex, Cursor, Devin, Warp hosted); customer-hosted runners with a vendor control plane (Claude self-hosted beta: runner polls outbound, no inbound; conversation still goes to Anthropic; owner-locked runners so code never mixes between owners; Warp self-hosted workers); edge durable objects (Cloudflare Agents; Open-Inspect's control plane); org devbox fleet (Stripe). Limits recorded: Claude cloud needs GitHub for clone/PR, is unavailable under ZDR/HIPAA/CMEK, and fails for orgs with IP allowlisting without an exemption.

**Axis 2/3, who owns the loop and coupling.** Most shared-session products couple the loop to their own harness. Exceptions: Open-Inspect's sandbox runs OpenCode or the Claude Agent SDK behind a Bridge; Anthropic frames Managed Agents as a "meta-harness" with replaceable harness behind stable interfaces. Cross-reference Track 1 (Omnigent, Cloudflare OS) and Track 2.

**Axis 5, invocation.** Slack/Linear/GitHub mentions create cloud tasks (Codex, Cursor, Devin, Claude Tag); HTTP `/fire` endpoint with per-task bearer token (Claude); cron; GitHub events; CLI follow-up into an existing cloud session from any machine. Practical notes: GitHub webhook events past hourly caps are dropped, GitHub-connection lapses silently skip runs for up to 72 hours, and a green run status "does not mean the work succeeded".

**Axis 6, session locality, sharing, persistence.**
- *Ephemeral-private:* local sessions; Claude Code deletes transcripts after 30 days by default ([ITdaily](../../research/sources/itdaily-claude-code-30-day-transcript-deletion.md), independent), keyed on file modification time.
- *Resumable-private, single-owner cloud:* history restored on reopen; running shell commands, subagents and session-scoped schedules are not.
- *Shared snapshot:* Claude Team visibility; link recipients do not get a live view.
- *Shared-live:* Inspect/Open-Inspect (presence, authored prompts), Warp (attach and steer).
- *Persistent-deployed:* Cloudflare durable agents ("durable identities, not always-on processes"), Managed Agents session log.
- *Team memory:* little independent evidence. LangGraph separates thread checkpoints from cross-thread stores; Unblocked's argument that stateless sessions repeat mistakes is a vendor pitch with unverified statistics. Ties to existing theme memory-architecture and to Track 4 skills as the main sharing mechanism.

**Axis 7, governance.** See identity comparison next.

### Identity and access: who is the agent acting as

| Product | Acts as | Who can steer | Reported or documented leakage mode | Evidence |
|---|---|---|---|---|
| Cursor cloud agent (Team Followups on) | Creator's OAuth tokens | Any teammate via Slack thread or web link | Teammate prompts run as creator; claimed deletable origin prompt removes audit trail; staff: "documented and intentional", mitigate with creator-only or service-accounts-only | anecdote + staff reply |
| Codex in Slack | Requester's account | Same account only (other account starts new task) | Channel readers see results; personal environments excluded | first-party |
| Claude Tag (channels) | Admin-provisioned service account, scoped access bundles | Anyone in the channel | Channel membership becomes IAM boundary; broad bundles on easy-to-join channels (Tenable) | first-party + independent |
| Claude scheduled tasks | Creating user's connected identity | Owner only; not shared | Actions "appear as you" | first-party |
| Copilot cloud agent | Agent with requester as co-author | Write-access users; requester cannot approve own PR | Firewall covers only agent-started processes, not MCP servers | first-party |
| Stripe minions | Sandboxed QA devbox, no human credentials | Engineer who launched it | Bounded by environment; humans review every PR | first-party |
| Open-Inspect | Shared GitHub App installation | Team/workspace visibility | Visibility enforcement default `shadow`; revoked grants do not revoke issued tokens; no personal-permission check at session creation | first-party README |

## 4. Failure modes (what is documented, how well)

- **Permission inheritance causing damage:** Kiro reported (FT via The Decoder, 2026-02-20; Amazon disputes, calls it user access control error) as operator-level permissions with no second approver. [independent, contested](../../research/sources/the-decoder-aws-kiro-outage.md).
- **Ignored freeze instruction and false recovery claims:** Replit/SaaStr 2025-07, reported by affected user and press; fix was architectural (dev/prod split, staging). [independent](../../research/sources/theregister-replit-saastr-response.md).
- **Stuck runs and unreliable autonomy:** Answer.AI Devin test, 3 successes, 14 failures, 3 inconclusive of 20; looped, persisted on impossible tasks. Jan 2025, product has changed. [independent](../../research/sources/answerai-month-with-devin.md).
- **Runaway cost:** a $47K eleven-day agent loop is **second-hand and unverified**, from an author who sells a related tool. [anecdote](../../research/sources/devto-47k-agent-loop.md). Claude's documented controls are rate limits, not per-run budgets.
- **State drift/expiry:** Claude environments expire and lose background work; snapshot-based sandboxes (Inspect, Cursor) risk stale snapshots (Wavect names this as a risk, not an observed incident).
- **Handoff gaps:** [Cursor cloud-to-local limitation](../../research/sources/cursor-forum-cloud-to-local-handoff.md).
- **Not found:** an independent post-mortem of a multi-user shared agent session going wrong, beyond the Cursor forum identity issue. Routes tried: product docs, forum threads, press, HN search, security vendors, incident write-ups.

## 5. Comparison table (maturity and trade-offs)

| Pattern | Maturity | Gives | Costs |
|---|---|---|---|
| Vendor cloud single-owner | early-adopter | no ops, laptop-independent | not live-shared, one-way handoff, GitHub-bound |
| Live multiplayer per-session control plane | early-adopter | cross-role collaboration | single-tenant trust, enforcement gaps, unclear cost |
| Durable session log | emerging | crash recovery | vendor-hosted, multi-user unstated |
| One-shot isolated runs | early-adopter | contained blast radius | not interactive; needs strong tests and dev infra |
| Scheduled/event cloud runs | early-adopter | unattended work | personal ownership, silent skips |
| Customer-hosted runners | emerging | data/network control | fleet ops, vendor still holds transcript |
| Chat-native shared agent | emerging | where teams already work | identity and channel-hygiene risks |
| Durable-execution engine | early-adopter | retry, replay | idempotency, determinism, re-paid model calls |

## 6. Options by dimension

Added to [options/DIMENSIONS.md](../../options/DIMENSIONS.md) (all end with key questions, none ranks a winner):
- [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-and-sharing): six options and five key questions added.
- [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-permissions-cost-identity-audit): six identity/blast-radius/cost options and four key questions.
- [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives): four options and three key questions.
- New: [session-handoff-portability](../../options/DIMENSIONS.md#session-handoff-portability-handing-a-session-between-people-devices-and-harnesses), [durability-substrate](../../options/DIMENSIONS.md#durability-substrate-how-persistence-and-recovery-are-implemented), [shared-agent-users-and-jobs](../../options/DIMENSIONS.md#shared-agent-users-and-jobs-which-users-and-jobs-a-shared-persistent-agent-serves-first).
- One cross-cutting question added (agent identity as product decision).

**Proposed structural changes (for the director):** (a) split identity out of governance-control-plane into its own dimension, `agent-identity-delegation`; (b) merge session-handoff-portability into session-persistence-sharing if fewer dimensions are preferred; (c) merge shared-agent-users-and-jobs into the user/product dimensions `target-user` and `target-outcome` added by another agent, keeping its options as examples; (d) the Contents list does not yet include my three new dimensions (director maintains it).

## 7. Open questions for Geoff

1. Which jobs do you want shared or unattended first: interactive co-working, recurring digests, or chat requests? The infrastructure differs sharply.
2. Which identity behaviour is acceptable for a shared agent: requester, creator-tokens, or service account? Needs a policy owner.
3. Is the target setting regulated (transcript retention, data residency)? It decides vendor cloud vs customer-hosted vs self-built.
4. Do you want us to chase non-Ramp, non-Stripe adopters (interviews) since independent success evidence is nearly absent?
5. For Glass-style scheduled work, is laptop-dependence a dealbreaker, given vendor cloud scheduled tasks are personal and not team-shared?

## 8. Caveats

Several vendor pages (Claude, Codex, Cursor, Warp, Devin) change monthly; statements are as of 2026-10-24. Cursor and Copilot facts partly come from search snippets and are marked in the notes. Not read: Devin and Cursor docs directly, the FT original, Cloudflare Workflows and Agents Week posts, Cloudflare OS, Omnigent (Track 1), Notion agent permissions (existing notes only), Slack-native agents beyond those listed, Temporal customer case studies.

## Source notes filed (all under ../../research/sources/)

anthropic-claude-code-cloud-sessions, anthropic-claude-code-scheduled-tasks, anthropic-self-hosted-environments, anthropic-engineering-scaling-managed-agents, anthropic-claude-tag-agent-identity, tenable-claude-tag-slack-access-model, modal-ramp-inspect-background-agent, wavect-ramp-inspect-architecture, github-open-inspect-background-agents, cursor-forum-team-followups-act-on-behalf, cursor-forum-cloud-to-local-handoff, openai-codex-cloud-slack, github-copilot-cloud-agent-risks, stripe-minions-part-2, cloudflare-agents-long-running-agents, temporal-openai-agents-sdk-integration, langchain-langgraph-persistence, hackernoon-durable-execution-compared, devto-47k-agent-loop, thoughtworks-radar-agent-trace, unblocked-agent-doom-loop, answerai-month-with-devin, theregister-replit-saastr-response, the-decoder-aws-kiro-outage, itdaily-claude-code-30-day-transcript-deletion, warp-oz-cloud-agents.
