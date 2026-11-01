# A requirements taxonomy for feature intent in a regulated, platform-centric organisation

Date: 2026-10-31. Part of the definition work for two product capabilities, intent shaping and delivery dependency mapping (see [00-overview.md](00-overview.md) when it lands, and the concept briefs [05](05-concept-intent-shaping.md) and [06](06-concept-delivery-dependency-mapping.md)). This document builds the categories that the structured inquiry in [02-structured-inquiry.md](02-structured-inquiry.md) walks: the kinds of requirement a feature carries once it lives in a large, matrixed, federated organisation under regulation. It compares two ways of cutting the space, by **obligation source** and by **quality attribute**, states each partition's principle and its tests for exclusivity and exhaustiveness in the way the dependency taxonomy in [09-dependency-taxonomy.md](../research-dependency-agent/09-dependency-taxonomy.md) does, tests both on four fictional features from different kinds of regulated business, reports where each breaks, and lays out the options, including a hybrid. A lean is given at the end with what would change it. The project aggregates options rather than converging; the lean is a lean.

Evidence is in the project's research library (`../../research/sources/`), labelled first-party, independent, vendor claim or anecdote. The features and organisations in this document are fictional and say nothing about any real company.

## 1. What a requirement is here, and what it is not

A **requirement** is a condition the feature must satisfy before it is ready to build and allowed to ship. Two kinds matter, and the inquiry must find both:

- **The feature's own requirements.** What the person bringing the goal wants: the problem, the treatment they have in mind, the behaviour, the customers it is for, the measures of success. These usually arrive with the intent, partially.
- **The enterprise's requirements.** What any feature of this kind carries in this organisation whether or not anyone mentioned it: the law and the regulator's rules, internal policy and control standards, the platforms' and architecture's conditions for being used, the business's commercial and operational constraints. These usually do not arrive with the intent, and discovering them late is the failure this work is about.

A **dependency**, by contrast, is something the work needs that the team does not control, classified by the act an outside party must perform ([09](../research-dependency-agent/09-dependency-taxonomy.md): build, grant, decide, fund, align in time, tell). A requirement says what must be true; a dependency says who must act to make it true. Every requirement produces zero or more dependencies, and the inquiry in [02](02-structured-inquiry.md) walks from the first to the second. The two taxonomies are therefore different cuts of different things, and the first test of a good requirements partition is that its classes predict, reasonably well, which dependency classes will follow.

Three published schemes stand behind the comparison. The international product quality model partitions by quality characteristic, nine of them, and excludes "purely functional properties" by design ([ISO/IEC 25010:2023](../../research/sources/iso-iec-25010-2023-product-quality-model.md), independent). The best-known practitioner template partitions by section, mixing quality families with obligation sources, and gives every requirement a fit criterion and the legal sections a named validator ([Volere](../../research/sources/volere-requirements-specification-template.md), first-party). The business-analysis body of knowledge partitions by abstraction and beneficiary: business, stakeholder, solution, transition ([summary of the BABOK scheme](../../research/sources/techcanvass-babok-types-of-requirements.md), vendor claim). The literature's own verdict on single-axis schemes is that they leak: a requirement's class depends on how it is written, so the same security need can be a function, a quality or a constraint ([Glinz](../../research/sources/glinz-on-non-functional-requirements.md), independent), and most requirements labelled non-functional in eleven industrial specifications turned out to describe behaviour ([Eckhardt et al.](../../research/sources/eckhardt-are-non-functional-requirements-really-non-functional.md), independent). That is the backdrop against which both partitions below should be read: the question is not whether they leak but where, and whether the leaks matter for the inquiry.

## 2. Partition A: by obligation source

### 2.1 Principle

Classify each requirement by **who imposes it, and therefore who can waive or change it**. The test question is: *if this requirement were dropped, whose permission would that take?* Five classes cover the space the project's working definition names.

| Class | Imposed by | Can be waived by | What it typically looks like |
|---|---|---|---|
| **S1. Customer and feature goal** | The intent owner, on behalf of the customer or user | The intent owner | The problem, the treatment, the behaviour, acceptance criteria, the customers it is for |
| **S2. Law and regulation** | Legislatures, regulators, supervisory bodies, courts | Nobody inside the organisation | Statute, rules, supervisory guidance, filed terms, licence conditions |
| **S3. Enterprise policy and standards** | The organisation's policy, control, brand, records and risk owners | The policy owner, through an exception process | Control standards, brand guidelines, records schedules, the chosen accessibility level, security baselines, procurement rules |
| **S4. Platform and architecture standards** | The owners of the platforms and the architecture the feature must use | The platform owner or the architecture authority | API and integration standards, golden paths, data contracts, observability and release conventions, mandated strategic platforms |
| **S5. The business** | The accountable business owner: product line, channel, operations, finance | The business owner | Target market, pricing, volume caps, budget, servicing capacity, channel strategy, KPIs |

