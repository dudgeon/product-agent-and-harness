# The context layer: where the work lives, what the organisation's context is made of, how use builds it, and what the destination needs

Date: 2026-10-31. Part of the definition of two enterprise product capabilities, intent shaping and delivery dependency mapping (overview in [00-overview.md](00-overview.md); concept briefs in [05-concept-intent-shaping.md](05-concept-intent-shaping.md) and [06-concept-delivery-dependency-mapping.md](06-concept-delivery-dependency-mapping.md); the structured inquiry both modules run in [02-structured-inquiry.md](02-structured-inquiry.md)). This document describes the **context layer**: the home of each feature's intent lifecycle (section 1), the enterprise context artifacts the modules read and write (section 2), the raw sources those artifacts can be built from on day one (section 3), the flywheel by which use builds the layer and tells the organisation what to build next (section 4), and the data sets, governed context and tools the destination needs (section 5). Its companion, [04-context-trust-criteria.md](04-context-trust-criteria.md), is the evaluation framework for what makes written-back context trusted.

It builds on the dependency-agent research ([destination](../research-dependency-agent/04-destination.md), [maturity model](../research-dependency-agent/05-maturity-model.md), [first move](../research-dependency-agent/06-mvp.md), [dependency taxonomy](../research-dependency-agent/09-dependency-taxonomy.md)) and the options register ([context-and-memory](../../options/DIMENSIONS.md#context-and-memory-context-and-memory), [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found), [dependency-knowledge-and-intake](../../options/DIMENSIONS.md#dependency-knowledge-and-intake-dependency-knowledge-and-intake)). The project's standing rule applies: options are laid out, not converged; where a lean is stated the evidence and what would change it are given. Evidence is labelled first-party, independent, vendor claim or anecdote, as the research library does; examples invented for this document are labelled fictional or illustrative. The setting throughout is a large, matrixed, platform-centric, regulated organisation, unnamed.

Two terms used throughout. The **intent lifecycle** is everything one feature accumulates from its first goal statement to delivery: intent, requirements, open questions, decisions with reasons, the dependency map, asks, gate evidence. The **enterprise context layer** is the organisation-wide knowledge the modules read and write across features: what each platform, process and gate is, who owns it, how to get onto it, how long it takes, and what has been decided before. The first is per feature; the second is shared. Both are "evidence, not yet fact" until a named person verifies an entry, which is the project's working definition from the intent-factory position ([Intent Factory](../../research/sources/geoff-building-accelerating-intent-factory.md), first-party proposal).

## 1. The intent lifecycle's home

### 1.1 What the home must hold

Whatever its form, the home holds a small set of typed objects per feature, each with a status, an owner, a version and a provenance trail. The set below is the project's working list; [02-structured-inquiry.md](02-structured-inquiry.md) says which step of the inquiry produces each.

| Object | What it is | Produced by | Read by |
|---|---|---|---|
| Intent | The goal, the problem, the treatment in mind, the scope and phases, in the feature owner's words plus the enterprise goals added by shaping | Shaping | Everything else |
| Requirements | Everything the feature must satisfy, in one list: the feature's own requirements (source class S1 in [01-requirements-taxonomy.md](01-requirements-taxonomy.md)) and the enterprise obligations (the label for source classes S2 to S6: law and regulation, enterprise policy and standards, platform and architecture standards, the business, contracts and counterparties), each carrying its source class, its attribute class, a source and a validation state | Shaping | Mapping; gates |
| Open questions | Questions whose answer changes scope or design, with owner, blocking flag and state | Both modules | Both; the feature owner |
| Decisions | Choices made with reasons, including reuse-vs-build choices and the considerations that decided them | Both modules, with the feature owner | Later features; auditors |
| Dependency map | For each requirement, the platforms, processes and gates that could satisfy it, the chosen route, and where build work is needed; every edge sourced or flagged | Mapping | The feature owner; platform owners; the plan |
| Asks | The questions and requests routed to owners, with state, dates and the answer | Mapping | Owners; the lead-time measurement |
| Gate evidence | Which gates apply, by published criteria, and the evidence packet for each | Mapping (later stages) | Gate owners; auditors |
| Status | Where the feature stands, what is waiting and on whom | Derived | Everyone |

A feature's home is also a place people other than the feature owner must be able to read and write: reviewers, platform owners answering an ask, a compliance reviewer answering the one question only a person can answer ([film brief](../research-dependency-agent/07-film-brief.md)). That constraint, more than any agent's preference, decides between the options below.

### 1.2 The options

The project's working hypothesis named one form: one repository per feature, indexed and findable through an enterprise data product. The evidence in the library supports five forms, each shipped somewhere.

| Option | What it is | Where it is seen | Evidence |
|---|---|---|---|
| **A. A Git repository per feature** | Each feature is its own repository of plain-text files with frontmatter; branches and pull requests carry review; an index service crawls all feature repositories | The playbook's "dedicated intent repo when intent spans many repos" | [AI-native SDLC playbook](../../research/sources/claude-ai-native-sdlc-playbook.md) (first-party guidance) |
| **B. A folder per feature in a shared repository** | One intent repository (per product area or per organisation) with a folder per feature; one schema, one set of checks, one index | The same playbook's `intent/` folder for one product; Shopify's monorepo "World" holding intent documents, runbooks and skills beside code; a PM hub repo with Markdown PRDs | [playbook](../../research/sources/claude-ai-native-sdlc-playbook.md) (first-party); [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (first-party); [Claire Vo](../../research/sources/howiai-claire-vo-beginner-prd-to-code.md) (anecdote) |
| **C. A versioned bundle in a document platform or tracker** | A space, project or initiative object in a wiki or work-tracking platform, with typed pages (requirements, decision, poster), page history, restrictions and an agent-readable instruction file per container; reached by agents over the platform's connector | Confluence space with PRD and decision templates linked to work items; Linear initiative, project and documents; Notion databases; Ramp's use of Notion and Linear as the formal record | [Confluence PRD template](../../research/sources/atlassian-confluence-prd-template.md), [decision template](../../research/sources/atlassian-confluence-daci-decision-template.md), [space permissions](../../research/sources/atlassian-confluence-roles-space-permissions.md), [Linear initiatives](../../research/sources/linear-initiatives-docs.md) (first-party docs); [Ramp's CPO](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party) |
| **D. A database with typed records** | The harness or an enterprise data product defines the object types, lifecycle states, provenance and permissions, and keeps or syncs them to repositories and platforms | No shipped example for product intent; the nearest are a software catalogue's typed entities and a decision-record convention; the register calls it the largest build | [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found) (the meta-harness row); [Backstage descriptor](../../research/sources/backstage-descriptor-format.md) (first-party) |
| **E. The session log as the record** | The shared persistent session per feature is the record; objects are extracted from it or written into a store beside it | Shopify River threads searchable by the next person; Ramp Glass sessions shared on demand; the dependency-agent film's "session of record" | [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (first-party); [Goddijn on Glass](../../research/sources/x-sebgoddijn-glass-article.md) (first-party); [shared-agents synthesis](../research-shared-persistent-agents/01-synthesis.md) |

E is rarely enough on its own: a transcript is not a typed record, and the register's story work found that what survives a person's absence in a session-only design is "the thread and its history", not the decisions as objects ([S05 worked derivation](../user-story-mapping/worked-derivation-s05.md)). It is included because every shipped shared-agent design keeps the session, and the question is what else is kept beside it.

### 1.3 The comparison

Scores are this document's judgement from the evidence cited, on a three-point scale (strong, partial, weak), and say why. Nothing here is measured; the key questions in 1.6 say what would measure it.

| Criterion | A. Repo per feature | B. Folder per feature, shared repo | C. Bundle in a doc platform or tracker | D. Database | E. Session as record |
|---|---|---|---|---|---|
| **Findable through an enterprise data product** | Partial: each repository must be registered and crawled; a thousand small repositories are easy to lose unless a catalogue entry is created at scaffold time | Strong: one repository to index; folder and frontmatter give the index its fields | Strong where the platform's graph is the data product (a vendor's graph indexes its own objects well); partial across platforms | Strong by construction: it is a data product | Partial: searchable as text (Shopify reports people search old threads); typed fields only if extracted |
| **Versioning** | Strong: every change is a commit with author and diff; ratification can be a merge or a tag | Strong, same mechanism; one history for all features, filterable by path | Partial: page history exists and is per page; a cross-page "version 3 of this feature" needs a convention; some platforms version documents, not bundles | Strong if designed in (typed versions, status transitions); the design cost is the risk | Weak: an append-only log versions the conversation, not the objects |
| **Access mirroring** (the viewer sees what their own rights allow, across sources) | Partial: repository permissions are coarse (read all or nothing per repository); a per-feature repository can mirror a feature's audience exactly but not a document's | Weak: folder-level permissions are not native to most Git hosts; everyone with repository read sees every feature | Strong within the platform (space and page restrictions are mature); weak across platforms (the register's key question 9) | Strong if the data product enforces row-level rights; costly | Weak to partial: channel or session membership becomes the access boundary, which the security evidence treats as a failure mode ([Tenable](../../research/sources/tenable-claude-tag-slack-access-model.md), independent) |
| **Agent-friendliness** (an agent can read, write, diff and check it) | Strong: plain text, frontmatter, deterministic checks in CI, pull requests as the review object | Strong, same; one place to point an agent at | Partial: connectors and MCP servers exist and are uneven; destructive calls gated; long-form pages are second-class in issue-centric tools ([Rovo MCP tools](../../research/sources/atlassian-rovo-mcp-server-supported-tools.md), first-party) | Strong if an API and schema exist; nothing exists to test | Strong for reading; weak for structure |
| **Job-family friendliness** (PMs, BAs, designers, compliance reviewers who do not use Git) | Weak unless Git is hidden behind a UI; the register found no adoption figure for PMs in Git and a reviewer-in-a-PR assumption untested ([S05](../user-story-mapping/worked-derivation-s05.md)) | Weak, same; Airbnb added an in-browser editor with review so non-Git users could contribute to its knowledge repository ([Airbnb](../../research/sources/airbnb-tech-scaling-knowledge-knowledge-repo.md), first-party) | Strong: this is where those roles already work | Partial: depends entirely on the UI built over it | Strong: a thread in chat, answerable from a phone ([dialogue](../research-dependency-agent/10-dialogue.md)) |
| **Audit** (a regulator or internal auditor accepts it as the record of intent, decision and approval) | Partial: immutable history and signed commits are strong; whether audit accepts a repository instead of the existing requirements or change tool is an open question (register Q11) | Partial, same | Strong where the platform is already the system of record for approvals; page history and restrictions are familiar to auditors | Strong if designed to the records-retention policy | Weak: a transcript is evidence, not a record; retention policies for sessions are unsettled |
| **Cost to start** | Low: a template and a scaffold skill | Low: one repository and a convention | Low: templates in a tool already licensed | High: a build | Low if the shared session already exists; the session itself is the project's larger bet |
| **Survives tool change** | Strong: plain text moves | Strong | Weak to partial: export is lossy; the typed structure belongs to the vendor | Partial: the schema is yours; the store is not | Weak |
| **Handles non-text artifacts** (designs, prototypes, data samples) | Partial: by link or by binary files | Partial | Strong: attachments and embeds are native | Partial | Partial |
| **Who owns the schema** | The team that writes the template | The repository's owner, typically product operations or platform engineering | The vendor, with the organisation's templates on top | The organisation | Nobody, unless extracted |

Three readings. First, B and C are the two serious candidates for a first deployment, and they fail on opposite criteria: B is what agents and audit want and non-engineers avoid; C is where non-engineers already are and what agents and version control find awkward. Second, every mature practice found pairs a text-first record with a UI for people who do not use its native tools: Airbnb's in-browser editor over its Git-backed knowledge repository, Shopify's threads in chat over a monorepo, Ramp's platform record beside skills in Git. Third, D is not a first move; the register's reading is that nothing like it exists to test and the risk is a competing system of record. Its right time, if ever, is when B or C has produced enough typed, consistent records that a database is a migration rather than a design.

### 1.4 Hybrids worth naming

- **Text canonical, platform for people.** The intent lifecycle lives as files (A or B); a document platform or tracker holds a synced, read-mostly view where reviewers comment; comments flow back as proposed edits. The register's hybrid row and the "name one system of record per artifact" row cover this: for each artifact, say which side is authoritative and keep a two-way link (record identifier in the file, commit identifier in the record) ([playbook sidebar](../../research/sources/claude-ai-native-sdlc-playbook.md), first-party).
- **Hidden Git.** Files and version control underneath; a web editor with review on top. Airbnb's knowledge repository is the shipped example in the library; whether the pattern holds for reviewers who are not data scientists is untested.
- **Descriptor plus links.** A thin feature descriptor (name, owner, reviewers, sources, artifact index, status) in whichever store, pointing at objects wherever they live; an agent resolves the descriptor first. The register's thin-descriptor row; cheapest to start, weakest at enforcing structure.
- **Session beside a typed store.** The session holds the conversation and the evidence trail; each turn that produces an object writes it to the home (any of A to D). This is the pattern the dependency-agent dialogue assumes and the one the flywheel in section 4 needs: the session is where verification happens, the store is where it lands.

### 1.5 A semi-structured convention, sketched

Whatever the store, the objects need a shape that people can read and agents can check. The sketch below is written as files with frontmatter because that is the most portable form; in a document platform each file is a page with properties, and in a database each is a record. The field names are the project's working proposal and are meant to be argued with. Statuses are deliberately few.

```
<feature-slug>/
  FEATURE.md            the descriptor: what this is, who owns it, who reviews it, where its pieces are
  intent.md             the goal, problem, treatment, scope and phases
  requirements/
    R-001.md ...        one file per requirement (or one table in requirements.md for small features)
  questions.md          the open-question register
  decisions/
    D-001.md ...        one file per decision, with reasons
  dependency-map.md     the map by requirement and by phase, with sources
  asks/
    A-001.md ...        one file per ask routed to an owner
  gates/
    G-change.md ...     one file per gate: applicability, criteria cited, evidence packet
  status.md             derived; regenerated, not hand-edited
```

Frontmatter fields, by object. Every object carries the common provenance block in section 2.1 (who or what wrote it, from which source, when, verified by whom, when it expires). Only the object-specific fields are listed here.

| Object | Fields | Status values |
|---|---|---|
| FEATURE.md | `feature`, `owner` (a person), `sponsor`, `reviewers` (by role), `product_area`, `phases`, `home` (where the canonical copy is, if not here), `links` (tickets, designs, prototypes), `created`, `stage` | `shaping`, `mapping`, `ready`, `in-delivery`, `delivered`, `withdrawn` |
| intent.md | `problem`, `treatment`, `goals` (feature goals; enterprise goals added by shaping, each with its source), `non_goals`, `phases` | `draft`, `shaped`, `ratified` |
| requirements/R-nnn.md | `id`, `statement` (in checkable form), `obligation_source` (the source class from 01: `S1` customer and feature goal, `S2` law and regulation, `S3` enterprise policy and standards, `S4` platform and architecture standards, `S5` the business, `S6` contracts and counterparties; `S2` to `S6` are the enterprise obligations), `attribute` (the quality-attribute class from 01: `Q1` functional behaviour to `Q10` change and transition, plus `Q11` process and evidence, which points at the gate it triggers), `representation` (operational, quantitative, qualitative, declarative) and `satisfaction` (hard, soft) as optional facets the agent fills and people confirm, `obligation_reference` (link to the obligation reference it derives from, for `S2` to `S6`), `fit_criterion` (how satisfaction will be judged, where one can be stated), `evidence` (links), `validated_by` (the validator by role), `satisfied_by` (links to dependency-map entries), `phase` | `proposed`, `validated`, `disputed`, `dropped` |
| questions.md (one row per question) | `id`, `question`, `why_it_matters` (what it changes), `owner`, `blocking` (yes or no), `asked_on`, `answered_on`, `answer`, `written_back_to` (which context artifact the answer updated) | `open`, `routed`, `answered`, `assumed` (with the assumption stated), `closed` |
| decisions/D-nnn.md | `id`, `decision`, `options_considered`, `considerations` (the deciding factors, each tagged `from_context` or `surfaced_in_session`), `chosen_because`, `rejected_because`, `decided_by`, `decided_on`, `reversible` (yes or no), `supersedes`, `kind` (`reuse-vs-build`, `scope`, `design`, `gate`, `other`) | `proposed`, `decided`, `superseded` |
| dependency-map.md (one row per edge) | `requirement`, `dependency_class` (A to F from the [taxonomy](../research-dependency-agent/09-dependency-taxonomy.md)), `candidate` (platform, process or gate card it points at), `chosen` (yes, no, pending), `route` (reuse, onboard, build, ask), `owner`, `source` (what evidence says this edge exists), `confidence`, `phase`, `wait_started`, `wait_ended` | `inferred`, `sourced`, `verified`, `could-not-find`, `disagreement` |
| asks/A-nnn.md | `id`, `to` (an owner record), `channel`, `serves` (requirement or edge), `question` (the smallest question), `if_no` (what happens if the answer is no), `drafted_on`, `sent_on`, `sent_by` (a person, at early stages), `answered_on`, `answer`, `written_back_to` | `drafted`, `sent`, `answered`, `waiting-on-priority` (the platform's priorities changed), `escalated`, `closed` |
| gates/G-slug.md | `gate` (a gate card), `applies` (yes, no, unknown), `criteria_cited`, `evidence_items` (required list, with present or missing per item), `judgement_gate` (yes or no), `submitted_on`, `decided_on`, `decision`, `decided_by` | `screened`, `preparing`, `submitted`, `decided`, `not-applicable` (with the criterion cited) |

Two rules make the convention checkable without grading its content, in the spirit of the dependency taxonomy's completeness check: no dependency-map row without a `source` or a `could-not-find` status, and no decision without `considerations`. Both can be scripted. The `written_back_to` field on questions and asks is what ties the per-feature home to the shared layer in section 2: it is how an answer given once becomes context for every later feature.

### 1.6 Key questions that would choose

1. Which roles must write to the home (not only read), and which of them will not use a Git-based tool even with a web editor? Answered by: walkthroughs with three to five reviewers of each job family on a real feature. Affects: A and B against C.
2. Which system does audit treat as the record of intent, decision and approval today, and would it accept a repository or a platform bundle instead or alongside? Answered by: the policy owner and an internal auditor. Affects: all; decides whether the home is canonical or a linked copy.
3. Does the enterprise data product (search, graph) index the candidate store with typed fields, or only as text? Answered by: a test with the search or graph owner on a sample feature. Affects: findability for every option.
4. What permission model do feature homes need: a feature-level audience, or document-level restrictions inside a feature? Answered by: a data-classification pass over three recent features. Affects: A against B against C.
5. Will a two-way link between a text record and a platform record stay in step without a person policing it? Answered by: a pilot of the hybrid on two features, measuring drift. Affects: the hybrids.

**Stated lean, and what would change it.** For a first deployment, B (a folder per feature in a shared intent repository) with a document-platform view for reviewers, because it is the cheapest form that agents can check deterministically, that versions by default, and that an enterprise index can read with typed fields; and because every scaled example in the library keeps text-first records with a people-facing surface over them. The lean would change if the walkthroughs in question 1 show reviewers will not use a web editor over Git, in which case C with an export to text becomes the lean; or if audit (question 2) will accept nothing but the existing tracker, in which case the home is a linked copy and the tracker is canonical for decisions and approvals.

## 2. The enterprise context artifacts

The shared layer is made of seven kinds of record. Each is a small, typed, owner-verifiable object with the same provenance block, so an agent reading any of them knows how much to trust it and a person reading any of them knows who to ask. The dependency-agent research set the platform card as "the unit of organisation context" ([destination](../research-dependency-agent/04-destination.md), section 4); this section gives it siblings. Schemas are sketches in the same frontmatter style as section 1.5, and the "where it lives today" row is the honest answer in most organisations.

### 2.1 The common provenance block

Every record, whether a platform card or one lead-time observation, carries:

```
recorded_by:       the agent (with its identity) or the person who wrote it
recorded_on:       date
source:            what the entry rests on: a link, a ticket, an answer in a session, a catalogue entry, an inference rule
source_kind:       owner-statement | document | system-of-record | ticket-history | chat | inference | observation
status:            provisional | verified | disputed | expired | superseded
verified_by:       a named person, by role, or empty
verified_on:       date or empty
expires_on:        date after which the entry is shown as unverified unless re-verified
supersedes:        the entry this replaces, if any
confidence:        the agent's own estimate, kept separate from status (an inferred owner at high confidence is still provisional)
```

The separation of `status` (what a person has done) from `confidence` (what the agent thinks) is the design rule the research insists on: the agent's write-back "must be visibly provisional until a person verifies it" ([destination](../research-dependency-agent/04-destination.md), V6), and a record that reads confidently from a stale source makes the layer worse ([stale docs as prompt injection](../../research/sources/codeminer42-stale-docs-prompt-injection.md), anecdote). The `expires_on` field is the mechanism Stripe used for its documentation (owner-verified or it "drifts away and gets archived", [Stripe panel](../../research/sources/stripe-sessions-2024-10x-engineer-panel.md), first-party) and the one a configuration database ships as a sixty-day staleness metric ([ServiceNow CMDB health](../../research/sources/servicenow-cmdb-health-kpis-metrics.md), vendor). Which combination of these fields earns trust is the question [04-context-trust-criteria.md](04-context-trust-criteria.md) is built to answer; the block carries the fields every candidate mechanism needs.

### 2.2 The platform or capability card

What one internal platform or shared capability is, who owns it, how to get onto it. The agent reads cards first; a card is also the thing a platform owner can write without waiting for the agent ([agent-ready checklist](../research-dependency-agent/06-mvp.md), section 4).

```
kind: platform-card
name:              e.g. "offers and decisioning engine" (fictional)
purpose:           what it does and does not do, in two sentences
capabilities:      what it can satisfy, as requirement statements with their attribute classes from 01 (e.g. "cohort eligibility rules" (Q1), "real-time decision at render" (Q8)); the standards it imposes on consumers are S4 obligations and get an obligation reference
owner_team:        a team
owner_person:      a named role or person, from an owner record
contract:          link to the API specification, data contract or SDK; version; deprecation terms
lifecycle:         experimental | supported | deprecated
intake:            how a consumer gets on: route (form, demand, chat channel, schema endpoint), what it needs, what it checks, who approves, policy for automatic approval if any
checklist_position: 0 to 7 on the agent-ready checklist
lead_times:        links to lead-time observations, summarised (median intake-to-first-response, to decision, to access)
calendar:          release trains, freezes, planning windows (link or inline)
known_conflicts:   records that disagree about this platform, with both sources
consumers:         features that depend on it (derived from dependency maps)
```

Where it lives today: a software catalogue entity with an owner field (purpose, owner, relations), a portal registration page (contract), a wiki page or a slide (intake), nowhere (lead times, calendar) ([legibility ladder](../research-dependency-agent/04-destination.md), section 1.3). The card is the one place those pieces are brought together, and the `checklist_position` field tells the feature owner how far to trust the rest.

### 2.3 The process and gate card

A governance gate or mandatory process (change authority, privacy assessment, model risk, financial-promotion sign-off, third-party risk, architecture review, records). It is a separate kind from the platform card because it is resolved by a decision, not a build or a grant ([taxonomy](../research-dependency-agent/09-dependency-taxonomy.md), class C), and because the design rule differs: a gate must be made easier to satisfy, never easier to skip.

```
kind: gate-card
name:              e.g. "financial-promotion sign-off" (fictional)
gate_type:         data gate (decides by policy on evidence) | judgement gate (a person must decide)
owner_function:    the second-line or governance team
owner_person:      a role, from an owner record
applicability:     the published screening criteria (e.g. "two of nine triggers"), with the source
criteria:          what the gate checks, as a list that can be marked present or missing
evidence_list:     the items a submission must contain
route:             how to submit (meeting, form, ticket, pipeline, schema endpoint) and who may submit (a person; an agent on behalf of a person; an agent under policy)
independence:      who may not decide (e.g. the requester; the developer of a model)
lead_times:        links to observations
decisions_recorded_at: where the gate's decisions are written (change record, assessment register, email)
never_rejects:     derived: share of submissions approved in the last period (the portfolio signal for a gate that never says no)
```

Where it lives today: the gate's own guidance page, when it has one (the privacy regulator's screening list is the model of a published, checkable applicability rule, [ICO](../../research/sources/ico-when-do-we-need-a-dpia.md), regulator); the reviewers' heads otherwise ([challenges](../research-dependency-agent/02-challenges.md), section 2.3).

### 2.4 The owner record

Who owns a platform, a gate, a data set or a decision right, and how to reach them. Owner records decay fastest of all: an ownership file silently drops people who leave ([CODEOWNERS](../../research/sources/github-docs-about-code-owners.md), first-party), and inferred owners are good enough to suggest, not to act on ([OpsLevel](../../research/sources/opslevel-docs-service-detection.md), first-party; [DeepTriage](../../research/sources/arxiv-pham-deeptriage-incident-routing.md), first-party).

```
kind: owner-record
subject:           the platform, gate, data set or decision right owned
role:              e.g. "platform product owner", "data owner", "compliance reviewer"
team:              a team
person:            a named person (or empty: team-level ownership is allowed and should be visible)
channel:           where they answer (a channel, a queue, a form); never a personal address in the shared layer
basis:             how ownership was established: catalogue field | ownership file | answered the last N tickets | confirmed by the person | named by their manager
last_confirmed:    date the person confirmed they own it (distinct from verified_on, which may be a third party)
succession:        who takes over if they leave, if known (the sponsor pattern in agent identity systems, [Entra](../../research/sources/microsoft-entra-agent-owners-sponsors.md), first-party)
```

Where it lives today: the catalogue's owner field, the ownership file in a repository, the people directory (for the person, not the subject), and the last three tickets answered.

### 2.5 The decision record

A choice with its reasons, written so the next feature can ask "has this been decided before, and does it still apply?" The reuse-vs-build decision is the one the project singles out: its deciding considerations are often not in the context, so the record exists to put them there ([dialogue](../research-dependency-agent/10-dialogue.md), day 4 and six weeks later). The shape follows the long-lived decision-record convention ([MADR](../../research/sources/adr-madr-template.md), first-party), with the considerations made explicit.

```
kind: decision-record
feature:           the feature it was made in
kind_of_decision:  reuse-vs-build | platform-choice | scope | design | gate-response | policy-interpretation
question:          e.g. "which rules engine should serve cohort eligibility for this offer?" (fictional)
options:           each candidate (platform cards or "build"), with what it would take (onboarding steps, lead time, build estimate)
considerations:    the factors that decided it, each tagged: from_context (was already in a card) | surfaced_in_session (came from a person during the choice) | assumed
decision:          the option chosen
because:           reasons, in prose, two to five sentences
rejected_because:  per rejected option, one line
decided_by:        the feature owner and anyone whose decision right it was
reusable:          whether the decision is specific to this feature or a general rule (and if general, who should ratify it as policy)
reversible:        yes | no | at a cost
```

The `considerations` tags are the flywheel's most important field. A consideration tagged `surfaced_in_session` is a thing the context did not know; once recorded, it is a candidate for the platform card (a capability or limit the card lacked) or for a general rule, and the next feature's choice is better informed. Where it lives today: meeting notes, a slide, a chat thread, a decision log updated when there is time ([maturity model](../research-dependency-agent/05-maturity-model.md), environment axis).

### 2.6 The ask record

One question or request routed to an owner, in the shape the research found owners accept: the smallest question, with the requirement it serves, the evidence, and what happens if the answer is no ([destination](../research-dependency-agent/04-destination.md), V4). The per-feature ask (section 1.5) is the instance; the shared layer keeps the aggregate and the answers that generalise.

```
kind: ask-record
feature:           the feature it served
to:                an owner record (by subject and role; the person's name stays in the session)
subject:           the platform, gate or data set it concerned
class:             the dependency class (A to F) and sub-class
question:          the smallest question
answer:            the answer, when it generalises beyond the feature
answer_written_to: the card or record the answer updated
drafted_on / sent_on / first_response_on / answered_on
sent_by:           a person (early stages) or the agent under its identity (later)
channel:           which route reached the owner
outcome:           answered | answered-after-chase | unanswered | redirected (wrong owner) | waiting-on-priority
```

Where it lives today: the sender's chat history and inbox, which is why the same question is asked of the same person by every team ([Stack Overflow 2024](../../research/sources/stackoverflow-dev-survey-2024-professional-developers.md), independent: managers spend over half an hour a day answering).

### 2.7 The lead-time observation

One measured wait, by platform and gate, never by person. The dependency-agent research found that no organisation publishes an intake-to-decision time for any internal platform ([challenges](../research-dependency-agent/02-challenges.md)); the agent's own timings are the first measurement, and the aggregate is the demand signal platform owners get on day one.

```
kind: lead-time-observation
subject:           a platform card or gate card
stage:             intake-to-first-response | first-response-to-decision | decision-to-access | ask-to-answer
started_on / ended_on
elapsed_working_days
feature:           the feature (kept for reconciliation; dropped from any aggregate shown to owners)
route:             the intake route used (form, demand, chat, endpoint)
state_at_end:      answered | granted | rejected | withdrawn | waiting-on-priority
estimate_or_measured: measured | estimated (from N past tickets)
```

The aggregate on a card reads, for example, "about 15 working days, estimated from two past requests; unverified by the security team" until measured, and then the measurement replaces the estimate ([dialogue](../research-dependency-agent/10-dialogue.md), day 9). The privacy rule is structural: the per-feature observation exists, the per-person one does not ([trust-privacy-defaults](../../options/DIMENSIONS.md#trust-privacy-defaults-trust-and-privacy-defaults-for-sessions-and-context), the "timings per platform and gate, never per person" row).

### 2.8 The obligation or policy reference

One enterprise obligation in the form the shaping module needs: what it requires, when it applies, who interprets it, and where its authoritative text is. "Enterprise obligation" is the label for requirements whose source class is S2 to S6 in [01-requirements-taxonomy.md](01-requirements-taxonomy.md): a regulation, an enterprise policy or standard, a platform or architecture standard, a business rule, or a counterparty's terms. A feature's own requirements (S1) have no reference record; they live only in the feature's home.

```
kind: obligation-reference
name:              e.g. "financial-promotion rules for customer-facing offers" (fictional, jurisdiction-generic)
obligation_source: S2 law and regulation | S3 enterprise policy and standards | S4 platform and architecture standards | S5 the business | S6 contracts and counterparties (the source classes of 01; S1 never appears here)
authority:         link to the authoritative text (the policy library entry, the regulator's page); never a paraphrase as the only source
applies_when:      triggers, as checkable conditions where the source gives them, prose otherwise
requires:          the requirement statements it imposes, as reusable requirement templates, each with its attribute class (Q1 to Q11)
interpreted_by:    the function that rules on edge cases (an owner record)
gate:              the gate card that checks it, if one does
prior_rulings:     decision records where this obligation was interpreted for a feature
jurisdictions:     where it applies
review_cadence:    how often the policy owner re-confirms it
```

Where it lives today: the policy library (often complete and rarely in a checkable form), the second line's guidance pages, and past specifications that quote it. A reference record is the shaping module's substitute for asking the compliance reviewer the same question every time; the `prior_rulings` list is the mechanism, and the risk advisor as classification against a known taxonomy is the project's model for it ([Intent Shaping](../../research/sources/geoff-intent-shaping-well-managed-environment.md), first-party proposal).

### 2.9 How the records link

A feature's requirement (an enterprise obligation, S2 to S6) cites an obligation reference; its dependency-map row points at a platform or gate card; the card points at an owner record; an ask goes to the owner and its answer is written to the card; the lead-time observation is timed from the ask; the decision record explains which card was chosen and why; and the decision's `surfaced_in_session` considerations feed back into the card. Each link is a plain reference (a slug or a stable identifier), which is what keeps the layer portable across the homes in section 1. Two things the inquiry in [02](02-structured-inquiry.md) writes back are derived from these records rather than kinds of their own: the **baseline for a kind of feature** (the verified requirements and map of past features of the same kind, which a new inquiry copies as its starting template, every copied row marked `inferred`) and the **onboarding steps** for a chosen platform (dependency-map rows with `route: onboard`, one per step of the platform card's intake).

## 3. The day-one source map

On day one none of the records in section 2 exist in the shape above. The modules must build provisional ones from raw sources, and the project's working assumption is that four families of source can be read in a large organisation: enterprise search over documents, decks, wikis and code; tickets, service-management records and intake history; catalogues (configuration database, developer portal, data catalogue, API registry); and chat history with the people directory. This section says what each can yield for each artifact, how far to trust it, what the access problems are, how it fails, and the heuristics for extracting it. The rule underneath is the dependency research's: no edge without a source, no owner without a source or an "inferred, unconfirmed" tag, no date without a source or an "assumed" tag ([first move](../research-dependency-agent/06-mvp.md), section 3).

### 3.1 Enterprise search over documents, decks, wikis and code

| | |
|---|---|
| **Yields** | Platform cards: purpose, capabilities and contract from design documents, architecture pages, API documentation and code. Gate cards: criteria and evidence lists from governance guidance pages. Obligation references: the policy library. Decision records: past specifications and architecture decision records. Owner records: author fields and "contact" lines (weak). Lead times: almost never. |
| **Reliability** | Mixed and unlabelled. A page's age is not shown as a warning; the catalogue and the runbook disagree and search returns both ([dialogue](../research-dependency-agent/10-dialogue.md), could-not-find item 3). Code is the most reliable source for what a system does today and the least for how to get onto it. Owner-verified documentation is the exception, and the one case where a documentation bot was trusted came after verification, not before ([Stripe panel](../../research/sources/stripe-sessions-2024-10x-engineer-panel.md), first-party). Drive-wide retrieval "failed miserably" at one large company until curated examples replaced it ([LinkedIn's CPO](../../research/sources/lenny-podcast-tomer-cohen-full-stack-builder.md), first-party). |
| **Access** | Search respects document permissions, so the agent sees what the requesting person sees; a shared agent with a service identity may see more than the person, which the project's identity research treats as a decision to make on purpose, not a default ([shared-agents synthesis](../research-shared-persistent-agents/01-synthesis.md), section E). Code access is usually read-wide for engineers and absent for other job families. |
| **Failure modes** | Stale pages presented as current; several pages for the same platform at different ages; decks that describe the plan, not the shipped system; private drives invisible to search; a confident synthesis that merges two sources ([AI synthesis hallucination theme](../../research/THEMES.md)); context files that are published but never read, so their existence is not evidence anyone maintains them ([llms.txt](../../research/sources/ppcland-llms-txt-adoption-zero-requests.md), independent). |
| **Heuristics** | Prefer the newest of several pages and record the conflict as a disagreement, not a choice. Treat a page's last-edited date as its `recorded_on` and set `expires_on` from it. Read the API specification and the code before the strategy for what exists; read the strategy for intent. Find past features of the same kind (same platform, same gate) and copy their map as a template, marking every copied edge `inferred`. Extract "contact" and "owner" lines as owner candidates with `basis: document`, never as owners. Quote the policy library by reference, never by paraphrase alone. |

### 3.2 Tickets, service-management records and intake history

| | |
|---|---|
| **Yields** | Owner records: who answered the last N tickets for a platform (the strongest cheap owner signal). Lead-time observations: from ticket timestamps on past requests of the same kind (estimates, labelled as such). Platform cards: the intake route and what it asked for, from past requests' forms and fields. Gate cards: past change records, assessment tickets and their outcomes, including how often the gate rejected. Decision records: outcomes of past demands and their stated reasons. Ask records: the question that was actually asked last time. |
| **Reliability** | High for timestamps and routes; medium for owners (the person who answered is often the triager, not the owner); low for reasons (tickets record outcomes, not considerations). Structured records produce better machine-extracted resolutions than chat ([NeurIPS 2025 workshop](../../research/sources/neurips-2025-resolution-extraction-slack-vs-tickets.md), independent). Routing from ticket history reaches production-grade accuracy as a recommender, with a large cost when wrong ([DeepTriage](../../research/sources/arxiv-pham-deeptriage-incident-routing.md), first-party). |
| **Access** | Ticket tools are often readable across the organisation but queues owned by second-line functions may be restricted; demand and portfolio tools are usually restricted to their users; audit records may be restricted by design. |
| **Failure modes** | The intake route changed and old tickets show the old one; the ticket tool holds only what came through it (chat intake leaves no ticket); timestamps measure the queue, not the work; a "closed" ticket may have been abandoned, which inflates measured rejection. |
| **Heuristics** | Owner inference: propose the team that answered the majority of the last N tickets, with `basis: answered the last N tickets`, and ask them to confirm as the smallest question riding on a real need. Lead-time estimates: from at least two past requests of the same kind, labelled `estimated (from N past tickets)` and replaced on first measurement. Intake description: reconstruct the form fields from the last two or three submissions. Gate behaviour: count approvals against submissions over the last period and show it on the card. Mark any platform whose last request was a chat message rather than a ticket as "intake by channel". |

### 3.3 Catalogues: configuration database, developer portal, data catalogue, API registry

| | |
|---|---|
| **Yields** | Platform cards: identity, purpose, relations (provides, consumes, depends on), lifecycle, owner team, contract links. Owner records: the owner field. Data access dependencies: data sets, their classification, their owners, the access-request route (data catalogue). Interface reliance: versions and deprecation terms (API registry). Gate cards: rarely; change-approval policies in pipeline tools are the exception. |
| **Reliability** | Structured but stale by default. Half of engineers do not strongly trust the system of record and 53% of organisations update metadata weekly or less often ([Port survey](../../research/sources/port-state-of-idp-2025-metadata-trust.md), vendor survey); the configuration database ships a staleness metric with a sixty-day default ([ServiceNow CMDB health](../../research/sources/servicenow-cmdb-health-kpis-metrics.md), vendor); regulatory dependency registers were 6.5% clean at first attempt ([ESAs dry run](../../research/sources/esas-dora-dry-run-register-of-information.md), regulator); a catalogue kept by hand is "already wrong" and runtime-derived relations are fresh only for system edges ([reliability engineer's essay](../../research/sources/thereliabilityengineering-service-catalog-already-wrong.md), anecdote). The team-level owner field is usually right; the named person is not. |
| **Access** | Portals and catalogues are built to be read widely and increasingly expose an agent interface ([Port](../../research/sources/port-docs-remote-mcp-server.md), [Backstage](../../research/sources/backstage-docs-mcp-actions.md), first-party); the configuration database is often restricted to operations; the data catalogue respects data classification. |
| **Failure modes** | Several catalogues that disagree (a portal, a configuration database, a spreadsheet); entries for retired platforms; owners who left; relations that were true at onboarding; a catalogue that describes the platform's own view and not its intake. |
| **Heuristics** | Read the catalogue as the index of what exists, not as the truth about any entry. Date every field from the entry's last update and expire accordingly. Cross-check the owner field against ticket history (3.2) and the ownership file in the repository; when they disagree, record a disagreement and route the smallest question. Take relations as candidate edges with `status: inferred`. Use the data catalogue's classification to open the privacy screen early. Prefer runtime-derived relations where a tool provides them, for system edges only. Record each platform's position on the agent-ready checklist from what the catalogue has: a card with purpose and owner is position 1; an intake schema is position 5. |

### 3.4 Chat history and the people directory

| | |
|---|---|
| **Yields** | Owner records: who answers in a platform's support channel; who is named as "the person who knows". Platform cards: the intake route when it is "message the lead" (the chat channel is the intake, and the dependency film treats that as a route to record, not a failure to hide); recent answers to recurring questions. Decision records: the reasons behind choices that never reached a document. Obligation interpretations: a compliance reviewer's answer in a thread. People directory: role, team, manager, succession (for owner records), and the organisation chart an agent needs to route anything ([Kai](../../research/sources/howiai-stripe-kai-krishnamurthy.md), first-party: the agent knows the organisation chart by default). |
| **Reliability** | Low to medium and highly variable. Inferring who knows what from communication logs was off by about 21 points out of 100 against self-report ([Watanabe et al.](../../research/sources/arxiv-watanabe-expertise-estimation-slack.md), independent); chat yields worse machine-extracted resolutions than tickets ([NeurIPS 2025 workshop](../../research/sources/neurips-2025-resolution-extraction-slack-vs-tickets.md), independent); an answer in a thread is an answer to that question on that day. The directory is reliable for role and manager and silent on ownership of platforms. |
| **Access** | The hardest family. Private channels and direct messages are invisible by design and should stay so; mining employee communications is restricted by privacy law and works councils in some jurisdictions ([Microsoft on works councils](../../research/sources/microsoft-insidetrack-copilot-works-councils.md), first-party); a channel-scoped agent's visibility follows channel membership ([Tenable](../../research/sources/tenable-claude-tag-slack-access-model.md), independent); broad visibility of who asked what breeds hiding ([Bernstein](../../research/sources/asq-bernstein-transparency-paradox.md), independent). |
| **Failure modes** | The expert who answers in chat is not the owner; the last answer contradicts the policy; the thread is a plan, not a decision; a person-level map of who knows what is built where it is not allowed; a private thread's content leaks into a shared card. |
| **Heuristics** | Read public platform-support channels only, and only for the platform's own questions. Record a chat-sourced answer as `source_kind: chat` with `status: provisional` and route it to the named owner for verification before any other feature reads it. Record "intake by channel" as a platform-card fact and a checklist gap. Never build or store a per-person expertise map; store owner records by subject and role. Use the directory for routing (role, team, manager, succession) and never as evidence that someone owns a platform. Prefer "the last two teams asked in this channel" as a fact about the route over any inference about the people. |

### 3.5 Which source feeds which artifact

A summary of the four sections above. Primary means the source usually yields a usable provisional entry; secondary means it corroborates or fills a field; blank means it rarely helps.

| Artifact | Enterprise search | Tickets and intake history | Catalogues | Chat and directory |
|---|---|---|---|---|
| Platform card: purpose, capability, contract | primary | secondary | primary | |
| Platform card: intake route and what it needs | secondary | primary | secondary (schema, where it exists) | primary when intake is by channel |
| Gate card: criteria, evidence list | primary | secondary (past submissions) | | secondary (reviewer answers) |
| Owner record | secondary | primary (who answered) | primary (team), secondary (person) | secondary (routing only) |
| Decision record | primary (past specifications, decision records) | secondary (outcomes) | | secondary (reasons never written) |
| Ask record (what was asked before) | | primary | | secondary |
| Lead-time observation | | primary (estimates) | | |
| Obligation reference | primary (policy library) | | | secondary (interpretations) |

### 3.6 The cross-checks and the could-not-find list

The sources are more useful together than apart, because their disagreements are information. Four cross-checks are cheap and should run on every map: catalogue owner against ticket answerer against ownership file; catalogue capability against the API specification against the runbook; the policy library's rule against the last reviewer answer in a thread; the published intake route against the route the last two requesters used. Each disagreement becomes an F3 item in the taxonomy ("record conflicts and staleness") and a smallest question with both sources attached ([taxonomy](../research-dependency-agent/09-dependency-taxonomy.md), section 3).

What the sources do not yield is as important as what they do. The "could not find" list is the first-class output of a day-one map ([film brief](../research-dependency-agent/07-film-brief.md)): the owner who moved, the intake nobody wrote down, the lead time nobody measured, the two records that disagree. Section 4 turns the aggregate of those lists across features into the demand signal.

## 4. The flywheel

### 4.1 What one session turn writes back

The modules write to the shared layer as a by-product of doing the feature's work, never as a separate curation pass; the research's reading of the scaled examples is that capture as a by-product is the pattern that worked and a standalone curation agent floods owners with requests that ride on nothing ([maturity model](../research-dependency-agent/05-maturity-model.md), section 5). The table lists the kinds of turn a session has and what each leaves behind. Everything written is `provisional` until a named person verifies it; the per-feature home (section 1) keeps the instance and the shared layer (section 2) keeps the generalisable part.

| Turn | What it writes to the per-feature home | What it writes to the shared layer | Who verifies | What it measures |
|---|---|---|---|---|
| The shaping module adds an enterprise obligation to the intent | A requirement with `obligation_source` (S2 to S6), `attribute`, `obligation_reference` and `evidence` | An obligation reference (new or updated with this feature as a prior use) | The feature owner validates the requirement; the policy owner verifies the reference on first use | Share of added obligations the feature owner accepted |
| The mapping module reads the sources and draws the map | Dependency-map rows, each `inferred` or `sourced` | Provisional platform and gate cards for anything not yet carded; `known_conflicts` on cards that disagree | Nobody yet | Coverage: share of the taxonomy's classes with items or an explicit "none, because" |
| The map has gaps | `could-not-find` rows | A could-not-find entry against the platform or gate (the demand signal's raw material) | Nobody; the gap itself is the record | Could-not-find count per platform and gate |
| The user and the module choose between candidate platforms (or build) | A decision record with `considerations` tagged by origin | Each `surfaced_in_session` consideration proposed as a card field or a general rule | The feature owner decides; the platform owner verifies card changes | Share of considerations that came from context (the reuse rate for decisions) |
| An ask is drafted and sent | An ask record with timestamps | The ask against the platform or gate (aggregate only) | A person sends at early stages | Ask count per platform; response rate per channel |
| An owner answers | The answer on the ask; the question closed or converted | The answer written to the card or owner record, `provisional` with the owner named as source; on the owner's confirmation, `verified` | The owner, in the same turn, by confirming | Verification rate; ask-to-answer time |
| Two records disagree and an owner settles it | The disagreement closed | The stale record `superseded`, and a correction drafted for the owner to accept at the record's home (the runbook, the catalogue) | The record's owner accepts the correction | Corrections accepted at source |
| A queue is waited on | `wait_started` and `wait_ended` on the row | A lead-time observation | Nobody; it is measured | Wait per platform and gate; share of elapsed time waiting |
| A platform's priorities change | The ask moves to `waiting-on-priority` | The observation's `state_at_end` | Nobody | Waits attributable to priority churn, kept separate because it is the larger cause of slip ([DORA 2024](../../research/sources/dora-accelerate-state-of-devops-2024.md), independent) |
| A later feature reads a verified entry | A `sourced` row citing it | The entry's use count | Nobody | Reuse rate |
| A gate is screened or prepared (later stages) | A gate file with criteria cited and evidence items | The gate card's `criteria` and `evidence_list` refined; `never_rejects` updated | The gate owner | Gate decision time; rejection reasons |

Three numbers summarise the flywheel's health from week one, as the first-move research set them: the verification rate (share of proposed cards and answers a named owner verified), the reuse rate (share of a new session's edges that came from an earlier session's verified entries), and the wait time per platform and gate ([first move](../research-dependency-agent/06-mvp.md), section 5). The first two test whether context compounds, which no source has measured anywhere; the third is the measurement nobody has.

### 4.2 How aggregated demand decides what to build next

Each session leaves asks, waits, could-not-find entries, conflicts and reuse counts against named platforms and gates. Aggregated across features they are a **demand ledger**, and the ledger is what tells the organisation which data set or tool is worth building next. The ledger reports platforms and gates, never people; that rule is structural, not editorial ([trust-privacy-defaults](../../options/DIMENSIONS.md#trust-privacy-defaults-trust-and-privacy-defaults-for-sessions-and-context)).

| Signal in the ledger | What it says | What it argues for building |
|---|---|---|
| Could-not-find count per platform | The platform is depended on and illegible | A platform card and intake description, co-written with the owner (checklist items 1 and 2) |
| Ask count per platform, and the share that are the same question | Owners answer the same thing repeatedly | The answer on the card; an intake FAQ; later, intake as a schema (item 5) |
| Wait per platform and gate, and the share of elapsed time spent waiting | Where the organisation's time goes | Published lead times (item 3); a status endpoint (item 5); for a gate, a data-gate path for its routine cases |
| Conflicts per platform | Several records disagree | One owner-verified card with expiry; corrections at the record's home |
| Reuse rate per entry kind | Which context pays back | Investment in verifying that kind first (owner records and intake routes typically; calendars rarely) |
| Gate approval share (`never_rejects`) | A gate that never says no | Evidence for the gate owner to move routine cases to policy, which is also the counterweight to the agent becoming a bureaucrat ([destination](../research-dependency-agent/04-destination.md), section 5) |
| `surfaced_in_session` considerations per platform | The card lacks what decides reuse-vs-build | Card fields for capability limits, costs and constraints |
| Waits attributable to priority churn | The slip is a planning problem, not an intake problem | Capacity and roadmap as data (the rung nothing has today) |

An illustrative prioritisation rule, which a pilot would tune rather than adopt: rank platforms and gates by (features depending on it in the period) × (median wait in working days + could-not-find entries + repeated asks), and offer the top three owners the agent-ready checklist with their own numbers attached. The dependency-agent dialogue's closing turn is the shape of the conversation: eighty per cent of a team's waiting sat in two queues, and the numbers go to those two owners "as a demand signal rather than a complaint" ([dialogue](../research-dependency-agent/10-dialogue.md)). The rule is illustrative because the weights are unmeasured; what the evidence does say is that a platform should see demand coming before it is asked to invest ([destination](../research-dependency-agent/04-destination.md), V7), and that the standard shape is adopted when a platform's asks already arrive in it, not when it is imposed ([NAO on Verify](../../research/sources/nao-investigation-into-verify.md), independent; [maturity model](../research-dependency-agent/05-maturity-model.md), section 5).

### 4.3 The two-sided marketplace, modelled

The project's framing is a two-sided marketplace, and the model below makes the sides, the cold start, the single-player strategy, the day-one value to owners and the tipping conditions explicit. The marketplace analogy is used because it names a known problem (nobody joins a side until the other side is there); section 4.4 adds the evidence on how internal platforms and knowledge bases have crossed that gap, and where the analogy breaks.

**The sides and what they exchange.**

| Side | What they give | What they get | What stops them joining |
|---|---|---|---|
| Feature teams (PMs, BAs, designers, engineers doing product tasks) | Their feature's intent and requirements; their time answering the inquiry; their choices, as decision records; their asks, as the demand signal | A map with sources and gaps on day one; enterprise obligations added before the gate finds them; fewer late surprises; a record the next feature reads | Thin context makes the first maps partial; the inquiry costs time; answering the agent's questions feels like filling another form |
| Platform, process and gate owners | A verified card; an intake description; answers to asks; later, intake as a schema and gates as policy | A demand signal before the demand arrives; asks in one shape; each question answered once; their own measured lead times | Owners' attention is the scarce resource; verification requests that ride on nothing get switched off ([Dependabot](../../research/sources/arxiv-he-dependabot-exploratory-study.md), [Wessel et al.](../../research/sources/arxiv-wessel-dont-disturb-me-bots.md), independent); a mandated shape fails on fit ([NAO on Verify](../../research/sources/nao-investigation-into-verify.md), independent) |
| The organisation (the second line, portfolio owners, the platform function) | Sponsorship; an identity for the agent; a home for the layer; a policy for what the agent may do | The dependency map regulation already demands ([EU DORA](../../research/sources/eu-dora-regulation-ict-risk-third-party.md), law); where the organisation waits and on whom; gates that never say no made visible | Governance automated badly; surveillance of owners; a new bureaucracy |

**The cold start.** On day one the shared layer is empty and both sides' reasons to join are weak. The strategy the project has settled on has two parts:

1. **Single-player usefulness.** The modules are useful to one feature team from raw sources alone (section 3): the map with its sources and its could-not-find list, the obligations added, the asks drafted in the shape owners accept, and the timings. None of that needs an owner to have done anything. Every single-player session nevertheless leaves provisional cards, measured waits and a demand entry, so the layer grows whether or not the other side has joined. This is the "come for the tool, stay for the network" shape: the tool must be worth using at zero network.
2. **Three to five anchors.** A handful of platforms and gates on the pilot's common paths (a decisioning or rules engine, an app platform's placement intake, a change authority, a privacy screen, a financial-promotion sign-off, in the fictional bank's case) are co-curated with their owners before launch: a verified card, an intake description, a first lead-time estimate. Anchors make the first maps good where it matters and give the first owners a reason to watch the ledger, because their own platforms are in it.

**The value to owners on day one** is the four things the project has committed to: a demand signal (which features will arrive, and when), asks that arrive in one shape (the ask record's fields, with the requirement, evidence and consequence attached), each question answered once (the answer written to the card, with the owner's name, so the next team reads it rather than asks), and their own lead times, measured per platform and never per person. None of the four needs the owner to publish anything; they are produced by feature teams' use. That is the designed asymmetry: the owner side is subsidised with information before it is asked for effort.

**The tipping conditions.** The marketplace has tipped when owners act without being asked. The observable conditions, each measurable from the ledger and the layer:

| Condition | Measured as | Why it matters |
|---|---|---|
| Owners verify when asked the smallest question riding on a real ask | Verification rate above a threshold the pilot sets, sustained across quarters | The compounding mechanism works; below it, the layer decays as fast as it grows |
| A later feature starts further along | Reuse rate rising quarter on quarter; time to a first map falling | The feature side's reason to join strengthens with every session |
| An owner writes a card or intake description unprompted, because asks already arrive in that shape | Cards with `recorded_by` an owner rather than the agent; the dialogue's document-generation owner receiving a drafted card after three sessions is the designed trigger | The standard shape has become the platform's input format by adoption |
| An owner asks for the ledger | Requests for per-platform reports; a platform roadmap item citing the ledger | The demand signal is being used to plan |
| A gate moves routine cases to policy, citing its own approval share | A data-gate path opened on a gate that previously decided everything by meeting | The environment has moved a step, which is the rule the maturity model sets |
| Owners pull it in unmandated | New platforms carded by their owners outside the pilot's scope | The project's fourth pilot proof |
| Context written by owners outweighs context written by the agent | Share of verified cards and fields whose `recorded_by` is an owner, trending up (the developer-portal precedent reports 85% of contributions from outside the central team, [Backstage adoption guide](../../research/sources/backstage-docs-adopting.md), first-party, unaudited) | The owner side has become the author, not the verifier of last resort |
| The number of platform and gate teams contributing grows without the pilot recruiting them | Teams with at least one owner-written entry per quarter | The portal precedent's own success measure, applied to the layer |

**Where it can stall.** The evidence names five stalls, each with the design response the research already prescribes: owners ignore the agent (verification rides on real asks, a person sends, response rate watched per channel); the layer grows wrong (provisional until verified; expiry; the trust criteria in 04); the shape is rejected (output format first, input format by adoption); the platform publishes and nobody reads (the consuming modules and the anchor cards are built together, because 97% of one kind of published context file got no requests, [llms.txt](../../research/sources/ppcland-llms-txt-adoption-zero-requests.md), independent); and visibility chills (platforms and gates, never people).

### 4.4 What the evidence on cold starts and network dynamics says

The research round run for this question filed fifteen sources on two-sided platform economics, critical-mass theory, internal developer portals, internal question-and-answer, enterprise social media and the two best-documented open knowledge communities. Their notes carry `filed_by: define-shaping-and-dependency-agents` in the [research index](../../research/INDEX.md), under the theme `two-sided-cold-start`. Five of the economics papers were read at abstract level only (paywalled); each note says so. What the evidence supports, what it warns, and where the marketplace analogy breaks:

**The problem is a known one, and the single-player strategy is a named answer to it.** Shared media inside a community are a public good whose early users depend on later ones, which makes them "extremely vulnerable to start-up problems and discontinuance" and badly described by adoption models where each person judges the tool on its own merits ([Markus](../../research/sources/markus-critical-mass-theory-interactive-media.md), independent, abstract). A platform must "get both sides of the market on board", and how the effort is split between the sides matters as much as how much is asked ([Rochet and Tirole](../../research/sources/rochet-tirole-platform-competition-two-sided-markets.md), independent, abstract); it can be rational to give one side the product free for ever ([Parker and Van Alstyne](../../research/sources/parker-van-alstyne-two-sided-network-effects.md), independent, abstract). The single-player tool is "kindling" that builds the first critical mass, after which the network supplies the long-term value ([Dixon](../../research/sources/cdixon-come-for-the-tool-stay-for-the-network.md), anecdote); the cold start is a race against early users leaving before the network forms ([Chen](../../research/sources/andrewchen-cold-start-problem-chapter-one.md), anecdote). The essays say nothing about how to recruit the second side once the first is using the tool, which is the half the anchors and the four day-one values are for.

**The owner side is the hard side, and it must be won on its own problems.** In consumer marketplaces a minority "hard side" creates most of the value and is hardest to recruit; the advice is to solve that side's own problems first ([Chen on the hard side](../../research/sources/andrewchen-solve-a-hard-problem-hard-side.md), anecdote, with an unaudited ride-hailing figure). The oldest finding in collaborative-software research says the same from the other direction: groupware fails when "the people doing the extra work are not the ones who benefit", and it asks whether such a system can succeed "if doing the extra work is left to individual discretion" and answers "probably not"; the ways out are to target groups that already do the work, add features that make the work worth it to the person doing it, and raise the perceived collective benefit ([Grudin](../../research/sources/grudin-why-cscw-applications-fail.md), independent). For this design that means three things: the anchor platforms should be ones whose owners gain directly (repeat questions, badly formed intake); the agent drafting cards from raw sources is what removes the extra work; and the four day-one values are the features that make verification worth it.

**Contribution concentrates, so capture must be a side effect of normal work.** In public communities 90% only read, 9% contribute a little and 1% produce most of the content; the remedies are to lower the barrier, capture data from normal use, provide templates and let people edit defaults rather than write from scratch ([Nielsen](../../research/sources/nngroup-participation-inequality-90-9-1.md), independent). On the fastest question-and-answer site, 1% of users supplied 27.8% of answers and obscure topics stayed thinly answered ([Mamykina et al.](../../research/sources/mamykina-stack-overflow-design-lessons-chi-2011.md), independent); inside one large company's internal communities most people who contributed somewhere only read elsewhere, and contribution tracked the person's stake in the topic ([Muller](../../research/sources/muller-ibm-lurking-enterprise-social-media.md), independent, abstract); contribution to internal repositories was driven by confidence that one's knowledge is useful and by enjoyment in helping, with rewards working only in some contexts ([Kankanhalli et al.](../../research/sources/kankanhalli-contributing-knowledge-electronic-repositories.md), independent, abstract). Three consequences for the flywheel: expect a few owners to do most verifying; ask each owner only about their own platform (a narrow, high-stake ask); and never ask anyone to write a card from scratch when the agent can draft it for correction.

**Critical mass can be inherited rather than built, and it can be lost.** The question-and-answer site had critical mass before launch because its founders brought an audience of about 140,000 readers, and the authors credit the founders' standing and daily involvement more than the software ([Mamykina et al.](../../research/sources/mamykina-stack-overflow-design-lessons-chi-2011.md), independent); a large company's internal deployment of the same product grew from about 900 users on its old tool to over 70,000 in about two and a half years, helped by developers already knowing the public site ([Stack Overflow for Teams](../../research/sources/stackoverflow-teams-microsoft-case-study.md), vendor claim). The lesson for a pilot is to launch where an audience already is (the channels, trackers and job families the feature teams use) and with a sponsor who shows up. The warning is from the largest open knowledge base: its active editors grew to 56,400 and then declined because tool-assisted rejection of newcomers' edits cut retention, and personalised welcomes worked where generic ones did not ([Halfaker et al.](../../research/sources/halfaker-rise-and-decline-wikipedia.md), independent). Quality controls added once a layer matters can reverse the tip; a first contribution from a new platform team should be corrected by a person who explains, never by an automated reject.

**Internal developer portals are the closest precedent, and they tipped on ownership.** The best-known portal started as an ownership catalogue because nobody knew who owned most services, which is the same seed the mapping module needs ([Spotify adoption article](../../research/sources/thenewstack-spotify-voluntary-99-percent-adoption.md), anecdote, vendor-sponsored). Its maintainers describe it as a "platform of platforms", a marketplace between platform teams and users, where the central team treats contributing platform teams as customers and recruits them by embedding, hack days, usage digests and proactive approaches; they report 85% of contributions from outside the central team and 135 plugins from 63 teams, and they measure success by the number of teams contributing and the share of contributions from outside the centre ([Backstage adoption guide](../../research/sources/backstage-docs-adopting.md), first-party, unaudited). The same source reports about 99% voluntary adoption after a year with no mandate, and says many other adopters stall near 10% (interviewee estimates). Those two measures (teams contributing; share of context written by owners rather than by the agent) are candidate tipping metrics for the context layer, and are added to the table in 4.3.

**Where the analogy breaks.** Both sides here are employees of one organisation, so the "price" that two-sided economics sets per side is effort, and the organisation can mandate what a market cannot. The evidence on mandates is thin and cautionary: the portal that tipped did so without one, the shared platform imposed from the centre failed on fit ([NAO on Verify](../../research/sources/nao-investigation-into-verify.md), independent), and an application "must adapt to the organization" because upkeep will not become a job requirement ([Grudin](../../research/sources/grudin-why-cscw-applications-fail.md)). None of the sources settles mandated against voluntary contribution for an internal layer. The project's position stays as the dependency research put it: the standard shape is the agent's output format first and the platform's input format only by adoption ([maturity model](../research-dependency-agent/05-maturity-model.md), section 5); a mandate, if one comes, should arrive after the ledger shows owners what they gain.

What the library already said, from earlier rounds, is consistent: the scaled examples captured context as a by-product of agents being used and corrected in the flow of work ([maturity model](../research-dependency-agent/05-maturity-model.md), section 5, first-party sources); knowledge-sharing systems lose contributors when an easier substitute appears ([PNAS Nexus](../../research/sources/pnas-nexus-llms-reduce-public-knowledge-sharing.md), independent) and knowledge hiding is common ([meta-analysis](../../research/sources/ebr-knowledge-hiding-meta-analysis.md), independent); and the platform-as-a-product doctrine says "compelling, not mandated" ([Bottcher](../../research/sources/fowler-bottcher-what-i-talk-about-platforms.md), independent essay).

## 5. The destination inventory

The destination, within policy and with well-governed context, is four acts: the agent submits intake and onboards; assembles gate evidence; closes routine gates by policy; and ratifies simple intent. Each needs data sets, governed context and tools that mostly do not exist in one place today, and each becomes needed at a different stage of the two-axis maturity model ([maturity model](../research-dependency-agent/05-maturity-model.md): environment scattered, verified, contracted; agent crawl, walk, run). The inventory below says, per item, which act needs it, what it is, where a piece of it exists today (from the legibility ladder in the [destination research](../research-dependency-agent/04-destination.md), section 1.3), and the stage at which it becomes necessary. The rule the model sets applies: the environment moves one step ahead of the agent, so an item's environment stage is the earlier of the two.

### 5.1 By destination act

| Act | Needs from the context layer | Needs as tools | Needs as governance |
|---|---|---|---|
| **Submit intake and onboard** | Verified platform cards with intake described (walk), then intake as a schema (run); owner records with succession; lead-time observations | Intake endpoint per platform that accepts a request from an agent acting for a named person, validates against the schema, returns status and records the decision; a status endpoint; agent identity with a sponsor and delegation from the requester | A policy per platform for which requests an agent may submit unaided; a rights ladder per task class; a revocation path that does not touch the person |
| **Assemble gate evidence** | Gate cards with criteria and evidence lists as checkable items; obligation references with triggers as conditions; the feature's requirements, decisions and map in the home | An evidence-packet schema per gate; fail-closed checks that every required item is present and every claim sourced; a submission route to data gates; a preparation route to judgement gates | The second line's acceptance of an agent-assembled packet as first-line evidence, with the agent's identity on it; separation of duties by identity (the requester cannot approve) |
| **Close routine gates by policy** | Gate cards with `gate_type: data gate` and the policy published beside the criteria; approval share and rejection reasons as data; decision records written automatically | Policy as code evaluated on the packet; a decision record written at decision time with evidence linked, in a form audit accepts; risk tiers with reverts and incidents measured | The policy owner's sign-off on each routine class; a labelled sample reviewed weekly; a rule that a model's confidence is never the gate ([ING warning](../../research/sources/arxiv-kapel-ing-change-incident-prediction.md), first-party, peer-reviewed) |
| **Ratify simple intent** | A completeness standard for agent-ready intent as checkable items; obligation references complete for the feature's categories; prior rulings for every interpretation the intent relies on | A readiness check against the standard; a ratification record with supersede-on-change; the risk-advisor classification against a known taxonomy with a curation path for novel risks | A definition of "simple" (which intents a policy may ratify) agreed by product and the second line; a named human on every change to the standard; false-positive and false-negative rates on obligations from a labelled sample |

### 5.2 By item, with the stage it becomes needed

| Item | What it is | Exists today as | Needed from (environment stage) | Needed for (act) |
|---|---|---|---|---|
| Platform card, owner-verified, with expiry | Section 2.2 | Catalogue entity plus the missing rungs; no verification date anywhere found | Verified (walk) | All |
| Gate card with published, checkable criteria | Section 2.3 | The privacy regulator's screening list; most gates' criteria in reviewers' heads | Verified (walk) | Assemble evidence; close by policy |
| Owner records with succession | Section 2.4 | Catalogue owner field; ownership files; agent-identity sponsors with succession ([Entra](../../research/sources/microsoft-entra-agent-owners-sponsors.md), first-party) | Verified (walk) | All |
| Decision records, written at decision time | Section 2.5 | Decision-record conventions ([MADR](../../research/sources/adr-madr-template.md)); change records with linked evidence; access audits with "requested by an agent on behalf of" ([SailPoint](../../research/sources/sailpoint-docs-mcp-server.md), first-party) | Verified (walk) for hand-written; contracted (run) for automatic | Close by policy; ratify intent |
| Lead-time observations and published lead times | Section 2.7 | Nowhere as published data; measurable from the agent's own asks | Verified (walk) | Submit and onboard (sequencing), the demand ledger |
| Calendars as data | Release trains, freezes, planning windows | Slide decks and pages; no machine-readable form found | Contracted (run) | Submit and onboard |
| Capacity and roadmap as data | Whether the platform can take the work | Nothing found in machine-readable form | Contracted (run), and may never arrive | Submit and onboard (the priority-churn problem) |
| Obligation references with triggers as conditions | Section 2.8 | Policy libraries in prose; the regulator's plan for machine-readable rules ([FCA, October 2026](../../research/sources/fca-rusu-building-future-finance-age-ai.md), regulator); control catalogues with testable requirements ([FINOS CCC](../../research/sources/finos-common-cloud-controls.md), [OSCAL](../../research/sources/nist-oscal-layers-and-models.md), first-party) | Verified (walk) for references; contracted (run) for conditions | Assemble evidence; ratify intent |
| Intake as a schema with an endpoint | The form as a schema, an endpoint that accepts "on behalf of", returns status, records the decision | Portal templates ([Backstage](../../research/sources/backstage-docs-writing-templates.md)), platform promises ([Kratix](../../research/sources/kratix-docs-promises-intro.md)), workload specifications ([Score](../../research/sources/score-dev-workload-specification.md)), portal registration over an agent interface ([Kong](../../research/sources/kong-docs-dev-portal-mcp-server.md)), data-product access requests ([Immuta](../../research/sources/immuta-docs-request-access-data-product.md)); all first-party; approval is the usual gap | Contracted (run) | Submit and onboard |
| Status endpoint | A request's state, readable by the requester's agent | Ticket and access tools expose it; platform intake rarely does | Contracted (run) | Submit and onboard |
| Evidence-packet schema per gate | The gate's evidence list as a schema with required items | Pipeline change records ([ServiceNow](../../research/sources/servicenow-docs-devops-change-velocity-approval.md), vendor); machine-readable authorisation packages ([FedRAMP 20x](../../research/sources/fedramp-20x-overview.md), first-party) | Contracted (run) | Assemble evidence |
| Policy as code at data gates | Policy evaluated on the packet, exceptions to people | Policy engines ([OPA](../../research/sources/openpolicyagent-docs-overview.md), first-party); pipeline change approval in banks ([NAB](../../research/sources/itnews-nab-cast-cloud-controls.md), [CBA](../../research/sources/itnews-cba-production-more-often-fewer-incidents.md), first-party via press); risk-tiered auto-approval on an easier population ([Meta RADAR](../../research/sources/arxiv-adams-meta-radar-low-risk-review.md), first-party, peer-reviewed) | Contracted (run) | Close by policy |
| Agent identity with a sponsor | The agent as a principal with an owner, a sponsor, succession and an audit trail | Every major identity provider ([Entra](../../research/sources/microsoft-entra-agent-owners-sponsors.md), [Okta](../../research/sources/okta-support-cross-app-access-ai-agents.md), [AWS](../../research/sources/aws-agentcore-identity-features.md), [Google Cloud](../../research/sources/google-cloud-iam-agent-identity-overview.md), first-party) | Verified (walk) for read scoped per session; contracted (run) for delegation on every request | Submit and onboard; close by policy |
| Delegation from the requester, recorded on every request | "Requested by the agent on behalf of a named person" | Token exchange with delegation chains ([RFC 8693](../../research/sources/ietf-rfc8693-oauth-token-exchange.md)); agent-specific drafts ([IETF draft](../../research/sources/ietf-draft-oauth-ai-agents-on-behalf-of-user.md)); asynchronous authorisation of one action by a named human ([Auth0](../../research/sources/auth0-docs-asynchronous-authorization.md), first-party) | Contracted (run) | Submit and onboard; assemble evidence |
| A completeness standard for agent-ready intent | Templates, examples, checkable items, evaluations for delivery-readiness | The intent-factory position's Action 3 ([Intent Factory](../../research/sources/geoff-building-accelerating-intent-factory.md), first-party proposal); spec-driven development's file sets ([Spec Kit](../../research/sources/github-spec-kit-sdd.md), first-party) | Verified (walk) | Ratify intent |
| A risk taxonomy with heuristics and a curation path | The risk advisor as classification; novel risks escalate to a person and may join the taxonomy | The intent-shaping position ([Intent Shaping](../../research/sources/geoff-intent-shaping-well-managed-environment.md), first-party proposal) | Verified (walk) for classification; contracted (run) for ratification by policy | Ratify intent |
| The demand ledger | Section 4.2 | Nothing; built from the first session | Scattered (crawl): collected from session one, reported from the walk stage | The flywheel; the portfolio signal |
| Per-feature home with typed objects | Section 1 | Repository conventions, platform templates; no shipped product-intent example | Scattered (crawl) | All; it is where the other items' inputs come from |
| A shared, durable session per feature | The conversation in which asks are answered and verification happens | In-house builds at several companies; vendor products share snapshots ([shared-agents synthesis](../research-shared-persistent-agents/01-synthesis.md), section A) | Scattered (crawl) for single-user; verified (walk) for owners joining | All |

### 5.3 Three readings of the inventory

First, nothing on the list is exotic; every item exists somewhere today, and what does not exist anywhere found is all of it on one platform, or lead times, calendars and capacity as data at all. Second, the items needed earliest are the cheapest: a per-feature home, a session, a card schema, a demand ledger, and owner verification with expiry are conventions and measurements, not systems. The expensive items (intake endpoints, policy at gates, delegation on every request) are needed only at the contracted stage and only for the platforms and gates the ledger says are worth it. Third, two acts have a ceiling set by governance rather than engineering: closing routine gates by policy depends on the second line accepting an agent-assembled packet and a policy-decided outcome, and ratifying simple intent depends on an agreed definition of "simple". Neither is a build; both are decisions, and the register's key questions already name their owners ([dependency-knowledge-and-intake](../../options/DIMENSIONS.md#dependency-knowledge-and-intake-dependency-knowledge-and-intake), questions 3 and 4).

## 6. Open questions this document leaves open

1. **The home.** Which of B and C (or which hybrid) the organisation's reviewers will use, and which store audit accepts (section 1.6).
2. **The schema.** Whether the seven record kinds and their fields are right, which a pilot's first fifty records would show; in particular whether `considerations` tagged by origin is a field people will fill, since it carries the flywheel.
3. **The sources.** Which of the four families the organisation can actually read with the permissions it will grant, and whether chat may be read at all in its jurisdictions.
4. **The flywheel's rates.** Whether owners verify when asked the smallest question riding on a real ask, at what rate, and whether reuse rises; nobody has measured either anywhere.
5. **The ledger's weights.** Whether the illustrative prioritisation rule ranks the platforms owners would themselves name as slowest.
6. **The ceiling.** Whether the second line will accept agent-assembled evidence and policy-decided routine gates, and what "simple intent" means to it.

The trust question underneath all six, what makes a written-back entry trusted enough to read, act on or drive a rule from, is the subject of [04-context-trust-criteria.md](04-context-trust-criteria.md).

See also: the requirements taxonomy ([01](01-requirements-taxonomy.md)) and structured inquiry ([02](02-structured-inquiry.md)), which produce the per-feature objects in section 1; the concept briefs ([05](05-concept-intent-shaping.md), [06](06-concept-delivery-dependency-mapping.md)) for what each module reads and writes; the staged roadmap ([07](07-staged-roadmap.md)) for when each inventory item is built; the options contribution for this task (contributions).
