# Follow-up 2: community and independent reaction to Databricks Omnigent

Filed by research-runtime-patterns-follow-up-round, 2026-10-24. Builds on [Track 1](track-1-meta-harnesses.md) and the existing Omnigent notes. A menu and a map, not a recommendation.

## Question and scope

**Thin spot.** The synthesis found only vendor material on Omnigent: a 15-point HN thread, an Atlan explainer and the open issues. No one had reviewed it hands-on. This round looked for:

- independent hands-on reviews, and blog, video and podcast discussion;
- reaction on Reddit, X and LinkedIn;
- comparisons with Warp Oz, Conductor, Nx Polygraph and Vercel HarnessAgent;
- adoption signals: star trend, outside contributors, release cadence, current issue themes, named adopters;
- the Berkeley RDI talk;
- Anthropic and OpenAI reactions, including the terms for wrapping subscription CLIs;
- security critiques of the policy model;
- Databricks product status (Agent Bricks, Unity Catalog).

**Where I looked:**

- Web search (standard and extended);
- the GitHub REST and GraphQL APIs, read-only: repo, releases, contributors and their profile company fields, issue search, security advisories, discussions, commit activity;
- the Databricks docs, the Claude Code docs, Latent Space, Substack, DEV, SecureLayer7 and Help Net Security.

Reddit could not be fetched from this environment (blocked for both WebFetch and curl). X and LinkedIn were reached only through search snippets.

**Search terms:** "Omnigent meta-harness review hands-on"; "Omnigent Databricks reddit"; "site:reddit.com Omnigent"; "Omnigent" + Claude Code/Codex blog; Omnigent youtube demo; Omnigent Agent Bricks Unity Catalog; Berkeley RDI Omnigent talk; Omnigent vs Warp Oz / Conductor / HarnessAgent / Polygraph; Omnigent security critique / CVE; Omnigent "in production"; Anthropic third-party harness subscription OAuth terms; OpenAI Codex subscription third-party; Omnigent LinkedIn scepticism / lock-in.

## Findings

**Bottom line**

