# Ready to ship: intent shaping in a regulated enterprise, and the product agent and harness that could do it

Task: [strategy-story-and-explainer-video](../strategy-story-and-explainer-video.md). Written 2026-10-24 on the outline Geoff approved at Checkpoint A ([00-outline.md](00-outline.md)). This is the strategy-shaped story the film is cut from: situation, complication, questions, options, and one hypothetical answer compared with the other implementations in the consideration set.

**Read this first.** The project's deliverable is a menu of options by dimension, with the key questions that would decide among them, to inform a resource request. It is not a recommendation ([PROJECT.md](../../PROJECT.md), Decisions). **Helm, the notional workspace in part 5, is a concept to illustrate the potential. It is not the answer to the case.** Every number and quote below is checked against the current, post-audit source note in `research/sources/`; the claim-check appendix lists each one with its evidence type. In the text, "first-party" means the builder describing its own system, "vendor claim" means promotional or about a customer, "independent" means nobody with a stake, and "anecdote" means a forum post, a blog or second-hand. All statements are as of 2026-10-24; the field changes monthly.

Sources are cited by note name; the notes link to the originals.

---

## 1. Situation

### 1.1 The factory sped up

Coding agents reached engineers first, and in the companies that let them run, they now write a large share of the code. Stripe says its Minions, one-shot coding agents on a Goose fork, produce more than 1,000 merged pull requests a week, every one reviewed by a human (first-party, March 2026; `stripe-minions-one-shot-coding-agents`). Ramp's chief product officer says Inspect, its background coding agent, accounts for 75% of Ramp's pull requests, with about a thousand a month opened by non-engineers (first-party, September 2026; `lenny-podcast-geoff-charles-product-when-coding-solved`). Shopify's CEO wrote in May that about one in eight pull requests merged into its monorepo the previous week was authored by River, its Slack-native agent, and reviewed by people (first-party; `x-tobi-learning-on-the-shop-floor`); by October Shopify reported River's share of merged mobile pull requests had gone from 6% to 61% (first-party; `shopify-engineering-remote-dev`).

None of these numbers has been verified by anyone outside the company that published it. The method behind each is unstated. But the direction is not in doubt, and the three companies agree on what made it work: not a better model, but the harness around it. Ramp's lead builder titled his account "The Models are Good Enough" (first-party; `x-sebgoddijn-glass-article`). Shopify says the agent "will not be the interesting part" in two years; the substrate under it will be (first-party; `shopify-engineering-under-the-river`).

### 1.2 The product job today

The product manager's job has not changed. Atlassian's chief product officer put it plainly: the job "is really the same as it always was"; what changed is how it is done (first-party; `lenny-podcast-tamar-yehoshua-roles-expanding`). The research for this project mapped ten recurring jobs, from customer contact and research synthesis through intent shaping, specs, prioritisation, delivery, launch, stakeholder communication, metrics and post-launch triage ([jobs map](../research-pm-agents-jobs-to-be-done/01-jobs-to-be-done-map.md)).

Product people already use agents for these jobs, but unevenly. In Lenny's survey of 1,750 respondents (independent, self-selected), writing PRDs is the top PM use of AI at 21.5%, and user research the lowest at 4.7% despite being the largest unmet demand (`lennys-newsletter-ai-tools-overdelivering-results`). The only telemetry-backed study, of 885 product managers at Microsoft (first-party, one company), finds 62% use generative AI daily, concentrated on drafting documents (73%) rather than research (22%) or prototyping (12%), and that specs are held back as high-accountability work; self-reports matched the telemetry only moderately (`arxiv-pm-delegating-work-to-genai`).

The baseline this project starts from is Geoff's own description, marked as such throughout the user stories: inconsistent use of Claude Code, artifacts scattered across chat transcripts and local folders, context re-supplied at the start of every session, and nothing shared ([stories README](../user-story-mapping/README.md)). Two independent facts sit under it. Claude Code deletes local session transcripts after 30 days by default, and users have reported losing decisions and reasoning without warning (independent; `itdaily-claude-code-30-day-transcript-deletion`). And across the platforms product teams use, there is no shared definition of what a "project" is or what a product artifact is: Atlassian alone has three objects called a project, and no vendor graph has a native type for a spec, an insight or a decision ([artifact research](../user-story-mapping/research-artifacts-standardization.md); `atlassian-teamwork-graph-object-types`, first-party).

### 1.3 The reference job

