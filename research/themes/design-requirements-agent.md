# Themes from design-requirements-agent

Filed 2026-11-06. Research for the high-level design of the enterprise requirements (intent-shaping) agent: how banks, large tech firms and standards bodies discover the obligations a change carries, what structured obligation data exists, and what is measured about elicitation agents. Evidence labels in brackets are the notes' own. New themes carry a description; bullets under existing slugs add evidence only.

## launch-readiness-review: New product approval and launch readiness review
The human processes that already ask "what must be true for this to ship here": bank new product approval (NPA) committees, regulators' product governance rules, and large-tech launch, privacy and operational readiness reviews. They define the triggers, categories, roles and records a requirements agent screens against and prepares for, and they show how such checklists are kept short and current.
- [OCC Bulletin 2017-43](sources/occ-bulletin-2017-43-new-modified-expanded-products.md): new, modified or expanded products need due diligence and approvals before launch, change management, monitoring with exit metrics and an exit strategy; named functions to consult. (first-party; design-requirements-agent)
- [NASD Notice to Members 05-26](sources/finra-ntm-05-26-reviewing-new-products.md): standard proposal, compliance triage of "new or material modification", working group, senior committee decision (often conditional), six-to-twelve-month post-approval review; 14 minimum questions. (first-party; design-requirements-agent)
- [FG22/5 Consumer Duty guidance](sources/fca-fg22-5-consumer-duty-guidance.md): product approval for new products and significant adaptations: granular target market, vulnerability, distribution strategy, testing with scenario analysis, regular review, listed evidence records. (first-party; design-requirements-agent)
- [Consumer Duty implementation: good practice](sources/fca-consumer-duty-implementation-good-practice.md): product development processes improving; weak spots are supply-chain information sharing and monitoring of distribution outcomes. (first-party; design-requirements-agent)
- [BCBS revised operational risk principles](sources/bcbs-revisions-principles-sound-management-operational-risk.md): Principle 7: first line assesses new products, activities, processes and systems; second line challenges and involves all control groups; review covers inherent, legal, ICT and model risk, residual risk, controls and metrics. (first-party; design-requirements-agent)
- [Reliable Product Launches at Scale](sources/google-sre-book-reliable-product-launches.md): Google's launch coordination checklist in nine categories, up to 70 launches a week, items justified by past disasters, low-risk fast path for about 30% of reviews. (first-party; design-requirements-agent)
- [Operational Readiness Reviews](sources/aws-operational-readiness-reviews-whitepaper.md): incident learnings distilled into curated questions; checklists per workload type; only GA-blocking risks included; self-assessment challenged by an Ops Champion. (first-party; design-requirements-agent)
- [Microsoft RAI Impact Assessment Template](sources/microsoft-rai-impact-assessment-template.md): completed when defining vision and requirements, reviewed and approved before development; per-intended-use stakeholders and harms; Goal applicability with a reason for every "No". (first-party; design-requirements-agent)
- [Microsoft Responsible AI Standard v2](sources/microsoft-responsible-ai-standard-v2.md): A1.1 to A1.3 set when the impact assessment is done, approved and re-done (annually, new intended use, new release stage). (first-party; design-requirements-agent)
- [Meta: Upholding Our Commitment to Protecting Your Privacy](sources/meta-upholding-commitment-privacy-ftc-2023.md): consent-order privacy review of about 1,200 products and features a month before ship. (vendor-claim; design-requirements-agent)
- [anthropics/claude-for-legal](sources/github-anthropics-claude-for-legal.md): launch-review skill walks eight categories with key questions and auto-skip conditions, calibrated on ten past reviews; daily launch-watcher on the tracker. (first-party; design-requirements-agent)
- [How Privacy-Savvy Are LLMs?](sources/arxiv-liu-privacy-savvy-llms-technical-review.md): ByteDance's privacy technical review reads requirement documents, designs, code and traffic before and after launch. (independent; design-requirements-agent)
- [Introducing AI Agents for Privacy](sources/privado-ai-agents-for-privacy.md): vendor agent pre-fills PIAs and DPIAs from PRDs and tickets. (vendor-claim; design-requirements-agent)

