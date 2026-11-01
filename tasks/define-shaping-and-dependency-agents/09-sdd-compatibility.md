# Ready for spec-driven development: what the toolchains consume, and how the two modules' outputs land in them

Date: 2026-11-01. Part of the definition of two enterprise product capabilities for a large, matrixed, platform-centric, regulated organisation ([00 overview](00-overview.md)). [00](00-overview.md) sets the goal for both modules: faster, lower-effort, higher-quality articulation of product intent, in a form that is maximally compatible with spec-driven development. This document says what that last clause means in practice. It covers what each spec-driven approach takes as input; how the requirement record in [03](03-context-layer-model.md), with its facets from [01](01-requirements-taxonomy.md), maps onto each tool's files; what a coding agent can read directly and what stays for people; where delivery dependency mapping's output plugs in; and how the delivery-ready slice reaches the code repository. It sets out options and gives a lean, with what would change it. Evidence is labelled first-party, independent, vendor claim or anecdote. The examples are fictional and say nothing about any real company.

## 1. What "maximally compatible" means, concretely

Spec-driven development (SDD) is a family of practices in which a coding agent works from a written specification kept in the repository, rather than from a chat prompt. The spec is usually split into requirements, a design or plan, and tasks, and the project's standing rules sit alongside it. The tools differ in layout and ceremony. An independent review found that "definitions are in flux", that every tool writes the spec first but few keep the spec as the maintained source afterwards, and that it is unclear whether the specs are for developers or product people ([Böckeler](../../research/sources/fowler-bockeler-sdd-kiro-speckit-tessl.md), independent).

For the two modules, "maximally compatible" is a set of properties of what they hand over. Each one can be checked:

