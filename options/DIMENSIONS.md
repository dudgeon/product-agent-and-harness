# Dimensions and options

The menu for the strategy deck: for each dimension, the options and the key questions that decide among them. Rules: [README.md](README.md). Sources: [../research/sources/](../research/sources/).

**Status:** Consolidated 2026-10-24 by the director per 01-synthesis.md D.0 (approved by Geoff)

Key-question numbers are kept from the sections they were filed in, so numbering inside a moved or merged section can skip. Each merged or split dimension has a "Formerly:" line naming the old slugs.

## Contents

(maintained by the director)

- [loop-source](#loop-source-who-supplies-the-agent-loop)
- [harness-layering](#harness-layering-is-there-a-layer-above-the-vendor-harnesses)
- [runtime-location](#runtime-location-where-the-agent-runtime-lives)
- [capability-format-portability](#capability-format-portability-capability-format-and-portability)
- [capability-distribution-trust](#capability-distribution-trust-capability-distribution-and-trust)
- [remote-invocation-route](#remote-invocation-route-how-a-primary-harness-reaches-a-remote-or-deployed-agent)
- [session-persistence-sharing](#session-persistence-sharing-session-persistence-sharing-and-handoff)
- [agent-identity-delegation](#agent-identity-delegation-agent-identity-and-delegation)
- [governance-control-plane](#governance-control-plane-governance-and-control-plane-policy-cost-audit)
- [durability-substrate](#durability-substrate-how-persistence-and-recovery-are-implemented)
- [model-provider-coupling](#model-provider-coupling-how-tightly-the-agent-is-coupled-to-one-model-provider)
- [harness-upkeep](#harness-upkeep-who-maintains-the-harness-over-time-and-at-what-cadence)
- [context-and-memory](#context-and-memory-context-and-memory)
- [artifact-and-project-structure](#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found)
- [target-user](#target-user-which-users-and-personas-we-serve-first-including-for-shared-agents)
- [target-outcome](#target-outcome-which-outcome-or-value-we-target)
- [pm-agent-evaluation](#pm-agent-evaluation-how-we-would-know-a-pm-agent-works)
- [sequencing](#sequencing-which-jobs-first-and-which-layer-first)
- [work-structure](#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent)
- [activity-classification](#activity-classification-how-we-classify-user-activity-for-agent-fit)
- [review-and-autonomy](#review-and-autonomy-review-and-autonomy)
- [intent-shaping-and-spec](#intent-shaping-and-spec-intent-shaping-mode-and-spec-standard)
- [adoption-model](#adoption-model-adoption-and-enablement-model)
- [Cross-cutting key questions](#cross-cutting-key-questions)

---

## loop-source: Who supplies the agent loop
**Choice:** Do users keep a vendor harness as the loop, do we embed a vendor's harness SDK in our own product, use a hosted harness, build on a general framework, fork an open harness, or write a minimal loop?
**Why it matters to the strategy:** It sets how dependent users are on one vendor's product and what we have to build and maintain; the evidence says the loop is cheap to build and its upkeep is not.
**Related themes:** [[harness-over-model]], [[build-vs-buy]], [[single-agent-many-skills]]   **Related dimensions:** [[harness-layering]], [[runtime-location]], [[model-provider-coupling]], [[harness-upkeep]], [[capability-format-portability]]
Formerly: harness-ownership (the loop-source rows and questions; the rows on layers above harnesses moved to [[harness-layering]], per 01-synthesis.md D.0)

### Original framing before the split — harness-ownership: Who owns the harness (the agent loop)
**Choice:** Do users keep working in a vendor harness (e.g. Claude Code), do we embed a vendor SDK in our own product, build on a framework, or put a meta-harness above existing harnesses?
**Why it matters to the strategy:** It sets how dependent users are on one vendor's product, what we have to build and maintain, and where standardised agents can live.
**Related themes:** [[harness-over-model]], [[build-vs-buy]], [[single-agent-many-skills]]   **Related dimensions:** [[runtime-location]], [[capability-format-portability]], [[capability-distribution-trust]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Use a vendor harness as is | Users work directly in Claude Code/Codex, extended by skills and subagents | Claude Code, Codex | Zero build; best-in-class loop | Tied to one vendor; local, private, ephemeral by default | mainstream | to be linked |
| Embed a vendor SDK in our own product | Own product and UX on a vendor's agent SDK | Ramp Glass on the Claude Agent SDK | Control of UX, memory, policy | Maintenance, a team to run it | early-adopter | [Glass teardown](../research/sources/x-sebgoddijn-glass-article.md) (first-party) |
| Build on an agent framework | Own harness from a framework | LangGraph, ADK, etc. (Track 2) | Maximum control, model-portable | Highest build cost; re-solves what vendor harnesses do | to be researched | to be researched |
| Embed vendor SDK, small core team (Glass detail) | Desktop app on the Claude Agent SDK; PM-led core team of 3-4 vibe-coded it with self-maintenance tooling (Defrag skill, design system, doc validation, pre-commit gates) | Ramp Glass | Own UX, memory, MCP proxy, Okta distribution | Fleet distribution/auth was called one of the hardest parts; codebase entropy; Ramp is a fast, AI-forward, engineering-heavy org | early-adopter | [Buchan build story](../research/sources/x-shanebuchan-how-we-built-glass.md) (first-party); [Charles AI-pilled](../research/sources/x-geoffintech-ai-pilled-article.md) (first-party; "team of four, under three months") |
| Build on top of own agent infra | Shared tool catalog, applied-AI service and sandboxed coding agent underneath many agents | Ramp Inspect, OmniChat | Reuse across agents; avoids duplicate agents | Needs a platform team and many tools | early-adopter | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party) |
| Embed a harness SDK, self-hosted (Agent SDK, Codex SDK) | Run the vendor's own harness as a library/subprocess inside our service; each session is a long-lived CLI process with local state | Claude Agent SDK, Codex SDK (app-server), OpenHands SDK | Vendor-grade loop, tools, permissions, hooks, subagents, skills without writing them; bundled binary pinned to SDK version | We own sandboxing, session storage (SessionStore), tenant isolation, scaling, OTel; Agent SDK is Claude-only; third-party products must use API keys, not claude.ai login; ~1 GiB RAM per concurrent agent as a floor; token cost dominates infra cost ~10x | early-adopter | [SDK overview](../research/sources/anthropic-agent-sdk-overview.md) (first-party); [hosting guide](../research/sources/anthropic-agent-sdk-hosting.md) (first-party); [Codex SDK](../research/sources/openai-codex-sdk-docs.md) (first-party); [eleven-system study: harness SDKs are the framework layer now](../research/sources/arxiv-harness-engineering-eleven-systems.md) (independent) |
| Hosted harness (managed) | Vendor runs loop, sandbox, event log; we send events and stream results | Claude Managed Agents (beta, with self-hosted sandbox option) | Least to build; sessions persistent, steerable, cron-schedulable; stable interfaces designed so harness can be swapped as models improve | Beta; Anthropic-only; not ZDR/HIPAA eligible; data held server-side; pricing not verified from a primary source | emerging | [Managed Agents docs](../research/sources/anthropic-managed-agents-overview.md) (first-party); [Scaling Managed Agents](../research/sources/anthropic-engineering-scaling-managed-agents.md) (first-party) |
| Build on a general agent framework | Compose our own agents on a library: loop, tools, state, durable execution, evals | LangGraph/LangChain Deep Agents, Google ADK, Pydantic AI (+Harness), Microsoft Agent Framework (+Harness Agent), OpenAI Agents SDK, Vercel AI SDK, Mastra, CrewAI | Model portability, durable execution, graph workflows, eval and deployment tooling; fits structured task agents and web products; frameworks are moving toward shipping a harness | 0 of 11 production coding harnesses use any of them (coding scope); framework churn (AutoGen archived; LangChain-family positioning changes); abstraction can obscure prompts; you still build sandbox, coding tools, context management, permissions; practitioner (Ronacher) would not repeat SDK use for provider abstraction | mainstream for workflow apps; unproven as coding/knowledge-work harness base | [eleven-system study](../research/sources/arxiv-harness-engineering-eleven-systems.md) (independent); [Ronacher](../research/sources/lucumr-agent-design-is-still-hard.md) (anecdote); [AutoGen archive notice](../research/sources/github-microsoft-autogen-archive-notice.md) (first-party); [MS Agent Framework](../research/sources/microsoft-agent-framework-overview.md) (first-party); [Deep Agents layering](../research/sources/langchain-deep-agents-vs-langchain-vs-langgraph.md) (vendor claim); [ADK](../research/sources/google-adk-docs.md) (first-party) |
| Fork or extend an open-source harness | Start from a working open harness and customise it (unattended mode, deterministic steps, own tools) | Stripe Minions (Goose fork); OpenClaw (embeds Pi); OpenCode; Cline SDK; Goose custom distributions | Working loop, provider-agnostic, permissive licences (MIT/Apache-2.0), customisable without writing a loop | We inherit merge and maintenance burden; project governance/rename risk (OpenCode repo moved orgs; Roo Code archived per a rival's page); Claude subscription credit not usable (API rates); security of an unattended fork is ours | early-adopter | [Stripe Minions](../research/sources/stripe-minions-one-shot-coding-agents.md) (first-party); [Goose](../research/sources/github-block-goose-repo.md) (first-party); [OpenCode](../research/sources/github-opencode-repo.md) (first-party); [Cline](../research/sources/github-cline-repo.md) (first-party); [subscription block](../research/sources/venturebeat-anthropic-third-party-harness-crackdown.md) (independent) |
| Write a minimal own loop | Own thin loop and a few tools (bash, read, write, edit), full control of context | Pi, Mini-SWE-Agent (about 50 lines, 74%+ SWE-bench Verified self-reported), Amp tutorial agent | Total context visibility, tiny prompt, cheap to understand; competitive on coding benchmarks per authors | Own provider abstraction, UI, caching, evals, safety; no marketplace/ecosystem; benchmarks are self-reported; Anthropic's own harness posts show scaffolding keeps being needed for reliability on long tasks | early-adopter (coding); untested for knowledge work | [Zechner/Pi](../research/sources/mariozechner-pi-minimal-coding-agent.md) (anecdote); [Ball/Amp](../research/sources/ampcode-how-to-build-an-agent.md) (first-party); [eleven-system study](../research/sources/arxiv-harness-engineering-eleven-systems.md) (independent); [long-running harness](../research/sources/anthropic-effective-harnesses-long-running-agents.md) (first-party) |

See also: "Stay in vendor harnesses, keep assets portable" (the no-layer alternative) is under [[harness-layering]]. The hosting side of "Embed a harness SDK, self-hosted" and "Hosted harness (managed)" is covered in [[runtime-location]] ("Self-host a vendor-SDK agent in our own containers", "Vendor-hosted agent runtime with self-hostable sandbox").

### Key questions to choose
3. What is the real cost and team size to build and run our own harness (beyond Ramp's account)? — *answered by:* Track 2 research, a scoped build estimate — *affects:* embed SDK, framework
4. Ramp's ownership rationale (moat, same-day fixes, learning for its own product) fits an AI-product company: does any of it apply to our target users' orgs, or are they buyers of a harness? — *answered by:* user/customer interviews — *affects:* embed SDK, build on framework
5. Glass's own accounts disagree on team size (3 vs 4) and give no run/maintenance cost: what would it cost an org without Ramp's engineering depth? — *answered by:* scoped build estimate, ask Ramp-like adopters — *affects:* embed SDK
7. Can the build-vs-buy choice be deferred by keeping the shaping skill, spec standard and context as plain text that any harness can read? Geoff's Intent Factory argues the context layer should be harness-agnostic so teams don't wait for patterns to settle ([source](../research/sources/geoff-building-accelerating-intent-factory.md), Action 5). — *answered by:* running one shaping skill and context repo in two harnesses — *affects:* all; links to [[context-and-memory]]
8. Which of our target jobs (e.g. PRD review, research synthesis) actually need a coding-style harness (shell, files, sandbox) and which are workflow-shaped (fixed steps, structured I/O)? The independent harness evidence covers coding agents only. — *answered by:* job inventory scored against the PM jobs map; one job built as a skill in Claude Code, as an Agent SDK app and as a framework workflow, compared on reliability, cost and effort — *affects:* framework, harness SDK, vendor harness
9. Who would maintain the harness through model releases? Anthropic, Cognition and Vercel each report stale harness components or rebuilds after a model change (e.g. Sonnet 4.5 context anxiety; sprint construct removed with Opus 4.6). What is the recurring effort and who is on call? — *answered by:* ask Ramp, Stripe-like adopters and framework vendors for upkeep effort; a staffing estimate; policy owner for the budget — *affects:* all own-harness options
10. What does using a non-Claude-Code harness cost with Claude models, given Claude subscription credit works only in Claude Code (third-party harnesses pay API rates) and Agent SDK usage on subscriptions was reported to move to a separate credit from 2026-06-15? — *answered by:* cost model against real usage; confirm current terms with Anthropic (account rep or terms review) — *affects:* all non-Claude-Code options
11. Does the finding that no production harness uses a general framework hold for non-coding, multi-user, long-running agents (where durable execution, HITL and evals matter more)? — *answered by:* more research on knowledge-work and enterprise agents built on LangGraph/ADK/MS Agent Framework with independent post-mortems; a prototype — *affects:* framework option
12. How much of the vendor-claimed harness benefit transfers to our setting (e.g. +13.7 points from harness changes alone on Terminal Bench; 20x cost for a full planner/evaluator harness)? — *answered by:* a small eval of our own jobs with and without added scaffolding — *affects:* build and fork options
- See also: key questions 1 (does harness independence matter to users) and 6 (are portable assets enough) are under [[harness-layering]].

#### Audit additions (competitive-teardown-ramp-glass, 2026-10-24)
Correction to the Glass rows above: "Ramp Glass on the Claude Agent SDK" is the April 2026 state (Charles). Ramp's Oct 20 post says every agentic product, Glass included, now runs on Laminar, its own harness ([first-party](../research/sources/ramp-builders-building-laminar.md); [independent coverage](../research/sources/thenewstack-ramp-laminar-agent-harness.md)).

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Own harness replacing vendor SDKs after trial | Try provider agent SDKs, managed-agent APIs, open-source agents and frameworks, then build a provider-agnostic harness in-house once the needs are known | Ramp Laminar (decided ~May 2026, v1 in six weeks, all products on it by Oct 2026) | Provider independence, same-day fixes next to product teams, own observability; Ramp says build cost was "marginal" with coding agents | Ramp's own caveat: engineers still needed on-call and to keep the platform healthy; no cost comparison published; Ramp has deep engineering capacity | early-adopter | [Building Laminar](../research/sources/ramp-builders-building-laminar.md) (first-party); [The New Stack](../research/sources/thenewstack-ramp-laminar-agent-harness.md) (independent, relies on the post) |

Key questions (unranked):
- Ramp outgrew the vendor SDK within about six months of shipping Glass on it. What signals would tell us we had reached that point (provider lock-in, missing observability, vendor response time), and can the first build be designed so that switching the loop is a migration rather than a rewrite? — *answered by:* list the SDK dependencies in a prototype; ask Ramp/Stripe-style adopters what triggered the switch — *affects:* embed SDK, own harness
- Kronick's claim that coding agents make an own harness "marginal" to build is unquantified. What did Ramp's six weeks cost in senior-engineer time, and what is the ongoing on-call load? — *answered by:* ask Ramp; our own time-boxed build spike — *affects:* own harness, framework

### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | intent-factory pass: research-product-agent-and-harness on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | audit pass: competitive-teardown-ramp-glass on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- The resource request may fund whatever mix of build and buy gives the highest leverage and the best experience and outcomes. Building, buying and layering all stay open. Harness and model independence are benefits, not goals, and their value has not been quantified. Geoff would not trade harness quality for harness independence. New key question: how much is independence worth to us, against harness quality? *answered by:* a cost/benefit estimate during the bake-off.

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
Evidence note: the "one engineer, one week" build is LangChain's headline; Stripe's own podcast says "one and a half people over two weeks" for v0, then 2.5-3 people in pilot and a core team under 10 at 10,000+ weekly users.

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Two loop sources by work family: framework harness for knowledge work, forked OSS harness for code | Kai is built on LangChain Deep Agents (Python) with a Stripe harness layer and a configuration layer above it; Minions run on a Goose fork | Stripe Kai + Minions | Each family gets a loop shaped to it (long multi-turn sessions and artifacts vs one-shot unattended runs); framework middleware (VFS, sandbox, summarization) avoided months of build | Two harnesses to staff and upgrade; Stripe had to add Python service scaffolding beside Ruby/Java; framework coupling | early-adopter | [LangChain case study](../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor claim); [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [How I AI, Kaliski](../research/sources/howiai-stripe-minions-kaliski.md) (first-party) |

Key questions (Stripe pass):
13. Kai is a production, non-coding, multi-user agent on a general framework (Deep Agents), a partial counterexample to "no production harness uses a general framework" (key question 11). How much of its fast build came from the framework, and how much from Stripe's pre-existing Toolshed MCP, data catalog and security stack? — *answered by:* interview Stripe's Agent Foundation team or a framework-vendor reference customer without Stripe's infra; a one-week spike of one PM job on Deep Agents vs Claude Agent SDK — *affects:* build on a framework, embed SDK
14. Should knowledge work and code delivery share one loop or use two (Stripe uses two; Ramp moved everything onto Laminar)? — *answered by:* compare upkeep cost and capability gaps in a two-job prototype; ask Ramp and Stripe about the trade — *affects:* all loop-source options



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Own disposable loop on an own substrate, outside the sandbox | Org writes its own harness ("reads history, calls the model, emits tool intents") as a cheap, disposable process separate from the sandbox; earlier Shopify workflows embedded Claude Code (Roast) | Shopify Aquifer (River, PR review, headless "pi" profile) | Swap models, runtimes, even languages on the harness side; loop outside the `rm -rf` blast radius; one observable decision stream | Requires a platform team and the 2024 monorepo/Nix substrate; models used not disclosed; no cost data | early-adopter (one large adopter) | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [Roast](../research/sources/shopify-engineering-introducing-roast.md) (first-party) |

Key questions (River pass):
- Did Shopify's move from embedding Claude Code (Roast, 2025) to an own loop (Aquifer, 2026) follow a specific limit (multiplayer, durability, observability), and would we hit the same limit? — *answered by:* ask Shopify builders; compare with Ramp's SDK-to-own-infra path — *affects:* embed SDK vs own harness

---

## harness-layering: Is there a layer above the vendor harnesses
**Choice:** None (users run vendor CLIs directly); a local parallel-session manager; a self-run meta-harness server; a hosted multi-harness control plane; an SDK-level adapter inside our product; or a platform-native workspace that replaces the CLI.
**Why it matters to the strategy:** The case for a layer is organisational (uniform governance, sharing and persistence across harnesses), so the buyer may be a platform or security owner while the PM is the user; "who supplies the loop" and "is there a layer above" have different buyers.
**Related themes:** [[harness-over-model]], [[harness-portability]], [[build-vs-buy]]   **Related dimensions:** [[loop-source]], [[governance-control-plane]], [[session-persistence-sharing]], [[model-provider-coupling]]
Formerly: harness-ownership (the meta-harness and layer rows and questions, per 01-synthesis.md D.0). The original harness-ownership framing is kept under [[loop-source]].

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Meta-harness above existing harnesses | A layer that runs and governs several harnesses | Databricks Omnigent, Cloudflare OS (Track 1) | Harness independence, policy, sharing | New dependency, alpha-stage | emerging | to be researched |
| Stay in vendor harnesses, keep assets portable | Users choose harnesses freely; the organisation invests in harness-neutral assets (SKILL.md skills, AGENTS.md, MCP servers, a Git-backed registry) | Skills read by Claude Code, Codex, Copilot, Gemini CLI, Cursor, OpenCode; Vercel `npx skills`; PayPal registry targeting Claude Desktop and Codex | Reduces lock-in without building a harness; assets survive a harness switch | Portability is of the file format, not behaviour: SkillsBench found Codex often ignored provided skills while Claude Code and Gemini CLI gained; subagents, hooks, plugins are not portable; each harness has its own admin controls | early-adopter | [SkillsBench](../research/sources/arxiv-skillsbench.md) (independent); [spec](../research/sources/agentskills-specification.md), [Copilot](../research/sources/github-copilot-agent-skills-docs.md) (first-party); [Vaughan](../research/sources/danielvaughan-agent-skills-open-standard-portable.md) (anecdote) |
| Meta-harness server above many harnesses (self-run) | A server plus runners launch Claude Code, Codex, Cursor, OpenCode, Pi etc. through a uniform session API, with policies and shared history | Databricks Omnigent (Apache-2.0, alpha); Nx Polygraph (closed) | Harness independence; same policy and sharing over any wrapped agent; import of local Claude/Codex transcripts | Alpha: open issues on stuck sessions, auth, sharing/host-access separation; a new dependency that depends on each vendor CLI's login and terminal behaviour; bypassed if someone runs the harness directly | emerging | [Omnigent repo](../research/sources/github-omnigent-repo.md) (vendor claim + open issues); [launch](../research/sources/databricks-omnigent-meta-harness-launch.md) (vendor claim); [Atlan](../research/sources/atlan-omnigent-explainer.md) (vendor-biased) |
| Hosted multi-harness control plane | Vendor-hosted (or self-hosted workers) cloud agents choose Claude Code, Codex or the vendor's agent per task with shared triggers, skills, rules, audit | Warp Oz (beta, May 2026) | No server to run; triggers from Slack/Linear/CI; per-team credit caps | Third-party harness inference billed outside the platform; only the vendor's own agent can be parent; no independent evidence | emerging | [Warp Oz](../research/sources/warp-oz-multi-harness.md) (vendor claim) |
| Vendor-hosted meta-harness on the model vendor's cloud | Managed service that hosts the session log, a stateless harness and sandboxes behind stable interfaces; harnesses (incl. Claude Code) are swappable behind it | Anthropic Managed Agents (public beta April 2026) | Durable sessions, credential vault, no ops | Runs only on the vendor's infrastructure; vendor's own harnesses first | emerging | [Anthropic engineering](../research/sources/anthropic-scaling-managed-agents.md) (first-party) |
| Framework-level harness adapter | Application code drives different coding-agent harnesses through one SDK class, in sandboxes | Vercel AI SDK 7 HarnessAgent (experimental) | Swap Claude Code/Codex/Pi like models inside our own product; no extra server | Experimental, breaking changes; execution environment and security vary by adapter | emerging | [Vercel docs](../research/sources/vercel-ai-sdk-harnesses.md) (vendor claim) |
| DIY coordinator calling harness CLIs | A light harness spawns `claude -p` and `codex exec` as sub-agents via profile files | Pi + pi-flow | Cheap, transparent, route by model strength | Cost fan-out (~23-25 sessions per delegation), debugging opacity, approvals bypassed in shared CI, weak context transfer | emerging | [Vaughan](../research/sources/danielvaughan-meta-harness-pattern-pi.md) (independent practitioner) |
| Local parallel-session manager | Desktop/terminal app runs several agent CLIs in isolated worktrees with notifications and review; no governance or sharing | Conductor (closed, Mac), Claude Squad (AGPL), Superset (source-available), Vibe Kanban (company shut down 2026-04-10, community maintained) | Many agents at once for one developer; picks up each harness's own skills/MCP | Single user, own machine; supplier risk; context switching limits benefit | early-adopter | [Franke](../research/sources/garrit-meta-harness-parallel-agents.md) (anecdote); [Claude Squad](../research/sources/github-claude-squad.md) (vendor claim); [Vibe Kanban shutdown](../research/sources/vibekanban-shutdown.md) (first-party) |
| Platform-native own harness on an infrastructure vendor | Build the harness and apps directly on an agent cloud's primitives; third-party CLIs are not the agent | Cloudflare OS (Code Mode agent on Pi), Project Think, Flue | Durable, multi-user, cheap idle; strong sandbox/capability model | Not harness-portable; tied to Cloudflare PaaS today (self-host on workerd 'coming soon'); early access | emerging | [Cloudflare OS repo](../research/sources/github-cloudflare-os-repo.md) (vendor claim); [HN](../research/sources/hn-cloudflare-os-thread.md) (anecdote); [Flue post](../research/sources/cloudflare-flue-agents-platform.md) (vendor claim) |

### Key questions to choose
1. How much does harness independence matter to our target users (do they care, or only to us)? — *answered by:* user interviews — *affects:* all
2. What do vendor harnesses lack that a layer would add (sharing, policy, persistence), and is the vendor roadmap closing that gap? — *answered by:* Track 1 and 3 research, vendor roadmap review — *affects:* meta-harness, own harness
6. Is "portable assets in several vendor harnesses" enough harness independence for our users, or does behaviour (triggering, tool semantics, permissions) differ enough that a layer above is needed? - *answered by:* two-harness prototype of one skill-based workflow; Track 1 comparison - *affects:* vendor-harness-with-portable-assets vs meta-harness
13. Which meaning of 'meta-harness' do we need: a governance/sharing layer over many vendor CLIs (Omnigent, Warp Oz), a local parallel-session manager (Conductor, Claude Squad), or a framework-level adapter (Vercel HarnessAgent)? They solve different problems. — *answered by:* mapping our three aims to each meaning; user interviews — *affects:* all meta-harness options
14. Does a layer that wraps vendor CLIs stay viable as the vendors change login, terminal and hook behaviour? Omnigent's open issues show auth and terminal failures; what is the maintenance burden and who absorbs it? — *answered by:* a two-week trial of Omnigent with Claude Code and Codex; read upstream issue history — *affects:* meta-harness server, hosted control plane
15. Is the first-party vendor path (Managed Agents, Claude Code on the web, Codex cloud) closing the gap a third-party layer would fill, and is Anthropic's own use of the word 'meta-harness' a signal it will cover this? — *answered by:* Track 3 roadmap review; vendor briefings — *affects:* all meta-harness options
16. Do our users' policies need to hold when someone runs the vendor CLI directly rather than through the layer? — *answered by:* security/policy owner — *affects:* meta-harness server, DIY coordinator
17. Is the independent evidence for any meta-harness thin by nature (new, alpha) or have we not found it? Omnigent's HN launch drew 15 points; Cloudflare OS 668. Is there anyone running Omnigent beyond Databricks? — *answered by:* more research (Reddit, X, Discord, GitHub discussions), ask Databricks — *affects:* meta-harness server

### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | intent-factory pass: research-product-agent-and-harness on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- Terms must follow real, common usage. Use 'meta-harness' only in its established sense (a layer above several harnesses), and record the competing usages found (Anthropic Managed Agents; the Stanford optimiser sense). Where a pattern lacks a consensus term (e.g. Cloudflare OS, an org-deployed agent workspace with its own agent), name it explicitly as our coined term and don't stretch 'meta-harness' to cover it.

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Company agent platform with a configuration layer that can front other harnesses | Layers: framework base, company harness (security, infra, services), configuration layer (custom agents with own skills, behaviour, persona), UI. A project can be "backed by a different API in the back end and a different harness" while keeping the platform's features | Stripe Kai (projects, custom Kai agents) | Teams customise without touching the harness; heterogeneous agents behind one front door and one governance model | Platform team owns the layer; the alternate-harness path was described, not shown | early-adopter | [LangChain case study](../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor claim); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |

Key questions (Stripe pass):
8. Is a configuration layer (custom agents and projects) enough "layer above" for teams, or do they need to bring their own harness behind the same UI as Stripe allows? — *answered by:* ask Stripe how many projects use a non-Kai backend; user interviews with teams that already own agents — *affects:* meta-harness options



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| One substrate under many agent profiles (layer below, not above) | Instead of a meta-harness over vendor CLIs, one platform (session, harness, sandbox, gateway, credentials proxy, observability) hosts many agents as config bundles | Shopify Aquifer: River, PR review, "pi" profiles; "future agents are peers, not children" | Next agent costs a bundle, not a platform; same session model across interactive, automation and job modes | Every agent shares one platform's limits and team; no portability to vendor harnesses stated | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party) |

Key questions (River pass):
- Is our layer of leverage above harnesses (meta-harness) or below agents (a substrate that hosts profiles)? Shopify's answer is below. — *answered by:* Geoff / director scoping; prototype of two profiles on one session store — *affects:* meta-harness vs substrate options

---

## runtime-location: Where the agent runtime lives
**Choice:** Where does the agent actually run: the user's machine, a user-owned remote box, a vendor cloud, an org-deployed service, or the edge?
**Why it matters to the strategy:** It determines privacy, persistence, shareability, and what data and tools an agent can reach.
**Related themes:** [[memory-architecture]]   **Related dimensions:** [[session-persistence-sharing]], [[governance-control-plane]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Local process | Runs on the user's laptop | Claude Code CLI | Fast, private, full local access | Dies with the laptop; hard to share | mainstream | to be linked |
| Sandboxed / remote per session | Isolated cloud sandbox per task | Ramp Inspect, cloud/background agents | Parallel, persistent, shareable | Cost, environment setup, data access | early-adopter | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party) |
| Org-deployed service | Long-running agent deployed by the org | Cloudflare OS, Glass | Always on, multi-user, governed | Ops burden, identity and data design | emerging | to be researched |
| Desktop app + laptop as server | Installed app; scheduled automations run while laptop is on; headless mode with phone approval of permissions | Ramp Glass | No server ops; uses the user's local context | Depends on the laptop being on; fleet management; not yet shown how shared/org-run jobs work | early-adopter | [Goddijn article](../research/sources/x-sebgoddijn-glass-article.md) (first-party) |
| Vendor-managed cloud VM per session | Session runs on the vendor's infrastructure with a configured environment and network allowlist | Claude Code on the web, Codex cloud, Cursor cloud agents, Devin, Warp Oz hosted | No ops; survives laptop close | Source must be on GitHub for full function; IP-allowlisted orgs fail; ZDR/HIPAA/CMEK orgs excluded for Claude; capacity provisioned on demand | early-adopter | [Claude cloud docs](../research/sources/anthropic-claude-code-cloud-sessions.md) (first-party) |
| Customer-hosted runners, vendor control plane | Org runs workers that claim sessions; queue, UI and transcripts stay with the vendor | Claude self-hosted environments (beta), Warp Oz self-hosted workers | Code and builds stay in the org network; internal services reachable | Org runs a fleet; owner-locked runners; conversation still goes to the vendor; lost turns on host kill | emerging | [Claude self-hosted](../research/sources/anthropic-self-hosted-environments.md) (first-party); [Warp Oz](../research/sources/warp-oz-cloud-agents.md) (first-party) |
| Agent as a durable object at the edge | Each agent is a stateful object with SQLite, alarms and WebSocket hub that hibernates and wakes | Cloudflare Agents SDK, Open-Inspect control plane | Cheap idle, always addressable, per-agent isolation | Recovery logic and idempotency are the developer's; hours-long work needs Workflows | emerging | [Cloudflare docs](../research/sources/cloudflare-agents-long-running-agents.md) (first-party); [Open-Inspect](../research/sources/github-open-inspect-background-agents.md) (first-party) |
| Pooled pre-warmed devboxes | Org's own dev environment fleet reused for agents | Stripe Minions | Reuses human tooling; ~10 s start | Needs mature dev infra | early-adopter | [Stripe Minions](../research/sources/stripe-minions-part-2.md) (first-party) |
| Self-host a vendor-SDK agent in our own containers | Run Agent SDK instances in Docker/Kubernetes/Modal/other sandboxes with our own gateway, egress proxy and storage | Claude Agent SDK hosting cookbook (Docker, Modal, Kubernetes); Codex SDK | Full control of data location and network; can use own cloud | One subprocess per session; 1 GiB RAM floor each; memory growth over long sessions; no built-in session timeout; multi-tenant leakage via CLAUDE.md/settings unless configured | early-adopter | [hosting guide](../research/sources/anthropic-agent-sdk-hosting.md) (first-party) |
| Org-deployed agent workspace with capability security | Per-employee browser workspace, apps as isolates with their own SQLite, access only through typed bindings and per-service Gatekeepers; open source, deploy in own Cloudflare account | Cloudflare OS (early access, Apache-2.0); internal v1 since May 2026 | Always on, multi-user, non-engineer friendly, permission re-check on sharing; deploy in minutes | Early access, 'rough edges', tied to Cloudflare PaaS and Workers Paid plan; not wrapping Claude Code/Codex; self-reported adoption only | emerging | [announcement](../research/sources/cloudflare-os-announcement.md) (vendor claim); [repo](../research/sources/github-cloudflare-os-repo.md) (vendor claim); [HN reports](../research/sources/hn-cloudflare-os-thread.md) (anecdote) |
| Third-party sandbox per session | Rent isolated microVM/container sandboxes by API and run any harness inside | E2B, Modal, Daytona, Vercel Sandbox, Cloudflare Sandbox SDK, Blaxel (Omnigent and HarnessAgent can target them) | Isolation without our own fleet; snapshots; pick vendor per workload | Persistence differs (files vs memory vs processes); egress often open by default; injected credentials readable by guest code; ownership churn (Blaxel acquired, Daytona open core reportedly private); no independent benchmark | early-adopter | [sandbox survey](../research/sources/rywalker-ai-agent-sandboxes.md) (independent, disclosed conflict); [Cloudflare docs](../research/sources/cloudflare-sandbox-sdk-docs.md) (vendor claim) |
| Vendor-hosted agent runtime with self-hostable sandbox | Vendor runs the loop and session log; tools run in a vendor sandbox or on your infrastructure | Anthropic Managed Agents (self-hosted sandbox option; also on AWS and Google Cloud), Claude Code self-hosted environments, AWS AgentCore Runtime | No loop to build; durable sessions; data-residency route via self-hosted sandbox | Beta; stateful so no ZDR/HIPAA BAA for Managed Agents; lock-in and trace portability concerns (CData, interested party) | emerging | [Managed Agents](../research/sources/anthropic-managed-agents-overview.md) (vendor) (vendor claim); [CData](../research/sources/cdata-claude-managed-agents-meta-harness.md) (independent) (independent-ish, interested party) |

See also: two [[loop-source]] options are also hosting choices: "Embed a harness SDK, self-hosted (Agent SDK, Codex SDK)" and "Hosted harness (managed)". They stay there as loop choices; their hosting is covered by the self-hosted SDK and vendor-hosted runtime rows above (01-synthesis.md D.0 moves "where the loop is hosted" here).

### Key questions to choose
1. Which tasks need local access (files, repos, private data) and which don't? — *answered by:* task inventory with users — *affects:* all
2. What are the data-residency and security constraints for our users' orgs? — *answered by:* policy owners / security review — *affects:* cloud and deployed options
3. Is a laptop-as-server model good enough for scheduled/unattended work, or do real org workloads need a deployed runtime? — *answered by:* inventory of unattended jobs; prototype — *affects:* local vs org-deployed
4. Which of our users' repos and data live on GitHub and which would have to be uploaded or bundled (Claude bundles up to 100 MB, excluding credential-like files)? — *answered by:* repo/data inventory; policy owner — *affects:* vendor cloud
5. Would we run any runner fleet ourselves, and who would operate it? — *answered by:* platform/IT owner; cost estimate — *affects:* customer-hosted, edge, devboxes
6. How fast must a session start to be adopted (Ramp frames startup speed as the adoption driver; snapshots refreshed every 30 minutes)? — *answered by:* prototype with user timing tests — *affects:* sandbox and cloud options
7. If we self-host, what are the real per-session RAM, cold-start and idle costs at our expected concurrency, and which sandbox provider meets the data-residency constraint? — *answered by:* prototype load test on the hosting cookbook; security review — *affects:* self-hosted SDK agent, org-deployed service
8. Do we want to run Claude Code/Codex inside rented sandboxes (Omnigent, HarnessAgent, Cloudflare Sandbox guide) or replace the CLI with a platform-native agent (Cloudflare OS Code Mode)? What do users lose in each? — *answered by:* side-by-side prototype of one workflow — *affects:* third-party sandbox, org-deployed workspace
9. What must survive between sessions in our workloads (files, memory, running processes), and which sandbox classes provide it? — *answered by:* task inventory; provider trial against the survey's persistence matrix — *affects:* third-party sandbox
10. Could we deploy Cloudflare OS in a pilot account, and what would our users and security owner say about its capability model and Workers Paid dependency? — *answered by:* 1-day deploy trial, security review — *affects:* org-deployed workspace
- (Track 3) 3. Do target orgs need the agent runtime inside their own network (self-hosted sandbox/environment), and which vendor options support that today? — *answered by:* security review; vendor trial of Managed Agents self-hosted sandboxes and Claude Code self-hosted environments (page not read here) — *affects:* vendor-hosted vs org-deployed
- (user-story-mapping) Which stories genuinely need to run when the performer's laptop is off (S02, S07, S09, S10, S14), and which are fine on demand? Scoring them settles whether unattended work is a core need or an extra. — *answered by:* story inventory with PMs ([stories](../tasks/user-story-mapping/INDEX.md)) — *affects:* local, laptop-as-server, cloud, org-deployed

#### Audit additions (competitive-teardown-ramp-glass, 2026-10-24)
Correction: the seed row lists Glass as an "Org-deployed service" and my April-based row as "Desktop app + laptop as server". Both are partly right at different dates. April 2026: desktop app, laptop-side MCP proxy and scheduling (Goddijn, Buchan). October 2026: Laminar runs all sessions on "a fleet of generic disposable workers" in the cloud with "Web + desktop" clients; Kronick calls local-first agents "a weird blip" and says it no longer matters "if their laptop goes to sleep" ([first-party](../research/sources/ramp-builders-building-laminar.md)). Treat the laptop-as-server row as superseded for Glass; whether the desktop client still executes anything locally is not stated.

Key questions (unranked):
- Is Kronick right that local-first agent runtimes were a transitional blip, or do some of our target users' jobs still need local files, repos or devices? — *answered by:* task inventory with users; check which of our stories touch local state — *affects:* local, laptop-as-server, cloud worker fleet
- If sessions live in the cloud, what happens to the "memory as local inspectable files" and "self-healing local integrations" properties Ramp praised in April? — *answered by:* ask Ramp; prototype memory files in a cloud session store — *affects:* cloud options, [[context-and-memory]]

### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 5 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | user-story-mapping pass on 2026-10-24 | audit pass: competitive-teardown-ramp-glass on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Cloud agent service with the sandbox as a tool | Agent runs as a hosted service (Kubernetes) outside the sandbox and calls a per-session secure sandbox for code/analytics; a multi-tenant virtual filesystem (S3-backed) holds artifacts; files synced in and out on each sandbox call | Stripe Kai | Always on, behind standard security boundaries; generated code kept behind a clean boundary; same substrate as Stripe's customer-facing agents | Must build VFS sync, sandbox service, multi-tenancy; no local tools or laptop files | early-adopter | [LangChain case study](../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor claim); [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Dedicated agent service distinct from ML inference | A shared service hosting many agents (stateless sync at first, now stateful multi-turn), with async execution and per-invocation cost tracking | Stripe agent service (100+ agents in under a year) | Fits network-bound, long, stateful agents; one place for cost and audit | Another platform to run; relation to Kai's runtime not stated | early-adopter | [AWS/Stripe compliance post](../research/sources/aws-stripe-compliance-agents.md) (first-party, vendor-hosted) |

Key questions (Stripe pass):
7. Sandbox-as-tool (Kai) vs agent-inside-sandbox (Minions, Claude cloud) vs laptop-as-server (Glass): which does our security owner accept for non-engineers handling customer data? — *answered by:* security/policy owner review of the three patterns — *affects:* sandboxed per session, org-deployed service, desktop app



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Org-hosted ephemeral session cells over a durable log | Each live session materialises a short-lived process (Go runtime + harness) on any host; it exits when idle and rehydrates from Postgres on the next message | Shopify Aquifer / River; Remote Dev adds a warm pool of remote Macs and Linux VMs claimed per session | No laptop dependency; cheap idle; parallel sessions; mobile builds without local Macs | Org runs the fleet; orchestrator not named; Remote Dev setup took iterations (warm pool, staggered refresh) | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [Remote Dev](../research/sources/shopify-engineering-remote-dev.md) (first-party) |

Key questions (River pass):
- Which of our first jobs need specialised execution environments (simulators, GPUs, data access) that a laptop or vendor cloud can't give, as River needed remote Macs? — *answered by:* jobs map with environment needs — *affects:* org-hosted vs vendor cloud vs laptop

---

## capability-format-portability: Capability format and portability
**Choice:** Is reusable know-how an always-on context file, an open-standard skill, a harness-extended skill, a packaged subagent, a plugin bundle, an MCP server, or a deployed agent; and how much of it moves between harnesses?
**Why it matters to the strategy:** It decides how complex a standardised capability (e.g. a PRD-review agent) can be and whether it works in more than one harness. Its decision owners are the capability authors; distribution and trust (security and platform owners) is [[capability-distribution-trust]].
**Related themes:** [[skills-marketplace]], [[one-job-per-agent]], [[harness-portability]]   **Related dimensions:** [[capability-distribution-trust]], [[remote-invocation-route]], [[loop-source]], [[work-structure]]
Formerly: capability-packaging (the format and portability rows and questions; registry and trust rows moved to [[capability-distribution-trust]], per 01-synthesis.md D.0 and the Track 4 proposal)

### Original framing before the split — capability-packaging: How skills and agents are packaged and invoked
**Choice:** Is reusable know-how a prompt, a skill, a plugin, a subagent, an MCP server, or a deployed agent called over a protocol, and how is it distributed and versioned?
**Why it matters to the strategy:** It decides how complex a standardised capability (e.g. a PRD-review agent) can be and whether it works in more than one harness.
**Related themes:** [[skills-marketplace]], [[org-learning-loop]], [[one-job-per-agent]]   **Related dimensions:** [[loop-source]], [[harness-layering]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Skill / plugin in the harness | Markdown/skill bundles loaded by the harness | Agent Skills, Cowork plugins, Ramp Dojo | Cheap, portable if standard | Limited complexity; runs in the host harness | early-adopter | [Glass teardown](../research/sources/x-shanebuchan-how-we-built-glass.md) (first-party) |
| Deployed agent called from a harness | Task-specific agent with its own runtime, called via MCP/A2A | Track 3 | Arbitrary complexity, own runtime, central governance | Latency, auth, two systems to debug | to be researched | to be researched |
| Open-standard skill (portable core only) | SKILL.md folder using only the six agentskills.io fields; scripts/references/assets optional | agentskills.io spec; read by Claude Code, Codex, Gemini CLI, Copilot, Cursor, OpenCode, ChatGPT | One authoring format across harnesses; ~100-token metadata per skill; version-controllable | No spec for triggering, sandboxing, script languages, versioning or dependencies; `allowed-tools` experimental; activation reliability varies by harness | early-adopter (broad adoption, thin guarantees) | [spec](../research/sources/agentskills-specification.md) (first-party); [Copilot](../research/sources/github-copilot-agent-skills-docs.md), [Codex](../research/sources/openai-codex-skills-docs.md) (first-party); [Vaughan](../research/sources/danielvaughan-agent-skills-open-standard-portable.md) (anecdote) |
| Harness-extended skill | Skill using Claude Code extensions (`context: fork`, `hooks`, `paths`, `disable-model-invocation`, `model`) or Codex `agents/openai.yaml` | Claude Code skills; Codex skills | Skill can delegate to a subagent, carry hooks and model/tool limits, i.e. a multi-step workflow without new infrastructure | Quietly harness-specific: claude.ai uploads and the Skills API hard-fail on non-spec keys; other tools silently ignore the extras so behaviour diverges | early-adopter | [Claude Code skills docs](../research/sources/anthropic-claude-code-skills-docs.md) (first-party); [OpenCode/Gemini](../research/sources/gemini-cli-and-opencode-skills-support.md) (first-party via search summaries) |
| Plugin bundle | Package of skills + subagents + commands + hooks + MCP/LSP servers + executables + settings, installed from a marketplace | Claude Code plugins, Cowork plugins, Cursor plugins, Codex plugins | Closest thing to a packaged "agent product" without a runtime of your own; dependencies, userConfig, namespacing, validate command | Each vendor has its own manifest (`.claude-plugin/`, `.cursor-plugin/`); hooks/monitors/bin are Claude-only and rejected by claude.ai/Cowork if `bin/` present; plugin code runs outside the sandbox | early-adopter | [Plugin reference](../research/sources/anthropic-claude-code-plugins-reference.md), [Cursor](../research/sources/cursor-plugins-building.md) (first-party); [Cowork PM plugins](../research/sources/anthropic-cowork-plugins-product-management.md) (vendor claim) |
| Packaged subagent definition | Markdown (Claude Code, Copilot `.agent.md`) or TOML (Codex) file defining role, tools, model, memory | `.claude/agents/`, `.codex/agents/`, `.github/agents/` | Reusable specialist role with tool and model limits; can preload up to 32 skills | No shared spec; formats and delegation semantics differ (implicit vs explicit spawning); plugin-shipped agents lose hooks/mcpServers/permissionMode | emerging | [Claude subagents](../research/sources/anthropic-claude-code-subagents-docs.md) (first-party); [Vaughan](../research/sources/danielvaughan-codex-vs-claude-code-multi-agent.md) (anecdote) |
| Always-on context file | AGENTS.md / CLAUDE.md instructions in the repo | AGENTS.md (60k+ repos claimed), CLAUDE.md | Most portable; no trigger decision; beat on-demand skills for reference docs in one Vercel eval | ETH study: reduced task success and +20% cost; consumes context every turn; not a place for workflows | mainstream | [agents.md](../research/sources/agentsmd-agents-md.md) (vendor claim); [Vercel](../research/sources/vercel-agents-md-outperforms-skills.md) (vendor claim); [ETH](../research/sources/arxiv-evaluating-agents-md.md) (independent) |
| Deployed agent behind MCP, A2A or a vendor API (Track 3 detail) | The 'Deployed agent called from a harness' option above, broken out by call route: sync MCP tool, MCP with Tasks, A2A, vendor cloud API, CI-triggered | Glean agents as MCP tools, Sentry Seer, AgentCore A2A, Copilot Studio A2A, Claude Code GitHub Actions | Complexity beyond a skill; own runtime, data and model; usable from several hosts | See [[remote-invocation-route]]: host timeouts, read-only/no-HITL limits (Glean), unproven A2A production use, auth on behalf of the user | emerging | [Glean](../research/sources/glean-agents-as-mcp-tools.md) (vendor) (vendor claim); [Glukhov on A2A](../research/sources/glukhov-a2a-adoption-hype-reality.md) (independent) (independent) |
| Task-specific multi-agent pipeline as a CI component | A structured job (code review) packaged as a coordinator plus specialist sub-agents on an open harness, run in CI, customised per repo through AGENTS.md and a shared template, with risk-tiered depth | Cloudflare AI code review on OpenCode (131k runs, $1.19 average) | Consistent, governed, cheap per run; runs outside any laptop | Stated weaknesses: architectural context, cross-system impact; needs platform team and telemetry | early-adopter | [Cloudflare post](../research/sources/cloudflare-ai-code-review-opencode.md) (first-party) |

#### Added evidence (research-pm-agents-jobs-to-be-done, 2026-10-24)
- PM-job packaging seen in the wild: Claude Cowork Product Management plugin (write-spec, roadmap, progress tracking) as a plugin of skills ([vendor claim, no outcomes](../research/sources/anthropic-cowork-plugins-product-management.md)); Ramp Glass skills for feedback capture and customer notification on ship ([first-party](../research/sources/x-eglyman-introducing-glass-learn-things-once.md)); PM-built agents inside the product platform (Rovo agent for weekly updates, [first-party talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md)).
- Packaging risk evidence for skills ecosystems: see other workers' notes on skill security and portability in research/sources (e.g. [independent](../research/sources/snyk-toxicskills-study.md)).

### Key questions to choose
1. What is the most complex standardised workflow we need (e.g. PRD review) and can a skill carry it? — *answered by:* a prototype of one workflow both ways — *affects:* all
2. How do deployed agents authenticate on behalf of a user across harnesses? — *answered by:* Track 3 research — *affects:* deployed agent
5. Which parts of a target workflow (PRD review as example) stay inside the portable six-field core, and which need `context: fork`, hooks or scripts? Is the harness-specific part small enough to maintain per harness? - *answered by:* prototype one workflow as a portable skill, test in two harnesses (e.g. Claude Code and Codex), following SkillsBench's design - *affects:* open-standard vs harness-extended vs plugin
6. How reliably do skills trigger in the harnesses our users use, with realistic prompts? (Vercel: skill never invoked in 56% of cases; SkillsBench: Codex often ignored provided skills; Claude's own eval tool flags "Claude isn't choosing your skill" as the common first finding) - *answered by:* trigger eval per harness (`claude plugin eval`-style cases with the no-skill baseline) - *affects:* all skill options, and the case for a deployed agent
7. When does a skill stop being enough? Which of: deterministic multi-step control, long-running or background execution, per-user credentials, shared state, audit - need a runtime? - *answered by:* prototype plus Track 3/5 research - *affects:* skills vs deployed agent
9. How much does it matter to users that a skill moves between harnesses at all, versus working well in the one they use? - *answered by:* user interviews, usage data - *affects:* open-standard vs harness-extended
10. Which PM jobs are low-variance enough that a skill suffices, and which need a deployed agent with its own evals? — *answered by:* scoring the jobs in the PM jobs map with PMs and prototyping one both ways — *affects:* skill vs deployed agent (added by research-pm-agents-jobs-to-be-done)
11. Is a PRD-review-style job closer to Cloudflare's CI code reviewer (event-triggered, risk-tiered, one comment) than to a chat skill, and what would its trigger be? — *answered by:* workflow prototype both ways — *affects:* deployed task agent vs skill
- (Track 3) 10. When a skill is not enough, is the first step up a plugin that delegates to a CI-hosted reviewer (GitHub Actions), a sync MCP agent, or a full deployed service? What does each add in latency, auth and ops over the skill? — *answered by:* the same PRD-review prototype built three ways — *affects:* skills vs the deployed-agent options (see [[remote-invocation-route]])
- (Track 3) 11. Does a deployed agent need to be callable from harnesses we do not control (Codex, Cursor, Claude Desktop), or only from our own? Only the former needs MCP/A2A; the latter can use a vendor API. — *answered by:* user interviews on which hosts they use — *affects:* MCP vs vendor API
- See also: key questions 3, 4 and 8 (Dojo reuse, review model, skill lifecycle) are under [[capability-distribution-trust]].

### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 (proposal: consider splitting this dimension into "capability-format-portability" and "capability-distribution-trust"; see track-4 report) | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Skills that gate tools, tiered by role | Agent Skills with allowedTools: the model picks skills, which then load only their tools (two-pass); foundational skills pinned; tiers by user profile, function and custom-agent config; skills follow the open spec | Stripe Kai (500+ MCP tools, 1,000-2,000 skills) | Keeps tool context small; one skill format portable to other harnesses | Selection degrades past ~150 skills with the system prompt; needs retrieval/classifier prefilter at scale | early-adopter | [LangChain case study](../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor claim); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Progressively disclosed skill (top skill plus sub-skills) | Modular skill whose sub-skills load on demand, owned by product teams | Stripe's public Stripe skill | ~10% better than a monolithic skill on Stripe's eval suite; fewer tokens | Needs an eval suite to tune | early-adopter | [steering experiments](../research/sources/stripe-ai-steering-experiments.md) (first-party) |

Key questions (Stripe pass):
10. At what catalog size does LLM-only skill selection break for our users (Stripe reports ~150), and what prefilter (RAG, classifier, role tiers) fixes it? — *answered by:* skill-routing eval on a synthetic catalog of PM skills; ask Stripe for the promised follow-up post — *affects:* open-standard skill, plugin bundle



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Agent profile as a data bundle | An agent product = system prompt + skills + extensions + sandbox policy + model defaults, built reproducibly (Nix) and shipped as a bundle; skills live as files in the monorepo next to code | Shopify Aquifer profiles; World skills, AGENTS.md, channel-preloaded skills | New agents are cheap; skills reviewed like code; one checkout-warehouse skill reused by 12 teams (claimed) | Format not stated (SKILL.md or own); Nix is a steep dependency; no portability claim | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [Tobi article](../research/sources/x-tobi-learning-on-the-shop-floor.md) (first-party) |

Key questions (River pass):
- Should our unit of packaging be the skill (portable file) or the whole agent profile (prompt + skills + tools + policy + model defaults)? — *answered by:* prototype packaging two PM agents both ways — *affects:* skill-file vs profile-bundle options

---

## capability-distribution-trust: Capability distribution and trust
**Choice:** How skills and plugins reach users and are trusted: public registries, a vendor-managed org marketplace, an org-governed private registry with scan plus review plus version pin, eval-gated changes, or Git-backed marketplace with hidden Git.
**Why it matters to the strategy:** Skills ecosystems carry an evidenced supply-chain risk and plugin code runs with user privileges; how capabilities are reviewed, versioned and distributed is owned by security and platform teams rather than by authors.
**Related themes:** [[skills-marketplace]], [[org-learning-loop]]   **Related dimensions:** [[capability-format-portability]], [[governance-control-plane]], [[adoption-model]]
Formerly: capability-packaging (registry, catalog and marketplace rows and questions) and governance-control-plane (plugin policy, registry-gate and eval-gate rows; key questions 4-6), per 01-synthesis.md D.0 and D.5. The original capability-packaging framing is kept under [[capability-format-portability]].

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Git-backed skills marketplace with hidden Git | Markdown skills; publish creates branch/PR/review invisibly; role-aware recommender (Sensei) | Ramp Dojo, 350+ skills claimed | Non-engineers contribute; versioned, reviewed; sharing at scale | Count only, no usage/quality data; curation/review load; skills stay in the host harness | early-adopter | [Goddijn article](../research/sources/x-sebgoddijn-glass-article.md), [Buchan](../research/sources/x-shanebuchan-how-we-built-glass.md) (first-party) |
| Shared tool catalog | Hundreds of tools built with product teams, reused by all agents and internal repos | Ramp tool catalog | Reuse; gap visibility | Needs owners per tool | early-adopter | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party) |
| Org-governed private skills registry | Teams author in Git; central registry validates (structure, secrets, prompt injection), human-reviews, versions and distributes to several harnesses | PayPal skills registry; Ramp Dojo; Claude org plugin sync; Vercel skills CLI as public analogue | Decentralised authoring with central trust; harness-neutral distribution (PayPal names Claude Desktop and Codex) | Review bottleneck; no usage or quality numbers published by anyone; PayPal Agent Plugins are planned | emerging | [PayPal](../research/sources/paypal-agent-skills-at-enterprise-scale.md) (first-party); [Claude org sync](../research/sources/anthropic-claude-org-plugin-sync.md), [org mgmt](../research/sources/anthropic-claude-code-plugins-org-management.md) (first-party) |
| Public skills registries | Community directories and installers | skills.sh/`npx skills add`, ClawHub, Anthropic official/community marketplaces | Fast discovery, cross-agent installers | Highest supply-chain risk: Snyk 36.8% any issue, 13.4% critical, 76 malicious in 3,984; 400 confirmed malicious of 150k in a 7-registry scan | early-adopter | [Snyk](../research/sources/snyk-toxicskills-study.md) (vendor claim); [MalSkills](../research/sources/arxiv-malskills.md) (independent); [Vercel skills](../research/sources/vercel-skills-sh-open-skills-ecosystem.md) (vendor claim) |
| Vendor-managed plugin policy | Org marketplace allow/block lists, force-enabled plugins, sideload bans, update policy, plugin telemetry via managed settings / admin console | Claude Code managed settings, claude.ai org plugin sync, Analytics API | Real fleet control over which skills/plugins/hooks load, plus install and invocation counts | Claude-only; per-group targeting needs endpoint-managed settings; allowlist does not restrict entries inside an allowed marketplace; third-party plugin names aggregated as `third-party` | early-adopter | [org mgmt](../research/sources/anthropic-claude-code-plugins-org-management.md) (first-party) |
| Registry-gate for skills (scan + review + version pin) | Fail-closed automated checks and human approval before a skill reaches users; revalidate every version | PayPal skills registry; Snyk `mcp-scan --skills`; Claude community marketplace commit-SHA pins | Addresses the evidenced supply-chain risk; auditable | Scanners miss natural-language payloads (CSA); evidence on false-negative rates is thin; plugin hooks/MCP run outside sandbox even after review | emerging | [PayPal](../research/sources/paypal-agent-skills-at-enterprise-scale.md) (first-party); [plugin security](../research/sources/anthropic-claude-code-plugin-security.md) (first-party); [CSA](../research/sources/csa-skill-md-context-poisoning.md) (independent); [MalSkills](../research/sources/arxiv-malskills.md) (independent) |
| Eval-gated skills/plugins | Skill/plugin changes must pass trigger and outcome evals vs a no-skill baseline in CI | `claude plugin eval` (3 runs with/without), skill-creator evals, SkillsBench-style benchmarks | Detects regressions and model-change breakage; quantifies value (SkillsBench: curated +16.2pp avg, 16 of 84 tasks worse) | Billed model calls; per-vendor tooling that does not read each other's cases; no cross-harness eval runner found | emerging | [plugin evals](../research/sources/anthropic-claude-code-plugin-evals.md) (first-party); [SkillsBench](../research/sources/arxiv-skillsbench.md) (independent) |

See also: the packaging-risk evidence note for skills ecosystems ("Added evidence (research-pm-agents-jobs-to-be-done)") is kept with the format rows under [[capability-format-portability]].

### Key questions to choose
3. How many of Dojo's skills are actually reused, and what is their quality control? (Ramp reports counts only) — *answered by:* ask Ramp/analogous adopters; prototype a marketplace — *affects:* skills options
4. What review model keeps a company-wide skills repo healthy without a central bottleneck? — *answered by:* trial of publish/review flow — *affects:* skills marketplace
8. Who owns the skill lifecycle (authoring, review, versioning, deprecation, evals), and will users accept a review step? The spec offers only free-text `metadata.version` and no compatibility guarantees. - *answered by:* policy owner / platform team; trial with PayPal/Ramp-style publish flow - *affects:* private registry options
- From governance-control-plane (numbered as filed there):
4. Is a skill/plugin an acceptable unit of trust, given plugin hooks, monitors and MCP servers run with user privileges outside Claude Code's sandbox? Which components do we allow in an internal marketplace (skills only? skills + MCP?) - *answered by:* security review / policy owner; test in a sandboxed runtime - *affects:* plugin bundle, public registries
5. What review and scan pipeline is proportionate (PayPal-style fail-closed checks vs allowlist of sources only), and what is its measured miss rate? - *answered by:* red-team a pilot registry with seeded malicious skills; more research on scanner evasion - *affects:* registry-gate options
6. Can governance for skills be uniform across harnesses, when each vendor's controls (managed settings, Codex ADMIN path, Copilot org settings) are separate? - *answered by:* vendor trial of Codex/Copilot admin controls (not researched here); Track 1 control-plane research - *affects:* vendor-managed vs control plane above harnesses

Attribution for the rows and questions from capability-packaging, then for those from governance-control-plane:
### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 (proposal: consider splitting this dimension into "capability-format-portability" and "capability-distribution-trust"; see track-4 report) | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24
### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 5 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24 | user-story-mapping pass on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Federated domain-owned control plane | Domain owners build, test and monitor their skills, custom agents and tool selections in a studio, organised into "areas", with usage and quality signals per asset; any user can publish a skill from a session; platform suggests improvements; telemetry promotes popular skills into the general context and moves niche ones out | Stripe Agent Studio + Kai skill creator | Expertise scales without centralising; quality signals visible to owners; context kept lean | Needs telemetry pipelines and owner accountability; review rules for "area" publishing not disclosed | early-adopter | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| No-code micro-agent builder (reported failure) | Anyone builds and deploys workflow agents with tools | Stripe NoCode Agent Builder (4,000+ agents, before Kai) | Fast, bottom-up | Similar prompts of uneven quality; sprawl hard to monitor and maintain; replaced by one agent plus skills | mainstream (as a pattern); retired at Stripe | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party) |
| Centrally run tool server that teams extend | One MCP server of all internal tools; owning teams add their own systems | Stripe Toolshed (~500 tools) | No central bottleneck for tools; reused by Kai, Minions and other agents | Tool sprawl; needs tool-level access control | early-adopter | [Latent Space, Sands](../research/sources/latentspace-emily-sands-stripe.md) (first-party); [LangChain case study](../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor claim) |

Key questions (Stripe pass):
8. Compared with Glass's Git-backed Dojo, does a studio with usage/quality signals and automatic suggestions keep a 2,000-skill library healthy, or does it still need human review and deprecation rules? — *answered by:* ask Stripe for skill quality and deprecation data; pilot telemetry on our own skill set — *affects:* Git-backed marketplace, org-governed registry, eval-gated skills


---

## remote-invocation-route: How a primary harness reaches a remote or deployed agent
**Choice:** When Claude Code, Codex or another general harness needs a powerful agent that runs elsewhere, does it use in-process subagents, a vendor cloud delegation, an MCP tool (sync or with Tasks), an A2A call, an event/CI trigger, or a human-triggered handoff?
**Why it matters to the strategy:** It decides whether a standardised task agent (code review, PRD review) can live outside any one harness and still be called from the harness users already have, and what latency, auth and debugging cost that adds. Proposed as a new dimension (Track 3); the director may prefer to merge it into capability-packaging.
**Related themes:** [[remote-agent-invocation]], [[identity-delegation]], [[harness-portability]], [[agent-failure-modes]]   **Related dimensions:** [[capability-format-portability]], [[runtime-location]], [[governance-control-plane]], [[loop-source]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| In-process subagent only (no remote) | Delegation inside the same session; own context window, tool allowlist, model | Claude Code subagents (up to 3 nesting layers, 20 concurrent), Copilot/Codex custom agents | Zero infrastructure; shares auth, permissions and usage limits | Same machine and lifetime as the session; no sharing; consumes the session's usage limits | mainstream | [Claude Code subagents](../research/sources/anthropic-claude-code-subagents.md) (vendor) (vendor claim) |
| Human-triggered handoff to the vendor cloud | User or script starts a cloud session from the harness and pulls it back | `claude --cloud`, `claude -p ... --cloud <id>`, `--teleport`; Codex cloud from web/CLI/Slack; Copilot cloud agent from issues | No protocol or infra to run; work continues while the laptop sleeps; parallel tasks | Vendor-specific and mostly GitHub-centric; handoff is one-way (cloud to terminal); excluded for ZDR/HIPAA/CMEK orgs and third-party model providers; Copilot cap 59 min/session | early-adopter | [Claude Code cloud sessions](../research/sources/anthropic-claude-code-cloud-sessions.md) (vendor), [Codex cloud](../research/sources/openai-codex-cloud-docs.md) (vendor), [Copilot cloud agent](../research/sources/github-copilot-cloud-agent.md) (vendor) (vendor claim) |
| Vendor background-agent API | Another system creates, steers and polls cloud agents over REST/SSE | Cursor Cloud Agents API (public beta, no webhooks in v1), Jules v1alpha API, Anthropic Managed Agents API (beta), Devin | Programmatic delegation from CI, bots or a custom harness; streaming and steering | Betas/alphas; each vendor's own API (no common protocol); community MCP wrappers are unofficial; quality of autonomous runs unpredictable | emerging | [Cursor API](../research/sources/cursor-cloud-agents-api.md) (vendor), [Jules API](../research/sources/google-jules-api.md) (vendor), [Managed Agents](../research/sources/anthropic-managed-agents-overview.md) (vendor) (vendor claim); [Answer.AI on Devin](../research/sources/answerai-thoughts-month-with-devin.md) (independent) (independent, dated) |
| MCP tool backed by an agent, synchronous | The harness calls an MCP tool; behind it is a deployed agent with its own loop and data | Glean agents as MCP tools; Sentry MCP with Seer; community CodeRabbit/Greptile wrappers | Works in any MCP host (Claude Desktop, Cursor, VS Code, Claude Code); admin-curated; bounded read-only capability that is easier to audit than shell access | Host timeouts (~30-60s, vendor-reported); no write tools or human-in-the-loop (Glean forbids them); tool-list bloat; sampling deprecated so the server brings its own model; no independent quality data found | early-adopter | [Glean](../research/sources/glean-agents-as-mcp-tools.md) (vendor), [Sentry](../research/sources/sentry-mcp-server-seer.md) (vendor) (vendor claim); [Willison](../research/sources/simonwillison-stateless-mcp.md) (independent) (independent, on auditability) |
| MCP tool with the Tasks extension | Server returns a durable task handle; client polls; task can pause as `input_required` | MCP Tasks extension (2026-07-28 revision); Claude Code MCP tasks (public beta, v2.1.304+) and 2-minute auto-backgrounding | Long-running agent-like backends without holding a connection; survives client restart; human input mid-task | Extension, so host support varies (`claude -p` does not wait for MCP tasks); very new; no production accounts found | emerging | [MCP Tasks](../research/sources/mcp-ext-tasks-long-running-operations.md) (first-party) (first-party spec); [Claude Code MCP docs](../research/sources/anthropic-claude-code-mcp-tasks-oauth.md) (vendor) (vendor claim) |
| A2A agent | Remote agent publishes an Agent Card; caller sends tasks over JSON-RPC/gRPC/REST with streaming or push | A2A v1.0; AWS AgentCore Runtime A2A hosting; Copilot Studio A2A client; Gemini CLI connects remote A2A agents (HN anecdote); community bridges to Claude Code | Vendor-neutral task lifecycle incl. INPUT_REQUIRED/AUTH_REQUIRED; cross-organisation boundaries; signed cards | Evidence is ecosystem membership (150+ orgs) not named production use; no native A2A client found in Claude Code or Codex; identity and delegation left to implementers; skeptics return to MCP/HTTP | emerging (spec v1.0; adoption unproven) | [A2A spec](../research/sources/a2a-project-specification-v1.md) (first-party) (first-party); [LF press release](../research/sources/linuxfoundation-a2a-one-year-press-release.md) (vendor) (vendor claim); [Glukhov](../research/sources/glukhov-a2a-adoption-hype-reality.md) (independent) (independent); [Ask HN](../research/sources/hn-ask-is-anyone-using-a2a.md) (anecdote) (anecdote) |
| Event or CI-triggered task agent | A workflow, cron or webhook runs the harness headless with a plugin skill as the prompt | Claude Code GitHub Actions (`/code-review:code-review`), Claude Code routines /fire endpoint, Cloudflare AI code review on OpenCode | Cheap shared reviewer versioned in the repo; OIDC federation avoids stored keys; per-run caps (`--max-turns`) | Not interactive; permission prompts denied in unattended runs; CI minutes plus tokens; GitHub-centric | early-adopter | [GitHub Actions](../research/sources/anthropic-claude-code-github-actions.md) (vendor) (vendor claim); [Cloudflare code review](../research/sources/cloudflare-ai-code-review-opencode.md) (first-party) (first-party, Cloudflare) |
| Self-hosted agent service | Org runs the Agent SDK or another loop as its own service callable by others | Agent SDK in Docker/Modal/Kubernetes (ephemeral, long-running, hybrid with SessionStore); Ramp Inspect/Glass | Full control of tools, data, identity and model | One subprocess per session, memory growth, no session timeout, own multi-tenant isolation; tokens dominate cost | early-adopter | [Agent SDK hosting](../research/sources/anthropic-agent-sdk-hosting.md) (vendor) (vendor claim) |
| Cross-harness delegation plugin | One vendor's harness delegates to another via a plugin | OpenAI `codex-plugin-cc` (review, rescue, background jobs) in Claude Code | Second opinion from a different model family; no infra | Local only; depends on the other vendor's app-server protocol; OpenAI removed the older `codex mcp-server` route, so integrations break; review-gate loop can drain limits | early-adopter | [codex-plugin-cc](../research/sources/openai-codex-plugin-for-claude-code.md) (first-party), [Codex MCP removal](../research/sources/openai-codex-mcp-server-removed.md) (first-party) (first-party) |

### Key questions to choose
1. Can the target standardised workflow (e.g. PRD review) finish inside host timeouts (about 30-60s per Glean) or does it need the Tasks extension, and do the hosts our users actually use support Tasks? — *answered by:* prototype one workflow as a sync MCP tool and as a Tasks tool, plus the MCP client support matrix — *affects:* MCP sync vs MCP Tasks vs vendor cloud
2. Do we have a genuine multi-owner or multi-vendor boundary that justifies A2A, or does an agent behind MCP / plain HTTP do? Which of our target hosts can act as an A2A client at all (Gemini CLI and Copilot Studio yes; none found for Claude Code or Codex)? — *answered by:* architecture review with candidate adopting teams; a feature check against the hosts — *affects:* A2A vs MCP
3. Is there independent evidence on quality, latency and cost of an agent reached over MCP or A2A (none found for Seer, CodeRabbit, Greptile, Glean)? How would we measure it? — *answered by:* a time-boxed trial of one existing remote agent from Claude Code with a no-agent baseline; interviews with existing users — *affects:* all remote options
4. With Sampling deprecated in the 2026-07-28 MCP revision, who pays for and chooses the model of a deployed task agent, and how is per-caller cost attributed? — *answered by:* policy/finance owner; design review — *affects:* MCP/A2A/self-hosted
5. How stable are vendor routes (Codex removed its MCP server; Cursor and Jules APIs are beta/alpha; Managed Agents is beta)? What is our exit cost if one changes? — *answered by:* vendor roadmap review; wrapper/adapter spike — *affects:* vendor API, cross-harness plugin
6. Which jobs can tolerate fire-and-forget autonomy, given the only independent test (Answer.AI, Jan 2025, 3/20) and its failure modes (infeasible tasks pursued, no blocker flagged)? — *answered by:* pilot on one job with human review gate; fresh independent evaluation of a current product — *affects:* vendor cloud and API options
7. Who debugs a failed call that crosses harness, protocol and remote runtime (traces, cost, logs)? — *answered by:* prototype with OpenTelemetry trace context (`traceparent` in MCP `_meta`) end to end — *affects:* all remote options

### Current lean (optional) and what would change it
Evidence so far favours MCP (sync, with Tasks for long jobs) over A2A for harness-to-agent calls today, because every named MCP host already supports MCP, concrete examples exist (Glean, Sentry), and A2A's production evidence is membership rather than use; this is thin, mostly vendor-sourced. It would change if a primary harness ships a native A2A client, or if independent accounts of A2A in production appear.

### Added by: research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Chat reaction on any message starts a remote agent | Emoji reaction (e.g. create-minion with repo) turns the message into the prompt; agent replies in-thread with a follow-along link; works from a phone | Stripe Minions in Slack | Lowest activation energy; any employee can start work where it is discussed | Only fits one-shot tasks with strong CI; who may trigger which repos is not described | early-adopter | [How I AI, Kaliski](../research/sources/howiai-stripe-minions-kaliski.md) (first-party) |
| Specialist tool exposes its toolset and engine over internal MCP | A specialised agent product publishes CRUD/publish tools and a rendering service other agents call | Stripe Harbor (used by Kai and devbox coding agents) | Agents stay specialised but chain without copy-paste; artifacts move between tools | Identity and ownership across hops not described | early-adopter | [Harbor post](../research/sources/stripe-harbor-ai-prototyping.md) (first-party) |
| Self-hosted agent service (evidence row) | Agents run as a shared internal service called by product tooling | Stripe compliance agents in review tooling | Embeds agents in existing work tools | Platform to run | early-adopter | [AWS/Stripe compliance post](../research/sources/aws-stripe-compliance-agents.md) (first-party, vendor-hosted) |



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Chat mention as the human route; external wake-up for automation | Humans @-mention the agent in Slack; systems wake durable sessions (PR review) or run ephemeral jobs (CI) on the same stack; workflows open their own threads | Shopify River (interactive), PR review (automation), CI/batch (job); security remediation opening one thread per finding | One stack, three modes; automation results land where humans already are | No API/MCP/A2A route for other harnesses documented; Slack as the bus | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [vuln remediation](../research/sources/shopify-engineering-river-vulnerability-remediation.md) (first-party) |

---

## session-persistence-sharing: Session persistence, sharing and handoff
**Choice:** Are sessions ephemeral and private, resumable, shared live with other people, or persistent and event-driven; and when work moves between people, devices or harnesses, what moves with it (fork-copy, move toggle, branch-only, message-in, neutral trace record, retained transcripts)?
**Why it matters to the strategy:** It is the shift from "local, private, ephemeral" to "deployed, shareable, multi-user, persistent", and shared or persistent sessions are only useful if people can pick them up; handoff is one of the decisions inside that shift.
**Related themes:** [[shared-persistent-sessions]], [[org-learning-loop]], [[memory-architecture]], [[harness-portability]]   **Related dimensions:** [[runtime-location]], [[durability-substrate]], [[agent-identity-delegation]], [[harness-layering]]
Formerly: session-persistence-sharing, session-handoff-portability (handoff merged in as a sub-axis, per 01-synthesis.md D.0)

### Sub-choice: session-persistence-sharing — Session persistence and sharing
**Choice:** Are sessions ephemeral and private, resumable, shared live with other people, or persistent and event-driven?
**Why it matters to the strategy:** It is the shift from "local, private, ephemeral" to "deployed, shareable, multi-user, persistent".
**Related themes:** [[org-learning-loop]], [[memory-architecture]], [[compounding-context-repo]]   **Related dimensions:** [[runtime-location]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Ephemeral-private | Today's default | Local Claude Code | Simplicity, privacy | Knowledge lost; no collaboration | mainstream | to be linked |
| Shared / multiplayer | Several people in one session | Glass, Inspect, Omnigent | Collaboration, learning once | Permissions, noise | early-adopter | [Glass launch](../research/sources/ramp-introducing-glass.md) (first-party) |
| Persistent / event-driven | Agent keeps running and reacts | Cloudflare OS, scheduled tasks | Work continues unattended | Cost, trust, failure handling | emerging | to be researched |
| Shared sessions + shared knowledge edits | Hand a session to a colleague mid-task; users edit what the agent knows (323 employees, 6,500+ edits) | Ramp Glass | Cross-role collaboration; learn once | Permissions, noise; no data on how often sharing is used | early-adopter | [Glyman launch](../research/sources/x-eglyman-introducing-glass-learn-things-once.md) (vendor claim) |
| Multiplayer-first background agent | Sandbox sessions several people can join; Slack-thread context carried in | Ramp Inspect | Pairing PM/design with engineers | Sandbox cost | early-adopter | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party) |
| Single-owner vendor cloud session, share by link | Session runs in a vendor VM and survives laptop close; teammates get a Team-visibility snapshot link or (Warp) can attach and steer | Claude Code on the web, Codex cloud, Warp Oz | Persistence without ops; mobile steering; Team visibility with repo-access check | Shared view is not live ('their view doesn't update in real time'); one-way terminal handoff; sessions expire on inactivity and lose running subagents/shell jobs | early-adopter | [Claude cloud docs](../research/sources/anthropic-claude-code-cloud-sessions.md) (first-party); [Warp Oz](../research/sources/warp-oz-cloud-agents.md) (first-party) |
| Live multiplayer on a per-session control plane | One session object holds state and a WebSocket hub; many clients (web, Slack, GitHub) prompt it, with presence and authored prompts | Ramp Inspect; Open-Inspect (open source, Cloudflare Durable Object per session) | Real co-working across roles; attributed prompts in commits | Single-tenant trust model; visibility enforcement off by default in Open-Inspect; credentials cached on disk; adoption figures vary by source | early-adopter | [Open-Inspect README](../research/sources/github-open-inspect-background-agents.md) (first-party); [Modal on Inspect](../research/sources/modal-ramp-inspect-background-agent.md) (vendor claim); [Wavect](../research/sources/wavect-ramp-inspect-architecture.md) (independent) |
| Durable session log decoupled from harness and sandbox | Append-only session event store outside both; a crashed harness is restarted from the log; a lost container is a tool error | Claude Managed Agents | Crash recovery without losing the session; credentials kept away from generated code | Vendor-hosted loop; multi-user semantics not stated; performance numbers are Anthropic's | emerging | [Managed Agents post](../research/sources/anthropic-engineering-scaling-managed-agents.md) (first-party) |
| One-shot isolated task runs, human at the PR | No shared live session: each task gets its own pooled devbox, runs to a PR with a capped CI retry, and a human reviews | Stripe Minions | Bounded blast radius; scales to many parallel runs; simple trust story | Not interactive or collaborative; works because Stripe has a strong test suite and devbox infra | early-adopter | [Stripe Minions part 2](../research/sources/stripe-minions-part-2.md) (first-party) |
| Scheduled / event-triggered cloud runs | Cron, API and webhook triggers start fresh sessions unattended | Claude scheduled tasks, Warp Oz schedules, Open-Inspect automations, Cloudflare Agents alarms | Work happens with the laptop closed | Claude's are personal, not team-shared, and act as the creator; runs can be skipped or dropped silently (72 h GitHub lapse, webhook caps); 'green' does not mean the work succeeded | early-adopter | [Claude scheduled tasks](../research/sources/anthropic-claude-code-scheduled-tasks.md) (first-party); [Cloudflare long-running agents](../research/sources/cloudflare-agents-long-running-agents.md) (first-party) |
| Reported failure of autonomous async agents | Evidence on what goes wrong when sessions run unattended | Devin (Answer.AI, Jan 2025: 3 of 20 tasks succeeded), Replit/SaaStr (Jul 2025), Kiro (reported, disputed) | Calibrates how much autonomy to allow | Dated and product-specific; Replit and Kiro accounts rest on the affected user or press reports | n/a (evidence) | [Answer.AI Devin](../research/sources/answerai-month-with-devin.md) (independent); [The Register on Replit](../research/sources/theregister-replit-saastr-response.md) (independent); [The Decoder on Kiro](../research/sources/the-decoder-aws-kiro-outage.md) (independent) |
| Hybrid: ephemeral container hydrated from a session store | Container spins down when idle; transcript restored by session ID from a SessionStore | Agent SDK `resume` + `SessionStore`; Managed Agents server-side log; Cloudflare/Temporal-style durability (Track 5) | Cheap idle; resumable for hours or days | Store mirrors transcripts only (not CLAUDE.md memory or working-directory files); mirror writes are best-effort | early-adopter | [hosting guide](../research/sources/anthropic-agent-sdk-hosting.md) (first-party); [Managed Agents](../research/sources/anthropic-managed-agents-overview.md) (first-party) |
| Shared live session over any harness | Server stores sessions and shares them by URL, with comments, steering, attach and fork, independent of which harness runs | Omnigent, Warp Oz run pages, Polygraph session graph | Colleagues join a Claude Code or Codex session; resume with a different agent | Open issues: chat access not separated from host access (#11413), side chats not allowed on another user's host (#11414), sessions stuck 'running' | emerging | [Omnigent repo](../research/sources/github-omnigent-repo.md) (vendor claim + open issues); [Polygraph](../research/sources/nx-polygraph-meta-harness.md) (vendor claim); [Warp Oz](../research/sources/warp-oz-multi-harness.md) (vendor claim) |
| Shareable apps with data-free blueprints | Work products are small apps; sharing the app shares live state, sharing a blueprint copies code without data, history, credentials or connections | Cloudflare OS | Clear line between sharing results and sharing a recipe; viewer permission re-check | Per-user copies may be a maintenance burden (HN); needs the platform's app model | emerging | [announcement](../research/sources/cloudflare-os-announcement.md) (vendor claim); [HN](../research/sources/hn-cloudflare-os-thread.md) (anecdote) |

#### Key questions to choose
1. Which user activities actually benefit from sharing or persistence, and which should stay private? — *answered by:* user interviews, usage data — *affects:* all
2. How is memory shared safely across users? — *answered by:* Track 5 research, prototype — *affects:* shared, persistent
3. What share of Glass sessions are shared, and does sharing change outcomes? — *answered by:* ask Ramp; design a pilot metric — *affects:* shared/multiplayer
4. Which target activities need live co-presence in one session, and which are fine with a share-by-link snapshot or a handoff? (No data yet on how often Glass or Inspect sessions are shared.) — *answered by:* user interviews; ask Ramp for usage data; a pilot metric — *affects:* live multiplayer vs single-owner snapshot
5. Which unattended jobs do users actually want (digests, triage, PR fixes), and how often must they run when no one's laptop is on? — *answered by:* job inventory with users; trial of cloud scheduled tasks on two real jobs — *affects:* scheduled/event-triggered, org-deployed
6. What retention, location and access rules apply to session transcripts (Claude Code deletes local ones after 30 days by default; cloud and self-hosted keep them with the vendor)? — *answered by:* policy/security owner; compare vendor docs for the harnesses in use — *affects:* all persistent options
7. Is independent evidence available of teams running shared or persistent agent sessions at scale and what went wrong? Found so far: Ramp and Stripe self-reports, and independent evidence only for failures and design critiques (Answer.AI, Tenable, Wavect, forum threads). — *answered by:* more research (practitioner interviews, conference talks, incident write-ups) — *affects:* all
8. What is the per-session cost of persistence and concurrency (VM, snapshots, tokens) at our expected number of users, and who pays? — *answered by:* pilot with metering; vendor pricing review (Claude cloud counts against plan limits; Warp charges credits and bars BYOK) — *affects:* vendor cloud, deployed
9. What state must survive a container restart for our jobs (transcript, memory files, working files, tool state), and does the chosen SDK/hosted option persist all of it? — *answered by:* list state per job; test kill-and-resume on a prototype — *affects:* hybrid, persistent options
10. Is the unit we want to share the conversation, the output/app, or a reusable recipe (blueprint/skill)? — *answered by:* user interviews on what colleagues actually reuse — *affects:* shared session, blueprint options
11. How do shared sessions treat the viewer's permissions: inherit the creator's access (risk, per Cursor findings) or re-check the viewer (Cloudflare OS design)? — *answered by:* security/policy owner; prototype — *affects:* all shared options
- (user-story-mapping) When a PM hands work to a reviewer ([S13](../tasks/user-story-mapping/stories-cross-cutting.md#s13-hand-work-to-a-teammate-and-get-their-input)), do reviewers want to enter the session (snapshot or live) or receive a finished artifact? — *answered by:* user interviews with the reviewing roles; two-version walkthrough using S05 journeys A and B — *affects:* shared/multiplayer, persistent/event-driven, ephemeral-private
- (user-story-mapping) How many of the 18 stories are recurring or need work to proceed while the PM is away ([S14](../tasks/user-story-mapping/stories-cross-cutting.md#s14-have-recurring-work-happen-without-me-prompting))? — *answered by:* a story inventory scored with PMs for how often each recurs and whether it must run unattended — *affects:* laptop-as-server versus deployed options (see [[runtime-location]])

#### Audit additions (competitive-teardown-ramp-glass, 2026-10-24)
Evidence (first-party, [Building Laminar](../research/sources/ramp-builders-building-laminar.md)): Laminar makes agents non-blocking by default and keeps "the agent session always open to new input", with human-in-the-loop approvals, message queuing and steering, subagent handoffs, multiplayer sessions and Slack as a first-class client; Glass tasks "can take minutes or hours". Session state (definition, history, turn state) lives in Postgres independent of any sandbox, so sessions survive sandbox and worker churn.

Key question (unranked):
- Ramp's multiplayer and always-open sessions depend on a cloud session store. Which of these properties do we lose if sessions stay in a local vendor harness, and which could a thin shared layer add back? — *answered by:* feature matrix across Claude Code/Cowork/Codex vs Laminar-style store; prototype — *affects:* shared, persistent

#### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 5 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | user-story-mapping pass on 2026-10-24 | audit pass: competitive-teardown-ramp-glass on 2026-10-24

### Sub-choice: session-handoff-portability — Handing a session between people, devices and harnesses
**Choice:** When work moves (laptop to cloud, cloud to laptop, person to person, harness to harness), what moves with it: the repo branch only, a forked copy of the transcript, or the live session itself?
**Why it matters to the strategy:** Shared and persistent sessions are only useful if people can pick them up, and today's products handle handoff asymmetrically.
**Related themes:** [[harness-portability]], [[shared-persistent-sessions]], [[memory-architecture]]   **Related dimensions:** [[session-persistence-sharing]], [[loop-source]], [[harness-layering]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Fork-copy handoff | Pull the session and branch into a terminal; the copy is independent | Claude `--teleport` | Full history locally | Needs clean git state, same repo and account; new work does not appear in the cloud session; terminal-to-cloud only as a new session or via Desktop | early-adopter | [Claude cloud docs](../research/sources/anthropic-claude-code-cloud-sessions.md) (first-party) |
| Move-to-cloud/local toggle | Same agent moved between machine and cloud | Cursor 3.x | One agent identity | Cloud-origin to local missing unless a local agent exists; GitLab handoff failure reported; staff: not being actively built | early-adopter | [Cursor forum](../research/sources/cursor-forum-cloud-to-local-handoff.md) (anecdote) |
| Branch-only handoff | Fetch the agent's branch and start fresh | Any harness | Harness-neutral | History and reasoning lost | mainstream | [Cursor forum](../research/sources/cursor-forum-cloud-to-local-handoff.md) (anecdote) |
| Message into a running session from anywhere | CLI or API posts a follow-up to a cloud session | `claude -p ... --cloud <id>`; Claude `/fire` API; Slack mentions | Humans and systems can steer one session | Identity of the sender vs the session owner varies by product (see governance) | early-adopter | [Claude scheduled tasks](../research/sources/anthropic-claude-code-scheduled-tasks.md) (first-party) |
| Neutral trace/attribution record | Vendor-neutral record linking code to the conversation that wrote it | Agent Trace (draft), Radar: Assess | Cross-harness audit and replay hooks | Early draft; storage not prescribed | emerging | [Thoughtworks Radar](../research/sources/thoughtworks-radar-agent-trace.md) (independent) |
| Retained transcripts as the shared record | Keep and publish transcripts for review and learning | Claude Code local files (30-day deletion default) | Review of reasoning | Retention default deletes; credentials in plain text | mainstream | [ITdaily](../research/sources/itdaily-claude-code-30-day-transcript-deletion.md) (independent) |

#### Key questions to choose
1. When users hand work to a colleague, do they need the transcript, only the branch plus a summary, or the live session? — *answered by:* user interviews; observe a handoff in a pilot — *affects:* all
2. Is cross-harness portability of a session (not just skills) a real need, or only per-harness handoff? — *answered by:* user interviews; Track 1 and 4 findings — *affects:* neutral trace, branch-only
3. Where should the canonical transcript live and who may delete it? — *answered by:* policy/legal owner — *affects:* retained transcripts, vendor-hosted options
4. Can a neutral record (Agent Trace or similar) be captured from the harnesses we would support, and is it enough for audit? — *answered by:* prototype of trace capture — *affects:* neutral trace
- (user-story-mapping) What must survive a session ending (reasoning, decisions, sources, the transcript itself) and for how long? ([S11](../tasks/user-story-mapping/stories-cross-cutting.md#s11-pick-up-where-i-or-someone-else-left-off-and-find-the-artifacts)) — *answered by:* the baseline interviews above; retention policy owner — *affects:* retained transcripts, neutral trace record, branch-only handoff

#### Added by: research-agent-runtime-patterns-taxonomy (Track 5) on 2026-10-24 (proposal: merge into session-persistence-sharing if the director prefers fewer dimensions) | user-story-mapping pass on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Long-lived single-user cloud session with evolving artifacts | Cloud-hosted session where artifacts live beside the chat and are iterated over hundreds of turns and weeks; private to the user; sharing on the roadmap | Stripe Kai (932-turn session) | Deep work without timeouts; token-efficient artifact edits | Context "locked in"; no handoff or co-editing yet | early-adopter | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Share the artifact, not the session | Publish one snapshot to a URL; viewers comment on elements; anchors re-resolve after the agent rewrites; remix into a copy | Stripe Harbor | Collaboration without exposing session context | Discussion lives outside the agent session | early-adopter | [Harbor post](../research/sources/stripe-harbor-ai-prototyping.md) (first-party) |
| Public chat channel as the observable run log | Agent runs triggered and reported in an open Slack channel others follow | Stripe Minions "robots" channel (76 people) | Open-by-default learning, "pair prompting" | Channel membership is the access boundary; noise | anecdote | [How I AI, Kaliski](../research/sources/howiai-stripe-minions-kaliski.md) (first-party) |

Key questions (Stripe pass):
9. Stripe chose single-user sessions plus shareable artifacts, Ramp chose shareable sessions: which do our users need first for handoffs? — *answered by:* user interviews on handoff moments; prototype both — *affects:* ephemeral-private, shared/multiplayer, artifact sharing



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Durable, threaded, multiplayer, public by construction | Session identity is an append-only Postgres event log; harness and sandbox die freely; the human surface is a public Slack thread anyone can join | Shopify River on Aquifer | Work survives process death; second humans join mid-task; searchable corpus; 171,853 same-thread co-writing links in Sep 2026 (self-reported) | Public-only has privacy costs (see [[trust-privacy-defaults]]); live sandbox state beyond the log not described; all figures self-reported | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [chart](../research/sources/x-tobi-river-floods-shopify-chart.md) (first-party) |

Key questions (River pass):
- Shopify's thread pattern is "agent pulled into a human conversation already in progress". How often does that happen in our target users' work, versus a person starting a task alone? — *answered by:* observation of PM threads; pilot metric (share of agent sessions with 2+ humans) — *affects:* multiplayer vs single-owner options

---

## agent-identity-delegation: Agent identity and delegation
**Choice:** Whose authority a shared or delegated agent uses: the creator's tokens (teammates can steer), the requester's account, an admin-provisioned service identity with scoped bundles, the agent as co-author under human approval, environment-bounded with no human credentials, or per-server OAuth with token exchange or a vault for downstream calls.
**Why it matters to the strategy:** The same question appears for shared sessions, remote invocation and governance; it decides what a shared agent can leak and who is accountable, and it has its own policy owner.
**Related themes:** [[identity-delegation]]   **Related dimensions:** [[governance-control-plane]], [[session-persistence-sharing]], [[remote-invocation-route]]
Formerly: governance-control-plane (the identity and delegation rows and questions, split out per 01-synthesis.md D.0; proposed by Tracks 3 and 5)

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Identity via SSO; central MCP config | Okta SSO, centrally configured connectors, self-healing re-auth | Ramp Glass | One-click connections; no IT tickets | Central team must own connectors; broad access risk | early-adopter | [Buchan](../research/sources/x-shanebuchan-how-we-built-glass.md) (first-party) |
| Agent runs as the creator, teammates can steer it | Session holds the initiating user's OAuth tokens; with Team Followups on, any teammate's follow-up runs as the creator | Cursor cloud agents | Easy team collaboration on one agent | Cursor staff confirm 'intended behavior'; a user reported follow-ups run as another person and the originating Slack prompt can be deleted; mitigations: creator-only or service-accounts-only | early-adopter | [Cursor forum](../research/sources/cursor-forum-team-followups-act-on-behalf.md) (anecdote) |
| Agent runs as the requester | Task runs under the requesting user's own account; follow-ups continue only from the same account; channel replies are visible to the whole channel | Codex in Slack | Clear attribution; no privilege escalation by teammates | Channel readers see output; different account starts a new task; personal environments excluded | early-adopter | [Codex Slack docs](../research/sources/openai-codex-cloud-slack.md) (first-party) |
| Agent runs as a service identity with scoped bundles | Shared channel agent acts as an admin-provisioned service account; access bundles attach to org/workspace/channel scopes | Claude Tag | Auditable service accounts; creds kept in a proxy; no personal tokens in shared channels | Everyone in the channel gets the same capability; channel membership becomes the IAM boundary (Tenable); still beta | emerging | [Claude Tag identity](../research/sources/anthropic-claude-tag-agent-identity.md) (first-party); [Tenable](../research/sources/tenable-claude-tag-slack-access-model.md) (independent) |
| Agent as co-author under human approval | Commits authored by the agent with the requesting human as co-author, signed and linked to the session log; draft PRs the requester cannot approve; only write-access users can trigger | GitHub Copilot cloud agent | Strong separation of duties; audit events for admins | Firewall covers only agent-started processes, not MCP servers; scope is GitHub repos | early-adopter | [Copilot risks](../research/sources/github-copilot-cloud-agent-risks.md) (first-party) |
| Bound blast radius by environment, not prompts | Full permissions inside an isolated QA devbox with no prod data or open egress; small curated MCP toolset; human review of every PR | Stripe Minions; Wavect's critique of Inspect-style sandboxes | Mistakes are contained; no per-action approvals needed | Needs QA environments, test suites and curated tools; the sandbox is not the policy (Wavect) | early-adopter | [Stripe Minions](../research/sources/stripe-minions-part-2.md) (first-party); [Wavect](../research/sources/wavect-ramp-inspect-architecture.md) (independent) |
| Per-server OAuth with audience-bound tokens (MCP) | Each remote MCP server is its own OAuth 2.1 resource server; tokens are bound to that server (RFC 8707) and must not be passed through to others | MCP authorization spec; Sentry and other hosted MCP servers; Claude Code `claude mcp login`; Cloudflare workers-oauth-provider | Standard consent and scopes (step-up on `insufficient_scope`); no shared master token | An agent calling downstream systems cannot reuse the caller's token: needs token exchange, a vault or Enterprise-Managed Authorization (listed Stable, mechanism not read); per-server consent fatigue; Dynamic Client Registration now deprecated | early-adopter | [MCP authorization](../research/sources/mcp-authorization-spec-draft.md) (first-party) (first-party); [Claude Code MCP docs](../research/sources/anthropic-claude-code-mcp-tasks-oauth.md) (vendor) (vendor claim) |
| Credential vault and proxy outside the agent sandbox | Agent holds a session-scoped token; a proxy fetches and attaches real credentials, so a prompt-injected sandbox cannot leak them | Managed Agents MCP proxy; Claude Code cloud GitHub proxy and network secrets; Agent SDK secure-deployment egress proxy | Limits credential exposure to injection | Still the agent's authority, not necessarily the user's; vendor-implemented, not portable across vendors | early-adopter | [Managed Agents design](../research/sources/anthropic-engineering-scaling-managed-agents.md) (vendor), [Cloud sessions](../research/sources/anthropic-claude-code-cloud-sessions.md) (vendor) (vendor claim) |
| OIDC workload-identity federation for CI agents | Pipeline exchanges its GitHub OIDC token for model-API access via a service account, no stored key; subscription OAuth tokens tied to one person are the weaker alternative | Claude Code GitHub Actions (Bedrock/Vertex/Foundry via OIDC; Console federation rules) | No long-lived secret; org-level service identity; per-run turn and budget caps | Only for CI-triggered agents; the shared GitHub App has a broad fixed permission set | early-adopter | [GitHub Actions](../research/sources/anthropic-claude-code-github-actions.md) (vendor) (vendor claim) |
| Agent Card signing and A2A security schemes | A2A agents declare API key, OAuth2, OIDC or mTLS in the card; cards can be signed (v1.0) | A2A spec; AgentCore (SigV4 or JWT); Copilot Studio (None/API key/OAuth) | Machine-readable auth requirements and cryptographic card identity | Credential issuance and delegation are left to implementers; secondary sources (Semgrep via grith/NHI Mgmt Group, unverified here) say signing is optional and identity is not propagated across hops | emerging | [A2A spec](../research/sources/a2a-project-specification-v1.md) (first-party) (first-party); [Copilot Studio](../research/sources/microsoft-copilot-studio-a2a.md) (vendor) (vendor claim); [Glukhov](../research/sources/glukhov-a2a-adoption-hype-reality.md) (independent) (independent, secondary) |

See also: "Zero-ambient-access capabilities plus observation log" (Cloudflare OS Gatekeepers holding credentials, viewer re-check) is under [[governance-control-plane]].

### Key questions to choose
7. Which identity model do target orgs accept for shared agents: acting as the requester, as a creator whose tokens teammates can drive, or as a scoped service account? — *answered by:* security/policy owners; threat-model workshop using the Cursor and Tenable findings — *affects:* all shared-session options
8. If channel membership is the access boundary, who owns channel hygiene and invite approval? — *answered by:* IT/security owner; trial in one pilot channel — *affects:* service-identity option
9. What would a permission-inheritance failure look like in our setting (the reported Kiro case: operator-level permissions, no second approver), and which controls (two-person rule, scoped tokens) are already in place? — *answered by:* security review of the tools the agent would touch — *affects:* all
10. Can we obtain audit trails that survive deletion of the originating prompt, and link code to the session that wrote it (Agent Trace, Assess ring)? — *answered by:* vendor trial; prototype of trace capture — *affects:* all shared options
- (Track 3) 11. When a harness calls a deployed agent, whose authority does the agent use downstream (the caller's via token exchange or enterprise-managed authorization, a service account, or the creator's)? — *answered by:* security architect plus a prototype against our IdP; read the MCP Enterprise-Managed Authorization extension — *affects:* all remote-invocation options (see [[remote-invocation-route]])
- (Track 3) 12. Do target orgs accept subscription OAuth tokens in CI, or require API keys/OIDC service accounts? Do cloud sessions and Managed Agents fit orgs that need Zero Data Retention, HIPAA BAA or customer-managed keys (documented as excluded)? — *answered by:* policy owners; vendor trial/contract review — *affects:* vendor cloud, Managed Agents, CI options
- (user-story-mapping) In a shared spec thread ([S05 journey B](../tasks/user-story-mapping/worked-derivation-s05.md)), what should a reviewer without access to some of the evidence see, and who decides? The agent's service identity can read more than any one reviewer. — *answered by:* security owner; interviews with risk reviewers — *affects:* service identity, agent-as-requester, per-run limits

### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 5 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24 | user-story-mapping pass on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Agent identity tagged by use case (unsolved) | Agents carry an identity saying what use case they serve, used for priority and load shedding in shared infrastructure | Stripe Kai | Protects core systems from agent load ("agents that went rogue") | Stripe says "we haven't solved this yet"; whose credentials Kai acts with is not disclosed | emerging | [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |

Key questions (Stripe pass):
7. Under whose identity do Kai's tool calls run (user OAuth, service account, project identity)? Not disclosed; matters for our audit design. — *answered by:* ask Stripe directly; compare Glass (user SSO) — *affects:* all identity options



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Broad-access agent behind a credentials proxy, directed from public channels (inferred) | The agent "has access to all the code, all the systems, all the tools... sandboxed and secure"; "River can see Slack messages... our data warehouse... our product management system" (Thawar); by contrast Shopify's assistant MCP tools go "through the same auth flow that you have" (BVP); Aquifer has a credentials proxy and gateway; anyone in a public channel can ask | Shopify River (details not disclosed) | Simple: no per-user OAuth; anyone can get help | Whoever can post can direct the agent's access (the Claude Tag risk); viewer and requester permissions not re-checked as far as disclosed | early-adopter (inferred; unverified) | [Knowledge Project](../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md) (first-party); [Beyond the Pilot](../research/sources/venturebeat-beyond-the-pilot-farhan-thawar.md) (first-party); [BVP](../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md) (first-party); [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [Tenable](../research/sources/tenable-claude-tag-slack-access-model.md) (independent, analogous) |

Key questions (River pass):
- Whose permissions does River use for warehouse and production-trace queries requested in a public thread, and does it restrict results by requester? — *answered by:* ask Shopify; not in any public source — *affects:* service identity vs on-behalf-of options

---

## governance-control-plane: Governance and control plane: policy, cost, audit
**Choice:** Where policy, spend limits and audit are enforced: per-harness settings; gateway or proxy; stateful session policies above harnesses; zero-ambient-access capabilities plus observation log; hosted multi-harness control plane with shared audit; deterministic gates in the harness (hooks); hard per-run limits outside the agent; per-project meter plus model router.
**Why it matters to the strategy:** Enterprise adoption depends on it, and it is the clearest value of a layer above individual harnesses.
**Related themes:** [[cost-control-routing]], [[risk-sloped-review]], [[evals-autonomy-trust]]   **Related dimensions:** [[harness-layering]], [[runtime-location]], [[agent-identity-delegation]], [[capability-distribution-trust]], [[review-and-autonomy]]
Formerly: governance-control-plane (identity rows and questions moved to [[agent-identity-delegation]]; plugin policy, registry-gate and eval-gate rows and key questions 4-6 to [[capability-distribution-trust]]; the "Autonomy slider + ground-truth evals" and "Logged human override" rows to [[review-and-autonomy]], per 01-synthesis.md D.0, D.5, D.8 and D.9)

### Original framing before the split — governance-control-plane: Permissions, cost, identity, audit
**Choice:** Where are policy, spend limits, identity and audit enforced: in each harness, in a gateway, or in a control plane above them?
**Why it matters to the strategy:** Enterprise adoption depends on it, and it is the clearest value of a layer above individual harnesses.
**Related themes:** [[cost-control-routing]], [[risk-sloped-review]], [[evals-autonomy-trust]]   **Related dimensions:** [[harness-layering]], [[runtime-location]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Per-harness settings | Each tool's own permissions | Claude Code settings | No new system | Inconsistent, hard to audit | mainstream | to be linked |
| Gateway / proxy | Central LLM and tool proxy | Ramp LLM proxy, AI Gateway | Cost and tool control | Doesn't govern the agent loop | early-adopter | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party) |
| Control plane above harnesses | Policy across agents | Omnigent policies, Cloudflare OS | Uniform governance | New layer to adopt | emerging | to be researched |
| Per-project cost meter + model router | Live cost per project, limits before crossing, router picks model per request; finance visibility | Ramp Glass + Ramp Router | Spend control at the point of use; 30% claimed saving | Savings claim self-reported, base unclear (press: 'certain accounts'); router quality unknown | early-adopter | [Glyman launch](../research/sources/x-eglyman-introducing-glass-learn-things-once.md) (vendor claim); [Glass video](../research/sources/ramp-introducing-glass.md) (vendor claim) |
| Hard per-run limits enforced outside the agent | Pre-call budget, iteration and wall-clock caps with a kill switch | Hypothetical (RiskKernel is a vendor example); Claude schedule caps are rate limits | Stops runaway loops (a reported $47K, eleven-day case) | The incident is second-hand and the author sells a tool; monitoring alone is called insufficient | emerging | [DEV post](../research/sources/devto-47k-agent-loop.md) (anecdote) |
| Stateful session policies above harnesses | Policies see every tool call and LLM event of any wrapped agent and keep per-session state (risk score, cost, confidential-read flag, original intent) | Omnigent contextual policies (server, per-agent, per-session; CEL on Databricks) | Rules like 'after a confidential read, no writes elsewhere'; soft/hard spend caps that force a cheaper model; intent-based blocking | Only covers agents launched through the layer; no effectiveness or false-positive data; custom Python policies unsupported on the Databricks-managed version | emerging | [Databricks](../research/sources/databricks-omnigent-contextual-policies.md) (vendor claim); [Atlan](../research/sources/atlan-omnigent-explainer.md) (vendor-biased) |
| Zero-ambient-access capabilities plus observation log | Agents start with no access; each resource granted as a typed binding via a per-service Gatekeeper that holds credentials, logs reads, queues side effects for approval with simulated results; later viewers are re-checked against what the agent observed | Cloudflare OS Gatekeepers | Sharing without leaking data the viewer could not see; credentials never in agent code; provisional writes | Requires building a Gatekeeper per service; early access; the design is Cloudflare-specific; HN raised sandbox-hardness doubts (workerd 'not a hardened sandbox') | emerging | [announcement](../research/sources/cloudflare-os-announcement.md) (vendor claim); [HN](../research/sources/hn-cloudflare-os-thread.md) (anecdote) |
| Hosted multi-harness control plane with shared audit | One cloud control plane applies access controls, audit logs and credit caps to Claude Code, Codex and the vendor agent; admins can disable a harness per workspace | Warp Oz | Admin-level harness allowlist; per-team billing | Vendor claim only; external inference bills outside the platform | emerging | [Warp Oz](../research/sources/warp-oz-multi-harness.md) (vendor claim) |

#### Added evidence and options (Track 6, research-agent-runtime-patterns-taxonomy, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Deterministic gates in the harness | Hooks or Stop hooks that block a turn until a check passes; read-only or manual-only flags for side-effect skills; classifier-based auto mode | Claude Code hooks, `disable-model-invocation`, auto mode | Enforcement without a new system; unlike CLAUDE.md, not advisory | Per-harness, not portable; gates only as good as the check | mainstream | [Claude Code best practices](../research/sources/anthropic-claude-code-best-practices.md) (first-party) |

See also: [[agent-identity-delegation]] for identity rows (creator, requester, service identity, co-author, environment-bounded, OAuth, vault, OIDC, A2A card signing) and for Track 3 key question 12 (subscription OAuth tokens in CI; ZDR, HIPAA and customer-managed-key fit).

### Key questions to choose
1. What are the governance requirements of target orgs (audit, data, spend)? — *answered by:* policy owners / customer interviews — *affects:* all
2. Ramp opened tools broadly (no token caps early) then added metering after a $1.5M week; what is our org's tolerance and sequencing? — *answered by:* policy owners / finance interviews — *affects:* meter/router vs caps
3. Is the 30% saving reproducible and what was it measured against? — *answered by:* ask Ramp; run a router pilot on own spend — *affects:* router option
11. Which of our governance needs are about what an agent has seen (observation-based, Cloudflare OS) versus what it does (action policies, Omnigent) versus how much it spends (gateway)? — *answered by:* policy owners; threat-model of the target workflow — *affects:* control-plane options
12. Do we accept governance that only holds for sessions launched through the layer? What happens when a user opens Claude Code directly? — *answered by:* security/policy owner — *affects:* Omnigent-style layer, Warp Oz
13. Has anyone shown contextual or capability policies reduce incidents in production? None of the sources give data. — *answered by:* more research; ask Databricks/Cloudflare for case evidence; red-team trial — *affects:* both control-plane options
- (Track 3) 13. Can cost and audit be attributed per caller across the hop (headless `total_cost_usd` is a client-side estimate; MCP `_meta` carries `traceparent`)? — *answered by:* prototype with tracing and billing reconciliation — *affects:* all remote options

- (Track 6) Which gates must be enforced outside the model (deterministic) for the jobs we pick, and which can be advisory? — *answered by:* policy owners; classify jobs by error cost and audit need — *affects:* per-harness settings vs control plane vs workflow engine

#### Audit additions (competitive-teardown-ramp-glass, 2026-10-24)
Correction to my row "Per-project cost meter + model router": the "30% claimed saving" is Ramp Router's launch claim from Jul 20, 2026 ("without any performance degradation", Diego Zaks), repeated by Glyman at the Glass launch; it is not a Glass measurement, no data was published, and one secondary outlet quotes 40% ([Router posts](../research/sources/x-ramp-router-launch-posts.md), vendor claim). The earlier "press: 'certain accounts'" qualifier came from a search summary and is unverified; disregard it.

### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 5 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24 | user-story-mapping pass on 2026-10-24 | audit pass: competitive-teardown-ramp-glass on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- The setting is regulated and audit is needed. Options that cannot provide audit and enforcement weigh less. The specific requirements (residency, retention, identity) remain key questions for the policy owner.

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Project as the unit of governance | A project owner (team or short-lived effort, 5-500 people) sets default model, blocks expensive models, tool policies (e.g. no writing sensitive data to company-wide docs), human-in-the-loop on sensitive tools, a separately secured back end, even a different harness; everyone in the project inherits it | Stripe Kai projects | Few experts make cost, safety and quality choices once for many; avoids prompt fatigue | Projects need owners; policy sprawl; enforcement details not public | early-adopter | [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Central LLM proxy with privacy-class checks (evidence row for Gateway / proxy) | All LLM calls via one authenticated proxy: noisy-neighbour limits, fallbacks, usage forecasting, check that models match the application's privacy class | Stripe LLM Proxy (on Bedrock) | One place for cost, model choice and privacy | Another platform; proxy outages are global | early-adopter | [AWS/Stripe compliance post](../research/sources/aws-stripe-compliance-agents.md) (first-party, vendor-hosted) |
| Full per-run agent logs for regulated work | Every agent action, decision and rationale logged and retrievable for each historical run | Stripe compliance agents | Meets examination standards | Storage, retention and privacy of logs | early-adopter | [AWS/Stripe compliance post](../research/sources/aws-stripe-compliance-agents.md) (first-party, vendor-hosted) |

Key questions (Stripe pass):
9. Who would own projects (policy) in our setting, and does project-scoped policy reduce approval prompts and unsafe workarounds vs per-user settings? — *answered by:* prototype project policies with two teams; count prompts and overrides — *affects:* per-harness settings, control plane, per-project meter



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Audit by public transcript plus a self-written session table | Every session is a public thread and a durable event log; the agent writes a `river_sessions` domain table; cost governance by a company usage dashboard where anyone sees their own AI spend (leaderboard removed) | Shopify River; Shopify usage dashboard | Audit and usage analytics come free; social accountability for spend | River cost not disclosed; no budget caps or per-project meters described; public transcript is not access control | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [Beyond the Pilot](../research/sources/venturebeat-beyond-the-pilot-farhan-thawar.md) (first-party) |

---

## durability-substrate: How persistence and recovery are implemented
**Choice:** What keeps a long-running or shared agent alive across crashes, restarts and idle periods: a platform session log, a framework checkpointer, a workflow engine, or a durable object?
**Why it matters to the strategy:** It decides who writes recovery and idempotency logic and where state lives (and so data residency).
**Related themes:** [[shared-persistent-sessions]], [[agent-frameworks]], [[memory-architecture]]   **Related dimensions:** [[runtime-location]], [[loop-source]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Platform session log | Vendor stores the session as an append-only event log; harness is disposable | Claude Managed Agents | No recovery code for you | Vendor-hosted; limited visibility | emerging | [Managed Agents post](../research/sources/anthropic-engineering-scaling-managed-agents.md) (first-party) |
| Framework checkpointer | Graph state saved per super-step/thread in your database | LangGraph (Postgres saver) | Uses your DB; thread resume and human-in-loop | Async mode may lose newest checkpoint on hard crash (independent test); checkpoints per node; growth needs pruning | mainstream | [LangGraph docs](../research/sources/langchain-langgraph-persistence.md) (first-party); [HackerNoon comparison](../research/sources/hackernoon-durable-execution-compared.md) (independent) |
| Workflow engine under the agent | Each agent call is a recorded step/activity with retry and replay | Temporal + OpenAI Agents SDK, Inngest, DBOS | Retries, versioning, per-tenant concurrency | Determinism rules (Temporal), cluster to run, model calls outside steps are re-paid, no automatic idempotency | early-adopter | [Temporal post](../research/sources/temporal-openai-agents-sdk-integration.md) (vendor claim); [HackerNoon comparison](../research/sources/hackernoon-durable-execution-compared.md) (independent) |
| Durable object agent | Stateful addressable agent with SQLite, alarms, fibers, hibernation | Cloudflare Agents SDK | Cheap idle, wakes on events | Recovery after eviction is yours; long jobs need Workflows | emerging | [Cloudflare docs](../research/sources/cloudflare-agents-long-running-agents.md) (first-party) |
| No durability, rerun from the repo | Treat sessions as disposable; state lives in git and tickets | Stripe Minions (capped retries), Claude cloud (history restored, background work not) | Simple | Lost in-flight work; reruns cost tokens | mainstream | [Stripe Minions](../research/sources/stripe-minions-part-2.md) (first-party); [Claude cloud docs](../research/sources/anthropic-claude-code-cloud-sessions.md) (first-party) |

### Key questions to choose
1. How long and how costly are our agent runs, and what is acceptable loss on a crash (rerun vs resume)? — *answered by:* run-length and token-cost inventory; fault-injection prototype (kill the harness mid-run) — *affects:* all
2. If we use a harness we do not control, can we get durability from the vendor, or do we need to wrap it? — *answered by:* Track 1 and 3 findings; vendor docs review — *affects:* platform log vs engine
3. Where may session state be stored (residency, vendor access)? — *answered by:* security/policy owner — *affects:* platform log, engine SaaS (Inngest sends step data to its platform)
4. Who will own idempotency for side effects (PRs opened, tickets created, emails)? — *answered by:* engineering owner; design review — *affects:* all but no-durability

#### Audit additions (competitive-teardown-ramp-glass, 2026-10-24)
Evidence row (first-party, [Building Laminar](../research/sources/ramp-builders-building-laminar.md)): Ramp chose "boring technology" — Postgres (sessions and messages), Temporal (durable orchestration of the loop, surviving deploys and ephemeral failures), S3 — on a disposable worker fleet, with "sandbox-as-a-tool" so sandbox lifetime is decoupled from session lifetime. Stated reason: the team already knows how to run and fix that stack at scale.

### Added by: research-agent-runtime-patterns-taxonomy (Track 5) on 2026-10-24 | audit pass: competitive-teardown-ramp-glass on 2026-10-24


River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Postgres event log + cattle session cells | Append-only session log in Postgres is the canonical truth; ephemeral per-session processes on any host; sandboxes warm or fresh | Shopify Aquifer | Crash and idle recovery without special workflow engines; "pick the end-to-end substrate, and refuse to compromise on cattle-not-pets" | Orchestrator unnamed; recovery of in-flight tool calls not described | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party) |

---

## model-provider-coupling: How tightly the agent is coupled to one model provider
**Choice:** Do we build on one provider's harness and models (best fit, vendor-bound), keep the model swappable behind our own abstraction, or run several providers' harnesses side by side?
**Why it matters to the strategy:** Reducing dependence on Claude Code is partly a model-access question: access terms, pricing and harness-model co-design differ by provider and have changed abruptly. (Proposed by Track 2; may merge with [[loop-source]].)
**Related themes:** [[build-vs-buy]], [[harness-over-model]], [[cost-control-routing]], [[harness-portability]]   **Related dimensions:** [[loop-source]], [[governance-control-plane]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Single-provider, native harness | Use the provider's harness and prompt-cache/thinking features directly | Claude Code + Claude; Codex + OpenAI models; Agent SDK (Claude only) | Best use of provider-specific features (caching, thinking tiers); lowest effort | Vendor access terms can change: subscription OAuth blocked outside official clients Jan 2026; Agent SDK may not offer claude.ai login to third parties | mainstream | [Agent SDK terms](../research/sources/anthropic-agent-sdk-overview.md) (first-party); [subscription block](../research/sources/venturebeat-anthropic-third-party-harness-crackdown.md) (independent) |
| Provider-agnostic abstraction we maintain | Own or library abstraction over several providers | Pi (pi-ai), OpenCode, Hermes, LiteLLM-based harnesses, Google ADK, Pydantic AI | Switch models, use cheaper or local models, avoid single-vendor risk | Abstractions leak (caching, thinking, tool schemas); needs a maintained per-provider conditioning layer; Ronacher: model differences are large; cost tracking best-effort | early-adopter | [eleven-system study (provider coupling)](../research/sources/arxiv-harness-engineering-eleven-systems.md) (independent); [Ronacher](../research/sources/lucumr-agent-design-is-still-hard.md) (anecdote); [Zechner](../research/sources/mariozechner-pi-minimal-coding-agent.md) (anecdote) |
| Multiple vendor harnesses behind one interface | Run several vendors' own harnesses and normalise the interface | Vercel AI SDK HarnessAgent (Claude Code, Codex, Pi); Omnigent (Track 1) | Keeps each vendor's best loop; avoids rewriting | Depends on each vendor's CLI/terms; behaviour differs per harness | emerging | [AI SDK agents](../research/sources/vercel-ai-sdk-agents-docs.md) (first-party); [eleven-system study (meta-harness)](../research/sources/arxiv-harness-engineering-eleven-systems.md) (independent) |

### Key questions to choose
1. Is model-provider independence a requirement for our users, or only harness independence? — *answered by:* user/customer interviews; procurement/policy owner at target orgs — *affects:* all
2. What are the current Anthropic and OpenAI terms for using subscriptions, SDKs and third-party products (resale, embedding, branding, login), and who at those vendors can confirm them? — *answered by:* terms review plus vendor account contact — *affects:* single-provider, multi-harness
3. How much quality and cost do we lose by routing the same jobs through a provider-agnostic abstraction versus the native harness? — *answered by:* same job run on native harness and on a portable loop with matching evals — *affects:* abstraction option

#### Audit additions (competitive-teardown-ramp-glass, 2026-10-24)
Evidence: Ramp made Laminar "model- and provider-agnostic from the start" because a single provider's managed-agents API "would lock us into their models", and routes every call through Ramp Router (its LLM gateway) to optimise cost, latency and performance ([first-party](../research/sources/ramp-builders-building-laminar.md)). Glyman's launch article sells "Any model. Open or closed." Independent data point on in-harness routing from LangChain's Open SWE experiment (−64% median cost per thread, no significant quality change across 973 threads) is in [The New Stack](../research/sources/thenewstack-ramp-laminar-agent-harness.md); Ramp was not part of it.

Key question (unranked):
- Ramp's provider-agnosticism rests on owning the harness and a router. If we stay in a vendor harness, how much provider choice do we actually get, and at what cost in features? — *answered by:* compare model options in Claude Code/Codex/Cowork vs an Agent-SDK app vs a gateway — *affects:* all

### Added by: research-agent-runtime-patterns-taxonomy (Track 2) on 2026-10-24 | audit pass: competitive-teardown-ramp-glass on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- Model independence is a benefit to weigh, not a goal (see loop-source).

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Provider-agnostic abstraction we maintain (evidence row) | Internal LLM proxy: one API across providers on Bedrock; model swap is a parameter; fallbacks | Stripe LLM Proxy; Kai projects choose default models | Swap models per job and cost | We maintain the abstraction | early-adopter | [AWS/Stripe compliance post](../research/sources/aws-stripe-compliance-agents.md) (first-party, vendor-hosted); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |


---

## harness-upkeep: Who maintains the harness over time, and at what cadence
**Choice:** Is harness upkeep borne by a vendor (buy), a community project (fork/adopt), or an internal team (build), and how is it re-tested when models change?
**Why it matters to the strategy:** It is the recurring cost behind any build option and a product/resource choice for the request, not an architecture detail. Sources show harness components going stale or being rebuilt on model releases. (Proposed by Track 2.)
**Related themes:** [[build-vs-buy]], [[harness-over-model]], [[evals-autonomy-trust]]   **Related dimensions:** [[loop-source]], [[pm-agent-evaluation]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Vendor maintains | Upkeep comes with the product or hosted service | Claude Code, Codex, Managed Agents | No team needed; harness tracks the model | Behaviour changes without notice; beta APIs; we cannot fix issues ourselves | mainstream / emerging (hosted) | [Managed Agents](../research/sources/anthropic-managed-agents-overview.md) (first-party); [assumptions go stale](../research/sources/anthropic-engineering-scaling-managed-agents.md) (first-party) |
| Internal team with model-release re-test | A named team owns the harness and re-evaluates scaffolding per model | Ramp Glass team; Stripe; Cognition (rebuilt Devin for Sonnet 4.5); Manus (framework rebuilt four times); LangChain harness tuning | Control and fast fixes | Ongoing headcount; evals are hard (Ronacher); changes can overfit benchmark tasks; Ramp-style engineering depth may not exist elsewhere | early-adopter | [Cognition](../research/sources/cognition-devin-sonnet-45-rebuild.md) (first-party); [Manus](../research/sources/manus-context-engineering-lessons.md) (first-party); [harness design](../research/sources/anthropic-harness-design-long-running-apps.md) (first-party); [LangChain](../research/sources/langchain-improving-deep-agents-harness-engineering.md) (vendor claim) |
| Community-maintained base | Adopt an open project and track upstream | OpenCode, Goose (Linux Foundation AAIF), Cline, Pi | Shared maintenance; no licence fee | Project may be archived, renamed or change direction; vendor access conflicts | early-adopter | [Goose](../research/sources/github-block-goose-repo.md) (first-party); [OpenCode](../research/sources/github-opencode-repo.md) (first-party); [AutoGen archived (framework analogue)](../research/sources/github-microsoft-autogen-archive-notice.md) (first-party) |

### Key questions to choose
1. What is the real recurring upkeep for an internal harness (people, eval infrastructure, per-model re-tests)? — *answered by:* interviews with Ramp/Stripe-like teams; a scoped staffing estimate — *affects:* internal team option
2. Which vendor-claimed upkeep savings (hosted harness) hold up, and what changes silently on the vendor side? — *answered by:* trial of Managed Agents or Agent SDK with a changelog and regression-test routine — *affects:* vendor-maintained
3. Do we have, or can we fund, an eval set for our jobs good enough to detect regressions after a model or harness update? — *answered by:* policy owner / PM team; link to [[pm-agent-evaluation]] — *affects:* all

#### Audit additions (competitive-teardown-ramp-glass, 2026-10-24)
Evidence: Ramp, after building Laminar, says "even though building in-house has never been cheaper, you still need good engineers to be on-call, keep the platform healthy, and figure out what product teams actually need" ([first-party](../research/sources/ramp-builders-building-laminar.md)); The New Stack notes Ramp published no operating-cost comparison or benchmarks ([independent](../research/sources/thenewstack-ramp-laminar-agent-harness.md)). Ramp also rebuilt its loop once already (vendor SDK in April → Laminar by October), which is a data point on cadence.

Key question (unranked):
- What is the realistic steady-state team for a harness like Laminar at our scale, and who pages when an agent session breaks at 2 a.m.? — *answered by:* ask Ramp; staffing estimate against our on-call model — *affects:* own harness options

### Added by: research-agent-runtime-patterns-taxonomy (Track 2) on 2026-10-24 | audit pass: competitive-teardown-ramp-glass on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Small platform team plus federated domain owners | Core team under 10 runs the platform; domain teams own skills and custom agents; telemetry and a planned reflection loop propose skill fixes to owners | Stripe Kai | Upkeep of domain content spread to those who know it | Platform team still owns model and framework upgrades; no model re-test data published | early-adopter | [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party); [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party) |


---

## context-and-memory: Context and memory
**Choice:** Three sub-choices. (a) Per-user memory: none, user-authored files, offline-built read-only profile, shared knowledge edited by users. (b) Where product context lives: scattered, shared plain-text repo near the code, systems of record queried by agents. (c) How org context reaches the agent: platform-native graph, connectors/MCP into a general harness, curated context repo, user-supplied.
**Why it matters to the strategy:** Agents are only as good as the context they can find; the three sub-choices are largely the same choice stated three ways, and together they decide portability across harnesses, which data we must integrate, and who governs it.
**Related themes:** [[memory-architecture]], [[compounding-context-repo]], [[org-context-grounding]], [[legible-org-for-agents]], [[org-learning-loop]]   **Related dimensions:** [[artifact-and-project-structure]], [[session-persistence-sharing]], [[loop-source]]
Formerly: memory-design, context-location, org-context-grounding-source (merged per 01-synthesis.md D.0)

### Sub-choice: memory-design — Memory design
**Choice:** How does an agent get durable context about the user and their work: none, user-authored files, an offline-built profile, or live retrieval?
**Why it matters to the strategy:** Memory is what makes company-wide agents feel useful on day one, and it creates privacy, staleness and sharing problems.
**Related themes:** [[memory-architecture]], [[compounding-context-repo]], [[org-learning-loop]]   **Related dimensions:** [[session-persistence-sharing]], [[runtime-location]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Offline-built profile, read-only in session | Built on first open from connections, refreshed every 24h by a pipeline over past sessions + Slack/Notion/Calendar; agent only reads at start | Ramp Glass | Inspectable files; predictable behaviour | Staleness up to a day; privacy of mined sessions; no data that it improves answers | early-adopter | [Buchan](../research/sources/x-shanebuchan-how-we-built-glass.md), [Goddijn](../research/sources/x-sebgoddijn-glass-article.md) (first-party) |
| Shared org knowledge edited by users | Employees correct what the agent knows (e.g. definition of UK customer) | Ramp Glass | Corrections reach everyone | Governance of edits; conflicting edits | early-adopter | [Glyman launch](../research/sources/x-eglyman-introducing-glass-learn-things-once.md) (vendor claim) |
| User-authored memory files | Users or teams write context files | Claude Code CLAUDE.md-style | Simple, transparent | Manual upkeep | mainstream | to be linked |

#### Key questions to choose
1. Does an automatically mined profile measurably improve results versus user-authored context? — *answered by:* A/B prototype — *affects:* all
2. What privacy rules apply to mining Slack/Notion/session history per user? — *answered by:* policy/security owners — *affects:* offline-built, shared
3. Who may edit shared knowledge, and how are conflicts resolved? — *answered by:* governance design, trial — *affects:* shared org knowledge

#### Audit additions (competitive-teardown-ramp-glass, 2026-10-24)
Caveat (audit): the offline-built, read-only memory-file design is from the April 2026 desktop architecture (Buchan, Goddijn). Ramp's October Laminar post does not re-describe memory; whether it still works as inspectable files in a cloud session store is unknown ([first-party](../research/sources/ramp-builders-building-laminar.md)).

#### Added by: competitive-teardown-ramp-glass on 2026-10-24 | audit pass: competitive-teardown-ramp-glass on 2026-10-24

### Sub-choice: context-location — Where product context lives for agents
**Choice:** Does the product context agents need (requirements, decisions, domain rules, research) stay scattered in docs and people's heads, live in a shared plain-text repo near the code, or live in systems of record that agents query?
**Why it matters to the strategy:** Agents are only as good as the context they can find. Where it lives decides portability across harnesses, governance (who promotes "evidence" to "fact"), and whether each feature makes the next one cheaper. This is distinct from [[context-and-memory]], which covers per-user memory; harness-mined memory is there.
**Related themes:** [[compounding-context-repo]], [[memory-architecture]], [[org-learning-loop]], [[legible-org-for-agents]]   **Related dimensions:** [[context-and-memory]], [[session-persistence-sharing]], [[loop-source]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Status quo: scattered | Private docs, drives, SMEs' heads, Slack | Most teams today | No change cost | Agents can't find context; it gets re-found per feature | mainstream | [Intent Factory §Current State](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party observation) |
| Shared plain-text context repo | Markdown in a repo near the code, held as "evidence, not yet fact", with a domain owner per topic; specs write their evidence back | Stripe rule files; AGENTS.md conventions | Works with any harness; versioned; compounds | Governance stalls (fear of publishing wrong context); upkeep | early-adopter | [Intent Factory Action 5](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party); [AGENTS.md](../research/sources/agentsmd-agents-md.md) (vendor claim); [Vercel evals](../research/sources/vercel-agents-md-outperforms-skills.md) (vendor claim: always-on context beat skills) |
| Systems of record queried by agents | Context stays in Notion/Confluence/Snowflake/Linear and agents query it through connectors | Glass connected to Snowflake, research and specs; Ramp Gadget over Notion and Linear | Uses existing systems; no new store | Quality depends on the source systems; retrieval misses | early-adopter | [Charles on Lenny](../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (vendor claim); [BuildBetter on Ramp](../research/sources/buildbetter-ramp-ai-product-factory.md) (vendor claim) |

#### Key questions to choose
1. Where does the context for a typical recent feature actually live today, and how long did it take to assemble? — *answered by:* a context audit of 2–3 shipped features — *affects:* all
2. Who would own each domain's context, and is there a promotion path from evidence to fact that risk and compliance accept? — *answered by:* domain leads; policy owners — *affects:* shared repo, systems of record
3. Will engineering allow product context in or near the code repo? — *answered by:* engineering leadership — *affects:* shared repo
4. Which questions do other teams keep asking us in Slack support channels? These are the first candidates to write down. — *answered by:* support-channel analysis — *affects:* shared repo, systems of record
5. Does always-on repo context outperform connector retrieval for our tasks? — *answered by:* a small eval on real tasks — *affects:* all

- (user-story-mapping) How do PMs who use Claude Code inconsistently actually store, name and find the artifacts of a piece of work today (spec drafts, synthesis outputs, prototypes, session history)? The story baseline ([S11](../tasks/user-story-mapping/stories-cross-cutting.md#s11-pick-up-where-i-or-someone-else-left-off-and-find-the-artifacts)) rests on Geoff's description plus an independent report of 30-day transcript deletion. — *answered by:* 6–8 short interviews or screen-share walkthroughs of real folders and sessions — *affects:* all; decides whether files-as-record or sessions-as-record is the larger need
- (user-story-mapping) Would a reviewer (engineer, designer, risk) review a spec in a PR against a context repo, or does that exclude people who do not use Git? ([S05 journey A](../tasks/user-story-mapping/worked-derivation-s05.md)) — *answered by:* ask 3–5 reviewers to walk through a real review; prototype of journey A with hidden Git — *affects:* shared plain-text context repo

#### Current lean and what would change it
Geoff's doc leans towards a harness-agnostic plain-text repo because it survives tool changes. That lean would weaken if connector retrieval proved reliably better in an eval, or if governance can't be solved for a repo.

#### Added by: research-product-agent-and-harness on 2026-10-24 | user-story-mapping pass on 2026-10-24

### Sub-choice: org-context-grounding-source — How organisation context reaches the agent
**Choice:** Does the agent get org context from a platform-native graph, connectors/MCP into a general harness, a curated plain-text context repo, or what the user pastes?
**Why it matters to the strategy:** Every success case depends on context; thin context gives generic PRDs and wrong answers. It determines which data we must integrate and who owns it.
**Related themes:** [[org-context-grounding]], [[compounding-context-repo]], [[harness-over-model]], [[legible-org-for-agents]]   **Related dimensions:** [[loop-source]], [[session-persistence-sharing]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Platform-native graph | Vendor's index of its own tools' data | Atlassian teamwork graph behind Rovo | Accurate within the vendor's tools; fast to adopt | Locks to one suite; blind to other data | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party) |
| Connectors / MCP into a general harness | Harness connects to warehouse, tickets, calls, code | Ramp Glass (Snowflake, calls, code); Cowork plugins | Cross-tool; harness-agnostic | Integration and permissions work; memory design | early-adopter | [Ramp launch video](../research/sources/ramp-introducing-glass.md) (first-party) |
| Curated plain-text context repo | Owned, reviewed files agents read and write back | Geoff's context-repo proposal | Portable, inspectable, compounds | Needs owners and discipline | emerging | [Intent Factory doc](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party, proposal) |
| User-supplied context | PM pastes or uploads inputs | ChatPRD-style tools | Zero integration | Generic output; PM labour | mainstream | [Fireside test](../research/sources/fireside-pm-tested-5-ai-tools-prd.md) (independent, weak) |

#### Key questions to choose
1. Which data sources do PM jobs actually need (calls, tickets, analytics, code, strategy docs), and where do they live today? — *answered by:* data inventory with PMs and IT — *affects:* all
2. Does the target org already run a platform graph (e.g. Atlassian) that makes native the cheapest path? — *answered by:* customer/stack discovery — *affects:* native vs connectors
3. Who owns context quality (domain owners)? — *answered by:* policy / org design — *affects:* context repo
#### Added by: research-pm-agents-jobs-to-be-done on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Identity and org context by default, personal sources opt-in per session (org-context-grounding) | Agent knows the user, org chart, date and the project-management system (OKRs, projects) by default; Drive, Slack and DMs connect only if the user allows, togglable per session or day | Stripe Kai | Good defaults without over-reach; user control over sensitive context | Less context for privacy-minded users; enforcement not described | early-adopter | [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Data-access path encoded as a skill (context-location) | A data-scientist-authored skill routes questions to existing reports first, then a blessed analytics layer, then the data catalog | Stripe Kai "ask data" on Hubble/Trino | Correct-by-default numbers on 5,000+ daily data sessions | Depends on years of catalog and semantic-layer work; warehouse must survive agent brute force | early-adopter | [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party); [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party) |
| Session-scoped virtual filesystem, no cross-session memory yet (memory-design) | State per session in an S3-backed VFS with summarization; no described long-term memory; sharing across sessions on the roadmap | Stripe Kai | Simple, private, inspectable files per session | Repeats context-gathering across sessions; compare Glass's offline memory pipeline | early-adopter | [LangChain case study](../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor claim); [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party) |

Key questions (Stripe pass):
11. Glass builds memory offline from connected accounts; Kai relies on org context, projects and skills with no long-term personal memory. Which matters more for PM work? — *answered by:* diary study of what PMs re-explain each session; prototype both — *affects:* memory-design options



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Monorepo as the intelligence layer | One repo holds code, skills, conventions, intent documents, runbooks, AGENTS.md and zone knowledge; sessions leave "a pebble, a skill update, an AGENTS.md diff" | Shopify World | Context compounds in reviewed files; agent and humans share one source | Needs a monorepo; non-code knowledge in a code repo may not suit non-engineers | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party) |
| Nightly "dreaming" over the day's sessions, per-person + per-channel memory | Off-hours job reviews conversations and skill use and rewrites text files, skills and instructions (no weights); injected at session start for the requester, plus channel memory | Shopify River | Agent improves without retraining; per-channel context | Tobi describes it inconsistently (per channel vs per person); no inspection or correction UX described | early-adopter | [Knowledge Project](../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md) (first-party) |
| Classifier mining of the public corpus | A fast cheap classifier ("Jev") tags every River mobile conversation by outcome; failures go to an LLM to propose skill and tooling fixes | Shopify Remote Dev team | Systematic improvement from real use | Depends on transcripts being available (public-by-default); method and results unquantified | emerging | [Remote Dev](../research/sources/shopify-engineering-remote-dev.md) (first-party) |

Key questions (River pass):
- If memory and skills are mined from shared sessions, how is sensitive content kept out of what gets injected into everyone's sessions? — *answered by:* prototype with a redaction step; security owner — *affects:* corpus-mining and shared-memory options

### Sub-choice: context-creation — How tacit business and operational knowledge is captured for agents
Proposed by competitive-teardown-stripe-knowledge-agents on 2026-10-24, to test Geoff's hypothesis that "there is a need for a business and operational context creation agent -- so much tacit knowledge needs to be captured from humans in order to be accessible to the agent ecosystem."
**Choice:** By what mechanism do we create the knowledge agents ground on that today lives only in people's heads (how the business works, which data to trust, design and architectural judgment, customer understanding): mine it from work exhaust, have owners curate and verify it, elicit it with an interviewing agent, or write it back from finished work? And is that a dedicated agent or a property of every agent?
**Why it matters to the strategy:** Every company that got agents working at scale (Stripe, Shopify, Ramp) did so on top of captured context. At Stripe that is Trailhead docs, a curated data catalog, Toolshed and 2,000 skills; at Shopify, AGENTS.md and skills; at Ramp, memory plus 6,500+ human edits. On Stripe's whiteboard chain, the human stages (opportunity, problem, goal: "customer conversations") are where most uncaptured knowledge sits. Whether capture needs its own funded agent changes the resource request.
**Related themes:** [[tacit-knowledge-capture]], [[opportunity-to-code-chain]], [[compounding-context-repo]], [[memory-architecture]], [[org-learning-loop]], [[legible-org-for-agents]], [[org-context-grounding]]   **Related dimensions:** [[sequencing]], [[intent-shaping-and-spec]], [[trust-privacy-defaults]], [[capability-distribution-trust]]

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Passive mining of work exhaust | A pipeline reads sessions, chat, docs, calendars and calls and rewrites memory, skills or a graph | Ramp Glass 24-hour memory pipeline; Shopify River corpus mined into skills; Glean / Atlassian Teamwork Graph | No extra work for people; scales | Noisy (Slack-mined knowledge needs high-precision filtering); inferring "who knows what" was off by ~21 points out of 100; works-council and privacy limits on mining employee communications; grounding gains mostly vendor claims | early-adopter (mainstream as search) | [Goddijn](../research/sources/x-sebgoddijn-glass-article.md) (first-party); [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [NeurIPS 2025 workshop](../research/sources/neurips-2025-resolution-extraction-slack-vs-tickets.md) (independent); [Watanabe](../research/sources/arxiv-watanabe-expertise-estimation-slack.md) (independent); [Microsoft works councils](../research/sources/microsoft-insidetrack-copilot-works-councils.md) (first-party) |
| Owner-curated, verified knowledge | Named owners write and periodically verify docs, canonical datasets, rules and skills; unverified content expires | Stripe Trailhead (verify or archive), Stripe data owners documenting canonical tables, Protodash design rules, Agent Studio domain owners; Glass shared-knowledge edits | Trustworthy enough for an agent to answer from (Stripe built its docs bot only after verification) | Authoring cost; contribution barriers; staleness unmeasured; needs a culture (Stripe's writing culture took a decade) | early-adopter | [Sessions 2024](../research/sources/stripe-sessions-2024-10x-engineer-panel.md) (first-party); [Sands](../research/sources/latentspace-emily-sands-stripe.md) (first-party); [Protodash](../research/sources/howiai-stripe-protodash-owen-williams.md) (first-party); [knowledge-activation skills](../research/sources/arxiv-yahoo-knowledge-activation-skills.md) (first-party) |
| Agent drafts, owner reviews | The agent proposes the doc, metadata or skill change from what it can see; an owner accepts or edits | Databricks AI table docs; Kai skill-creator plus planned skill-improvement proposals to owners; Stripe "docs written for AI consumption" | Cuts authoring cost while keeping a human accountable | Review fatigue; quality of drafts; owner must exist | early-adopter | [Databricks](../research/sources/databricks-ai-generated-table-documentation.md) (vendor claim); [Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [SDK post](../research/sources/stripe-ai-didnt-write-our-sdk.md) (first-party) |
| Interview-style elicitation agent | An agent interviews experts, PMs or customers and writes structured knowledge (decision rules, context, rationale) into the shared store | Stripe payment-method factory planning agent interviews the engineer and writes a shared knowledge base; Anthropic Interviewer (attitudes at scale); Geoff's shaping-skill "named source per question, answers written back" | Reaches knowledge nobody writes down; fits the upper chain (problem, goal) | LLM interviewers rarely probe (4.9% deepening turns); structuring loses data and hallucinates; no study measures fidelity of captured expertise | emerging | [payment-method factory](../research/sources/stripe-payment-method-factory.md) (first-party); [InterviewBot](../research/sources/arxiv-interviewbot-mllm-led-interviews.md) (independent); [Anthropic Interviewer](../research/sources/anthropic-interviewer-launch.md) (first-party); [knowledge elicitation](../research/sources/swj-knowledge-elicitation-automation-llms.md) (independent, weak) |
| Write-back from shipped work | Each finished task leaves learning: learning and decision logs, review comments and transcripts feed updates to prompts, skills, AGENTS.md or memory, ideally with citations checked on read | Stripe payment-method factory; River sessions leaving "a skill update, an AGENTS.md diff"; GitHub Copilot citation-verified memory | Context compounds with every task; verifiable where there is a source of truth | Weak without ground truth (business facts lack code-style citations); drift | early-adopter | [payment-method factory](../research/sources/stripe-payment-method-factory.md) (first-party); [Copilot memory](../research/sources/github-blog-agentic-memory-copilot.md) (first-party, A/B 83% to 90% merge rate); [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party) |
| No dedicated capture: rely on existing knowledge culture | Agents read whatever docs, catalogs and tools exist; no capture agent | Stripe before 2026 (writing culture, Trailhead, Compass); most orgs by default | Nothing to build | Works only where a writing culture already exists; elsewhere agents meet scattered private docs and SMEs (Intent Factory current-state gap) | mainstream | [Pragmatic Engineer, Stripe part 2](../research/sources/pragmaticengineer-inside-stripe-engineering-culture-part-2.md) (independent); [Nunez](../research/sources/firstround-nunez-internal-documentation.md) (independent); [Intent Factory](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party) |

**Key questions to choose**
1. Can an elicitation agent get experts past surface answers? Measure probe depth, and have a second expert check the fidelity of what was captured, compared with a human interviewer. — *answered by:* prototype, then trial — *affects:* interview-style elicitation
2. Without a code-style source of truth, how is business and operational knowledge verified and expired: owner sign-off, links to evidence, expiry dates? What is its staleness half-life? — *answered by:* prototype with instrumentation; Stripe's Trailhead verification rules if obtainable — *affects:* owner-curated, write-back, agent-drafts
3. Will experts contribute when they gain little themselves (+34% for novices, about 0 for experts in the call-centre study) and knowledge hiding is common? Which incentives or role expectations make them? — *answered by:* interviews, then a trial with a contribution metric — *affects:* owner-curated, elicitation
4. Which sources (Slack, email, meetings, calls) may legally be mined in the target orgs, and is a person-level "who knows what" map allowed? — *answered by:* policy owner (privacy, legal, works council) — *affects:* passive mining
5. Is capture a separate agent ("context creation agent") or a duty of every agent (write-back plus skill-creator), with one shared store? Stripe, Shopify and Ramp all chose the latter, with no dedicated capture agent found. — *answered by:* Geoff; a prototype of each on one job (e.g. intent shaping, S05) — *affects:* all
6. Is the marginal value in eliciting new knowledge at the top of the chain (opportunity, problem, goal) or in codifying and writing back knowledge for the lower chain (intent, plan, code)? — *answered by:* trial comparing the two on agent output quality — *affects:* elicitation vs agent-drafts and write-back

**Current lean and what would change it:** Evidence so far favours capture as a **by-product of work**: owner-verified curation plus agent drafts plus write-back from finished tasks, inside the agents people already use. A standalone interview agent is the least proven route. Every scaled example (Stripe, Shopify, Ramp) captures through use and owners, and the best interview-agent evidence shows shallow probing. The hypothesis holds for the **need** (strong evidence: all three companies built on captured context, and people stop writing knowledge down once they can ask an AI). It is unproven for the **form** (a dedicated agent). What would change the lean: a trial where an elicitation agent captures expert decision rules with high fidelity (checked by a second expert) and those rules measurably improve agent output on upper-chain work (problem, goal, intent).

**Department of Product pass (competitive-teardown-stripe-knowledge-agents, 2026-10-24):** new evidence for the options above, plus two options the first pass lacked.

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Owner-curated, verified knowledge (evidence row) | Named domain experts own "clusters": datasets with profiling, expert-vetted question-SQL pairs, business docs; a computed health score flags decay; every conversation is shown to owners | Spotify Vedder (2,100+ users, 177 clusters) | Trustworthy answers on 70,000+ datasets; the experts' role becomes "shaping the knowledge layer that answers thousands" | Curation effort; when Spotify tried to skip curators, they **rejected 87.5% of examples auto-generated from query history** | early-adopter | [Spotify](../research/sources/spotify-engineering-vedder-context-layer.md) (first-party) |
| Knowledge readiness as a release gate | A feature is "shipped" only when the agent can answer about it: PMs and engineers submit a "what we built" doc; walkthrough and GTM notes join it; an agent drafts and tests the content; a named owner signs off; results are monitored for 2-4 weeks | Intercom Fin NPI with the Operator agent | Context created *at the moment of shipping*, from the people who built it, with a test | A process role (NPI manager); depends on PMs writing the doc; no outcome numbers published | early-adopter | [Intercom](../research/sources/intercom-fin-npi-agent-readiness.md) (first-party, vendor) |
| Embedded human elicitation (pods) | Engineers shadow domain experts for days, document the workflow, then build the agent with them and validate it with others | Uber Agentic Pods (16 pods in 16 functions in two months) | Finds knowledge "rarely visible from the outside"; redesigns whole workflows | Scarce engineer time; captured knowledge lives in the agent built, not in a shared store | early-adopter | [Uber CTO](../research/sources/x-praveen-uber-agentic-pods.md) (first-party) |

Key questions (DoP pass):
7. Spotify's 87.5% rejection rate says mined examples are mostly noise. What share of mined context would our domain owners reject, and how much curation time does a cluster take? — *answered by:* a one-domain trial using our own query or document history — *affects:* passive mining, owner-curated
8. Could "knowledge readiness as a release gate" generalise from support to internal agents? Every shipped feature or decision would update what the internal agent knows, with a named owner. Who would own it in our setting? — *answered by:* Geoff / product ops; a pilot on two launches — *affects:* write-back, owner-curated

Update to the lean: the three new cases strengthen it. Each puts a **human owner or embedded human** at the point of capture: Spotify's curators, Intercom's NPI manager, Uber's pod engineers. Agents draft, test and monitor. None of the three uses a standalone capture agent.

---

## artifact-and-project-structure: How PM artifacts and projects are structured, stored and found
**Choice:** Do PM artifacts (specs, research syntheses, decisions, status updates, prototypes, dashboards) stay ad hoc and local, follow repo conventions, live as objects in a platform (Atlassian, Notion, Linear style), sit behind a thin product-defined project descriptor, or does a product meta-harness define typed artifact primitives and a project structure itself?
**Why it matters to the strategy:** Multi-party collaboration, reuse across sessions and harnesses, review, permissions and provenance all depend on a shared answer to "what is a project, what artifact types does it have, where do they live and who may see them". Today there is no cross-tool answer: "project" means different things even inside one vendor, and PM artifacts are mostly local files or scattered docs. This is the structural question behind [[context-and-memory]] (where context lives), [[context-and-memory]] (how context reaches the agent) and [[context-and-memory]] (per-user memory). Those three answer *where and how it is read*; this one answers *what the things are and how a project is defined*. Director: consider merging context-location and org-context-grounding-source into this dimension as its "location" half, or keep all four linked; I have kept them separate and cross-referenced.
**Related themes:** [[product-artifact-primitives]], [[artifact-standardization]], [[docs-as-code-prd]], [[pm-tool-connectivity]], [[project-taxonomy]], [[compounding-context-repo]], [[org-context-grounding]], [[memory-architecture]]   **Related dimensions:** [[context-and-memory]], [[intent-shaping-and-spec]], [[session-persistence-sharing]], [[governance-control-plane]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Ad hoc and local | Artifacts are files and chats on each person's machine plus whichever docs tool they like; no shared project definition | Inconsistent Claude Code use today (Geoff's baseline); local session history | No change cost; maximum flexibility | Findability and sharing depend on one person; local transcripts auto-deleted after 30 days by default; agents cannot answer "what exists for project X" | mainstream | [itdaily-claude-code-30-day-transcript-deletion](../research/sources/itdaily-claude-code-30-day-transcript-deletion.md) (independent); [geoff-building-accelerating-intent-factory](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party, Geoff); [hn-ask-claude-code-non-coding-workflows](../research/sources/hn-ask-claude-code-non-coding-workflows.md) (anecdote) |
| Repo-native conventions (docs-as-code) | PRDs, specs, decisions live as typed files in a repo with agreed folders and frontmatter | Spec Kit `specs/NNN-feature/`, Kiro `requirements/design/tasks`, ADR/MADR `docs/decisions/`, AGENTS.md, Gherkin | Versioning, review (PRs), permissions and history come free; works with any harness; agents read it natively | Spec-driven tools disagree on file sets; specs are developer-feature specs, not research/strategy; review burden high and agents may ignore specs; non-engineers may not use Git; no adoption data for PMs | early-adopter (engineering); emerging (PM) | [github-spec-kit-sdd](../research/sources/github-spec-kit-sdd.md), [kiro-specs-docs](../research/sources/kiro-specs-docs.md) (first-party); [fowler-bockeler-sdd-kiro-speckit-tessl](../research/sources/fowler-bockeler-sdd-kiro-speckit-tessl.md) (independent); [adr-madr-template](../research/sources/adr-madr-template.md) (first-party); [lenny-cursor-better-product-manager](../research/sources/lenny-cursor-better-product-manager.md) (anecdote) |
| Platform-owned objects | Artifacts and projects are objects in a work/knowledge platform, reached by agents through that platform's MCP and permissions | Atlassian (Jira work items in spaces, Confluence spaces, Home projects, Teamwork Graph), Notion databases, Linear initiative > project > issue + documents, Productboard product hierarchy with specs on features | Existing governance, permissions, UI and history; many PMs already live there; Ramp uses Notion and Linear as the formal record | "Project" differs per platform (Atlassian has three); no vendor graph has native spec/insight/decision types; long-form specs second-class in issue-centric tools; MCP coverage and plan gating uneven; cross-platform view missing | mainstream (platforms); early-adopter (agent access) | [atlassian-teamwork-graph-object-types](../research/sources/atlassian-teamwork-graph-object-types.md), [atlassian-jira-space-definition](../research/sources/atlassian-jira-space-definition.md), [atlassian-confluence-space-definition](../research/sources/atlassian-confluence-space-definition.md), [atlassian-rovo-mcp-server-supported-tools](../research/sources/atlassian-rovo-mcp-server-supported-tools.md), [notion-api-databases-data-sources](../research/sources/notion-api-databases-data-sources.md), [linear-initiatives-docs](../research/sources/linear-initiatives-docs.md), [productboard-product-hierarchy](../research/sources/productboard-product-hierarchy.md) (first-party) |
| Inferred enterprise context layer | A vendor graph indexes many tools and infers entities (projects, people, customers) rather than prescribing structure | Glean Enterprise Graph; Atlassian Teamwork Graph (partly inferred relationships) | No migration; cross-tool search for agents | Inferred, not authored: no owner/status/version semantics; vendor claims only; permission mirroring is only as good as connectors | early-adopter | [glean-enterprise-graph-product-page](../research/sources/glean-enterprise-graph-product-page.md) (vendor claim); [atlassian-teamwork-graph-glossary](../research/sources/atlassian-teamwork-graph-glossary.md) (first-party) |
| Thin project descriptor that points at things | A small manifest (name, owner, sources, instructions, artifact index) per project that points at objects in repos and platforms, not a competing store; exposed to agents as a resource | Cowork project (description, folders, instructions, links, scoped memory; local-only); Backstage `catalog-info.yaml` envelope; MCP resources (uri, mimeType, lastModified) | Gives agents a stable answer to "what is this project"; harness-agnostic if plain text; cheap to start | Needs a convention and an owner; no existing standard for typed PM artifacts; MCP resources are under-implemented; Cowork project not shareable | emerging (concept; components mature) | [anthropic-cowork-projects-docs](../research/sources/anthropic-cowork-projects-docs.md), [backstage-descriptor-format](../research/sources/backstage-descriptor-format.md), [mcp-spec-resources](../research/sources/mcp-spec-resources.md) (first-party); [anthropic-claude-projects-support](../research/sources/anthropic-claude-projects-support.md) (first-party: shareable project is files-only) |
| Meta-harness-defined artifact primitives and project structure | The harness defines typed artifact kinds (e.g. intent/spec, evidence, decision, risk, status update), a project schema, lifecycle states, provenance and permissions, and keeps or syncs them to repos and platforms | Spec Kit's constitution/spec/plan/tasks set (narrow); Geoff's implied primitives (intent, evidence, risk taxonomy, shaping skill); Backstage envelope + MADR-style frontmatter as nearest composition | A shared vocabulary for multi-party work; cross-harness consistency; lifecycle and provenance can be enforced; stories can reference types | Biggest build; risk of a competing system of record; migration and adoption cost; schema must survive model and tool change; nothing like it exists to test | emerging (concept) | [geoff-building-accelerating-intent-factory](../research/sources/geoff-building-accelerating-intent-factory.md), [geoff-intent-shaping-well-managed-environment](../research/sources/geoff-intent-shaping-well-managed-environment.md) (first-party, Geoff's concepts); [github-spec-kit-readme](../research/sources/github-spec-kit-readme.md) (first-party); [w3c-prov-overview](../research/sources/w3c-prov-overview.md) (first-party, provenance vocabulary) |
| Hybrid: repo canonical for long-form, platform for tracking, descriptor ties them | Specs, decisions and research notes as files; work items and roadmap in the platform; a descriptor links both | Productboard spec-to-coding-agent hand-off over MCP; Spec Kit plus Linear/Jira; Ramp (Notion/Linear as record, skills in Git) | Each system does what it is good at | Two sources of truth to keep in step; permissions and identity differ across systems | early-adopter | [productboard-mcp-server-spark](../research/sources/productboard-mcp-server-spark.md) (first-party); [x-sebgoddijn-glass-article](../research/sources/x-sebgoddijn-glass-article.md) (first-party, Ramp) |

#### Audit correction (user-story-mapping, 2026-10-24)
- Repo-native row: the Lenny/Cursor note is evidence of PMs drafting PRDs with a coding agent over the codebase and pushing them to Confluence/Notion, not of PRDs kept in git; the PRD-in-repo practice itself is Geoff's observation (`[G]`) with no published adoption figure. The row's "early-adopter (engineering); emerging (PM)" maturity stands on the spec-driven-development evidence only.
- Platform-owned row, Atlassian detail (Fable verification pass, verbatim re-reads): Rovo MCP `delete_jira` and `manage_jira` are off by default and destructive calls go through a separate confirmation path ([tools](../research/sources/atlassian-rovo-mcp-server-supported-tools.md)); the Teamwork Graph API is read-only, Forge-app-only and org-admin installed, so it is not a direct data path for an external harness ([scopes](../research/sources/atlassian-teamwork-graph-scopes.md), [limitations](../research/sources/atlassian-teamwork-graph-limitations.md)); Atlassian's guidance on where PRDs and decisions live is Confluence page templates (PRD, project poster, DACI) linked to Jira by embedded issue links ([PRD template](../research/sources/atlassian-confluence-prd-template.md), [DACI](../research/sources/atlassian-confluence-daci-decision-template.md)); Confluence spaces carry agent-readable "space instructions", a per-container context file ([tools](../research/sources/atlassian-rovo-mcp-server-supported-tools.md)). JPD idea access over MCP is claimed in a vendor blog but unconfirmed ([blog](../research/sources/atlassian-blog-mcp-enhancements-jpd.md)).
- Hybrid row: "Glass projects are per-project cost meters" is an inference from two sentences in the Glyman essay; what a Glass project contains is unestablished.
- Platform-owned row: Ramp's use of Notion and Linear as "the formal record" is confirmed verbatim in the Charles transcript at 11:43 ([transcript](../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.transcript.md)).

### Key questions to choose
1. How do PMs (not engineers) actually store and find artifacts today, per artifact type, and how long does finding the last version take? Evidence is Geoff's description and anecdotes. — *answered by:* 6–8 walkthrough interviews of real folders, sessions and tools; an artifact audit of 2–3 recent initiatives — *affects:* all
2. What share of PMs (and of the reviewing roles) can and will work in Git for long-form artifacts? No adoption figure was found. — *answered by:* survey or interviews; check with engineering leadership — *affects:* repo-native, hybrid
3. Which artifact types does a multi-party team actually need to share and review (spec, research synthesis, decision, status, prototype, dashboard), and which can be left platform-specific? — *answered by:* story inventory (S05, S13, S16, S17) scored with PMs, designers, engineers — *affects:* primitives, descriptor
4. Does a team already agree what a "project" is (initiative, epic, space, feature folder), or would the harness be imposing one? — *answered by:* ask 3–5 teams to list their current projects and boundaries; compare with Atlassian/Linear/Backstage models — *affects:* descriptor, meta-harness-defined
5. Can the main BI and research tools be reached by agents with user-level permissions without admin work (Amplitude, Dovetail, Notion yes; Snowflake needs an admin, Looker a self-run server), and what is the blocking tool in our target orgs? — *answered by:* connectivity inventory in a target org; security owner — *affects:* platform-owned, inferred layer, hybrid
6. Would a thin descriptor plus MCP resources give agents enough structure, or do agents need typed primitives with lifecycle and provenance to be reliable and reviewable? — *answered by:* prototype one project in both forms (see S05 journeys); small eval on retrieval and review tasks — *affects:* descriptor vs meta-harness-defined
7. What should provenance and versioning mean for PM artifacts (who or what produced it, from which sources, which version was ratified)? Git covers files; MCP resources carry only `lastModified`; platforms have their own history. — *answered by:* reviewers' and risk owners' requirements; prototype of an artifact record — *affects:* primitives, hybrid
8. Who would own the schema and keep it current (product ops, a domain owner per area, the harness vendor)? — *answered by:* product ops and domain leads; compare with ADR/Backstage governance — *affects:* all but ad hoc
9. If sharing happens by project, what permissions model applies when artifacts live in several systems with different ACLs (mirror the viewer's rights per source, or a project-level ACL)? — *answered by:* security/policy owner; test with two platforms — *affects:* descriptor, meta-harness-defined, inferred layer
10. Can a standard be adopted bottom-up through a skill or template people choose (as MADR and AGENTS.md spread) or does it need a platform behind it? — *answered by:* look at adoption paths of ADR, AGENTS.md, Spec Kit; pilot a template in one team — *affects:* repo-native, descriptor, meta-harness-defined

### Current lean (optional) and what would change it
No lean. Evidence is thin on PM-side practice (anecdote and vendor guides); the strongest independent evidence says spec-driven tooling is young and divergent. The thin-descriptor option is the cheapest to test and the meta-harness-defined option the largest bet; Q1, Q4 and Q6 decide between them.

### Added by: user-story-mapping on 2026-10-24 (research: [platforms](../tasks/user-story-mapping/research-artifacts-platforms.md), [standardization](../tasks/user-story-mapping/research-artifacts-standardization.md))

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Project as intent plus governance container | A project states what the user is trying to do (a strong intent signal) and carries its skills, tools, model and policies; open to join | Stripe Kai projects | Better routing and safer defaults per workflow | Another object to curate | early-adopter | [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Artifacts live beside the conversation and evolve in place | Reports, dashboards and docs created in the session and edited turn by turn; published prototypes at URLs with anchored comments | Stripe Kai; Stripe Harbor | Work product is the unit, not the chat | Artifacts locked in sessions until sharing ships (Kai) | early-adopter | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [Harbor post](../research/sources/stripe-harbor-ai-prototyping.md) (first-party) |



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Channel as project, thread as unit, outputs as links | No project object; channels hold team skills and memory; threads end in PRs, tickets, diagrams, prototypes, Quick sites, Live Preview links or generated videos | Shopify River + Quick (50,000+ internal sites, open to all employees, no owners) | Zero new containers; findable by Slack search | Non-code artifacts (specs, decks) have no stated home; Quick has no permissions or ownership | early-adopter | [Knowledge Project](../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md) (first-party); [Quick](../research/sources/shopify-engineering-quick.md) (first-party) |

---

## target-user: Which users and personas we serve first, including for shared agents
**Choice:** IC PM at a mid or large company; head of product or CPO; founder-PM or AI builder; technical or platform PM and product ops; adjacent roles; every employee including non-engineers (agent workspace); engineers running many agents in parallel; and, for a shared persistent agent, which users and jobs it serves first.
**Why it matters to the strategy:** Personas differ in which jobs they own, how much AI they already use and what they would pay for; the shared-agent options differ sharply by job (interactive co-working vs unattended jobs) and the evidence base is mostly engineering.
**Related themes:** [[pm-persona-role-expansion]], [[pm-ai-usage-surveys]], [[non-engineer-builders]], [[shared-persistent-sessions]]   **Related dimensions:** [[target-outcome]], [[sequencing]], [[work-structure]], [[adoption-model]]
Formerly: target-user, shared-agent-users-and-jobs (merged per 01-synthesis.md D.0; the shared-agent options are kept as examples)

### Sub-choice: target-user — Which users and personas we serve first
**Choice:** Do we build first for the IC PM, the group PM / head of product / CPO, the founder-PM or "AI builder", the technical or platform PM, product ops, or adjacent roles (designer, eng lead, PMM)?
**Why it matters to the strategy:** Personas differ in which jobs they own, how much AI they already use and what they would pay for; the choice shapes the PM jobs map used for everything else.
**Related themes:** [[pm-persona-role-expansion]], [[pm-ai-usage-surveys]], [[human-judgment-pm-jobs]]   **Related dimensions:** [[sequencing]], [[work-structure]], [[adoption-model]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| IC PM at a mid/large company | Day-to-day PM jobs: discovery, spec, comms, triage | Atlassian PMs (prototyping, evals, update agents); Lenny survey respondents | Largest pool; clear jobs; measured pain (user research is the biggest wanted-vs-current gap) | Keeps "steering" role, so judgment jobs stay human; org-context access needed | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party); [Lenny survey](../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md) (independent, self-selected) |
| Head of product / CPO | Consumes briefings, decisions, portfolio views | Meta VP's personal agents (decision punch list); CEO self-serving via Rovo | High leverage; sponsors the budget | Few users; needs trusted summaries | emerging | [Meta VP piece](../research/sources/lenny-newsletter-meta-chawla-pm-leader-agents.md) (first-party; by Nikhyl Singhal, cross-posted by Lenny's Newsletter, not sponsored content) |
| Founder-PM / AI builder | One person spans PM, design and build | Startups hiring builders; Gamma ~1 PM per 4 engineers | Fast adopters; fewer approval layers | Thin evidence (job posts, anecdotes); wants a builder tool more than a PM agent | emerging | [Gamma piece](../research/sources/atlassian-bottleneck-keeps-shifting-gamma.md) (vendor-adjacent, anecdote); [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party, counter-view for large companies) |
| Technical / platform PM and product ops | Internal-platform, tooling and process roles | Vendor and job-post descriptions | Natural early adopters of agents for ops work | Evidence mostly vendor blogs and job postings | emerging | [TechnicalPM](../research/sources/thetechnicalpm-platform-vs-core-vs-technical-pm.md) (practitioner); [Parallel](../research/sources/parallelhq-what-does-product-operations-do.md) (vendor blog) |
| Adjacent roles (designer, eng lead, PMM) | Hand-offs with PM: launch, design review | PMM launch coordination; designers prototyping | Covers cross-role jobs | Dilutes focus; ownership disputes (PM vs PMM) | emerging | [Product School](../research/sources/productschool-launch-checklist-product-marketers.md) (vendor) |
| Every employee including non-engineers (agent workspace) | Workspace designed for non-technical staff after developer-style tools failed them | Cloudflare OS; Ramp Glass | Broad reach; non-engineers become builders | Evidence is the vendors' own; PM-specific need not shown | emerging | [Rhea post](../research/sources/cloudflare-how-we-rethink-work-with-cloudflare-os.md) (first-party, self-reported) |
| Engineers running many agents in parallel | Developer users of Claude Code/Codex wanting parallel sessions, review and governance | Conductor, Claude Squad, Superset, Omnigent | Existing, technical early adopters | May not be our PM users; independent advice says individuals can skip a meta-harness | early-adopter | [CodePick guide](../research/sources/codepick-meta-harness-guide.md) (independent); [Franke](../research/sources/garrit-meta-harness-parallel-agents.md) (anecdote) |

#### Key questions to choose
1. Which persona feels the most pain and has budget and authority to adopt? — *answered by:* interviews with each persona; sponsor interviews — *affects:* all
2. Do the personas we would serve share a jobs map, or do we need one per persona? — *answered by:* card-sort of the PM jobs map with each persona — *affects:* agent-unit, pm-job-sequencing
3. Is the "AI builder" collapse real in the orgs we target, or do roles expand instead (Atlassian's view at 10,000+ people)? — *answered by:* target-org discovery — *affects:* founder-PM vs IC options
4. Is the buyer of a meta-harness the platform/engineering team (governance) while the user is a PM who just wants a workflow? If so, which do we target first? — *answered by:* sponsor and user interviews — *affects:* all harness-ownership options

- (Track 6) Do the first users mainly do open work (individual PMs ideating and planning) or standardise a team process (a lead or product-ops owner)? The fit of runtime patterns differs sharply between the two. — *answered by:* interviews with both kinds of user; check who owns the standard (PRD review, launch checklist) today — *affects:* general-harness vs task-agent options
- (user-story-mapping) The stories are performer-agnostic by design (the performer can be PM, analyst, designer or engineer). Do non-PM performers want the same variants, or does the performer's role change which variant fits? — *answered by:* interviews with analysts, designers and engineers who do PM jobs ([S01](../tasks/user-story-mapping/stories-jobs.md#s01-turn-a-batch-of-customer-conversations-into-what-we-learned), S04, S10) — *affects:* all

#### Added by: research-pm-agents-jobs-to-be-done on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | user-story-mapping pass on 2026-10-24

### Sub-choice: shared-agent-users-and-jobs — Which users and jobs a shared, persistent agent serves first
**Choice:** Do we aim shared/persistent sessions at engineers' code work, at non-engineers building things, at recurring scheduled digests and triage, or at team Q&A in chat, and for which roles?
**Why it matters to the strategy:** The infrastructure options differ sharply by the job (interactive co-working vs unattended jobs), and the evidence base is mostly engineering.
**Related themes:** [[non-engineer-builders]], [[shared-persistent-sessions]], [[one-job-per-agent]]   **Related dimensions:** [[work-structure]], [[adoption-model]], [[session-persistence-sharing]], [[target-user]], [[target-outcome]] (overlap: consider merging this into target-user)

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Engineers' background code tasks | Parallel PR-producing agents | Ramp Inspect, Stripe Minions, Copilot cloud agent | Strongest reported scale (Stripe >1,300 merged PRs/week; Inspect about half of Ramp's merged PRs) | Needs tests and dev infra; figures are self-reported and vary by source | early-adopter | [Stripe Minions](../research/sources/stripe-minions-part-2.md) (first-party); [Modal on Inspect](../research/sources/modal-ramp-inspect-background-agent.md) (vendor claim) |
| Non-engineers building via a shared agent | Product, design, legal, finance use a multiplayer agent with Slack/web/Chrome extension | Ramp Inspect | New builders | Review capacity and permissions; Ramp-specific | early-adopter | [Modal on Inspect](../research/sources/modal-ramp-inspect-background-agent.md) (vendor claim) |
| Scheduled digests and triage | Recurring cloud runs that read systems and post to Slack or open PRs | Claude scheduled tasks (backlog grooming, alert triage, docs drift) | Fits PM monitoring jobs | Personal ownership; success not visible from run status | early-adopter | [Claude scheduled tasks](../research/sources/anthropic-claude-code-scheduled-tasks.md) (first-party) |
| Team Q&A and requests in chat | A shared agent in Slack channels | Claude Tag, Codex in Slack, Cursor in Slack, Devin | Where teams already work | Channel as access boundary; identity choices | emerging | [Tenable](../research/sources/tenable-claude-tag-slack-access-model.md) (independent); [Codex Slack docs](../research/sources/openai-codex-cloud-slack.md) (first-party) |
| Mostly private, individual sessions | No shared agent; individual harnesses with team skills | Claude Code locally | Least risk | Corrections do not propagate (vendor argument, unverified) | mainstream | [Unblocked](../research/sources/unblocked-agent-doom-loop.md) (vendor claim) |

#### Key questions to choose
1. Which PM or team jobs (from the PM jobs map) are recurring and unattended versus interactive and shared? — *answered by:* score the jobs map with users — *affects:* scheduled vs multiplayer
2. Is there any independent outcome evidence (quality, time saved, incidents) for non-engineer use of shared agents? None found beyond Ramp's accounts. — *answered by:* more research; interviews with adopters — *affects:* non-engineer option
3. Who is the first user group worth a pilot, and what decision would a pilot inform? — *answered by:* Geoff / user interviews — *affects:* all
- See also: key question 4 (what value outcome we target, and how to measure it) moved to [[target-outcome]].

#### Added by: research-agent-runtime-patterns-taxonomy (Track 5) on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- Users are our own team plus a small number of beta users across the company. This is internal tooling, not a commercial product. Commercial-buyer options and questions are out of scope.

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Every employee including non-engineers (evidence row) | One company agent for all functions | Stripe Kai: 83% weekly; Marketing 95%, GTM 87%, higher than engineering; GTM was the pilot | Broad reach; GTM pulled hardest | Engineers less served; numbers self-reported | early-adopter | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [LangChain case study](../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor claim) |


---

## target-outcome: Which outcome or value we target
**Choice:** Do PM agents aim at PM time saved, faster delivery (throughput), better decisions and spec quality, lower risk, or product and business outcomes?
**Why it matters to the strategy:** It decides the pitch, the measurement ([[pm-agent-evaluation]]) and which jobs rank first. Surveys report time saved and yet only about 1 in 4 PMs have a strategy to show for it (Productside, vendor survey).
**Related themes:** [[outcome-measurement-gap]], [[pm-ai-usage-surveys]], [[intent-factory-before-discovery]]   **Related dimensions:** [[pm-agent-evaluation]], [[sequencing]], [[target-user]]
Also holds: key question 4 from shared-agent-users-and-jobs (now under [[target-user]]).

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| PM time saved | Remove note-taking, updates, drafting | 63% of PMs save 4+ h/week (Lenny survey); Atlassian "no manual updates" | Easy to demonstrate | Reclaimed time goes to reactive work (Atlassian survey); weak strategic value | mainstream | [Lenny survey](../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md) (independent); [Atlassian State of Product](../research/sources/atlassian-state-of-product-2026-webinar-event.md) (vendor survey) |
| Delivery speed / throughput | Idea-to-customer cycle time, features shipped | Atlassian: 6-8 weeks vs ~6 months, ~3x Jira throughput | Concrete and executive-friendly | Self-reported, no baselines; attribution unclear | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party) |
| Decision and spec quality | Better-grounded specs, fewer gaps, fewer rework loops | Torres-style quote checks; Meta VP paragraph+prototype in place of PRD | Aligns with the intent-first thesis | Nobody publishes measures; needs rubrics | emerging | [Torres](../research/sources/echai-torres-ai-interview-analysis.md) (independent); [Meta VP piece](../research/sources/lenny-newsletter-meta-chawla-pm-leader-agents.md) (first-party) |
| Product / business outcomes | Adoption, retention, revenue | None found | The real goal | Long lag; confounded | emerging | none found (unsourced) |

### Key questions to choose
1. What outcome would the resource sponsor fund against (hours, cycle time, quality, revenue)? — *answered by:* sponsor interviews — *affects:* all
2. Is reclaimed PM time actually redirected to higher-value work in target orgs, or absorbed by reactive work? — *answered by:* pilot with before/after time diary — *affects:* time-saved option
- (Track 6) Is the target outcome speed, consistency (same standard applied every time), reduced review effort, or org learning? Consistency and reduced noise are the measurable outcomes in the code-review cases (Cloudflare, CR-Bench); speed alone is contested (METR RCT, early-2025: AI-allowed tasks 19% slower while experts believed faster). — *answered by:* choose metric with Geoff; baseline trial — *affects:* task-agent vs general harness
- (moved from shared-agent-users-and-jobs, Track 5:)
4. What value outcome do we target (cycle time, review load, consistency, learning once), and how would we measure it, noting Wavect's point to measure accepted changes per review effort rather than PR count? — *answered by:* metrics design with policy owner — *affects:* all

### Added by: research-pm-agents-jobs-to-be-done on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- Geoff's target: free human time for discovering novel problems, experiments and insight. Shaping simple intent should become trivial and approach full autonomy while meeting organisational standards for quality and good management. Consistency, reduced review effort, org learning and speed are all wanted. New key question: how would we measure the shift of human time toward discovery? *answered by:* baseline time study plus pilot instrumentation.

---

## pm-agent-evaluation: How we would know a PM agent works
**Choice:** What counts as success: self-reported time saved, throughput (PRs deployed, features delivered), output quality against a human baseline, or product outcomes?
**Why it matters to the strategy:** Nobody has published outcome measures; Atlassian says it hasn't figured it out. A measurement approach is both a risk and a possible differentiator.
**Related themes:** [[outcome-measurement-gap]], [[vendor-claims-vs-independent-evidence]], [[evals-autonomy-trust]]   **Related dimensions:** [[review-and-autonomy]], [[sequencing]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Self-reported time saved | Survey users | Lenny survey (63% of PMs save 4+ h/week); vendor case claims | Cheap | Biased, says nothing on quality | mainstream | [Lenny survey](../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md) (independent, self-selected) |
| Delivery throughput | PRs deployed, features delivered, idea-to-customer time, usage | Atlassian's measures | Objective, available | Team vs org measurement, attribution unclear | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party) |
| Output quality vs human baseline | Blind-rated agent vs human artifacts, evals | Torres's quote/fact evals; Fireside five-tool test (weak) | Tests the real claim | Needs rubrics and raters; none published for PM jobs | emerging | [Torres](../research/sources/echai-torres-ai-interview-analysis.md) (independent) |
| Product outcomes | Adoption, retention, revenue effects | Not found for any PM agent | The true goal | Long lag, confounded | emerging | none found (unsourced) |
| Intent-factory KRs | Share of well-specified intent delivered end to end by agents before human intervention; intent-completeness rate against an agreed standard; time to remediate a defect or vulnerability (target: near-instant) | Geoff's Actions 1 and 3; Stripe's (~30% of merges by Minions) and Ramp's (75% of PRs by Inspect) reported shares | Measures the factory, not PM opinion; ties to a business goal | Attribution across shaping and build; needs an agreed completeness standard first | emerging | [Intent Factory Actions 1, 3](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party proposal; company shares are vendor claims, relayed) |
| Classification accuracy vs SME labels | For judgement jobs framed as classification (e.g. risk review), grade a sample of agent outputs against SME labels for false positives and negatives | Geoff's risk-agent concept | Objective, cheap to sample; each error points to a heuristic to fix | Only fits jobs with a known taxonomy; needs SME labelling time | emerging (concept) | [Intent Shaping in a Well-Managed Environment](../research/sources/geoff-intent-shaping-well-managed-environment.md) (first-party concept) |

### Key questions to choose
1. What would a sceptical exec accept as proof that a PM agent helped? — *answered by:* exec/sponsor interviews — *affects:* all
2. Can we get a before/after baseline for the first job in a pilot org? — *answered by:* pilot design with a policy owner — *affects:* throughput, quality
3. Which PM jobs can be framed as classification against a known taxonomy (risk review, feedback routing, spec-completeness checks), so that SME-labelled accuracy becomes the measure? — *answered by:* reviewing the PM jobs map with domain SMEs — *affects:* classification accuracy
- (user-story-mapping) Can each story's success criteria be measured as written (for example 'few gaps in first review', 'reliance matches measured accuracy')? Which need new instrumentation? — *answered by:* review the 15 stories' success criteria with whoever would run an evaluation — *affects:* all evaluation options

### Added by: research-pm-agents-jobs-to-be-done on 2026-10-24; intent-factory rows: research-product-agent-and-harness on 2026-10-24 | user-story-mapping pass on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Within-user on/off comparison | Compare the same people's outcomes in weeks they use the agent vs weeks they don't; power vs low users in a cohort | Stripe Kai sales metrics (+39% deals) | Cheap, uses existing CRM data | Selection bias and reverse causality; not a controlled test | emerging | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [AI Founders critique](../research/sources/aifounders-stripe-kai-dont-copy-sales-numbers.md) (independent) |
| Handling-time reduction plus helpfulness rating on a fixed workflow | Measure median handling time on a decomposed workflow and ask reviewers to rate each agent answer | Stripe compliance agents (-26%, >96% helpful) | Concrete, attributable to one workflow | Narrow; rating can be lenient | early-adopter | [AWS/Stripe compliance post](../research/sources/aws-stripe-compliance-agents.md) (first-party, vendor-hosted) |

Key questions (Stripe pass):
6. Can we run a randomised or staggered rollout instead of on/off comparisons, so outcome claims survive the critique Stripe's numbers face? — *answered by:* experiment design with a pilot team — *affects:* all evaluation options



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Outcome-reached per item, not motion | Measure whether each item reaches an evidence-supported outcome (fixed, rejected, escalated); "PR count and green-branch count measure motion, not remediation" | Shopify River security remediation | Guards against vanity metrics like thread counts | Defined for security; PM equivalent unclear | early-adopter | [vuln remediation](../research/sources/shopify-engineering-river-vulnerability-remediation.md) (first-party) |
| Usage and merge-share metrics | Threads, sessions, coauthored-PR share, merge rate | Shopify River (36%→77% merge rate; ~1 in 8 merged PRs; 121,804 threads/month) | Easy to collect from the agent's own tables | No definitions; volume not value (Dealroom) | early-adopter | [Tobi article](../research/sources/x-tobi-learning-on-the-shop-floor.md) (first-party); [Dealroom](../research/sources/dealroom-river-threads-121804.md) (independent) |

---

## sequencing: Which jobs first and which layer first
**Choice:** Job level: feedback triage and synthesis (J1, J10); status and "ask the org" (J8); spec/PRD draft and review (J4); prototyping (J3); metrics review (J9); strategy and prioritisation (J2, J5). Stage level: delivery factory first, shaping layer first, or discovery first.
**Why it matters to the strategy:** It decides what the resource request funds first and what evidence we can gather soonest; the two sub-choices ask the same "what first" question at different granularity.
**Related themes:** [[intent-factory-before-discovery]], [[agent-factory-sdlc]], [[human-judgment-pm-jobs]]   **Related dimensions:** [[work-structure]], [[activity-classification]], [[review-and-autonomy]], [[harness-upkeep]], [[adoption-model]]
Formerly: pm-job-sequencing, investment-sequencing (kept as two sub-choices and presented together, per 01-synthesis.md D.0)

### Sub-choice: pm-job-sequencing — Which PM jobs to automate first
**Choice:** Which PM jobs does the first agent(s) take on: feedback triage and synthesis, status and comms, spec/PRD drafting and review, prototyping, metrics review, or strategy and prioritization?
**Why it matters to the strategy:** It decides what the resource request funds first and what evidence we can gather soonest. Related to Geoff's thesis of accelerating intent shaping before discovery.
**Related themes:** [[feedback-triage-agents]], [[status-update-agents]], [[prd-agents]], [[human-judgment-pm-jobs]], [[intent-factory-before-discovery]]   **Related dimensions:** [[work-structure]], [[review-and-autonomy]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Feedback triage and research synthesis | Cluster and route feedback, calls, tickets | Atlassian Rovo categorized 900+ items; Ramp Glass feature-request capture (~20k/month); Notion routing agent; Enterpret, Unwrap, Dovetail | Most claims; bounded; reviewable | Invented or merged quotes, silent omissions; vendor-heavy evidence | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party); [Torres failures](../research/sources/echai-torres-ai-interview-analysis.md) (independent); [Enterpret](../research/sources/enterpret-canva-customer-story.md) (vendor claim) |
| Status, updates and "ask the org" | Draft weekly updates; answer launch/status questions from org context | Atlassian weekly-update agent and CEO's Rovo query; Meta VP decision punch list | Removes PM follow-up work; easy to check | Needs accurate org context; little outcome evidence | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party); [Meta VP piece](../research/sources/lenny-newsletter-meta-chawla-pm-leader-agents.md) (first-party; by Nikhyl Singhal, cross-posted by Lenny's Newsletter, not sponsored content) |
| Spec / PRD draft and review | First drafts, gap and edge-case review | ChatPRD, Cowork write-spec, Notion/Atlassian agents | PRDs are PMs' top AI use (21.5%) | Generic output when context thin; no quality comparison vs human PRDs | early-adopter | [Lenny survey](../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md) (independent, self-selected); [Fireside test](../research/sources/fireside-pm-tested-5-ai-tools-prd.md) (independent, weak) |
| Prototyping (spec becomes prototype) | PM or agent builds a working prototype as the spec | Atlassian Loom-to-coding-agent flow; Lovable/Figma Make/v0 | Fast tight iteration; strong PM anecdotes | Breaks as complexity grows; handoff to engineering | early-adopter | [Product Talk roundup](../research/sources/producttalk-ai-prototyping-lovable.md) (independent, candid); [Atlassian](../research/sources/atlassian-ai-turns-pms-into-builders.md) (first-party) |
| Metrics review | Metric Q&A, anomaly flags, adoption analytics | Amplitude, Mixpanel, Pendo agents | Cheap to pilot on existing data | Evidence is vendor launches; interpretation needs judgment | emerging | [Mixpanel](../research/sources/mixpanel-spark-agent-mcp.md) (vendor claim); [Amplitude](../research/sources/amplitude-ai-agents-launch.md) (vendor claim) |
| Strategy, opportunity selection, prioritization | Agent prepares, human decides | Cowork roadmap skill; scoring tools | Where leverage may be highest | Practitioners say judgment stays human; weakest evidence; surveys show strategy lagging | emerging | [SVPG](../research/sources/svpg-four-big-risks.md) (first-party opinion); [Productside survey](../research/sources/productside-state-of-ai-for-pms-2026.md) (vendor survey) |

#### Key questions to choose
1. Which jobs do the target PMs actually find most painful and most repetitive (frequency x pain x cost of error)? — *answered by:* PM interviews and a time diary; scoring the PM jobs map — *affects:* all options
2. Do we agree with the intent-first order (shape intent and delivery before AI discovery)? — *answered by:* Geoff / the strategy owner — *affects:* order of options
3. For the first job, what baseline would let us show improvement (review time, rework, cycle time)? — *answered by:* a trial with before/after measurement — *affects:* all
4. Which jobs have org data we can legally and technically reach (calls, tickets, analytics)? — *answered by:* data-access inventory with policy owners — *affects:* feedback, metrics, status

- (Track 6) Score each PM job step on the activity axes (predictability, verifiability, repeatability, error cost, audit need, context breadth) before choosing: jobs high on repeatability, audit and context are candidates for a constrained agent; jobs low on all are better left in the general harness. — *answered by:* scoring workshop with PMs and a policy owner — *affects:* order of options; see activity-classification
- (user-story-mapping) Do the cross-cutting needs (S11 continuity, S12 context, S13 hand-off, S15 trust) need to be met before the job stories pay off, or can job stories succeed on their own? The baseline pain Geoff describes suggests the former; no evidence tests it. — *answered by:* prototype one job story (S01 or S05) with and without the cross-cutting need met; PM interviews — *affects:* sequencing

#### Current lean (optional) and what would change it
Evidence so far leans toward bounded, reviewable jobs (feedback triage, status/updates, spec first draft + gap review) as first candidates, because they have the most first-party use and checkable output; it would change if user interviews show a different top pain, or if a trial shows review cost cancels the time saved.

#### Added by: research-pm-agents-jobs-to-be-done on 2026-10-24 | user-story-mapping pass on 2026-10-24

### Sub-choice: investment-sequencing — Where to invest first
**Choice:** Does the resource request fund the delivery factory first (agentic coding, verification, gates), the intent-shaping layer first, or AI discovery first?
**Why it matters to the strategy:** Geoff's thesis is that order matters. Discovery without a faster factory swells the backlog, and a factory without agent-ready intent idles. This choice shapes the resource request directly.
**Related themes:** [[intent-factory-before-discovery]], [[agent-factory-sdlc]], [[build-vs-buy]]   **Related dimensions:** [[intent-shaping-and-spec]], [[loop-source]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Delivery factory first | Sustained capacity for agentic delivery with KRs (one SDD approach, verification, gates) | Stripe Minions, Ramp Inspect | Throughput and quality; frees capacity | Starved by vague intent; engineering-led | early-adopter | [Intent Factory Actions 1–2](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party) |
| Shaping layer first | A shaping skill, spec standard and context repo before or alongside the factory | Ramp Glass as the define-stage agent | Agent-ready intent ready when the factory scales | Little visible delivery gain on its own | early-adopter | [Intent Factory Actions 3–5](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party); [Charles on Lenny](../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (vendor claim) |
| Discovery first | AI for feedback, insight and opportunity discovery | Productboard Spark, feedback-analysis tools | Visible PM value fast | Balloons the backlog if delivery doesn't scale (Geoff's argument) | early-adopter | [Productboard Spark](../research/sources/productboard-introducing-spark.md) (vendor claim) |

#### Key questions to choose
1. Where is our actual bottleneck today: shovel-ready intent, build, review, or release? — *answered by:* value-stream data (lead time by stage) — *affects:* all
2. Will engineering commit sustained capacity to factory work, rather than spending AI gains on new features? — *answered by:* engineering and product leadership — *affects:* delivery-first, shaping-first
3. Can shaping and factory investment run together, so that neither idles? — *answered by:* a joint pilot on one team — *affects:* delivery-first, shaping-first

#### Current lean and what would change it
Geoff's doc leans towards delivery-first, then shaping, then discovery. Bottleneck data showing build is not the constraint would change that lean.

#### Added by: research-product-agent-and-harness on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- Reference workload for the first bake-off is **intent shaping**: take high-level intent and shape it against the real constraints of a large enterprise into intent that deserves to ship and is ready to, with constraints identified and resolved, dependencies mapped, and ready to hand to an engineering team or coding agent. It replaces PRD review as the example job.


River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Substrate first, agent second | Make the org legible (monorepo, reproducible environments, written-down skills, fast CI) years before the agent; then ship one agent, then turn it into a platform of profiles | Shopify (2024 bets; River 2026; Aquifer under it) | "Agent-friendly ≈ human-friendly": the prep pays off for humans too | Two years and an order-of-magnitude CI scale-up before payoff; a monorepo migration is out of reach for most | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party) |

Stripe chain additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24): Stripe's whiteboard chain **Opportunity → Problem → Goal → Intent → Plan → (Code)** is a way to read the sequencing choice ([video](../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md), first-party). At Stripe, agents were built bottom-up: Minions (code, early 2026), then the review agent, then Orbit (plan, shown 2026-10-22). Kai, Harbor and Protodash support research and prototyping across the middle of the chain. Opportunity, problem and goal stay with people and customer conversations.

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Bottom-up along the chain (code → review → plan → intent) | Automate delivery first, then planning, and leave the upper stages to people | Stripe (Minions → Gru → Orbit) | Each step has a verifiable artifact (PR, plan) | Starves on vague intent if the upper stages aren't fed (Geoff's Intent Factory warning) | early-adopter | [video](../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md); [Intent Factory](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party) |
| Context layer first, under every stage | Capture business and operational context (docs, data catalog, skills) before or alongside the agents | Stripe Trailhead verification, data catalog and Toolshed years before Kai and Orbit | Every later agent grounds on it | Slow, cultural, hard to show ROI | early-adopter | [Sessions 2024](../research/sources/stripe-sessions-2024-10x-engineer-panel.md) (first-party) |

Key question (Stripe pass): 9. Which stage of the chain loses the most time or quality for our target PMs today: opportunity-to-goal (human, conversational) or intent-to-plan (Stripe automated it)? — *answered by:* a diary or time study across the six stages with 5-8 PMs — *affects:* delivery factory first, shaping layer first, discovery first

---

## work-structure: How structured the work is, what agent shape fits, and the unit of an agent
**Choice:** Which work stays in a flexible general harness and which moves to a task-specific agent or workflow; and what the unit is (persona, job, stage, chain).
**Why it matters to the strategy:** It is the basis for deciding what to standardise and what to leave unstructured, and the unit sets what we name, evaluate and sell.
**Related themes:** [[one-job-per-agent]], [[single-agent-many-skills]], [[human-judgment-pm-jobs]], [[pm-persona-role-expansion]]   **Related dimensions:** [[activity-classification]], [[capability-format-portability]], [[sequencing]], [[target-user]]
Formerly: work-structure, agent-unit (agent-unit merged in as "the naming unit", per 01-synthesis.md D.0)

### Sub-choice: work-structure — How structured the work is, and what agent shape fits
**Choice:** Which work stays in a flexible general harness, and which moves into a task-specific agent or workflow?
**Why it matters to the strategy:** It is the basis for deciding what to standardise and what to leave unstructured.
**Related themes:** [[one-job-per-agent]], [[single-agent-many-skills]], [[human-judgment-pm-jobs]]   **Related dimensions:** [[capability-format-portability]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| General harness for all work | One flexible agent | Claude Code, Glass ("one agent, many skills") | Flexibility, one surface | Inconsistent results on standard tasks | mainstream | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party) |
| Task-specific agent per job | One agent per defined job | PM-agent jobs map | Consistency, evals, governance | Many agents to maintain | early-adopter | PM agents brief (see tasks/research-pm-agents-jobs-to-be-done/) |
| Hybrid | General harness delegates structured jobs to task agents | Track 6 | Both | Handoff design | to be researched | to be researched |
| One agent, many skills | Single surface; skills carry task shape | Ramp (OmniChat, Glass) | Fewer agents to maintain | Standard jobs may be inconsistent | early-adopter | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party: teams built four versions of the same agent) |
| Chain of specialised agents across the SDLC | Insight, define (Glass), build (Inspect), review, test (Testo), coordinate (Gadget), autonomous small loops | Ramp 'software factory' | End-to-end bottleneck removal | Needs mature infra; numbers self-reported | emerging | [Charles on Lenny](../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party) |
| Role/function plugin packs | Vendor- or org-authored bundles of skills per business function, installed by role | Anthropic Cowork knowledge-work plugins (11, incl. Product Management: write-spec, roadmap, progress tracking); PayPal planned function/persona "Agent Plugins" (Sales, HR, IT, Developer) | Fast start for non-engineers; a unit that can be assigned and measured by role | No outcome data from either vendor; skills inside remain general-harness prompts, not enforced workflows; SkillsBench shows gains vary hugely by domain (Healthcare +51.9pp, Software Engineering +4.5pp) and 16 of 84 tasks got worse | emerging | [Cowork PM plugins](../research/sources/anthropic-cowork-plugins-product-management.md) (vendor claim); [PayPal](../research/sources/paypal-agent-skills-at-enterprise-scale.md) (first-party); [SkillsBench](../research/sources/arxiv-skillsbench.md) (independent) |
| Fire-and-forget autonomous delegation | A whole task handed to a cloud agent that returns a PR or report | Codex cloud, Claude Code on the web, Jules, Copilot cloud agent, Devin | Parallel throughput; works while the user is away | Only independent test (Answer.AI, Jan 2025, Devin): 3 of 20 succeeded, success unpredictable; merge rates differ by tool (Willison's PRarena snapshot) | early-adopter | [Answer.AI](../research/sources/answerai-thoughts-month-with-devin.md) (independent) (independent, dated); [Willison](../research/sources/simonwillison-async-coding-agents-tag.md) (independent) (independent) |
| Read-only bounded task agent exposed to many hosts | Short, non-interactive, read-only agent published by an admin and reached from whichever chat or coding host the user has | Glean agents as MCP tools | Consistent structured result across hosts | Vendor itself excludes write tools and human-in-the-loop steps and advises under ~30s runtime: suits review/analysis, not iterative drafting | early-adopter | [Glean](../research/sources/glean-agents-as-mcp-tools.md) (vendor) (vendor claim) |


##### Added evidence and options (research-pm-agents-jobs-to-be-done, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Task-specific agent per PM job (scoped, human in loop) | One agent per defined PM job, e.g. feedback triage, weekly status, PRD review | Atlassian PM-built weekly-update agent and Rovo feedback categorizer (900+ items); Microsoft multi-agent feedback system (specialist agents with own schema/guardrails); Vercel one-job agents (lead processing, abuse, data analyst) | Consistency, evals per job, clear review point | Many agents to maintain; evidence is talk anecdotes and vendor claims, no head-to-head vs a skill | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party, no baselines); [Microsoft](../research/sources/microsoft-feedback-noise-multi-agent.md) (vendor claim); [Vercel](../research/sources/vercel-sweet-spot-agentic-ai.md) (first-party, not PM) |
| Persona agent / "PM agent" (one agent doing the PM's whole job) | A role-shaped assistant bundling many PM jobs | Claude Cowork PM plugin (write-spec, roadmap, updates); ChatPRD; Meta VP's personal agents (review-doc drafting, decision punch list, analytics) | Easy to explain; one thing to adopt | Blurry scope, hard to evaluate; Meta write-up: a VP's personal system, "six months in, it's accurate" per nightly self-checks; one brief dropped source links | emerging | [Cowork PM plugin](../research/sources/anthropic-cowork-plugins-product-management.md) (vendor claim, no outcomes); [Meta VP piece](../research/sources/lenny-newsletter-meta-chawla-pm-leader-agents.md) (first-party; by Nikhyl Singhal, cross-posted by Lenny's Newsletter, not sponsored content); [Fireside PM five-tool test](../research/sources/fireside-pm-tested-5-ai-tools-prd.md) (independent, single author) |
| General harness plus skills for PM work (no dedicated agents) | PMs use Claude Code/Glass/Cursor with PM skills | Ramp Glass (feature-request capture skill, specs from connected data); Claude Code for PMs | Flexibility; no new surface | Inconsistent on standard tasks; PM-specific outcome evidence thin | early-adopter | [Ramp Glass post](../research/sources/x-eglyman-introducing-glass-learn-things-once.md) (first-party); [Cursor for PMs](../research/sources/lenny-cursor-better-product-manager.md) (anecdote) |

Evidence caveat: no source found compares a task agent with a skill in a general harness; the Atlassian chain (Jira agent in Slack triages, then hands to a coding agent) suggests hybrids are in use but is only described in a talk.
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Workflow engine with embedded agents | Deterministic steps and agent steps in one graph; the engine owns control flow, the model fills steps | LangGraph, Google ADK workflow agents, Microsoft Agent Framework workflows, CrewAI Flows, Pydantic Graph, Stripe Minions blueprints (deterministic nodes around a Goose loop) | Predictability, evals per step, checkpoint/resume, audit; Microsoft's guidance: if you can write a function, do that | Less flexible for exploratory work; a second control-flow language to maintain | mainstream (workflow apps); early-adopter for coding agents | [Building effective agents](../research/sources/anthropic-building-effective-agents.md) (first-party); [MS Agent Framework](../research/sources/microsoft-agent-framework-overview.md) (first-party); [Stripe Minions](../research/sources/stripe-minions-one-shot-coding-agents.md) (first-party); [LangGraph](../research/sources/langchain-docs-langgraph-overview.md) (first-party) |

##### Added evidence and options (Track 6, research-agent-runtime-patterns-taxonomy, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Structure added on demand inside the general harness | One harness; the user or team adds structure when the job needs it: vague prompts to explore, plan mode for uncertain work, skills for repeatable workflows, hooks and Stop hooks as deterministic gates, subagent review, `claude -p` for unattended fan-out | Claude Code (explore/plan/verify ladder; fix-issue skill with side effects manual-only) | No second system; the same surface spans exploration and routine work | Skills are advisory and run with the host's permissions; consistency on standard jobs unmeasured | mainstream | [Claude Code best practices](../research/sources/anthropic-claude-code-best-practices.md) (first-party); [Agent Skills](../research/sources/anthropic-engineering-equipping-agents-agent-skills.md) (first-party) |
| Coordinator plus narrow specialists for a standardised job | A fixed set of single-purpose reviewers, each told what to flag and what not to, merged by a coordinator that dedupes and grades severity; risk-tiered effort | Cloudflare AI code review (7 specialists, 131,246 runs in a month, avg $1.19) | Less noise than one big prompt; cost scales with risk; auditable override | Needs a platform team; code review is verifiable, PRD review is less so; a first-party account | early-adopter | [Cloudflare](../research/sources/cloudflare-ai-code-review-opencode.md) (first-party); [CR-Bench](../research/sources/arxiv-cr-bench.md) (independent, preliminary) |
| Deterministic wrapper around an agentic core | Required steps (lint, tests, CI cap, hydration) run as code; open-ended work runs as an agent loop; humans review the output | Stripe Minions | Guaranteed team-required steps with agent creativity | Wrapper must be built and maintained; coding-specific | early-adopter | [Stripe](../research/sources/stripe-minions-one-shot-coding-agents.md) (first-party) |
| Constrain by default, loosen with evidence | Short bounded loops with human checkpoints and human evaluation; scope grows as quality is shown | Deployed agents in the Berkeley/Stanford production study; 12-factor "small focused agents" | Reliability first; easy to test | May cap value on open-ended work; scope-growth rule is untested | early-adopter | [Measuring Agents in Production](../research/sources/arxiv-measuring-agents-in-production.md) (independent); [12-factor](../research/sources/humanlayer-12-factor-agents-small-focused-agents.md) (first-party) |
| Expect structure to decay: invest in context, checks and permissions, not model-compensating workflow | Prune scaffolding as models improve; keep verification, rubrics, audit | Claude Code team practice (second-hand) | Avoids sunk cost in workflows a new model makes redundant | Second-hand summary only; durable moat claims exist on the other side | emerging | [Traces summary](../research/sources/traces-boris-cherny-light-cone-summary.md) (anecdote, second-hand) |

Evidence note: still no controlled comparison of a task agent vs a skill in a general harness (key question 2 above). Track 6 report: [track-6-work-structure-fit](../tasks/research-agent-runtime-patterns-taxonomy/track-6-work-structure-fit.md).

#### Key questions to choose
1. Which jobs are standardisable enough to deserve a task agent (frequency, variance, cost of error)? — *answered by:* PM jobs map scored with users — *affects:* all
2. What evidence is there that task agents outperform a skill in a general harness? — *answered by:* Track 6 research, a bake-off prototype — *affects:* task-agent options
3. Ramp consolidated from many agents to one with skills; does that hold for regulated or high-error-cost PM jobs? — *answered by:* bake-off prototype on one standard job — *affects:* general harness vs task agent
4. Which job families gain most from curated skills? SkillsBench suggests larger gains in domains models handle poorly (healthcare, manufacturing) and small ones in software engineering: does that hold for product-management jobs? - *answered by:* run a PM-job benchmark with and without the Cowork PM plugin and a custom skill; more research - *affects:* function plugin packs, which jobs to automate first
5. For the PM jobs we would standardise, does a task-specific agent beat a skill in a general harness on output quality and review effort? — *answered by:* bake-off prototype on 1-2 jobs (feedback triage, PRD review) with a human-scored rubric — *affects:* task-agent vs general vs hybrid (added by research-pm-agents-jobs-to-be-done)
6. Does the PM (or the org) want to adopt "a PM agent" or a set of named job agents? — *answered by:* PM user interviews — *affects:* persona vs job options (see agent-unit)
7. Cognition reports multi-agent crews make conflicting implicit decisions while Anthropic reports gains from orchestrator-worker systems: for our jobs, is one context-sharing agent plus skills better than a crew? — *answered by:* bake-off on one structured job (single agent + skill vs orchestrator-worker) — *affects:* task-agent and hybrid options ([source](../research/sources/cognition-dont-build-multi-agents.md), first-party)
- (Track 3) 3. Which target jobs are read-only, non-interactive and short enough to ship as an agent behind MCP today (a PRD review that returns findings) versus interactive and write-heavy (drafting a PRD) that must stay in a harness or use Tasks/input_required? — *answered by:* classify the PM jobs map against Glean's constraints; prototype — *affects:* task agent behind MCP vs general harness

- (Track 6) Is the step, not the person or the tool, the unit we classify? A PRD job mixes an open step (framing), a standardised step (review against a team standard) and an accountable step (ratify). — *answered by:* walk three real PM jobs end to end with users and mark each step's class — *affects:* all options (see activity-classification)
- (Track 6) For a standard such as PRD review, is the standard a rubric of judgment criteria or a completeness checklist, and can SMEs label 20+ past PRDs against it? — *answered by:* policy/standard owner; SME labelling exercise; Cloudflare-style specialist-plus-exclusions prototype — *affects:* coordinator plus specialists, task-agent options
- (Track 6) Does a gate need to be enforced (hook, workflow node, deployed service) or is a skill plus logged human sign-off enough for the jobs we pick? — *answered by:* risk/compliance owner; compare a skill+hook prototype with a workflow prototype — *affects:* structure inside general harness vs workflow engine vs deployed agent
- (Track 6) How fast does structure decay: would the model-compensating parts of a task workflow be redundant in 6-12 months, leaving only checks, rubrics and permissions? — *answered by:* re-run the same job with the newest model with and without the scaffold; vendor roadmap review — *affects:* all task-specific options
- (Track 6) Is there any ideation or planning outcome we can measure (decision quality, options generated, time to a decision), or is "leave it unstructured" an untestable default? — *answered by:* user interviews; a small trial with a rubric scored by the decision owner — *affects:* general harness for open work
- (user-story-mapping) For which of the 18 stories would a PM prefer a task-specific agent over a skill in a general harness, and does the preference follow the story's shape (recurring and standardised versus exploratory)? The S05 journeys A and B are the first pair to compare. — *answered by:* run the S05 pair as clickable prototypes with 5–8 PMs; compare preference and trust — *affects:* general harness plus skills, task-specific agent, hybrid

#### Added by: director (seed), 2026-10-24; Glass pass: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24 | Track 2 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | user-story-mapping pass on 2026-10-24

### Sub-choice: agent-unit — Persona, job, or stage as the unit of an agent
**Choice:** Is the unit we standardise a persona (a "PM agent"), a job (e.g. feedback triage), a lifecycle stage (discovery, shaping, delivery), or a workflow chaining several?
**Why it matters to the strategy:** It sets what we name, evaluate and sell, and how the PM jobs map is turned into a product. Overlaps [[work-structure]] but concerns the unit's definition, not whether it is a skill or agent.
**Related themes:** [[one-job-per-agent]], [[pm-persona-role-expansion]], [[pm-job-stable-methods-change]]   **Related dimensions:** [[work-structure]], [[capability-format-portability]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Persona agent | "PM agent" bundling a role's jobs | Cowork PM plugin; Meta VP personal agents | Maps to how buyers think | Roles are expanding, so the persona keeps changing (Atlassian: "roles are expanding"); hard to evaluate | emerging | [Cowork](../research/sources/anthropic-cowork-plugins-product-management.md) (vendor claim); [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party) |
| Job agent | One agent per job | Atlassian weekly-update agent; Vercel one-job agents | Evaluable, composable | Many units | early-adopter | [Vercel](../research/sources/vercel-sweet-spot-agentic-ai.md) (first-party) |
| Stage agent | One agent per lifecycle stage | Ramp: Glass as the define-stage agent in a software factory | Fits an end-to-end pipeline | Large scope per agent | emerging | [Charles podcast](../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party) |
| Workflow chain | Agents hand off across jobs | Atlassian Loom -> work item -> coding agent; Jira agent -> coding agent | End-to-end flow | Handoff design, failure handling | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party) |

#### Key questions to choose
1. Do PMs in the target orgs think in personas, jobs or stages when they ask for help? — *answered by:* PM interviews, card sort of the jobs map — *affects:* all
2. Are personas stable enough to build on (founder-PM vs IC PM vs CPO differ)? — *answered by:* persona research with each type — *affects:* persona agent
#### Added by: research-pm-agents-jobs-to-be-done on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- Agreed as the first hypothesis to test: 'a task agent beats a skill in a general harness on a standardised job', on intent shaping. Geoff says 'we don't know' whether standards should be encoded as fixed workflows or as rubrics and evals, and the call should not be forced. Keep it as a bake-off variable and key question.

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Federation of specialised agents linked over MCP | Keep agents specialised (research, coding, browser prototyping) and expose each one's capabilities to the others | Stripe Kai + Harbor + Minions | Each agent tuned for its job; chained work without copy-paste | Cross-agent identity and context transfer | early-adopter | [Harbor post](../research/sources/stripe-harbor-ai-prototyping.md) (first-party) |
| Human-driven DAG with agent research per sub-question (evidence row for workflow engine with embedded agents) | Review tooling orchestrates a DAG of quality-tested sub-questions; agents pre-fetch research; humans answer each | Stripe compliance review | Bounded context, measured quality, audit | Needs workflow decomposition and per-question evals | early-adopter | [AWS/Stripe compliance post](../research/sources/aws-stripe-compliance-agents.md) (first-party, vendor-hosted) |
| Orchestration in code over hardened reusable prompts (evidence row for deterministic wrapper) | Plan of steps, one prompt and one PR per step, coordinated by code; an orchestrator LLM was dropped as slow and unreliable | Stripe payment-method factory | Predictable, reviewable steps | Prompt upkeep (solved with a learning loop) | early-adopter | [payment-method factory](../research/sources/stripe-payment-method-factory.md) (first-party) |

Key questions (Stripe pass):
7. Stripe says one agent architecture fits coding but knowledge work differs per task, yet chose one general agent plus skills and projects (not many agents) after 4,000 no-code agents sprawled. Where is our line between "skill in the general agent" and "specialised agent"? — *answered by:* sort the PM jobs map by tools, data and definition of done; prototype the two most different jobs — *affects:* one agent many skills, task-specific agents, federation


---

## activity-classification: How we classify user activity for agent fit
**Choice:** Do we classify work by a single structure axis (structured vs unstructured), by several task properties, or by what workers want to hand off?
**Why it matters to the strategy:** The classification is how we decide which jobs get a constrained agent or workflow and which stay in a flexible harness; the wrong axis misroutes work.
**Related themes:** [[work-structure-spectrum]], [[one-job-per-agent]], [[single-agent-many-skills]], [[human-judgment-pm-jobs]]   **Related dimensions:** [[work-structure]], [[sequencing]], [[review-and-autonomy]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Two classes: structured vs unstructured | Binary split by whether the path can be written down | Anthropic workflows vs agents | Simple; matches Geoff's framing | Hides the middle; most production systems are hybrids | mainstream | [Building effective agents](../research/sources/anthropic-building-effective-agents.md) (first-party); [LangChain](../research/sources/langchain-how-to-think-about-agent-frameworks.md) (vendor claim, "how agentic") |
| Multi-axis task properties | Score each job step on predictability, verifiability, repeatability, error cost, audit need, context breadth, collaboration | Google's requirement-driven decision table; Track 6 axes A1-A7 | Explains why review and policy work constrain while ideation does not | Axes are a synthesis, untested with users | emerging | [Google design patterns](../research/sources/google-cloud-choose-design-pattern-agentic-ai.md) (vendor claim); [Track 6 report](../tasks/research-agent-runtime-patterns-taxonomy/track-6-work-structure-fit.md) (judgment) |
| Worker-desired agency | Classify by how much human involvement the person wants (Human Agency Scale H1-H5) crossed with agent capability | Stanford WORKBank (844 tasks, 104 occupations) | Captures adoption and trust, not only feasibility | Self-reported; O*NET tasks, not PM jobs | emerging | [Future of Work with AI Agents](../research/sources/arxiv-future-of-work-with-ai-agents.md) (independent) |
| Usage-derived pattern | Classify by how people actually use the agent: directive/automation vs iterative/augmentation | Anthropic Economic Index | Grounded in logs | Reflects access route (API vs chat) as much as the job | emerging | [Economic Index Jan 2026](../research/sources/anthropic-economic-index-2026-01.md) (first-party) |

### Key questions to choose
1. Which axes actually predict where a general harness underperforms a constrained agent for PM jobs? — *answered by:* score 10-20 PM job steps on the axes, then test the extremes in a bake-off — *affects:* all options
2. Does the person's wish for control (agency) diverge from task structure for PM jobs (for example people wanting to keep prioritisation but hand off synthesis)? — *answered by:* a short WORKBank-style survey of target PMs — *affects:* worker-desired agency vs multi-axis
3. Is the classification stable across users and over model generations, or must it be re-run per team and per model release? — *answered by:* repeat the scoring with two teams and again after a model upgrade — *affects:* all options

### Added by: research-agent-runtime-patterns-taxonomy (Track 6) on 2026-10-24

#### Geoff's answers, 2026-10-24 (via research-agent-runtime-patterns-taxonomy)
- Agreed: classify by job step, not by user.

---

## review-and-autonomy: Review and autonomy
**Choice:** Where gates sit (human every time; automated verifiers plus spot check; isolation and blast-radius limits; risk-sloped autonomy; upstream risk classification at shaping time) and who sets autonomy (fixed by policy per task class; user-set slider; earned from measured accuracy; classifier-gated).
**Why it matters to the strategy:** Review is where agentic throughput meets regulatory accountability; the documented failures are review problems, and autonomy determines review effort and risk. Gates are "where", calibration is "who sets how much".
**Related themes:** [[risk-sloped-review]], [[human-review-gates]], [[risk-review-as-classification]], [[evals-autonomy-trust]], [[ai-synthesis-hallucination-risk]]   **Related dimensions:** [[governance-control-plane]], [[intent-shaping-and-spec]], [[activity-classification]], [[sequencing]]
Formerly: review-gating, review-gate-placement, autonomy-calibration, plus two review rows from governance-control-plane (merged per 01-synthesis.md D.0)

### Sub-choice: review-gating — How human review of agent output is gated
**Choice:** Does every agent change get human review, is review sloped to scored risk, or does risk review move upstream into intent shaping (classifying risk before anything is built)?
**Why it matters to the strategy:** Review is where agentic throughput meets regulatory accountability. The gating model sets how much automation is actually realised, and it is the hardest sell in a regulated organisation.
**Related themes:** [[risk-sloped-review]], [[risk-review-as-classification]], [[evals-autonomy-trust]]   **Related dimensions:** [[governance-control-plane]], [[intent-shaping-and-spec]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Human review on every change | A person reviews every agent PR; code owners review sensitive areas | Stripe Minions ("not moving money without human review") | Clear accountability; easy to defend to regulators | Review becomes the bottleneck as agent volume grows (Stripe: ~7,000 PRs/week reported) | mainstream | [Intent Factory §Vision 7](../research/sources/geoff-building-accelerating-intent-factory.md) (vendor claim, relayed in Geoff's doc) |
| Risk-scored routing with partial auto-approve | PRs scored for complexity or risk; low-risk ones auto-approved; PRs opened under the requester's identity so no one approves their own agent's work | Ramp Inspect and Review Buddy | Throughput; human attention goes where risk is | Needs a trusted scorer and audit trail; regulators may not accept it | early-adopter | [Intent Factory §Vision 7](../research/sources/geoff-building-accelerating-intent-factory.md) (vendor claim, relayed); [Charles on Lenny](../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (vendor claim: Review Buddy handles 93% of PRs) |
| Upstream risk classification at shaping time | A risk-advisor agent classifies the spec against a MECE risk taxonomy before build; mitigations become requirements; novel risks go to SMEs | Geoff's risk-agent concept | Catches risk while the plan can still change; consistent; measurable against SME labels | Needs a curated taxonomy and heuristics; untested in practice | emerging (concept) | [Intent Shaping in a Well-Managed Environment](../research/sources/geoff-intent-shaping-well-managed-environment.md) (first-party, Geoff's concept) |
| Logged human override on an approval-biased AI reviewer | AI findings block only for critical issues; a human can force approval, recorded in telemetry | Cloudflare "break glass" (0.6% of MRs) | Keeps AI from becoming a bottleneck; measurable disagreement | Bias to approval is a policy choice; first-party figures | early-adopter | [Cloudflare](../research/sources/cloudflare-ai-code-review-opencode.md) (first-party) |

#### Key questions to choose
1. What review evidence do our regulators and second-line risk functions actually require for agent-written changes, and would risk-scored auto-approval satisfy it? — *answered by:* risk, compliance and audit policy owners — *affects:* all
2. Does a documented risk taxonomy with applicability heuristics already exist, and is it complete enough to classify against? — *answered by:* operational-risk and compliance teams; a sample of past risk reviews — *affects:* upstream classification
3. How accurate is an agent at classifying risk compared with SME reviewers (false positives and negatives on past initiatives)? — *answered by:* a prototype risk agent run on labelled historical reviews — *affects:* upstream classification, risk-scored routing
4. What share of today's changes are low-risk enough to auto-approve, and what is human review costing in elapsed time? — *answered by:* SDLC and PR data analysis — *affects:* risk-scored routing

- (user-story-mapping) How long does a PM currently take to check agent output for each job story, relative to the time it saves ([S15](../tasks/user-story-mapping/stories-cross-cutting.md#s15-know-whether-i-can-trust-what-came-back))? — *answered by:* timed checks on 3–4 real outputs (S01, S05, S09) — *affects:* all gating options; frames the cost of 'human review on every change'

#### Current lean and what would change it
No lean yet. In regulated organisations, evidence so far points to every-change review as the floor (Stripe), with upstream classification as the lever that could shrink review effort. That would change if policy owners accept risk-scored auto-approval.

#### Added by: research-product-agent-and-harness on 2026-10-24 | user-story-mapping pass on 2026-10-24
Row moved from governance-control-plane: "Logged human override on an approval-biased AI reviewer" (Track 6). Its attribution is that section's Added by line, under [[governance-control-plane]].

### Sub-choice: review-gate-placement — Where review gates sit on PM-agent output
**Choice:** Is PM-agent output reviewed by a human every time, sloped by risk, checked by automated verifiers, or contained by isolation (sandbox, isolated repo)?
**Why it matters to the strategy:** The documented failures (invented quotes, silent omissions, generic output) are review problems; gate design sets trust, cost and speed.
**Related themes:** [[human-review-gates]], [[ai-synthesis-hallucination-risk]], [[risk-sloped-review]], [[evals-autonomy-trust]]   **Related dimensions:** [[governance-control-plane]], [[sequencing]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Human reviews every output | PM checks before use or send | Most PM practice; 85% of PMs validate AI output with own expertise (survey summary) | Simple, trusted | Review cost eats savings; reviewer fatigue | mainstream | [Product Focus survey](../research/sources/productfocus-industry-survey-2026.md) (vendor survey, search summary only) |
| Automated verifiers plus human spot check | Quote/fact checks, evals, source links required | Torres built quote and fact-check evals after invented details in AI interview summaries | Catches known failure modes cheaply | Needs building and maintaining evals | early-adopter | [Torres](../research/sources/echai-torres-ai-interview-analysis.md) (independent practitioner); [Product Talk glossary](../research/sources/producttalk-ai-hallucination-glossary.md) (independent) |
| Isolation / blast-radius limits | Agent may act only in a contained space | Atlassian gave a PM an isolated repo; kept PMs out of Jira production code | Lets non-experts act safely | Doesn't improve content quality | early-adopter | [Atlassian talk](../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) (first-party) |
| Risk-sloped autonomy | Review depth set by risk class | Ramp auto-approves low-complexity PRs (engineering, not PM) | Speed where safe | Classification must be right | early-adopter | see [[risk-sloped-review]] sources (first-party) |

#### Key questions to choose
1. For each candidate PM job, what is the cost of an error (wrong customer claim, wrong status, wrong spec) and who bears it? — *answered by:* PM and stakeholder interviews — *affects:* all
2. Can source-link / quote verification be automated for the first job, and at what false-negative rate? — *answered by:* prototype with a seeded-error test set — *affects:* verifiers
3. What review time per output do PMs consider acceptable before the agent is not worth it? — *answered by:* trial — *affects:* human-every-time vs sloped
#### Added by: research-pm-agents-jobs-to-be-done on 2026-10-24

### Sub-choice: autonomy-calibration — Who sets how much autonomy an agent gets, and how it changes
**Choice:** Is autonomy fixed per task class by policy, set by each user on a slider, earned over time from measured accuracy, or decided by a classifier?
**Why it matters to the strategy:** Autonomy determines review effort and risk. Evidence shows it drifts with user experience, so a static table by task class would be wrong for some users.
**Related themes:** [[evals-autonomy-trust]], [[human-review-gates]], [[risk-sloped-review]]   **Related dimensions:** [[governance-control-plane]], [[review-and-autonomy]], [[activity-classification]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Fixed by policy per task class | The org sets autonomy per job (for example suggest-only for policy checks) | Approval-biased review with critical blocking | Predictable; auditable | Ignores user skill; can create friction | mainstream | [Cloudflare](../research/sources/cloudflare-ai-code-review-opencode.md) (first-party) |
| User-set slider | Users choose how much to approve or review, per session | Claude Code permission modes; Karpathy's autonomy-slider framing | Fits different tasks and tolerances | Users may over- or under-trust; needs good visibility | mainstream | [Measuring agent autonomy](../research/sources/anthropic-measuring-agent-autonomy.md) (first-party); [Karpathy notes](../research/sources/latent-space-karpathy-software-3-notes.md) (anecdote, secondary) |
| Earned from measured accuracy | Start as suggestions, raise autonomy as labelled accuracy proves out | Ramp Policy Agent | Trust grounded in data | Needs labelling effort | early-adopter | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party) |
| Classifier-gated | A separate model reviews actions and blocks risky ones | Claude Code auto mode | Fewer prompts, still a check | Classifier errors; vendor-specific | emerging | [Claude Code best practices](../research/sources/anthropic-claude-code-best-practices.md) (first-party) |
| Autonomy slider + ground-truth evals | Suggestions first, user-set auto-approve thresholds, weekly labeling, evals from five examples | Ramp Policy Agent | Trust built over time | Needs labeling effort | early-adopter | [Ramp lessons](../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party) |

#### Key questions to choose
1. Do our target users' autonomy preferences change with experience as the Anthropic data suggests, and should the product track that? — *answered by:* usage telemetry from a pilot; interviews — *affects:* user-set slider vs fixed policy
2. For which jobs would a policy owner refuse user-set autonomy? — *answered by:* risk/compliance owners — *affects:* fixed policy vs slider
3. What labelled data exists to earn autonomy for a job such as PRD review? — *answered by:* SME labelling exercise — *affects:* earned autonomy

#### Added by: research-agent-runtime-patterns-taxonomy (Track 6) on 2026-10-24
Row moved from governance-control-plane: "Autonomy slider + ground-truth evals" (Ramp Policy Agent, Glass pass). Its attribution is that section's Added by line, under [[governance-control-plane]].

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Fixed by policy per task class (evidence row) | Project owner marks sensitive tools as needing human confirmation for that project only | Stripe Kai projects | Friction only where risk is | Owner judgment; not adaptive | early-adopter | [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Human reviews every output (evidence row, knowledge work) | Agent output is supplementary research; the human answers every sub-question | Stripe compliance agents | Accountability kept; 26% faster | Caps the gain | early-adopter | [AWS/Stripe compliance post](../research/sources/aws-stripe-compliance-agents.md) (first-party, vendor-hosted) |



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Agent drives the pipeline, hands off one small decision | Agent validates live state, repairs, and routes "the smallest question that an owner has to answer" with evidence; owners approve and merge; guarantees enforced in code, judgement in prompts | Shopify River security remediation | Owners stop shuttling state; trust kept by explicit stopping points | Prompts alone failed to enforce complete enumeration (observed) | early-adopter | [vuln remediation](../research/sources/shopify-engineering-river-vulnerability-remediation.md) (first-party) |

---

## intent-shaping-and-spec: Intent shaping mode and spec standard
**Choice:** Who shapes intent (PM-led bespoke; PM-led with a versioned shaping skill; agent-led interrogation and research; prototype-first; agent-originated) and what counts as agent-ready intent (narrative PRD; short evidence-tied spec with a completeness standard; prototype as spec; canonical spec plus risk mitigations; spec pushed straight to coding agents).
**Why it matters to the strategy:** Refinement is the stated bottleneck of the intent factory and the core job a "product agent" would take on; the spec standard is the contract between the product agent and the coding factory.
**Related themes:** [[agent-led-intent-shaping]], [[agent-ready-intent]], [[intent-factory-before-discovery]], [[prd-agents]]   **Related dimensions:** [[work-structure]], [[review-and-autonomy]], [[sequencing]], [[artifact-and-project-structure]]
Formerly: intent-shaping-mode, spec-standard (grouped as two sub-choices, per 01-synthesis.md D.19)

### Sub-choice: intent-shaping-mode — Who shapes intent, and how
**Choice:** Is rough intent turned into delivery-ready requirements ad hoc by a PM, by a PM following a standard question set, by an agent-led interrogation and research skill, or by building a prototype first?
**Why it matters to the strategy:** Refinement is the stated bottleneck of the intent factory. This is the core job a "product agent" would take on.
**Related themes:** [[agent-led-intent-shaping]], [[intent-factory-before-discovery]], [[agent-factory-sdlc]]   **Related dimensions:** [[intent-shaping-and-spec]], [[work-structure]], [[review-and-autonomy]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| PM-led, bespoke | Each PM shapes intent their own way, just in time | Most teams | Flexibility | Inconsistent; slow; refinement 1–2 sprints ahead at most | mainstream | [Intent Factory §Current State](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party observation) |
| PM-led with a versioned shaping skill | A standard question set, a named source per question, answers written back, revised on a cadence | Geoff's Action 4 | Consistency; compounds; a low-tech start | Needs upkeep and adoption; the PM still does most of the work | emerging | [Intent Factory Action 4](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party) |
| Agent-led interrogation and research | The agent runs parallel research (code, wiki, competitors, calls), asks set questions, and challenges requirements that lack evidence | Ramp's shaping skill in Glass; Stripe Kai for research | Speed; evidence-tied requirements | Depends on context access; risk of shallow answers | early-adopter | [Intent Factory §Vision 2–3](../research/sources/geoff-building-accelerating-intent-factory.md) (vendor claim, relayed); [Charles on Lenny](../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (vendor claim) |
| Prototype-first | The PM or designer builds a working prototype in place of a written spec | Stripe Harbor (12,000 prototypes reported) | Concrete, testable intent quickly | Hidden requirements (risk, edge cases) go unstated | early-adopter | [Intent Factory §Vision 4](../research/sources/geoff-building-accelerating-intent-factory.md) (vendor claim, relayed) |
| Agent-originated intent | An agent mines tickets, calls and surveys and proposes the work | Ramp (90 days of tickets in ~8 minutes) | Signal-driven backlog | Noise; needs human prioritisation | emerging | [Intent Factory §Vision 1](../research/sources/geoff-building-accelerating-intent-factory.md) (vendor claim, relayed) |

#### Key questions to choose
1. What are the universal questions every piece of intent must answer here (including risk questions), and where is the source for each answer? — *answered by:* a workshop with PMs plus a review of past specs — *affects:* shaping skill, agent-led
2. Which of those answers can an agent find with today's context access, and which stay with a person? — *answered by:* a prototype shaping skill run on 3–5 live initiatives — *affects:* agent-led
3. How far ahead of delivery is shovel-ready intent today, and does a shaping skill extend that? — *answered by:* backlog analysis before and after a pilot — *affects:* all
4. Is a prototype acceptable as the spec of record in a regulated setting? — *answered by:* risk and compliance policy owners — *affects:* prototype-first

#### Added by: research-product-agent-and-harness on 2026-10-24

### Sub-choice: spec-standard — What counts as agent-ready intent
**Choice:** What artifact hands intent to delivery agents: a narrative PRD or deck, a short evidence-tied spec held to a completeness standard with evals, a prototype, or a canonical spec that also carries risk mitigations?
**Why it matters to the strategy:** No delivery approach reaches its automation potential on vague intent. The standard is the contract between the product agent and the coding factory.
**Related themes:** [[agent-ready-intent]], [[prd-agents]]   **Related dimensions:** [[intent-shaping-and-spec]], [[review-and-autonomy]]

#### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Narrative PRD or deck (AI-drafted or not) | A high-level document; the PM answers questions during development | Most teams; ChatPRD-style drafting | Familiar; quick to draft | Not executable by agents; refinement deferred | mainstream | [Intent Factory §Current State](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party observation); [ChatPRD guide](../research/sources/aakashg-chatprd-guide.md) (vendor claim) |
| Short evidence-tied spec with a completeness standard | Numbered requirements, "what not how", evidence links; templates, examples, and evals that gate delivery | Ramp's seven-part spec; Geoff's Action 3 | Agent-executable; measurable as a KR | Upfront work to define and maintain the standard | early-adopter | [Intent Factory Action 3](../research/sources/geoff-building-accelerating-intent-factory.md) (first-party; Ramp example a vendor claim) |
| Prototype as spec | A working prototype is the handoff | Stripe Harbor; Ramp's "data + requirements + prototype" | Unambiguous behaviour | Non-functional and risk requirements implicit | early-adopter | [Intent Factory §Vision 4](../research/sources/geoff-building-accelerating-intent-factory.md) (vendor claim, relayed); [Charles on Lenny](../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (vendor claim) |
| Canonical spec plus risk mitigations | A spec that absorbs mitigations as requirements and is re-assessed for residual risk | Geoff's risk-agent concept | Risk traceable to requirements | Heavier artifact; concept only | emerging (concept) | [Intent Shaping in a Well-Managed Environment](../research/sources/geoff-intent-shaping-well-managed-environment.md) (first-party) |
| Spec pushed straight to coding agents | A PM tool writes the spec and hands it to coding agents via MCP | Productboard Spark | Closes the define-to-build gap inside a vendor tool | Vendor lock-in; launch claims only | emerging | [Productboard Spark](../research/sources/productboard-introducing-spark.md) (vendor claim) |

#### Key questions to choose
1. What did the specs behind our highest-automation deliveries have in common, and what did the failures lack? — *answered by:* a retrospective on agent-delivered work — *affects:* all
2. Can product and engineering agree on one completeness standard, and can an eval judge it reliably? — *answered by:* a joint working session, then an eval prototype — *affects:* evidence-tied spec, canonical spec
3. Which spec format does the chosen SDD or coding-agent approach expect? — *answered by:* engineering, and a review of the SDD tooling — *affects:* all

#### Added by: research-product-agent-and-harness on 2026-10-24

#### Stripe chain additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
A Stripe engineer's whiteboard (Not My Business video, ~12:24) frames product work as **Opportunity → Problem → Goal → Intent → Plan**. A brace over Problem and Goal is labelled, partly legibly, "Customer conv…". Code follows: the plan is handed to a minion. Orbit (Stripe's planning agent) owns Intent research and Plan, and minions own Code. Opportunity, Problem and Goal stay with people. This separates two things the options above treat as one: **intent shaping** (problem, goal, intent) and **planning** (intent to an agent-executable plan).

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Plan as the agent-ready artifact (intent in, reviewed plan out) | The person states intent; a planning agent researches the codebase and internal docs and drafts a step plan; teammates comment on it; one button hands it to a coding agent that may run for hours and pause to ask | Stripe Orbit + Minions | The review gate moves to the plan, before code; the intent can stay informal | Problem and goal quality is assumed, not checked; engineer-first, and PM use isn't stated | emerging (first shown 2026-10-22) | [Not My Business video](../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) (first-party, vendor-produced) |
| Agent-drafted spec reviewed as an issue, then delegated | The agent drafts a precise spec (contract, valid and invalid examples); the team reviews it before implementation | Stripe extensibility SDK (~20 lint rules) | Catches design issues before code review | Works for bounded work with clear correctness | early-adopter | [SDK post](../research/sources/stripe-ai-didnt-write-our-sdk.md) (first-party) |

Key questions (Stripe pass):
4. Is the gap we fund **above intent** (opportunity, problem, goal, which Stripe leaves to people and customer conversations) or **below it** (intent to plan, which Stripe has automated with Orbit)? Geoff's Intent Factory loop starts at "informal intent", so it covers the lower half. — *answered by:* Geoff, plus a time study of where PM hours and delays sit across the six stages — *affects:* agent-led interrogation, prototype-first, plan-as-artifact
5. Does a reviewed plan (Stripe) do the job of a completeness-standard spec (Ramp, Geoff's Action 3), or do they gate different risks? — *answered by:* compare defect and rework rates of plan-gated vs spec-gated agent work in a pilot — *affects:* short evidence-tied spec, plan as artifact

---

## adoption-model: Adoption and enablement model
**Choice:** How do users become effective: training, mandates and metrics, a champions network, or enablement built into the product?
**Why it matters to the strategy:** The best harness fails if people stay stuck; Ramp's account makes adoption design part of the product.
**Related themes:** [[enablement-by-product]], [[non-engineer-builders]], [[org-learning-loop]]   **Related dimensions:** [[capability-distribution-trust]], [[governance-control-plane]]

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Product-led enablement | Auto-configured on install, skills and nudges teach 'what good looks like' | Ramp Glass | Day-one results without training | Claim that product taught faster than training is anecdotal | early-adopter | [Goddijn](../research/sources/x-sebgoddijn-glass-article.md) (first-party) |
| Mandates, leaderboards, proficiency ladder | L0-L3 levels, usage leaderboards, AI in hiring screens, hackathon, no caps | Ramp culture | Rapid visible adoption | Vanity-metric risk; Ramp-specific culture of velocity | early-adopter | [Charles AI-pilled](../research/sources/x-geoffintech-ai-pilled-article.md) (first-party) |
| Training and workshops | Traditional enablement | most orgs | Familiar | Ramp reports it mattered less than day-one skills | mainstream | [Goddijn](../research/sources/x-sebgoddijn-glass-article.md) (first-party) |
| Decentralised authoring, central trust | Domain teams write skills in their own repos; a central registry reviews, versions and distributes; adoption comes from contributors becoming authors | PayPal skills registry ("Decentralize authoring. Centralize trust, governance, and distribution"); Ramp Dojo | Skills reflect domain expertise; org learns once; fits non-engineer contributors | Review bottleneck; no published reuse or quality data from either; depends on a platform team | emerging | [PayPal](../research/sources/paypal-agent-skills-at-enterprise-scale.md) (first-party); [Goddijn](../research/sources/x-sebgoddijn-glass-article.md) (first-party) |
| Intake alias, then skills, plus champions and interns | Staff send unwanted work to a small team that does it with AI; recurring patterns become skill files, connections and automated apps; champions and assigned interns drive uptake | Cloudflare OS rollout (thousands of weekly users, >4,000 apps in 30 days, self-reported) | Finds real jobs before building; reveals which to standardise | Manual, costly early phase (admitted); self-reported numbers with no measurement method; Cloudflare-specific talent | early-adopter | [Rhea post](../research/sources/cloudflare-how-we-rethink-work-with-cloudflare-os.md) (first-party, self-reported) |
| Admin-curated agent catalog surfaced in the host users already use | An admin selects which task agents appear as tools in the org's MCP server; users do nothing but connect their host | Glean MCP server (agents as tools), Sentry hosted MCP | No new surface to learn; central curation; consistent across hosts | Tool-count bloat degrades host tool selection; descriptions drive routing; no adoption data published | early-adopter | [Glean](../research/sources/glean-agents-as-mcp-tools.md) (vendor) (vendor claim) |

### Key questions to choose
1. Would our target users' orgs tolerate mandates/leaderboards, or does adoption have to be product-led? — *answered by:* user interviews — *affects:* all
2. How is 'adoption' defined and does it correlate with outcomes (Ramp reports 99.5% but no outcome data)? — *answered by:* ask Ramp; define own metrics — *affects:* all
3. Who should author and maintain standard skills for our users (a central product team, domain experts, or the users themselves), and what incentive or tooling makes them do it? - *answered by:* user interviews with domain experts; trial of a contribute-and-review flow - *affects:* decentralised authoring vs product-led enablement
4. Is an intake-alias discovery phase (watch real requests, then productise the patterns) a cheaper way to choose which jobs to standardise than designing a jobs map first? — *answered by:* small pilot with one team; compare with the PM jobs map — *affects:* intake-alias vs product-led enablement
- (Track 3) Do users call task agents from the harness they already use (Claude Desktop, Cursor, Claude Code, Codex) or from a new surface, and which hosts must we support? Protocol features (MCP Tasks, A2A clients, plugins) differ by host. — *answered by:* user interviews, usage data — *affects:* MCP-agent catalog vs own surface

### Added by: competitive-teardown-ramp-glass on 2026-10-24 | Track 4 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | Track 1 pass: research-agent-runtime-patterns-taxonomy on 2026-10-24 | research-agent-runtime-patterns-taxonomy (Track 3) on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
Baseline evidence: before Kai, 8,500 of ~10,000 Stripes used LLM tools daily (Oct 2025), via GoLLM presets and a LibreChat front end on Toolshed ([Latent Space, Sands](../research/sources/latentspace-emily-sands-stripe.md) (first-party)).

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| One front door, no knobs, pilot then company demo | Ship a v0 fast, pilot with the most eager function (GTM), then a company-wide demo; no setup ("available to every employee on Day 0"); remove configuration choices | Stripe Kai (296 to 5,000+ users in ~4 weeks; 83% weekly) | Fast ramp among people who had bounced off configurable tools | Self-reported; Stripe's AI-forward culture and infra may not transfer | early-adopter | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [LangChain case study](../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor claim); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Put the install prompt at the moment of intent | Distribution plays (install prompts at CLI login, docs buttons) beat better content | Stripe skill for external developers (30-35% copied the install command) | Cheap adoption lever | Measured for developers, not employees | early-adopter | [steering experiments](../research/sources/stripe-ai-steering-experiments.md) (first-party) |

Key questions (Stripe pass):
5. How much of Kai's ramp is the product vs Stripe's preconditions (an AI-forward culture, 8,500 daily LLM-tool users already in Oct 2025, a mature data catalog)? — *answered by:* compare adoption curves at a less AI-forward org; ask Stripe what the pre-Kai baseline was — *affects:* all adoption options



River/Aquifer additions (competitive-teardown-shopify-river, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Visibility as enablement, CEO in public | Agent works only in public; the CEO runs his own channel (#tobi_river, 100+ watchers); learning by watching, "no curriculum, no training plan, no manager"; AI use assessed in performance reviews | Shopify River | Fast diffusion (5,938 users in 30 days by May 2026, self-reported) | Needs leadership modelling and a culture of working in public; chilling effect (see [[trust-privacy-defaults]]) | early-adopter | [Tobi article](../research/sources/x-tobi-learning-on-the-shop-floor.md) (first-party); [BVP](../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md) (first-party) |
| Internal marketing with an agent persona | AI-generated ads with the agent as a character (Mac-vs-PC parody) to win back users who tried an early version | Shopify Remote Dev team (River share of merged mobile PRs 6%→61%) | Reverses "this is not for me" after a bad first try | Attribution mixed with infra improvements; self-reported | early-adopter | [Remote Dev](../research/sources/shopify-engineering-remote-dev.md) (first-party) |

Department of Product pass (competitive-teardown-stripe-knowledge-agents, 2026-10-24):

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Agentic pods: engineers embedded with a function | Two-week pods pair an AI-proficient engineer with a domain expert: shadow, prioritise, build with them, validate, ship | Uber (~30 engineers; 16 pods in 16 functions; e.g. city capital allocation 15 h → 30 min) | Agents fit real workflows; whole workflows redesigned; adoption built in | Engineer capacity; scales only with pods; outcomes self-reported | early-adopter | [Uber CTO](../research/sources/x-praveen-uber-agentic-pods.md) (first-party) |
| One domain, one surface first | Start with the most repeatable job and the tool its people already use, then widen | Stripe Kai (GTM pilot, per Stripe; "sales reps researching accounts", per DoP) | Fast proof, clear measure | Can stall as a point tool | early-adopter | [Department of Product](../research/sources/departmentofproduct-stripe-kai.md) (independent); [How I AI](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |

---

## agent-interface: Agent interface: own app, chat, or embedded
**Choice:** Where people meet the agent: our own app (desktop or web workspace), the chat tool they already live in (Slack, Teams), the IDE/CLI, embedded inside existing tools (docs, tracker, browser), or one agent service behind several of these.
**Why it matters to the strategy:** The surface decides who can use the agent on day one, what work is visible to others, what UI we must fund (artifact rendering, review panes, cost meters), and how much of the experience a chat vendor controls. River (Slack only) and Glass (own desktop app) are the two strongest opposite data points.
**Related themes:** [[agent-as-service-many-surfaces]], [[org-learning-loop]], [[shared-persistent-sessions]], [[remote-agent-invocation]], [[enablement-by-product]]   **Related dimensions:** [[trust-privacy-defaults]], [[session-persistence-sharing]], [[artifact-and-project-structure]], [[adoption-model]], [[remote-invocation-route]], [[runtime-location]]
Opened by competitive-teardown-shopify-river (Geoff's request), in parallel with competitive-teardown-stripe-knowledge-agents.

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Chat-native only (agent as a channel member) | The agent has no UI of its own; you @-mention it in a channel and it replies in thread; outputs are links (PRs, sites) | Shopify River (Slack, no DMs, "@river" top-level post then thread) | Zero install; joins human threads already in progress ("@river would be good to get your opinion"); visibility and search come free from the chat tool; 5,938 employees in 30 days by May 2026, 121,804 threads in Sep 2026 (self-reported) | Chat UI is poor for long artifacts, diffs, rich review, cost meters; rich outputs need a second surface (Shopify built Quick and Live Preview links); chat vendor owns UX, retention and API limits; visibility follows the chat tool's permission model | early-adopter | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [Tobi article](../research/sources/x-tobi-learning-on-the-shop-floor.md) (first-party); [Tobi replies](../research/sources/x-tobi-river-replies-may-2026.md) (first-party); [Tobi chart](../research/sources/x-tobi-river-floods-shopify-chart.md) (first-party) |
| Chat-native plus a companion web surface for rich output | Chat is the front door; links open a web page for what chat can't show (live app preview, hosted artifact) | River + Quick sites + Remote Dev Live Preview (simulator streamed to a shareable Quick page) | Keeps chat as the shared place while giving review a real UI | Two surfaces to maintain; still no place to browse or manage sessions outside chat | early-adopter | [Quick](../research/sources/shopify-engineering-quick.md) (first-party); [Remote Dev](../research/sources/shopify-engineering-remote-dev.md) (first-party) |
| Own app / workspace | A desktop or web app built for agent work: panes, inline rendering, skills marketplace, scheduling, cost meter | Ramp Glass (desktop app, SSO, split panes, Dojo); Claude Cowork; Cloudflare OS | Full control of UX for long and artifact-heavy work; can expose memory, cost and review; suits non-engineers' multi-step work | A new surface to adopt; work is private unless the app builds sharing (Glass added share-session); laptop-bound runtime in Glass's case | early-adopter | [Goddijn](../research/sources/x-sebgoddijn-glass-article.md) (first-party); [Buchan](../research/sources/x-shanebuchan-how-we-built-glass.md) (first-party); [Cloudflare OS](../research/sources/cloudflare-os-announcement.md) (vendor claim) |
| IDE / CLI | The agent lives in the developer's terminal or editor | Claude Code, Cursor, Codex CLI | Best for engineers' deep work; mature tooling | "Local agents have a ceiling": private, dies with the session, others don't learn (Shopify's stated reason for building River); excludes most non-engineers | mainstream | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party) |
| Embedded in existing tools / host-agnostic service | One agent service reached from many hosts: chat, web, browser extension, docs, tracker, or as tools in another harness via MCP | Ramp Inspect (Slack, web with hosted VS Code, Chrome extension); Glean agents as MCP tools; Open-Inspect (web, Slack, GitHub, Linear) | Meets each user where they are; one backend and session model | Capabilities differ per surface; harder to make work visible across surfaces; more integration upkeep | early-adopter | [Modal on Inspect](../research/sources/modal-ramp-inspect-background-agent.md) (vendor claim); [Glean](../research/sources/glean-agents-as-mcp-tools.md) (vendor claim); [Open-Inspect](../research/sources/github-open-inspect-background-agents.md) (first-party) |
| Public community chat as the primary interface (precedent outside agents) | Users must work in shared public channels to use the tool | Midjourney's Discord-first years | Users learn a new tacit skill by watching others' prompts | Consumer precedent; opinion, not data | n/a (precedent) | [Simon Willison](../research/sources/simonwillison-learning-on-the-shop-floor.md) (independent) |
| Vendor chat-agent offering | The model vendor's or chat vendor's own agent in Slack/Teams | Claude Tag in Slack; Codex Slack integration; Devin in Slack | No build; chat-native from day one | The vendor's identity and visibility model applies (channel members can direct the agent within its bundle; approval responses readable in channel) | early-adopter | [Tenable on Claude Tag](../research/sources/tenable-claude-tag-slack-access-model.md) (independent); [Codex Slack docs](../research/sources/openai-codex-cloud-slack.md) (first-party); [Answer.AI on Devin](../research/sources/answerai-month-with-devin.md) (independent) |

### Key questions to choose
1. Where do our target users already ask colleagues for help and discuss work (Slack, Teams, doc comments, tracker), and is that tool a system of record or just a chat pipe? — *answered by:* user interviews; chat-tool usage data from IT — *affects:* chat-native vs own app
2. Which of the first jobs produce artifacts that chat can't show well (specs, prototypes, decks, dashboards, diffs), and would a companion link surface be enough? — *answered by:* jobs map plus a two-version prototype (thread only vs thread + web page) on two real jobs — *affects:* chat-native only vs chat + companion vs own app
3. Does the org's chat tool allow a bot of this kind: API rate limits, retention settings, eDiscovery, admin approval for apps, Enterprise Grid features? — *answered by:* IT / chat-platform owner — *affects:* chat-native options, vendor chat-agent
4. Is Shopify's adoption (5,938 users in 30 days) due to the Slack surface, the monorepo substrate, or a CEO-led culture? Can we separate them? — *answered by:* ask Shopify builders if reachable; compare with Ramp's own-app adoption curve; more research — *affects:* all
5. Do non-engineers (PMs, designers, support) get as much from a chat-only agent as engineers do? Shopify says PMs and designers use River via Remote Dev but gives no split by role. — *answered by:* ask Shopify; pilot with mixed roles — *affects:* chat-native vs own app
6. If we choose a chat surface, which one: is the target org on Slack or Teams, and does it differ across target orgs? — *answered by:* Geoff / target-org inventory — *affects:* chat-native, vendor offering

### Current lean and what would change it
No lean. Evidence so far: chat-native wins on reach and on making work visible by default (River); an own app wins on rich, artifact-heavy, multi-step work for non-engineers (Glass); and both large adopters ended up with more than one surface (River + Quick/Live Preview; Inspect's Slack + web + extension). A finding that our first jobs are artifact-heavy would push toward an own app or chat + companion; a finding that most value comes from pulling the agent into existing human threads would push toward chat-native.

### Added by: competitive-teardown-shopify-river on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| One agent service, web app default plus chat, browser extension and API embedding (Stripe detail) | "The agent is a service, not an application, and surfaces are simply customized views into it": an opinionated web app most people use (no setup, day 0), a Slack integration, Chrome extensions inside third-party web tools, and internal apps embedding the agent via API (e.g. Finance's budget-modelling app) | Stripe Kai | Meets people in each tool without a product per surface; one agent and governance model behind all | Building the API, extension and embeds; rich artifacts still need the web app | early-adopter | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Chat reaction as the front door for unattended task agents (evidence row for chat-native) | Any Slack message becomes a task by emoji reaction; results reported in thread; runs on a phone | Stripe Minions | Lowest activation energy; the whole company is already in Slack | Only for one-shot tasks with strong CI | early-adopter | [How I AI, Kaliski](../research/sources/howiai-stripe-minions-kaliski.md) (first-party) |
| Specialist agents with their own app, exposed to other agents over MCP | A specialist keeps its own UI (browser tab with prototype and chat) but publishes tools so a general agent can drive it | Stripe Harbor (driven by Kai and coding agents) | Rich, job-specific UI where it matters, no forced app-switch elsewhere | Several apps to learn | early-adopter | [Harbor post](../research/sources/stripe-harbor-ai-prototyping.md) (first-party) |

Key questions (Stripe pass):
7. Stripe rejected both a standalone app ("would force users out of their natural workflows") and a product per surface ("hard to maintain"), yet most use is still its web app. What share of use would land in embedded surfaces for our users, and is the embed work worth funding before the web app? — *answered by:* ask Stripe for the surface split; instrument a pilot with web plus one embed — *affects:* embedded/host-agnostic, own app, chat-native


---

## trust-privacy-defaults: Trust and privacy defaults for sessions and context
**Choice:** Who can see an agent session (its transcript, artifacts and memory) by default: only its owner, the people invited, a team or project, or everyone in the org; and whether private work is allowed at all.
**Why it matters to the strategy:** It decides how much the org learns from each session (Shopify's whole thesis) against what users will be willing to ask, what sensitive data leaks, and whether the design survives a regulated setting. It is a policy choice as much as a product one and has its own owners (security, legal, HR, works councils).
**Related themes:** [[public-by-default-agent-work]], [[org-learning-loop]], [[shared-persistent-sessions]], [[identity-delegation]], [[task-context-isolation]], [[scoped-governance-containers]], [[compounding-context-repo]]   **Related dimensions:** [[agent-interface]], [[session-persistence-sharing]], [[agent-identity-delegation]], [[governance-control-plane]], [[context-and-memory]], [[artifact-and-project-structure]]
Opened by competitive-teardown-shopify-river (Geoff's request), in parallel with competitive-teardown-stripe-knowledge-agents.

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Private by default, no sharing | Sessions belong to one user; nothing visible to others | Local Claude Code, Cursor, ChatGPT ("a private window" in Tobi's words) | Users ask anything; no leakage between colleagues; simplest compliance story | Org learns nothing ("the only person who learns anything is the person at the keyboard"); transcripts deleted (Claude Code 30-day default) | mainstream | [Tobi article](../research/sources/x-tobi-learning-on-the-shop-floor.md) (first-party, argues against); [ITdaily](../research/sources/itdaily-claude-code-30-day-transcript-deletion.md) (independent) |
| Private by default, share on demand | The owner chooses to share a session (snapshot link, hand-off, invite) | Ramp Glass share-session; Claude Code on the web Team-visibility link | Users control exposure; supports hand-off | Few sessions may be shared (Ramp gives no share rate); learning depends on individual effort | early-adopter | [Glass launch](../research/sources/ramp-introducing-glass.md) (first-party); [Claude cloud docs](../research/sources/anthropic-claude-code-cloud-sessions.md) (first-party) |
| Private draft, then publish the outcome | Work privately; share a cleaned artifact, skill or blueprint, not the transcript | Cloudflare OS blueprints (code without data or history); skills marketplaces (Glass Dojo) | Learning through reusable recipes; experiments stay private | Loses "how people begin the work", which Tobi says matters most; relies on people publishing | emerging | [Cloudflare OS](../research/sources/cloudflare-os-announcement.md) (vendor claim); [Goddijn](../research/sources/x-sebgoddijn-glass-article.md) (first-party); [Bernstein](../research/sources/asq-bernstein-transparency-paradox.md) (independent: privacy zones, then share once there is data) |
| Team- or project-scoped by default | Sessions visible to a team, project or workspace with its own policies | Confluence space permissions; Stripe Kai project-scoped tool policies | Learning within the group that shares context; sensitive work fenced by container | Silos between teams; container design and membership upkeep | early-adopter | [Confluence restrictions](../research/sources/atlassian-confluence-page-restrictions.md) (first-party) |
| Public by default org-wide, no private mode | Every session is a transcript open to all employees; the agent refuses DMs and private channels ("you can't go into a private channel and say, 'Hey, River, help me build'", Thawar) | Shopify River ("River only works in the open. No direct messages"); Shopify Quick (all sites open to all employees, no owners) | Osmosis learning (Lehrwerkstatt); a corpus to mine into skills and defaults (merge rate 36%→77% claimed); "honesty pressure" on agent and user; co-participation (171,853 same-thread links in Sep 2026) | Chilling effect ("Some questions that would have been asked in a DM just don't get asked", River's own words); sensitive data (customer PII, security findings, HR, M&A, incidents) in open threads; channel join policy becomes the access control; broad visibility can breed hiding (Bernstein); unclear fit with regulated walls; all evidence self-reported | early-adopter (one large adopter) | [Under the River](../research/sources/shopify-engineering-under-the-river.md) (first-party); [Tobi article](../research/sources/x-tobi-learning-on-the-shop-floor.md) (first-party); [River's reaction](../research/sources/x-tobi-river-reaction-to-shop-floor-post.md) (first-party); [Quick](../research/sources/shopify-engineering-quick.md) (first-party); [Bernstein](../research/sources/asq-bernstein-transparency-paradox.md) (independent, counter-evidence); [Beyond the Pilot](../research/sources/venturebeat-beyond-the-pilot-farhan-thawar.md) (first-party); critiques: [Magica, quoting Slack's CPO on a boundary for "genuinely sensitive work"](../research/sources/magica-shopify-river-agent-context-cost.md) (independent), [AI Slopcast: an archive of everyone's gaps is "a treasure trove" for HR](../research/sources/oleg-guru-ai-slopcast-shopify-river-lehrwerkstatt.md) (independent), [HN anecdote](../research/sources/hn-shopify-river-discussion.md) (anecdote) |
| Public by default with fenced exceptions | Open by default, with named private zones (security, HR, legal, regulated teams) and information barriers | Implied by River's security-remediation threads (where they live is unstated); Slack information barriers | Most of the learning benefit, with walls where law or risk requires | Who decides the exceptions; exceptions grow; agent memory and skills may carry data across the wall | emerging (inferred; no documented example) | [River vuln remediation](../research/sources/shopify-engineering-river-vulnerability-remediation.md) (first-party, silent on visibility); [Slack information barriers](../research/sources/slack-information-barriers-docs.md) (first-party: barriers don't stop interaction in shared channels) |
| Channel-membership-scoped agent credentials | The agent acts with a bundle or service identity in a channel; whoever can post there can direct it, and new members see scrollback | Claude Tag; Codex Slack (responses readable by channel members) | Simple to deploy in chat | Visibility and authority both follow channel membership; public-channel join policy governs access to bundled credentials | early-adopter | [Tenable](../research/sources/tenable-claude-tag-slack-access-model.md) (independent); [Codex Slack](../research/sources/openai-codex-cloud-slack.md) (first-party) |

### Key questions to choose
1. What share of the target jobs touch data that can't be open to the whole org (customer PII, financials, security, HR, legal, unreleased strategy), and can those jobs be fenced without killing the default? — *answered by:* jobs map scored with a data-classification owner; security/privacy policy owner — *affects:* public-by-default, fenced exceptions, team-scoped
2. Is the target a regulated organisation with information barriers, records-retention, or works-council rules on employee monitoring? If so, is public-by-default allowed at all? — *answered by:* Geoff; compliance, legal and (in the EU) works council — *affects:* public options
3. How large is the chilling effect: which questions stop being asked when sessions are public, and are they the low-value ones (River's claim) or the important, uncertain ones (Bernstein's finding)? — *answered by:* a pilot with matched teams (public vs private default), counting questions asked and their kind; user interviews — *affects:* public-by-default vs private-by-default
4. Does visibility itself drive the learning, or does it come from someone mining the corpus into skills (Shopify does both)? If mining is what matters, private-by-default with an opt-in corpus might capture most of the value. — *answered by:* ask Shopify; a pilot measuring reuse of others' threads vs reuse of mined skills — *affects:* public-by-default vs private draft then publish
5. When a session is visible, does the viewer see only what their own permissions allow (re-check), or everything the session saw with the creator's access? — *answered by:* security owner; prototype — *affects:* all shared options; see [[agent-identity-delegation]]
6. What does our org's culture support: would a CEO-modelled public channel (Tobi's #tobi_river, 100+ watchers) work here, or does public-by-default need a leadership mandate we don't have? — *answered by:* Geoff / leadership; user interviews — *affects:* public-by-default
7. How are memory and skills learned from public sessions scrubbed of sensitive data before they are reused everywhere? — *answered by:* prototype of a mining pipeline with a redaction step; Track 5 memory research — *affects:* public-by-default, private draft then publish

### Current lean and what would change it
No lean. Shopify is the only large-scale evidence for public-by-default and it is all self-reported; the one independent study found the opposite effect in a very different setting (factory floor, 2009). A finding that the target org is regulated, or that the first jobs are mostly sensitive, pushes toward private or team-scoped defaults with a publish step; a pilot showing a small chilling effect and high reuse of others' threads would push toward public-by-default.

### Added by: competitive-teardown-shopify-river on 2026-10-24

#### Stripe knowledge-agents additions (competitive-teardown-stripe-knowledge-agents, 2026-10-24)
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Private single-user sessions, personal sources opt-in per session (Stripe detail for "Private by default") | Sessions belong to the user (sharing on the roadmap); org chart, date and project system known by default; Drive, Slack and DMs connect only if the user opts in, togglable per session or day | Stripe Kai | Users control what personal context the agent sees; low leakage risk | Context "locked in"; org learns only through published skills | early-adopter | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Isolation by task context, not just user permission | The platform forbids combining data from two unrelated customer contexts in one session even when the user can access each; boundary is "what should this task be allowed to view given this context?" | Stripe Kai | Prevents cross-customer contamination in analyses and artifacts | Needs data tagged by context and enforcement in tools; mechanism not disclosed | emerging | [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party) |
| Team- or project-scoped by default (Stripe evidence) | Projects (5 to 500 people, open to join) carry tool policies, default model, human confirmation on sensitive tools, and for HR a separately secured back end | Stripe Kai projects | Policy fits the work's sensitivity; one owner decides for many | Session visibility inside a project not stated (sessions appear single-user) | early-adopter | [How I AI, Krishnamurthy](../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party) |
| Open by default for coding-agent runs, private for knowledge work (mixed defaults by work family) | Coding-agent runs posted in a public Slack channel others watch; knowledge-work sessions private | Stripe Minions robots channel (76 watchers) vs Kai | Learning from visible runs where data is low-risk (code in QA devboxes) | Two policies to explain | anecdote | [How I AI, Kaliski](../research/sources/howiai-stripe-minions-kaliski.md) (first-party); [Stripe Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party) |

Key questions (Stripe pass):
8. Stripe makes coding runs visible and knowledge-work sessions private; Shopify makes everything public. Is the right default set per work family or data class rather than org-wide? — *answered by:* jobs map scored by data class; ask Stripe and Shopify why their defaults differ — *affects:* all options
9. How would task-context isolation be enforced in our setting (data tags, tool-level checks, session forks)? — *answered by:* security owner; prototype with two customer datasets — *affects:* private, project-scoped and public options


Department of Product pass (competitive-teardown-stripe-knowledge-agents, 2026-10-24): an independent explainer extends Stripe's task-context isolation to other domains: never two candidates for the same role side by side; never two patients summarised together; never performance and compensation data combined in one output. It argues such **combination guardrails** must be enforced at infrastructure or session level, not left to skill owners, and offers a discovery method: list what each group may access, then look at combinations, define each rule by harm and detection, and rank by likelihood × severity ([Department of Product](../research/sources/departmentofproduct-stripe-kai.md), independent). Key question: 10. Which combinations of individually accessible data must never meet in one session in our target orgs (e.g. two customers' roadmaps, a person's performance and pay), and can they be enforced below the skill layer? — *answered by:* security and policy owner workshop using that method — *affects:* all options

---


## Cross-cutting key questions


1. Who is the user we are choosing for (individual PM, product team, whole org), and does the answer differ by dimension? — *answered by:* Geoff / user interviews
2. What would the resource request fund first: a prototype to choose between options, or a build of the leading option?
3. Is the target setting a regulated organisation (as in Geoff's two intent docs)? If so, how does regulatory review shape every dimension: review gating, prototype-as-spec, context governance, and harness choice? — *answered by:* Geoff; risk and compliance policy owners — *affects:* [[review-and-autonomy]], [[intent-shaping-and-spec]], [[context-and-memory]], [[governance-control-plane]] (added by research-product-agent-and-harness)
4. Shared-agent identity (creator, requester, service account) is a product decision as much as a security one: what is the least surprising behaviour for our users when a teammate sends an instruction to an agent holding someone else's access? — *answered by:* user interviews plus security owner — *affects:* governance-control-plane, session-persistence-sharing (Track 5)
5. (Track 3) Is the first deployed task agent meant to be called from many harnesses we do not control, or only from our own product? The answer decides whether protocols (MCP/A2A) matter at all or a vendor API suffices. — *answered by:* Geoff / user interviews; see [[remote-invocation-route]]
6. (Track 2) Is the thing being funded a harness at all, or the assets and governance around vendor harnesses? The independent evidence says the competitive unit has moved from the loop to the ecosystem surface (skills, marketplaces, governance), and that building the loop is cheap while upkeep and evals are not. — *answered by:* Geoff / director deciding the scope of the request; Track 4 and 5 findings; a scoped upkeep estimate

- (Track 6) Does the project treat "unstructured" work as out of scope for standardisation (leave it in a flexible harness) or as something that still needs structured context (folders, memory, rubrics)? The evidence (best-practices guidance, vault anecdotes) says the path is open but the context is structured. — *answered by:* Geoff; user interviews

- (user-story-mapping) Which embodiment fits depends on a fact we lack in several stories: how PMs keep artifacts today, whether reviewers will enter agent sessions, and whether a machine-checkable spec standard exists. Are these three facts the first things to establish before any prototype? The cross-cutting stories ([S11–S15](../tasks/user-story-mapping/stories-cross-cutting.md)) and the S05 pair ([worked derivation](../tasks/user-story-mapping/worked-derivation-s05.md)) mark where each bites. — *answered by:* a short interview round plus one clickable prototype pair — *affects:* all
7. Ramp changed its answer on who supplies the loop (vendor SDK → own harness) and where it runs (laptop → cloud workers) within about six months of shipping Glass. Should the resource request fund a reversible first step and an explicit revisit point rather than a one-time pattern choice, and what would the revisit criteria be? — *answered by:* Geoff / the strategy deck's framing; evidence in [Building Laminar](../research/sources/ramp-builders-building-laminar.md) (competitive-teardown-ramp-glass, audit 2026-10-24)
8. (competitive-teardown-stripe-knowledge-agents) Stripe runs its internal knowledge agent on the same harness, sandbox, orchestration and access control as its customer-facing agents, arguing the shared substrate forces the external security bar inside and improves both. Does our resource request assume the internal PM agent and any customer-facing agent share a substrate, or are they separate bets? It bears on loop-source, runtime-location, governance-control-plane and trust-privacy-defaults. — *answered by:* Geoff / product leadership; ask Stripe what sharing has cost them — *affects:* the scope of the request ([source](../research/sources/stripe-meet-knowledge-ai-platform.md), first-party)

- (competitive-teardown-shopify-river) Does the strategy assume the target org will accept agent work being visible by default? Shopify's River (public-only, no DMs) shows the learning upside; the cost (chilling effect, sensitive data, regulated walls) is unmeasured. The answer moves [[agent-interface]], [[trust-privacy-defaults]], [[context-and-memory]] (corpus mining), [[adoption-model]] and [[agent-identity-delegation]] together. — *answered by:* Geoff; policy/compliance owners; a matched public-vs-private pilot
