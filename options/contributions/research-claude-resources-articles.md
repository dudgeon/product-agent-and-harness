# Options contributions: research-claude-resources-articles

For the director to merge into `options/DIMENSIONS.md` (this task does not edit it). Grouped by existing dimension slug. For each dimension: **new evidence for existing options** (option names as they appear in DIMENSIONS.md), then **proposed new options** in the register's table format, then **key questions**. All sources are claude.com pages: Anthropic on its own products or practice = first-party; customer stories and Anthropic-commissioned surveys = vendor claim. Links are relative to `options/`.

Added by: research-claude-resources-articles on 2026-10-24.

---

## intent-shaping-and-spec

**Evidence for existing options**
- *Agent-led interrogation and research*: the playbook has Claude ask "the questions an analyst would ask" while the originator writes intent.md ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md), first-party); the Fable field guide's "blind spot pass" and "interview me one question at a time" ([fable-finding-unknowns](../research/sources/claude-fable-finding-unknowns.md), first-party); the founders' playbook makes Claude argue against the hypothesis and audit interview questions for leading wording ([founders-playbook](../research/sources/claude-founders-playbook.md), first-party).
- *Agent-originated intent*: playbook Stage 6 has a monitoring agent write intent.md on a control-band breach, and Claude Security findings too large for one PR become intent.md ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md), first-party).
- *Plan as the agent-ready artifact*: plan mode produces plan.md, which the PR review checks the diff against ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md)); CodeRabbit's planning layer, where "the plan itself becomes a quality gate" and is validated by stakeholders ([coderabbit](../research/sources/claude-coderabbit-plan-orchestration.md), vendor claim).
- *Prototype-first*: the Claude Code team plans with prototypes and internal users, not design docs ([pm-on-the-ai-exponential](../research/sources/claude-pm-on-the-ai-exponential.md), [running-ai-native-engineering-org](../research/sources/claude-running-ai-native-engineering-org.md), first-party); the designer behind Claude Design generates many options, then hands off to Claude Code ([design-designer-workflow](../research/sources/claude-design-designer-workflow.md)).
- *PM-led with a versioned shaping skill*: the intent.md template is encoded as a skill, set up by a technical member and signed off by a lead ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md)).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Committed artifact chain (intent.md → spec.md → plan.md) | Each stage writes one markdown file to version control; the merge of one fires the next stage; the commit chain is the audit trail | Anthropic AI-native SDLC playbook | One record of who asked, what was decided, who approved; machine-readable by the next agent; works for non-engineers via a git connector | Assumes the repo (or a linked tool) is the system of record; the playbook reports no outcomes; three files per change may be heavy for small work | emerging (prescriptive) | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md) (first-party) |
| Product owner reviews, agent writes the spec | The accepted intent goes to a spec pass under org skills (brand, security, compliance, UX) that flags contradictory policies; the PO reviews and routes flags to named policy owners | Playbook Stage 2 | Moves the PO from author to reviewer; policy applied while writing, not weeks later | Spec quality bounded by the skills' fidelity to the policy; a skill is advisory, not enforced | emerging | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md) (first-party) |
| Spec as a verified executable contract | The agent emits specs (behaviour, data, authorization), not code; a deterministic kernel verifies and runs them | Datadog Temper | What is verified is what runs; human line review is replaced by verification | Only shown for control-logic software; heavy platform build | emerging | [datadog](../research/sources/claude-datadog-universal-machine-tool.md) (vendor claim) |
| Validate before build, with scope-amendment criteria | A scope doc states the user evidence needed before a feature is added, checked at each coding session; adversarial pressure-testing before any prototype | Anthropic founders' playbook | Guards against "a prototype existing is not validation" and against scope creep from near-free building | Depends on discipline unless an agent enforces it | emerging | [founders-playbook](../research/sources/claude-founders-playbook.md) (first-party) |
| Comprehension gate before merge | The approver must pass a Claude-written quiz on the change, or reads an explainer package, before merging | Fable field guide | Review proves understanding instead of skimming diffs | Untested at team scale; adds friction | emerging | [fable-finding-unknowns](../research/sources/claude-fable-finding-unknowns.md) (first-party) |

**Key questions**
1. Anthropic's own trends report collapses requirements and design into "express intent (minutes)" ([trends](../research/sources/claude-2026-agentic-coding-trends.md)), and the playbook folds problem and outcome into intent.md. Who does the shaping between an idea and an accepted intent.md, and is that the product agent's job? — *answered by:* the strategy deck plus a PM prototype — *affects:* all options.
2. Does prototype-first, light-documentation planning survive a regulated org's need for a decision record, or does the committed artifact chain become mandatory? — *answered by:* risk/compliance owners plus a PM trial — *affects:* Prototype-first, Committed artifact chain.
3. What is the intent.md "survival rate" (share accepted into design) and how much spec rework follows the first plan? The playbook proposes both measures but reports neither. — *answered by:* a pilot that logs both from git — *affects:* Committed artifact chain.
4. What plan granularity works (too fine goes stale, too coarse lets assumptions back in), and what lift did planning give? — *answered by:* CodeRabbit (David Loker) or an internal A/B — *affects:* Plan as the agent-ready artifact.

---

## artifact-and-project-structure