### 2.2 Tests

**Exclusivity.** Ask "who could waive it?" and take the answer that is *furthest from the feature team*. A disclosure that the regulator requires and that brand also has an opinion on is S2, because brand cannot waive it. A security control that policy mandates and a platform also enforces is S3, because the platform enforces it on policy's behalf. The rule is "file under the strictest imposer, record the others"; without it, exclusivity fails on every requirement that two parties care about, which in a regulated organisation is many.

**Exhaustiveness.** Every requirement has an imposer. The imposer is either external to the organisation (S2) or internal. If internal, it is either the feature's own owner (S1), a cross-cutting policy or control owner (S3), the owner of a platform or architecture the feature consumes (S4), or the business owner accountable for the feature's commercial and operational result (S5). Two groups of imposers do not fit cleanly, and section 5 reports them: counterparties under contract (card scheme rules, partner agreements, vendor terms), and the delivery team's own standards (an engineering definition of done). The first is external but not law; the second is internal but owned by the team, which the principle treats as "no requirement at all".

### 2.3 Why this partition is attractive for an agent

The class tells the agent **where to look and whom to ask**. S2 lives in regulator pages and the legal and compliance team's library; S3 in the policy library and the standards wiki; S4 in platform cards, developer portals and architecture decision records; S5 in business cases and the product line's plan; S1 in the intent itself and in past specs for similar features. The class also names the **validator**, and the validator is usually the owner of the dependency that follows ([09](../research-dependency-agent/09-dependency-taxonomy.md), class C). And it mirrors how risk review already works in regulated organisations: a knowable universe of enterprise obligations, each with an owner and heuristics for when it applies, which is the classification framing in the project's working definition ([intent shaping in a well-managed environment](../../research/sources/geoff-intent-shaping-well-managed-environment.md), first-party position).

## 3. Partition B: by quality attribute

### 3.1 Principle

Classify each requirement by **the property of the feature it constrains, and therefore how it is verified**. The test question is: *what kind of test, review or measurement would show this requirement is met?* Ten classes, drawn from the product quality model, the practitioner template and what regulated product work adds.

| Class | What it constrains | Verified by |
|---|---|---|
| **Q1. Functional behaviour** | What the feature does: inputs, rules, outputs, eligibility, flows | Functional test, review of rules |
| **Q2. Data** | What data is used, created, shared, classified, retained, and under what terms | Data lineage review, contract check, retention check |
| **Q3. Experience** | Usability, accessibility, content and wording, brand and design conformance | Usability test, accessibility audit, content review |
| **Q4. Security** | Confidentiality, integrity, authentication, authorisation, fraud resistance, audit trail | Security review, threat model, penetration test |
| **Q5. Privacy** | Lawful basis, consent, purpose limitation, minimisation, individual rights | Privacy assessment, consent-flow check |
| **Q6. Conduct and compliance** | How the feature treats customers against conduct rules: fairness, disclosure, suitability, promotions, complaints handling | Compliance review, sample testing |
| **Q7. Operability and resilience** | Running it: availability, support, servicing, incident handling, observability, release and rollback | Operational acceptance, resilience test |
| **Q8. Performance and capacity** | Speed, volume, throughput, limits | Measurement |
| **Q9. Measurement** | Instrumentation, success metrics, reporting, experiment design | Metrics review, data-quality check |
| **Q10. Change and transition** | Migration, training, rollout, maintainability, architecture conformance, the temporary needs of getting from here to there | Architecture review, migration test, readiness review |

### 3.2 Tests

**Exclusivity.** Ask "which verification proves it?" and file under the discipline that runs that verification. A disclosure requirement is Q6 if compliance samples it, Q3 if a content designer reviews it; it is one or the other by whose check is the gate. Where two disciplines both check (accessibility: audited by an accessibility specialist and sampled by compliance), the class is the one whose check is *mandatory*. This works less well than it sounds, because in a regulated organisation many checks are mandatory.

**Exhaustiveness.** Compared against the quality model's nine characteristics, the template's nine non-functional families and the business-analysis scheme's transition type: functional suitability maps to Q1; performance efficiency to Q8; compatibility and maintainability to Q10; interaction capability to Q3; reliability to Q7; security to Q4; flexibility and safety partly to Q7 and Q10 and partly nowhere (section 5). Privacy, conduct and measurement are additions the quality model lacks and regulated product work needs. What has no class at all is any requirement that is not a property of the product: *submit a change record*, *obtain actuarial sign-off*, *run a privacy assessment*, *train the servicing team*. The quality model excludes those by design; the practitioner template keeps them as "project issues" outside the requirements; the business-analysis scheme calls some of them transition requirements.

