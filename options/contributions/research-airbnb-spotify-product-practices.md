# Options contributions: research-airbnb-spotify-product-practices

Proposed additions to `options/DIMENSIONS.md` from task research-airbnb-spotify-product-practices: 90 source notes on how Airbnb and Spotify run product, filed in `research/sources/`. **Nothing has been merged into DIMENSIONS.md**; this file is for the director.

How to read it:
- Dimensions appear in DIMENSIONS.md order, and only those this task touches are listed.
- Option names under "New evidence for existing options" are spelled as in DIMENSIONS.md.
- Evidence types are first-party, vendor claim, independent and anecdote. Almost all Airbnb and Spotify evidence is first-party.
- Links are relative to `options/contributions/`.
- Brief: [00-brief.md](../../tasks/research-airbnb-spotify-product-practices/00-brief.md). Maps: [Airbnb](../../tasks/research-airbnb-spotify-product-practices/01-pdlc-airbnb.md), [Spotify](../../tasks/research-airbnb-spotify-product-practices/02-pdlc-spotify.md).

Added by: research-airbnb-spotify-product-practices on 2026-10-24.

---

## harness-layering: Is there a layer above the vendor harnesses

### New evidence for existing options
- **Hosted multi-harness control plane** (company-built). Spotify's Xirp runs Claude Code, Gemini CLI and Codex sessions. A user can switch tool or model mid-task and keep working state. Sessions start with catalog context, transcripts flow back to Portal, and leaders see "thousands of concurrent sessions". It is in public beta as a product (Aug 2026) — [xirp](../../research/sources/spotify-portal-blog-introducing-xirp.md) (first-party, also marketing).
- **Company-branded internal harness over vendor agents.** Airbnb's AirChat CLI wraps Claude Code and Codex behind one gateway for cost and metrics. It adds default MCPs, a plugin and skill marketplace, an SDK with about 40 apps, and AirChat Remote for async runs on isolated cloud workspaces — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md) (first-party, DX-hosted talk).

### Key questions to add
1. Is a company-branded harness over vendor agents (AirChat, Xirp) a cause of adoption or a result of it? Both companies built theirs after vendor tools spread. — *answered by:* interviews with Airbnb's Dev AI team and Spotify's Portal team; adoption curves before and after launch.

## context-and-memory: Context and memory

### New options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Software catalog as the agent context layer | Owners, lineage, standards, docs, skills and MCP servers are owned entities in one catalog. Agents query it over MCP, sessions start with it, and transcripts flow back | Spotify Backstage/Portal (`AiResource` kind, MCP actions); Xirp | Systems context with owners and health signals; reuses an existing source of truth | Covers systems, not product rationale; needs years of ownership discipline; the actions registry leaves permission checks to each tool (fail-open risk) | early-adopter | [backstage-docs-ai](../../research/sources/backstage-docs-ai.md); [portal-mcp](../../research/sources/spotify-portal-docs-mcp.md); [xirp](../../research/sources/spotify-portal-blog-introducing-xirp.md) (first-party) |
| LLM-built org context graph | An org graph built with LLMs and embeddings across the codebase and projects, so generalists can plan in specialist areas and learnings carry to the next build | Airbnb Everest | Breadth without hand-curation | Inputs and accuracy unpublished; code- and project-oriented; one interview is the only source | emerging | [latent-space-al-dahle](../../research/sources/latent-space-airbnb-al-dahle-inside-out-ai.md) (first-party) |
| Method package as shared memory | An expert team's method (framing, evidence selection, labelling) is wrapped around the model as a shared package that every run can improve | Airbnb Insight Miner | Reproducible, auditable research by non-experts; compounding method | Needs an owning expert team; one domain (text investigations) so far | emerging | [insight-miner](../../research/sources/airbnb-tech-insight-miner-agent-harness.md) (first-party) |

### New evidence for existing options
- **Governed semantic layer with owned definitions.** Airbnb's Minerva holds 12,000+ certified metrics, defined in GitHub and code-reviewed. They feed experiments, dashboards and automated executive reports — [minerva](../../research/sources/airbnb-tech-minerva-metric-consistency.md) (first-party, 2021).
  - Spotify's Vedder uses expert-curated clusters with health scores (already filed) — [vedder](../../research/sources/spotify-engineering-vedder-context-layer.md).
