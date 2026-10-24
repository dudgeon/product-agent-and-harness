# Follow-up 1: A2A in production

Date: 2026-10-24. Filed by: research-runtime-patterns-follow-up-round (follow-up researcher N=1). Builds on [Track 3](track-3-remote-deployed-agents.md) and [01-synthesis.md](01-synthesis.md) section B.2 P6 and D.6. Not a recommendation: options and key questions only.

Evidence labels: first-party (builder or vendor describing its own system), vendor-claim (promotional, or about customers), independent (no stake in the outcome), anecdote (forum or second-hand). Source notes are under `../../research/sources/`.

## Question and scope

**Thin spot.** The synthesis said A2A v1.0 (March 2026, Linux Foundation, 150+ organisations) is specified and has platform support (Copilot Studio as client, AWS Bedrock AgentCore as host), but no named production deployment. That rested on Glukhov (independent) and an Ask HN thread (anecdote).

**What I looked for.**
- Named organisations running A2A between agents in production: which agents talk to which, at what volumes, and whether the evidence is independent.
- Vendor case studies and docs from Google Cloud, Salesforce, SAP, ServiceNow, Microsoft, AWS, Atlassian and Box.
- Usage signals: SDK downloads, dependents and stars.
- Criticisms and security research.
- The A2A and MCP convergence story.
- Whether Claude Code, Codex, Cursor or Copilot have a native A2A client.

**Angle.** Should a regulated enterprise building an internal intent-shaping agent expect to reach deployed agents over A2A, over MCP (including the Tasks extension), or over vendor APIs? This bears on the dimensions `remote-invocation-route` and `agent-identity-delegation`.

**Where I looked.**
- Web search, standard and extended.
- Primary pages: AAIF, a2a-protocol.org, Atlassian developer and support docs, ServiceNow Community, Salesforce blog, Google Cloud blog and release notes, Unit 42, Semgrep, Keysight, arXiv, KrASIA, Credal.
- GitHub API: issues and PRs in anthropics/claude-code, openai/codex, openai/openai-agents-python and github/copilot-sdk; repository stars; the contents of codex-rs.
- PyPI JSON API for framework dependencies, and pepy.tech for download counts.
- HN Algolia API, to read the Ask HN thread verbatim and find other A2A stories.

**Search terms included:**
- "A2A protocol production deployment case study"
- "Agentforce A2A production"
- "A2A agent card spoofing security research"
- "Unit 42 agent session smuggling"
- "SAP Joule A2A ServiceNow"
- "Atlassian Rovo A2A"
- "AWS Bedrock AgentCore A2A customer case study"
- "Gemini Enterprise A2A agents customers"
- "\"A2A in production\" engineering blog"
- "A2A MCP merger Agentic AI Foundation"
- "Gemini CLI remote subagents A2A"
- "forum.cursor.com A2A"
- "Anthropic Claude A2A support"
- "a2a-sdk pypi downloads"

## Findings

**Bottom line**
- **Still no independent evidence of a named enterprise running cross-vendor A2A traffic in production, and no volumes anywhere.** The best named case is first-party: Eon, published on the foundation's own blog. It moved 3 of about 20 specialist agents behind A2A because they sit across an ownership boundary. It gives no volumes and lists several new failure modes ([Eon](../../research/sources/aaif-eon-a2a-into-production.md), first-party, 2026-08-26). AAIF now names consumer cases (Huawei Celia/HarmonyOS, WeChat with phone-maker assistants, PayPal with Google Cloud commerce) ([AAIF](../../research/sources/aaif-a2a-joins-aaif.md), vendor-claim, 2026-08-17). Independent reporting confirms that the WeChat integrations are being built, but it does not name the protocol ([KrASIA](../../research/sources/kr-asia-wechat-phone-agents-a2a.md), independent, 2026-06-09).
- **Platform support is now broad and mostly GA, but mostly on A2A 0.3, and it lives in enterprise agent platforms, not coding harnesses.**
  - Atlassian runs an inbound A2A gateway to Rovo that acts as the signed-in user ([Atlassian](../../research/sources/atlassian-rovo-a2a-gateway-docs.md), first-party, 2026-08-07, v0.3.0).
  - ServiceNow can be A2A client or server ([ServiceNow](../../research/sources/servicenow-community-action-fabric-mcp-a2a.md), first-party, 2026-06-16).
  - Gemini Enterprise made A2A agent registration GA on 2026-08-17 ([release notes](../../research/sources/gemini-enterprise-release-notes-a2a.md), first-party).
  - Agentforce A2A was beta in April 2026 ([Salesforce](../../research/sources/salesforce-agentforce-integration-pattern-api-mcp-a2a.md), vendor-claim, 2026-04-01).
  - Copilot Studio and AgentCore were covered earlier.
