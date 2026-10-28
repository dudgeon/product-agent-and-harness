# The MVP: which value types to build first, and why

Date: 2026-10-28. Part of the dependency-agent research (see [00-summary.md](00-summary.md)). Of the seven value types in [04-destination.md](04-destination.md), this document recommends the two to build first and one to build in a limited form, with the reasoning (value, feasibility in a limited-context environment, what it teaches, what it builds toward); what the MVP must not try to do; what "agent-ready" means for a platform, as a checklist; the key questions and risks; and the alternatives rejected and what would change the choice. The project aggregates options rather than converging, so this is a lean with its reasons, and the alternatives are kept visible. Evidence is in `../../research/sources/`, labelled.

## 1. The recommendation

Build **V1 Discovery and mapping** and **V6 Context curation and write-back** as the core, and **V4 Routing and asking** in its crawl form (the agent drafts, a person sends, the agent tracks). Build them as one loop, because each is weak alone:

- discovery produces the map and the "could not find" list;
- asking turns each gap and each dependency into the smallest question for a named owner, which a person sends;
- write-back records every answer with owner, date and source, in a standard shape, so the next map starts further along.

Call it the **map-ask-record loop**. Its unit of work is one feature's dependency session, open for weeks, with the product owner steering. It fits the working hypothesis directly: the agent creates value in a limited-context environment by aggregating and curating context, and by producing a standard shape for platform cards and asks that platforms can adopt.

## 2. The reasoning per value type

| Value type | Value now | Feasible with thin context? | What it teaches | What it builds toward | Verdict |
|---|---|---|---|---|---|
| V1 Discovery and mapping | High: late discovery is the named cause in the independent evidence ([NAO](../../research/sources/nao-framework-to-review-programmes.md), [FCA](../../research/sources/fca-implementing-technology-change.md), [HHS OIG](../../research/sources/hhs-oig-healthcare-gov-case-study.md)); no shipped product does it ([04](04-destination.md), section 1.1) | Yes, if every edge is sourced or flagged; partial maps with explicit gaps are the honest product of a crawl environment | Where the context is thin, per platform and per dependency type; which owners answer | Every other value needs the map | **Core** |
| V6 Write-back and curation | Medium now, compounding later; the measurement nobody has (lead time per platform) is a side effect | Yes; it needs a store with a schema and owners who verify, which is the thing being tested | Verification rate, staleness rate, reuse rate: whether compounding is real | The walk environment: platform cards, published intake, measured lead times | **Core** |
| V4 Routing and asking | High: the chasing job is measured ([Microsoft Research](../../research/sources/microsoft-research-coordination-large-scale-development.md): 49% chase status, 67% see changes unannounced); targeted chasing works ([Nudge](../../research/sources/arxiv-maddila-nudge-overdue-pull-requests.md)) | Drafting and tracking: yes. Sending as the agent: needs identity and channel trust that a crawl environment lacks | Which channels owners read; response rates; what makes an ask answerable | Walk-stage posting and chasing under rules | **Crawl form only**: agent drafts and tracks; a person sends |
| V3 Sequencing | Medium; today's tools already check dates | Partly: the calendars are not data ([04](04-destination.md), ladder) and a precise plan on guessed lead times is worse than a rough one | Lead times, as a by-product of V6 | The walk environment's calendar rung | Not in the MVP beyond "proposed order with assumptions tagged" |
| V2 Intake translation and submission | High where a platform has an intake schema; nil where it has a form in an email | Only for platforms that already publish a schema; needs agent identity and a policy | Which platforms could accept an agent request | The run environment | Not in the MVP; pre-filling a form from the spec is a cheap extra once V1 exists |
| V5 Governance evidence assembly | High in regulated organisations; also the highest risk | Pre-screening applicability from published criteria is feasible; assembling packets needs the gate's evidence list as data, which few gates have | Which gates are data gates | The run stage for data gates | Not in the MVP; the applicability pre-screen is a candidate second step |
| V7 Portfolio signal | High for platform owners and governance owners | Needs many sessions | Where the organisation waits | Governance redesign | Not in the MVP, but the MVP must collect the data for it from session one |