- **Shared org knowledge edited by users.** AiKA (Spotify, Dec 2023 onward) prompted teams to improve their docs so the assistant answers better — [aika](../../research/sources/spotify-portal-blog-aika-data-plugins.md) (first-party).
  - In 2016, Airbnb's Knowledge Repo already named cross-individual synthesis as unsolved — [knowledge-repo](../../research/sources/airbnb-tech-scaling-knowledge-knowledge-repo.md) (first-party).
- **Counter-evidence: decisions kept tacit on purpose.** Airbnb's leadership principles live in "one shared consciousness" of 60–70 people, with no written list — [decoder-2024](../../research/sources/verge-decoder-chesky-founder-mode-2024.md) (first-party). A context layer that captures decisions would cut against that culture.

### Key questions to add
1. Can product rationale (why a bet, on what evidence) live in the same owned, health-scored catalog as systems context, or does it need a separate store? — *answered by:* a prototype catalog kind for a bet or brief; a Backstage/Portal maintainer.
2. In orgs that decide in the room, is a recorded decision log wanted at all, and by whom? — *answered by:* interviews with execs and program managers in the target org; Airbnb's and Spotify's own reluctance is the prior.

## artifact-and-project-structure: How PM artifacts and projects are structured, stored and found

### New options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| The ranked bet as the project container | A six-month bet (sponsor, success metrics, related bets, linked experiments) is the unit of commitment and the natural home for briefs, prototypes, PRs and results | Spotify bets board (2016 DIBB brief; 2025 stack rank of 30–50 bets) | Matches how the company already commits; one place to link evidence to work | No current written brief shown; links from bet to PRs and tests are not built yet | early-adopter (as a process); emerging (as an agent artifact) | [rhythm](../../research/sources/kniberg-spotify-rhythm.md); [ilb-soderstrom](../../research/sources/colossus-ilb-gustav-soderstrom-how-spotify-thinks.md); [office-hours](../../research/sources/claude-customers-spotify-office-hours.md) (first-party / vendor claim) |
| Roadmap row plus review schedule | Each project is a row on one company roadmap with a review cadence (1–12 weeks) and a green/yellow/red status kept by program managers | Airbnb since 2020 | Central visibility; a fixed place for an agent to prepare and record reviews | Review outcomes not recorded; depends on a CEO-centred model | mainstream (at Airbnb) | [lenny-chesky](../../research/sources/lenny-podcast-brian-chesky-new-playbook.md); [config-2023](../../research/sources/figma-config-2023-brian-chesky.md) (first-party) |
| Experiment decision record | Every experiment ends with a structured, explainable label (ship, abort, iterate) produced by a platform rule | Spotify Confidence; Airbnb ERF guardrails | Machine-readable "operate and learn" output that agents could cite | Covers measurable changes only; the link to the next plan is not described | mainstream (in these companies) | [risk-aware](../../research/sources/spotify-engineering-risk-aware-product-decisions.md); [ewl](../../research/sources/spotify-engineering-experiments-with-learning.md); [guardrails](../../research/sources/airbnb-tech-designing-experimentation-guardrails.md) (first-party) |

### New evidence for existing options
- **Living prototype library.** Spotify runs an internal "app store" of end-to-end prototypes built by anyone up to the co-CEOs — [office-hours](../../research/sources/claude-customers-spotify-office-hours.md) (vendor claim).
- **Repo-native conventions (docs-as-code).**
  - Spotify's fleet-change prompts are versioned in Git; TechDocs keep Markdown next to code — [agent-sdk](../../research/sources/claude-customers-spotify-agent-sdk.md) (vendor claim); [techdocs](../../research/sources/backstage-announcing-techdocs.md) (first-party).
  - Airbnb's metrics and research posts were reviewed by pull request — [minerva](../../research/sources/airbnb-tech-minerva-metric-consistency.md); [knowledge-repo](../../research/sources/airbnb-tech-scaling-knowledge-knowledge-repo.md).
- **A documented failure of artifacts drifting apart.** At Airbnb the concept brief "isn't updated" after prototyping, and reviews go out of order. A proposed "AI project coordinator" would keep brief, prototypes and Jira in sync — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md) (first-party). This argues for **Hybrid: repo canonical for long-form, platform for tracking, descriptor ties them**, plus an agent that keeps the parts in sync.

### Key questions to add
1. What is the project container in the target org: a bet, a roadmap row, an epic or a repo? Does the agent attach to it or create its own? — *answered by:* a review of the target org's planning tools; interviews with program managers.
2. Who keeps brief, prototype and tickets in sync once prototyping changes the plan, and can an agent do it without owning any of them? — *answered by:* a prototype "coordinator" agent on one live project; Airbnb's Dev AI team if reachable.