## obligation-libraries-as-data: Obligations and controls as structured, mapped data
Regulation and policy decomposed into single, identifiable mandates mapped to common controls, kept current from regulatory-change feeds, and in a few domains executed as code. This is the authoritative structured data a requirements agent would read obligations from, and the evidence on how far machine-readable regulation actually gets.
- [UCF Mapping Report: NIST CSF 1.1 Draft 2](sources/ucf-mapping-report-nist-csf-1-1.md): authority document to citations to single mandates to common controls in impact zones; 176 citations to 134 controls; open ambiguity questions recorded. (first-party; design-requirements-agent)
- [ServiceNow Regulatory Change Management](sources/servicenow-docs-regulatory-change-management.md): regulatory alerts from feeds (TRRI, LexisNexis, regulator RSS) triaged for applicability, gap-analysed against policies, citations and controls, closed after post-implementation review. (first-party; design-requirements-agent)
- [FCA/BoE Digital Regulatory Reporting Pilot Phase 1](sources/fca-boe-digital-regulatory-reporting-pilot-phase-1.md): no method yet scales to convert natural-language rules to code; humans must bridge gaps; interpret once centrally. (first-party; design-requirements-agent)
- [ISDA Digital Regulatory Reporting](sources/isda-digital-regulatory-reporting.md): industry-agreed interpretation of 14 reporting regimes coded on the Common Domain Model, live since 2022; a tracer agent explains field values. (first-party; design-requirements-agent)
- [CUBE and IBM target AI regulatory blind spot](sources/fintech-global-cube-ibm-regulatory-horizon-scanning.md): regulatory-intelligence vendor feeding horizon scanning into an AI-governance platform with an auditable review record. (vendor-claim; design-requirements-agent)
- [How Meta enforces purpose limitation](sources/meta-engineering-pai-purpose-limitation.md): a privacy requirement with an owner becomes data-flow labels and runtime enforcement across systems. (first-party; design-requirements-agent)

## elicitation-agent-evidence: Measured performance of LLM requirements-elicitation agents
Controlled studies and benchmarks of LLM interviewers and requirement classifiers: how much of what a stakeholder did not say they surface, what structure helps, and where they fail. It bears on how much of the requirements agent's inquiry can be open conversation versus structured screening.
- [LLMREI](sources/arxiv-korn-llmrei.md): GPT-4o interviewer elicited up to 73.7% of requirements with mistake rates similar to trained student interviewers; one hallucinated estimate, one request for personal data. (independent; design-requirements-agent)
- [ReqElicitGym](sources/arxiv-jin-reqelicitgym.md): best frontier model elicited 32% of implicit requirements; Claude Opus 4.5 7 to 8%; probing beats clarifying; style requirements near zero. (independent; design-requirements-agent)
- [From Chat to Interview (OntoAgent)](sources/arxiv-jin-ontoagent-chat-to-interview.md): an ontology of requirement concerns selecting each next question gave +33% implicit-requirement elicitation over baselines. (independent; design-requirements-agent)
- [Elicitron](sources/arxiv-ataei-elicitron.md): latent-need classification F1 rose from 0.76 zero-shot to 0.95 with explicit criteria and chain-of-thought. (independent; design-requirements-agent)
- [How Privacy-Savvy Are LLMs?](sources/arxiv-liu-privacy-savvy-llms-technical-review.md): personal-data extraction F1 about 99 and legal key-point detection about 94 to 95, QA exact-match weak. (independent; design-requirements-agent)