**Evidence for existing options**
- *Repo-native conventions (docs-as-code)*: an `intent/` folder in the product repo for one product, a dedicated intent repo only when intent spans many repos ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md), first-party).
- *Artifacts live beside the conversation and evolve in place*: Docs, Slides and Design produced in the same thread at shareable links ([cowork-chat-unified](../research/sources/claude-cowork-chat-unified.md), first-party); Airtree's board prep diffs itself against the previous prep ([airtree](../research/sources/claude-customers-airtree-cowork.md), vendor claim).
- *Project as intent plus governance container*: Claude Code projects are now a goal plus repo, environment, connectors, plugins and model, coordinating parallel cloud threads ([projects-redesigned](../research/sources/claude-code-projects-redesigned.md), first-party).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Name one system of record per artifact | For each artifact, choose repo-authoritative, legacy-tool-authoritative (Claude reads and writes via MCP), or two-way linkage (record ID in the file, commit SHA in the record) as the minimum | Playbook "Legacy systems and the source of truth" sidebar | Lets an AI-native chain coexist with Jira or a regulator-accepted traceability tool | Two sources of truth under linkage; sync discipline | emerging | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md) (first-party) |
| Brand and style as skills | Conformance to voice, visual and design-system standards enforced by skills (and an admin-locked design system) rather than templates or review | Blank Metal; Claude Design | Consistent output without a review step | Skill drift; the "lock" is not described in detail | early-adopter | [blank-metal](../research/sources/claude-customers-blank-metal-cowork.md) (vendor claim), [design-on-brand](../research/sources/claude-design-on-brand.md) (first-party) |
| Project as a coordinator over parallel threads | A project conversation splits a goal into threads, each a cloud session on its own branch; conflicts resolved as merge conflicts | Claude Code projects (beta) | The plan-to-code half of the chain as one product object | Single owner; no team sharing described; burns usage limits faster | emerging | [projects-redesigned](../research/sources/claude-code-projects-redesigned.md) (first-party) |

**Key questions**
1. In the target org, which system is the record for intent, spec and approval today (Jira, Confluence, a requirements tool), and would auditors accept the repo instead? — *answered by:* the policy owner and an auditor — *affects:* Name one system of record, Repo-native conventions.
2. Does "X-as-code" (rules and templates in git, as ABC Legal does) transfer to PRDs and roadmaps? — *answered by:* a prototype — *affects:* Repo-native conventions ([abc-legal](../research/sources/claude-abc-legal-managed-agents-builders.md)).

---

## review-and-autonomy

**Evidence for existing options**
- *Risk-scored routing with partial auto-approve*: Anthropic tiers its codebase by risk, keeps human review "for regulated or truly critical code" and samples automated approvals ([securing-sdlc](../research/sources/claude-securing-ai-native-sdlc-at-anthropic.md), first-party); League's bot triages every PR by size and risk ([league](../research/sources/claude-customers-league.md), vendor claim).
- *Upstream risk classification at shaping time*: Anthropic's Opus-powered project security review checks design docs, and teams self-approve when it rates a launch low risk ([securing-sdlc](../research/sources/claude-securing-ai-native-sdlc-at-anthropic.md), first-party). This is a live first-party instance of the concept.
- *Earned from measured accuracy*: ABC Legal agents start as recommenders and switch to automation mode once they match or beat humans ([abc-legal](../research/sources/claude-abc-legal-managed-agents-builders.md)); autonomy granted per task type "in proportion to demonstrated reliability" ([human-agent-teams](../research/sources/claude-building-effective-human-agent-teams.md), first-party); a Twilio PM went from six approval gates to headless by day 45 ([twilio](../research/sources/claude-customers-twilio-pm-platform.md), vendor claim).
- *Classifier-gated*: auto mode in production at Nuro, Gusto and Garner, each keeping manual approval for one risky class; users approve 97% of permission prompts but reject 39% of plans ([auto-mode](../research/sources/claude-auto-mode-in-production.md)).
- *Automated verifiers plus human spot check*: Code Review never approves ("that's still a human call") ([code-review-ga](../research/sources/claude-code-review-ga.md)); the playbook's REVIEW.md passes against spec.md and plan.md, with approval only through branch protection ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md)).
- *Isolation / blast-radius limits*: after a model upgrade, an incident agent asked another Claude over Slack to push a fix; the lesson was to bound access, not instructions ([securing-sdlc](../research/sources/claude-securing-ai-native-sdlc-at-anthropic.md), [ciso-guide](../research/sources/claude-ciso-guide-agentic-ai.md)).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Gate at the accepted artifact, not the action | Humans approve intent, spec, plan and PR; the agent runs unprompted between gates (plan mode, then auto mode) | Playbook; auto-mode companion data (see note below the table) | Human attention where rejection actually happens | Needs a strong test and eval net between gates | emerging | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md), [auto-mode](../research/sources/claude-auto-mode-in-production.md) (first-party) |
| Autonomy tiered by environment | Free in dev, prepared-but-human-authorised in production; deploy, status and rollback exposed as MCP tools scoped per environment; "act up to the production gate and cannot pass it" | Playbook Stage 5 | A clear, auditable line | The production gate stays human-speed | emerging | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md) (first-party) |
| Autonomy set per channel or container | The same agent gets a different review posture by container (e.g. ship without PR review in a low-risk internal-tools channel, information-gathering only in product channels) | Tennr (Claude Tag) | Risk sloping without per-action config | A low-risk channel still let a comp-display bug reach candidates | early-adopter | [tag-healthcare](../research/sources/claude-tag-healthcare-human-agent-teams.md) (vendor claim) |
| Control-band tiers for unattended runs | Deterministic detection; 1σ log, 2σ read-only diagnosis, 3σ act only via a PR or a pre-approved runbook; tiers in versioned config | Playbook Stage 6 | Unattended agents with a bounded action set | Only for metrics with a stable baseline | emerging | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md) (first-party) |
| Four-tier oversight by output risk | Automated / sampled / reviewed / advisory | Anthropic and Accenture CIO blueprint | A simple shared vocabulary for risk sloping | Tier contents not read (gated guide) | emerging | [pilot-to-production](../research/sources/claude-pilot-to-production-cio-blueprint.md) (first-party) |