## target-user: Which users and personas we serve first, including for shared agents

### New evidence for existing options
- **Adjacent roles (designer, eng lead, PMM).** At Airbnb the PM's tasks are split four ways: product marketer (story and customer), program manager (plan and coordination), business lead (model and pricing) and designer — [config-2023](../../research/sources/figma-config-2023-brian-chesky.md); [decoder-2024](../../research/sources/verge-decoder-chesky-founder-mode-2024.md) (first-party).
  - An ex-insider calls the change "a little overblown" but "very liberating" — [loktev](../../research/sources/lenny-podcast-vlad-loktev-airbnb.md) (anecdote).
- **Head of product / CPO.** At Spotify the research → plan seam sits with VPs who pitch bets. At Airbnb the CEO is the product reviewer of every project — [ilb-soderstrom](../../research/sources/colossus-ilb-gustav-soderstrom-how-spotify-thinks.md); [lenny-chesky](../../research/sources/lenny-podcast-brian-chesky-new-playbook.md) (first-party).
- **Every employee including non-engineers.**
  - Airbnb: agentic-tool users are about twice the ~2,000 developers, and Insight Miner has more non-technical than technical users — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md); [insight-miner](../../research/sources/airbnb-tech-insight-miner-agent-harness.md) (first-party).
  - Spotify: PMs make small changes through Honk; a principal PM built a Claude Code plugin — [honk-1](../../research/sources/spotify-engineering-honk-part-1-1500-prs.md); [portal-tokens](../../research/sources/spotify-engineering-portal-claude-code-token-usage.md) (first-party).

### Key questions to add
1. Where the PM role is split (story, plan, prototype, business model), does the agent serve one role or carry context between all of them? — *answered by:* a task-level time study in the target org; an interview with an Airbnb product marketer or program manager.
2. Is the program manager's job (tracking, scoring, coordinating reviews) the most automatable part of product work, and who would own the agent that does it? — *answered by:* shadowing two program managers; a prototype that drafts a project's red/yellow/green status.

## pm-agent-evaluation: How we would know a PM agent works

### New evidence for existing options
- Both companies report activity, not outcomes:
  - Airbnb: "60% of code" AI-written or co-authored (definitions vary); features shipped up ~80%; concept-to-launch up to 60% faster — [q2-2026](../../research/sources/airbnb-earnings-q2-2026.md); [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md) (first-party).
  - Spotify: PR frequency +76%; features per six-month cycle "doubling", no count — [coding-constraint](../../research/sources/spotify-engineering-coding-no-longer-constraint.md); [q1-2026](../../research/sources/spotify-q1-2026-earnings-call.md) (first-party).
  - Chesky calls engineers' tool usage a "vanity metric" — [q4-2025](../../research/sources/airbnb-earnings-q4-2025.md).
- **Eval sets owned by the product decision-maker.** At Airbnb, AI-feature goals and gates are fixed up front; PMs label golden sets; 5% of production is sampled daily into a weekly PM review — [eval-driven](../../research/sources/airbnb-tech-eval-driven-development.md) (first-party).
- **Calibrate evals against outcomes.** "Without offline-online signal calibration, our evals are opinions, not evidence" — [llm-evals-funnel](../../research/sources/spotify-engineering-llm-evals-funnel.md) (first-party). Raw LLM predictions recovered only ~39% of a real A/B effect — [llms-ab](../../research/sources/spotify-engineering-llms-replace-humans-ab-tests.md) (first-party).

### Key questions to add
1. Can a PM agent's output be judged by the experiment record it leads to (ship, abort or iterate rates), as Spotify judges experiments? — *answered by:* Spotify's Confidence team; a back-test on past briefs and their experiment outcomes.

## work-structure: How structured the work is, what agent shape fits, and the unit of an agent

### New evidence for existing options
- **Task-specific agent per job.**
  - Airbnb: Insight Miner (research), Pascal (concept brief), @generateMock (prototype data), the migration framework, on-call agents.
  - Spotify: Honk (migrations, small changes), Vedder (data), AiKA (knowledge).
  - In both, named agents sit on one task each, inside a general harness — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md); [honk-1](../../research/sources/spotify-engineering-honk-part-1-1500-prs.md) (first-party).
- **Deterministic wrapper around an agentic core.**
  - Spotify's Fleetshift does targeting, scheduling and tracking deterministically; Honk only edits and verifies, with three tools — [honk-2](../../research/sources/spotify-engineering-honk-part-2-context-engineering.md); [honk-3](../../research/sources/spotify-engineering-honk-part-3-feedback-loops.md) (first-party).
  - Airbnb's migration loop is validate, transform, validate — [test-migration](../../research/sources/airbnb-tech-llm-test-migration.md).
