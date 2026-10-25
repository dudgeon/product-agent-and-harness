# Track 1: Meta-harnesses and harness-agnostic layers

Filed by research-agent-runtime-patterns-taxonomy, 2026-10-24. Plan: [00-research-plan.md](00-research-plan.md). This is a menu and a map, not a recommendation. Evidence is marked vendor claim / independent / first-party / anecdote throughout; this field moves monthly, so dates are given.

## 1. Headline findings

1. **"Meta-harness" is a real but unsettled term, with two senses.** Horizontal: a layer above several agent harnesses (Omnigent, Warp Oz, Polygraph, local parallel-session managers). Vertical: a system that optimises one harness's code (Stanford/Khattab/Finn paper, arXiv 2026-03-30). No standards body or neutral definition exists; an independent buyer's guide says so explicitly ([CodePick](../../research/sources/codepick-meta-harness-guide.md)). First-party use predates Omnigent: Anthropic called Managed Agents "a meta-harness" on 2026-04-08 ([Anthropic](../../research/sources/anthropic-scaling-managed-agents.md)); Databricks coined its headline use on 2026-06-13.
2. **Omnigent (Databricks) is the clearest horizontal example, and it is alpha.** Apache-2.0, ~11k stars, runner + server, 13+ harnesses, 12 sandbox providers, stateful policies, shared sessions. Independent evidence is thin: the HN launch drew 15 points, and the repo's open issues (all opened 2026-10-23/24) include sharing that does not separate chat access from host access, stuck-running sessions, opaque auth failures and Entra OIDC login failing. No third-party hands-on review found.
3. **Cloudflare OS is not a meta-harness.** It is an org-deployable per-employee agent workspace (persistent, shared, governed) with its own Code Mode agent on Pi, built on Durable Objects, Dynamic Workers and Gatekeepers. It does not wrap Claude Code or Codex. It is the best example in this track of the deployed/shared/persistent end, and its security model (zero ambient access, typed bindings, an observation log that re-checks a later viewer's access) is the most distinctive idea found. It drew real independent discussion (668 points, 330 comments) with lock-in, naming and sandbox-hardness critiques and early deployment problems.
4. **Cloudflare's wider "agentic cloud" (Agents Week, 2026-04-14 to 20)** is an infrastructure play: Sandboxes GA, Artifacts (Git for agents), Workflows v2, Mesh, Managed OAuth, Agent Memory, Project Think, then Flue and an Agents SDK that any harness can target (2026-06-17). Its three-layer vocabulary (framework / harness / runtime) is useful. It positions Claude Code as "second wave", laptop-bound. A Sandbox guide does exist for running Claude Code/Codex in a per-task sandbox.
5. **The category has many shapes.** At least six distinct things are called a meta-harness or sit in the layer: server-level governance layers, hosted control planes, SDK-level adapters, DIY CLI coordinators, local parallel-session managers, and model-vendor hosted services. They solve different problems and should not be compared as one product class.
6. **Supplier risk is already visible.** Vibe Kanban's company shut down 2026-04-10 for lack of a business model (local tool continues, community maintained). Sandbox vendors are changing hands (Baseten-Blaxel, 2026-09-10).

## 2. Vocabulary other sources use

| Term | Used by | Meaning |
|---|---|---|
| meta-harness (horizontal) | Databricks Omnigent, Nx Polygraph, Anthropic (Managed Agents), CodePick, Vaughan, Franke, Warp (says "control plane") | Layer above or around harnesses |
| meta-harness (vertical) | Stanford paper, HarnessX, HyperAgents | Optimiser of harness code |
| control plane | Warp Oz, Atlan on Omnigent | Governance + orchestration over agents |
| harness / framework / runtime | Cloudflare Flue post | Loop / project structure + DX / compute, state, storage |
| agentic cloud / agent cloud | Cloudflare (blog says "agentic cloud"; press says "agent cloud") | Infrastructure for agents as primary workload |
| agent OS / agentic OS | Cloudflare OS, Google Gemini Enterprise Agent Platform commentary, Lyzr | Platform layer for agent runtime + governance (marketing-heavy; HN disputes "OS") |
| orchestrator / conductor / multiplexer | Conductor, Claude Squad, Superset | Local parallel sessions in worktrees |
| ACP ("LSP for agents") | Zed, JetBrains | Editor-to-agent protocol, not governance |

## 3. Comparison table

Evidence column: V = vendor claim, I = independent, F = first-party account, A = anecdote.

| Product | Layer / shape | Wraps Claude Code/Codex? | Runtime location | Sharing / persistence | Governance | Maturity (2026-10-24) | Evidence |
|---|---|---|---|---|---|---|---|
| [Omnigent](../../research/sources/github-omnigent-repo.md) (Databricks) | Meta-harness: runner + server | Yes, plus ~11 others | Local, Modal, Daytona, E2B, K8s and more | URL sharing, attach, fork, import | Stateful policies, cost caps, OS sandbox | Alpha OSS; Beta on Databricks | V; issues F |
| [Warp Oz](../../research/sources/warp-oz-multi-harness.md) | Hosted multi-harness control plane | Yes (Claude Code, Codex) | Cloud, self-hosted K8s/Docker | Shareable run transcripts; memory in research preview | Access, audit, credit caps | Beta (2026-05) | V |
| [Anthropic Managed Agents](../../research/sources/anthropic-scaling-managed-agents.md) | Hosted harness/session/sandbox | Claude's own; calls itself a meta-harness | Anthropic cloud | Durable session log | Credential vault | Public beta (2026-04) | F + V |
| [Vercel HarnessAgent](../../research/sources/vercel-ai-sdk-harnesses.md) | SDK-level adapter | Yes (Claude Code, Codex, Pi, later others) | Sandboxes per adapter | Resumable sessions | Per adapter | Experimental | V |
| [Cloudflare OS](../../research/sources/cloudflare-os-announcement.md) | Org-deployed agent workspace | No (own Code Mode agent on Pi) | Cloudflare Workers / DOs | Persistent workspaces, shareable apps/blueprints | Capabilities, Gatekeepers, observation log | Early access, v2 | V; HN A |
| [Cloudflare Agents SDK / Think / Flue](../../research/sources/cloudflare-flue-agents-platform.md) | Runtime + framework + harness | Not claimed | Edge | Durable fibers, tree sessions | Platform | Beta / experimental | V |
| [Nx Polygraph](../../research/sources/nx-polygraph-meta-harness.md) | Meta-harness (cross-repo, session graph) | Agent-agnostic, none named | Not stated | Session graph | Not stated | Announced 2026-06-26 | V |
| [Zed ACP + registry](../../research/sources/zed-agent-client-protocol.md) | Editor-to-agent protocol | Via adapters | Local | None | None | Protocol live; registry beta (2026-01) | V |
| [Conductor](../../research/sources/conductor-build-homepage.md), [Claude Squad](../../research/sources/github-claude-squad.md), Superset | Local parallel sessions | Yes | Own machine | None | None | Mainstream among early adopters | V, A |
| [Vibe Kanban](../../research/sources/vibekanban-shutdown.md) | Kanban over parallel agents | Yes | Local | Hosted sharing removed | None | Company shut down 2026-04-10 | F |
| [Pi-based DIY coordinator](../../research/sources/danielvaughan-meta-harness-pattern-pi.md) | CLI composition | Yes (`claude -p`, `codex exec`) | Local / CI | Workspace files | Bypasses approvals | Practitioner pattern | I |
| [Sandbox providers](../../research/sources/rywalker-ai-agent-sandboxes.md) (E2B, Modal, Daytona, Vercel, Cloudflare) | Session runtime | Run any harness inside | Vendor cloud | Snapshots vary | Egress often open | Beta to GA, churn | I (disclosed conflict) |

## 4. Patterns on the plan's axes

- **Where the runtime lives.** Three clusters: local (Conductor, Claude Squad), vendor/third-party cloud sandboxes (Omnigent managed hosts, Warp, Managed Agents, E2B/Modal/Daytona), and org-deployed on an infrastructure vendor (Cloudflare OS, Think). Omnigent spans the first two by design.
- **Who owns the harness.** Meta-harnesses deliberately leave the loop to vendors (Claude Code, Codex) and own the session API, policy and sharing. Cloudflare OS and Think own the loop. Anthropic does both: owns its harness and presents the hosted layer as a meta-harness.
- **Coupling.** Portability is mostly at the process boundary (launch a CLI, intercept its tool calls, drive a terminal in tmux) or at the SDK boundary (HarnessAgent). Both depend on each vendor's CLI behaviour; no interop standard exists (Vaughan: "no interop standard exists yet"). ACP standardises only the editor boundary.
- **Packaging.** Shared skills, rules and environments are carried across harnesses in Warp Oz; Omnigent uses YAML agent definitions; Cloudflare uses skill files plus apps/blueprints; Cloudflare's code reviewer uses AGENTS.md per repo.
- **Invocation.** Delegation by spawning CLIs (`claude -p`, `codex exec`), by sub-agent profiles, or by triggers (Slack, Linear, schedules, CI, API) in Warp Oz and Cloudflare apps.
- **Session locality, sharing, persistence.** The shift from private/ephemeral to shared/persistent is the main selling point of Omnigent, Warp, Polygraph and Cloudflare OS. Weak points show in the same sources: Omnigent's sharing-vs-host-access issue, per-user copies as maintenance burden (HN on Cloudflare OS), checkpoints that do not undo external effects (sandbox survey).
- **Governance.** Three distinct designs: stateful action policies (Omnigent), capability + observation-based access (Cloudflare OS), hosted allow/disable and audit (Warp). Gateways (AI Gateway) cover cost. None has published effectiveness data.
- **Structured vs unstructured fit.** Parallel-session managers suit quick, separable engineering tasks and degrade for large features (Franke); heterogeneous staged pipelines (implement then review by another vendor) work, tight edit-test loops do not (Vaughan). Cloudflare OS targets non-engineers' unstructured requests first (email alias), then productises repeated patterns. Cloudflare's code reviewer is the structured case: a risk-tiered pipeline as a CI component.

## 5. Maturity assessment

Nothing here is mainstream except local parallel-session managers. Omnigent is alpha with an active issue stream; Cloudflare OS v2 is early access; Warp multi-harness is beta; HarnessAgent is experimental; Managed Agents is public beta; ACP is the most standardised piece (JetBrains and Zed support) but covers only the editor boundary. Adoption evidence is almost entirely self-reported (Cloudflare "thousands of weekly users, 4,000 apps in 30 days, 10,000 hours saved"; Omnigent "3,000+ Databricks engineers" in a secondary talk write-up, not verified). The independent signals are: HN reaction (Cloudflare OS substantial, Omnigent minimal), practitioner write-ups of the pattern's failure modes, Vibe Kanban's shutdown, and the open issue list.

## 6. Trade-offs (from the sources)

- **Independence vs a new dependency.** A layer reduces vendor dependence but adds one more thing that must track each vendor's CLI (auth, terminal, hooks). Omnigent's issues show this cost.
- **Governance coverage vs bypass.** Policies hold only when agents are launched through the layer (Omnigent), and wrapper tools can bypass the harness's own approvals (Vaughan).
- **Cost.** Delegating across harnesses can multiply sessions (~23-25 internal sessions for one high-reasoning Codex delegation, Vaughan, practitioner estimate). Third-party harness inference is billed outside Warp's summaries.
- **Platform lock-in.** Cloudflare OS is open source but today depends on Cloudflare's PaaS (HN, repo); Managed Agents runs on Anthropic infrastructure; Omnigent's richer features sit on Databricks.
- **Supplier risk.** Small orchestration vendors can disappear (Vibe Kanban).
- **Security.** Sandbox egress is often open by default and injected credentials are readable by guest code (sandbox survey); Cloudflare's approach keeps credentials in Gatekeepers, Anthropic in a vault behind a proxy; HN contests workerd's hardness.

## 7. Options by dimension

I added options, evidence rows and key questions (unranked) to these sections of [options/DIMENSIONS.md](../../options/DIMENSIONS.md):

- [harness-ownership](../../options/DIMENSIONS.md#harness-ownership-who-owns-the-harness-the-agent-loop): seven options (self-run meta-harness server, hosted multi-harness control plane, vendor-hosted meta-harness, framework-level adapter, DIY coordinator, local parallel-session manager, platform-native own harness) and five questions.
- [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives): org-deployed workspace with capability security (Cloudflare OS), third-party sandbox per session; three questions.
- [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-permissions-cost-identity-audit): stateful session policies, zero-ambient-access plus observation log, hosted multi-harness control plane; three questions.
- [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-and-sharing): shared session over any harness, shareable apps with data-free blueprints; two questions.
- [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model): intake alias then skills with champions/interns (Cloudflare); one question.
- [target-user](../../options/DIMENSIONS.md#target-user-which-users-and-personas-we-serve-first): every employee incl. non-engineers; engineers running many agents; one question.
- [capability-packaging](../../options/DIMENSIONS.md#capability-packaging-how-skills-and-agents-are-packaged-and-invoked): task-specific pipeline as a CI component (Cloudflare code review); one question.

**Proposed structural changes:**
1. Split harness-ownership: "who owns the loop" is a different choice from "is there a layer above harnesses" (meta-harness). Suggest a new dimension `harness-layering` (layer over vendor harnesses: none / local manager / server / hosted control plane / SDK adapter), leaving harness-ownership for build-vs-embed-vs-use.
2. Merge session-persistence-sharing with the later session-handoff-portability and durability-substrate, or cross-link them clearly; the three overlap.
3. `governance-control-plane` now has 20+ rows; consider splitting identity-on-behalf-of (a cross-cutting dimension) from cost/policy/audit.
4. Rename "meta-harness" in options to the specific shape (see harness-layering) because the term covers six different products.

## 8. Source notes filed (Track 1)

Omnigent: [launch](../../research/sources/databricks-omnigent-meta-harness-launch.md), [repo + issues](../../research/sources/github-omnigent-repo.md), [contextual policies](../../research/sources/databricks-omnigent-contextual-policies.md), [Atlan explainer](../../research/sources/atlan-omnigent-explainer.md), [HN thread](../../research/sources/hn-omnigent-launch-thread.md).
Cloudflare: [Cloudflare OS](../../research/sources/cloudflare-os-announcement.md), [rollout post (Rhea)](../../research/sources/cloudflare-how-we-rethink-work-with-cloudflare-os.md), [repo](../../research/sources/github-cloudflare-os-repo.md), [HN thread](../../research/sources/hn-cloudflare-os-thread.md), [Agents Week recap](../../research/sources/cloudflare-agents-week-in-review.md), [Project Think](../../research/sources/cloudflare-project-think.md), [Flue / Agents SDK](../../research/sources/cloudflare-flue-agents-platform.md), [AI code review](../../research/sources/cloudflare-ai-code-review-opencode.md), [Sandbox docs](../../research/sources/cloudflare-sandbox-sdk-docs.md).
Others: [Anthropic Managed Agents (addendum)](../../research/sources/anthropic-scaling-managed-agents.md), [Zed ACP](../../research/sources/zed-agent-client-protocol.md), [ACP registry](../../research/sources/zed-acp-registry.md), [Vercel HarnessAgent](../../research/sources/vercel-ai-sdk-harnesses.md), [Warp Oz multi-harness](../../research/sources/warp-oz-multi-harness.md), [CodePick guide](../../research/sources/codepick-meta-harness-guide.md), [Vaughan](../../research/sources/danielvaughan-meta-harness-pattern-pi.md), [Franke](../../research/sources/garrit-meta-harness-parallel-agents.md), [Nx Polygraph](../../research/sources/nx-polygraph-meta-harness.md), [Meta-Harness paper](../../research/sources/arxiv-meta-harness-optimization.md), [Vibe Kanban shutdown](../../research/sources/vibekanban-shutdown.md), [Claude Squad](../../research/sources/github-claude-squad.md), [Conductor](../../research/sources/conductor-build-homepage.md), [sandbox survey](../../research/sources/rywalker-ai-agent-sandboxes.md).
Overlap noticed: another track filed [warp-oz-cloud-agents](../../research/sources/warp-oz-cloud-agents.md) (docs) and [anthropic-engineering-scaling-managed-agents](../../research/sources/anthropic-engineering-scaling-managed-agents.md) and [cdata-claude-managed-agents-meta-harness](../../research/sources/cdata-claude-managed-agents-meta-harness.md); I added my Anthropic addendum to the first Anthropic note and filed Warp's press release as a separate source. Suggest merging the two Anthropic notes.

## 9. Gaps and what I could not verify

- Omnigent: no independent hands-on review, Reddit/X/Discord not searched; harness support tiers come only from Atlan; Berkeley RDI talk claims (8,000 stars at the time, 3,000+ Databricks engineers) are second-hand. Runner/server internals are not documented on the pages fetched; how Claude Code and Codex are driven is only evidenced by tmux/native-TUI mentions.
- Cloudflare OS: the license is named in the repo only; the HN thread was sampled, not read in full; "10,000 hours saved" and "4,000 apps" are Cloudflare's own estimates. Sandbox SDK overall GA status not stated on the docs page; the coding-agents guide itself not read.
- Not researched in depth (searches only): Goose (existing low-relevance note covers the Block interview), OpenCode, Cline, Amp, Cursor SDK (public beta 2026-04-29, uses Cursor's own harness per commentary; no evidence found of it hosting Claude Code), Superset (source-available, per search summaries), Sculptor. Enterprise "agent OS" platforms (Google Gemini Enterprise Agent Platform, Lyzr, Microsoft, Glean, OpenAI Frontier) produced only vendor/analyst marketing; nothing filed.
- Sandbox provider claims: only the Tembo-CEO survey was filed; the superagent.sh benchmark has no documented methodology and was not filed.