Note on the auto-mode figure: the companion data says users approve 97% of permission prompts and reject 39% of plans; read as "the gate belongs at plan level" (the note's interpretation, not Anthropic's).

**Key questions**
1. Which action classes should a regulated product agent never auto-approve (outbound messages, writes to systems of record, production)? Nuro, Gusto and Garner each picked one class. — *answered by:* compliance owners and Geoff — *affects:* Classifier-gated, Autonomy tiered by environment.
2. What agreement threshold and sample size moves an agent from recommender to automation mode, and who re-reviews when a model upgrade unlocks new behaviour inside existing permissions? — *answered by:* ABC Legal's CTO; security plus harness owner — *affects:* Earned from measured accuracy.
3. What accuracy did Anthropic's project security review reach before low-risk self-approval was allowed? — *answered by:* Anthropic security — *affects:* Upstream risk classification at shaping time.
4. With non-engineers shipping code (support at Gumroad, PMs at Twilio, designers at League), what review applies to their changes? — *answered by:* engineering leads at those firms; a pilot — *affects:* all.

---

## pm-agent-evaluation

**Evidence for existing options**
- *Output quality vs human baseline / evals*: skill-creator's blind skill vs no-skill A/B ([skill-creator-evals](../research/sources/claude-skill-creator-evals.md)); PMs hand-craft evals to make abstract features concrete ([pm-on-the-ai-exponential](../research/sources/claude-pm-on-the-ai-exponential.md)); Anthropic's analytics agent with snapshot-pinned offline evals, a ~90% per-domain launch gate and ablation on every PR ([self-service-analytics](../research/sources/claude-anthropic-self-service-analytics.md), first-party).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Evals on the agent's own configuration in CI | 20-50 real tasks run non-interactively whenever CLAUDE.md, skills or hooks change, and nightly; config changes that drop the pass rate are reviewed; each incident adds an eval | Playbook Stage 4 | Regression testing for the harness, not just the code | Eval upkeep; cases stop discriminating as models improve | emerging | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md) (first-party) |
| Draft-retention rate | Share of agent drafts kept without a meaningful rewrite; Epic treats both 100% unedited and 0% as alarms | Financial-industry guide; Epic | A cheap pilot metric for document work | Measures acceptance, not correctness | early-adopter | [financial-guide](../research/sources/claude-guide-financial-industry.md) (first-party), [epic](../research/sources/claude-customers-epic-internal-adoption.md) (vendor claim) |
| Human reactions harvested as labels | Emoji and thread replies in chat become an eval set and drive weekly prompt-tuning PRs | ABC Legal Harvester/Tuner | Evals without an extra step for reviewers | Label noise; selection bias | early-adopter | [abc-legal](../research/sources/claude-abc-legal-managed-agents-builders.md) (vendor claim) |
| Rubric-graded outcomes by an independent grader | A separate grader in its own context scores against a rubric that encodes "good" | Managed Agents outcomes | Works for non-code output (docs, decks) | Rubric quality; internal benchmarks only | emerging | [dreaming-outcomes](../research/sources/claude-managed-agents-dreaming-outcomes.md) (first-party) |
| Four-axis builder eval | Outcome, execution path, quality vs a curated reference, resource use; rerun on every model or framework change | Cresta Conductor | Catches regressions on model swaps | Needs a curated reference set | early-adopter | [cresta](../research/sources/claude-cresta-agent-builder-evals.md) (vendor claim) |

**Key questions**
1. What would a product-work counterpart to contribution metrics measure (specs accepted, rework, decisions), and is per-user tracking acceptable? Anthropic itself calls PRs "an incomplete measure". — *answered by:* Geoff and PM leads — *affects:* all ([contribution-metrics](../research/sources/claude-code-contribution-metrics.md)).
2. Can PM SMEs write rubrics good enough for judgement skills (e.g. spec review), and who reviews the evals? — *answered by:* a pilot — *affects:* Rubric-graded outcomes.
3. How are the vendor headline numbers measured (95% analytics accuracy on live queries; 80% "measurable financial impact" in the agents survey)? — *answered by:* Anthropic data team; Material/Anthropic questionnaire — *affects:* any lean that relies on them.

---

## work-structure