- **Constrain by default, loosen with evidence.** Honk deliberately withholds code search and doc tools and condenses context into the prompt — [honk-2](../../research/sources/spotify-engineering-honk-part-2-context-engineering.md).

### Key questions to add
None new; see the agent-unit question already in the register.

## review-and-autonomy: Review and autonomy

### New options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Hidden deterministic verifiers before a PR exists | Verifiers the agent can't see run in the stop hook, then a separate service runs real CI. Only validated changes become PRs; the LLM judge is dropped | Spotify Honk | Fewer bad PRs reach humans; autonomy earned by checks, not by a judge | Needs strong tests; "passes CI but wrong" is still the worst failure; review volume still grows | early-adopter | [honk-3](../../research/sources/spotify-engineering-honk-part-3-feedback-loops.md); [qcon](../../research/sources/infoq-qcon-spotify-ai-codebase-migration-agent.md) (first-party) |
| Platform-encoded ship rule with reasons | A pre-agreed rule maps measured results to ship, abort or iterate and explains why | Spotify Confidence; Airbnb ERF guardrails (about 25 escalations a month in 2021) | Explainable, consistent release decisions | Only for measurable changes; more guardrails mean more false alarms | mainstream (in these companies) | [risk-aware](../../research/sources/spotify-engineering-risk-aware-product-decisions.md); [guardrails](../../research/sources/airbnb-tech-designing-experimentation-guardrails.md) (first-party) |
| Leadership review cadence as the gate | Every project is reviewed by the top leader on a fixed cadence and scored; autonomy is let out as trust builds ("golf instructor") | Airbnb | Coherence; one place for judgment | Doesn't scale past one person; decisions unrecorded; critics ask who tells the leader it has stopped working | mainstream (at Airbnb) | [lenny-chesky](../../research/sources/lenny-podcast-brian-chesky-new-playbook.md); [decoder-2024](../../research/sources/verge-decoder-chesky-founder-mode-2024.md); [cutler-perri](../../research/sources/cutler-perri-tbm-255-new-airbnb.md) (first-party / independent) |

### New evidence for existing options
- **Risk-scored routing with partial auto-approve.** Spotify auto-merges safe fleet changes (2.5M+ merged PRs, most with no human). After an auto-merged upgrade broke production, it added safeguards and scheduled changes in owners' working hours — [coding-constraint](../../research/sources/spotify-engineering-coding-no-longer-constraint.md); [quality-velocity](../../research/sources/spotify-engineering-quality-at-higher-velocity.md) (first-party).
- **Autonomy tiered by environment / earned from measured accuracy.** Airbnb's support agent went answer → personalise → act. AI search went from traffic slices to an opt-in toggle. Async on-call agents may close alerts but only propose fixes — [q2-2026](../../research/sources/airbnb-earnings-q2-2026.md); [latent-space-al-dahle](../../research/sources/latent-space-airbnb-al-dahle-inside-out-ai.md) (first-party).
- **Human review on every change** (Airbnb variant): the engineer must be able to explain any AI-written PR — [latent-space-al-dahle](../../research/sources/latent-space-airbnb-al-dahle-inside-out-ai.md).
- **Verification capacity as the limit** (new theme `verification-capacity-gap`). Spotify's merged changes went from about 8,100 to about 17,000 (August, year over year): "The next constraint became our ability to verify it" — [quality-velocity](../../research/sources/spotify-engineering-quality-at-higher-velocity.md). Airbnb's platform lead predicts "overwhelming code review" — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md).

### Key questions to add
1. When agents double the volume of change, where does verification capacity come from: more tests, auto-merge for reversible classes, or fewer changes? Who decides which classes are "safe"? — *answered by:* the target org's change-failure data; Spotify's published incident follow-ups; a control owner.

## intent-shaping-and-spec: Intent shaping mode and spec standard