### 3.3 Why this partition is attractive for an agent

The class tells the agent **how to write the requirement so it can be checked**, which is what a coding agent or a reviewer downstream needs: a fit criterion, in the template's term, or an operational, quantitative, qualitative or declarative representation, in Glinz's ([Glinz](../../research/sources/glinz-on-non-functional-requirements.md), Table 2). It matches the way engineers and designers already think and the way a definition of done is written. And it keeps the requirements list to things the feature must *be*, pushing the things people must *do* toward the dependency taxonomy, where they arguably belong.

## 4. The test: four fictional features

Each feature is invented. Each table lists the requirements the inquiry would be expected to find, assigns a class under each partition, and marks the cases that break one partition or the other: **(2)** lands in two classes, **(0)** lands in none.

### 4.1 The bank's home-screen loan offer

A large retail bank, fictional and unnamed, wants to show a personal-loan offer on the home screen of its servicing app, with a tap-through to a pre-filled application. This is the scenario of the project's film brief ([07](../research-dependency-agent/07-film-brief.md)).

| # | Requirement | By source | By attribute | Note |
|---|---|---|---|---|
| 1 | Show a loan placement on the home screen to existing customers | S1 | Q1 | |
| 2 | Show it only to customers who pass a pre-eligibility screen (not in arrears, not already holding the product) | S1, S5 **(2)** | Q1, Q6 **(2)** | The business sets the screen; responsible-lending rules shape it; it is behaviour and conduct at once |
| 3 | Wording approved as a regulated financial promotion before it is shown | S2 | Q6, Q3 **(2)** | Compliance signs the wording; content design writes it |
| 4 | Representative rate and terms shown in the form the rules require | S2 | Q6 | |
| 5 | Customers who have opted out of marketing never see it | S2, S3 **(2)** | Q5 | Privacy law and the bank's own marketing policy |
| 6 | Suppressed for customers flagged as vulnerable or in financial difficulty | S2, S3 **(2)** | Q6 | Conduct rules and the bank's vulnerability policy |
| 7 | Accessible to the organisation's chosen conformance level | S2, S3 **(2)** | Q3 | Equality law in most jurisdictions; the level is policy ([WCAG 2.2](../../research/sources/w3c-wcag22-understanding-intro.md), first-party) |
| 8 | Uses the design system and brand tone | S3 | Q3 | |
| 9 | Built on the app's content-slot system, not custom screen code | S4 | Q10 | |
| 10 | Tap-through pre-fills the application from the customer record | S1 | Q1, Q2 **(2)** | |
| 11 | Every impression and decision logged and retained for the records period | S2, S3 **(2)** | Q4, Q7, Q6 **(2)** | Records law, records policy; an audit trail is security, operations and compliance evidence |
| 12 | Impressions and conversions instrumented into the metrics platform | S5, S4 **(2)** | Q9 | |
| 13 | Released on the app's train with a change record and store review | S4, S3 **(2)** | **(0)** | A process requirement, not a product property |
| 14 | The offer call adds under a set latency budget to the home screen, or fails silently | S4, S1 **(2)** | Q8, Q7 **(2)** | |
| 15 | Approvals capped at a monthly volume within the lending budget | S5 | Q1 | A business constraint written as behaviour |

### 4.2 The bank's cohort-targeted offer that needs a rules engine

The same bank's marketing team wants to show a fee-waiver offer only to a cohort: customers with regular salary credits above a threshold, no savings product, and marketing consent. This is the example in the project's working definition, and the worked example in [02](02-structured-inquiry.md), section 10.

| # | Requirement | By source | By attribute | Note |
|---|---|---|---|---|
| 1 | Offer shown only to customers in the defined cohort | S1 | Q1, Q2, Q6 **(2)** | Behaviour, data use and fair treatment at once |
| 2 | Cohort membership evaluated at display time, not from a nightly batch | S1 | Q1, Q8 **(2)** | |
| 3 | The rule that decided each customer's eligibility is reproducible and explainable for a complaint | S2, S3 **(2)** | Q6, Q7 **(2)** | Conduct rules on complaints; the bank's decisioning policy |
| 4 | The cohort definition must not act as a proxy for a protected characteristic | S2 | Q6 | |
| 5 | If a propensity model is used, it enters model-risk governance | S2, S3 **(2)** | **(0)** | A governance process, not a property ([SR 11-7](../../research/sources/federalreserve-sr-11-7-model-risk-guidance.md), regulator) |
| 6 | Salary-credit data used only within consented purposes | S2 | Q5, Q2 **(2)** | |
| 7 | Rule changes go through controlled change with an audit trail | S3 | Q7, Q4 **(2)** | |
| 8 | All offer decisions written to the one decisioning log the bank keeps | S3, S4 **(2)** | Q2 | An architecture principle enforced by a platform |
| 9 | Offer copy is a financial promotion and is approved as one | S2 | Q6 | |
| 10 | Uplift measured against a holdout; experiment registered | S5 | Q9 | |
| 11 | Servicing staff can see why a customer did or did not get the offer | S5, S2 **(2)** | Q7 | Operations wants it; complaints handling requires it |
| 12 | Must use the strategic decisioning platform where one exists | S4 | Q10 | The mandate that creates the platform-choice question |

