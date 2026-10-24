# Track 3: general harnesses calling powerful deployed agents

Date: 2026-10-24. Filed by: research-agent-runtime-patterns-taxonomy (Track 3). Plan: [00-research-plan.md](00-research-plan.md). Not a recommendation: this is a menu with the questions that decide among options.

Evidence labels: first-party (a spec or doc by the thing's owner describing itself), vendor claim, independent, anecdote. Source notes: `../../research/sources/<slug>.md` (linked below).

## 1. Summary (what the evidence supports)

1. **There are about eight distinct ways for a primary harness (Claude Code, Codex) to reach a more powerful agent that runs elsewhere**, and only some need a protocol. The most-used today need none: vendor cloud sessions (`claude --cloud`, Codex cloud, Copilot cloud agent, Jules, Cursor) and CI-triggered headless runs (Claude Code GitHub Actions). See the table in section 3.
2. **MCP is the only protocol with demonstrated, documented examples of a deployed task agent reached from a general harness** (Glean agents-as-tools, Sentry MCP with Seer). Both are vendor docs; no independent account of their quality, latency or cost was found despite several query routes. Their own restrictions are the finding: read-only, no human-in-the-loop, aim for about 30 seconds, because hosts time out at 30 to 60 seconds.
3. **MCP has just changed in ways that matter for this**: the 2026-07-28 revision makes MCP stateless, moves Tasks (durable handle, polling, `input_required`) into an extension, replaces server-initiated elicitation/sampling with input-required results, and deprecates Sampling. So a served agent must bring its own model; long jobs have a standard path; support depends on the host (Claude Code has MCP Tasks in public beta; `claude -p` does not wait for them).
4. **A2A is a real, stable spec (v1.0, March 2026, Linux Foundation) with real platform support (Copilot Studio as client, AWS AgentCore as host, Gemini CLI), but the honest evidence of use is thin.** Adoption evidence is organisation counts (150+ supporters) and platform integrations, no named end-user production deployment; independent commentary and an Ask HN thread are mixed to sceptical. We found no native A2A client in Claude Code or Codex (only community bridges, one marked not production ready). Treat A2A as "specified and platform-supported, production use unproven".
5. **Vendors are consolidating on their own APIs rather than protocols for delegation**: Cursor Cloud Agents API (public beta), Jules API (v1alpha), Anthropic Managed Agents (beta), and OpenAI **removed** `codex mcp-server` in favour of an experimental, non-MCP app server. So "wrap a coding harness as an MCP agent" is an unstable route for Codex, and OpenAI's own Claude Code plugin (`codex-plugin-cc`) uses the app server locally.
6. **Identity on behalf of the user is the least settled piece.** MCP's authorization spec forbids token passthrough (audience-bound tokens), so an agent acting downstream as the user needs token exchange, a vault or the Enterprise-Managed Authorization extension (listed Stable; mechanism not read). A2A leaves credential issuance and delegation to implementers. Vendor cloud sessions keep credentials in a proxy outside the sandbox but act with the agent's, not necessarily the user's, authority.
7. **Independent evidence on how well delegated agents work is scarce and dated.** The best is Answer.AI's January 2025 trial of Devin (3 of 20 tasks succeeded; success unpredictable; infeasible tasks pursued, not flagged) and Simon Willison's running log (PR-merge rates by tool, Jules tests failing, prompt-injection cautions). Nothing comparable was found for current Codex cloud, Claude Code web, or any MCP-served agent.

## 2. Patterns on the plan's axes

Axis numbers follow the plan's draft axes.

| Pattern | 1 Runtime | 2 Harness owner | 3 Coupling | 4 Packaging | 5 Invocation | 6 Session | 7 Governance |
|---|---|---|---|---|---|---|---|
| Vendor cloud session from CLI | Vendor cloud (or self-hosted env) | Vendor product | Tied to one vendor | Task prompt plus repo's skills/subagents | Human-triggered handoff; follow-up by id | Resumable, team-visible link | Plan limits; GitHub proxy; excludes ZDR/HIPAA/CMEK |
| Background-agent API (Cursor, Jules, Managed Agents) | Vendor cloud | Vendor | Per-vendor API | Agent definition or prompt | Remote call, SSE/polling | Durable agent with runs | API/service-account keys |
| Agent behind sync MCP | Org or vendor service | The service owner | Portable across MCP hosts | Deployed agent as a tool | Remote call within host timeout | Stateless per call | Per-server OAuth |
| Agent behind MCP + Tasks | Org or vendor service | Service owner | Portable where host supports extension | Deployed agent with durable handle | Remote call, poll, input_required | Task survives disconnect | Per-server OAuth; trace context |
| A2A agent | Any (AgentCore, Cloud Run, own) | Service owner | Vendor-neutral on paper; few harness clients | Agent Card with skills | Peer/remote delegation, streaming or push | Task and context ids | Card-declared schemes; delegation unspecified |
| CI/event-triggered task agent | CI runner | Vendor harness headless (or OpenCode) | Harness-tied, repo-versioned | Plugin skill as the prompt | Event/scheduled | Ephemeral | OIDC federation, turn caps, write-access check |
| Self-hosted Agent SDK service | Org container/Modal/K8s | Vendor SDK in own service | SDK-tied | Whatever the service exposes | Any of the above on top | Ephemeral, long-running or hybrid with SessionStore | Own gateway, egress proxy, per-tenant isolation |
| Cross-harness plugin | Local | Both vendors | Plugin per host | Plugin plus subagent | Human or hook-triggered | Local plus resumable Codex thread | Local auth, review-gate loop risk |

## 3. Comparison: protocols and products

Maturity: mainstream, early-adopter, emerging. "Independent evidence" means evidence not authored by the vendor.

| Item | What it is | Status (as read, Oct 2026) | Task/long-running | Auth | Independent evidence of real use | Source notes |
|---|---|---|---|---|---|---|
| MCP sync tool backed by an agent | Hosted MCP server fronting an agent | Glean, Sentry shipped; emerging | No: host timeout ~30-60s | Per-server OAuth | None found for quality; Willison argues MCP tools are easier to audit than shell | [Glean](../../research/sources/glean-agents-as-mcp-tools.md), [Sentry](../../research/sources/sentry-mcp-server-seer.md), [Willison](../../research/sources/simonwillison-stateless-mcp.md) |
| MCP Tasks extension | Durable task handle, poll, `input_required` | Extension in 2026-07-28; Claude Code public beta | Yes | Same as MCP | None | [Tasks](../../research/sources/mcp-ext-tasks-long-running-operations.md), [changelog](../../research/sources/mcp-spec-2026-07-28-key-changes.md), [Claude Code MCP](../../research/sources/anthropic-claude-code-mcp-tasks-oauth.md) |
| A2A v1.0 | Agent Card, tasks, streaming/push | Stable spec; emerging adoption | Yes (task lifecycle) | API key, OAuth2, OIDC, mTLS; delegation unspecified | Sceptical analysis; HN mixed | [Spec](../../research/sources/a2a-project-specification-v1.md), [A2A vs MCP](../../research/sources/a2a-project-a2a-and-mcp.md), [LF](../../research/sources/linuxfoundation-a2a-one-year-press-release.md), [Google](../../research/sources/googleopensource-a2a-anniversary.md), [Glukhov](../../research/sources/glukhov-a2a-adoption-hype-reality.md), [HN](../../research/sources/hn-ask-is-anyone-using-a2a.md), [AgentCore](../../research/sources/aws-bedrock-agentcore-runtime-a2a.md), [Copilot Studio](../../research/sources/microsoft-copilot-studio-a2a.md) |
| ACP (IBM) | Agent Communication Protocol | Merged into A2A under LF, repo archived 2025-08-27 (search-engine summaries of IBM material; not verified at source). Not Zed's Agent Client Protocol (editor-to-agent; Track 1) | n/a | n/a | n/a | not filed |
| Claude Code cloud sessions | `--cloud`, `--teleport`, follow-up by id | Available on paid plans | Yes (hours, survives laptop) | claude.ai account; GitHub proxy | Willison (heavy user, positive, container lowers risk) | [Cloud sessions](../../research/sources/anthropic-claude-code-cloud-sessions.md), [Willison](../../research/sources/simonwillison-async-coding-agents-tag.md) |
| Claude Code headless / Actions | `claude -p`, GitHub Action, plugin skills | Mainstream among Claude Code teams | Per run | API key, OAuth token, OIDC federation | Cloudflare code-review pipeline (first-party) | [Headless](../../research/sources/anthropic-claude-code-headless-agent-sdk.md), [Actions](../../research/sources/anthropic-claude-code-github-actions.md), [Cloudflare review](../../research/sources/cloudflare-ai-code-review-opencode.md) |
| Anthropic Managed Agents | Hosted loop, sandbox, sessions, SSE | Beta (header 2026-04-01) | Yes | API key; vault/MCP proxy; self-hosted sandbox | CData (interested party): lock-in, portability, status incidents | [Overview](../../research/sources/anthropic-managed-agents-overview.md), [Engineering post](../../research/sources/anthropic-engineering-scaling-managed-agents.md), [CData](../../research/sources/cdata-claude-managed-agents-meta-harness.md), [SDK hosting](../../research/sources/anthropic-agent-sdk-hosting.md) |
| Codex cloud / plugin / app server | Cloud tasks; Claude Code plugin; MCP server removed | Cloud mainstream-ish; app server experimental | Yes (cloud) | ChatGPT/API auth; environment access control | Willison PRarena: Codex cloud highest PR volume | [Cloud](../../research/sources/openai-codex-cloud-docs.md), [Plugin](../../research/sources/openai-codex-plugin-for-claude-code.md), [MCP removed](../../research/sources/openai-codex-mcp-server-removed.md) |
| Cursor Cloud Agents API | REST, SSE, steer | Public beta | Yes | User or service-account key | None found | [Cursor](../../research/sources/cursor-cloud-agents-api.md) |
| Jules API | REST sessions/activities | v1alpha | Yes | API key | Willison: PR "covers most requirements" but tests failed (2025-05) | [Jules](../../research/sources/google-jules-api.md) |
| Copilot cloud agent | Issue/PR/panel to PR | Product | Yes, 59-min cap | GitHub; see also Track 5 risk note | PRarena merge rate 61.5% (2025-10) | [Copilot](../../research/sources/github-copilot-cloud-agent.md) |
| Devin | Slack-driven cloud agent | Product | Yes | n/a here | Answer.AI: 3/20 (Jan 2025) | [Answer.AI](../../research/sources/answerai-thoughts-month-with-devin.md) |
| OpenAI Agents SDK / Responses (remote MCP, background mode) / AgentKit | Build-your-own | Responses remote MCP since 2025-05-21; AgentKit/Agent Builder from DevDay Oct 2025; a guide claims Agent Builder deprecation on 2026-11-30 (unverified) | Background mode | n/a | Forum reports of Agent Builder/ChatKit latency | not filed: only secondary search snippets were reached; see section 7 |

Related notes filed by other tracks that bear on this track: [Claude Code scheduled tasks/routines](../../research/sources/anthropic-claude-code-scheduled-tasks.md) (API-triggered `/fire` endpoint), [Codex cloud and Slack](../../research/sources/openai-codex-cloud-slack.md), [Claude Tag agent identity](../../research/sources/anthropic-claude-tag-agent-identity.md), [Copilot cloud agent risks](../../research/sources/github-copilot-cloud-agent-risks.md), [Cursor team follow-up forum](../../research/sources/cursor-forum-team-followups-act-on-behalf.md), [Stripe Minions](../../research/sources/stripe-minions-part-2.md), [Wavect on Inspect](../../research/sources/wavect-ramp-inspect-architecture.md).

## 4. What a "deployed task agent called from a general harness" looks like, with examples

- **Glean agents as MCP tools** (vendor docs): admin adds agents to the Glean MCP server; users in Claude Desktop, Cursor, VS Code call them. Constraints are stated outright: no write tools, no human-in-the-loop steps (also for sub-agents), runtime about 30 s, descriptions drive routing, large tool lists degrade selection. Closest real analogue to a PRD-review agent exposed to many hosts, with the caveat that it is read-only.
- **Sentry MCP with Seer** (vendor docs, partly unverified): hosted OAuth MCP server; the root-cause-analysis agent is one of several permission sets a user grants.
- **Claude Code GitHub Actions running `code-review`** (vendor docs) and **Cloudflare's AI code review on OpenCode** (first-party, Track 1 note): a standardised reviewer as a CI component, with 131k runs and cost per review reported by Cloudflare. This is the best-evidenced "task-specific agent called by an event" example, though it is called by CI, not by a general harness.
- **codex-plugin-cc** (first-party): Claude Code delegates review and tasks to a different vendor's agent, locally.
- **Community A2A/MCP bridges** (a2a MCP servers, Claude Code wrappers, Codex-as-MCP wrappers, Jules and Devin MCP wrappers): exist, are unofficial, and one README says not production ready. No first-hand reports found.

Honest gap: no source describes a PRD-review or security agent exposed over MCP/A2A and used in anger, and no independent account of how well any MCP-served agent works.

## 5. Trade-offs

- **Latency and timeouts.** Sync MCP: host limits (Glean: Claude Desktop ~60 s, Cursor 30-60, VS Code ~30; vendor-reported, may be stale). Tasks fix this where supported. Claude Code auto-backgrounds MCP calls after 2 minutes, but background tasks do not survive session exit, and `claude -p` loses results of backgrounded calls. Nested agents compound latency and retry amplification (Gravitee, secondary).
- **Cost.** Subagents and cloud sessions draw on the same plan limits; parallel cloud sessions consume proportionally. A self-hosted Agent SDK service costs about $0.05 per container hour versus dollars of tokens per long session (vendor doc). Managed Agents adds $0.08 per session-hour per a third party (not verified on Anthropic's pages). The Codex plugin's review gate can drain limits.
- **Debuggability.** Three systems (host, protocol hop, remote runtime). MCP now carries `traceparent` in `_meta`; A2A and vendor APIs vary. Ramp-style single-harness designs avoid this; nothing measured.
- **Trust and permissions.** Per-server consent, audience-bound tokens, credentials kept outside sandboxes (Managed Agents, Claude Code cloud). Open: user-versus-agent authority downstream, A2A card spoofing/confused deputy (secondary sources, unverified), auto-fix replies posted under the user's account, headless runs denying prompts.
- **Portability and lock-in.** MCP servers work across hosts, but support for Tasks, sampling and elicitation varies by host and Sampling is deprecated. Vendor APIs are per-vendor. Vendor routes can disappear (Codex MCP server).
- **Reliability of autonomy.** Independent evidence says unpredictable (Answer.AI) and varied by tool (PRArena merge rates). Human review of the output stays necessary, which links to the human-review-gates themes.

## 6. Options by dimension (links, not copies)

Entries appended to [options/DIMENSIONS.md](../../options/DIMENSIONS.md):

- [remote-invocation-route](../../options/DIMENSIONS.md#remote-invocation-route-how-a-primary-harness-reaches-a-remote-or-deployed-agent): **new** (proposed), nine options and seven key questions.
- [capability-packaging](../../options/DIMENSIONS.md#capability-packaging-how-skills-and-agents-are-packaged-and-invoked): a row breaking out the "deployed agent" option, key questions 10 and 11.
- [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-permissions-cost-identity-audit): four identity/credential rows (MCP per-server OAuth, vault proxy, OIDC federation for CI, A2A card/schemes), questions 11 to 13.
- [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives): vendor-hosted runtime with self-hostable sandbox row, question 3.
- [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-and-what-agent-shape-fits): fire-and-forget delegation and read-only bounded task agent rows, question 3.
- [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model): admin-curated agent catalog row (user and product choice), one question; plus cross-cutting question 5.

**Proposed structure changes (for the director):**
1. Keep `remote-invocation-route` as its own dimension or fold it into `capability-packaging`'s "deployed agent" option; I split it out because the choice among six call routes is separable from the choice of packaging format, and capability-packaging is already long (Track 4 also proposed a split).
2. Consider a new dimension `agent-identity-delegation` (whose authority a delegated or shared agent uses). It currently sits as rows in governance-control-plane, overlaps Track 5's identity rows (creator/requester/service account) and my MCP/A2A rows, and has its own theme slug `identity-delegation` in THEMES.md.
3. `session-handoff-portability` (Track 5) and my "human-triggered handoff" option overlap; merge candidates.

## 7. Open questions for Geoff

Unranked.

1. Is the first deployed task agent (PRD review?) meant to be called from harnesses we do not control (Claude Code, Codex, Claude Desktop, Cursor), or from our own surface? That decides whether MCP/A2A matter at all.
2. Which hosts do your target users actually use? Support for MCP Tasks, A2A clients, plugins and background agents differs per host.
3. Do target orgs require Zero Data Retention, HIPAA or customer-managed keys? Claude Code cloud sessions and Managed Agents are documented as excluded, which constrains vendor-cloud options.
4. Who should the agent act as when it touches downstream systems: the requester, a service account, or the creator? Needs a security/policy owner.
5. Are you willing to fund a small prototype: one workflow (PRD review) built as a skill, as a sync MCP agent, as an MCP+Tasks agent and as a CI-triggered reviewer, with a no-agent baseline, because the independent evidence for every one of these is missing?
6. Should I look further for A2A production evidence (e.g. named customer case studies from Microsoft, AWS, Salesforce, ServiceNow, SAP) or accept "unproven" for the synthesis?

## 8. Gaps and what I could not verify

- **Not found after 4+ routes each:** independent quality/latency/cost reports for agents served over MCP (Seer, CodeRabbit, Greptile, Glean); any first-hand report of an A2A deployment reaching production; a native A2A client in Claude Code or Codex (only community bridges and an editor-protocol ACP request, #6686).
- **Only secondary snippets reached:** OpenAI AgentKit/Agent Builder/Responses background mode (including a claimed Agent Builder deprecation on 2026-11-30, forum reports of ChatKit latency); Devin's official MCP/API docs (404 on the URL tried); Semgrep's original A2A security analysis and arXiv 2608.01558 on delegation chains (cited via blogs; not opened); IBM ACP-to-A2A merger (via search summaries only, not filed).
- **Truncated reads:** A2A spec (first 100k of 256k characters, Appendix B unread), Claude Code MCP docs (organisation controls and `claude mcp serve` unread), Cursor API (last 33k), subagents doc (last 16k). MCP Enterprise-Managed Authorization mechanism not read. Claude Code self-hosted environments and MCP tunnels not read. Vercel/Modal hosting of such agents: only the Agent SDK hosting doc (which names Modal) was read; no Vercel-specific source (an existing Vercel note is in sources/). Cloudflare's agent offerings beyond the 2025 remote-MCP post are Track 1's.
- **Dates:** several docs pages show no publication date (marked `unknown`); the Codex MCP-server removal date is not on the page.