### New options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Narrative-first intent | The launch story, keynote or press release is drafted first, with product marketing and comms, and shapes the product | Airbnb since 2020 | Clarity of the why and the customer story before building; a test of clear thinking | Evidence and edge cases may not be written down; depends on a strong editor (the CEO) | mainstream (at Airbnb) | [lenny-chesky](../../research/sources/lenny-podcast-brian-chesky-new-playbook.md); [config-2023](../../research/sources/figma-config-2023-brian-chesky.md); [decoder-2024](../../research/sources/verge-decoder-chesky-founder-mode-2024.md) (first-party) |
| Opportunity tree as the intent record | A tree from goal to data and insights, opportunities, hypotheses, solutions and learnings is the one required artifact, then a kick-off brief and a role-owned scorecard | Spotify Thoughtful Execution tree, Understand It Brief, Scorecard (2020–21) | Evidence linked to each hypothesis; clear phase gates by role | Kept optional; at least one page has lapsed; lives in docs and boards, not linked to code | early-adopter (lapsed?) | [thoughtful-exec](../../research/sources/spotify-design-thoughtful-execution-framework.md); [scorecards](../../research/sources/spotify-design-scorecards-alignment.md) (first-party) |
| Agent-drafted concept brief, then many prototypes | An internal app drafts a short brief from market research, the roadmap and objectives; pods build 5–10 high-fidelity prototypes and reason on those | Airbnb Pascal (2026) | Fast shaping; prototypes as the shared artifact | The brief drifts after prototyping (named by Airbnb); whether the brief cites evidence is unknown | emerging | [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md); [latent-space-al-dahle](../../research/sources/latent-space-airbnb-al-dahle-inside-out-ai.md) (first-party) |

### New evidence for existing options
- **Spec or goal with an executable verification contract.**
  - Spotify's rules for agent prompts: describe the end state, state when not to act, give examples, define done as tests, one change at a time — [honk-2](../../research/sources/spotify-engineering-honk-part-2-context-engineering.md).
  - A reused human migration guide made Honk guess; explicit mapping tables worked — [honk-4](../../research/sources/spotify-engineering-honk-part-4-dataset-migrations.md) (first-party).
- **Eval set or golden examples as the spec.**
  - Airbnb: research taxonomies became datasets and evals; PMs label golden sets; gates are fixed up front — [insight-miner](../../research/sources/airbnb-tech-insight-miner-agent-harness.md); [eval-driven](../../research/sources/airbnb-tech-eval-driven-development.md).
  - Spotify: offline evals pick treatments before A/B tests — [llm-evals-funnel](../../research/sources/spotify-engineering-llm-evals-funnel.md) (first-party).
- **Prototype-first.** Both companies now prototype in the real apps before committing: Spotify runs a prototyping phase before each bets cycle — [ilb-soderstrom](../../research/sources/colossus-ilb-gustav-soderstrom-how-spotify-thinks.md); Airbnb uses "the code and prototype is the artifact" — [latent-space-al-dahle](../../research/sources/latent-space-airbnb-al-dahle-inside-out-ai.md).

### Key questions to add
1. Which intent form survives in the target org: a narrative (Airbnb), an evidence tree (Spotify, lapsed), or a short brief plus prototypes plus evals? What made Spotify's frameworks lapse? — *answered by:* an interview with a Spotify designer or PM from Growth or Premium R&D; a review of the target org's last 10 specs.
2. Can an agent keep the brief true after prototypes change the plan, without anyone being asked to update it? — *answered by:* the coordinator prototype under artifact-and-project-structure.

## adoption-model: Adoption and enablement model

### New options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| Standardise for humans first, then agents | Golden technologies chosen by small advisory boards, enforced by monorepo, lint and shared skills, plus a software catalog with owners; agents work because the estate is uniform | Spotify | Agents succeed on uniform code; the same rules serve people and agents | Years of platform work before agents pay off; varied systems get dropped from automation (Scio pipelines) | early-adopter | [qcon](../../research/sources/infoq-qcon-spotify-ai-codebase-migration-agent.md); [coding-constraint](../../research/sources/spotify-engineering-coding-no-longer-constraint.md); [honk-4](../../research/sources/spotify-engineering-honk-part-4-dataset-migrations.md) (first-party) |

### New evidence for existing options
- **Mandates, leaderboards, proficiency ladder** versus organic adoption: both companies show both at once.
  - Airbnb's platform team says AirChat spread with no quotas or review link. Yet the CEO calls AI "existential", tracks token use and says winners run in "founder mode" — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md); [q2-2026](../../research/sources/airbnb-earnings-q2-2026.md); [fortune-60](../../research/sources/fortune-chesky-ai-60-percent-code-founder-mode.md).
  - Spotify's co-CEO: "We're retooling the entire company" — [q4-2025-spotify](../../research/sources/spotify-q4-2025-earnings-call.md).