### 4.3 The insurer's self-service mid-term vehicle change

A fictional insurer wants customers to add a vehicle to a motor policy mid-term in its app, see the re-rated premium and bind. This is the scenario of the project's dependency research ([01](../research-dependency-agent/01-dependency-management-today.md), [10](../research-dependency-agent/10-dialogue.md)).

| # | Requirement | By source | By attribute | Note |
|---|---|---|---|---|
| 1 | Customer can add a vehicle mid-term and see a re-rated premium | S1 | Q1 | |
| 2 | The re-rate uses the filed rating algorithm with no unfiled deviation | S2 | Q1, Q6 **(2)** | A filed term is law for this purpose; it is also the behaviour |
| 3 | Disclosure wording shown before bind in the states that require it | S2 | Q6, Q3 **(2)** | |
| 4 | Vehicle data validated against the vehicle-data vendor's service | S1, S4 **(2)** | Q2, Q1 **(2)** | |
| 5 | Driver records are personal data; a privacy assessment runs before bind | S2 | Q5, **(0)** for the assessment | The data condition is Q5; the assessment itself is a process |
| 6 | Proof-of-insurance documents regenerated within the time the state allows | S2, S1 **(2)** | Q1, Q8 **(2)** | |
| 7 | Billing adjusts the remaining instalments | S1 | Q1 | |
| 8 | Actuarial sign-off on mid-term re-rating | S5 | **(0)** | A business decision right |
| 9 | Velocity limits on self-service changes as a fraud control | S3 | Q4 | |
| 10 | Accessible to the chosen level | S2, S3 **(2)** | Q3 | |
| 11 | A call-centre agent can complete any change the app fails to | S5 | Q7 | |
| 12 | Records kept for each state's retention period | S2, S3 **(2)** | Q2 | |

### 4.4 The healthcare provider's patient-portal proxy access

A fictional healthcare provider wants patients to nominate a family member who can see chosen parts of their record in the patient portal.

| # | Requirement | By source | By attribute | Note |
|---|---|---|---|---|
| 1 | A patient can nominate a proxy and choose which record categories to share | S1 | Q1 | |
| 2 | The proxy's identity is verified to the assurance level the policy sets | S3, S2 **(2)** | Q4 | Policy sets the level; health-privacy law requires one |
| 3 | Consent is captured, revocable at any time and logged | S2 | Q5 | |
| 4 | Sensitive categories are excluded by default and need separate consent | S2, S3 **(2)** | Q2, Q6 **(2)** | Law for some categories; clinical policy for others |
| 5 | A clinical safety case shows the feature cannot harm a patient through a wrong record being shown | S2 | **(0)** or Q7 | Safety is a quality characteristic in the 2023 model and absent from this partition; the case itself is a process |
| 6 | Every proxy view is in the audit trail and visible to the patient | S2 | Q4, Q5 **(2)** | |
| 7 | Proxy access for minors follows age-based rules | S2 | Q1, Q6 **(2)** | |
| 8 | Accessible to the chosen level | S2, S3 **(2)** | Q3 | |
| 9 | Integrates through the record system's published interfaces and onboarding | S4 | Q10 | |
| 10 | A helpdesk process exists for disputes and revocation | S5 | Q7 | |
| 11 | Availability meets the portal's service level | S4 | Q7 | |
| 12 | Patient-facing wording reviewed for health literacy by the patient panel | S3 | Q3 | |
| 13 | Information-governance sign-off before go-live | S3 | **(0)** | |

### 4.5 Tally

Across the 52 fictional requirements:

| | Lands in two classes | Lands in none |
|---|---|---|
| By source | 22 | 0 inside the five classes, but see section 5.1 for the two imposers the classes do not name |
| By attribute | 19 | 6 (every process requirement, and clinical safety) |

The counts are from invented examples and prove nothing on their own. What they show is the *shape* of each partition's failure, which section 5 describes.

## 5. Where each partition breaks

### 5.1 By source