| # | Property | Test | Why it serves the goal |
|---|---|---|---|
| P1 | **In the tool's layout.** The handover is files in the paths and with the section headings the chosen tool already reads | The tool's own commands accept it with no manual step (Spec Kit's analyze command; `openspec validate`; Kiro opens the spec) | No translation step, so less effort and nothing lost in translation |
| P2 | **One checkable statement per requirement, in the tool's notation, with a stable identifier** | Each functional or conduct requirement is a single SHALL or MUST (EARS where the tool uses it); the identifier traces back to the record's `R-nnn` | Actionable: a coding agent can implement and test one thing at a time |
| P3 | **Every requirement carries its acceptance** | A Given/When/Then scenario, an EARS acceptance criterion or a measurable success criterion, generated from `fit_criterion` | Coding agents verify against it; review has a finish line ([verification-contract row](../../options/DIMENSIONS.md#sub-choice-spec-standard--what-counts-as-agent-ready-intent)) |
| P4 | **Standing obligations sit in the standing layer** | Requirements every feature of a kind carries are in the constitution, steering or config file, cited by the feature, not restated in every spec | Shorter specs; one place to change a rule; less context for the coding agent to carry |
| P5 | **Outside dependencies are visible where the build sees them** | Chosen platforms appear as constraints; external interfaces as contracts; work that cannot start is shown as blocked, with the ask that unblocks it | Dependencies are solved or owned before handoff, and nothing that cannot start is presented as ready |
| P6 | **Nothing open is hidden** | Every open question that blocks something is marked in the tool's own marker (`[NEEDS CLARIFICATION]` in Spec Kit) or listed as an open item, with an owner | Fewer requirements missed after handoff |
| P7 | **Generated, not hand-written** | The SDD files can be regenerated from the record; edits made in the code repo flow back as proposed changes to the record | People who do not use Git still own the content; the two copies do not drift (section 7, tension 5) |
| P8 | **Minimal** | Only what the coding agent needs to build and verify; provenance stays in the record, linked by identifier | Context files that carry unnecessary requirements make agent tasks harder and costlier ([AGENTS.md evaluation](../../research/sources/arxiv-evaluating-agents-md.md), independent) |

The measure that summarises them is the **share of a feature's requirements the toolchain consumes without manual translation**. Read it together with rework after handoff: the AI-native SDLC playbook proposes "spec commits after the first plan.md commit" as its requirements-rework measure ([playbook](../../research/sources/claude-ai-native-sdlc-playbook.md), first-party, a proposed indicator only). Sections 10 and 11 say where the measures sit in [05](05-concept-intent-shaping.md), [06](06-concept-delivery-dependency-mapping.md) and [07](07-staged-roadmap.md).

## 2. What each approach consumes

All sources are first-party docs except where marked. Retrieval dates and what could not be checked are in each note.

| Approach | Layout | Requirement notation | Acceptance | Standing rules | Constraints and non-functional requirements | How tasks are derived | Outside dependencies and blocked work | Human gates |
|---|---|---|---|---|---|---|---|---|
| **Kiro** ([specs](../../research/sources/kiro-specs-docs.md), [steering](../../research/sources/kiro-steering-docs.md), [hooks](../../research/sources/kiro-hooks-docs.md)) | `.kiro/specs/<feature>/` with requirements.md (or bugfix.md), design.md, tasks.md; a central specs repo across teams by submodule or link | [EARS](../../research/sources/alistairmavin-ears.md): "WHEN [condition/event] THE SYSTEM SHALL [expected behavior]", under user stories | Acceptance criteria in EARS; correctness properties extracted from them and run as property-based tests | `.kiro/steering/` product.md, tech.md, structure.md and custom files, with inclusion modes (always, fileMatch, manual, auto); AGENTS.md read too | No dedicated section; design-first is advised for "strict non-functional requirements (latency, throughput, compliance)" | Generated from design; dependencies between tasks; optional vs required | None documented beyond task-to-task order; requirements can be imported from trackers and wikis over MCP | A person confirms requirements, then design, then tasks; Quick Spec skips the gates |
| **GitHub Spec Kit** ([templates](../../research/sources/github-spec-kit-templates.md), [method](../../research/sources/github-spec-kit-spec-driven.md)) | `specs/NNN-feature/` with spec.md, plan.md, research.md, data-model.md, contracts/, quickstart.md, tasks.md, checklists/; `.specify/memory/constitution.md` | "**FR-001**: System MUST ..."; prioritised user stories (P1, P2 ...) | Given/When/Then per story; "SC-001" measurable success criteria; checklists as "Unit Tests for English" | The constitution: principles, extra constraint and workflow sections, governance, a version; a Constitution Check gate in plan.md; analyze treats any conflict as CRITICAL | plan.md's Technical Context has **Constraints** and **Performance Goals**; the clarify scan covers non-functional attributes including "Compliance / regulatory constraints" | Generated from plan and spec, grouped by user story; `[P]` parallel; "(depends on T012)" | spec.md Assumptions holds "Dependency on existing system/service"; tasks have a "Foundational (Blocking Prerequisites)" phase; no blocked state; clarify has "Integration & External Dependencies" | A person runs each command; at most three `[NEEDS CLARIFICATION]` markers per spec |
| **OpenSpec** ([README](../../research/sources/github-openspec-readme.md), [docs](../../research/sources/openspec-docs-concepts.md), [stores](../../research/sources/openspec-docs-stores-beta.md)) | Living specs in `openspec/specs/<capability>/spec.md`; each change in `openspec/changes/<name>/` with proposal.md, design.md, tasks.md and delta specs; planning-only "stores" that code repos reference | "### Requirement:" blocks, "one statement, one SHALL/MUST", SHOULD only when meant; deltas as ADDED, MODIFIED and REMOVED | Named GIVEN/WHEN/THEN scenarios, each "could become an automated test" | `openspec/config.yaml`: `context:` (facts, conventions, constraints; "a required prompt-level input") and `rules:` per artifact | "External constraints (security, privacy, reliability, compatibility)" belong in the spec; "full spec" rigour for security, privacy, cross-team and contract changes | tasks.md as numbered checkbox groups | `blocked` means missing artifacts; cross-team requirements come in by **reference** to another team's store; no owner or ask field | Review of the change before code; `validate` checks structure |
| **BMAD** ([PRD template](../../research/sources/bmad-v4-prd-template.md), [organisation](../../research/sources/bmad-docs-plan-inside-an-organization.md), [loops](../../research/sources/bmad-docs-autonomous-development-loops.md)) | PRD, UX files, architecture spine, epic files, a ticket tree and one plan per story | "FR1: ..." and "NFR1: ..." as two numbered lists; stable requirement IDs through updates | Numbered acceptance criteria per story, told to include "any critical non-functional requirements from the PRD" | The PRD as "the document the organization owns"; the architecture spine for shared decisions | The NFR list; Technical Assumptions | A product-owner agent slices epics into tickets; ordering by `after` fields | Plan status `blocked` with a recorded reason halts later dispatch; no outside owner (only internal approvers) | Five named sign-offs, each blocking the next step |
| **OpenAI ExecPlans** ([PLANS.md](../../research/sources/openai-cookbook-codex-exec-plans.md)) | One self-contained plan file, defined by a PLANS.md and pointed to from AGENTS.md | Prose; no requirement IDs | "Validation and Acceptance"; each milestone "independently verifiable"; "demonstrably working behavior" | AGENTS.md and PLANS.md | Prose, in Context and Orientation; "Interfaces and Dependencies" names the services to use | Milestones and a Progress checklist, written by the agent | Prose only; "Surprises & Discoveries" and a Decision Log | Plan reviewed up front; the agent then proceeds without asking |
| **AI-native SDLC playbook** ([playbook](../../research/sources/claude-ai-native-sdlc-playbook.md)) | `intent/` folder in the product repo (a dedicated intent repo when intent spans repos): intent.md, spec.md, then plan.md | Template agreed by the organisation, encoded as a skill | Not fixed; spec review flags "where you cannot satisfy contradicting policies" | CLAUDE.md under a page; skills with a named policy owner; hooks for rules that must always hold | Through the organisation's skills for brand, security, compliance and UX | plan.md from plan mode; the PR review checks the diff against spec and plan | Flagged concerns go to named policy owners before engineering sees the spec; one system of record per artifact, with two-way links | Product owner accepts intent and spec; engineer accepts plan; code owner merges |
| **Tessl** ([docs](../../research/sources/tessl-docs-overview.md)) | Skills, rules, docs and config as repo files; no spec pages in the current docs | n/a | Evals with and without a skill's context; verifiers for repository invariants | Rules and skills, scored for governance | n/a | n/a | n/a | n/a |
| **AGENTS.md** ([convention](../../research/sources/agentsmd-agents-md.md)) | One plain-Markdown file at the root or nearest directory; read by many coding agents | None | None | It is the standing layer | Free text | n/a | n/a | n/a |

Five readings:

1. **The notation converges; the layouts do not.** Kiro, Spec Kit and OpenSpec all write a requirement as one normative statement (SHALL or MUST) with scenario-shaped acceptance (EARS, or Given/When/Then). An export that writes each requirement as "one SHALL, one or more scenarios" is close to valid in all three. Each tool puts that content in different files and paths.
2. **Every tool has a standing layer.** Constitution, steering, `config.yaml`, AGENTS.md and CLAUDE.md all hold rules every feature inherits. None of them is typed, and the independent evidence says to keep them small ([AGENTS.md evaluation](../../research/sources/arxiv-evaluating-agents-md.md), independent; [Vercel](../../research/sources/vercel-agents-md-outperforms-skills.md), vendor claim, finds an always-on index beat on-demand skills for reference knowledge).
3. **Non-functional requirements and constraints have no common home.** BMAD keeps an NFR list; Spec Kit splits them between success criteria and the plan's Constraints; Kiro sends them to design; OpenSpec puts them in the spec as external constraints. An export must choose per tool (section 3).
4. **No tool represents an outside owner, an ask or a gate.** The dependency vocabulary is between tasks ("depends on T012"), between phases ("BLOCKS all user stories") or about missing artifacts (OpenSpec's `blocked`). BMAD's `blocked` with a reason is the nearest to "waiting on someone". The only cross-team mechanism designed as such is OpenSpec's read-only reference to another team's planning store. This is the largest gap the dependency module fills, and the export must encode it by convention (section 5).
5. **Who writes the spec is unsettled.** Every author shown in the first-party cases is an engineer ([Nystrom](../../research/sources/howiai-notion-ryan-nystrom-spec-driven.md), first-party), and Böckeler asks whether the tools are for product people at all. The playbook's answer is that "the product owner reviews that spec, but doesn't write it". That is the opening for intent shaping: produce the spec a coding agent reads, upstream of the code repository.

## 3. Mapping the requirement record to each tool's files

The record is the `requirements/R-nnn.md` object in [03, section 1.5](03-context-layer-model.md), with the facets from [01](01-requirements-taxonomy.md). Each field's destination per tool:

| Record field (03; facets from 01) | Kiro | Spec Kit | OpenSpec | BMAD | ExecPlan | Stays in the record only |
|---|---|---|---|---|---|---|
| `id` | Requirement number; the record id in a trailing comment or a front-matter map | FR-nnn, with the record id in a trailing comment (`<!-- R-01 -->`) | Requirement heading carries the id | FRn or NFRn; BMAD keeps IDs stable | Named in prose | The id is the join key, so it appears everywhere |
| `statement` (checkable form) | EARS acceptance criterion under a user story | "System MUST ..." | "The system SHALL ..." | FR or NFR bullet | Purpose and Plan of Work prose | |
| `obligation_source` (S1 to S6) | Not rendered; S1 grouped under user stories, S2 to S6 under a heading such as "Enterprise requirements" or in steering | Not rendered as a field; S2 to S6 standing items go to the constitution | Not rendered; can go in `.openspec.yaml` `x-` keys | Not rendered | Not rendered | **Yes**, with the source chain |
| `obligation_reference` | A link in a comment, or the steering file it came from | A link in a comment | A link | A link | Restated in words: ExecPlans forbid relying on outside links | **Yes**, canonical |
| `attribute` (Q1 to Q11) | Decides placement: Q1, Q3, Q4 to Q6 to requirements.md; Q7, Q8, Q10 to design.md; Q11 to tasks (section 5) | Decides placement: Q1 to Q6 to FR; Q8, Q9 to SC or plan Constraints; Q10 to plan; Q11 to tasks | Q1 to Q8 as requirements with scenarios; Q10 to design.md; Q11 to tasks | Q1 to FR; the rest to NFR; Q11 to the ticket tree | Q10 and Q11 in Concrete Steps | The class itself |
| `representation` (operational, quantitative, qualitative, declarative) | Decides the notation: operational to an EARS pattern; quantitative to a measurable criterion; qualitative to a design-review item; declarative to steering | Operational to FR plus scenario; quantitative to SC; qualitative to a checklist item; declarative to the constitution | Operational to Requirement plus scenario; declarative to `config.yaml` context or rules | Operational to FR; quantitative to NFR | Validation and Acceptance | |
| `satisfaction` (hard, soft) | SHALL for hard; soft goes to design as a goal | MUST for hard; soft as SHOULD (Spec Kit's template uses MUST only) | SHALL or MUST for hard; SHOULD for soft, as the docs define it | Priority wording | Prose | |
| `fit_criterion` | EARS acceptance criteria; Kiro derives correctness properties from them | Given/When/Then scenarios; SC-nnn when measurable | GIVEN/WHEN/THEN scenarios | Story acceptance criteria | Validation and Acceptance | |
| `evidence` | Not rendered | Not rendered | Not rendered | Not rendered | Not rendered | **Yes** |
| `validated_by` (role) | Not rendered; validation must be complete before export, or the item exports as open (P6) | Not rendered; unvalidated items export as `[NEEDS CLARIFICATION: ... owner: role, ask A-nnn]` | Not rendered; open items listed in proposal.md | Not rendered | Not rendered | **Yes** |
| `satisfied_by` (dependency-map edges) | Chosen platform to design.md as a constraint and interface; edges with work to tasks | Chosen platform to plan.md Constraints and Primary Dependencies; interfaces to `contracts/`; onboarding steps to Foundational tasks | Interfaces to design.md, or a reference to the platform's store; tasks | Technical Assumptions; tickets | Interfaces and Dependencies | The edge's evidence, confidence and wait times |
| `phase` | One spec per phase, or a phase heading | One feature directory per phase, or the user story priority | One change per phase | Epic | Milestone | |
| status (`proposed`, `validated`, `disputed`, `dropped`) | Only `validated` exports as a requirement; `disputed` exports as an open item; `dropped` not at all | Same; `disputed` becomes `[NEEDS CLARIFICATION]` | Same | Same | Same | Full history |

Three rules make the mapping deterministic, so the export can be scripted rather than written by a model each time:

- **Attribute and representation choose the slot. Source does not.** Source decides who validates and who can waive, which the record needs and the coding agent does not. This answers tension 7 (section 7).
- **Only validated requirements become normative statements.** Anything else becomes an open item in the tool's own marker, with the owner by role and the ask that will close it. A spec never presents an inferred obligation as settled.
- **Q11 process and evidence requirements never become behaviour requirements.** "Model-risk entry before use" is not something the system shall do. It becomes a readiness gate or a blocked task (section 5). This keeps 01's lean of finding process obligations early, as requirements, without putting them in the spec as code to write.

## 4. What a coding agent can consume, and what stays for people

| Output of the two modules | Consumed directly by a coding agent or the SDD toolchain | Human-readable only, or read by people and the modules |
|---|---|---|
| Validated behaviour, data, experience, security, privacy and conduct requirements (Q1 to Q6) | **Yes**, as requirements with scenarios | |
| Performance, operability and measurement requirements (Q7 to Q9) with a number | **Yes**, as success criteria, plan constraints or NFRs | Without a number, as review checklist items for people |
| Change and transition requirements (Q10), such as "built on the content-slot system" | **Yes**, as plan or design constraints | Training and rollout items stay with people |
| Process and evidence requirements (Q11) | **Partly**: as a gate the toolchain checks for (the record says the gate is passed) or a blocked task | The gate packet, the judgement and the sign-off |
| Standing enterprise obligations for a kind of feature | **Yes**, as constitution, steering or config entries, kept short | The obligation reference, its owner and its expiry |
| Chosen platform and its interface | **Yes**, as constraint and contract | The reuse-or-build decision and its considerations |
| Open questions that block a requirement | **Yes**, as markers the toolchain refuses to build past | The question's history and the answer's reach |
| Asks to owners, their state and wait times | **Only as blocked-task markers** | The ask register, the tracker item, the chase |
| Obligation source chain, evidence, confidence, validator | No (P8) | **Yes**, by design |
| Dependency map edges, could-not-find list | No, except as constraints and blocked tasks | **Yes** |
| Decisions with reasons | A one-line pointer in design or the Decision Log | **Yes** |
| The readiness statement | A check the toolchain can run (section 5d) | The text and the ratification |

## 5. Where the dependency output plugs in

Delivery dependency mapping produces the map, the asks and the gate records ([06](06-concept-delivery-dependency-mapping.md); [03, section 1.5](03-context-layer-model.md)). None of the tools has a slot for these as such, so there are five plug points. Each is stated with the tool's nearest native slot and, where none exists, a proposed convention.

**(a) Constraints.** A chosen route becomes a constraint on the build: "must use the offers and decisioning engine", "writes to the single decisioning log". Kiro: design.md, and steering when the constraint holds for every feature of a kind. Spec Kit: plan.md Technical Context, Constraints and Primary Dependencies, checked against the constitution. OpenSpec: the spec, as an external constraint, or `config.yaml` context. BMAD: Technical Assumptions or an NFR. ExecPlan: Interfaces and Dependencies.

**(b) External-interface contracts.** When a platform's interface is known (an API, an event, an intake schema), it lands as a contract the build is tested against. Spec Kit has a `contracts/` directory for this, and its tasks template starts with contract tests. Kiro: design.md's data models and interfaces. OpenSpec: a reference to the platform team's own store, if it keeps one, so the contract is read from its owner rather than copied ([stores](../../research/sources/openspec-docs-stores-beta.md), first-party, beta). That is the platform card from [03, section 2.2](03-context-layer-model.md) published in a form coding agents can read, and it is a step up the agent-ready checklist the roadmap tracks.

**(c) Tasks blocked on an ask.** Work that cannot start until an owner acts (a data-access grant, a client registration, a pricing committee decision) must not look ready. None of Kiro, Spec Kit or OpenSpec has a "waiting on someone outside" state. The options:

| Option | What it is | For | Against |
|---|---|---|---|
| A marker in the task line | `[BLOCKED: A-003 data-access request, data owner, sent day 2]` in tasks.md, plus Spec Kit's Foundational phase for anything every story needs | Readable by people and agents; works in every tool; an analyze or validate pass can be told to refuse it | A convention, not a feature; the tool's "run all tasks" will not respect it without a hook |
| Hold the task back | Export only unblocked tasks; blocked work stays in the record and is exported when its ask closes | Nothing false in the spec | The coding agent cannot see what is coming; the plan may assume something it should not |
| A status field where the tool has one | BMAD's plan status `blocked` with a reason; an issue in the tracker with a blocking link, when tasks are turned into issues | Native; an orchestrator halts on it | Only BMAD and tracker-backed flows have it |
| A hook that enforces the marker | A pre-task hook (Kiro hooks; a Claude Code or Codex hook; a CI check) reads the marker or the ask register and stops the task | Deterministic, as the playbook advises for rules that must hold | One hook per toolchain to build and maintain |

**(d) Readiness gates.** The readiness statement from [02, section 6](02-structured-inquiry.md) (every validated requirement mapped, every blocking item owned, gate applicability screened) becomes a check the toolchain runs before implementation. Spec Kit's plan has a Constitution Check gate, and its extensions file can register a `before_implement` hook. Kiro's hooks can block a tool call. The playbook gates each accepted artifact by merge. The gate records (`gates/G-*.md`) export as a short readiness file, or as constitution entries such as "Implementation MUST NOT start while a Foundational task is BLOCKED". A model reads the second form, a script checks the first.

**(e) Standing enterprise requirements as constitution or steering.** The baseline for a kind of feature ([02](02-structured-inquiry.md): the obligations every customer-facing offer carries, say) is the natural content of a constitution, a steering file with `fileMatch` inclusion, or `config.yaml` rules. Three cautions. Keep them short, because always-on context that is not needed costs task success ([AGENTS.md evaluation](../../research/sources/arxiv-evaluating-agents-md.md), independent). Generate them from verified obligation references ([03, section 2.8](03-context-layer-model.md)), so each line has an owner and an expiry in the record even though the file shows neither. And put a hook behind any rule that must always hold, because "the skill makes violations rare and the hook makes them close to impossible" ([playbook](../../research/sources/claude-ai-native-sdlc-playbook.md), first-party). Kiro's global steering can be distributed centrally, so one organisation-wide file can serve every repository ([steering](../../research/sources/kiro-steering-docs.md), first-party).

## 6. The handoff: when, in which layout, who triggers it

**What crosses.** The **delivery-ready slice** of a feature: the validated requirements of one phase, with every `satisfied_by` edge chosen and owned, every blocking question either answered or exported as an open marker with an owner, every task that waits on an ask exported as blocked, and the readiness check passing. It is a slice, not the whole record: provenance, evidence and asks stay home (P8).

**When.** Options, tied to the handoff points in [02, section 7](02-structured-inquiry.md):

| Option | When the slice is exported | For | Against |
|---|---|---|---|
| **At readiness (H5)** | Once, when the sponsor ratifies the phase | Clean; one review | The coding agent starts late; requirement changes found in design come back as rework |
| **Per phase, early** | A provisional export as soon as a phase's requirements are validated (H3), marked draft; final at readiness | Engineers and their agents can plan and spike while asks are open; blocked markers show what is waiting | Two versions to reconcile; the draft may be built on |
| **Continuous (H4)** | Every change to the record regenerates the files and opens a pull request | The spec in the code repo stays true; matches spec-anchored practice | Noise; review fatigue on many small Markdown diffs, which the independent review already found tedious ([Böckeler](../../research/sources/fowler-bockeler-sdd-kiro-speckit-tessl.md), independent) |

**In which layout, and where.** This is tension 4: [03](03-context-layer-model.md)'s lean puts the feature's record in a shared intent repository with a document-platform view, while the SDD tools expect specs beside the code in their own layout. Four options:

| Option | What it is | Evidence it exists | For | Against |
|---|---|---|---|---|
| **H-A. Generate into each code repo** | The export writes `specs/NNN-feature/` or `.kiro/specs/<feature>/` into the code repo that will build it, by pull request, and records the commit in the intent record | The playbook's two-way linkage rule (record id in the file, commit in the record) | Every SDD tool works unchanged; the coding agent sees one local spec | One feature touching three repos needs three slices; the code repo copy can drift |
| **H-B. The intent repository as a planning store that code repos reference** | The record's export lives in the shared intent repository in OpenSpec's layout; each code repo declares a reference and opens a small local change that cites it | OpenSpec stores, beta ([stores](../../research/sources/openspec-docs-stores-beta.md), first-party) | Matches 03's lean exactly; requirements owned once and consumed by many repos; "the wiki version drifts, and your coding agent can't read it anyway" is the problem it was built for | Beta, one tool; "OpenSpec currently does not route tasks to repos" |
| **H-C. A central specs repository linked in** | The export lives in a central specs repository that code repos pull in as a submodule or package | Kiro's best-practice advice across teams ([Kiro specs](../../research/sources/kiro-specs-docs.md), first-party) | Works with Kiro today; one review process | Submodules are a known source of friction; access is all or nothing per repository |
| **H-D. An intent folder in the product repo** | For a product that lives in one repository, the intent record itself is the `intent/` folder there, and the SDD files sit beside it | The playbook's default for a single product ([playbook](../../research/sources/claude-ai-native-sdlc-playbook.md), first-party) | No copy at all | Breaks for platform-centric work, where one feature spans many repositories, which is this organisation's common case |

**Who triggers it.** Options: the sponsor's ratification of a phase triggers the export automatically, as the playbook's merge-triggered design does; or the engineer who will build pulls the slice into their repository with a command (a slash command or CLI that reads the record by feature id); or both, with the automatic export opening a pull request the engineer accepts. The automatic route is lower effort. The pull route keeps the build team's consent visible, which matters in a matrixed organisation where the building team may not be the shaping team.

**The way back.** Edits made in the code repository (a requirement tightened during design, a scenario added) must return to the record or the two copies drift. BMAD's rule is the model: "if a ticket needs an answer the PRD lacks, update the PRD first", and reviewers request changes in the source document, not copies ([BMAD in an organisation](../../research/sources/bmad-docs-plan-inside-an-organization.md), first-party). In practice a check in the code repository compares the spec with the last export. Any difference becomes a proposed change on the record, and for the coding agent the record stays canonical. Kiro's design-first workflow and Spec Kit's converge command produce exactly these changes (requirements derived from design; unbuilt work appended), so the way back will be used.

## 7. Three tensions, answered

**Tension 4: a shared intent repository against specs beside the code.** The record stays where [03](03-context-layer-model.md) leans (a shared repository, with a document-platform view). The SDD files are an export, not the record. Where the export lands is H-A to H-D above. **Lean: H-A (generate into the code repo by pull request) for the pilot, with H-B as the option to test**, because H-A works with every tool today, and the pilot's engineering teams will already have chosen theirs. H-B is the closest fit to a platform-centric organisation, but it is beta and one tool. What would change it: if pilot features commonly span three or more repositories, H-B or H-C earns its cost; if OpenSpec's stores leave beta and its references gain task routing, H-B becomes the lean; if the pilot repositories are single-product, H-D is cheaper still.

**Tension 5: job-family agnostic against Git- and IDE-centric tools.** The person shaping the feature never edits SDD files. They work in the session and the document view; the SDD files are generated from the record (P7). Engineers can edit the generated files, and their edits come back as proposals. This is the playbook's split ("the product owner reviews that spec, but doesn't write it") with one difference: here the product owner's object of review is the record, and the spec is derived from it. It keeps the module usable by product managers, analysts and designers who do not use Git. It also accepts a cost: one generator per tool to build and keep current. What would change it: if engineers in the pilot routinely rewrite the generated spec, the export is in the wrong shape, and the measure (requirements consumed without manual translation) will show it.

**Tension 7: 01's source-primary conversation against the tools' functional, acceptance-criteria form.** The conversation and the record keep source as the primary axis. The export is organised by attribute and behaviour, which is the "spec view generated by attribute while the record keeps both" that [01, section 7](01-requirements-taxonomy.md) already lists as the condition for its lean. Concretely: S1 requirements become user stories; S2 to S6 requirements become requirements or constraints placed by attribute (section 3), with their identifiers; standing S2 to S6 obligations become constitution or steering lines; Q11 obligations become gates and blocked tasks. The source class is not rendered, but it can be recovered from the identifier. What would change it: if coding agents or reviewers do better when they can see that a requirement is regulatory (for example, they refuse to relax it during design), then render the source as a short tag on the requirement (`[regulatory]`). That would be one line in the export, and an eval can test it.

## 8. The cohort offer, rendered twice

Fictional, from [02, section 10](02-structured-inquiry.md), at day 9: twelve requirements validated, two changed by mapping, the demand to the decisioning team waiting, and the promotion reading of the servicing wording open with the compliance reviewer. Excerpts only.

### In Spec Kit's layout

`specs/014-salary-cohort-fee-waiver/spec.md`

```markdown
# Feature Specification: Fee-waiver offer for salaried customers without a savings pot

**Feature Branch**: `014-salary-cohort-fee-waiver`  **Status**: Ready (phase 1)  **Input**: intent record FEAT-0412, export of day 9

## User Scenarios & Testing *(mandatory)*

### User Story 1 - See the fee-waiver offer at login (Priority: P1)
A customer with regular salary credits and no savings pot sees an offer at login: open a pot and the monthly fee is waived for a year.

**Acceptance Scenarios**:
1. **Given** a customer meets the cohort rule and has not seen the offer this month, **When** they log in, **Then** the offer is shown. <!-- R-01 -->
2. **Given** a customer opened a savings pot today, **When** they log in again today, **Then** the offer is not shown. <!-- R-02 -->
3. **Given** a customer has opted out of marketing, **When** they log in, **Then** the offer is not shown. <!-- R-06 -->

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: System MUST show the offer only to customers meeting the cohort rule (three salary credits from one payer in three months; no savings product; consent flags as R-06). <!-- R-01 S1 Q1,Q2 -->
- **FR-002**: System MUST evaluate cohort membership at the moment of display and stop showing the offer the same day a pot is opened. <!-- R-02 S1 Q1,Q8 -->
- **FR-003**: System MUST be able to reproduce, for any customer and date, the rule version and inputs that decided whether the offer was shown. <!-- R-03 S2 Q6,Q7 -->
- **FR-004**: System MUST write every offer decision to the single decisioning log. <!-- R-07 S3 Q2 -->
- **FR-005**: System MUST let servicing staff see why a customer did or did not get the offer. <!-- R-10 S5 Q7 -->
- **FR-006**: Offer copy MUST use the approved wording for [NEEDS CLARIFICATION: whether the servicing-message wording is a financial promotion; owner: compliance reviewer for the product line; ask A-007, sent day 5] <!-- R-08 -->

## Success Criteria *(mandatory)*
- **SC-001**: Pot opening among shown customers is measured against a registered holdout. <!-- R-11 S5 Q9 -->

## Assumptions
- Cohort evaluation is provided by the offers and decisioning engine (decision D-003); this feature onboards as a new real-time client.
- The time-limited waiver has pricing approval (R-09) [BLOCKED: A-005, pricing committee, next sitting day 14].
```

`.specify/memory/constitution.md` (excerpt; generated from verified obligation references for customer-facing offers)

```markdown
### Customer-facing eligibility
Eligibility decisions shown to customers MUST be made on the strategic decisioning platform and MUST be logged to the single decisioning log. <!-- R-12, R-07; architecture decision record -->
Cohort definitions MUST NOT use or proxy for a protected characteristic. <!-- R-04 -->
Implementation MUST NOT start while a Foundational task is marked BLOCKED.
```

`plan.md` sets Technical Context **Constraints** to "real-time rule evaluation through the offers and decisioning engine; within the home-screen latency budget", and `contracts/decisioning-eligibility.md` holds the engine's request and response, taken from its card. `tasks.md` (excerpt):

```markdown
## Phase 2: Foundational (Blocking Prerequisites)
- [ ] T004 Register the app as a real-time client of the decisioning engine [BLOCKED: A-002, decisioning platform intake; demand awaiting decision, day 4 in queue]
- [ ] T005 Request access to the salary-credit feature from the transactions domain [BLOCKED: A-003, data owner]
- [ ] T006 [P] Contract test for decisioning eligibility in tests/contract/test_decisioning_eligibility.py
```

### In Kiro's layout

`.kiro/specs/salary-cohort-fee-waiver/requirements.md` (excerpt)

```markdown
### Requirement 1: Offer eligibility at login  <!-- R-01, R-02, R-06 -->
**User Story:** As a salaried customer without a savings pot, I want to be told I can waive my monthly fee, so that I can decide whether to open a pot.

#### Acceptance Criteria
1. WHEN a customer who meets the cohort rule logs in THE SYSTEM SHALL display the fee-waiver offer at most once per calendar month.
2. WHEN a customer opens a savings pot THE SYSTEM SHALL stop displaying the offer to that customer from the same day.
3. IF the customer has opted out of marketing THEN THE SYSTEM SHALL NOT display the offer.

### Requirement 2: Explainable decisions  <!-- R-03, R-07, R-10 -->
**User Story:** As a servicing agent handling a complaint, I want to see why a customer did or did not get the offer, so that I can answer them.

#### Acceptance Criteria
1. WHEN an offer decision is made THE SYSTEM SHALL write the decision, rule version and inputs to the decisioning log.
2. WHEN a servicing agent opens a customer's offer history THE SYSTEM SHALL show the rule version and the inputs that decided each display.
```

`.kiro/steering/customer-offers.md` carries the standing obligations, with `inclusion: fileMatch` and `fileMatchPattern` set to the offer code paths, so the rules load only when offer code is touched. `design.md` names the decisioning engine as a constraint and lists its interface. In `tasks.md`, task 2 ("Register as a real-time client of the decisioning engine") carries the same `[BLOCKED: A-002 ...]` marker, and a Kiro `PreToolUse` hook reads the ask register and stops the task while the marker stands. The requirement back-references that Kiro-generated tasks commonly carry were not confirmed in the docs read, so the record identifiers are kept in comments.

Read together, the two renderings show the argument of this document. The content is the same twelve requirements. The notation differs by a keyword. Placement differs by file. The provenance (source, validator, evidence) is absent from both, and in both the identifier leads back to it. The dependency output appears only as constraints, a contract, blocked markers and a standing-rules file.

## 9. Options for the export target, and a lean

| Option | What it is | For | Against | What would favour it |
|---|---|---|---|---|
| **E1. One tool** | Export only to the SDD tool the organisation standardises on | Simplest; one generator | Ties the modules to one vendor's layout; the review found layouts in flux | An organisation-wide standard already chosen |
| **E2. A neutral requirement block plus thin adapters** | The record exports one neutral form (each requirement as one SHALL or MUST with named scenarios, a stable id, an attribute-chosen slot, and the five plug points as conventions); a small adapter per tool writes the layout | Survives tool churn; the neutral form is already near-valid in Kiro, Spec Kit and OpenSpec (section 2, reading 1); adapters are mechanical | An extra layer; each adapter must track its tool's changes | Pilot teams on more than one tool; tools still moving |
| **E3. The standing layer only** | Export only AGENTS.md, constitution or steering entries, and let each team write its own feature specs | Least work; no per-feature generator | Leaves the main translation, and its errors, to people; misses the goal | Engineering teams unwilling to accept generated specs |
| **E4. The record as a store, referenced** | H-B as the whole design: the intent repository is the planning store; code repos reference it | No copies | One tool, beta | OpenSpec adopted widely; stores stable |

**Lean: E2, starting with the adapter for whichever tool the pilot's engineering teams already use, and the neutral form written so that Spec Kit's analyze and `openspec validate` pass on its output.** Reasons: the goal asks for compatibility with spec-driven development as an approach, not with one product; the notations have converged enough that a neutral block is cheap; the layouts have not, and they are still changing (Spec Kit's commands were renamed between its own two docs; Tessl moved away from specs altogether). Today, teams in the organisation use a variety of spec-driven tools, and consolidation is expected over time; that consolidation is what would move the lean towards E1. What else would change it: evidence that generated specs are rewritten by engineers more often than not (fix the neutral form first, and consider E3 for the teams concerned); OpenSpec's stores reaching a stable release with task routing (E4).

## 10. How the goal is measured

The measures below are threaded into the four pilot outcomes in [05, section 7](05-concept-intent-shaping.md) and [06, section 8](06-concept-delivery-dependency-mapping.md), and into the stage triggers in [07](07-staged-roadmap.md). They are listed here in one place:

| Goal | Measure | Pilot outcome it sits under |
|---|---|---|
| Speed | Elapsed working days from first statement of intent to the delivery-ready slice landing in the code repository | Time to ready |
| Lower human effort | Person-hours of the feature owner, validators and owners per feature, from session and ask timestamps plus a short self-report; asks sent by a person (the crawl stage's known cost) counted, not hidden | Time to ready |
| Fewer missed requirements | Requirements and obligations found after handoff (by design, build, review, a gate or after release) per feature, against the prospective control | Fewer late surprises, less rework |
| More actionable requirements | Share of exported requirements with a fit criterion a coding agent turned into a test or check; share that needed no clarification after handoff | Fewer late surprises, less rework |
| Dependencies solved before handoff | Share of dependency edges resolved, or owned with an open ask, at handoff; count of tasks that started and then stopped on an unmapped dependency | Fewer late surprises, less rework |
| SDD compatibility | Share of requirements consumed by the toolchain without manual translation (exported, accepted by the tool's own check, not rewritten before the first plan commit); spec commits after the first plan commit (rework) | Fewer late surprises, less rework; and context compounds, as the standing layer is reused |

## 11. Open questions

1. Which SDD tools do the pilot's engineering teams use today, and do they use them for the kind of feature the pilot will shape? (Partly answered: there is no single standard today, teams use a variety of tools and consolidation is expected over time, so E1 is not settled and E2 stands. Which tool gets the first adapter is still answered by asking three to five pilot teams.)
2. Will engineers accept a generated spec as the starting point, or rewrite it? (Answered by the translation-free share on the first five features; decides E2 against E3.)
3. Do coding agents keep a regulatory requirement under design pressure better when its source is visible? (Answered by an eval with and without a `[regulatory]` tag; decides tension 7's rendering.)
4. Can a blocked-task marker be enforced in each pilot toolchain by a hook, and does the coding agent respect it without one? (Answered by a test per toolchain; decides option (c) in section 5.)
5. How large can the standing layer for a kind of feature get before it costs task success? (Answered by a with-and-without eval on the pilot's own repositories, in the manner of the AGENTS.md study; decides what goes into constitution and steering, and what stays as on-demand skills.)
6. How often do code-repository edits flow back to the record, and how often does the record change after export? (Answered by the drift check in section 6; decides the export timing.)
7. Will platform owners publish their interface contracts in a form coding agents read (a contract file, or a planning store), once asks arrive in that shape? (Answered by the anchors in the pilot; it is a step on the agent-ready checklist and a measure of owner pull.)

## 12. Evidence and its limits

The tool descriptions are first-party docs, read on 2026-11-01 or earlier and filed with their dates. The Spec Kit templates and the OpenSpec and ExecPlans files were read verbatim from their repositories; the Kiro pages were read through a summarising fetch, so their wording is quoted only where the page gave it. The tools change quickly, and OpenSpec's stores are beta. The only independent evidence on SDD practice is one review ([Böckeler](../../research/sources/fowler-bockeler-sdd-kiro-speckit-tessl.md)), and one study on context files ([AGENTS.md evaluation](../../research/sources/arxiv-evaluating-agents-md.md)), whose benchmark is Python-only. No source measures whether a generated, upstream spec improves delivery against a spec engineers write themselves. The properties, mappings, conventions and options here are this document's design, and the worked example is fictional and was written by the same hand. Section 11 says what a pilot would measure first.