- **Steering committee of builders who train their teams.** AirChat grew through a community of champions and train-the-trainer; usage went from 0 to 97% weekly over about three years, with a step after a model jump around Dec 2025 – Jan 2026 — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md) (first-party).
- **A precedent from experimentation.** Spotify grew experimenting teams from ~40 to ~300 (2018–22) with an engagement team, training and management expectation — [ewl](../../research/sources/spotify-engineering-experiments-with-learning.md) (first-party).

### Key questions to add
1. How much of Airbnb's and Spotify's agent adoption depends on prior platform standardisation that the target org lacks? — *answered by:* a codebase and catalog audit in the target org; comparison with Spotify's golden-tech coverage.

## agent-interface: Agent interface: own app, chat, or embedded

### New evidence for existing options
- **Chat-native.** Slack is Honk's front door. An engineer on a commute asked for an iOS fix, got a build by QR code, and merged it before reaching the office — [q4-2025-spotify](../../research/sources/spotify-q4-2025-earnings-call.md); [honk-1](../../research/sources/spotify-engineering-honk-part-1-1500-prs.md) (first-party).
- **Own app / workspace.**
  - Airbnb's AirChat Remote web UI shows many parallel async sessions with next-step buttons instead of chat. Domain teams build their own apps on the SDK in 2–4 hours — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md).
  - Spotify's Xirp offers multi-session, multi-vendor work — [xirp](../../research/sources/spotify-portal-blog-introducing-xirp.md).
- **Specialist agents exposed to other agents over MCP.** AiKA is both an MCP client and an MCP server — [aika-hub](../../research/sources/spotify-portal-aika-hub.md); [sdtimes](../../research/sources/sdtimes-spotify-portal-ga.md).
  - For a large API, Spotify chose a CLI plus an OpenAPI spec over MCP to keep the API out of context — [ads-plugins](../../research/sources/spotify-engineering-ads-api-claude-plugins.md).
- **Rich UI over chat for product work.** Chesky publicly prefers rich, visual interfaces to chat. Airbnb's AI search is "less chatty" and visual — [q2-2026](../../research/sources/airbnb-earnings-q2-2026.md). Product marketers and the CEO review prototypes and keynotes, not documents.

### Key questions to add
None new.

## trust-privacy-defaults: Trust and privacy defaults for sessions and context

### New evidence for existing options
- **Isolation / task-scoped permissions.**
  - Spotify's Honk runs in a container with few binaries and almost no access to other systems, and can't push — [honk-3](../../research/sources/spotify-engineering-honk-part-3-feedback-loops.md).
  - Airbnb's remote agent workspaces are network-isolated from production and user data, and production samples are de-identified before human review — [dx-airchat](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md); [eval-driven](../../research/sources/airbnb-tech-eval-driven-development.md) (first-party).
- **A permissions gap.**
  - Spotify Portal's actions registry does not enforce permissions; each tool must check — [portal-mcp](../../research/sources/spotify-portal-docs-mcp.md).
  - AiKA reportedly runs third-party MCP actions without confirmation; this comes from a search snippet of a 404'd page.
  - Airbnb's CTO says connector security for email and Slack is unsolved — [deepview](../../research/sources/deepview-al-dahle-airbnb.md).
- **Open by default for planning.** Spotify's bets board was a sheet open to everyone (2016) — [rhythm](../../research/sources/kniberg-spotify-rhythm.md). Agent sessions' defaults are not described for either company.

### Key questions to add
1. Who checks permissions when an agent reaches internal tools through a shared actions registry: the registry or each tool? — *answered by:* the target org's security owner; a review of Backstage's MCP actions design.

## Proposed new dimensions

None. Two candidates to raise with the director:

1. **"Where the research → plan seam sits"** (peer level vs leader level). Airbnb and Spotify put it at a leader (CEO review, VP pitch), while Stripe, Intercom and Ramp put it between peers. This may be a key question under target-user rather than a dimension.
2. **"Decision record"** (whether reviews and bets are written down for agents). This may fold into artifact-and-project-structure.

## Cross-cutting key questions

1. In orgs where a senior person carries the evidence into the plan (Airbnb's CEO, Spotify's VPs), does an agent help that person or replace the need for them? — *answered by:* interviews with two product VPs; a prototype that drafts a bet from linked research.
2. Both companies now sell or open-source their internal context layers and harnesses (Spotify Portal, Confidence, Xirp; Airbnb's Knowledge Repo earlier). Is the moat the harness or the org context it reads? — *answered by:* more research on Spotify Technology's customers; the build-vs-buy dimension owner.
