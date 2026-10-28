# A dependency taxonomy for product intent, with the agent's triage questions

Date: 2026-10-28. Part of the dependency-agent research (see [00-summary.md](00-summary.md)). Geoff asked for a representative MECE taxonomy (mutually exclusive, collectively exhaustive) of the kinds of dependency any product intent should be assessed for, with the agent-led triage questions that could explore and complete each. This document gives the taxonomy, the test that makes it MECE, the triage questions per class, and the order in which an agent should ask them. It draws on the practices and evidence in [01](01-dependency-management-today.md) and [02](02-challenges.md); the taxonomy itself is this research's design, and the questions are written to be used as a checklist an agent (or a programme manager) runs against an intent.

## 1. The partition principle

A dependency is something the work needs that the team does not control. To make the classes mutually exclusive, the taxonomy partitions by **the kind of act the outside party must perform** for the dependency to be resolved. Six acts cover the space:

| Class | The outside party must... | Resolved when... |
|---|---|---|
| **A. Build** | Make or change something | The thing exists in the form the work needs, and the owning team has committed to it |
| **B. Grant** | Give access to, or a path to, something that already exists | The work can reach the thing, under terms it can live with |
| **C. Decide** | Approve, sign off, or rule | A named role has recorded a yes (or a no, or a condition) |
| **D. Fund** | Pay for it, or allocate capacity to it | Money or capacity is committed against a named line |
| **E. Align in time** | Make dates line up | The sequence and the calendars are consistent and committed |
| **F. Tell** | Supply knowledge the work needs and nobody has written down | The answer is recorded with an owner, a date and a source |

The test for exclusivity: ask "what act resolves it?" A privacy assessment is C (someone must rule), even though it concerns data; the data itself is B (someone must grant access). A platform team's work on your feature is A (they must build), but their prioritising it against their backlog is D (they must allocate capacity), and the release train it must ride is E. If one real-world item needs several acts, it is several dependencies, and the agent should record it as such; that is a feature of the partition, not a flaw, because each act has a different owner, a different route and a different wait.

The test for exhaustiveness: every dependency named in the research (team, system, data, process gate, approval, vendor, funding, people, sequencing, knowledge; Strode and Huff's task, resource and knowledge types; the RAID log's "external reliance") lands in exactly one class once its resolving act is named. Vendors, for example, are not a class of their own: a vendor must build (A), grant (B), or be approved (C), and the agent should say which.

## 2. The taxonomy

Each sub-class gives: what it is, an example from the fictional insurer in [01](01-dependency-management-today.md) (Lantern Mutual, labelled fictional), where the agent would find it, and who typically resolves it.

### A. Build: someone must make or change something

| Sub-class | What it is | Fictional example | Where the agent finds it | Who resolves it |
|---|---|---|---|---|
| A1. Internal system or service change | An owned system must expose, change or support a behaviour | Rating must re-rate a policy mid-term; billing must add an instalment option | Catalogue relations, API specs, past integrations, tickets | The owning team |
| A2. Platform capability | A shared platform must add or extend a capability for this consumer | Document generation must regenerate an ID card after an endorsement | Platform cards, golden-path templates, platform backlog | The platform team |
| A3. Third-party deliverable | An external party must build, change or deliver | The vehicle-data vendor must add a field; a consultancy must deliver a module | Contracts, vendor roadmaps, the third-party register | Vendor management, the vendor |
| A4. Content, configuration and rules | Non-code artefacts must be produced by another team | Actuarial rate tables; disclosure wording per state; product configuration | Product configuration systems, legal and actuarial teams | The owning function |

### B. Grant: someone must give access to something that exists