**Double imposition is the norm, not the exception.** Twenty-two of fifty-two requirements have two imposers, and the pattern is always the same: the law requires something and the organisation's policy specifies how it is met (accessibility level, marketing opt-out handling, vulnerability treatment, records retention, identity assurance). The "strictest imposer" rule resolves every case, but it hides something the inquiry needs: *the policy is the document the agent will find, and the law is the reason the policy cannot be waived.* An agent that files accessibility under S2 and reads only regulator pages misses the organisation's chosen level; one that files it under S3 and reads only the policy does not know the policy is non-negotiable. The fix is to record the chain, not the class: `imposed by: policy X; because: law Y`. That is a field, not a partition.

**Two imposers have no class.** Counterparties under contract impose real requirements that are neither law nor the organisation's own choice: card scheme rules in payments, a partner's co-branding terms, a vendor's acceptable-use terms, a reinsurer's conditions. And the delivery team's own standards (its definition of done, its test coverage bar) are internal requirements owned by nobody outside the team. The options are a sixth class, **S6 Contracts and counterparties**, with the team's own standards treated as S4 when the platform or architecture authority has adopted them and as S1 otherwise; or folding contracts into S2 as "external rules" at the cost of mixing what a regulator imposes with what a counterparty negotiated, which have different waiver paths. The lean is the sixth class, because waiver path is the partition's principle and the two differ.

**The source is often unknowable on day one.** The agent finds a wiki page that says "all offers must be suppressed for vulnerable customers" and nothing says why. Until a person tells it, the requirement sits in S3 by default (it is written in an internal document) with `source chain: unknown` flagged. This is the partition's weakness as a day-one instrument and its strength as a context-building one: every "why" the agent learns is written back once.

**Business constraints masquerade as behaviour.** "Approvals capped at a monthly volume" is S5 by source and Q1 by attribute. Under the source partition it is filed with the business owner, which is right for validation and wrong for implementation, because an engineer needs it as a rule in the feature. The hybrid fixes this: source for validation, attribute for writing.

### 5.2 By attribute

**Process requirements land nowhere.** Six requirements are things people must do, not properties the feature must have: a change record, a model-risk entry, a privacy assessment, actuarial sign-off, a clinical safety case, an information-governance sign-off. The quality model excludes them on purpose; the practitioner template parks them outside the requirements as project issues; the business-analysis scheme calls a few of them transition requirements. There are two honest responses. Add a class, **Q11 Process and evidence**, which keeps the requirements list complete but admits that the class is defined by "none of the above" and verified by "the gate accepted it". Or decide that these are not requirements at all but dependencies of class C in [09](../research-dependency-agent/09-dependency-taxonomy.md) (someone must decide), and let the dependency screen find them. The second is cleaner in theory and dangerous in practice: the inquiry's job is to surface these *early*, with the requirement that triggers them, and a privacy assessment that only appears when the universal screen runs is the late surprise the whole programme exists to prevent. The lean is to keep them as requirements with an explicit process class, each pointing at the gate it triggers.

**Conduct cuts across everything.** Nineteen requirements land in two attribute classes, and conduct and compliance (Q6) is one of the two in most of them. That is not a flaw in the examples; it is what regulated product work is like. Fair treatment is a property of the eligibility rule (Q1), of the data (Q2), of the wording (Q3) and of the complaint path (Q7). A compliance reviewer will say Q6 is not a quality attribute at all but a lens over all of them, and the literature says the same about security ([Glinz](../../research/sources/glinz-on-non-functional-requirements.md), section 3.3: a quality that applies to some use cases and not others "cannot be documented adequately with classic requirements specification templates"). The attribute partition therefore does worse on the enterprise obligations that matter most in this setting.

**Safety has no home.** The 2023 quality model added safety as a ninth characteristic. In the healthcare example it is a regulator-imposed, process-verified enterprise obligation that is also a property of the feature. The ten classes above fold it into operability and resilience, which a clinical safety officer would reject. Any organisation where safety is a first-order concern (healthcare, energy, transport) needs it as a class; a bank does not. That the right class list varies by industry is itself a finding: the attribute partition is less portable across regulated businesses than the source partition, because the sources (law, policy, platform, business, customer) are the same everywhere and the qualities are not.

**Representation decides the class.** "Offer shown only to customers in the cohort" is Q1 when written as a rule, Q6 when written as "treat customers fairly", Q2 when written as "use salary data to decide". The agent will meet all three phrasings in the sources it reads, and the class it assigns will depend on which it read first. This is the classification problem in its textbook form ([Glinz](../../research/sources/glinz-on-non-functional-requirements.md), section 3.2; [Eckhardt et al.](../../research/sources/eckhardt-are-non-functional-requirements-really-non-functional.md)). The practical consequence: an attribute class is only stable once the requirement has been rewritten into a checkable form, which happens *after* the inquiry has found it, not before. So the attribute partition is a poor index for finding and a good one for writing.