- **Independent hands-on evidence now exists, but it is thin and only covers one user.** One writer with no Databricks affiliation ran it ([Beach, 2026-08-31](../../research/sources/dataengineeringcentral-omnigent-hands-on.md), independent). The local single-user path worked, and he liked the policies best. The shared-server deploy failed on an undocumented `DATABASE_URL`, so he never reached the multi-user path. Nobody has published a review of the server, sharing, audit or policy effectiveness.
- **The best independent evidence about the governance model is in the security record, and it is mixed.** The maintainers published 13 advisories in four months, 4 of them critical ([advisories](../../research/sources/github-omnigent-security-advisories.md), first-party). Several reproduced bugs show policies silently failing open:
  - when the policy server errored (#536);
  - for the direct Codex harness, whose shell runs inside its own process (#5455);
  - for sub-agents (#7316);
  - for unparsed shell forms (CVE-2026-62676, [SecureLayer7](../../research/sources/securelayer7-cve-2026-62676-omnigent.md), independent).

  Each was fixed within days, and the fixes moved to deny-by-default.
- **Adoption looks real but is still centred on Databricks.** The repo has 11.0k stars, but growth has slowed (about 10.8k on 2026-10-12). Releases ship about weekly (v0.2.0 to v0.19.1), commits run at 200 to 500 a week, and about 675 new issues were opened in October, half of them by seven core accounts. The top ten committers are Databricks or MLflow staff. Outside evaluators are visible (SciChart, a multi-user pilot evaluator, a Kubernetes deployer), but no outside organisation has been named as running it in production ([repo follow-up](../../research/sources/github-omnigent-repo.md), first-party data, our analysis).
- **For a regulated audit setting, the issue tracker already names the gaps a trial would hit** ([identity and audit issues](../../research/sources/github-omnigent-identity-audit-issues.md), anecdote):
  - a shared session executes as its owner, so editors act with the owner's credentials;
  - there is no durable governance evidence timeline;
  - authorisation stops at authentication: no IdP group mapping, no SCIM, no audit trail;
  - an auditor "has to trust" the harness's own record.
- **The vendor terms are asymmetric.** Anthropic allows hosting the unmodified Claude Code binary with each user's own sign-in. It forbids third parties from collecting, storing or intermediating Claude.ai credentials ([Anthropic docs](../../research/sources/anthropic-claude-code-legal-and-compliance.md), first-party). A proposed Omnigent subscription token broker (#11493) appears to sit close to that line; that is our reading. OpenAI is permissive (secondary press). Neither vendor has commented on Omnigent itself. **Databricks does ship it as a product:** managed Omnigent is in Beta on Databricks, with workspace IdP, Unity Gateway, Databricks Sandboxes in select AWS regions, and CEL-only custom policies ([Databricks docs](../../research/sources/databricks-docs-omnigent-on-databricks.md), first-party).

**Reviews and commentary (all dates 2026)**

| Source | Date | Hands-on? | Evidence | Gist |
|---|---|---|---|---|
| [Data Engineering Central (Beach)](../../research/sources/dataengineeringcentral-omnigent-hands-on.md) | 08-31 | Yes, short | independent (Delta-sponsored post) | Easy install; Claude Code + Copilot detected; plain-language policies worked but were session-scoped; Polly orchestration "worked"; Railway server deploy failed (undocumented `DATABASE_URL`) |
| [SSD Nodes (Connor)](../../research/sources/ssdnodes-omnigent-multi-agent-harness.md) | 10-12 | Not stated | independent (sells VPS) | "Alpha means alpha"; releases broke documented commands; sandbox skips MCP servers and the supervisor; telemetry on by default; would not run on a host with production credentials |
| [SecureLayer7](../../research/sources/securelayer7-cve-2026-62676-omnigent.md) | 09-02 | Advisory analysis | independent | Shell parser fail-open: "the worst possible default for a security control" |
| [Latent Space AINews](../../research/sources/latent-space-ainews-meta-harness-summer.md) | 06-25 | No | independent | Calls the category "the harness of harnesses"; unsure Omnigent has MCP-like traction |
| [Superagentic MetaHarness](../../research/sources/superagentic-metaharness-omnigent.md) | 06-13 | Yes, smoke test | vendor-claim | Integrated as backend; friction with bundle layout, tmux, scratch files |
| [DEV (Lu)](../../research/sources/devto-renolu-omnigent-harness-for-harnesses.md), [MCP.Directory](../../research/sources/mcp-directory-omnigent-explained.md), [Help Net Security](../../research/sources/helpnetsecurity-omnigent-open-source.md) | 07 | No / unclear | anecdote | Explainers; Windows degraded mode; a commenter warns meta-harnesses "get risky fast" by multiplying tool access |
| [Orchestra (Lu)](../../research/sources/orchestra-databricks-omnigent-lock-in.md) | 06-14 | No | anecdote (adjacent vendor) | Only explicit lock-in scepticism, by analogy to Unity Catalog |
| [Latent Space podcast (Zaharia, Xin)](../../research/sources/latent-space-databricks-zaharia-xin.md) | 06-24 | Builder | first-party | Built for security approval, sharing and vendor API churn; claimed about half of the first ~400 merged PRs came from outside Databricks |

**Reddit, X, LinkedIn, YouTube and podcasts.**

- **Reddit:** no thread was found. There is a cross-post on r/machinelearningnews (MarkTechPost, 2026-06-14), and MCP.Directory relays one Reddit question ("What can you do with it that you can't do with good ol Claude Code, Codex, or Genie Code?"). Neither could be read directly.
- **LinkedIn:** the visible posts are by Databricks staff, plus one Databricks MVP community post ("If you haven't tried Omnigent yet, you are missing out"). No critical LinkedIn post was found.
- **YouTube:** no review or demo video was found.
- **Podcasts:** Latent Space only, first-party.

**Comparisons.** No independent source compares Omnigent with Warp Oz, Conductor, Nx Polygraph or Vercel HarnessAgent. AINews lists Conductor, ACP, Flue and HarnessAgent as lineage without evaluating them. SSD Nodes and MCP.Directory separate Omnigent from MCP gateways ("what an agent can reach" versus "which agent runs, under what limits"). A HN commenter likened it to kandev. Comparisons therefore remain our own (Track 1 table).

**Berkeley RDI talk.** According to search summaries, Databricks engineers Aravind Segu and Dhruv Gupta ran a 40-minute live demo at the Agentic AI Summit (UC Berkeley, 2026-08-01/02). Zaharia did not present there. The only write-up (Adnan Masood, Medium) returned 403. A tracker post (SEMS, discussion #1434, 2026-08-29) independently mentions "the recent workshop from Aravind and Dhruv". The "8,000 stars / 3,000+ Databricks engineers" figures remain second-hand and unverified.

**Anthropic and OpenAI.**

- **Anthropic:** its Claude Code legal page (first-party, undated) allows platforms to host the unmodified binary. Each end user authenticates with their own key, plan or 3P credential, with no intermediating and no storing of Claude.ai tokens. Pro/Max limits "assume ordinary, individual usage". HIPAA configuration excludes Claude Code routed through a gateway. Omnigent's README offers "Claude Pro/Max or ChatGPT plan, via the official `claude` / `codex` CLIs", which fits the user-signs-in-to-the-binary case.
- **Inside the tracker:** issue #11493 (2026-10-24) proposes storing the user's `claude setup-token` token server-side and vending it to sandboxes. Discussion #1133 (2026-06-24) asks whether Omnigent breaches Anthropic's terms and has no answer. Issue #857 proposes failover "across pooled provider credentials".
- **OpenAI:** it lets ChatGPT plans power third-party tools ("Sign in with ChatGPT", September 2026, per The New Stack). This is secondary press and was not filed.
- No reaction from either vendor to Omnigent itself was found.

**Product status.** Managed Omnigent is in Beta on Databricks (docs updated 2026-09-28). The details:

- a Databricks-operated server tied to the workspace IdP;
- models only via Foundation Model APIs and Unity Gateway, with no bring-your-own keys on Sandbox hosts;
- built-in and CEL policies, no custom Python;
- Sandbox only in select AWS regions, and not with serverless egress control.

Search summaries of Agent Bricks pages mention contextual policies enforced through Unity AI Gateway and MLflow tracing. No fetched page confirms Omnigent is part of Agent Bricks.

## What changed for the taxonomy

- **P4 meta-harness (horizontal), maturity:** stays *emerging*. The evidence label moves from "vendor only" to "vendor plus independent security record plus one short independent trial". The security record should be cited as the main independent signal on P4's governance claims.
- **P4 should split into two Omnigent variants with different trade-offs:** self-run OSS (alpha, full policy expressiveness including Python, any model or sandbox) and vendor-managed on Databricks (Beta, CEL-only, Databricks models and sandboxes, workspace IdP). The managed variant is closer to "hosted control plane" (Warp Oz) than to a self-run server.
- **Governance axis:** a new property should be recorded for every control-plane option: **enforcement seam and failure mode.**
  - A policy above the harness sees only what the harness exposes through hooks or tool events.
  - Harness-internal shells, sub-agents, and policy-server outages were all silent bypasses at some point.
  - The useful comparison is "fails open or closed, and is the seam the same for every harness?", rather than "policy above harness: yes or no".

  This bears on P4, P5 (Cloudflare's capability model, where Kenton Varda argues per-agent permissioning "does not scale") and P1 (Claude Code hooks).
- **Session-sharing axis (P8):** Omnigent's maintainers chose the invariant "a shared session always executes as its owner". This is a concrete design option for shared sessions in a regulated setting (attribution identity separate from execution identity). The SciChart account warns against per-message acting identity: about six weeks to build, removed after privilege escalation.
- **Terms:** no new term needed. "Meta-harness" in the horizontal sense is confirmed as common usage by independent commentary (AINews: "the harness of harnesses"). I propose the theme slug `policy-enforcement-fail-open` for the new idea; this is a coined label, see THEMES below.
- **Trial design (Geoff approved a short Omnigent trial as proposed work):** the evidence now says what the trial must test, in the order the tracker suggests it will fail:
  1. Server deploy with OIDC (Entra issue #11417).
  2. Fail-closed behaviour when the policy server is down.
  3. The same policy enforced identically on Claude Code, Codex (native and direct) and sub-agents.
  4. Whether the audit evidence for one session tree is reconstructable without an external tracing backend.
  5. Shared-session credential behaviour.
  6. Subscription versus API-key auth against Anthropic's terms.
  7. Upkeep: how often a Claude Code or Codex update breaks the bridge over two weeks.

## Proposed INDEX lines

- [Omnigent. Too afraid to ask what a meta-harness for Agents is?](sources/dataengineeringcentral-omnigent-hands-on.md) · article · 2026-08-31 · relevance high · Only independent hands-on account: local path and policies worked, shared-server deploy failed · https://dataengineeringcentral.substack.com/p/omnigent-too-afraid-to-ask-what-a
- [Omnigent: one harness for many agent CLIs](sources/ssdnodes-omnigent-multi-agent-harness.md) · article · 2026-10-12 · relevance medium · Independent self-host guide: alpha in practice, breaking releases, "I would not" list · https://www.ssdnodes.com/learn/omnigent-multi-agent-harness
- [omnigent-ai/omnigent security advisories and policy-bypass issues](sources/github-omnigent-security-advisories.md) · docs · 2026-10-14 · relevance high · 13 advisories (4 critical) and reproduced policy fail-open bugs, all fixed fast · https://github.com/omnigent-ai/omnigent/security/advisories
- [CVE-2026-62676: omnigent Shell-Command Parser Fails Open](sources/securelayer7-cve-2026-62676-omnigent.md) · article · 2026-09-02 · relevance medium · Independent analysis of the guardrail fail-open CVE · https://securelayer7.net/lab/cve-2026-62676-omnigent-shell-parser-fails-open-policy-bypass
- [omnigent-ai/omnigent issues on shared-session identity, audit evidence and enterprise authorisation](sources/github-omnigent-identity-audit-issues.md) · other · 2026-10-24 · relevance high · Evaluators (SciChart et al.) on owner-identity execution, missing audit timeline, no SCIM/group mapping, subscription token broker · https://github.com/omnigent-ai/omnigent/issues/2150
- [Claude Code docs: Legal and compliance](sources/anthropic-claude-code-legal-and-compliance.md) · docs · unknown · relevance high · Anthropic's rules for hosting Claude Code and subscription OAuth in third-party layers · https://code.claude.com/docs/en/legal-and-compliance
- [Omnigent on Databricks (AWS docs)](sources/databricks-docs-omnigent-on-databricks.md) · docs · 2026-09-28 · relevance high · Managed Omnigent in Beta: workspace IdP, Unity Gateway, CEL-only policies, AWS-region Sandboxes · https://docs.databricks.com/aws/en/omnigent/
- [Why the Frontier Ecosystem must be Open — Matei Zaharia and Reynold Xin](sources/latent-space-databricks-zaharia-xin.md) · podcast · 2026-06-24 · relevance medium · Builder's motivation for Omnigent; claim of ~half outside PRs at launch · https://latent.space/p/databricks
- [[AINews] It's Meta-Harness Summer](sources/latent-space-ainews-meta-harness-summer.md) · article · 2026-06-25 · relevance medium · Independent framing of "the harness of harnesses" and lineage; unsure of Omnigent's traction · https://www.latent.space/p/ainews-its-meta-harness-summer
- [Omnigent is a harness for your harnesses](sources/devto-renolu-omnigent-harness-for-harnesses.md) · article · 2026-07-01 · relevance low · Community explainer; commenter warns meta-harnesses multiply tool access · https://dev.to/renolu/omnigent-is-a-harness-for-your-harnesses-one-layer-over-claude-code-codex-and-the-rest-16d7
- [Databricks announce Omnigent (Orchestra newsletter)](sources/orchestra-databricks-omnigent-lock-in.md) · article · 2026-06-14 · relevance low · Only explicit lock-in scepticism, by analogy to Unity Catalog · https://orchestra.substack.com/p/databricks-announce-omnigent-anthropics
- [Optimizing Databricks Omnigent Agents with MetaHarness](sources/superagentic-metaharness-omnigent.md) · article · 2026-06-13 · relevance low · Third-party optimiser integration; practical friction · https://shashikantjagtap.net/optimizing-databricks-omnigent-agents-with-metaharness/
- [Omnigent: The Meta-Harness Explained (2026)](sources/mcp-directory-omnigent-explained.md) · article · 2026-07 · relevance low · Explainer; relays Reddit "what can it do that Claude Code can't?" · https://mcp.directory/blog/omnigent-meta-harness-2026
- [Omnigent: Open-source AI agent framework and meta-harness](sources/helpnetsecurity-omnigent-open-source.md) · article · 2026-07-06 · relevance low · Security press feature summary, no testing · https://www.helpnetsecurity.com/2026/07/06/omnigent-open-source-ai-agent-framework/

(Amended, no new INDEX line: [github-omnigent-repo](../../research/sources/github-omnigent-repo.md) has a new "Follow-up (2026-10-24)" section with adoption statistics.)

## Proposed THEMES bullets

**New theme proposed:** `## policy-enforcement-fail-open: Agent policy layers that fail open`. Policy and governance layers above or inside agent harnesses enforce only at the seams they hook, and gaps (errors, unparsed actions, harness-internal tools, sub-agents) have defaulted to allow. In a regulated setting, whether a control fails open or closed matters as much as what it expresses. Justification: none of the existing themes (`identity-delegation`, `skill-supply-chain-security`, `evals-autonomy-trust`, `human-review-gates`) covers whether enforcement itself holds. This label is our coinage.

policy-enforcement-fail-open
- [omnigent-ai/omnigent security advisories and policy-bypass issues](sources/github-omnigent-security-advisories.md): policy hook failed open on server errors (#536), not enforced for direct Codex (#5455), skipped for sub-agents (#7316), bypassed by command wrappers (#3557); 13 advisories in four months (research-runtime-patterns-follow-up-round)
- [CVE-2026-62676 (SecureLayer7)](sources/securelayer7-cve-2026-62676-omnigent.md): independent analysis; unparsed shell forms resolved to allow; fixed by deny-by-default in 0.3.0 (research-runtime-patterns-follow-up-round)
- [Omnigent identity/audit issues](sources/github-omnigent-identity-audit-issues.md): discussion #5931 argues policies are not narrowed across sub-agent hand-offs and the allow record lives in the harness, so an auditor "has to trust it rather than verify it" (research-runtime-patterns-follow-up-round)

meta-harness
- [Data Engineering Central (Beach)](sources/dataengineeringcentral-omnigent-hands-on.md): only independent hands-on account; local path and policies worked, shared-server deploy failed on an undocumented env var (research-runtime-patterns-follow-up-round)
- [SSD Nodes](sources/ssdnodes-omnigent-multi-agent-harness.md): "The cost is the layer itself"; releases broke documented commands; would not run with production credentials on the host (research-runtime-patterns-follow-up-round)
- [Latent Space AINews](sources/latent-space-ainews-meta-harness-summer.md): independent use of "the harness of harnesses" for the horizontal sense; unsure Omnigent has MCP-like traction (research-runtime-patterns-follow-up-round)
- [Omnigent on Databricks docs](sources/databricks-docs-omnigent-on-databricks.md): managed Omnigent in Beta with workspace IdP, Unity Gateway, CEL-only policies (research-runtime-patterns-follow-up-round)
- [github-omnigent-repo follow-up](sources/github-omnigent-repo.md): 11.0k stars with slowing growth, weekly 0.x releases, top-ten committers Databricks/MLflow staff, ~675 new issues in October (research-runtime-patterns-follow-up-round)

identity-delegation
- [Omnigent identity/audit issues](sources/github-omnigent-identity-audit-issues.md): shared sessions execute as the owner (editors act with owner credentials); SciChart built per-message acting identity and removed it after privilege escalation; no IdP group mapping or SCIM (#10359) (research-runtime-patterns-follow-up-round)
- [Claude Code legal and compliance](sources/anthropic-claude-code-legal-and-compliance.md): third parties may not collect, store or intermediate Claude.ai credentials; each end user authenticates with own key/plan (research-runtime-patterns-follow-up-round)

shared-persistent-sessions
- [Omnigent identity/audit issues](sources/github-omnigent-identity-audit-issues.md): maintainer invariant "a shared session always executes as its owner", attribution separate from execution identity; chat vs host access not separated (#11413) (research-runtime-patterns-follow-up-round)

harness-portability
- [Claude Code legal and compliance](sources/anthropic-claude-code-legal-and-compliance.md): wrapping Claude Code is allowed only as the unmodified binary with users' own credentials; HIPAA configuration excludes Claude Code routed through a gateway (research-runtime-patterns-follow-up-round)

vendor-claims-vs-independent-evidence
- [Data Engineering Central (Beach)](sources/dataengineeringcentral-omnigent-hands-on.md): four months after launch, one short independent trial is the only hands-on review found; no Reddit, YouTube or comparative review (research-runtime-patterns-follow-up-round)

## Proposed DIMENSIONS additions

### harness-layering

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Vendor-managed meta-harness on a data platform | The data-platform vendor operates the meta-harness server, sandboxes and model gateway inside the customer's workspace; vendor CLIs are still the agents | Omnigent on Databricks (Beta) | No server to run; workspace IdP; models and policies routed through the platform's gateway | CEL-only custom policies (no Python); models only via Databricks (no own keys on Sandbox hosts); Sandbox only in select AWS regions; ties the layer to one data platform; no audit, pricing or GA details published | emerging | [Databricks docs](../research/sources/databricks-docs-omnigent-on-databricks.md) (first-party); [Orchestra](../research/sources/orchestra-databricks-omnigent-lock-in.md) (anecdote, lock-in scepticism) |

Evidence update for the existing row "Meta-harness server above many harnesses (self-run)": add [Beach hands-on](../research/sources/dataengineeringcentral-omnigent-hands-on.md) (independent; local path works, server deploy failed), [SSD Nodes](../research/sources/ssdnodes-omnigent-multi-agent-harness.md) (independent; breaking 0.x releases), [security advisories](../research/sources/github-omnigent-security-advisories.md) (first-party; 13 advisories, 4 critical) and [repo follow-up](../research/sources/github-omnigent-repo.md) (adoption statistics). Maturity stays emerging.

Key questions:
1. Answer to existing Q17 (is independent evidence thin by nature, or have we not found it?): as of 2026-10-24 it is genuinely thin. There is one short independent trial, one independent CVE analysis, no comparative review and no named outside production adopter. The tracker shows outside evaluators (SciChart, a multi-user pilot), and Databricks is the only confirmed heavy user. The rest of Q17 stays open: ask Databricks for reference customers and interview SciChart-type evaluators. — *answered by:* Databricks briefing; adopter interviews — *affects:* meta-harness server, vendor-managed meta-harness
2. Would we run Omnigent self-hosted (full policy expressiveness, any model, our ops and patching burden at about weekly 0.x releases) or Databricks-managed (less ops, CEL-only policies, Databricks models and regions)? Does our company already have a Databricks workspace in a supported region? — *answered by:* platform owner; procurement check — *affects:* self-run vs vendor-managed meta-harness
3. How often does a Claude Code or Codex update break the layer's terminal bridge, and how long until a fix ships? Most open issues on 2026-10-23/24 concern the Claude-native and Codex-native bridges. — *answered by:* two-week trial logging each break against vendor CLI versions — *affects:* all meta-harness options (links to harness-upkeep)

### governance-control-plane

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Fail-closed policy enforcement with harness-uniform seams (requirement, not a product) | A control plane that denies when the policy engine is unreachable or the action cannot be parsed, and enforces the same policy through the same seam for every harness and sub-agent | Omnigent after fixes (deny-by-default shell parsing from 0.3.0; fixes for #536, #5455, #7316); no product publishes it as a guarantee | Controls that hold under errors and across harnesses; testable in a trial | More false denials and friction; harness-internal tools (e.g. Codex's own shell) may be invisible to the layer unless the harness is sandboxed or run in a mode that surfaces tool calls; must be re-verified at each release | emerging | [advisories](../research/sources/github-omnigent-security-advisories.md) (first-party); [SecureLayer7](../research/sources/securelayer7-cve-2026-62676-omnigent.md) (independent) |
| Verifiable audit log outside the harness | Policy decisions, approvals, agent switches and child sessions recorded in one durable, tamper-evident timeline that an auditor can verify without trusting the harness | Requested in Omnigent #5670 (open); a third party claims a hash-chained log running on Omnigent 0.11.0 (discussion #5931) | Audit evidence for a regulated setting; incident review | Not shipped in Omnigent; today needs an external tracing backend (MLflow spans on Databricks, per search summaries); third-party claim unverified | emerging | [identity/audit issues](../research/sources/github-omnigent-identity-audit-issues.md) (anecdote; includes a vendor claim) |

Key questions:
1. Does each candidate control plane fail closed when its policy engine is slow or down, and does one policy produce the same result on Claude Code, Codex (native and direct) and sub-agents? Omnigent failed each of these at least once (fixed). — *answered by:* red-team script in the Omnigent trial (kill the policy server; run the same deny-rule across harnesses and a spawned sub-agent) — *affects:* stateful session policies, hosted control plane, deterministic gates
2. Can an auditor reconstruct "every allow, deny and ask decision for this session tree, and who approved it" from the product alone, in a format our audit function accepts? — *answered by:* policy/audit owner reviews a trial session's export; Omnigent #5670 status — *affects:* stateful session policies, verifiable audit log
3. Which policy expressiveness do we need: built-in plus CEL (Databricks-managed) or arbitrary Python (self-run, which has had RCE advisories via policy and tool handlers)? — *answered by:* threat model of intent-shaping job steps; security owner — *affects:* self-run vs vendor-managed meta-harness
4. What is our tolerance for a 0.x component with 13 security advisories in four months (fixed within days)? Is fast disclosure a positive signal or a disqualifier for our security review? — *answered by:* security owner — *affects:* meta-harness server options

### agent-identity-delegation

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Shared session executes as owner; authorship is attribution only | Collaborators can see and steer a shared session, but every tool call runs with the owner's credentials; message author is shown to the model but never changes authority; only the owner approves tool calls | Omnigent maintainer proposal on #2150 (2026-07-28) | Simple, predictable credential model; avoids privilege escalation from per-message identity | Editors effectively act as the owner (impersonation risk for git, Slack, Atlassian); audit must record who typed and who executed separately; approvals bottleneck on the owner | emerging | [identity/audit issues](../research/sources/github-omnigent-identity-audit-issues.md) (anecdote + maintainer first-party) |
| Per-message acting identity | Each tool call authorised as the human who sent the latest message | SciChart's SciClawd (built, then removed June 2026) | Least-privilege per human | About six weeks to build; fought the harness boundary; produced privilege escalation even when identity looked correct; removed | emerging (abandoned by one adopter) | [identity/audit issues](../research/sources/github-omnigent-identity-audit-issues.md) (anecdote, first-person adopter) |

Key questions:
1. In a regulated setting, may a collaborator in a shared agent session cause actions under the owner's credentials, or must each action run under the actor's own identity? Do our audit rules require both identities to be logged? — *answered by:* policy/identity owner — *affects:* both rows; session-persistence-sharing
2. Can the layer map IdP groups to roles and provision via SCIM, or are admins and entitlements maintained by hand (Omnigent #10359)? — *answered by:* trial against our IdP (incl. Entra, #11417) — *affects:* meta-harness server, vendor-managed meta-harness

### model-provider-coupling

Key questions:
1. Which credential model would a company-internal layer use for Claude Code: users signing in to the unmodified binary with their own Team/Enterprise seat, or org API keys? Does any feature (e.g. a server-side subscription token broker as in Omnigent #11493, or pooled credentials as in #857) conflict with Anthropic's rule that third parties may not "collect, store, or intermediate Claude.ai credentials"? OpenAI's stance is more permissive, so the two vendors need different answers. — *answered by:* legal/procurement review of Anthropic Commercial Terms; Anthropic account team — *affects:* all meta-harness options, hosted control plane

## Could not verify / still thin

- **Reddit:** both fetch paths were blocked. No r/ClaudeAI, r/LocalLLaMA or r/databricks thread found via search. One relayed question (MCP.Directory) and a MarkTechPost cross-post were seen only second-hand.
- **X and LinkedIn:** search snippets only. No critical non-Databricks post found. Absence in search is not absence.
- **YouTube:** no demo or review found. The Berkeley RDI talk recording and the Masood write-up (403) were not read. The speaker names come from search summaries corroborated by a tracker post. "8,000 stars" and "3,000+ Databricks engineers" remain unverified.
- **Star trend:** the stargazer timestamp API was unavailable, so the trend rests on three points from different sources.
- **Contributor affiliation:** inferred from profile company fields and handles. Unsponsored individual contributions cannot be told apart from employer-sponsored ones.
- **Named adopters:** none in production outside Databricks/Neon. SciChart is "experimenting". Others are unnamed or unaffiliated.
- **Anthropic/OpenAI on Omnigent:** no statement found. Whether #11493's token broker breaches Anthropic's terms is our reading. The page is undated, and the February 2026 terms change and OpenAI's "Sign in with ChatGPT" come from secondary press (not filed).
- **Databricks product:** no fetched page confirms Omnigent is part of Agent Bricks. Audit logging, pricing, Azure/GCP and GA are undocumented on the page read. MLflow tracing of sessions comes from search summaries only.
- **Comparisons:** no independent comparison with Warp Oz, Conductor, Nx Polygraph or Vercel HarnessAgent exists.
- **Policy effectiveness:** no false-positive or incident-reduction data for contextual policies from anyone.