- **Among general coding harnesses, only Gemini CLI has a native A2A client** ([Gemini CLI](../../research/sources/gemini-cli-remote-subagents-a2a.md), first-party, 2026-01-27).
  - Claude Code: none. The feature request has been open since 2026-02-24 and Anthropic staff have not commented on it ([#28300](../../research/sources/github-claude-code-issue-28300-a2a.md), anecdote).
  - Codex: none. There is no A2A crate in `codex-rs`, and OpenAI's Agents SDK maintainers have declined A2A three times, the latest on 2026-06-24 ([OpenAI PRs](../../research/sources/github-openai-agents-sdk-a2a-prs-declined.md), first-party).
  - Copilot: the SDK has an open request (#2270), and VS Code is rebuilding its agent infrastructure on Microsoft's Agent Host Protocol, not A2A ([AHP](../../research/sources/microsoft-agent-host-protocol.md), first-party; [HN follow-up](../../research/sources/hn-ask-is-anyone-using-a2a.md), anecdote).
  - Cursor: only a forum request was found.
- **Governance converged; the protocols did not.** A2A joined the Agentic AI Foundation in August 2026, alongside MCP, AGENTS.md and goose. Both announcements call the two complementary layers, and neither mentions a merger or a joint spec ([AAIF](../../research/sources/aaif-a2a-joins-aaif.md), vendor-claim; [A2A blog](../../research/sources/a2a-project-joining-aaif.md), first-party, 2026-08-27). In practice MCP's Tasks extension covers much of what made A2A distinct (long-running work, input-required). Practitioners describe putting an agent behind an MCP server instead of using A2A ([HN](../../research/sources/hn-ask-is-anyone-using-a2a.md), anecdote, 2026-06-18).
- **Security research is now substantial and points at the hard parts the synthesis flagged: identity across hops, trust in the remote agent, and audit.**
  - A spec-level analysis finds 11 vulnerabilities, including credential harvesting via multi-hop identity loss ([A2ABreak](../../research/sources/arxiv-a2abreak-security-analysis.md), independent, 2026-09-09).
  - Session smuggling made a client agent buy stock unprompted ([Unit 42](../../research/sources/unit42-agent-session-smuggling-a2a.md), independent, 2025-10-31).
  - Agent Card signing is supported but not enforced ([Semgrep](../../research/sources/semgrep-security-engineers-guide-a2a.md), independent, 2025-12-17).
  - ServiceNow's AI Gateway governs MCP traffic but not A2A ([ServiceNow](../../research/sources/servicenow-community-action-fabric-mcp-a2a.md), first-party).

**Named deployments, by strength of evidence**

| Who | What talks to what | Volume | Evidence | Source |
|---|---|---|---|---|
| Eon (cloud data platform) | The Buzz orchestrator calls 3 remote specialists over A2A: a triage agent holding production credentials, a semantic-layer agent, and tenant-built agents on other frameworks. About 20 other specialists stay in-process | None given | First-party, on the AAIF blog | [Eon](../../research/sources/aaif-eon-a2a-into-production.md) |
| Huawei, WeChat, phone makers | Phone system assistants (Xiaoyi, Xiao Ai, Yoyo, V, Aicy) send intents to WeChat's agent | None | Vendor-claim (AAIF says "over A2A"); independent journalism confirms integrations without naming the protocol | [AAIF](../../research/sources/aaif-a2a-joins-aaif.md), [KrASIA](../../research/sources/kr-asia-wechat-phone-agents-a2a.md) |
| PayPal with Google Cloud | Merchant agent talks to PayPal agent over A2A, with AP2 mandates | None; GA status unknown | Vendor-claim (announced 2025-10-28) | [AAIF](../../research/sources/aaif-a2a-joins-aaif.md) (Google Cloud post not filed) |
| Infor | Copilot Studio connects to Infor's GenAI over A2A (feature toggle) | None | Vendor docs (search snippet only, not filed) | not filed |
| HN commenters | "Using A2A at work" (lazharichir, techwizrd); one megacorp employee saw no A2A in any final product | None | Anecdote | [HN](../../research/sources/hn-ask-is-anyone-using-a2a.md) |

**Vendor products and whether they show cross-vendor traffic.** None of these publishes a customer with measured A2A traffic.

| Vendor | A2A role | Version | Auth | Cross-vendor traffic shown? | Source |
|---|---|---|---|---|---|
| Atlassian Rovo | Server (inbound only); Gemini is the featured client | 0.3.0 | OAuth 2.0/2.1 with PKCE, DCR only, acts as the user; admin can disable | No customers or figures; GA post body unreadable | [Atlassian](../../research/sources/atlassian-rovo-a2a-gateway-docs.md) |
| ServiceNow AI Agent Fabric | Client and server | 0.3 (v1.0 planned) | OAuth 2.0 or API key per external agent | No; scenarios illustrative; A2A outside AI Gateway governance | [ServiceNow](../../research/sources/servicenow-community-action-fabric-mcp-a2a.md) |
| Salesforce Agentforce | Outbound and inbound (per architect guide) | not stated | OAuth 2.0 handshake | No; beta as of April 2026 | [Salesforce](../../research/sources/salesforce-agentforce-integration-pattern-api-mcp-a2a.md) |
| Google Gemini Enterprise | Host registers A2A agents; Marketplace A2A agents | not stated | not read | No figures; the Next 2026 wrap-up never mentions A2A | [release notes](../../research/sources/gemini-enterprise-release-notes-a2a.md), [Next wrap-up](../../research/sources/google-cloud-next-2026-wrap-up.md) |
| Microsoft Copilot Studio | Client | not stated | None/API key/OAuth | No | [Copilot Studio](../../research/sources/microsoft-copilot-studio-a2a.md) (earlier) |
| AWS Bedrock AgentCore | Host | 0.3 and 1.0 extras in the SDK | SigV4 or JWT | AWS reference example only (ADK host, Strands and OpenAI SDK agents); no customer found | [AgentCore](../../research/sources/aws-bedrock-agentcore-runtime-a2a.md) (earlier), [pepy](../../research/sources/pepy-a2a-sdk-downloads.md) |
| SAP Joule, Box | Listed supporters | — | — | Nothing found beyond an EPAM job ad asking for Joule-to-ServiceNow A2A experience | not filed |

**Usage signals** ([pepy and GitHub](../../research/sources/pepy-a2a-sdk-downloads.md), independent measurement, 2026-10-24)
- Python `a2a-sdk` had 12.2M downloads in the last 30 days (89.5M total, CI included). Python `mcp` had 273.9M in the same period, about 22 times more. An A2A package author reported a similar 24x gap in June.
- A2A arrives mainly as an optional extra of agent frameworks: ADK, Strands, CrewAI, AgentCore and Microsoft agent-framework-a2a.
- Several frameworks (Strands, CrewAI) still pin A2A below 0.4.
- A2A spec repo stars (26k) are on a par with MCP's python-sdk; A2A SDK repo stars are far lower.

**Criticisms**
- HN practitioners, verbatim ([HN follow-up](../../research/sources/hn-ask-is-anyone-using-a2a.md), anecdote, 2026-06-18): "back to Agent <> MCP"; "stayed with agent-behind-MCP"; "we didn't need an agent on the other side". The hard problem named is authority and revocation, not message format.
- Credal argues MCP won on time-to-value. Credal sells MCP governance and gives no data ([Credal](../../research/sources/credal-what-happened-to-a2a.md), vendor-claim, 2026-03-06).
- Glukhov's tiers (earlier note) still hold: logo support, then SDK adoption, then platform adoption, then production retention. This round adds one first-party production account to the last tier.

**Security**
- **Spec-level.** A2ABreak models the spec as a 37-state machine and finds 11 vulnerabilities exploitable by a fully compliant adversary: context injection via unprotected context IDs, identity loss across delegation hops, and exfiltration through unattested capability claims ([A2ABreak](../../research/sources/arxiv-a2abreak-security-analysis.md), independent; abstract only).
- **Interaction-level.**
  - Session smuggling works across turns. Unit 42 says it is not a protocol flaw; the cause is agents trusting each other by default. Its mitigations are out-of-band human approval, context grounding and signed cards ([Unit 42](../../research/sources/unit42-agent-session-smuggling-a2a.md)).
  - Agent Card poisoning puts card text into the caller's prompt ([Keysight](../../research/sources/keysight-agent-card-poisoning.md), independent, 2026-03-12).
- **Auth.** Semgrep: signing supported but not enforced; no enforced short-lived tokens; no consent step; authorisation implementation-defined ([Semgrep](../../research/sources/semgrep-security-engineers-guide-a2a.md)). A vendor blog (grith, cited in the Semgrep note) credits v1.0 with requiring PKCE and dropping the implicit and password flows, and says the other gaps remain.
- **Production confirmation.** Eon independently hit identity loss: the far side answered as a service identity, and Eon worked around it by encoding the user in `context_id` ([Eon](../../research/sources/aaif-eon-a2a-into-production.md)).

**A2A and MCP convergence**
- **Governance.** Both are now in AAIF, whose other hosted projects include AGENTS.md, goose and, from 2026-10-22, Agent Skills. Both announcements frame the protocols as "vertical vs horizontal". No merger, no joint working group and no bridging spec was found.
- **Functionally converging.** MCP Tasks gives durable handles, polling and input-required, which overlaps A2A's task lifecycle. Vendors now offer both side by side:
  - Atlassian: separate MCP and A2A endpoints.
  - ServiceNow: MCP for "do X", A2A for "handle the Y part".
  - Salesforce: API for sensitive or bulk work, MCP where a server exists, A2A where an agent exists.
  - Gemini Enterprise: one Agent Registry list holds both.
- **"Agents as MCP servers"** is common usage among practitioners (HN: holografix, time0ut) and is how Glean and Sentry ship. No formal MCP-A2A merger proposal was found.

**Harness clients by October 2026**

| Harness | Native A2A client? | Evidence |
|---|---|---|
| Gemini CLI | Yes: remote subagents defined by agent card URL in `.gemini/agents/*.md`; auth via apiKey, http, google-credentials or OAuth; honours proxy settings | [docs](../../research/sources/gemini-cli-remote-subagents-a2a.md) (first-party) |
| Claude Code | No. #28300 open since 2026-02-24 with about 55 comments and no Anthropic staff reply; community bridges only | [issue](../../research/sources/github-claude-code-issue-28300-a2a.md) (anecdote) |
| Codex / OpenAI Agents SDK | No. No A2A in codex-rs; SDK maintainers: "We still don't have immediate plans to add A2A support" (2026-06-24) | [PRs](../../research/sources/github-openai-agents-sdk-a2a-prs-declined.md) (first-party) |
| GitHub Copilot / VS Code | No native client found. Copilot SDK request #2270 is open; VS Code is moving to AHP (a session-host protocol) | [AHP](../../research/sources/microsoft-agent-host-protocol.md) (first-party) |
| Cursor | No. Only a forum feature request found, with no team response visible | search result only, not filed |

**For the relevance angle (an options view, not a pick).**

A regulated enterprise building an internal intent-shaping agent would meet A2A mainly where enterprise SaaS exposes an agent endpoint, for example Rovo for Jira and Confluence, ServiceNow or Agentforce. Most often that agent would be called from an enterprise agent host (Gemini Enterprise, Copilot Studio, Agentforce, ServiceNow), not from Claude Code or Codex.

If the intent-shaping agent lives in or is called from a coding harness, the reachable routes today are MCP (sync or Tasks), vendor APIs, or a bridge that wraps the A2A agent as an MCP server.

The audit question matters more than the protocol choice:
- One platform governs MCP but not A2A.
- A2A has no first-class "who is asking" field.
- Atlassian is the one example found of A2A carrying user-delegated authority (OAuth as the user).

## What changed for the taxonomy

- **P6 (general harness calling deployed task agents).**
  - Keep A2A at **emerging**, but change the reason. It is no longer "no named production use". It is now "GA in several enterprise agent platforms (mostly v0.3); one named first-party production account (Eon); no independent or volume evidence; no native client in Claude Code, Codex or Copilot".
  - Add Gemini CLI as the one coding-harness A2A client.
  - Replace "no native A2A client in Claude Code or Codex" with the dated evidence: #28300 open; OpenAI declined A2A in 2025-07 and twice in 2026-06.
- **New sub-shape under P6, coined here (our term, no consensus term found): "SaaS agent endpoint".** A SaaS vendor hosts an agent-facing endpoint over its product (Rovo A2A gateway, ServiceNow secondary agents, Agentforce inbound), next to its MCP server. The caller hands off a goal rather than calling tools. For PM work this is the relevant A2A shape, because Jira and Confluence already offer it.
- **A2A splits into two settings that should not be compared as one.** Both differ from P6's "harness calls agent":
  - (a) Enterprise agent host to SaaS agent: Gemini Enterprise, Copilot Studio, Agentforce, ServiceNow as clients.
  - (b) An in-house boundary, where most agents stay in-process and only agents across an ownership, credential or release boundary go behind A2A (Eon).
- **Axis 7 (governance).** Add "does the gateway or audit plane cover this route?" as an explicit attribute. ServiceNow's AI Gateway covers MCP only. Gemini Enterprise's registry lists both.
- **Axis 5 (invocation relation).** Record the A2A version split (0.3 vs 1.0) as a portability risk within A2A itself.
- **Terms.** "Agent-behind-MCP" (practitioner usage on HN, and Glean's "agents as tools") is the common term for the main alternative; use it. ACP's merger into A2A (August 2025) is now confirmed at a primary-ish source (AAIF), resolving a Track 3 gap.
- **P8 (shared sessions), side finding.** Microsoft's Agent Host Protocol (VS Code; multi-client synchronised session state) is a new standard candidate for shared sessions and host portability. It is not A2A.

## Proposed INDEX lines

- [A2A joins AAIF's open agentic stack](sources/aaif-a2a-joins-aaif.md) · article · 2026-08-17 · relevance high · A2A moves into the Agentic AI Foundation beside MCP; names Huawei, WeChat, PayPal as production users; no enterprise volumes · https://aaif.io/blog/a2a-joins-aaif
- [A New Chapter for A2A: Joining the Agentic AI Foundation](sources/a2a-project-joining-aaif.md) · article · 2026-08-27 · relevance medium · A2A project's own AAIF announcement; Growth Stage; complementary to MCP, no merger · https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/
- [What We Learned Putting A2A Into Production](sources/aaif-eon-a2a-into-production.md) · article · 2026-08-26 · relevance high · Eon moved 3 of ~20 agents behind A2A at ownership boundaries; identity loss, provenance, timeouts, fabricated answers on empty errors; would choose again · https://aaif.io/blog/what-we-learned-putting-a2a-into-production
- [Rovo A2A (Atlassian A2A Gateway developer documentation)](sources/atlassian-rovo-a2a-gateway-docs.md) · docs · 2026-08-07 · relevance high · Inbound A2A server to Rovo for Jira/Confluence; OAuth-only, acts as the user; v0.3.0; ~30 s sync cap · https://developer.atlassian.com/cloud/rovo-a2a/
- [Action Fabric: MCP Server, MCP Client, and A2A explained](sources/servicenow-community-action-fabric-mcp-a2a.md) · article · 2026-06-16 · relevance high · ServiceNow as A2A client and server; OAuth or API key; AI Gateway governs MCP but not A2A · https://www.servicenow.com/community/servicenow-otto-articles/action-fabric-mcp-server-mcp-client-and-a2a-explained/ta-p/3557794
- [Choose the Right Agentforce Integration Pattern: API, MCP, or A2A](sources/salesforce-agentforce-integration-pattern-api-mcp-a2a.md) · article · 2026-04-01 · relevance medium · Salesforce's rule for API vs MCP vs A2A; both protocols beta in Agentforce; MCP tool suspended on description change · https://www.salesforce.com/blog/how-to-choose-integration-pattern-for-agentforce/
- [WeChat opens the door to phone-based AI agents, on its own terms](sources/kr-asia-wechat-phone-agents-a2a.md) · article · 2026-06-09 · relevance medium · Independent report of phone-assistant-to-WeChat agent integrations with dual authorisation; protocol not named · https://kr-asia.com/wechat-opens-the-door-to-phone-based-ai-agents-on-its-own-terms
- [When AI Agents Go Rogue: Agent Session Smuggling Attack in A2A Systems](sources/unit42-agent-session-smuggling-a2a.md) · article · 2025-10-31 · relevance high · Malicious remote agent smuggles instructions across an A2A session; data leak and unauthorised trade in ADK PoC; out-of-band human approval advised · https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/
- [A Security Engineer's Guide to the A2A Protocol](sources/semgrep-security-engineers-guide-a2a.md) · article · 2025-12-17 · relevance medium · Primary source for "card signing supported but not enforced"; no enforced short-lived tokens, no consent step · https://semgrep.dev/blog/2025/a-security-engineers-guide-to-the-a2a-protocol
- [A2ABreak: Systematic Security Analysis of the A2A Protocol](sources/arxiv-a2abreak-security-analysis.md) · paper · 2026-09-09 · relevance medium · Formal model of the A2A spec finds 11 vulnerabilities incl. multi-hop identity loss · https://arxiv.org/abs/2609.10871
- [Agent Card Poisoning](sources/keysight-agent-card-poisoning.md) · article · 2026-03-12 · relevance low · Instructions in a remote agent's card hijack the host LLM and exfiltrate payment data in a simulation · https://keysight.com/blogs/en/tech/nwvs/2026/03/12/agent-card-poisoning
- [Multi-agent collaboration across machines (Agent-to-Agent protocol), claude-code #28300](sources/github-claude-code-issue-28300-a2a.md) · other · 2026-02-24 · relevance medium · Open A2A feature request for Claude Code, ~55 comments, no Anthropic staff reply; community bridges instead · https://github.com/anthropics/claude-code/issues/28300
- [OpenAI Agents SDK A2A PRs declined (#1245, #3567, #3683)](sources/github-openai-agents-sdk-a2a-prs-declined.md) · other · 2025-07-25 · relevance medium · OpenAI maintainers declined A2A three times through 2026-06-24; no A2A in Codex · https://github.com/openai/openai-agents-python/pull/1245
- [a2a-sdk download statistics with GitHub and PyPI checks](sources/pepy-a2a-sdk-downloads.md) · other · 2026-10-24 · relevance medium · 12.2M/month vs MCP 273.9M (~22x); A2A mostly an optional framework extra; many pinned to 0.3 · https://pepy.tech/projects/a2a-sdk
- [Remote Subagents (Gemini CLI documentation)](sources/gemini-cli-remote-subagents-a2a.md) · docs · 2026-01-27 · relevance high · The one coding harness with a native A2A client; remote agents declared like subagents in repo files · https://geminicli.com/docs/core/remote-agents/
- [Google Cloud Next 2026 wrap-up](sources/google-cloud-next-2026-wrap-up.md) · article · 2026-04-24 · relevance medium · Google's Next 2026 wrap-up never mentions A2A; customer stories are intra-platform agent fleets · https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up
- [Gemini Enterprise release notes (A2A entries)](sources/gemini-enterprise-release-notes-a2a.md) · docs · unknown · relevance medium · A2A agent registration GA 2026-08-17; A2A agents and MCP servers in one Agent Registry · https://docs.cloud.google.com/agentspace/docs/release-notes
- [What happened to A2A Protocol?](sources/credal-what-happened-to-a2a.md) · article · 2026-03-06 · relevance low · MCP-governance vendor argues A2A lost on use cases and implementation burden; no data · https://www.credal.ai/blog/what-happened-to-a2a-protocol
- [Agent Host Protocol](sources/microsoft-agent-host-protocol.md) · docs · 2026-03-12 · relevance medium · VS Code's multi-client agent session protocol; IDE side standardising on host protocols, not A2A · https://github.com/microsoft/agent-host-protocol

Amended (no new INDEX line): [Ask HN: Is anyone using the A2A protocol?](../../research/sources/hn-ask-is-anyone-using-a2a.md). I added a `## Follow-up (2026-10-24)` section with the exact date (2026-06-18), the original URL, verbatim quotes, the download comparison and the VS Code/AHP comment. **The INDEX line for this note should change its date from "2026" to "2026-06-18".**

## Proposed THEMES bullets

**New theme proposed: `agent-protocol-security`: Security of agent-to-agent and agent-to-tool protocols.**
Attacks and gaps that arise because a remote agent or its metadata becomes input to your agent: card or description poisoning, session smuggling, identity loss across delegation hops, optional signing, and gateways that cover one protocol but not another.

Why it is new: `skill-supply-chain-security` covers installed skills and plugins, and `identity-delegation` covers whose authority is used. Neither covers runtime attacks from a live remote counterparty, or audit coverage of a protocol route. If the director prefers, it could be folded into `identity-delegation` plus `agent-failure-modes`.

- [When AI Agents Go Rogue: Agent Session Smuggling](sources/unit42-agent-session-smuggling-a2a.md): malicious remote agent injects instructions across an A2A session; unauthorised `buy_stock` in an ADK PoC; not a protocol flaw (research-runtime-patterns-follow-up-round)
- [A2ABreak](sources/arxiv-a2abreak-security-analysis.md): 11 spec-level vulnerabilities exploitable by a compliant adversary, incl. multi-hop identity loss (research-runtime-patterns-follow-up-round)
- [A Security Engineer's Guide to the A2A Protocol](sources/semgrep-security-engineers-guide-a2a.md): card signing supported but not enforced; no enforced short-lived tokens; no consent step (research-runtime-patterns-follow-up-round)
- [Agent Card Poisoning](sources/keysight-agent-card-poisoning.md): card metadata treated as instructions; payment data exfiltrated in a simulation (research-runtime-patterns-follow-up-round)
- [Action Fabric: MCP Server, MCP Client, and A2A explained](sources/servicenow-community-action-fabric-mcp-a2a.md): ServiceNow AI Gateway governs MCP traffic only; A2A outside its scope at GA (research-runtime-patterns-follow-up-round)

**remote-agent-invocation**
- [What We Learned Putting A2A Into Production](sources/aaif-eon-a2a-into-production.md): only named production A2A account found; 3 of ~20 agents behind A2A at ownership boundaries; first-party, no volumes (research-runtime-patterns-follow-up-round)
- [A2A joins AAIF's open agentic stack](sources/aaif-a2a-joins-aaif.md): A2A now in the same foundation as MCP; framed as complementary, no merger (research-runtime-patterns-follow-up-round)
- [Rovo A2A gateway docs](sources/atlassian-rovo-a2a-gateway-docs.md): Jira/Confluence reachable as an agent over A2A (inbound, v0.3.0) beside the Rovo MCP server (research-runtime-patterns-follow-up-round)
- [Remote Subagents (Gemini CLI)](sources/gemini-cli-remote-subagents-a2a.md): the one coding harness with a native A2A client (research-runtime-patterns-follow-up-round)
- [claude-code #28300](sources/github-claude-code-issue-28300-a2a.md): no A2A client in Claude Code; request open since 2026-02-24 (research-runtime-patterns-follow-up-round)
- [OpenAI Agents SDK A2A PRs declined](sources/github-openai-agents-sdk-a2a-prs-declined.md): OpenAI declined A2A three times through 2026-06-24 (research-runtime-patterns-follow-up-round)
- [Choose the Right Agentforce Integration Pattern](sources/salesforce-agentforce-integration-pattern-api-mcp-a2a.md): vendor rule: API for sensitive or bulk, MCP where a server exists, A2A where an agent exists (research-runtime-patterns-follow-up-round)
- [Gemini Enterprise release notes](sources/gemini-enterprise-release-notes-a2a.md): A2A agent registration GA 2026-08-17 (research-runtime-patterns-follow-up-round)

**identity-delegation**
- [Rovo A2A gateway docs](sources/atlassian-rovo-a2a-gateway-docs.md): A2A with user-delegated OAuth; "All actions respect the authenticated user's existing Atlassian permissions" (research-runtime-patterns-follow-up-round)
- [What We Learned Putting A2A Into Production](sources/aaif-eon-a2a-into-production.md): asker identity lost across the hop; workaround encodes user in `context_id` (research-runtime-patterns-follow-up-round)
- [WeChat opens the door to phone-based AI agents](sources/kr-asia-wechat-phone-agents-a2a.md): dual authorisation (user plus app) for agent-to-agent calls (research-runtime-patterns-follow-up-round)

**vendor-claims-vs-independent-evidence**
- [a2a-sdk download statistics](sources/pepy-a2a-sdk-downloads.md): A2A SDK ~12M/month vs MCP ~274M; mostly installed as framework extras (research-runtime-patterns-follow-up-round)
- [Google Cloud Next 2026 wrap-up](sources/google-cloud-next-2026-wrap-up.md): A2A absent from its originator's own conference wrap-up (research-runtime-patterns-follow-up-round)
- [WeChat opens the door to phone-based AI agents](sources/kr-asia-wechat-phone-agents-a2a.md): independent report does not confirm AAIF's "over A2A" claim (research-runtime-patterns-follow-up-round)
- [What happened to A2A Protocol?](sources/credal-what-happened-to-a2a.md): sceptical but interested-party, no data (research-runtime-patterns-follow-up-round)

**agent-failure-modes**
- [What We Learned Putting A2A Into Production](sources/aaif-eon-a2a-into-production.md): empty error events dropped, so the orchestrator fabricated answers; remote context exhaustion; 60 s gateway timeout (research-runtime-patterns-follow-up-round)

**human-review-gates**
- [Agent Session Smuggling](sources/unit42-agent-session-smuggling-a2a.md): first mitigation is human approval of sensitive actions delivered out of band (research-runtime-patterns-follow-up-round)

**shared-persistent-sessions**
- [Agent Host Protocol](sources/microsoft-agent-host-protocol.md): VS Code's synchronised multi-client session protocol (research-runtime-patterns-follow-up-round)

## Proposed DIMENSIONS additions

### remote-invocation-route

Option rows. The first one replaces the evidence and maturity text of the existing "A2A agent" row; the others are new.

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| A2A agent (update to existing row) | Remote agent publishes an Agent Card; caller sends tasks over JSON-RPC/gRPC/REST with streaming or push | A2A v1.0 spec; implementations mostly on 0.3 (Atlassian, ServiceNow, Gemini CLI, Eon, Strands, CrewAI); now hosted by AAIF beside MCP | Vendor-neutral task lifecycle; runtime-readable capability cards; cross-ownership contracts | One named first-party production account and no volumes; 0.3/1.0 version split; no native client in Claude Code, Codex or Copilot (OpenAI declined three times); SDK downloads ~22x below MCP; spec-level vulnerabilities (A2ABreak) | emerging (GA in enterprise platforms; production use thinly evidenced) | [Eon](../research/sources/aaif-eon-a2a-into-production.md) (first-party); [AAIF](../research/sources/aaif-a2a-joins-aaif.md) (vendor claim); [pepy](../research/sources/pepy-a2a-sdk-downloads.md) (independent); [OpenAI PRs](../research/sources/github-openai-agents-sdk-a2a-prs-declined.md) (first-party); [A2ABreak](../research/sources/arxiv-a2abreak-security-analysis.md) (independent) |
| SaaS agent endpoint over A2A (our coined term) | A SaaS vendor hosts an agent-facing A2A server over its product, next to its MCP server; the caller hands off a goal, not a tool call | Atlassian Rovo A2A gateway (Jira, Confluence; inbound only, v0.3.0); ServiceNow secondary agents; Agentforce inbound | Reach a vendor's own agent with its data and permissions without building tools; Rovo acts as the signed-in user | Mostly reachable from enterprise agent hosts (Gemini Enterprise, Copilot Studio), not coding harnesses; ~30 s sync cap (Rovo); opaque remote reasoning; audit coverage varies | early-adopter (GA products, no published usage) | [Atlassian](../research/sources/atlassian-rovo-a2a-gateway-docs.md) (first-party); [ServiceNow](../research/sources/servicenow-community-action-fabric-mcp-a2a.md) (first-party); [Salesforce](../research/sources/salesforce-agentforce-integration-pattern-api-mcp-a2a.md) (vendor claim) |
| Enterprise agent host as A2A client | An enterprise agent app registers external A2A agents and routes to them, governed in one registry with MCP servers | Gemini Enterprise (A2A registration GA 2026-08-17); Copilot Studio; ServiceNow primary agents; Agentforce outbound (beta April 2026) | Admin-curated catalogue; one place to approve agents and MCP servers | Ties the route to the host product; per-connection API keys common (service identity); cross-vendor traffic unshown | early-adopter | [Gemini Enterprise notes](../research/sources/gemini-enterprise-release-notes-a2a.md) (first-party); [Copilot Studio](../research/sources/microsoft-copilot-studio-a2a.md) (vendor claim); [ServiceNow](../research/sources/servicenow-community-action-fabric-mcp-a2a.md) (first-party) |
| Hybrid: in-process specialists, A2A only at ownership boundaries | Most specialists stay in-process; only agents with separate owners, credentials or release cycles go behind A2A | Eon Buzz (3 of ~20 agents remote) | Protocol cost paid only where a contract is needed; tenant or third-party agents pluggable at runtime | ~400 lines of wrapper; identity, provenance and session-lifecycle extensions are custom; "added failure modes rather than removing them" | emerging | [Eon](../research/sources/aaif-eon-a2a-into-production.md) (first-party) |
| Coding harness with native A2A subagents | Remote A2A agents declared like local subagents in repo files | Gemini CLI `.gemini/agents/*.md` with `kind: remote` | Team-versioned remote agents; OAuth/apiKey auth; proxy-aware | Only Gemini CLI found; none in Claude Code, Codex, Copilot or Cursor | emerging | [Gemini CLI](../research/sources/gemini-cli-remote-subagents-a2a.md) (first-party); [#28300](../research/sources/github-claude-code-issue-28300-a2a.md) (anecdote) |
| Agent behind MCP (bridging an A2A agent) | Wrap a remote agent, A2A or not, as an MCP server so any MCP host can call it | Glean agents-as-tools; practitioners on HN; community A2A-to-MCP bridges | Works in every MCP host today; MCP Tasks for long jobs | Loses A2A's native task lifecycle unless Tasks is supported; bridges unofficial | early-adopter | [HN](../research/sources/hn-ask-is-anyone-using-a2a.md) (anecdote); [Glean](../research/sources/glean-agents-as-mcp-tools.md) (vendor claim) |

Key questions (continuing the existing numbering):

8. Which systems must the intent-shaping agent reach (Jira and Confluence, ServiceNow, Salesforce, Workday, internal services), and does each expose MCP, an A2A agent endpoint, or only APIs, at which A2A version (0.3 or 1.0)? — *answered by:* system inventory with platform owners; vendor docs check — *affects:* SaaS agent endpoint, A2A agent, agent behind MCP, vendor API
9. Where will the intent-shaping agent be called from: a coding harness (no A2A client except Gemini CLI), an enterprise agent host (Gemini Enterprise, Copilot Studio, Agentforce, ServiceNow), or our own surface? This is the A2A-specific form of Geoff's open Q7, still open. — *answered by:* user interviews; usage data — *affects:* all A2A options vs MCP
10. Does our audit and gateway plane see A2A traffic as well as MCP, given that ServiceNow's AI Gateway covers MCP only? — *answered by:* security architect; gateway vendor trial — *affects:* all A2A options
11. When a remote agent's answer feeds intent shaping, how is its provenance carried and checked (Eon had to invent a `DataContext` extension), and what happens on empty or failed remote responses? — *answered by:* prototype with one remote agent and injected failures — *affects:* A2A, agent behind MCP, SaaS agent endpoint
12. Which sensitive actions need out-of-band human approval when a remote agent is in the loop (Unit 42's mitigation), and can the chosen host do that? — *answered by:* threat-model workshop; host feature check — *affects:* all remote options

**Lean (unchanged in direction, with stronger grounds).** For calls from general harnesses, the evidence still favours MCP (sync, or Tasks for long jobs) and vendor APIs over A2A:
- Claude Code, Codex and Copilot have no A2A client, and OpenAI has declined to add one.
- MCP downloads are about 22 times higher.
- A2A's production evidence is one first-party account.

A2A is a live option for reaching SaaS agent endpoints (notably Rovo for PM data) from enterprise agent hosts. The lean would change if:
- Claude Code or Codex ships an A2A client;
- a system we must reach exposes its capability only as an A2A agent;
- an independent production account with volumes appears.

### agent-identity-delegation

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| User-delegated OAuth over A2A | The A2A server authenticates the end user by OAuth (PKCE, DCR) and acts within that user's existing permissions; an admin can disable it | Atlassian Rovo A2A gateway | Clear attribution; no privilege beyond the user's; admin kill switch | Only inbound to Atlassian; DCR required; audit of A2A calls not documented; per-user consent | early-adopter | [Atlassian](../research/sources/atlassian-rovo-a2a-gateway-docs.md) (first-party) |
| Per-connection service credential for A2A | Each external agent is configured with one OAuth client or API key; the remote acts as a service | ServiceNow AI Agent Studio; Copilot Studio (None/API key/OAuth) | Simple to set up | The asker's identity is lost; confused-deputy risk; A2A outside ServiceNow's AI Gateway | early-adopter | [ServiceNow](../research/sources/servicenow-community-action-fabric-mcp-a2a.md) (first-party); [Copilot Studio](../research/sources/microsoft-copilot-studio-a2a.md) (vendor claim) |
| User identity carried in A2A context (workaround) | Encode app, user and session into `context_id` so the remote can apply per-user rules | Eon | Works without spec changes | Not standard; spoofable unless the transport authenticates it; A2ABreak lists unprotected context IDs and multi-hop identity loss as spec-level vulnerabilities | emerging | [Eon](../research/sources/aaif-eon-a2a-into-production.md) (first-party); [A2ABreak](../research/sources/arxiv-a2abreak-security-analysis.md) (independent) |

Key questions:

13. Across a chain (our agent, then a SaaS agent endpoint, then that vendor's tools), can the end user's identity be propagated and checked at each hop, or does it collapse to a service identity? Is that acceptable to the policy owner in a regulated setting? — *answered by:* security/policy owner; prototype against Rovo A2A (user OAuth) and one API-key A2A agent — *affects:* all A2A rows; MCP per-server OAuth row
14. Do we require signed Agent Cards and a private registry or allow-list of remote agents, given that signing is optional in the spec and cards can carry injected instructions? — *answered by:* security architect; registry trial (Gemini Enterprise Agent Registry or our own) — *affects:* A2A card signing row, enterprise host row

### governance-control-plane

Key question:

- Does each control point (our MCP proxy, an enterprise AI gateway, the agent host's registry) cover every remote route we allow (MCP, A2A, vendor APIs), or do some routes bypass audit? — *answered by:* gateway inventory; vendor trial — *affects:* all remote-invocation options. Evidence: [ServiceNow](../research/sources/servicenow-community-action-fabric-mcp-a2a.md) (first-party); [Gemini Enterprise notes](../research/sources/gemini-enterprise-release-notes-a2a.md) (first-party).

## Could not verify / still thin

- **No independent production account and no volumes.** Nothing gives call counts, active agent counts or latency for any A2A deployment. Eon's account is first-party, on the foundation's blog.
- **Huawei and WeChat.** I could not confirm at a primary Huawei or Tencent source that the protocol is LF A2A. Huawei also has a telecom "A2A-T" and a HarmonyOS agent protocol. A Portuguese HDC 2026 snippet suggests HarmonyOS uses LF A2A.
- **PayPal and Google Cloud commerce.** GA status unknown; the original Google Cloud post was not filed.
- **Atlassian.** The body of the "Now GA" community post was unreadable. A2A audit logging is undocumented.
- **ServiceNow.** Official product docs were not read; endpoint paths differ between community posts.
- **Agentforce.** October 2026 status and developer docs not reached.
- **Not reached:** SAP Joule and Box (no primary source), Microsoft Azure AI Foundry customer stories, AWS AgentCore customer stories (the Axonius post was not checked for A2A).
- **Read only in part:**
  - A2ABreak: abstract only (spec version, vulnerability list and disclosure not read).
  - Gemini Enterprise release notes: first 100k of about 191k characters.
  - Semgrep audit checklist and Unit 42's full post-v1.0 relevance: not read.
  - arXiv 2609.01693 (MCP-to-A2A egress study, 2026-09-01): abstract only, not filed. It finds "PUBLIC - OK TO SHARE" labels associated with more verbatim egress in some models.
- **Cursor.** A forum request was found; whether Cursor ships anything A2A-related was not confirmed.
- **Unchecked claims.** That Gemini CLI is "deprecated and replaced by antigravity-cli" (HN claim). Laurie Voss's talk on agent protocols was not watched.
- **Download counts include CI**; npm, Maven and NuGet were not checked, and GitHub dependents are not available through the API.
- **Process note for the coordinator.** My first 11 note files were written by mistake to the shared checkout (`/Users/geoff/claude-home/project-agent-and-harness/research/sources/`) before the session switched to this worktree. Bash is blocked there, so I could not delete them. Their corrected copies are in this worktree. The shared-checkout strays to delete are:
  - `aaif-a2a-joins-aaif.md`
  - `a2a-project-joining-aaif.md`
  - `aaif-eon-a2a-into-production.md`
  - `atlassian-rovo-a2a-gateway-docs.md`
  - `servicenow-community-action-fabric-mcp-a2a.md`
  - `salesforce-agentforce-integration-pattern-api-mcp-a2a.md`
  - `kr-asia-wechat-phone-agents-a2a.md`
  - `unit42-agent-session-smuggling-a2a.md`
  - `semgrep-security-engineers-guide-a2a.md`
  - `arxiv-a2abreak-security-analysis.md`
  - `keysight-agent-card-poisoning.md`