| Sub-class | What it is | Fictional example | Where the agent finds it | Who resolves it |
|---|---|---|---|---|
| B1. Data access and terms | Data another domain owns, under its classification, consent and sharing terms | Vehicle and driver records; consent flags for both | Data catalogue, data contracts, data-product access requests | The data owner or domain |
| B2. Platform and environment access | Entitlements, environments, credentials, quotas, client registration | Non-production credentials for the identity platform; an API client on the gateway | Identity and access systems, portal registration, environment requests | Platform team, identity team, approvers |
| B3. Interface and contract reliance | A specific interface version the work relies on, and its deprecation and change terms | The rating API v2 contract; the mobile platform's SDK version | API specs, contract registries, deprecation notices | The provider, via consumer-driven contracts |
| B4. People and expertise availability | A scarce person's time, as a resource rather than as knowledge | Ruth's availability for two weeks of filing work | Rotas, allocation plans, the person | Their manager |

### C. Decide: someone must approve, sign off, or rule

| Sub-class | What it is | Fictional example | Where the agent finds it | Who resolves it |
|---|---|---|---|---|
| C1. Technical governance gates | Change authority, architecture review, security review and threat model | The change record for the rating release; the architecture review of the integration pattern | Gate criteria pages, the change calendar, past records | Change authority, architecture and security review |
| C2. Risk and compliance gates | Privacy assessment, model risk, third-party risk, records and audit evidence | A privacy assessment because two of the published triggers apply; model-risk tiering if a pricing model is touched | Published screening criteria, inventories, registers | Second-line functions |
| C3. Business decision rights | A named role must say yes on a business question | Actuarial sign-off on a mid-term re-rate; pricing approval; brand and legal on wording | Decision-rights documents, past decisions | The named decider |
| C4. External regulatory approval | A regulator or external body must accept a filing or grant a permission | A state rate or form filing; a regulator's no-objection | Filing systems, regulatory calendars, the filings archive | The regulator, via the filings team |

### D. Fund: someone must pay or allocate capacity

| Sub-class | What it is | Fictional example | Where the agent finds it | Who resolves it |
|---|---|---|---|---|
| D1. Funding and business case | Money must be approved against a cost centre or a demand | The billing platform's work needs a funded demand with a business case | Portfolio and demand-management tools | Portfolio owner, finance |
| D2. Capacity allocation and prioritisation | The owning team must place this work in its plan ahead of other work | Rating's next planning window is in seven weeks; this must make the cut | Roadmaps, planning boards, backlog | The owning team's product owner |
| D3. Chargeback and internal agreement | A charging or service agreement must be in place to consume | The document-generation platform charges per render; an internal agreement is needed | Service catalogues, internal contracts | Platform owner, finance |

### E. Align in time: dates must line up

| Sub-class | What it is | Fictional example | Where the agent finds it | Who resolves it |
|---|---|---|---|---|
| E1. Sequencing | This cannot start or finish until that has | Bind cannot ship before the billing contract and the security review | The map itself; the plan | The product owner, with the owners of the predecessors |
| E2. Cadence and calendar alignment | Release trains, freezes, planning windows and maintenance windows that must coincide | The mobile train and the platform train ship on different dates; a year-end freeze | Release calendars, train schedules, freeze notices | Release and train managers |
| E3. External and regulatory dates | Effective dates, contract expiries, market events the work must meet or avoid | A state disclosure rule effective on a fixed date; a vendor contract renewal | Regulatory calendars, contracts | Nobody; the date is a constraint to plan around |

### F. Tell: someone must supply knowledge nobody wrote down

| Sub-class | What it is | Fictional example | Where the agent finds it | Who resolves it |
|---|---|---|---|---|
| F1. Tacit knowledge | What only an experienced person knows | Whether a self-service endorsement counts as a filed rule | It does not; the agent finds the gap and the person | The person who knows |
| F2. Open decisions and assumptions | Questions whose answer changes scope, not yet decided by anyone | Whether phase one ships in twelve states or four | The open-question register | The product owner, or a named decider (which makes it C3 once routed) |
| F3. Record conflicts and staleness | Two sources disagree, or the record names an owner who left | The catalogue says API re-rate; the runbook says overnight batch; billing's owner left in the spring | The agent's own cross-checks | The owner who can settle it |

