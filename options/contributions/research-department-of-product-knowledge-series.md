# Options contribution: research-department-of-product-knowledge-series

Proposed additions to [DIMENSIONS.md](../DIMENSIONS.md) from the Department of Product Knowledge Series sweep: posts from 2024-10-24 to 2026-10-13 ([triage](../../tasks/research-department-of-product-knowledge-series/01-triage.md), [summary](../../tasks/research-department-of-product-knowledge-series/00-summary.md)). For the director to merge. The rows are grouped under existing dimension slugs, and no new dimension is proposed. Each row was checked against DIMENSIONS.md as of 2026-10-24, and anything already there was left out.

**Links** resolve from this folder (`../../research/...`); drop one `../` when merging into DIMENSIONS.md.

**Evidence caveat for every row.** DoP is a PM-audience explainer by one author, Rich Holmes. Its notes are marked `independent` because DoP has no stake in the companies it covers, but nearly every company fact in it is relayed from that company's own announcement. "(independent, relaying vendor claims)" means the number is the vendor's. Rows that rest on the author's own tutorial builds are practitioner demos, with nothing measured.

---

## activity-classification

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Three-axis automation canvas (safety, volume, verifiability) | Score each task 1–3 on safety-if-wrong, volume and how easily the output can be checked. Plot verifiability against volume, coloured by safety, then map each task to automate now, AI assistant, or not ready | DoP AI Automation Opportunity Canvas, with a scoring prompt, a pre-mortem and a workshop mini-app | Cheap, workshop-ready and in PM vocabulary. The "assistant" tier hands over naturally to review-and-autonomy | The author's own framework, not validated. Three axes leave out context breadth, collaboration and audit need (Track 6 axes) | emerging | [DoP automation opportunities](../../research/sources/departmentofproduct-ai-automation-opportunities.md) (independent) |
| Repetition report mined from the harness | The harness reads one person's session history and flags same-shaped repeated tasks as candidates for a command or skill | Claude Code `/insights` | Bottom-up discovery from real usage, not from a workshop | One user's view only. No evidence that people act on it | emerging | [DoP slash commands](../../research/sources/departmentofproduct-loops-goals-slash-commands.md) (independent) |

**Key questions**
1. Do three axes (safety, volume, verifiability) sort PM job steps as well as the seven Track 6 axes, so the simpler canvas could be used in user workshops? — *answered by:* scoring the same 10–20 steps both ways and comparing against bake-off results — *affects:* three-axis canvas, multi-axis task properties
2. Do the candidates mined from usage (`/insights`) match what workshops pick? — *answered by:* a pilot with 3–5 PMs: report first, then workshop, then compare — *affects:* repetition report, usage-derived pattern

**Correction for the owning task:** the [Stripe Kai DoP note](../../research/sources/departmentofproduct-stripe-kai.md) describes this canvas as "frequency vs volume". The source post's axes are safety, volume and verifiability.

## review-and-autonomy

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Reversibility split enforced by the harness | Actions that are easy to undo (drafts, proposals, summaries) run freely. Hard-to-undo actions (payments, publishing, financial records) sit in a hard-coded approval layer the model cannot bypass | DoP harness principle 2; Square Managerbot | A rule PMs and risk owners can both reason about. Fits the "deterministic gates" row | Reversibility is not binary, and someone must classify every tool | emerging | [DoP agent harnesses](../../research/sources/departmentofproduct-agent-harnesses-secret-sauce.md) (independent, relaying vendor claims) |
| Propose-only agent with approval in the loop | The agent monitors and proposes, and every action waits for an explicit tap from the user. Approval is designed into the loop, not bolted on | Square Managerbot (the second regulated-payments case after Stripe) | Clear accountability in a regulated domain | Approval fatigue; little automation realised | early-adopter | [DoP agent harnesses](../../research/sources/departmentofproduct-agent-harnesses-secret-sauce.md) (independent, relaying vendor claims) |
| Autonomy set by a spec complexity tag | The spec-writing agent tags each item's size and type. Small code fixes go to an autonomous coding agent, the rest become tickets for people, and the threshold rises "as you build trust" | Amplitude Wave (closed beta); DoP Claude Code template | Autonomy decided per item, and auditable | The tag can be wrong. Amplitude's own ship rate is ~11% | emerging | [DoP self-improving product](../../research/sources/departmentofproduct-self-improving-product.md) (independent; Amplitude figures are vendor claims) |
| "Describe done" goal runs | The user states the end state, how to verify it and what must be preserved, and the agent runs many turns until that condition holds. The guidance excludes strategic or costly-to-get-wrong work | Claude Code `/goal`, Codex `/goal` | Delegation without step prompts; a "done" that can be checked | Wrong tool for judgement work; long runs spend tokens | emerging | [DoP slash commands](../../research/sources/departmentofproduct-loops-goals-slash-commands.md) (independent) |