Two reasons the core is V1 plus V6 rather than V1 plus V4 or V1 plus V5:

1. **V6 is the one that compounds, and the one the evidence says to do first.** Stripe verified its documentation before putting a bot over it, and the beacons' agents got better because corrections were captured in the flow of work ([Stripe panel](../../research/sources/stripe-sessions-2024-10x-engineer-panel.md); [Shopify River](../../research/sources/venturebeat-beyond-the-pilot-farhan-thawar.md), first-party). An MVP that maps and asks but does not record repeats the status quo: the knowledge leaves with the session.
2. **V5 is where automating badly does the most harm**, and the data gates it needs barely exist outside change approval ([02](02-challenges.md), section 2.4). A first agent that is seen to make a gate easier to skip, or that assembles a packet from a stale source, loses the trust of the second line, which is the trust the whole programme needs. It should be the second step, not the first.

## 3. What the MVP must not try to do

- **Not send, submit or approve anything unaided.** Rights: agent proposes, a person decides, everywhere. A human sends the first batch of asks and every batch after until a labelled sample says otherwise.
- **Not decide at any governance gate**, and not advise that a gate can be skipped. It may say which gates appear to apply and why, from published criteria, with the criteria cited.
- **Not invent an edge.** No dependency without a source; no owner without a source or an "inferred, unconfirmed" tag; no date without a source or an "assumed" tag. Zero-shot over-prediction is documented ([LEREDD](../../research/sources/arxiv-darif-leredd-requirement-dependencies.md)).
- **Not chase.** Tracking, yes; reminders, no, until the walk stage, because untargeted bot volume gets switched off ([Dependabot](../../research/sources/arxiv-he-dependabot-exploratory-study.md)) and the chase rules need an identity and a channel decision the MVP does not have.
- **Not ask an owner to verify anything the feature does not need.** Verification rides on real asks.
- **Not write back as fact.** Every entry is provisional until a named person verifies it, and the map shows which entries are provisional.
- **Not build a new catalogue.** It reads what exists, writes its cards to a store the organisation already trusts (a repository, a wiki space with owners, a catalogue), and links platform objects rather than copying them.
- **Not report on people.** The timings it collects are per platform and per gate, for V7 later; they are not a league table of owners.

## 4. What "agent-ready" means for a platform: a checklist

A platform owner can act on this list without waiting for the agent. Items 1 to 4 are the walk environment; 5 to 7 are the run environment. Each item names the thing that exists today (from the legibility ladder in [04](04-destination.md)).