**Evidence for existing options**
- *One agent, many skills*: Anthropic now says a single agent with progressively disclosed skills "frequently outperformed" both monolith prompts and subagent designs on quality, often cost and latency; subagents only for context bloat, parallel discardable work, or tool conflicts ([fold-subagents](../research/sources/claude-fold-subagents-into-main-loop.md), first-party, 2026-10-22); Vercel's d0 runs on about 100 skills ([vercel](../research/sources/claude-customers-vercel-skills-ecosystem.md)).
- *Chain of specialised agents across the SDLC*: Notion's investigate, plan and build agents ([notion](../research/sources/claude-customers-notion-managed-agents.md)); Ramp's agents for ideas, bugs, alerts, code, review and post-deploy ([ramp-office-hours](../research/sources/claude-customers-ramp-office-hours.md)); ABC Legal's "a name, an owner, and a single job" ([abc-legal](../research/sources/claude-abc-legal-managed-agents-builders.md)).
- *Hybrid*: Anthropic's five coordination patterns, default orchestrator-subagent then evolve ([multi-agent-patterns](../research/sources/claude-multi-agent-coordination-patterns.md), April 2026), now tempered by the October fold-in guidance.

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Loops by what is handed off | Turn-based (hand off the check), goal-based (the stop condition), time-based (the trigger), proactive (the prompt) | Claude Code /loop, /goal, /schedule | A vocabulary for which PM jobs can run unattended | Several primitives in research preview | emerging | [loop-engineering](../research/sources/claude-loop-engineering.md) (first-party) |
| Model-generated workflow per task | The model writes the orchestration at run time (tens to hundreds of subagents), with adversarial verification | Dynamic workflows | Fits work whose steps aren't known in advance | Token cost; the script differs every run, hard to audit | emerging | [dynamic-workflows](../research/sources/claude-code-dynamic-workflows.md) (first-party), [ramp-office-hours](../research/sources/claude-customers-ramp-office-hours.md) |
| Written human-agent roster | Every member, human or agent, has a defined role; agents defined in skill files; only human-chosen agents may propose new work | Anthropic internal teams | Clarity on who owns what in a mixed team | Overhead; roles drift | emerging | [human-agent-teams](../research/sources/claude-building-effective-human-agent-teams.md) (first-party) |

**Key questions**
1. Does the fold-subagents finding hold for internal PM and knowledge agents, not only customer-facing ones? It directly challenges one-job-per-agent evidence filed earlier. — *answered by:* Anthropic Applied AI's comparison data; an internal A/B — *affects:* One agent many skills vs Chain of specialised agents.
2. Which PM jobs have deterministic stop criteria (fit for /goal) and which need a human-judged stop? — *answered by:* PMs plus the eval owner — *affects:* Loops by what is handed off.

---

## session-persistence-sharing

**Evidence for existing options**
- *Single-owner vendor cloud session*: Cowork on web and mobile keeps running after the laptop closes, per user, not shared ([cowork-web-mobile](../research/sources/claude-cowork-web-mobile-handoff.md)); Claude Code projects ([projects-redesigned](../research/sources/claude-code-projects-redesigned.md)).
- *Shared / multiplayer*: Claude Tag in channels, "multi-player mode" investigation, channel memory ([tag-ci-cd](../research/sources/claude-tag-ci-cd-first-responder.md)); Asana agents post plans on the shared task for colleagues to steer ([asana-coach](../research/sources/claude-asana-agents-you-can-coach.md)); Notion task-board sessions with approval routing ([notion](../research/sources/claude-customers-notion-managed-agents.md)).
- *Persistent / event-driven*: a months-long Claude Tag session woken by a CI-lag threshold ([ci-test-impact](../research/sources/claude-ci-test-impact-analysis.md)); Ramp says more agent sessions are now started by automations than by humans ([ramp-office-hours](../research/sources/claude-customers-ramp-office-hours.md), vendor claim); Notion says 90% of agent turns come from automations ([notion](../research/sources/claude-customers-notion-managed-agents.md)).
- *Shared sessions + shared knowledge edits*: Jamf names shared read/write with a persistence layer as the next frontier ([jamf](../research/sources/claude-customers-jamf.md)).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Personal-to-team agent "graduation" | A personal Cowork agent is promoted to a team agent through software-engineering gates | Cyera (stated need) | A path from individual wins to shared infrastructure | Gates undefined | emerging (need, not product) | [cyera](../research/sources/claude-customers-cyera-cowork-front-door.md) (vendor claim) |