**Key questions**
1. For each tool a PM agent can call, is the action reversible, and who classifies it? — *answered by:* a tool inventory reviewed with policy owners — *affects:* reversibility split, propose-only, deterministic gates
2. What approval rate per proposal can a PM sustain before propose-only becomes rubber-stamping? — *answered by:* a pilot that logs approvals, time to approve and edits — *affects:* propose-only, risk-scored routing

## pm-agent-evaluation

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Proposal funnel: would-do rate vs ship rate | Measure the share of agent-proposed work a human says they would do against the share that actually ships, and train a judge to predict human approval | Amplitude Wave (~50% would do, ~11% shipped) | Measures the proposal pipeline, not activity. A rare candid vendor number | Says nothing about the outcome or quality of what shipped | emerging | [DoP self-improving product](../../research/sources/departmentofproduct-self-improving-product.md) (vendor claim, relayed) |
| Calibrated LLM-judge stack | Programmatic checks first, then an LLM judge calibrated to 80–90% agreement with human labels, then human review on top | Airbnb; DoorDash (from ~1 human review a day to 2,000 judged sessions) | Grading at a scale humans can't reach | Needs a calibration set per job; second-hand claims | early-adopter | [DoP managing agents](../../research/sources/departmentofproduct-managing-ai-agents.md) (independent, relaying vendor claims) |
| The most-asked real questions as the eval set | Use the 20–30 questions people ask most as both the build target and the eval, and require ~80% before rollout | Anthropic data team (reported 21%→95% after a semantic layer and two skills) | Grounded in real demand | Narrow coverage; the 80% bar is arbitrary | emerging | [DoP semantic layers](../../research/sources/departmentofproduct-semantic-data-layers.md) (independent, relaying vendor claims) |
| A PM-kept "model sense" log | A prompt library, a log of what each model claimed against what was observed, and a small domain eval rerun at each model release | DoP Model Sense Notebook | A cheap regression check on PM jobs, owned by PMs | Manual; subjective scoring | practice | [DoP model sense](../../research/sources/departmentofproduct-model-sense-testing.md) (independent) |

**Key questions**
1. Would PMs accept an agent that proposes backlog items from metrics and tickets, and what ship rate would make reviewing its proposals worthwhile? — *answered by:* a pilot on one product area that logs why items are rejected — *affects:* proposal funnel, intent-shaping "agent-originated intent"
2. Which PM jobs are in the "frontier zone" (possible now, reliable in about six months), so they can be prototyped internally without shipping? — *answered by:* a fixed PM eval suite rerun at each release — *affects:* model-sense log, sequencing