## regulatory-drivers-of-process: Regulation prescribes the record and the independence, not the meeting
- [OCC Bulletin 2017-43](sources/occ-bulletin-2017-43-new-modified-expanded-products.md): sets risk categories, functions and artefacts for new activities but no template; each bank writes its own NPA form. (first-party; design-requirements-agent)
- [NASD Notice to Members 05-26](sources/finra-ntm-05-26-reviewing-new-products.md): written procedures required under supervision rules; best practices "not designed as a safe harbor". (first-party; design-requirements-agent)
- [FG22/5 Consumer Duty guidance](sources/fca-fg22-5-consumer-duty-guidance.md): lists the records that evidence product governance (target market assessment, testing with scenario analysis, distributor information, reviews). (first-party; design-requirements-agent)
- [Consumer Duty implementation: good practice](sources/fca-consumer-duty-implementation-good-practice.md): boards expected to use outcome data, including for vulnerable customers. (first-party; design-requirements-agent)
- [BCBS revised operational risk principles](sources/bcbs-revisions-principles-sound-management-operational-risk.md): three-lines roles in change approval; central product record expected. (first-party; design-requirements-agent)
- [Microsoft Responsible AI Standard v2](sources/microsoft-responsible-ai-standard-v2.md): internal policy written where law had not caught up, as a living document. (first-party; design-requirements-agent)
- [Meta: Upholding Our Commitment to Protecting Your Privacy](sources/meta-upholding-commitment-privacy-ftc-2023.md): a consent order drives per-launch review and biennial external assessment. (vendor-claim; design-requirements-agent)