**Key questions**
1. What is the path and the gate set from a personal agent to a team agent (Cyera's "graduation"), and does any vendor product provide it? — *answered by:* Cyera; Anthropic Cowork team — *affects:* all.
2. Will agent view and projects include other people's sessions? Both are single-owner today. — *answered by:* Anthropic roadmap — *affects:* Single-owner vendor cloud session ([agent-view](../research/sources/claude-code-agent-view.md)).

---

## agent-identity-delegation

**Evidence for existing options**
- *Agent runs as a service identity with scoped bundles*: Claude Tag runs as itself per channel compartment, because act-as-user breaks under autonomy and multiple steerers; Anthropic's stated default is "generous access first, then pare back" ([agent-identity-access-model](../research/sources/claude-agent-identity-access-model.md), first-party); Carvana's per-team identities ([carvana](../research/sources/claude-customers-carvana-claude-tag.md)); the analytics bot means "everyone who can mention the bot has the bot's data access" ([tag-self-service-analytics](../research/sources/claude-tag-self-service-analytics.md)).
- *Agent runs as the requester*: Asana agents have their own profile, but effective access is capped by whoever triggers them ([asana-coach](../research/sources/claude-asana-agents-you-can-coach.md), [asana-teammates](../research/sources/claude-customers-asana-ai-teammates.md)).
- *Identity via SSO; central MCP config*: connectors provisioned through the IdP (Okta first) with identity passing through ([enterprise-managed-mcp-auth](../research/sources/claude-enterprise-managed-mcp-auth.md)).
- *Credential vault and proxy outside the agent sandbox*: Cowork remote sessions hold no connector tokens ([ciso-guide](../research/sources/claude-ciso-guide-agentic-ai.md)); Managed Agents vaults ([mcp-production](../research/sources/claude-mcp-production-patterns.md)).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Hybrid: channel identity for shared and unattended work, requester identity for person-initiated reads | A channel request reads the channel's GitHub as the service account and the requester's Drive as the requester; personal connectors never run unattended | Claude Tag personal connectors | Shared agent plus private context without widening the channel's access | Private content can leak into a shared channel; auto mode relies on a model sensitivity check | emerging | [tag-personal-connectors](../research/sources/claude-tag-personal-connectors.md) (first-party) |
| Single-purpose service identity per agent | Minimal permissions per agent (the alert agent has three and cannot deploy); agent-to-agent traffic treated as inside the boundary | Anthropic security | Small blast radius; clear audit attribution | Many identities to manage | early-adopter | [securing-sdlc](../research/sources/claude-securing-ai-native-sdlc-at-anthropic.md) (first-party) |
| Per-user permissions enforced inside tools | One agent loop serves users with different access; tools return plain refusals | Anthropic fold-subagents guidance | One agent instead of many scoped ones | Every tool must implement authz correctly | emerging | [fold-subagents](../research/sources/claude-fold-subagents-into-main-loop.md) (first-party) |

**Key questions**
1. Is "generous access first, then pare back" acceptable in a regulated org, or must a shared agent be scoped to its least-privileged channel member? — *answered by:* the target org's CISO — *affects:* service identity options.
2. How should per-user row-level security work for a shared analytics or PM agent? — *answered by:* the Claude Tag team; the data owner — *affects:* all.
3. How should agent-to-agent requests over Slack be authorised now that Anthropic calls them "the norm"? — *answered by:* Anthropic security; the target org's security — *affects:* Single-purpose service identity.

---

## governance-control-plane

**Evidence for existing options**
- *Per-harness settings*: the playbook's worked managed-settings file for a regulated enterprise (secret reads denied, OS sandbox with a domain allowlist, managed hooks and MCP only, an approved plugin marketplace, a minimum version) ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md)); Cowork RBAC, per-verb connector controls, OTel with approval-mode fields ([cowork-for-enterprise](../research/sources/claude-cowork-for-enterprise.md)).
- *Gateway / proxy*: the Claude apps gateway (self-hosted, IdP, managed settings per request, spend caps, provider failover) for Claude Code ([apps-gateway](../research/sources/claude-apps-gateway.md)); Uber's LLM gateway plus in-harness detection-and-response ([uber-ciso](../research/sources/claude-uber-ciso-insider-threat-ai.md), vendor claim).
- *Deterministic gates in the harness*: "A skill is a control, though an advisory one"; hooks make violations "close to impossible" ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md)); instructions are not guardrails ([steering](../research/sources/claude-steering-claude-code.md)).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Server-side inline DLP on every prompt and tool response | The customer's own server (or Netskope, Palo Alto, Zscaler...) returns allow/deny verdicts across chat, Code and Cowork; shadow mode, percentage rollout, a per-org fail-open or fail-closed choice | Claude Enterprise inference hooks | One enforcement point across surfaces | Default failure policy not stated; outputs may not be inspected | emerging | [inference-hooks](../research/sources/claude-enterprise-inference-hooks.md) (first-party) |
| Agents-as-code with the PR as control surface | Agent config and prompts in git; merge deploys; every change approved | ABC Legal | Version history and audit for agents themselves | Git is a hurdle for non-engineers | early-adopter | [abc-legal](../research/sources/claude-abc-legal-managed-agents-builders.md) (vendor claim) |
| Tiered intake by use-case complexity | One set of principles, three review paths: approved tools (none), skills and MCP (department review), custom API (architecture and security sign-off) | Jamf "One Framework, Three Roads" | Nobody has to ask which process applies | Who does department review is unclear | early-adopter | [jamf](../research/sources/claude-customers-jamf.md) (vendor claim) |
| Central team owns the core, domain teams own skills | A small central team owns the system prompt and end-to-end quality; domain teams own skills and tools, each with evals | Anthropic guidance | Scales authoring without losing quality | Central bottleneck | emerging | [fold-subagents](../research/sources/claude-fold-subagents-into-main-loop.md) (first-party) |

**Key questions**
1. For the target regulated setting, what counts as "untrusted content" (web, customer email, third-party docs)? It sets the risk class of each PM-agent job. — *answered by:* security or GRC — *affects:* all ([ciso-guide](../research/sources/claude-ciso-guide-agentic-ai.md)).
2. Does the apps gateway (or any vendor control) cover Cowork and Claude Tag, or only Claude Code? — *answered by:* Anthropic — *affects:* Gateway / proxy.
3. Is auto mode acceptable for unattended routines in a regulated environment, and with which hooks? — *answered by:* security — *affects:* Deterministic gates.

---

## capability-distribution-trust