## governance-control-plane

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Agent-to-tool gateway with an allowlist | A single checkpoint before every tool call: authenticate, rate-limit, hand off credentials, check an agent-to-tool allowlist | DoorDash Agent Gateway; AWS deny-by-default runtime | One place for tool access and audit | Governs only the traffic routed through it | early-adopter | [DoP managing agents](../../research/sources/departmentofproduct-managing-ai-agents.md) (independent, relaying vendor claims) |
| Pre-execution action interception (open checklist) | Each agent action is checked against policy, or by a human, before it runs, with build-time and run-time controls kept separate | Vanta Agentic Trust Controls; the AARM proposal | Open, and mappable to audit requirements | At proposal stage; no deployment data | emerging | [DoP managing agents](../../research/sources/departmentofproduct-managing-ai-agents.md) (independent) |
| Spend tied to output | A spend console that sets token spend against output (PR volume, rework) as well as totals | Rippling AI Spend Console; Ramp token spend management | Answers "is it paying off" as well as "how much" | PR volume measures motion, not value; vendor claims | emerging | [DoP managing agents](../../research/sources/departmentofproduct-managing-ai-agents.md) (independent, relaying vendor claims) |
| Typed-answer classifier for routing and pre-action checks | A small fixed-choice "decision model" decides tool or model routing, and "is this safe to run?", before each step, in place of an LLM call | Vercel safety checks (claimed 18x faster); Higgsfield routing; Rippling GrowthOS | Low latency and low cost per check | Needs fixed answer sets. In Rippling's test it failed wherever business definitions mattered. Benchmarks are at v0.2–0.3 | experimental | [DoP decision models](../../research/sources/departmentofproduct-decision-models.md) (independent, relaying vendor claims) |

**Key questions**
1. Does the Agentic Trust Controls checklist cover our regulated audit needs, or does it duplicate controls we already hold? — *answered by:* a policy owner review — *affects:* interception, gateway
2. Should routing and pre-action checks run on a typed classifier rather than an LLM call? — *answered by:* an engineering benchmark on our own agent traces — *affects:* typed classifier, review-and-autonomy "classifier-gated"

## agent-identity-delegation

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Connector list as the unattended permission boundary | A scheduled run can touch whatever connectors are attached to it, writes included, with no approval per action. You scope it by attaching less | Claude Code routines | A simple mental model for PMs | Coarse: per connector, not per action. The author found the read-only controls unclear | early-adopter | [DoP Claude Routines](../../research/sources/departmentofproduct-claude-routines-for-product-teams.md) (independent) |
| Dual identity carried through every hop | The human and the agent travel as two identities on every call, or each agent has its own cryptographic identity, so "who authorised what" survives multi-agent chains | Block User Identity Delegation; Uber agent identity | Attribution across agent hops | Infrastructure work; both cases second-hand | early-adopter | [DoP managing agents](../../research/sources/departmentofproduct-managing-ai-agents.md) (independent, relaying vendor claims) |
| Delegated session capped at user ∩ agent ceiling | A delegated session gets the intersection of the user's permissions and an agent ceiling, with step-up auth on sensitive calls | WorkOS Agent Auth | Least privilege by construction | A vendor product, and it needs every tool to honour it | emerging | [DoP headless strategy](../../research/sources/departmentofproduct-headless-product-strategy.md) (independent, relaying vendor claims) |

**Key questions**
1. Is connector-level scoping fine-grained enough for unattended PM runs, or do we need read/write limits per action? — *answered by:* security owners reviewing the routines permission model — *affects:* connector boundary, credentials proxy

## session-persistence-sharing

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| In-session interval loop | A recurring check that runs inside the open session at a fixed or self-chosen interval, calling a command file | Claude Code `/loop` | No setup; cheap monitoring | Probably ends with the session (not verified); unclear for weekly cadences | emerging | [DoP slash commands](../../research/sources/departmentofproduct-loops-goals-slash-commands.md) (independent) |

**Key questions**
1. Which PM monitoring jobs fit an in-session loop, and which need a cloud routine? — *answered by:* trialling both on two real weekly jobs — *affects:* in-session loop, scheduled or event-triggered runs
2. Will PMs without a code repo adopt scheduled agents that need one? Remote routines need a repo, so the DoP tutorial starts by creating one on GitHub. — *answered by:* a setup test with 3–5 PMs — *affects:* routines, agent-interface "own workspace"