Class F is the one most taxonomies omit and the research says is where the delay sits: the slow edges are support functions, external parties and "the person who knows" ([Tkalich et al.](../../research/sources/arxiv-tkalich-critical-dependencies-cse.md), independent; [Stack Overflow 2024](../../research/sources/stackoverflow-dev-survey-2024-professional-developers.md), independent). F-class items are usually temporary: once answered and recorded, they become an A, B, C, D or E item or disappear.

## 3. The agent's triage questions

The questions are written to be asked of the intent and of the context, not of the product owner, wherever the context can answer them; the agent asks a person only what it could not read (the rule the project's skill-spectrum guide sets: never ask what you can read). Each question says what the agent does with the answer.

### Screening: the first pass over any intent

Run before the classes, to decide which classes need expanding. The screening is modelled on published gate screenings such as the UK privacy regulator's two-of-nine triggers ([ICO](../../research/sources/ico-when-do-we-need-a-dpia.md), regulator).

1. Which systems of record does this intent read from or write to? (Each answer opens A1 and B3.)
2. Which shared platforms does it consume, and is this team already onboarded to each? (Each "not yet" opens A2, B2, D3 and the onboarding cascade.)
3. Which data does it need that this team does not own, and what is its classification? (Opens B1; personal or special-category data opens C2.)
4. Does it change a price, a rate, a rule, a disclosure or a filed form? (Opens A4, C3, C4.)
5. Does it use or change a quantitative model, including a vendor or AI component? (Opens C2 model risk.)
6. Does it involve a third party, new or existing? (Opens A3, C2 third-party risk, E3.)
7. Does it need work from another team that is not already on their plan? (Opens D1, D2.)
8. Which release vehicles would it ride, and are there freezes or windows in the period? (Opens E2.)
9. What has to be true before each phase can start, and who has to say so? (Opens E1, C3, F2.)
10. What did the agent fail to find, and what disagreed? (Opens F1 and F3; this is the "could not find" list and it is never empty on the first pass.)

### A. Build

- For each system or platform touched: does the behaviour the intent needs exist today, or must it change? *Source: catalogue, API spec, a past integration. If unknown, flag F3 and ask the owner the smallest question: "Does the rating API re-rate mid-term today? The catalogue says yes, the runbook says batch."*
- Who owns it, by what evidence, and when was that verified? *Source: catalogue owner field, CODEOWNERS, the last three tickets answered. If the owner has left or the record is older than the expiry, propose the inferred owner and ask them to confirm.*
- Is the change on the owning team's plan, and if not, what is the route to get it there? *Opens D2; the route is the platform's intake, from its card.*
- What is the platform's intake, what does it check, and what evidence does it want from this team? *Source: the platform card and intake description. If none exists, this is a checklist gap for the platform owner.*
- For a third party: what does the contract allow, what change process does the vendor run, and who in vendor management owns the relationship? *Source: the third-party register.*
- For content and rules: which function produces it, in what system, and what is their lead time? *Source: past features of the same kind.*

### B. Grant

- For each data set: who owns it, what is its classification, what consent or purpose limitation applies, and is there a data contract or access request route? *Source: data catalogue, data contracts. If the data is personal, raise the C2 privacy screen now rather than later.*
- Does this team already hold access to each platform and environment, and at what level? *Source: entitlement records. For each gap: the access-request route, its approver and its measured lead time; if no lead time is published, time this request and record it.*
- Which interface versions does the intent rely on, and what are their deprecation dates and change terms? *Source: contract registry, deprecation notices. Register this team as a consumer so the provider can see the reliance.*
- Which scarce people must be available, for how long, and when? *Source: the plan; confirm with their manager. Keep this separate from F1: availability is a grant; the answer they hold is a tell.*

### C. Decide

- Which technical gates apply, by their published criteria, and what evidence does each want? *Source: gate pages. Produce the evidence list per gate and the share already satisfied by the spec and the map. Never conclude a gate does not apply without citing the criterion.*
- Which risk and compliance screens trigger? *Run each published screening (privacy triggers, model-risk scope, third-party criticality, records and retention). Pre-fill the assessment where one is needed and route it; the agent is first-line only and does not assess.*
- Which business decisions does the intent need, who holds each decision right, and has an equivalent decision been made before? *Source: decision records, decision-rights documents. If a prior decision exists, cite it and ask only whether it still applies.*
- Does anything need an external approval or filing, in which jurisdictions, and what is each regulator's process and calendar? *Source: the filings archive and regulatory calendar. If the archive does not answer whether this case is a filed item, that is an F1 question for the filings expert, and it decides scope.*
- For every gate: what is its measured lead time, and if none is measured, when did this request enter the queue? *The agent's own timing is the first measurement.*

### D. Fund

- Is the work on the other team funded, and against what line? *Source: the demand or portfolio record. If not, draft the demand from the spec with the business case fields the tool wants, and show who approves it.*
- Where does this sit in the owning team's priorities, and what would move it? *Ask the owning product owner the smallest question: "Can this make your next planning window on the eleventh, and if not, what date can you commit to?" Record the answer as a commitment or a counter-date, as the Jira Align pattern does ([Eficode](../../research/sources/eficode-manage-dependencies-jira-align.md), vendor).*
- Does consuming the platform need a charging or service agreement, and does one exist for this team? *Source: service catalogue, internal contracts.*

### E. Align in time

- For each phase: what must be complete before it starts, and who confirms completion? *Draw the sequence from the map; every edge sourced or assumed-and-tagged.*
- Which release vehicles does each phase ride, when do they ship, and what freezes fall in the period? *Source: release calendars. Where calendars are not published, ask the release manager once and write the answer to the platform card.*
- Which external dates bind: effective dates, expiries, events? *Source: regulatory calendar, contracts. Mark them as constraints, not dependencies on a person.*
- When something moves, which commitments move with it, and who must hear? *Re-plan from the sequence; tell only the affected owners, once; a person accepts any move to a commitment.*

### F. Tell

- What did the agent look for and not find? *List it. Each item becomes a question to a named person, or a checklist gap for a platform owner.*
- Which open questions change scope, and who can close each? *Put them in the open-question register with an owner and a blocking flag; the product owner decides which to route and which to assume.*
- Where do two records disagree, and who can settle it? *Route the smallest question with both sources attached; when answered, strike through the stale record with the superseding source and the owner's name.*
- Who holds the knowledge this intent needs, and is there a prior answer from them on record? *Search decision records and past sessions first; ask only what is not there; write the answer back with owner, date and source so the next team does not ask again.*

## 4. The triage sequence

The order matters, because later classes depend on earlier answers and because asking a person before reading the record is the failure the research warns against.

1. **Read, then screen.** The agent reads the spec, the catalogue, the platform cards, the decision records and past sessions, and runs the ten screening questions. Nothing is asked of a person yet.
2. **Expand the open classes.** For each class the screen opened, run its questions against the context. Every finding gets a source, a confidence and an owner; every gap goes on the "could not find" list.
3. **Cross-check.** Compare sources that should agree (catalogue against runbook, owner field against recent tickets, contract against spec). Disagreements become F3 items.
4. **Draft the asks.** One per item that needs a person: the smallest question, the requirement it serves, the evidence attached, what happens if the answer is no, and the owner and channel. Group by owner so nobody gets five messages.
5. **The product owner reviews and sends.** At the crawl stage a person sends; the agent tracks.
6. **Record every answer** with owner, date and source; close the item or convert it (an F item becomes an A, B, C, D or E item); strike through superseded records.
7. **Re-screen on change.** When the spec changes or an answer arrives, re-run the screen on what changed; tell only the affected owners.

## 5. Using the taxonomy as a completeness check

The classes double as the deterministic check the skill-spectrum guide recommends for process artefacts: a map is incomplete if any class the screen opened has no items and no explicit "none found, because" note. The check is cheap to script and honest: it does not grade the content of the map, only whether each class was looked at. The research says the classes most likely to be empty by omission are C, D and F, because they live in forms, portfolios and people rather than in code, and those are the ones that cause the most delay. An agent that shows those rows as "not yet assessed" rather than leaving them out has already done something today's tools do not.