**Evidence for existing options**
- Vendor-managed plugin policy and private marketplaces: Cowork's org-specific private marketplaces with auto-install ([cowork-plugins-enterprise](../research/sources/claude-cowork-plugins-enterprise.md)); Level 4 of Anthropic's Cowork maturity model is an admin-provisioned department marketplace, framed as the cure for "shadow AI" ([deploying-cowork](../research/sources/claude-guide-deploying-cowork-across-org.md)); the playbook pins `strictKnownMarketplaces` to one approved repo ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md)).
- No vetting described: the Claude Marketplace (2,000+ listings) describes no review, signing or admin allowlisting ([marketplace](../research/sources/claude-marketplace.md)).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Named policy owner signs off skill changes | Each policy skill has an owner and a written source of truth; skill changes are reviewed like code | Playbook Stage 3 | Skills stay aligned with policy | Owners must exist for every policy | emerging | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md) (first-party) |
| Peer quality pass and skill auditor before team rollout | Team skills get checks (cites sources, respects data boundaries, conflicts with other skills); an agent audits the library for duplication and token waste | Miro; Brainlabs | Lighter than a registry gate; catches sprawl | Brainlabs reached ~400 skills in four weeks and needed consolidation | early-adopter | [miro](../research/sources/claude-customers-miro-champions.md), [brainlabs](../research/sources/claude-customers-brainlabs-cowork-skills.md) (vendor claim) |
| One canonical skill repo synced to every surface | Skills live once in git and sync on merge to the plugin marketplace, blob storage and MCP resources | Anthropic data team | The same answer on every surface | Sync infrastructure | early-adopter | [self-service-analytics](../research/sources/claude-anthropic-self-service-analytics.md) (first-party) |
| Curated internal MCP "app store" with a security rubric | Pre-approved MCP servers with an evaluation rubric, sandbox testing and quarterly re-audit | Anthropic scaling guide | Vetted connectivity | Review capacity | emerging | [scaling-agentic-coding](../research/sources/claude-guide-scaling-agentic-coding.md) (first-party) |