## context-and-memory

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Governed semantic layer with owned definitions | Canonical, versioned metric definitions that agents query first. AI drafts each definition and a named human owns it | Anthropic data team (second-hand: ~95% of data requests automated) | Large claimed accuracy gains for analytics agents; the organisation's vocabulary becomes legible | Needs a data team and an owner per definition; drifts without owners | early-adopter | [DoP semantic layers](../../research/sources/departmentofproduct-semantic-data-layers.md) (independent, relaying vendor claims) |
| Repo snapshot file as state between runs | A scheduled agent writes what it saw to a file in the repo and diffs against it on the next run | DoP competitor-changelog routine | Inspectable, versioned memory without a memory system | The first run only sets a baseline; someone must own the file | emerging | [DoP Claude Routines](../../research/sources/departmentofproduct-claude-routines-for-product-teams.md) (independent) |
| Memory per product area, written by a reflection agent | After each cycle a reflection agent rewrites one markdown file per product area: what worked, what didn't, what the team keeps rejecting | DoP self-improving product template | The agent learns the team's taste from its rejections | Unreviewed memory can harden bias | emerging | [DoP self-improving product](../../research/sources/departmentofproduct-self-improving-product.md) (independent) |
| Vendor CLI as the tool route | The harness calls a vendor CLI whose workflow commands bundle several API calls and encode the vendor's recommended patterns | Google Workspace CLI; Stripe Projects; Ramp CLI | Text-native workflows the vendor supports; a third route beside MCP and APIs | Needs a shell and per-user auth ("fiddly"); chat surfaces have no shell | early-adopter | [DoP CLIs](../../research/sources/departmentofproduct-cli-for-product-teams.md) (independent) |
| One code-mode tool in place of many tools | A single MCP tool in which the agent writes a sandboxed program that combines calls | Rippling MCP (claims 98% cheaper); Cloudflare Code Mode | Fewer tokens; can compute fields no single API returns | Sandbox and security cost | emerging | [DoP headless strategy](../../research/sources/departmentofproduct-headless-product-strategy.md) (vendor claim, relayed) |
| Aggregator MCP | One connector exposes user-chosen actions across thousands of apps | Zapier MCP | Fast breadth | A third party in the data path; permissions are set per Zapier action | early-adopter | [DoP MCP at work](../../research/sources/departmentofproduct-mcp-at-work.md) (independent) |