## process-governance-load: Process governance as a dependency: gates, evidence and waiting
- [OCC Bulletin 2017-43](sources/occ-bulletin-2017-43-new-modified-expanded-products.md): due diligence consults compliance, legal, risk, IT and security, audit, credit, payments, accounting, operations, marketing and treasury. (first-party; design-requirements-agent)
- [NASD Notice to Members 05-26](sources/finra-ntm-05-26-reviewing-new-products.md): compliance and legal embedded early so they are not a late obstacle. (first-party; design-requirements-agent)
- [BCBS revised operational risk principles](sources/bcbs-revisions-principles-sound-management-operational-risk.md): second line ensures finance, compliance, legal, business, ICT and risk are involved. (first-party; design-requirements-agent)
- [ServiceNow Regulatory Change Management](sources/servicenow-docs-regulatory-change-management.md): role split from triage to SME assessment to action tasks. (first-party; design-requirements-agent)
- [Meta: Upholding Our Commitment to Protecting Your Privacy](sources/meta-upholding-commitment-privacy-ftc-2023.md): 800+ engineers and $5bn+ (Meta's figures) for the privacy program. (vendor-claim; design-requirements-agent)

## risk-review-as-classification: Risk review as a specification and classification problem
- [OCC Bulletin 2017-43](sources/occ-bulletin-2017-43-new-modified-expanded-products.md): new, modified and expanded defined by nature, terms, purpose, scale, use, customers, markets and channels. (first-party; design-requirements-agent)
- [NASD Notice to Members 05-26](sources/finra-ntm-05-26-reviewing-new-products.md): practical criteria for "new" or "material modification"; err to full review when unsure. (first-party; design-requirements-agent)
- [FG22/5 Consumer Duty guidance](sources/fca-fg22-5-consumer-duty-guidance.md): "significant adaptation" judged by potential customer impact, with worked examples; small changes can add up. (first-party; design-requirements-agent)
- [Microsoft RAI Impact Assessment Template](sources/microsoft-rai-impact-assessment-template.md): sensitive-use triggers and single-choice ratings of readiness, complexity, human role. (first-party; design-requirements-agent)
- [anthropics/claude-for-legal](sources/github-anthropics-claude-for-legal.md): each review category has a key question and an explicit auto-skip condition. (first-party; design-requirements-agent)
- [How Privacy-Savvy Are LLMs?](sources/arxiv-liu-privacy-savvy-llms-technical-review.md): ten legal key points detected as binary classification at F1 about 94 to 95. (independent; design-requirements-agent)

## requirements-partitions: How requirements are partitioned, and why every single-axis partition leaks
- [Microsoft RAI Impact Assessment Template](sources/microsoft-rai-impact-assessment-template.md): enterprise obligations partitioned by Goal family, each with an applicability condition and a mandatory reason when not applicable. (first-party; design-requirements-agent)
- [UCF Mapping Report: NIST CSF 1.1 Draft 2](sources/ucf-mapping-report-nist-csf-1-1.md): controls partitioned by impact zone, independent of each source document's structure. (first-party; design-requirements-agent)
- [FG22/5 Consumer Duty guidance](sources/fca-fg22-5-consumer-duty-guidance.md): the target market anchors design, distribution and review requirements. (first-party; design-requirements-agent)
- [INCOSE Guide to Writing Requirements (Jama)](sources/jama-incose-requirements-writing-guide.md): statement-level versus set-level characteristics; completeness is a set property. (vendor-claim; design-requirements-agent)

## rules-vs-judgment-encoding: Encoding standards as rules vs as reasons and judgment
- [INCOSE Guide to Writing Requirements (Jama)](sources/jama-incose-requirements-writing-guide.md): NLP checks vague terms, escape clauses, passive voice, combinators; necessity and correctness need an engineer. (vendor-claim; design-requirements-agent)
- [Jama Connect Advisor: Interpreting the results](sources/jama-connect-advisor-interpreting-results.md): per-rule INCOSE scores and EARS rewrites; scoring method undisclosed. (first-party; design-requirements-agent)
- [FCA/BoE Digital Regulatory Reporting Pilot Phase 1](sources/fca-boe-digital-regulatory-reporting-pilot-phase-1.md): even "unambiguous" rules need human assumptions before they can be code. (first-party; design-requirements-agent)
- [UCF Mapping Report: NIST CSF 1.1 Draft 2](sources/ucf-mapping-report-nist-csf-1-1.md): one mandate per mapped statement; explanatory text ignored. (first-party; design-requirements-agent)
- [Operational Readiness Reviews](sources/aws-operational-readiness-reviews-whitepaper.md): each question carries guidance and risk-rated answers. (first-party; design-requirements-agent)
- [How Meta enforces purpose limitation](sources/meta-engineering-pai-purpose-limitation.md): point checks in code were fragile; infrastructure enforcement scaled. (first-party; design-requirements-agent)

## governance-as-code: Governance as code: gates and evidence as data
- [BCBS revised operational risk principles](sources/bcbs-revisions-principles-sound-management-operational-risk.md): "central record of their products and services" expected. (first-party; design-requirements-agent)
- [Microsoft Responsible AI Standard v2](sources/microsoft-responsible-ai-standard-v2.md): requirements with IDs, "Applies to" scopes and tags. (first-party; design-requirements-agent)
- [ISDA Digital Regulatory Reporting](sources/isda-digital-regulatory-reporting.md): committee-governed interpretation executed as code. (first-party; design-requirements-agent)
- [UCF Mapping Report: NIST CSF 1.1 Draft 2](sources/ucf-mapping-report-nist-csf-1-1.md): NLP tagging plus vector matching of mandates to controls. (first-party; design-requirements-agent)
- [Consumer Duty implementation: good practice](sources/fca-consumer-duty-implementation-good-practice.md): outcome metrics and out-of-target-market tracking as monitoring requirements. (first-party; design-requirements-agent)

## checklist-implementation-fidelity: Checklists work through the behaviour they force
- [Reliable Product Launches at Scale](sources/google-sre-book-reliable-product-launches.md): engineers skip burdensome processes; checklist must be lightweight yet thorough, applied high-touch. (first-party; design-requirements-agent)

## skill-improvement-loops: How skills and agent instructions get better
- [Reliable Product Launches at Scale](sources/google-sre-book-reliable-product-launches.md): items justified by past disasters; full review once or twice a year. (first-party; design-requirements-agent)
- [Operational Readiness Reviews](sources/aws-operational-readiness-reviews-whitepaper.md): Ops Champions turn new incident analyses into new questions and retire stale ones. (first-party; design-requirements-agent)

## compounding-context-repo: Context that compounds with each shipped feature
- [Operational Readiness Reviews](sources/aws-operational-readiness-reviews-whitepaper.md): the organisation's own incident data is the source of the checklist. (first-party; design-requirements-agent)
- [anthropics/claude-for-legal](sources/github-anthropics-claude-for-legal.md): calibration table learned from ten past launch reviews; "The calibration table is the whole thing". (first-party; design-requirements-agent)
- [ISDA Digital Regulatory Reporting](sources/isda-digital-regulatory-reporting.md): interpretation done once and shared across firms. (first-party; design-requirements-agent)

## risk-sloped-review: Human review sloped to risk
- [Reliable Product Launches at Scale](sources/google-sre-book-reliable-product-launches.md): low-risk launches get a shortened checklist (about 30% by 2008). (first-party; design-requirements-agent)

## agent-led-intent-shaping: Agents shape intent, not only execute it
- [Microsoft RAI Impact Assessment Template](sources/microsoft-rai-impact-assessment-template.md): a feature-first interview structure an agent could run and pre-fill. (first-party; design-requirements-agent)
- [LLMREI](sources/arxiv-korn-llmrei.md): one question at a time; context-deepening questions dominate. (independent; design-requirements-agent)
- [ReqElicitGym](sources/arxiv-jin-reqelicitgym.md): free-form interviewing misses most unstated requirements. (independent; design-requirements-agent)
- [From Chat to Interview (OntoAgent)](sources/arxiv-jin-ontoagent-chat-to-interview.md): concern ontology mined from past requirements drives the next question. (independent; design-requirements-agent)
- [Elicitron](sources/arxiv-ataei-elicitron.md): explicit criteria lift classification of unstated needs. (independent; design-requirements-agent)

## synthetic-users-limits: Synthetic users and AI personas: limits
- [Elicitron](sources/arxiv-ataei-elicitron.md): simulated users surface many latent needs, but labelling is subjective and prioritising stays with the designer. (independent; design-requirements-agent)

## ai-synthesis-hallucination-risk: AI synthesis can invent or merge facts
- [anthropics/claude-for-legal](sources/github-anthropics-claude-for-legal.md): "No silent supplement" rule and source-tiered citation tags. (first-party; design-requirements-agent)
- [LLMREI](sources/arxiv-korn-llmrei.md): an unfounded price estimate and a request for personal data in 33 interviews. (independent; design-requirements-agent)

## human-review-gates: Human review gates on agent output
- [anthropics/claude-for-legal](sources/github-anthropics-claude-for-legal.md): every output a draft for attorney review; consequential actions confirmed. (first-party; design-requirements-agent)

## evals-autonomy-trust: Evals, autonomy sliders and earned trust
- [ReqElicitGym](sources/arxiv-jin-reqelicitgym.md): oracle user and LLM judge validated against real transcripts and experts (kappa 0.73 to 0.78). (independent; design-requirements-agent)

## method-as-harness: Method as harness
- [From Chat to Interview (OntoAgent)](sources/arxiv-jin-ontoagent-chat-to-interview.md): a fixed per-turn procedure over a concern ontology. (independent; design-requirements-agent)

## standard-form-spectrum: The form a standard takes
- [Microsoft Responsible AI Standard v2](sources/microsoft-responsible-ai-standard-v2.md): principles to Goals to identified requirements with applicability scopes. (first-party; design-requirements-agent)

## spec-edge-case-review: Agents for spec edge-case review
- [INCOSE Guide to Writing Requirements (Jama)](sources/jama-incose-requirements-writing-guide.md): set-level completeness (C10) is what an obligation screen adds. (vendor-claim; design-requirements-agent)

## prd-agents: PRD and spec writing/review as an agent job
- [Introducing AI Agents for Privacy](sources/privado-ai-agents-for-privacy.md): PRDs and tickets as the input for pre-filled privacy assessments. (vendor-claim; design-requirements-agent)

## vendor-claims-vs-independent-evidence: Vendor claims dominate; independent evidence is rare
- [CUBE and IBM target AI regulatory blind spot](sources/fintech-global-cube-ibm-regulatory-horizon-scanning.md): conflicting coverage figures; no accuracy evidence for obligation extraction. (vendor-claim; design-requirements-agent)
- [Jama Connect Advisor: Interpreting the results](sources/jama-connect-advisor-interpreting-results.md): no published accuracy for requirements-quality tools. (first-party; design-requirements-agent)
- [Introducing AI Agents for Privacy](sources/privado-ai-agents-for-privacy.md): no metrics or review design. (vendor-claim; design-requirements-agent)