Geoff fixed the reference workload for this project on 2026-10-24: **intent shaping**. Take high-level intent and shape it against the real constraints of a large regulated enterprise into intent that deserves to ship and is ready to, with constraints identified and resolved, dependencies mapped, and ready to hand to an engineering team or a coding agent ([synthesis, Geoff's answers](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#geoffs-answers-2026-10-24)). The first users are his own team plus a small number of beta users across the company. The outcome he wants is human time freed for discovering novel problems, running experiments and finding insight, with the shaping of simple intent becoming near-autonomous while meeting the organisation's standards for quality and good management.

---

## 2. Complication

### 2.1 The bottleneck moved to intent

Geoff's own framing, in his Intent Factory document (first-party proposal, filed as anecdote because it is a position piece): organisations hold years of goals but only one or two sprints of shovel-ready intent; refinement is done bespoke each time, just in time; context is scattered across private documents and subject-matter experts; PRDs are vague (`geoff-building-accelerating-intent-factory`). That is a framing, not a measurement, and the resource request would have to measure it (value-stream data by stage is the instrument the register names).

The companies that automated delivery describe the same squeeze from the other side. Ramp's shaping skill reads 90 days of tickets in about eight minutes before a PM is interrogated with a standard question set, a Ramp claim relayed in Geoff's document (vendor claim). Stripe's rule is a human on every change: "not moving money without human review" (relayed in the same document). Shopify's head of engineering said in April that requiring a human reviewer on every PR "is now becoming a big bottleneck" (first-party; `bvp-inside-shopifys-ai-first-engineering-playbook`), and its CEO has a name for unread agent output pushed onto colleagues: "slop grenades" (first-party; `fs-knowledge-project-tobi-lutke-ai-agents`). When the factory runs faster than the people shaping and reviewing its inputs, the work piles up at both ends.

### 2.2 The evidence is thin, and most of it is the vendors' own

This is the complication that shapes everything else. After re-checking about 540 claims against their sources in the PM-agents audit, the project found **no independent, controlled evaluation of any PM agent doing a PM job**, and no agent-versus-human comparison of spec, prioritisation or status quality ([brief](../research-pm-agents-jobs-to-be-done/00-brief.md)). Atlassian says plainly it has not figured out how to measure outcomes (first-party, transcript 19:35 to 20:35). Across the runtime research, **no controlled comparison exists of a task-specific agent against a skill in a general harness for any standard job**; the synthesis calls this the central evidence gap ([synthesis A](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#a-executive-summary)).

What independent evidence exists is mostly about failure, and it is instructive:

- **Self-report is unreliable.** METR's randomised trial with experienced developers on early-2025 tools found AI-allowed tasks took 19% longer while the developers believed they were about 20% faster (independent; `metr-early-2025-experienced-developer-rct`). It is about coding, not PM work, but it is the only randomised evidence nearby and it is a warning about every "hours saved" figure in this corpus.
- **Synthesis invents.** Teresa Torres, comparing her own interview synthesis with ChatGPT's, found about 30% of the direct quotes wrong or missing (practitioner's own test, first-party; `producttalk-customer-interview-analysis-ai`).
- **Models agree too much.** A Stanford study in Science found eleven state-of-the-art models affirmed users' actions about 49% more often than humans did, and users trusted the sycophantic answers more (independent, read via summaries; `stanford-cheng-sycophantic-ai-science-2026`).
- **Skills do not reliably fire.** Vercel's own eval saw a skill never invoked in 56% of cases (vendor claim; `vercel-agents-md-outperforms-skills`). The independent SkillsBench study found curated skills gave +16.2 points on average but made 16 of 84 tasks worse, and Codex often ignored provided skills (independent; `arxiv-skillsbench`).
- **Delegation is unpredictable.** The best-known independent test of a fully delegated cloud agent, Answer.AI's month with Devin, saw 3 of 20 real tasks succeed, and infeasible tasks pursued rather than flagged (independent, January 2025, product since changed; `answerai-thoughts-month-with-devin`).

### 2.3 The ground moves

The field changes its answers within months, and the vendors change their terms within weeks.

- **Ramp reversed two architecture decisions in about six months.** In April 2026 Glass was a desktop app on the Claude Agent SDK that "turns your laptop into a server". By October it ran on Laminar, Ramp's own provider-agnostic harness, built in six weeks, on a fleet of disposable cloud workers; the local-first era was "a weird blip". Ramp's own caveat: building was cheap with coding agents, but you still need good engineers on call (first-party; `ramp-builders-building-laminar`; [Glass audit](../competitive-teardown-ramp-glass/audit-2026-10-24.md)). Any slide that says Glass runs on the Agent SDK is six months stale.
- **Access terms changed under third-party harnesses.** Anthropic blocked subscription credentials outside its own clients on 2026-01-09, sent legal demands in March, and ended Pro and Max coverage of third-party tools in April; API keys were never blocked (independent timeline; `falcao-anthropic-claude-access-crackdown`).
- **Governance layers failed open.** Omnigent, the most visible horizontal meta-harness, published 13 security advisories in its first four months, four of them critical, and several reproduced bugs showed its policies silently allowing actions when the policy server errored, for a harness running shell inside its own process, and for sub-agents. Each was fixed within days, by moving to deny-by-default (first-party advisories; `github-omnigent-security-advisories`; independent CVE analysis in `securelayer7-cve-2026-62676-omnigent`).
- **The vocabulary is unsettled.** "Meta-harness" is used for at least six different shapes, from a governance server over many CLIs to a local worktree manager to a model vendor's hosted service ([synthesis A](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#a-executive-summary); independent buyer's guide `codepick-meta-harness-guide`). This story uses the word only in its common horizontal sense, a layer above several vendor harnesses, and names other patterns as what they are.

### 2.4 The regulated setting adds three locks

Geoff confirmed the setting is regulated and audit is needed. Three constraints follow, and none has a settled public answer.

**Audit coverage follows the surface and the route.** Syracuse University disabled Claude Cowork organisation-wide because its activity was not in Anthropic's audit logs or Compliance API (independent; `syracuse-claude-cowork-security-considerations`). Anthropic closed that gap for Cowork and Claude Code on 2026-08-26, but the coverage still excludes Claude Code on the web, via the Claude Platform, and on Bedrock, Vertex or Foundry (first-party; `anthropic-compliance-api-cowork-claude-code`). The same harness has a different audit trail depending on where it runs.

**Nobody agrees whose identity a shared agent uses.** Cursor runs shared cloud agents with the creator's tokens, so a teammate's follow-up executes as the creator, which Cursor staff called intended (anecdote plus staff reply; `cursor-forum-team-followups-act-on-behalf`). Codex in Slack runs as the requester. Claude Tag runs as a service account, which makes channel membership the access boundary (independent; `tenable-claude-tag-slack-access-model`). Copilot's cloud agent is a co-author under a separate human approver. Omnigent's maintainers chose the invariant that "a shared session always executes as its owner" and that message authorship never changes authority, after one adopter built per-message acting identity and removed it because it produced privilege escalation (maintainer proposal and adopter accounts, anecdote; `github-omnigent-identity-audit-issues`).

**Visibility is a policy choice with a cost on each side.** Shopify made River public-only: "River only works in the open. No direct messages" (first-party; `shopify-engineering-under-the-river`). Its stated gains are learning by watching, a corpus to mine into skills, and "honesty pressure". River's own write-up names the cost: "Some questions that would have been asked in a DM just don't get asked", a trade-off it calls "mostly the right" one but "not free" (first-party; `x-tobi-river-reaction-to-shop-floor-post`). The one independent study of visibility and learning points the other way: Bernstein's factory-floor experiment found broad visibility bred hiding, and small privacy zones raised defect-free output by as much as 10 to 15% (independent, 2009 setting; `asq-bernstein-transparency-paradox`). Stripe went the other way from Shopify for knowledge work: Kai sessions are private, personal sources are opt-in per session, and a project is the unit of policy (first-party; `howiai-stripe-kai-krishnamurthy`).

---

## 3. The questions

Everything above narrows to seven questions. Only the first part of each has a direction from Geoff; the rest are what the research leaves open, and what a resource request would fund. The register holds the full list under each dimension; these are the cross-cutting ones, reframed around intent shaping.

1. **Is the thing being funded a harness, or the assets and governance around vendor harnesses?** The independent evidence says the loop is cheap (an agent in under 400 lines, first-party; `ampcode-how-to-build-an-agent`) and upkeep is not (Manus rebuilt its framework four times; Cognition rebuilt parts of Devin for one model; first-party). Geoff's direction: build, buy and layer all stay open; harness quality is not to be traded for independence.
2. **Which steps of intent shaping are standardised judgement, and which are open exploration?** Geoff agreed to classify by job step, not by user. Shaping an intent contains an open step (framing the problem), standardised steps (interrogation against a question set; risk classification against a taxonomy) and an accountable step (ratifying and accepting residual risk).
3. **Does a task-specific agent beat a skill in a general harness on intent shaping?** Geoff chose this as the first hypothesis to test. No evidence exists either way.
4. **Where does it run, and whose identity does it act under?** Local, our own containers, a vendor cloud, or an org platform; creator, requester, owner or service account. The policy owner decides the acceptable answers; the research only lists them.
5. **What is the record: the session, the artifact, or the project?** Ramp shares sessions; Stripe shares artifacts and keeps sessions private; Shopify's record is a public thread; nobody has a typed PM artifact or a shared project object.
6. **What default visibility will the organisation accept?** Public by default with fenced exceptions, team- or project-scoped, or private with a publish step. Regulated walls and works-council rules may settle it before user preference does.
7. **How would we know it worked?** Geoff's outcome is human time moved to discovery. The measures on the menu are a baseline time study, a completeness rate against an agreed spec standard, SME-labelled accuracy of risk classification, and review effort per output. Speed alone is contested (METR).

---

## 4. The options

The register holds 23 dimensions ([options/DIMENSIONS.md](../../options/DIMENSIONS.md)), each with options, evidence rows labelled by type, and unranked key questions. No winner is picked in any of them; where a lean is recorded it comes with what would change it. This story groups them into five banks so the film can show them at once. The eleven pattern classes beneath them come from the synthesis (P1 to P10) and the follow-up round (P11).

### 4.1 Loop and layer

*loop-source, harness-layering, runtime-location, model-provider-coupling, harness-upkeep, durability-substrate.*

Who supplies the agent loop: a vendor harness as is (Claude Code, Codex; mainstream); a vendor's harness SDK embedded in our own product (the Claude Agent SDK, Codex SDK, Cursor SDK; early-adopter; Ramp's April shape); a hosted harness (Claude Managed Agents, beta); a general framework (LangGraph, ADK, Microsoft Agent Framework; mainstream for workflow apps, and now with one production knowledge-work example in Stripe's Kai on Deep Agents, first-party); a fork of an open harness (Stripe on Goose; Goose now foundation-governed with a documented custom-distribution path, no named non-coding distribution); or an own loop on an own substrate (Ramp Laminar, Shopify Aquifer; first-party, well-resourced companies). The independent study of eleven production coding harnesses found none imports a general agent framework (independent; `arxiv-harness-engineering-eleven-systems`), scope coding only.

Whether there is a layer above: none; a local parallel-session manager (Conductor, Superset; developer throughput tools); a self-run horizontal meta-harness (Omnigent, alpha, one short independent hands-on account; `dataengineeringcentral-omnigent-hands-on`); a hosted multi-harness control plane (Warp Oz; GitHub's AI Controls over Copilot, Claude and Codex agents on GitHub.com, GA); a configuration layer in front of other harnesses (Stripe Kai projects); one substrate under many agent profiles, a layer below rather than above (Shopify Aquifer); or a governance-only agent control plane beside the harness (Microsoft Agent 365, ServiceNow AI Control Tower; the market's term, per Forrester). Independent evidence on the whole class is three items: one security test, one customer turn-off, one adoption check.

Where it runs: laptop; laptop as server (superseded at Ramp); our own containers running a vendor SDK (one subprocess per session, about 1 GiB RAM floor, first-party hosting guide); a vendor cloud VM (excluded for zero-data-retention, HIPAA and customer-managed-key organisations in Claude's case; first-party); customer-hosted runners under a vendor control plane; an org-deployed workspace; pooled devboxes. The durability choice under it (platform event log, framework checkpointer, workflow engine, durable object, or rerun from the repo) decides who writes recovery code and where state may live.

**Key questions, abridged.** Which steps need a coding-style harness and which are workflow-shaped? Who maintains the harness through model releases, at what recurring cost? Can build-versus-buy be deferred by keeping the shaping skill, spec standard and context as plain text any harness reads? What signals would tell us we had outgrown a vendor SDK, and can the first build make that a migration rather than a rewrite?

### 4.2 Capability and work shape

*capability-format-portability, capability-distribution-trust, remote-invocation-route, work-structure, activity-classification, intent-shaping-and-spec.*

How know-how is packaged: an always-on context file (most portable; an independent study found context files reduced task success and raised cost by over 20%, `arxiv-evaluating-agents-md`, against Vercel's vendor eval in favour); an open-standard skill (one format read by Claude Code, Codex, Copilot, Gemini CLI, Cursor and OpenCode; triggering unreliable); a harness-extended skill or packaged subagent (no shared format); a plugin bundle; an MCP server; or a deployed agent (own runtime, two systems to debug). Stripe reports that frontier-model skill selection degrades above about 150 skills (first-party, no eval published). Distribution runs from public registries (36.8% of 3,984 skills with some issue in Snyk's scan, vendor claim; 400 confirmed malicious of 150,108 in an independent scan) to org-governed registries with scan, review and version pins (PayPal, first-party) and telemetry-driven studios (Stripe Agent Studio).

How a general harness reaches a deployed agent: an in-process subagent; a human-triggered cloud handoff; a vendor background-agent API; an agent behind an MCP tool (Glean's own constraints: read-only, no human in the loop, finish in about 30 seconds because hosts time out; vendor claim); MCP with the Tasks extension for long jobs; A2A (now hosted beside MCP at the Agentic AI Foundation, GA in several enterprise agent platforms mostly at version 0.3, one named first-party production account, no native client in Claude Code, Codex or Copilot, SDK downloads about 22 times below MCP's; `pepy-a2a-sdk-downloads`, independent); an event or CI trigger; a chat reaction. The lean recorded in the register favours MCP over A2A for calls from general harnesses today, and says what would change it.

What agent shape fits the work: one general harness with structure added on demand (skills, hooks, plan mode; first-party guidance); a task-specific agent per job; a coordinator plus narrow specialists for a standardised job (Cloudflare's code review: 131,246 runs in a month at an average $1.19, humans forcing approval on 0.6% of merge requests; first-party); a deterministic wrapper round an agentic core (Stripe Minions); a workflow engine with embedded agents; constrain by default and loosen with evidence (68% of 86 deployed systems run at most 10 steps before a human intervenes; independent). Ramp and Stripe both consolidated from many agents to one agent with many skills, and Stripe retired 4,000 no-code micro-agents to do it (first-party). Classification: two classes, multi-axis task properties by job step, worker-desired agency, or usage-derived. Geoff: by step.

Who shapes intent and what counts as ready: PM-led bespoke; PM-led with a versioned shaping skill (Geoff's Action 4); agent-led interrogation and research (Ramp's shaping skill, vendor claim); prototype-first (Stripe Harbor, 12,000 prototypes, first-party); agent-originated. The spec: a narrative PRD; a short evidence-tied spec held to a completeness standard with evals (Geoff's Action 3); a prototype as spec; a canonical spec that absorbs risk mitigations and is re-assessed for residual risk (Geoff's risk-agent concept); a spec pushed straight to coding agents by a vendor tool.

**Key questions, abridged.** What are the universal questions every piece of intent must answer here, and where is the source for each? Can product and engineering agree one completeness standard, and can an eval judge it? How reliably do skills trigger in the harnesses our users run? When does a skill stop being enough: deterministic control, long-running work, per-user credentials, shared state, audit? Is the standard a rubric of judgement or a completeness checklist, and can SMEs label 20 past cases against it?

### 4.3 Sessions, identity and governance

*session-persistence-sharing, agent-identity-delegation, governance-control-plane, trust-privacy-defaults, agent-interface.*

Sessions: ephemeral and private (today's default); single-owner cloud with share by link (a snapshot, not live); live multiplayer on a per-session control plane (Ramp Inspect, Open-Inspect); shared sessions plus shared knowledge edits (Glass: 323 employees, 6,500 edits, vendor claim, no share rate published); a durable session log with a disposable harness (Managed Agents; Shopify's Postgres event log; Ramp's Postgres plus Temporal); long single-user sessions with shared artifacts (Kai, one session of 932 turns); one-shot isolated runs with a human at the PR; scheduled runs (personal, not team-shared, in Claude's case; "green does not mean the work succeeded"). Every shipped handoff is asymmetric.

Identity: creator's tokens; requester's account; service identity with scoped bundles; agent as co-author with a separate approver; environment-bounded with no human credentials; shared session executes as owner with authorship as attribution; user-delegated OAuth over A2A (Atlassian's Rovo gateway is the one example that acts as the signed-in user); vendor-provisioned service accounts (Codex); directory-issued agent identity (Entra Agent ID, where an independent test found 944 of 1,041 Graph permissions allowed and an owner able to escalate to Global Administrator; `compass-security-entra-agent-id-security`).

Governance: per-harness settings; vendor-native managed policy, now fail-closed and centrally delivered in all three major harnesses but per vendor; a gateway or proxy for model calls; a per-project meter and router (Ramp; the 30% saving is Router's own launch claim, not a Glass result); stateful session policies above harnesses (Omnigent; only for sessions launched through the layer); zero-ambient-access capabilities with an observation log and viewer re-check (Cloudflare OS, vendor claim); deterministic gates in the harness (hooks); the project as the unit of governance (Kai: a project owner sets the model, tool policies and human confirmation for 5 to 500 people); a verifiable audit log outside the harness (requested, not shipped anywhere found); deterministic policy at the tool gateway with a log-only rollout (AWS AgentCore, vendor claim). The follow-up round added the property that matters most in a regulated setting: whether a control fails open or closed, and whether its seam is the same for every harness and sub-agent.

Trust and privacy defaults: private with no sharing; private with share on demand; private draft then publish the outcome (blueprints, skills); team- or project-scoped; public by default org-wide with no private mode (River); public with fenced exceptions (inferred, no documented example); mixed by work family (Stripe: coding runs public, knowledge work private).

Interface: chat-native only (River); chat plus a companion web surface (River plus Quick); an own workspace (Glass, Cowork, Cloudflare OS); the IDE or CLI; one agent service behind several surfaces (Kai: web app by default, Slack, browser extension, API embedding). Both large adopters ended up with more than one surface.

**Key questions, abridged.** Which activities benefit from live co-presence versus a snapshot or a handoff? Which identity behaviour is acceptable for a shared agent, and must both the typist and the executor be logged? For an audit, which artefact is the record: the vendor's transcript, the control plane's telemetry, the gateway's policy log, or the workflow system's approval trail? What share of the target jobs touch data that cannot be open to the organisation? Is the learning in visibility itself, or in mining a corpus into skills, which private-by-default with an opt-in corpus could also capture?

### 4.4 Context and artifacts

*context-and-memory, artifact-and-project-structure.*

Context creation (a sub-choice added by the Stripe teardown's second pass): passive mining of work exhaust; owner-curated and verified knowledge that expires if unverified (Stripe's Trailhead, first-party); agent drafts with owner review; an interview-style elicitation agent (the least proven: LLM interviewers rarely probe); write-back from shipped work; or no dedicated capture. The recorded lean is capture as a by-product of work with owners verifying; a dedicated capture agent is unproven in form, and no company runs one.

Context: user-authored files; an offline-built profile, read-only in session (Glass in April; whether it survived the move to cloud sessions is unknown); shared organisation knowledge edited by users; a shared plain-text context repo near the code (Geoff's Action 5; the register records his lean towards it because it survives tool changes, and the counter-evidence on always-on context files); systems of record queried through connectors; a monorepo as the intelligence layer with nightly "dreaming" that rewrites skill files (Shopify, first-party); org context by default with personal sources opt-in (Kai).

Artifacts and projects: ad hoc and local (the baseline); repo-native conventions (Spec Kit, Kiro, ADRs; the independent review finds their file layouts diverge and few keep the spec authoritative after the first build; `fowler-bockeler-sdd-kiro-speckit-tessl`); platform-owned objects (Atlassian, Notion, Linear; many PMs already live there; Ramp uses Notion and Linear as the formal record); an inferred enterprise graph (Glean, vendor claim); a thin project descriptor that points at things (Cowork projects, Backstage, MCP resources; cheapest to test); workspace-defined typed artifact primitives with lifecycle and provenance (the biggest build; nothing like it exists to test); a hybrid of repo for long-form and platform for tracking with a descriptor tying them; the channel as the project and the thread as the unit (Shopify, with no stated home for non-code artifacts).

**Key questions, abridged.** How do product people actually store and find artifacts today, per type? What share of them, and of the reviewing roles, will work in Git for long-form artifacts? Would a thin descriptor plus MCP resources give agents enough structure, or do they need typed primitives to be reliable and reviewable? Who owns the schema?

### 4.5 People and outcome

*target-user, target-outcome, pm-agent-evaluation, sequencing, adoption-model.*

Users: Geoff has set them (own team plus beta users; internal tooling). Outcome: Geoff has set the aim (human time to discovery) and wants consistency, reduced review effort, organisational learning and speed as well. The measures on the menu: self-reported time saved (biased); throughput (self-reported, attribution unclear); blind-rated quality against a human baseline (no published rubric for PM jobs); consistency and reduced noise (measurable in code review); intent-factory key results (completeness rate against an agreed standard; share of well-specified intent delivered end to end); classification accuracy against SME labels (Geoff's risk-agent concept); within-user on/off comparisons (Stripe's sales figures, which an independent critique says confound adoption with ability); outcome reached per item rather than motion (Shopify's own warning that PR counts "measure motion, not remediation").

Sequencing: at job level, the register leans to bounded, reviewable jobs first (feedback triage, status, spec first draft plus gap review) because they have the most first-party use and checkable output; Geoff's reference job, intent shaping, sits across that line, which is why it is the right bake-off. At stage level: delivery factory first, shaping first, discovery first, or substrate first (Shopify's two-year monorepo bet before any agent). Adoption: product-led enablement (Glass); mandates, leaderboards and a proficiency ladder (Ramp's culture); decentralised authoring with central trust (PayPal, Dojo); an intake alias then skills (Cloudflare's rollout); visibility as enablement with the CEO in public (Shopify); one front door with no knobs, piloted with the most eager function then demoed company-wide (Kai: 296 to 5,000 users in about four weeks, first-party, from a company where 8,500 of about 10,000 staff already used LLM tools daily); guided creation with owned promotion (GitLab's adopter mapping).

**Key questions, abridged.** What would the sponsor fund against? How would we measure the shift of human time toward discovery (baseline time study plus pilot instrumentation)? Where is the bottleneck today: shovel-ready intent, build, review or release? Who would promote a skill from personal to canonical, and does the regulator accept owner-based control where the platform cannot enforce scope?

---

## 5. One hypothetical answer: Helm

**Helm is a concept to illustrate the potential. It is not the answer to the case, and the project does not recommend it.** It exists so the audience can see one path through the menu end to end, with every setting named by its register option, and then see the same job done two other ways (part 6). The name is a stand-in.

### 5.1 What Helm is, named by pattern

Helm is an **org-deployed product workspace on a swappable vendor loop**. In the taxonomy's terms it is P2 (a vendor harness SDK embedded in an own product) combined with P8 (shared, persistent sessions) and P10 (portable skills as the unit of packaging), running in the organisation's own cloud. It is **not a meta-harness** in the common horizontal sense: it does not wrap Claude Code, Codex and other CLIs under one session API. The word is reserved for that pattern. The one thing Helm borrows from that family is the lesson behind it: the loop sits behind an interface so it can be replaced, because Ramp replaced its loop within six months and said so.

The persona subagents, delegated fully for the standardised steps of intent shaping:

- **Researcher.** Reads the connected systems of record (tickets, calls, the research library, prior specs) and files typed evidence notes, each claim linked to its passage, with a list of what was read and what could not be found. The stories behind it: S01, S03, S12.
- **Dependency Mapper.** Finds the systems, teams and in-flight work the intent touches, from the ticket tool, the code host and the service catalogue, and files a dependency map with owners. Geoff's definition of the workload: "dependencies mapped".
- **Shaper.** Interrogates the human against the versioned shaping standard, one cluster of questions at a time, naming the source for each answer it already has, and drafts the canonical intent spec with open items marked. Geoff's Action 4; story S05 variant 3 and journey B.
- **Risk Advisor.** Classifies the spec component by risk against the organisation's taxonomy, proposes mitigations as numbered requirements, re-classifies after they are accepted, and routes anything off-taxonomy to a named subject-matter expert. Geoff's Intent Shaping document: specify, classify, augment.
- **Checker.** Runs the completeness standard and the quote and source check before any human review, and lists its findings against spec lines. Story S15; Torres's practice turned into a gate.

The human in the product role, whoever that is (PM, designer, engineer or analyst), steers at six points and nowhere else is required: states the intent in a line; answers the interrogation, or redirects it; resolves a trade-off the agents surface; accepts residual risk; ratifies with the reviewers; approves the hand-off. Everything between those points runs without them, and everything they do is attributed.

### 5.2 Every setting, with its register option

| Bank | Helm's setting | Register option it embodies | What the evidence says about it |
|---|---|---|---|
| Loop | Claude Agent SDK embedded, behind a loop interface | loop-source: embed a harness SDK, self-hosted (P2) | Vendor-grade loop, tools, permissions, subagents without writing them; Claude-only; API keys not subscriptions; we own sandboxing, session store, tenancy and scaling (first-party hosting guide). Ramp outgrew this shape in six months (first-party) |
| Layer | None above; the workspace is the product | harness-layering: no layer; agent-interface: own workspace plus chat front door | No uniform policy over other harnesses people may still run directly (register Q16) |
| Runtime | Sessions in our own cloud containers | runtime-location: self-host a vendor-SDK agent in our own containers | Data location and network under our control; about 1 GiB RAM per concurrent session as a floor; audit via the Compliance API only for the routes it covers (first-party) |
| Durability | Append-only session log in our database; sandbox as a tool | durability-substrate: event log; Shopify and Ramp precedents | Sessions survive worker churn; recovery and idempotency for side effects are ours to write |
| Upkeep | Vendor maintains the loop; a small internal team maintains the workspace, skills and standards | harness-upkeep: vendor maintains plus internal team | Behaviour changes without notice on the vendor side; on-call still needed (Ramp's caveat) |
| Packaging | One general agent; persona subagents as skill and subagent files; the shaping standard and risk taxonomy as plain text in a reviewed repo | work-structure: structure added on demand plus coordinator and narrow specialists; capability-format-portability: open-standard skill plus harness-extended skill | The standard survives a harness change (Geoff's Action 5); triggering and consistency on standard jobs unmeasured; subagent definitions are not portable |
| Distribution | Org-governed registry: scan, review, version pin, owned promotion | capability-distribution-trust: org-governed private registry | Review bottleneck; no reuse data published by any adopter |
| Work shape | Classified by step: framing open; interrogation and risk classification standardised with gates; ratification an accountable human commitment | activity-classification: multi-axis by job step | Axes are a synthesis, untested with users |
| Intent and spec | Agent-led interrogation against a versioned shaping skill; a short evidence-tied canonical spec that absorbs risk mitigations | intent-shaping-and-spec: agent-led plus versioned skill; canonical spec plus mitigations | Depends on context access; needs a standard that does not exist yet |
| Sessions | Persistent, project-scoped, joinable; share on demand; resume from any device | session-persistence-sharing: live multiplayer on a per-session store, share on demand | No independent evidence of shared sessions at scale; no share rate published anywhere |
| Identity | Session executes as its owner; authorship is attribution; viewers re-checked against their own access before they see evidence | agent-identity-delegation: shared session executes as owner; viewer re-check (Cloudflare OS design) | Owner impersonation risk unless both typist and executor are logged; re-check needs per-source permission mirroring |
| Governance | Project as the unit of policy; deterministic gates at ratify and hand-off; audit timeline kept outside the harness; per-project cost meter | governance-control-plane: project as governance unit (Kai); deterministic gates; verifiable audit log outside the harness | The outside-the-harness audit log is requested in the field but not shipped anywhere found; Kai's enforcement details are not public |
| Trust default | Private to the project; personal sources opt-in per session; publish the outcome (spec, decision record, skill revision), not the transcript | trust-privacy-defaults: project-scoped; private draft then publish | Loses "how people begin the work" (Shopify's claim for public); matches Bernstein's privacy-zone finding; fits regulated walls |
| Context | Connectors into systems of record plus a small curated plain-text context repo that each shaped intent writes back to | context-and-memory: connectors plus curated context repo | Geoff's lean; counter-evidence on always-on context files; governance of "evidence versus fact" unsolved |
| Artifacts | A thin project descriptor pointing at platform objects, plus typed slots the workspace defines for the shaping job only: intent, evidence, risk, dependency, decision, hand-off | artifact-and-project-structure: thin descriptor now; typed primitives where the job needs them; hybrid with platform tracking | Cheapest option to test plus the narrowest version of the biggest bet; schema ownership open |
| Users, outcome | Own team plus beta users; measured by a baseline time study, completeness rate against the standard, SME-labelled risk accuracy, review minutes per output | target-user, target-outcome, pm-agent-evaluation | No published rubric for any PM job; the standard and the labels have to be made first |
| Sequencing, adoption | Shaping layer alongside the delivery factory; product-led with owned promotion of skills; pilot with the most eager team, then demo | sequencing: shaping first alongside factory; adoption-model: product-led, guided creation with owned promotion | Stripe's ramp came from a company already at near-universal AI use; ours may not |

### 5.3 The flow, in brief

The prototype design ([02-prototype-design.md](02-prototype-design.md)) defines the screens, the motion and the demo paths. In outline, on the worked scenario from the user-story task (Sam, a PM, shaping "let finance approvers approve invoices in bulk"; Priya the engineering lead, Jo the designer, Alex from risk):

1. **Start.** Sam types one line of intent. Helm creates a project with typed slots (intent, evidence, risk, dependency, decision, hand-off), asks for an owner and reviewers, and shows which connectors are on and that personal sources are off. The project is private to its members.
2. **Fan out.** Researcher and Dependency Mapper run in parallel, in their own contexts. Each reports what it read and what it could not find; evidence notes land in the evidence slot with quote links; the dependency map lands with owners.
3. **Shape.** Shaper interrogates Sam against the shaping standard. Questions it can answer from evidence arrive pre-filled with their source; Sam confirms or corrects. The completeness meter fills. The draft spec grows beside the conversation, open items marked.
4. **Classify.** Risk Advisor lays the spec's components against the risk taxonomy. Two cells light up; mitigations appear as numbered requirements; one cell is off-taxonomy and is routed to Alex. Sam resolves a trade-off the mitigations force (bulk limit versus approver workload) and accepts the residual risk, with their name on it.
5. **Check.** Checker runs the completeness standard and the quote check. Three findings, each pointing at a spec line. Sam fixes two and overrides one, with a reason that is logged.
6. **Share and resume.** Priya, Jo and Alex are invited; each sees the section they are asked to review; the session still executes as Sam, and each viewer sees only the evidence their own access allows. Two days later Sam opens the project from a phone; the thread and the state are there.
7. **Ratify and hand off.** Sign-offs are recorded against the spec version. The hand-off packet (spec, evidence, decisions, dependency map, draft tickets, acceptance criteria) goes to engineering or a coding agent, with the engineering review that follows out of Helm's scope. A decision record is filed. The shaping standard receives a proposed revision from this run, for its owner to accept. The knowledge the run surfaced (the approver roles, the limit, who owns pricing constraints) is written back to the shared context with an owner to verify it and an expiry date: capture as a by-product of shaping, which is what the register's context-creation sub-choice leans to, not a separate interviewing agent (the least proven route). The audit timeline shows every allow, ask, deny and override, who typed and who executed, and what it cost.


### 5.5 The edges of the ecosystem

Geoff's direction (2026-10-24): assume hand-offs at the edges of a product-agent ecosystem. Helm is the product-agent part of a loop, and its edges are packets with an agent's mark on them. Candidates come in from **analyst agents** that watch the market, the data and the feedback (and from problem-discovery product agents that inform them); the human promotes a candidate to a project or declines it with a reason that goes back. Product agents shape and harden the intent until it is ready for **coding agents** or an engineering team. A **Shepherd** persona then tracks delivery against the spec and drafts the acceptance, with the Risk Advisor's governance review beside it, and the human accepts or sends the work back. After launch, **analyst agents** monitor business impact in market and **risk agents** monitor the controls around correct, well-managed execution; both reports land in the project's decision record, and one may become the next candidate at intake. A Stripe engineer's whiteboard, in a vendor-produced video from October 2026, names the stages: opportunity, problem, goal, intent, plan, with the plan then handed to a coding agent by one button (first-party; `youtube-notmybusiness-inside-stripe-ships-fast`, 12:24 to 12:31; [Stripe teardown, second pass](../competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md)). At Stripe people own the top of that chain through customer conversations and agents own the bottom: Orbit researches the intent and drafts the plan, a minion writes the code. The step from goal to intent is the one no Stripe agent owns, and it is the step Helm's personas are drawn for. None of these edge agents is Helm's; each has its own owner and reaches Helm over whatever route the register's remote-invocation options allow, which is itself an open key question (remote-invocation-route; agent-identity-delegation).

The evidence for the edges is the same first-party material as for the middle: Ramp's chain of specialised agents across the lifecycle (insight, define, build, review, test, coordinate; first-party), Stripe's federation of Kai, Harbor and Minions linked over MCP (first-party), Shopify's River opening one thread per security finding and checking back on them (first-party). Nobody has published an end-to-end loop with analyst, product, coding and risk agents handing packets to each other, so this is the assumption the film states and the resource request would test.

### 5.4 What Helm does not solve

Helm makes several bets the evidence cannot yet support, and the film says so on screen. A machine-checkable shaping standard and a risk taxonomy with applicability heuristics have to exist before Shaper, Risk Advisor and Checker can do anything; neither exists today. Viewer re-check across several systems of record needs permission mirroring per connector, which is uneven in the tools product teams use. An audit log outside the harness that an auditor can verify without trusting the harness is requested in the field and shipped nowhere. The "learn once" loop, where a run improves the standard for everyone, is described by Glass and Shopify in their own words and measured by nobody. And Helm's value over the two cheaper paths in part 6 is exactly the hypothesis Geoff asked to test first.

---

## 6. The same job three ways

Geoff asked for Helm to be compared against other implementations in the consideration set. The two the user-story task already derived in detail are the natural comparators ([S05 worked derivation](../user-story-mapping/worked-derivation-s05.md)), and a third, the horizontal meta-harness, is the one most often proposed for the organisational benefits. Same scenario, same reviewers, same forgotten decision.

**Path A: skills in Claude Code, plus a shared context repo.** The vendor harness as is (P1 plus P10). A team plugin carries the shaping skill, the risk taxonomy and the checker as skills; the project is a folder in a context repo with a short descriptor and frontmatter; reviewers read a pull request; the session is local and ephemeral.

**Path B: a deployed shaping agent as a service.** A platform team builds and runs a task-specific shaping agent (P6 plus P8), reached from the chat tool and from Claude Code over MCP; the project is an object the service defines; reviewers join the thread; the service has its own identity.

**Path C: a horizontal meta-harness over vendor CLIs.** Omnigent-style (P4): Claude Code and Codex run under one session API with shared sessions, policies and audit; the shaping skill and taxonomy are the same files as in path A; projects are whatever the underlying harness and repo provide.

| | A: skills in Claude Code | B: deployed shaping agent | C: horizontal meta-harness | Helm: org-deployed workspace on a vendor loop |
|---|---|---|---|---|
| What must exist before first use | A convention, a skill plugin, a context repo | A deployed service, connectors, an owner, a spec standard, an identity model | A server and runners, a policy set, each vendor CLI's login working under it | A workspace build, connectors, a session store, a spec standard, a registry |
| Who relays between reviewers and the agent | The PM, between the PR and a fresh session | Nobody; reviewers answer in the thread | The PM, unless reviewers join the shared session | Nobody; reviewers are in the project |
| What survives when the PM is away a week | The repo, not the reasoning (30-day deletion) | The thread and its history | The shared session, if the layer keeps it | The project: session, artifacts, decisions |
| Where it runs and under whose identity | The PM's laptop, as the PM | A service identity; reviewers' rights must be reconciled | Owner's credentials; a shared session executes as its owner | Our containers; executes as owner; viewers re-checked |
| Governance and audit | Per-harness settings and hooks; the Compliance API for covered routes; local prompts outside most logs | Per-run logs on the service; whatever the service builds | Policies that hold only for sessions launched through the layer; fail-open history, since fixed | Project-scoped policy; gates at ratify and hand-off; an audit timeline we have to build |
| Artifact and project structure | Folder convention, by discipline | Objects the service defines | None of its own | Thin descriptor plus typed slots for the shaping job |
| Harness and vendor dependence | Highest on the vendor product; nothing to run | Lowest on the vendor product; most to run | Independence from any one CLI, dependence on the layer tracking every CLI's changes | Dependence on one vendor loop, behind an interface |
| Upkeep | Skills and the repo; the vendor maintains the loop | A platform team on call | The layer and every vendor bridge (most Omnigent issues in October were bridge breaks) | A small team for the workspace and standards; the vendor for the loop |
| Enforcement | Advisory, unless hooks; a skill cannot enforce a gate | Enforced by the service | Enforced only through the layer's seams | Enforced at the gates the workspace owns |
| Main failure risk | Lost reasoning; relay burden; inconsistent triggering | Access scope; a service to run forever; one job per service | Bypassed when someone runs the CLI directly; the layer breaks on vendor changes | A product to maintain; a standard that must exist first; one vendor's terms |
| Evidence that this shape works for intent shaping | None; first-party only for PM skills in general harnesses | None; analogues are code review (Cloudflare) and compliance research (Stripe) | None; one short independent hands-on account of the layer itself | None; analogues are Glass (first-party) and Kai (first-party) |
| What it would test | Whether the standard and context alone give most of the value | Whether enforcement and persistence are worth a service | Whether governance above harnesses is worth the layer | Whether shared persistent projects and delegated personas move human time |

Three things stand out, and they are findings rather than a ranking.

First, the cheapest path and the most expensive one share their most important asset: the shaping standard, the risk taxonomy and the context repo as plain text. That asset can be built and tested first in path A, in weeks, and carried into any of the others unchanged. It is what Geoff's Action 5 argued for, and it is the only part of any path that survives a change of harness, vendor or terms.

Second, the paths differ most on what they enforce and what they persist, which are exactly the properties a regulated setting cares about and exactly the ones the vendor harness does not give by default. Path A cannot enforce a gate or keep a session; B and Helm can, at the price of something to run; C enforces only what passes through its seams.

Third, nobody has compared any two of these on a job like intent shaping. The user-story task's recommendation stands: run the S05 pair as clickable prototypes with five to eight product people, and the bake-off below with a human-scored rubric. Until then, Helm is a picture of what the better paths could feel like, not evidence that they do.

---

## 7. What a resource request would fund

The request funds answers first, not a build. Grouped by instrument, with the dimensions each informs. The full list is in the synthesis ([G.2](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#g2-what-a-resource-request-would-need-to-fund-to-answer-these)) and the register's key questions.

**The intent-shaping bake-off.** One reference job, three to five real intents from the team, built as: a portable skill in Claude Code with the context repo (path A); a deployed shaping agent reached over MCP (path B); a workflow with deterministic gates; and, if funded, a thin workspace slice (Helm's shape and classify flow). A no-agent baseline. Scored by a human rubric and by SME labels on the risk classification. It answers Geoff's first hypothesis and informs loop-source, capability format, work structure, review and autonomy, and intent-shaping-and-spec. Prerequisite work it also forces: writing the shaping standard and the risk taxonomy, and labelling 20 past cases.

**A short interview round.** Six to eight walkthroughs of how product people here actually keep artifacts, sessions and context; three to five reviewers walking through a real review; a card sort of the jobs map. It settles the baseline the stories rest on (artifact-and-project-structure, context-and-memory, target-user).

**Policy-owner answers.** Audit evidence required for agent-shaped intent; retention and residency; which identity behaviour is acceptable for a shared session; whether public-by-default is permitted at all; which gates must be deterministic. These are decisions, not research, and they move more dimensions than any prototype.

**Trials and adopter interviews.** A two-week Omnigent trial scripted against its own issue tracker (fail-closed behaviour, the same policy across Claude Code, Codex and sub-agents, audit reconstruction, shared-session credentials); a one-day Cloudflare OS deploy in a pilot account with a security review; a trial export of each vendor's compliance stream into our own log; interviews with Ramp, Stripe, PayPal, Cloudflare and Databricks on upkeep headcount, reuse and share rates, and what triggered Ramp's switch of loop.

**A reversible first step.** Whatever is built first, build it with a revisit point and criteria, because the one well-documented adopter changed two of its answers inside six months.

---

## 8. What we do not know, and the close

The research base is 511 source notes, and most of what matters in them is first-party. There is no independent post-mortem of a shared multi-user session, no cost-of-ownership account of an own harness from a company that is not an AI product company, no quality or latency data for any agent reached over MCP, no evaluation of any PM agent on a PM job, and no comparison of a task agent against a skill. The architecture write-ups from Ramp, Stripe and Shopify are specific enough to learn from. Their outcome numbers are marketing until someone else measures them.

That is the case. The factory sped up. The bottleneck moved to the shaping of intent and the review of what the factory makes. Product people already use agents, in private, inconsistently, with no record that survives the month. A workspace like Helm shows what it could feel like when the standardised steps are delegated to named personas, the record persists and is shared on purpose, the organisation's standards are enforced at the gates, and the human's time goes where their judgement is needed. Whether that is worth building, and in which of the shapes on the menu, is what the resource request would find out.

---

## Appendix A. Claim check

Every factual claim, number and quote used in this story and the film, checked against the current, post-audit source note on 2026-10-24. Evidence type is the note's frontmatter label unless stated. "Checked" means the figure or quote was found in the note (or its transcript) as written here.

| # | Claim as used | Source note | Evidence type | Checked |
|---|---|---|---|---|
| 1 | Stripe Minions: over 1,000 merged, fully agent-written, human-reviewed PRs a week (March 2026); 1,300 in a later post | stripe-minions-one-shot-coding-agents; stripe-minions-part-2 | first-party | yes |
| 2 | Geoff's document relays "about 7,000 a week (~30% of merges) by August" | geoff-building-accelerating-intent-factory | relayed vendor claim | yes; not used as a figure in the narration |
| 3 | Ramp Inspect: 75% of PRs; about 1,000 PRs a month from non-engineers | lenny-podcast-geoff-charles-product-when-coding-solved | first-party | yes |
| 4 | Review Buddy handles 93% of PRs | same | first-party (vendor claim in register) | yes; not used in narration |
| 5 | Gadget (not Glass) credited with answering 85% of questions asked to PMs | same, transcript 13:01; PM audit | first-party | yes; corrected attribution applied |
| 6 | Shopify: about one in eight merged PRs authored by River, reviewed by people (week to 2026-05-09); 5,938 employees in 30 days | x-tobi-learning-on-the-shop-floor | first-party | yes |
| 7 | River's share of merged mobile PRs 6% to 61% (reported 2026-10-22; window not stated) | shopify-engineering-remote-dev | first-party | yes |
| 8 | River threads 35,418 to 121,804 a month; same-thread links 61,680 to 171,853 (Mar to Sep 2026) | x-tobi-river-floods-shopify-chart | first-party | yes; not used in narration |
| 9 | Merge rate 36% to 77% in two months, measurement undefined | x-tobi-learning-on-the-shop-floor | first-party | yes; not used in narration |
| 10 | "The Models are Good Enough" | x-sebgoddijn-glass-article | first-party | yes (title) |
| 11 | "the agent will not be the interesting part" in two years | shopify-engineering-under-the-river; River teardown | first-party | yes (teardown quotes it) |
| 12 | PM job "is really the same as it always was" (02:30) | lenny-podcast-tamar-yehoshua-roles-expanding | first-party | yes |
| 13 | Atlassian has not figured out how to measure outcomes (19:35 to 20:35) | same; PM brief | first-party | yes |
| 14 | Lenny survey, 1,750: PRDs 21.5%, user research 4.7%, 63% of PMs save 4+ hours a week | lennys-newsletter-ai-tools-overdelivering-results | independent, self-selected | yes |
| 15 | Microsoft 885 PMs: 62% daily; drafting 73%, research 22%, prototyping 12%; specs held back; self-report vs telemetry Spearman 0.37 | arxiv-pm-delegating-work-to-genai | first-party (one company) | yes |
| 16 | Claude Code deletes local transcripts after 30 days by default; users report losing decisions | itdaily-claude-code-30-day-transcript-deletion | independent | yes |
| 17 | Atlassian has three objects called a project; no vendor graph has a spec, insight or decision type | atlassian-jira-space-definition, atlassian-confluence-space-definition, atlassian-teamwork-graph-object-types; research-artifacts-standardization | first-party; task research | yes (per stories S16, S17 and the user-story audit) |
| 18 | Years of goals, 1 to 2 sprints of shovel-ready intent; refinement bespoke; context scattered; PRDs vague | geoff-building-accelerating-intent-factory | first-party position piece (filed as anecdote) | yes; labelled a framing not a measurement |
| 19 | Ramp's agent reads 90 days of tickets in about 8 minutes | same (relayed) | vendor claim, relayed | yes |
| 20 | "not moving money without human review" (Stripe) | same (relayed) | vendor claim, relayed | yes |
| 21 | "We still require a human PR reviewer, which is now becoming a big bottleneck" (Thawar, April 2026) | bvp-inside-shopifys-ai-first-engineering-playbook | first-party | yes |
| 22 | "slop grenades" | fs-knowledge-project-tobi-lutke-ai-agents | first-party | yes |
| 23 | About 540 claims re-checked, about 110 corrections; no independent controlled evaluation of any PM agent; no agent-vs-human quality comparison | 00-brief (research-pm-agents-jobs-to-be-done, audited) | task deliverable | yes |
| 24 | No controlled comparison of a task agent vs a skill in a general harness; the central gap | 01-synthesis A and D.17 | task deliverable | yes |
| 25 | METR: AI-allowed tasks 19% slower; developers believed about 20% faster; 16 developers, 246 issues, early-2025 tools | metr-early-2025-experienced-developer-rct | independent | yes |
| 26 | Torres: about 30% of direct quotes wrong or missing (ChatGPT) | producttalk-customer-interview-analysis-ai | first-party practitioner test | yes |
| 27 | Stanford/Science: 11 models affirmed users about 49% more often than humans; users trusted sycophantic answers more | stanford-cheng-sycophantic-ai-science-2026 | independent (read via summaries) | yes |
| 28 | Vercel: skill never invoked in 56% of cases | vercel-agents-md-outperforms-skills | vendor claim | yes |
| 29 | SkillsBench: +16.2pp average; 16 of 84 tasks worse; Codex often ignored skills | arxiv-skillsbench | independent | yes (text figure; Figure 2 says +12.66pp) |
| 30 | Answer.AI: 3 of 20 tasks succeeded; infeasible tasks pursued | answerai-thoughts-month-with-devin | independent, Jan 2025 | yes |
| 31 | Glass April: desktop app on the Claude Agent SDK, laptop as server; October: Laminar, own harness, six weeks, disposable cloud workers, "a weird blip"; engineers still on call; build "marginal" | ramp-builders-building-laminar; x-sebgoddijn-glass-article; Glass audit | first-party | yes |
| 32 | Anthropic: subscription OAuth blocked outside official clients 2026-01-09; legal demands and OpenCode removal 2026-03-19; API keys never blocked | falcao-anthropic-claude-access-crackdown | independent | yes |
| 33 | Omnigent: 13 advisories in four months, 4 critical; policies failed open (server error, in-process shell, sub-agents); fixed within days with deny-by-default | github-omnigent-security-advisories; securelayer7-cve-2026-62676-omnigent | first-party; independent | yes |
| 34 | "Meta-harness" used for at least six shapes; Anthropic used it for Managed Agents (2026-04-08) before Databricks (2026-06-13) | 01-synthesis A; codepick-meta-harness-guide; anthropic-engineering-scaling-managed-agents; databricks-omnigent-meta-harness-launch | task deliverable; independent; first-party | yes |
| 35 | Syracuse disabled Cowork org-wide over audit coverage | syracuse-claude-cowork-security-considerations | independent | yes |
| 36 | Compliance API covers Cowork and Claude Code from 2026-08-26; excludes web, Platform, Bedrock, Vertex, Foundry | anthropic-compliance-api-cowork-claude-code | first-party | yes |
| 37 | Cursor: follow-ups run as the creator; staff: intended | cursor-forum-team-followups-act-on-behalf | anecdote plus staff reply | yes |
| 38 | Claude Tag: channel membership becomes the IAM boundary | tenable-claude-tag-slack-access-model | independent | yes |
| 39 | Omnigent maintainers: "A shared session always executes as its owner"; SciChart built and removed per-message identity | github-omnigent-identity-audit-issues | anecdote plus maintainer first-party | yes |
| 40 | "River only works in the open. No direct messages." | shopify-engineering-under-the-river | first-party | yes |
| 41 | "Some questions that would have been asked in a DM just don't get asked"; "isn't free" | x-tobi-river-reaction-to-shop-floor-post | first-party | yes |
| 42 | Bernstein: broad visibility bred hiding; curtained lines up 10 to 15% defect-free units per hour | asq-bernstein-transparency-paradox | independent (2009 field experiment) | yes |
| 43 | Kai: sessions private; personal sources opt-in per session; projects 5 to 500 people set policy | howiai-stripe-kai-krishnamurthy; stripe-meet-knowledge-ai-platform | first-party | yes |
| 44 | An agent in under 400 lines | ampcode-how-to-build-an-agent | first-party | yes |
| 45 | Manus rebuilt its framework four times; Cognition rebuilt parts of Devin for Sonnet 4.5 | manus-context-engineering-lessons; cognition-devin-sonnet-45-rebuild | first-party | yes |
| 46 | 0 of 11 production coding harnesses import a general framework | arxiv-harness-engineering-eleven-systems | independent (coding scope) | yes |
| 47 | Kai on LangChain Deep Agents with a Stripe harness layer; "1.5 people over two weeks" for v0 | stripe-meet-knowledge-ai-platform; howiai-stripe-kai-krishnamurthy | first-party | yes (teardown) |
| 48 | One short independent hands-on account of Omnigent; shared-server deploy failed | dataengineeringcentral-omnigent-hands-on | independent | yes |
| 49 | Agent 365 "governs; it does not host or run agents"; Forrester's "agent control plane" category | microsoft-fasttrack-agent-365-lifecycle-atlas; forrester-agent-control-planes-standards-stack | first-party; independent analyst | yes (follow-up 6) |
| 50 | Agent SDK self-hosting: about 1 GiB RAM per concurrent agent as a floor | anthropic-agent-sdk-hosting | first-party | yes (register row) |
| 51 | Claude Code cloud sessions excluded for ZDR, HIPAA, CMEK orgs | anthropic-claude-code-cloud-sessions | first-party | yes |
| 52 | ETH: context files reduced task success and raised cost over 20% | arxiv-evaluating-agents-md | independent | yes |
| 53 | Stripe: skill selection degrades above about 150 skills | howiai-stripe-kai-krishnamurthy; langchain-how-stripe-built-kai-deep-agents | first-party; vendor claim | yes (teardown) |
| 54 | Snyk: 36.8% of 3,984 skills with any issue; 13.4% critical; 76 malicious | snyk-toxicskills-study | vendor claim | yes |
| 55 | MalSkills: 400 confirmed malicious of 150,108 across 7 registries (v2) | arxiv-malskills | independent | yes |
| 56 | Glean agents as MCP tools: read-only, no human in the loop, finish in about 30 seconds | glean-agents-as-mcp-tools | vendor claim | yes |
| 57 | A2A: joined AAIF Aug 2026; one named first-party production account (Eon, 3 of about 20 agents); no native client in Claude Code, Codex or Copilot; a2a-sdk 12.2M vs mcp 273.9M downloads in 30 days (about 22x) | aaif-a2a-joins-aaif; aaif-eon-a2a-into-production; github-claude-code-issue-28300-a2a; github-openai-agents-sdk-a2a-prs-declined; pepy-a2a-sdk-downloads | vendor claim; first-party; anecdote; first-party; independent | yes (follow-up 1) |
| 58 | Cloudflare code review: 131,246 runs (2026-03-10 to 04-09), average $1.19, break-glass 0.6% of MRs, about 1.2 findings per review | cloudflare-ai-code-review-opencode | first-party | yes |
| 59 | 68% of 86 deployed systems run at most 10 steps before a human intervenes | arxiv-measuring-agents-in-production | independent | yes |
| 60 | Ramp consolidated to one agent with many skills (four versions of the same agent); Stripe retired 4,000 no-code agents | pragmatic-engineer-ramp-lessons-new-ai-product; stripe-meet-knowledge-ai-platform | first-party | yes |
| 61 | Harbor: 12,000 prototypes, 3,000+ people since May 2026 | stripe-harbor-ai-prototyping | first-party | yes |
| 62 | Glass: 323 employees, 6,500+ edits; 350+ skills; 700 DAU within a month | x-eglyman-introducing-glass-learn-things-once; x-sebgoddijn-glass-article; x-geoffintech-ai-pilled-article | vendor claim; first-party; first-party | yes |
| 63 | Kai: one session of 932 turns; sharing on the roadmap | stripe-meet-knowledge-ai-platform; howiai-stripe-kai-krishnamurthy | first-party | yes (teardown) |
| 64 | Scheduled tasks personal, not team-shared; "green does not mean the work succeeded" | anthropic-claude-code-scheduled-tasks | first-party | yes (register row) |
| 65 | Atlassian Rovo A2A gateway acts as the signed-in user | atlassian-rovo-a2a-gateway-docs | first-party | yes (follow-up 1) |
| 66 | Compass: 944 of 1,041 Graph permissions allowed; owner escalation to Global Administrator | compass-security-entra-agent-id-security | independent | yes |
| 67 | Ramp's 30% saving is Router's July launch claim, not a Glass result | x-ramp-router-launch-posts; Glass audit | vendor claim | yes |
| 68 | Cloudflare OS: zero ambient access, Gatekeepers, viewer re-check | cloudflare-os-announcement | vendor claim | yes (register row) |
| 69 | AgentCore Policy: Cedar at the gateway, outside the reasoning loop, log-only mode | aws-agentcore-policy-evaluations-blog | vendor claim | yes (follow-up 6) |
| 70 | Vendor-native managed policy now fail-closed in Codex, Copilot and Claude Code, per vendor | openai-codex-managed-configuration; github-copilot-enterprise-managed-settings; anthropic-claude-code-plugins-org-management | first-party | yes (follow-up 4) |
| 71 | Shopify Quick: 50,000+ internal sites, no owners; non-code artifacts have no stated home | shopify-engineering-quick; River teardown | first-party | yes |
| 72 | Spec-driven tools' file layouts diverge; few keep the spec authoritative | fowler-bockeler-sdd-kiro-speckit-tessl | independent | yes (stories S11, S18) |
| 73 | Ramp uses Notion and Linear as the formal record (11:43) | lenny-podcast-geoff-charles transcript | first-party | yes |
| 74 | Stripe sales figures compare the same sellers' Kai weeks with non-Kai weeks; independent critique on selection | stripe-meet-knowledge-ai-platform; aifounders-stripe-kai-dont-copy-sales-numbers | first-party; independent | yes |
| 75 | "PR count and green-branch count measure motion, not remediation" | shopify-engineering-river-vulnerability-remediation | first-party | yes (teardown) |
| 76 | Kai ramp: 296 to 5,000+ users in about four weeks; 83% weekly; 8,500 of about 10,000 staff already used LLM tools daily (Oct 2025) | stripe-meet-knowledge-ai-platform; latentspace-emily-sands-stripe | first-party | yes |
| 77 | Shopify: substrate first, two years of monorepo and Nix before the agent | shopify-engineering-under-the-river | first-party | yes (teardown) |
| 78 | Agentforce: about 12% of customers with deals, about 6% paid | salesforceben-agentforce-adoption | independent | yes |
| 79 | Geoff's answers of 2026-10-24: reference workload, users, outcome, classify by step, first hypothesis, regulated and audit, terms by common usage, independence a benefit not a goal | 01-synthesis "Geoff's answers"; DIMENSIONS.md "Geoff's answers" blocks | first-party (Geoff) | yes |
| 80 | Baseline: inconsistent Claude Code use, poor artifact management; PRD-in-repo trend | user-story-mapping README and audit (tagged [G]) | Geoff's statement, not independently evidenced | yes; labelled as his |
| 81 | 511 source notes in the library | research/sources count on 2026-10-24 | count | yes |
| 82 | Product Focus: 85% of PMs validate AI output with their own expertise | productfocus-industry-survey-2026 | vendor survey (PDF read in audit) | yes; not used in narration |
| 83 | Claude Code hooks are deterministic where CLAUDE.md is advisory | anthropic-claude-code-best-practices | first-party | yes |
| 84 | Auto-approve drifts from about 20% (new users) to over 40% (experienced) | anthropic-measuring-agent-autonomy | first-party | yes; not used in narration |
| 85 | Meta piece by Nikhyl Singhal, cross-posted, not sponsored; PRD became a paragraph plus prototype | lenny-newsletter-meta-chawla-pm-leader-agents | anecdote (first-person) | yes; not used in narration |
| 86 | Stripe whiteboard chain: opportunity, problem, goal, intent, plan; code as the one-button hand-off to a minion; "happening a lot more in Orbit now" (12:22 to 12:33); people own the top, agents the bottom | youtube-notmybusiness-inside-stripe-ships-fast (2026-10-22) | first-party, vendor-produced | yes |
| 87 | Context creation: Trailhead verify-or-archive; no dedicated capture agent at Stripe, Shopify or Ramp; LLM interviewers probe in 4.9% of turns; lean to capture as a by-product | DIMENSIONS.md context-creation sub-choice; stripe-sessions-2024-10x-engineer-panel; arxiv-interviewbot-mllm-led-interviews | first-party; independent | yes (register; notes filed by the Stripe teardown) |

Corrections carried from the audits and applied here: Glass runs on Laminar, not the Agent SDK (October 2026); the 30% saving is Router's claim; Gadget, not Glass, answers 85% of PM questions; Torres's three figures are credited to their own pages; the Meta piece is by Nikhyl Singhal and not sponsored; "AI summaries miss 20 to 40%" and the CleverX fabricated-quote warning existed in no source and are not used; S02's Ramp figure is feature-request capture, not categorisation; the Lenny/Cursor note is not evidence of PRDs kept in repos.

## Appendix B. Concept map (terms by common usage)

- **Harness.** The software around the model: the loop, tools, context management, permissions, sandbox, memory. "The harness, not the model, limits real-world value" is the project's first theme.
- **Meta-harness (horizontal sense).** A layer that launches, governs or shares several vendor harnesses while leaving the loop to them: Omnigent, Warp Oz, Nx Polygraph. Competing usages recorded and not adopted: Anthropic's use for Managed Agents; the Stanford optimiser sense.
- **Org-deployed agent workspace (our coined term, P5).** A platform the organisation deploys that gives each employee a persistent, governed workspace running the platform's own agent: Cloudflare OS; at enterprise scale, the "agent platforms" (Gemini Enterprise, Frontier, Glean, Writer).
- **Agent control plane (P11, Forrester's and Microsoft's term).** Governance-only: registry, identity, policy, audit over agents that run elsewhere: Agent 365, ServiceNow AI Control Tower.
- **Agent behind MCP (practitioner usage).** A deployed agent exposed as an MCP tool to any host.
- **Intent shaping (Geoff's definition).** Shaping high-level intent against enterprise constraints into intent ready to hand to engineers or coding agents.
- **Persona subagent (this story).** A named specialist, defined as a skill plus subagent file, to which a standardised step of a PM job is fully delegated. Not a "PM agent" persona in the register's sense (one agent for the whole role).
- **Helm.** The notional workspace used to illustrate the hypothetical answer. A concept, not the answer, and a stand-in name.

## Appendix C. Sources

Task deliverables drawn on: the runtime-patterns synthesis and its six tracks and five follow-up reports; the options register; the Ramp Glass teardown and audit; the Shopify River and Stripe knowledge-agents teardowns; the PM jobs brief, map and audits; the 18 user stories, recipe and S05 derivation; Geoff's two intent documents. Source notes cited are listed in Appendix A by slug; each is in `research/sources/` with a link to the original.