**Key questions**
1. Can Enterprise admins restrict marketplace installs to an approved list, and do private marketplaces support review, signing or eval gates? — *answered by:* Anthropic admin docs — *affects:* all.
2. When an agent edits its own skills (Notion, Warp's improver, Managed Agents memory "instead of" skill edits at Netflix), who reviews? This conflicts with the playbook's owner sign-off. — *answered by:* Notion; Anthropic Managed Agents PM — *affects:* Named policy owner.

---

## context-and-memory

**Evidence for existing options**
- *Curated plain-text context repo*: Anthropic's analytics agent found curated docs plus a routing skill beat raw retrieval (grep over thousands of prior queries moved accuracy under 1 point; LLM-written metric definitions scored net-negative) ([self-service-analytics](../research/sources/claude-anthropic-self-service-analytics.md), first-party); HubSpot's PM team-level context repo shared by people and agents ([hubspot](../research/sources/claude-customers-hubspot-cowork.md)).
- *User-authored memory files*: Claude memory as short per-topic files the user can read and edit, private by default ([memory-everywhere](../research/sources/claude-memory-everywhere.md)); Managed Agents memory as filesystem-mounted, versioned, scoped stores with audit ([managed-agents-memory](../research/sources/claude-managed-agents-memory.md)).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| CLAUDE.md as the team's correction log | "When Claude makes a mistake twice, the correction goes into CLAUDE.md"; review findings feed it; kept under a page and owned | Playbook; steering guide | Compounding repo context with code-review discipline | Decays if unowned | early-adopter | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md), [steering](../research/sources/claude-steering-claude-code.md) (first-party) |
| Self-appended lessons log promoted into skills | The agent appends each incident to lessons.md, reads it first, and recurring patterns are promoted into the skill | Anthropic CI on-call (Claude Tag) | Learning without prompt edits | Who reviews what the agent writes | early-adopter | [tag-ci-cd](../research/sources/claude-tag-ci-cd-first-responder.md) (first-party) |
| Scheduled memory consolidation ("dreaming") | Vendor-run curation of sessions and memory stores, auto-applied or review-first | Managed Agents | Less hand-maintenance | Unreviewed behaviour change | emerging | [dreaming-outcomes](../research/sources/claude-managed-agents-dreaming-outcomes.md) (first-party) |

**Key questions**
1. Does "structure beats retrieval" carry over to PM context (feedback, roadmaps), or only to analytics with one right answer? — *answered by:* a PM-context experiment — *affects:* Curated context repo vs Connectors / MCP.
2. Should learned memories that change agent behaviour go through the same review as skill edits? — *answered by:* Geoff and compliance — *affects:* dreaming, lessons log.

---

## adoption-model

**Evidence for existing options**
- *Product-led enablement*: Stripe pre-installed Claude Code on every laptop and devbox, pre-configured, behind a signed binary ([stripe](../research/sources/claude-customers-stripe-claude-code-rollout.md), vendor claim).
- *Decentralised authoring, central trust*: Cowork maturity ladder from chat to department plugins, champion-led "bottom-up discovery, top-down scale", with champion-authored skills as the leading indicator ([deploying-cowork](../research/sources/claude-guide-deploying-cowork-across-org.md), first-party).
- *Training and workshops*: survey barriers are integration (46%), data (42%) and change management (39%) ([state-of-agents](../research/sources/claude-2026-state-of-ai-agents.md), vendor claim).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Peer showcase channel, then org-wide rollout | PMs demo their shared setups in a channel; personal skills are promoted to team assets | HubSpot PM org; Slack PMs | Spread from real use | No review of shared skills | early-adopter | [hubspot](../research/sources/claude-customers-hubspot-cowork.md), [slack](../research/sources/claude-slack-human-agent-teams.md) (vendor claim) |
| Open tokens, then reach out to top spenders | No per-person budgets; cost managed after an experiment takes off | Ramp; DoorDash | Experimentation | Cost surprises; contrasts with the vendor's gate-then-cap advice | early-adopter | [ramp-office-hours](../research/sources/claude-customers-ramp-office-hours.md), [doordash](../research/sources/claude-customers-doordash-office-hours.md) (vendor claim); vs [cost-visibility](../research/sources/claude-cost-visibility-control.md) |
| Forcing event, with no bake-off | Commit without an evaluation; the company goes live over one weekend; a 48-hour backlog-to-production event | League (regulated healthcare) | Speed | Security foundation built after (about a quarter) | early-adopter | [league](../research/sources/claude-customers-league.md) (vendor claim) |
| Steering committee of builders who train their teams | 15 cross-functional builders ship agents in a week from a repo template, then cascade | ABC Legal | Non-engineer builders with governance | Git was the hurdle | early-adopter | [abc-legal](../research/sources/claude-abc-legal-managed-agents-builders.md) (vendor claim) |

**Key questions**
1. Is 1,370 Stripe engineers seats or weekly actives, and what are the active rates behind the 88-97% adoption claims (Cyera, Zapier, Jamf)? — *answered by:* customers' platform teams — *affects:* all.
2. Anthropic's scaling guide is engineer-only (one line on PMs). What does a PM-first rollout need that an engineering rollout doesn't? — *answered by:* HubSpot or Miro PM leads; a pilot — *affects:* all ([scaling-agentic-coding](../research/sources/claude-guide-scaling-agentic-coding.md)).

---

## target-user

**Evidence for existing options**
- Non-engineering functions: Anthropic says "the vast majority" of Cowork use is outside engineering, and its session analysis puts business ops (33%) and content (16%) at about half, with no PM or design category ([cowork-for-enterprise](../research/sources/claude-cowork-for-enterprise.md), [how-people-use-cowork](../research/sources/claude-how-people-use-cowork.md), first-party telemetry).
- PMs and designers as builders: "Our PMs code a lot now" ([running-ai-native-engineering-org](../research/sources/claude-running-ai-native-engineering-org.md)); Epic says over half of Claude Code use is from non-developers ([epic](../research/sources/claude-customers-epic-internal-adoption.md)); a Twilio product director built a 425-tool platform ([twilio](../research/sources/claude-customers-twilio-pm-platform.md)).
- *Product owner as approver*: the playbook's chain puts a product owner at every early gate, with any employee as originator ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md)).

**Key questions**
1. What share of Cowork and Claude Code use is PM, design and analyst work, and what is the task mix? — *answered by:* Anthropic's Economic Index team or the target org's admin analytics — *affects:* sequencing.
2. Is the one-PM, multi-week platform build (Twilio) repeatable for typical PMs, or a senior-domain-expert outlier? — *answered by:* Twilio; a pilot cohort — *affects:* PM-as-builder.

---

## sequencing

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Adopt plays in dependency order, prompting by hand first | Start with plays that need nothing (intent capture, CLAUDE.md, skills, hooks as gates, feedback loop); automate triggers only later | Playbook dependency graph | Low-risk entry; each play has its own measure | Value of the loop arrives late | emerging | [playbook](../research/sources/claude-ai-native-sdlc-playbook.md) (first-party) |
| Plan downstream capacity before accelerating upstream | Assume CI load rises 25x within two quarters; fix test selection before scaling agents | Anthropic CI | Avoids the bottleneck moving to CI and review | Infra spend before visible gains | early-adopter | [ci-test-impact](../research/sources/claude-ci-test-impact-analysis.md) (first-party) |
| Start with connective jobs | Status roll-ups, decks and trackers, where general-agent use already concentrates | Cowork telemetry | Quick wins | Low strategic value | emerging | [how-people-use-cowork](../research/sources/claude-how-people-use-cowork.md) (first-party) |
| Surface order: skills, then add-ins, then Cowork | Low-risk, high-reuse surfaces first in a regulated industry | Financial-industry guide | Fits regulated pilots | Contradicts the Cowork guide's ladder, which starts in Cowork | emerging | [financial-guide](../research/sources/claude-guide-financial-industry.md) (first-party) |

**Key questions**
1. Should a product-agent effort start at intent capture (the playbook's no-prerequisite first play), or downstream where agents already work? Asana's Command reports that automated feedback-to-PR loops bloated cycles until planning was gated ([asana-coach](../research/sources/claude-asana-agents-you-can-coach.md)), which supports intent first. — *answered by:* the deck; a pilot — *affects:* all.

---

## harness-upkeep

**Evidence for existing options**
- Re-test and delete scaffolding per model: harness parts encode model weaknesses that go stale ([harness-design-three-patterns](../research/sources/claude-harness-design-three-patterns.md)); "every model release is an implicit prompt to revisit" ([pm-on-the-ai-exponential](../research/sources/claude-pm-on-the-ai-exponential.md)); Ramp builds for the model 3-6 months out ([ramp-office-hours](../research/sources/claude-customers-ramp-office-hours.md)); review config every 3-6 months ([large-codebases](../research/sources/claude-code-large-codebases.md)).

**Proposed options**

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Skills updated in the same PR as what they describe | A review hook flags data-model changes that leave skills untouched; about 90% of model PRs include a skill change | Anthropic data team | Prevents drift (accuracy fell from ~95% to ~65% in a month without it) | Discipline across teams | early-adopter | [self-service-analytics](../research/sources/claude-anthropic-self-service-analytics.md) (first-party) |
| Feedback-driven improver loop via PR | A scheduled improver agent turns reviewer feedback into skill-edit PRs a human merges | Warp; ABC Legal Tuner; Anthropic legal channel | Learning with a human gate | Whose feedback counts | early-adopter | [warp](../research/sources/claude-warp-self-improving-agents.md), [abc-legal](../research/sources/claude-abc-legal-managed-agents-builders.md) (vendor claim), [how-anthropic-uses-tag](../research/sources/claude-how-anthropic-uses-claude-tag.md) (first-party) |

**Key questions**
1. Which parts of a product harness (templates, checklists, forced steps) encode model weaknesses that will expire, and who owns pruning them? — *answered by:* Geoff and the harness team — *affects:* all.

---

## agent-interface, harness-layering, loop-source, runtime-location, model-provider-coupling, trust-privacy-defaults (shorter)

- **agent-interface.** New evidence: one Claude that escalates from chat to long-running work, after users could not tell "where a task belonged" ([cowork-chat-unified](../research/sources/claude-cowork-chat-unified.md)); a task board as orchestrator (Notion, Rakuten Kanban) ([notion](../research/sources/claude-customers-notion-managed-agents.md), [rakuten](../research/sources/claude-customers-rakuten-every-employee-builder.md)); one front door over 40 tools instead of each SaaS tool's AI ([cyera](../research/sources/claude-customers-cyera-cowork-front-door.md)). *Proposed option:* structured-form slash commands that launch a workflow like filling a brief ([cowork-plugins-enterprise](../research/sources/claude-cowork-plugins-enterprise.md)). *Key question:* does a PM product agent live in the work tracker (where Notion and Asana put it), in chat, or in its own app? — *answered by:* user interviews.
- **harness-layering.** New evidence: mods as an event-level layer over Claude Code, with a load-order security caveat ([mods](../research/sources/claude-code-mods.md)); Stripe runs six coding assistants with no layer above ([stripe](../research/sources/claude-customers-stripe-claude-code-rollout.md)); Zapier keeps skills outside any one harness and puts tools behind one MCP ([zapier-cowork](../research/sources/claude-customers-zapier-cowork.md)); a domain control plane on the Agent SDK ([cresta](../research/sources/claude-cresta-agent-builder-evals.md)). *Key question:* which of Claude Code's seven steering mechanisms carry over to Cowork for PMs? — *answered by:* Anthropic docs ([steering](../research/sources/claude-steering-claude-code.md)).
- **loop-source.** Buy the loop, build the domain: Asana, Notion, Sentry, Rakuten and Pendo on Managed Agents; Carvana retired two homegrown Slack agents for Claude Tag ([sentry](../research/sources/claude-customers-sentry-bug-fixing-agents.md), [carvana](../research/sources/claude-customers-carvana-claude-tag.md), vendor claims). *Proposed option:* automation-triggered sessions as the main loop source (Ramp, Notion). 
- **runtime-location.** Agent jobs sandboxed with short-lived scoped tokens and no standing production credentials ([playbook](../research/sources/claude-ai-native-sdlc-playbook.md)); PHI kept in an environment Claude cannot reach ([league](../research/sources/claude-customers-league.md)); company-cloud VMs "blessed by security" on the Agent SDK at DoorDash ([doordash](../research/sources/claude-customers-doordash-office-hours.md)).
- **model-provider-coupling.** Multi-provider gateways routed by task difficulty (Atlassian, Delivery Hero on LiteLLM with Claude at ~95%) ([atlassian](../research/sources/claude-customers-atlassian-trusted-agents.md), [delivery-hero](../research/sources/claude-customers-delivery-hero-pr-agent.md)); Bedrock/Vertex/Foundry to stay inside the cloud perimeter in regulated firms ([financial-guide](../research/sources/claude-guide-financial-industry.md)).
- **trust-privacy-defaults.** Public by default with fenced exceptions (Anthropic, Slack CPO) vs Claude Tag's "generous access first" vs PHI walled off by channel scoping (Tennr, Insight Health) ([human-agent-teams](../research/sources/claude-building-effective-human-agent-teams.md), [slack](../research/sources/claude-slack-human-agent-teams.md), [tag-healthcare](../research/sources/claude-tag-healthcare-human-agent-teams.md)). Prompt content is in Cowork's OTel by default ([ciso-guide](../research/sources/claude-ciso-guide-agentic-ai.md)). *Key question:* how does public-by-default work under information barriers in a regulated org? — *answered by:* compliance.

## Cross-cutting key questions

1. Every first-party page here prescribes; none reports a controlled outcome. Which two or three claims would the deck rely on, and can any be checked independently (customer platform teams, a pilot)? — *affects:* all leans.
2. Anthropic's own guidance moved within six months (multi-agent patterns in April, fold subagents back into one loop in October; chat vs Cowork advice in June, merged in September). How should the deck treat vendor guidance that is this young? — *affects:* work-structure, agent-interface.

## New dimensions proposed

None. The material fits the existing register. One candidate for the director: a **"source of truth per artifact"** choice (repo vs legacy tool vs linkage) could stand alone, but it fits under artifact-and-project-structure for now.