**Key questions**
1. For PM metrics agents, is a semantic layer a prerequisite, or is a context file of healthy ranges enough for a first job? — *answered by:* prototyping both on one metric set — *affects:* semantic layer, sequencing
2. When should a PM agent reach a tool through a vendor CLI rather than MCP? — *answered by:* a prototype comparing the Workspace CLI with a Google MCP server on 2–3 PM jobs — *affects:* CLI route, agent-interface
3. As PM tools get more traffic from agents than from people (Linear's CEO says agent-created issues now outnumber human ones), how much does our harness depend on those vendors' MCP quality and rate limits? — *answered by:* a review of vendor MCP servers — *affects:* all tool-route rows

## artifact-and-project-structure

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Sub-projects owned by each function, with a master roll-up | One project per area, owned by its function; a master project combines them | DoP product-health setup on Claude Projects | Delegated ownership; smaller contexts | The roll-up is manual copy-paste, and filename prefixes stand in for structure | early-adopter | [DoP Projects product health](../../research/sources/departmentofproduct-claude-projects-product-health.md) (independent) |
| Decision queue as a first-class artifact | Open decisions kept as records (the call, its kind, who it waits on, age, context), extracted from inbox and chat. "A forcing function", not a to-do list | DoP product dashboard | Makes a PM's real bottleneck visible | Extraction accuracy; overlaps with trackers | experimental | [DoP product dashboard](../../research/sources/departmentofproduct-product-dashboard-stakeholder-updates.md) (independent) |
| Stage-artifact skill family | Skills split by stage (what, then how, then build), each writing a durable file the next one reads | Every compound-engineering; gstack; Atlassian spec-to-backlog (the breakdown is approved first) | Stages can be inspected and swapped; no dependence on one long chat | A convention, not a standard; files drift | emerging | [DoP agent skills](../../research/sources/departmentofproduct-practical-agent-skills.md) (independent) |

**Key questions**
1. Do roll-ups across projects (team to master) need to be native to our project model, or is a scheduled summary skill enough? — *answered by:* interviews with PMs who run health checks across functions — *affects:* sub-project roll-up, project-taxonomy
2. Is "open decision" an artifact type we should model? — *answered by:* PM research on where decisions stall — *affects:* decision queue, status-update sequencing

## intent-shaping-and-spec

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Closed sense-decide-act-learn loop (evidence for "agent-originated intent") | Agents read analytics, support and errors against a map of product areas. They judge and spec opportunities (checked against the codebase, tagged for complexity), route them, check the PR against the acceptance criteria and write memory for each area | Amplitude Wave; DoP Claude Code template | A signal-driven backlog that learns from rejections | ~11% shipped against ~50% would do. Chasing metrics can harm coherence ("AI optimized product slop") | emerging | [DoP self-improving product](../../research/sources/departmentofproduct-self-improving-product.md) (independent; vendor numbers) |
| Diverge-first ideation agent | The agent researches named products and proposes N directions. The PM picks one, the agent drafts a PRD for editing, then it generates screens and a deck | Google Stitch Ideate; the Stitch MCP chained in Claude Code | Breadth before convergence; fast material for stakeholders | Output is for discussion only; beta | emerging | [DoP Stitch Ideate](../../research/sources/departmentofproduct-google-stitch-ideate-agent.md) (independent) |
| Framework-scripted sparring partner | The agent recommends three frameworks (Kano, pre-mortem, JTBD...) and walks the PM through the chosen one step by step: "cognitive expansion, not offloading" | DoP Strategy Thought Partner | Keeps the PM's own reasoning in the loop; a repeatable shape | Frameworks can become theatre; risk of sycophancy | prototype | [DoP strategy thought partner](../../research/sources/departmentofproduct-strategy-thought-partner.md) (independent) |
| Synthetic persona panel as a check before research | The feature is put to several AI personas built from research data, optionally on a voice call, before real users see it | DoP Persona Feature Tester | A fast check of assumptions from several viewpoints | The demo's "grounding" data was itself AI-generated. NN/g documents the optimism of synthetic users | emerging | [DoP persona tester](../../research/sources/departmentofproduct-persona-feature-tester.md) (independent) |
| Two-layer spec artifact (machine tokens plus rationale prose) | Exact values in front matter and judgement guidance in prose, checked by a CLI linter | Google DESIGN.md (open-sourced) | Precise where it can be, guided where it can't; lintable | Agents fill gaps silently with plausible values, and finished-looking output suppresses critique | early-adopter | [DoP DESIGN.md](../../research/sources/departmentofproduct-design-md-explained.md) (independent) |

**Key questions**
1. Do synthetic persona verdicts agree with what real users later said, for our own features? — *answered by:* a back-test on past features whose reception is known — *affects:* persona panel
2. Could the intent-shaping spec standard take the DESIGN.md shape (machine-checkable fields plus rationale), and what would its linter check? — *answered by:* drafting the standard with product and engineering leads, then linting 10 past specs — *affects:* two-layer artifact, the existing "evidence-tied spec" row

## capability-distribution-trust

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Curated starter pack from public repos | A small, hand-picked bundle of public skills given to PMs as a folder | DoP's 10-skill download (one source repo holds 1,000+ skills) | A fast start without searching an estimated 40k–100k published skills | No scanning, pinning or review; trust rests on the curator | common practice | [DoP agent skills](../../research/sources/departmentofproduct-practical-agent-skills.md) (independent) |
| Official vendor skill paired with its MCP server | A tool vendor ships a skill that drives its own MCP server in the right object order | Atlassian spec-to-backlog; Notion Spec to Implementation | Correct semantics, from the vendor | Locks the workflow to that vendor (Notion's assumes the whole cycle lives in Notion) | early-adopter | [DoP agent skills](../../research/sources/departmentofproduct-practical-agent-skills.md), [DoP Claude Skills](../../research/sources/departmentofproduct-claude-skills-for-product-work.md) (independent) |

**Key questions**
1. Do we let PMs install public skills, and through what vetting: a registry gate, a curated pack, or none? Mainstream PM media hands them out with no security framing. — *answered by:* security and IT policy, plus an audit of the skills the pilot's PMs actually use — *affects:* curated pack, org-governed registry

## agent-interface

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Separate design surface with a handoff to the coding harness | Prototypes and decks are made on a design canvas grounded in the design system, then one command pulls them into Claude Code | Claude Design | Visual iteration for PMs, with continuity into the repo | Another surface to govern. It is a research preview, and export failed when DoP tested it | preview | [DoP Claude Design](../../research/sources/departmentofproduct-claude-design.md) (independent) |
| Personal PM cockpit with a "draft an update" action | A PM vibe-codes a local dashboard over their own data, with an action that generates an update for a chosen audience | DoP product dashboard | Tailored and immediate | Personal and local, on dummy data unless wired up; nothing is shared | early-adopter | [DoP product dashboard](../../research/sources/departmentofproduct-product-dashboard-stakeholder-updates.md) (independent) |

**Key questions**
1. Is our PM agent an MCP client that reaches other tools, or a server that other agents call? DoP reports that Intercom chose the first and Stripe the second. — *answered by:* where PMs already work, and whether the agent's value depends on being the front door — *affects:* agent-interface, remote-invocation-route

## loop-source

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Hosted multi-model general agent for knowledge workers | A prosumer cloud agent plans the work, runs sub-agents and routes each subtask to a different vendor's model. It acts through two-way connectors and runs always-on background workers | Perplexity Computer | Nothing to build; model-agnostic; UX for non-developers | Metered in credits; no evidence on enterprise governance; vendor-controlled | emerging | [DoP Perplexity Computer](../../research/sources/departmentofproduct-perplexity-computer.md) (an independent tutorial; the capabilities are as the vendor describes them) |

## adoption-model

| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Per-person tool budget; buy what spreads | Each person gets a monthly budget for approved tools, and whatever peers adopt widely is bought company-wide | Brex (second-hand) | A bottom-up signal of adoption | Tool sprawl; governance comes after the fact | early-adopter | [DoP engineering velocity](../../research/sources/departmentofproduct-engineering-velocity-non-engineers.md) (independent, relaying) |
| AI fluency rubric for every role | A published rubric of the AI use expected in each role, which rates manual-only work "unacceptable" | Zapier (Wade Foster) | Makes the expectation explicit | Mandates usage, not outcomes; risk of performative use | early-adopter | [DoP AI fluency](../../research/sources/departmentofproduct-ai-fluency.md) (independent, relaying) |

**Key questions**
1. Do personal tutorials, which teach PMs to build their own dashboards, Projects and loops, produce anything others reuse, or do they need a packaging step (Glass's "one person's win becomes everyone's baseline")? — *answered by:* counting reuse of PM-built tools in a pilot — *affects:* adoption-model, capability-distribution-trust

## Cross-cutting key question (proposed)
- Almost every number in PM-audience explainers belongs to the vendor; DoP relays Strella, Amplitude, DoorDash, Anthropic, Rippling and Vercel figures without checking them. Must every figure be traced to its primary source and labelled before the deck uses it? — *answered by:* the claim-check practice the story worker already uses — *affects:* all dimensions