## 6. Options

| Option | What it is | Gives you | Costs and risks | What it needs |
|---|---|---|---|---|
| **O1. Source only** | Five (or six) classes by imposer; attribute recorded as free text if at all | One question per class tells the agent where to read and whom to ask; validators fall out; portable across industries | Double imposition everywhere; behaviour-like business constraints filed away from the engineers who implement them; the source is often unknown on day one | A source-chain field; a default class for "found in an internal document, reason unknown" |
| **O2. Attribute only** | Ten classes by property, plus a process-and-evidence class to be exhaustive | Each requirement written with a fit criterion; matches definitions of done and the quality model; engineers and designers recognise it | Conduct and security cut across; process requirements in a "none of the above" class; the class list varies by industry; class depends on phrasing | A rewriting step before classification; an industry-specific class list |
| **O3. Hybrid: source × attribute** | Every requirement carries a source class and an attribute class; the inquiry walks one axis and checks the other | Finding and validating by source; writing and verifying by attribute; the matrix's empty cells are a completeness check ("no S2 requirement with a Q4 attribute: is that right for a feature that handles personal data?") | Two classifications per requirement; the double-imposition and cross-cutting problems remain inside each axis; a 6×11 matrix is a lot of cells to show a product manager | A record schema with both fields; an inquiry that asks source questions first (section 3 of [02](02-structured-inquiry.md)) |
| **O4. Faceted** | Source, attribute, representation (operational, quantitative, qualitative, declarative), satisfaction (hard, soft), validator, as independent facets on a record ([Glinz](../../research/sources/glinz-on-non-functional-requirements.md), section 4.1) | The literature's answer to the classification problem; representation facet tells a downstream agent how to verify; satisfaction facet separates "must" from "should" | More fields than most people will fill; the facets are for the record, not for the conversation | A semi-structured record (the intent lifecycle home in [03](03-context-layer-model.md)); facets filled by the agent, confirmed by people |
| **O5. By validator** | Classes are the roles that sign off: the intent owner, legal and compliance, the policy owner, the platform owner, the business owner, the second line | The class *is* the dependency owner; asks group by person; closest to how a regulated organisation already runs review | Validators differ per organisation and change with reorganisations; two validators per requirement is common; it classifies by the organisation chart, which is the least stable thing in the building | A current decision-rights record; re-classification on every reorganisation |

The options are not exclusive. O3 is the usual form of O1 plus O2; O4 is O3 with two more fields; O5 is what O1 becomes once the validators are known, and the inquiry can run O1 and arrive at O5 by writing the validator back.

## 7. The lean, and what would change it

**Lean: the hybrid (O3), with source as the primary axis and attribute as the secondary, carried on a faceted record (O4) that fills in over time.** Concretely: the inquiry walks the source classes, because they tell a context-constrained agent where to look and whom to ask on day one and they are the same in a bank, an insurer and a hospital; each requirement found is then rewritten into a checkable form and given an attribute class, because that is what the people who build and verify it need; both classes, the source chain, the validator and the representation go on the record. The matrix of source by attribute is shown only as a completeness check, never as the conversation.

Reasons:

1. **Day-one findability** favours source. The raw sources the project assumes (enterprise search, tickets, catalogues, chat, the directory) are organised by owner and document type, which is the source axis. Nobody files a policy by quality attribute.
2. **Validation** favours source. The validator of a requirement is its imposer or that imposer's delegate, and the validator becomes the owner of the dependency. Source classes therefore predict dependency classes: S2 and S3 produce class C (decide) dependencies, S4 produces A, B and D (build, grant, fund), S5 produces C3 and D, S1 produces mostly A. The attribute classes predict nothing about who must act.
3. **Writing and verifying** favour attribute, and that is a later step. Once a requirement is found and validated, the attribute class and the representation tell a reviewer or a coding agent how to check it. The project's working definition wants a short, evidence-tied spec with a completeness standard ([intent factory](../../research/sources/geoff-building-accelerating-intent-factory.md), first-party position); the attribute class is where that standard bites.
4. **Portability across regulated businesses** favours source. The attribute list needed a safety class for healthcare that a bank does not need; the source list did not change.
5. **The literature** says a single axis leaks and recommends facets. The hybrid is the smallest faceted scheme that keeps the conversation simple.

What would change it:

- If a pilot shows that feature owners **cannot or will not name a source** for most enterprise requirements, and the agent cannot infer one from the documents it finds, then the source axis is an aspiration and the inquiry should walk attributes with source as an optional field. The test is the share of requirements with a verified source chain after the first quarter.
- If the context layer matures so that **every obligation has a published owner and reason** (the walk environment of the maturity model, [05](../research-dependency-agent/05-maturity-model.md)), source-first strengthens and the attribute axis can be generated from the obligation references rather than asked.
- If the organisation already runs a **validator-based review process** with stable decision rights, O5 may be the form people recognise, and the inquiry should group its questions by validator from the start.
- If engineers and designers find the source classes **alien in the artefact they read**, the spec view should be generated by attribute while the record keeps both.

## 8. Category reference

For the hybrid, both axes need the per-category detail the inquiry uses: what the class is, a fictional example, where an agent could find the requirement on day one, and who validates. Day-one sources are the raw ones the project assumes exist: enterprise search over documents, decks, wikis and code; tickets and intake history; catalogues, stale as they are; chat history; the people directory. The context-layer model in [03](03-context-layer-model.md) describes each source's yield and failure modes.

### 8.1 Source classes

| Class | What it is | Fictional example | Where the agent finds it on day one | Who validates |
|---|---|---|---|---|
| **S1. Customer and feature goal** | What the intent owner wants for the customer: problem, treatment, behaviour, acceptance, the customers it is for, success measures | "Customers with salary credits above the threshold and no savings product see the fee-waiver offer at login" | The intent itself; past specs for features of the same kind, found by enterprise search and the ticket history; research notes; the prototype | The intent owner; design research where it exists |
| **S2. Law and regulation** | Statute, regulator rules, supervisory guidance, filed terms, licence conditions, and the conduct they require | "Offer copy is a financial promotion and needs the approval the rules require"; "the re-rate uses the filed algorithm" | The legal and compliance team's library; regulator pages; gate criteria pages for the privacy, model-risk and promotion reviews (the published screening lists are the best day-one source: [ICO DPIA screening](../../research/sources/ico-when-do-we-need-a-dpia.md), regulator); past features' compliance findings in tickets | Legal and compliance; the second line; for filed terms, the filings team |
| **S3. Enterprise policy and standards** | The organisation's own rules: control standards, brand, records, accessibility level, security baseline, vulnerability policy, procurement, data classification | "Suppress all offers for customers flagged as vulnerable"; "retain decision logs for the records period" | The policy library; standards wikis; the control catalogue; brand and design-system sites; records schedules; a published service standard where one exists ([Service Standard](../../research/sources/govuk-service-standard.md), first-party, as the form); past specs' "non-functional" sections | The policy or control owner; brand; records management; the accessibility lead |
| **S4. Platform and architecture standards** | The conditions for using the platforms and the architecture the feature must consume: integration standards, golden paths, data contracts, mandated strategic platforms, observability and release conventions | "Use the content-slot system, not custom screen code"; "all offer decisions go to the one decisioning log"; "ride the app train" | Platform cards where they exist; developer portals and catalogues; API registries; architecture decision records; golden-path templates; the last two integrations' tickets and code | The platform owner; architecture review; the release manager |
| **S5. The business** | Commercial and operational constraints: target market, pricing, volume caps, budget, servicing capacity, channel strategy, KPIs, decision rights | "Approvals capped at a monthly volume"; "servicing staff can see why a customer did not get the offer"; "actuarial sign-off on mid-term re-rating" | The business case and the product line's plan; decision-rights documents; operations runbooks; the metrics platform's existing KPIs; the sponsor | The accountable business owner; operations; finance; the named decider |
| **S6. Contracts and counterparties** (proposed) | Obligations negotiated with a party outside the organisation that is not a regulator: scheme rules, partner terms, vendor terms, reinsurance conditions | "The partner's co-branding terms require their logo and disclosure"; "scheme rules fix the dispute window" | The contract register; vendor management; the third-party register; the partnership's own documents | Vendor or partnership management; legal |

### 8.2 Attribute classes