1. **A platform card, owner-verified and dated.** Purpose, what it does and does not do, the owning team with a named person, the contract (API specification, data contract), lifecycle. Verified on a date; expires if not re-verified. (Exists today as a Backstage or Port entity with an owner field; the verification date is the addition.)
2. **Intake described in one place, in the common shape.** What the platform needs from a consumer, what it checks, who approves, and the route in. Prose is fine at walk; the point is that there is one answer to "how do I get onto this". (NHS England's onboarding guidance is the model for completeness; its gap is lead time.)
3. **Lead times measured and published.** Intake to first response; first response to decision; decision to access. Measured from real requests, not promised. (No source found publishes these; the agent's timings are a way to get them.)
4. **A calendar.** Release trains, freezes, planning windows, as a page the agent can read and later as data.
5. **Intake as a schema with an endpoint.** The form as JSON Schema or equivalent; a request endpoint that accepts "on behalf of" and returns a status; approvers and policy declared next to the schema. (Backstage templates, Kratix promises, Score, portal registration forms and data-product access requests all have the schema; approval is the usual gap.)
6. **Decisions recorded automatically.** Every intake decision written with its evidence linked, in a form an auditor accepts. (Pipeline change records and access-package audits do this today.)
7. **Agent-compatible identity.** The platform accepts a request from an agent with a sponsor, acting for a named person, records both, and can revoke the agent without touching the person. (Entra agent access packages and SailPoint's "Requested by AI on behalf of" show the shape.)

A platform at 1 to 4 can be mapped and asked well. A platform at 5 to 7 can be submitted to. The agent's map should show each platform's position on this list, which is itself a prompt to the platform owner.

## 5. The MVP's shape

- **Where it runs.** In a shared, persistent session per feature, in the harness the organisation already runs, with the product owner as the steerer and owners joining to answer; the project's shared-persistent-agents synthesis sets out the conditions (durable session, identity decided, a visibility default, a place to report and ask, a human gate on side effects, a curate step on anything that compounds) ([synthesis](../research-shared-persistent-agents/01-synthesis.md)).
- **What it reads.** The catalogue(s), the CMDB, ownership files, the ticket tool, the wiki, past sessions and decision records, and the public guidance of each gate; all read-only, scoped per session.
- **What it writes.** The map with evidence; the open-question register; the ask drafts; the platform cards and decision entries, provisional, to the agreed store; its own timings.
- **How it is checked.** The skill-spectrum profile for the crawl stage: path code-fixed for the stages (read, map, check, draft asks, record), model-chosen within them; deterministic checks that every edge has a source and every card has owner, date and source; a fresh-context reader test of the map against the dependency-type checklist; the product owner reviews asks before sending; a weekly labelled sample of maps and cards graded by the owners who know. The map, the register and the cards are the record; corrections are the loop.
- **The three numbers it reports from week one.** Verification rate (share of its proposed cards and answers a named owner verified), reuse rate (share of a new session's edges that came from a previous session's verified entries), and wait time per platform and gate. The first two test compounding; the third is the measurement nobody has.

## 6. What the MVP teaches, and the decision it sets up

After a quarter of sessions on real features, the organisation will know: which platforms answer and which do not; which dependency types the agent finds and which it misses (expect the system-to-system ones to be found and the support-function and third-party ones to be the gaps); whether owners verify when asked the smallest question riding on a real ask, and at what rate; how long each platform's intake actually takes; and whether a second session on a related feature starts further along. Those answers decide whether the next step is the walk agent (posting and chasing under rules, with an identity) or the walk environment (platform cards and published intake for the platforms that proved slowest), and the maturity model's rule says the environment goes first.

## 7. Alternatives rejected, and what would change the choice

| Alternative | Why it is attractive | Why not first | What would change the choice |
|---|---|---|---|
| **Governance evidence first (V5)** | The pain is sharpest at the gates in a regulated organisation; change approval already has machine-readable intake | Highest harm if done badly; most gates lack an evidence list as data; trust of the second line is at stake | A sponsor in the second line who wants it, and a change process whose criteria are already published and checkable; then V5's applicability pre-screen is a strong second step |
| **Intake submission first (V2)** | The intake rung is the most machine-readable; a visible "the agent got us onto the platform" moment | Needs agent identity, delegation and a policy per platform, which a crawl environment does not have; nil value on platforms whose intake is a form in an email | Two or three platforms already at checklist items 5 to 7; then V2 on those platforms is a cheap, visible win |
| **Chasing first (V4 at walk)** | The measured pain (49% chase status); Nudge's 60% result | Needs an identity and a channel decision; bot noise risk before trust exists | An organisation that already runs agents in its channels with an identity model; then chase rules can be the first autonomy earned |
| **Sequencing and re-planning first (V3)** | The visible product of planning tools; the film's "re-plan on day nine" beat | Calendars and lead times are not data; precise plans on guessed inputs mislead | Published release calendars and measured lead times for the platforms in scope |
| **Portfolio signal first (V7)** | The thing platform owners and governance owners would pay for | Needs many sessions; nothing to aggregate on day one | Nothing changes the order; V7 is the payoff of doing V1 and V6 on enough features |
| **A standalone context-creation agent** | Geoff's earlier hypothesis; the catalogue is the bottleneck | The project's earlier finding: capture as a by-product of work is what has worked; a standalone curation agent floods owners with requests that ride on nothing | Evidence that owners verify unprompted at a useful rate; none found |
| **Buy a vendor planner (Asana, ServiceNow, Planview)** | Shipped; critical path, alerts, re-plan proposals | None discovers undeclared dependencies or routes across platforms; each sees only its own graph; no outcome evidence | A vendor shipping discovery across platforms with sourced edges and a write-back store; worth re-checking each quarter |

## 8. Key questions and risks

Questions only the organisation can answer, each with who or what answers it:

1. **Where does dependency context live today, and how long does assembling it take for a recent feature?** A context audit of two or three shipped features, with the product owners. Decides how thin "thin" is.
2. **Will owners verify when asked the smallest question riding on a real ask, and at what rate?** The MVP's first quarter. Decides whether compounding is real.
3. **Which store will the organisation accept as the home for platform cards and decision records, and who owns it?** Platform engineering and the second line. Decides V6's write target and whether audit accepts it.
4. **What identity will the agent have when it moves to the walk stage, and who sponsors it?** Identity and security owners, from the project's identity register. Decides when V4 can post and V2 can submit.
5. **Which gates will publish their criteria and evidence list in checkable form?** The change, security and privacy owners. Decides whether V5 is a second step or a third.
6. **Which two platforms are the slowest and most-depended-on, by the MVP's own timings?** The MVP. Decides where the walk-environment investment goes first.
7. **Does the second line accept an agent-assembled packet as first-line evidence, with the agent's identity on it?** Risk and audit. Decides V5's ceiling.

Risks, with the mitigation the evidence suggests:

- **Owners ignore the agent.** Mitigation: verification rides on real asks; the smallest question; a person sends; watch the response rate per channel from week one ([Nudge](../../research/sources/arxiv-maddila-nudge-overdue-pull-requests.md), [Wessel](../../research/sources/arxiv-wessel-dont-disturb-me-bots.md)).
- **The map is confidently wrong.** Mitigation: no edge without a source; provisional until verified; the reader test against the type checklist ([LEREDD](../../research/sources/arxiv-darif-leredd-requirement-dependencies.md)).
- **The record decays as fast as it grows.** Mitigation: expiry on unverified entries; staleness measured; cards generated from systems where possible ([Port](../../research/sources/port-state-of-idp-2025-metadata-trust.md), [ServiceNow CMDB](../../research/sources/servicenow-cmdb-health-kpis-metrics.md)).
- **The agent becomes the new ticket queue.** Mitigation: it does not hold requests; it drafts them into the platform's own route and tracks them there.
- **The standard shape is rejected by platform teams.** Mitigation: it is the agent's output format first and the platform's input format only by adoption ([NAO on Verify](../../research/sources/nao-investigation-into-verify.md)).
- **Visibility chills.** Mitigation: timings per platform and gate, never per person; the project's privacy defaults apply ([Bernstein](../../research/sources/asq-bernstein-transparency-paradox.md)).
- **Priority churn, not dependencies, is the real cause of slip.** Mitigation: the ask register records "waiting on a platform whose priorities changed" as its own state, so the larger cause is visible ([DORA 2024](../../research/sources/dora-accelerate-state-of-devops-2024.md)).

## 9. Options by dimension

The register entries this task proposes are in options/contributions/research-dependency-agent.md: rows and key questions for context-and-memory, governance-control-plane, session-persistence-sharing, agent-identity-delegation, target-outcome, sequencing, review-and-autonomy, adoption-model and trust-privacy-defaults, and one proposed new dimension, dependency-knowledge-and-intake (where dependency knowledge lives, who verifies it, and how far the agent may act on platform intake).
