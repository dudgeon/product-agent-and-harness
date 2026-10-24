# Teardown: Stripe's agents for knowledge workers (summary)

Date: 2026-10-24. Worker draft for Geoff's review. Source notes are in the research library (`../../research/sources/`). Primary sources: [Stripe's Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md) (2026-07-30), [LangChain case study](../../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (2026-08-03, vendor), [How I AI with Sharadh Krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md) (2026-09-07, 50-minute demo), [AWS/Stripe compliance agents](../../research/sources/aws-stripe-compliance-agents.md) (2026-06-26), [Harbor](../../research/sources/stripe-harbor-ai-prototyping.md) (2026-09-14), [payment-method factory](../../research/sources/stripe-payment-method-factory.md) (2026-09-30), [How I AI with Steve Kaliski on Minions](../../research/sources/howiai-stripe-minions-kaliski.md) (2026-03-24), [Latent Space with Emily Sands](../../research/sources/latentspace-emily-sands-stripe.md) (2025-10-30, the pre-Kai baseline), plus leader posts ([Sands](../../research/sources/x-emilygsands-kai-launch.md), [Weinstein](../../research/sources/x-jeff-weinstein-kai-sibling.md), [Krishnamurthy](../../research/sources/linkedin-sharadhk-kai-launch-post.md)) and one independent critique ([AI Founders](../../research/sources/aifounders-stripe-kai-dont-copy-sales-numbers.md)). Everything about how the agents work and what they achieve comes from Stripe or its vendors (LangChain, AWS). Nothing has been independently verified, and nothing here comes from using the product.

Minions (the coding agents) are already covered in [part 1](../../research/sources/stripe-minions-one-shot-coding-agents.md) and [part 2](../../research/sources/stripe-minions-part-2.md). This teardown adds only how Minions are started and watched, which was missing.

## What the agents are, and which jobs they serve

When I searched, "Stripe's knowledge-worker agents" meant one main product and three related systems. The scope was clear enough that I didn't need to ask.

| System | What it is | Who uses it, for what | Scale (Stripe-reported) |
|---|---|---|---|
| **Kai** (Knowledge AI Platform) | A company-wide agent for people who don't write code. It is a hosted agent service with a web app, a Slack integration, Chrome extensions inside third-party tools, and an API that internal apps embed. | Sales: account research before calls, deal prep. Finance: messy-data analysis, recurring digests, budget modelling inside Finance's own app. Ops, legal and marketing. Engineers use it for system questions, log analysis and plans. Data analysis is the biggest use: 5,000+ sessions a day. | Launched April 2026. 83% weekly active (blog, Jul 30). "86+%" and "10,000+ weekly" (podcast, Sep). Marketing 95%, GTM 87%, both above engineering. 1,000+ skills from 100+ teams, about 2,000 by September. 500+ MCP tools. |
| **Agent Studio** | The control plane for domain owners. Teams build, test and monitor their skills, custom Kai agents and tool selections, with usage and quality signals for each. | Domain owners in GTM, Finance, Legal and other functions | Not given |
| **Harbor** | A browser-based prototyping agent. It is designer-first but now used across the company, and its tools are exposed over internal MCP to Kai and to coding agents. | Designers. Finance presents monthly actuals as clickable prototypes. Account executives build pricing proposals and ROI calculators. Risk ops builds dashboards. | 3,000+ people, 12,000 prototypes since May 2026; 25% of Stripes have made at least one |
| **Compliance review agents** | Agents embedded in analysts' review tooling. They answer quality-tested sub-questions as pre-fetched research, and the human still answers every question. | Financial-crime compliance analysts | Median handling time down 26%; >96% rated helpful; runs on an agent service hosting 100+ agents |

Before Kai (Oct 2025, [Sands](../../research/sources/latentspace-emily-sands-stripe.md)), Stripe had:
- GoLLM, a ChatGPT-style UI with shareable prompt "presets"; hundreds appeared overnight. It was later replaced by an open-source LibreChat front end.
- Toolshed, a central MCP server that owning teams extend themselves.
- Hubert, a text-to-SQL assistant with about 900 weekly users.
- A NoCode Agent Builder that produced more than 4,000 agents. Kai replaced it because the micro-agents repeated each other, varied in quality and were hard to maintain ([Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md)).

Daily LLM-tool use was already 8,500 of roughly 10,000 staff. Kai therefore landed in a company that already used AI tools heavily.

## How Kai works, by dimension

**Loop source and layering.** Kai is built on LangChain's open-source Deep Agents harness, in Python. Stripe adds its own harness layer for security, infrastructure and internal services. Above that is a configuration layer: teams define custom Kai agents with their own skills, behaviour and persona without touching the harness. Minions run on a fork of Goose. So Stripe runs **two loop sources for two families of work**. Kai is also the first production example in our library of a non-coding, multi-user agent built on a general framework, which partly answers open key question 11 in loop-source. The caveat is that the "one engineer in a week" build story is LangChain's marketing line. Stripe's own account is "one and a half people over two weeks" for v0, a core team now under 10, and the pre-existing Toolshed and data catalog doing much of the work. A Kai **project can be backed by a different harness and API** while keeping Kai's features. That makes Kai a front door and governance layer that can sit in front of other harnesses ([podcast](../../research/sources/howiai-stripe-kai-krishnamurthy.md), 31:00).

**Runtime location.** Kai is a cloud service on Kubernetes: always on, inside Stripe's standard security boundary. Each session gets a secure sandbox, but the **sandbox is a tool the agent calls**, not the place the agent runs. Artifacts live in a multi-tenant virtual filesystem backed by S3, with files synced into and out of the sandbox on every call. The core pieces (harness, sandbox, orchestration, access control) are shared with Stripe's customer-facing agents on purpose, so internal work meets the same security bar. Compare Glass, which is a desktop app that turns the laptop into a server.

**Capability packaging and distribution.**
- Skills follow the open spec and are loaded in tiers: foundational skills are pinned for everyone, then more load by function, by custom-agent config and by user profile.
- Skills gate tools. The model picks skills, and each skill's `allowedTools` loads only the tools it needs (a two-pass load).
- Stripe reports that frontier-model quality drops above **about 150 skills** combined with the system prompt, and is moving to a hybrid retrieval-plus-LLM selector.
- A skill-creator turns a session into a skill. The author can publish it privately or to an "area", edit drafts in an IDE-like editor, and receives automatic improvement suggestions.
- Telemetry sorts the library: about 50 skills are used heavily every day, 100-150 by sub-organisations, and a long tail by two or three people each. A pipeline tells the platform team which skills to promote into the default context and which to move out.
- This compares with Glass's Git-backed Dojo marketplace (Git hidden from users, 350+ skills). Both are federated, but Stripe leans on telemetry and quality signals, while Glass leans on Git review.

**Remote invocation.**
- Minions start from a **Slack emoji reaction**: the message becomes the prompt and the emoji picks the repo. They can also start from Docs or tickets, or from a phone. Engineers follow along in the thread and can drop into the devbox.
- Harbor publishes its tools and rendering engine over internal MCP, so Kai and devbox coding agents can create and publish prototypes.
- Stripe's stated principle: "keep agents specialized ... while exposing them to capabilities in other systems" ([Harbor](../../research/sources/stripe-harbor-ai-prototyping.md)).

**Sessions, persistence and sharing.** Kai sessions are long and stateful (one reached 932 turns; some run for weeks), and the user iterates on artifacts in place. They are **single-user**. Stripe itself says context is "locked in", and sharing across sessions or collaborating on one artifact is roadmap. Collaboration happens today at the artifact level: Harbor publishes a snapshot to a URL, and comments are anchored to elements and re-checked when the agent rewrites the page. Minions are the open-by-default exception: Kaliski runs his in a public Slack "robots" channel that 76 people follow. Compare Glass, which shares sessions themselves.

**Identity and delegation.** Kai knows who the user is and where they sit in the org chart. Krishnamurthy says Stripe "haven't solved" agent identity. They do tag agents by the use case they serve, for priority and load shedding, after agents "went rogue" and "almost took down core systems". **None of the sources says under whose credentials Kai's tool calls run.**

**Governance, cost, audit and review.**
- **Projects are the unit of governance** (new to our register). A project owner can:
  - set the default model and block expensive models;
  - set tool policies, for example stopping HR's sensitive data from being written to a company-wide Google Doc without banning tools;
  - require a human to confirm specific sensitive tools, in that project only;
  - give the project a separately secured back end.
- Projects range from 5 to 500 people. The reasoning: a few experts make the cost and safety choices once, and everyone else avoids prompt fatigue ("eventually you're going to press the wrong button").
- All LLM calls go through an internal LLM proxy. It limits noisy neighbours, provides fallbacks, tracks usage, and checks that the model fits each application's privacy class.
- Compliance agents keep a full log of every run, and a human answers every sub-question.
- The Minions rule (a human reviews every PR) is already filed.

**Context, memory and artifacts.**
- By default Kai knows the user, the org chart, the date and the project-management system (OKRs, projects). **Drive, Slack and DMs are opt-in, and the user can switch them per session.** Krishnamurthy switches his own off and on daily.
- Data questions go through a skill written by data scientists: existing reports first, then a blessed analytics layer, then the data catalog. It sits on years of work on the data catalog and table tiering, plus a Trino warehouse hardened against agents' brute-force querying.
- No long-term personal memory is described. State lives in the session's virtual filesystem, with summarization. Compare Glass's offline memory pipeline.
- Artifacts (dashboards, reports, docs) live beside the chat and change with it.

**Agent interface.** "The agent is a service, not an application, and surfaces are simply customized views into it." Stripe rejected a standalone app because it "would force users out of their natural workflows", and rejected a separate product per surface because it would be hard to maintain. Most people use the web app, which needs no setup on day 0. Slack, the Chrome extension and API embedding cover everywhere else. This is a third answer between "own app" (Glass) and "just Slack". It feeds the agent-interface dimension that the River teardown is opening.

**Trust and privacy defaults.** Kai sessions are **private by default** (single-user). Personal sources are **opt-in**. **Isolation is set by task context, not only by user permission**: "you shouldn't combine data from two unrelated customer contexts in a single analysis", even when the user can see both. Projects are "all open" for anyone to join, but each carries its own tool policies. Minions run in the open. So Stripe makes **knowledge-work sessions private and coding-agent runs public**.

**Adoption.**
- Kai shipped as a v0 (1.5 people, about 2 weeks), went to a pilot with GTM (200-300 users, 2.5-3 people), then a company-wide demo started the steep ramp: 296 users to 5,000+ in about 4 weeks, and the quarterly target hit in the first week of open preview.
- The design principle: "you don't need to tune knobs". The heaviest adopters were users who had "found the previous thing unapproachable".
- The preconditions are not small: AI use was already near-universal, there was a culture of friction logs, and devex and data platforms already existed.

**Outcomes (all Stripe-reported).**
- Kai:
  - Account executives, in weeks they use Kai compared with weeks they don't: 2x sales activity, +17% opportunities, +26% revenue opportunities, +39% deals.
  - GTM new hires use Kai 2.7x more, and power users close 80% more value than low users in the same cohort.
  - "25,000 hours per year" moved from admin work to revenue work.
- Compliance: median review time down 26%, >96% helpful, and prompt caching cut cost 60%.
- Harbor: 12,000 prototypes.
- Payment-method factory: integrations went from up to 6 months to 2-6 weeks.
- The independent critique points out that the sales figures compare usage with non-usage, and the best sellers adopt first, so cause is unproven ([AI Founders](../../research/sources/aifounders-stripe-kai-dont-copy-sales-numbers.md)). Sands herself said in Oct 2025: "I have a really hard time understanding impact."

## Design choices worth noting (for the deck)

1. **An agent service with surfaces, not an app.** One agent behind an API, with the web app as the default, and Slack, a browser extension and embedding wherever people already work.
2. **Projects as governance.** Policy (model, tools, human confirmation, back end, harness) is set once per project by an owner, not by each user and not org-wide.
3. **Isolation by task context.** Session boundaries are set by what the task should see, not only by what the user can see.
4. **One general agent with many skills, plus a few specialists.** Stripe dropped 4,000 no-code micro-agents for one agent with skills, kept separate specialists (Harbor, Minions, compliance) and connects them over MCP.
5. **Skills gate tools.** Tool context stays small; there is a measured limit at about 150 skills; telemetry decides what goes into the default context.
6. **Share the substrate with the external product.** The internal agent runs on the same harness, sandbox and access control as customer-facing agents. Stripe argues this keeps internal work to the external security bar and lets each side improve the other.
7. **Specific human gates on judgment work.** In compliance, agents fetch the research and humans answer. Kai asks for confirmation only on tools the project owner marks as sensitive.
8. **Orchestration in code.** Both the compliance review graph and the payment-method factory found that predictable coordination belongs in code, not in an orchestrator LLM.

## Compared with Ramp Glass

| | Stripe Kai | Ramp Glass |
|---|---|---|
| Form factor | Cloud service; web app by default, plus Slack, Chrome extension, embedding | Desktop app; laptop acts as the server; Slack assistants |
| Loop | Deep Agents framework plus a Stripe harness layer | Claude Agent SDK at first, now Laminar (Ramp's own harness) |
| Skills | 1,000-2,000; Agent Studio; telemetry-driven | 350+; Dojo marketplace on Git with Git hidden from users |
| Governance unit | Project (model, tools, human confirmation, back end) | Per-project cost meter plus a model router |
| Memory | Session virtual filesystem; org context; no personal memory described | Offline memory pipeline that is read-only during sessions |
| Sharing | Single-user sessions; artifacts shared (Harbor) | Shared sessions; shared knowledge edits |
| Privacy default | Private sessions; personal sources opt-in; task-context isolation | Not described in our sources |
| Adoption | 83-86% weekly, from a high AI baseline | 99% "use AI daily"; about 700 daily users in month one |

## Claims vs evidence

| Claim | Source | Evidence status |
|---|---|---|
| 83% weekly (Jul), 80% weekly and 20,000+ sessions a day (LinkedIn), 86%+ and 10,000+ weekly (Sep), ">60k sessions" (LangChain) | Stripe staff, LangChain | Self-reported on different bases and dates; the periods aren't stated |
| AEs +39% deals, +26% revenue opportunities | Kai post | Same sellers' Kai weeks vs non-Kai weeks; selection bias ([independent critique](../../research/sources/aifounders-stripe-kai-dont-copy-sales-numbers.md)) |
| 25,000 hours a year moved to revenue work | Kai post | Method not stated |
| Built by one engineer in one week | LangChain | Vendor headline; Stripe says 1.5 people over 2 weeks |
| Quality degrades above about 150 skills | LangChain quoting Stripe | Internal observation; no eval published |
| Compliance review time -26%, >96% helpful | AWS/Stripe | Stripe-reported; the most measurable claim here |
| Harbor: 3,000+ people, 12,000 prototypes | Harbor post | Stripe-reported counts |
| Agents "almost took down core systems" | Krishnamurthy | Anecdote; no details |

The architecture claims (layering, sandbox as a tool, the VFS, skills gating tools, projects) come from the builders and are specific and technically credible. They are the strongest material in this teardown. The outcome claims are the weakest.

## Open gaps and caveats

- Whose credentials Kai's tool calls use, how task-context isolation is enforced, who approves publishing a skill to an "area", and data retention and visibility of sessions for admins: none of this was found.
- The follow-up post Stripe promised on skill routing (hybrid RAG/LLM) had not appeared as of 2026-10-24.
- Both podcast transcripts are YouTube auto-captions. Timestamps are rounded to two-minute blocks.
- X posts were read through a read-only mirror, without logging in, and replies were not read. The LinkedIn post was read from a public profile, and its date is unconfirmed.
- Checked but with nothing on internal agents: Stripe's 2025 annual letter (PDF) and the Sessions 2026 coverage, which is about external agentic commerce. The Department of Product piece is paywalled after the intro.
- I found no talk by Stripe's AI Platform lead (Chrissie Cui) and no independent post-mortem.

## Options by dimension

Every Stripe design choice is filed as option or evidence rows, with key questions, under a "Stripe knowledge-agents additions" heading in each of these sections of [options/DIMENSIONS.md](../../options/DIMENSIONS.md):

- [loop-source](../../options/DIMENSIONS.md#loop-source-who-supplies-the-agent-loop): two loop sources by family of work. Questions 13-14: how much of Kai's fast build came from the framework vs Stripe's existing infrastructure; one loop or two?
- [harness-layering](../../options/DIMENSIONS.md#harness-layering-is-there-a-layer-above-the-vendor-harnesses): a company agent platform whose configuration layer can sit in front of other harnesses.
- [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives): a cloud agent service with the sandbox as a tool; a dedicated agent service.
- [capability-format-portability](../../options/DIMENSIONS.md#capability-format-portability-capability-format-and-portability): skills that gate tools, tiered by role; progressively disclosed skills.
- [capability-distribution-trust](../../options/DIMENSIONS.md#capability-distribution-trust-capability-distribution-and-trust): a federated control plane owned by domain teams; the no-code builder (reported failure); a tool server that teams extend.
- [remote-invocation-route](../../options/DIMENSIONS.md#remote-invocation-route-how-a-primary-harness-reaches-a-remote-or-deployed-agent): a chat reaction starts a remote agent; a specialist tool exposed over internal MCP.
- [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff): long single-user sessions; sharing the artifact rather than the session; a public channel as the run log.
- [agent-identity-delegation](../../options/DIMENSIONS.md#agent-identity-delegation-agent-identity-and-delegation): agent identity tagged by use case (unsolved).
- [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-governance-and-control-plane-policy-cost-audit): **project as the unit of governance**; a central LLM proxy with privacy-class checks; full logs of every run.
- [model-provider-coupling](../../options/DIMENSIONS.md#model-provider-coupling-how-tightly-the-agent-is-coupled-to-one-model-provider), [harness-upkeep](../../options/DIMENSIONS.md#harness-upkeep-who-maintains-the-harness-over-time-and-at-what-cadence): evidence rows.
- [context-and-memory](../../options/DIMENSIONS.md#context-and-memory-context-and-memory): org context by default with personal sources opt-in; a data-access path encoded as a skill; a session-scoped virtual filesystem with no long-term memory.
- [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found): the project as a container for intent plus governance; artifacts that evolve beside the conversation.
- [target-user](../../options/DIMENSIONS.md#target-user-which-users-and-personas-we-serve-first-including-for-shared-agents), [pm-agent-evaluation](../../options/DIMENSIONS.md#pm-agent-evaluation-how-we-would-know-a-pm-agent-works): comparing the same users with and without the agent; handling time plus a helpfulness rating.
- [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent): a federation of specialised agents connected over MCP; a human-driven review graph; orchestration in code.
- [review-and-autonomy](../../options/DIMENSIONS.md#review-and-autonomy-review-and-autonomy), [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model): one front door with no knobs, piloted then demoed company-wide; install prompts at the moment of intent.
- [agent-interface](../../options/DIMENSIONS.md#agent-interface-agent-interface-own-app-chat-or-embedded) (opened by the Shopify River teardown): one agent service with the web app as default plus chat, browser extension and API embedding; a chat reaction as the front door for task agents; specialist apps exposed over MCP. Question 7: would embedded surfaces get real use for our users?
- [trust-privacy-defaults](../../options/DIMENSIONS.md#trust-privacy-defaults-trust-and-privacy-defaults-for-sessions-and-context) (opened by River): private single-user sessions with personal sources opt-in per session; isolation by task context; project-scoped policies; open defaults for coding runs, private for knowledge work. Questions 8-9: should the default differ by type of work or data class, and how would isolation be enforced?
- Cross-cutting question 8: should the internal agent share a substrate with any customer-facing agent?

New themes in [research/THEMES.md](../../research/THEMES.md): `agent-as-service-many-surfaces`, `scoped-governance-containers`, `task-context-isolation`.