| Class | What it is | Fictional example | How it is verified | Where the agent finds the bar on day one |
|---|---|---|---|---|
| **Q1. Functional behaviour** | What the feature does | "Evaluate cohort membership at display time" | Functional test; rule review | The intent; past specs; the platform's capability description |
| **Q2. Data** | Data used, created, shared, classified, retained | "Salary-credit data read from the transactions domain under its data contract" | Lineage review; contract check; retention check | Data catalogue; data contracts; classification policy; records schedule |
| **Q3. Experience** | Usability, accessibility, content, brand | "Offer copy in the approved plain-language form; conformance to the chosen accessibility level" | Usability test; accessibility audit; content review | Design system; content guidelines; accessibility standard ([WCAG 2.2](../../research/sources/w3c-wcag22-understanding-intro.md)); past approved copy |
| **Q4. Security** | Confidentiality, integrity, authentication, authorisation, fraud resistance, audit trail | "Velocity limits on self-service changes"; "every proxy view in the audit trail" | Security review; threat model; test | Security baseline; control catalogue; past threat models |
| **Q5. Privacy** | Lawful basis, consent, purpose, minimisation, rights | "Marketing opt-outs honoured; data used within consented purposes" | Privacy assessment; consent-flow check | Privacy policy; consent records' schema; the published screening criteria |
| **Q6. Conduct and compliance** | Fairness, disclosure, suitability, promotions, complaints | "The cohort must not proxy for a protected characteristic" | Compliance review; sample testing | Conduct policies; promotion approval criteria; complaints procedures; past findings |
| **Q7. Operability and resilience** | Availability, support, servicing, incidents, observability, release, rollback | "A call-centre agent can complete a failed self-service change" | Operational acceptance; resilience test | Service levels; runbooks; operations' intake; the release calendar |
| **Q8. Performance and capacity** | Speed, volume, limits | "Offer call within the home-screen latency budget or fail silent" | Measurement | Platform performance budgets; past load tests |
| **Q9. Measurement** | Instrumentation, success metrics, reporting, experiments | "Uplift against a holdout; experiment registered" | Metrics review; data-quality check | The metrics platform; experiment registry; the product line's KPI definitions |
| **Q10. Change and transition** | Migration, training, rollout, maintainability, architecture conformance | "Built on the content-slot system"; "servicing team trained before launch" | Architecture review; migration test; readiness review | Architecture decision records; golden paths; past launch checklists |
| **Q11. Process and evidence** (needed for exhaustiveness) | A review, record or sign-off that must happen, pointing at the gate it triggers | "Model-risk entry if a propensity model is used"; "change record for the release" | The gate accepts it | Gate criteria pages; the change calendar; past features' gate records |

## 9. Key questions that would decide

1. **What share of enterprise requirements found in a pilot have a verifiable source chain (document, owner, reason) on day one, and what share after a quarter?** Answered by the pilot's requirements registers. Decides source-first against attribute-first.
2. **Do feature owners, engineers and designers recognise the source classes, or do they need the attribute view to read a spec?** Answered by watching three to five shaping sessions across job families. Decides which axis the conversation uses and which the record keeps.
3. **Which validators exist as stable roles with published decision rights, and which are "whoever answered last time"?** Answered by a decision-rights audit with the second line. Decides whether O5 is available.
4. **Are process requirements better found at stage 1 (with the triggering requirement) or as dependencies (by the universal screen)?** Answered by comparing, on past features, when each would have surfaced the privacy, model-risk and change requirements. Decides Q11 against class C in [09](../research-dependency-agent/09-dependency-taxonomy.md).
5. **Does the organisation have counterparty obligations (scheme rules, partner terms) often enough to need S6?** Answered by the contract register and the last year's features. Decides the sixth class.
6. **Which attribute classes does each industry need?** Answered per organisation: safety for healthcare and energy, conduct for financial services, and so on. Decides whether the attribute list is a fixed standard or a per-organisation configuration.
7. **Can the two classifications be assigned by the agent with acceptable false-positive and false-negative rates against labelled samples?** Answered by the labelled-sample evaluation the concept briefs propose ([05](05-concept-intent-shaping.md)), on the model of risk review as classification. Decides how much of the inquiry can be automated.
8. **How many requirements does the baseline (the obligations every feature of a kind carries) account for, against those specific to the feature?** Answered by the pilot's registers, by kind of feature. Decides how much of the inquiry can be copied from the last feature of the same kind, which is the first day-one heuristic in [02](02-structured-inquiry.md).

## 10. Evidence and its limits

The partitions are this document's design. The published schemes behind them are a standard ([ISO/IEC 25010:2023](../../research/sources/iso-iec-25010-2023-product-quality-model.md), independent), a practitioner template ([Volere](../../research/sources/volere-requirements-specification-template.md), first-party) and a body-of-knowledge scheme read through a training vendor's summary ([BABOK types](../../research/sources/techcanvass-babok-types-of-requirements.md), vendor claim). The leakage findings are independent and peer-reviewed ([Glinz](../../research/sources/glinz-on-non-functional-requirements.md); [Eckhardt et al.](../../research/sources/eckhardt-are-non-functional-requirements-really-non-functional.md)) but concern software requirements generally, not regulated product intent. The four feature tests are fictional and were written by the same hand as the partitions; they illustrate the failure modes rather than measure their frequency. The regulatory examples are generic (a promotion rule, a privacy screen, a model-risk regime, a filed term, a clinical safety case) and are not claims about any jurisdiction's current rules. Nothing here has been tried on a real organisation's features; question 1 in section 9 is the first thing a pilot should measure.
