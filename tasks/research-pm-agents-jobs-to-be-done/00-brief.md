# Brief: PM jobs to be done, and where job/persona-based PM agents have worked

Date: 2026-10-24. Read-only web research (search + page fetches; no logins). Three subagents produced the detailed files; I read the video transcript myself (primary source). **Audited 2026-10-24 (Fable 5.1, with Opus sub-auditors):** every claim in files 01-03 was re-checked against its source note and, where the note was thin, against the original page; about 540 claims checked, about 110 corrections made, 24 source notes added, and anything still unconfirmed is marked "(unverified)" in the detail files. Audit logs: [audit-2026-10-24.md](audit-2026-10-24.md) (lead), [01](audit-2026-10-24-01-jobs-map.md), [02](audit-2026-10-24-02-commercial.md), [03](audit-2026-10-24-03-in-practice.md). Quotes were read through a page-fetch tool, so treat them as near-verbatim and spot-check before public use.

Files in this folder:
- `01-jobs-to-be-done-map.md`: 40 sources (9 added in audit); frameworks (SVPG, Torres, Pragmatic, JTBD), PM time/AI-use surveys, personas, job x stage x persona matrix, 10 job cards, automatable-vs-judgment.
- `02-commercial-pm-agents.md`: 23 commercial products, evidence rated.
- `03-in-practice-cases-and-failures.md`: 20 in-practice cases (Ramp, Atlassian, Meta, Anthropic, Intercom, Notion, ...) plus failures and limits.
- Source notes live in the shared library, not here: [Atlassian talk note](../../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md) and [full transcript](../../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.transcript.md) (YouTube auto-captions). Every other source has a note in `research/sources/` (see `research/INDEX.md`), linked from files 01-03.

## Bottom line

1. **The jobs are stable; the methods are moving.** Yehoshua (Atlassian CPO): the PM job "is really the same as it always was" (find product-market fit, build products people love, build a business); what changed is how ([transcript](../../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.transcript.md) 02:30). The jobs-map file agrees: ten recurring jobs, from customer contact and synthesis through spec, prioritization, delivery, launch, stakeholder comms, metrics and post-launch triage.
2. **Best-evidenced agent jobs are the "bounded, context-fed, reviewable" ones:** feedback/voice-of-customer triage and synthesis, status/update drafting and aggregation, spec/PRD first drafts, prototyping, and "answer questions from org context" (e.g. launch timing). Weakest: strategy, opportunity selection, prioritization trade-offs, interviewing. These match survey data and practitioner statements (file 01 sec. 3, 7).
3. **Hard evidence is thin everywhere.** After re-fetching every reachable source: no independent controlled evaluation of any PM agent doing a PM job exists in what we found (file 02), none of the 20 in-practice cases is an independently measured success (file 03), and there is no agent-vs-human comparison of PRD, prioritization or status quality. Time-saved numbers are self-reported; none measure decision quality or product outcomes. Atlassian says plainly it has not figured out how to measure outcomes (transcript 19:35-20:35). The only randomized evidence nearby is the [METR RCT](../../research/sources/metr-early-2025-experienced-developer-rct.md) on coding (developers 19% slower while believing they were ~20% faster), which is a warning about self-reports, not about PM agents.
5. **Two findings cut against the map's own ratings** (from the audit): Lenny's 2024 piece ([S40](../../research/sources/lenny-how-ai-will-impact-product-management.md), opinion) rates strategy and goals as the PM tasks most exposed to AI, against the map's Low rating for J2; and Microsoft's 885-PM telemetry study ([S34](../../research/sources/arxiv-pm-delegating-work-to-genai.md)) shows far lower AI use for research (22%) and prototyping (12%) than for drafting (73%), with specs held back as high-accountability work. Both are now in the map; the ratings stay labelled as judgment.
4. **Pattern that recurs among successes: the agent is wired into org context** (Atlassian "teamwork graph"; Ramp Glass connected to data/codebase/customer calls; Meta VP's agents over his own docs) and a human reviews. Failures cluster where context is thin or synthesis is unchecked.

## Jobs to be done (condensed; full matrix in file 01)

| Job | Typical artifacts | Agent suitability (my judgment, from file 01) | Best evidence it works |
|---|---|---|---|
| Customer contact and research synthesis | interview notes, insight snapshots | Medium: cluster/draft = high; choosing questions, interviewing = human | Atlassian: Rovo agent categorized 900+ feedback items (talk, self-reported); Torres: invented details and merged quotes in a 17-transcript error analysis, ~30% of ChatGPT's direct quotes wrong or missing in a separate test, so she checks quotes against source (independent practitioner, three Product Talk pages) |
| Opportunity, strategy, vision | strategy docs, opportunity trees | Low | Surveys: strategy/discovery sit at bottom of AI use (Lenny survey); 49% of PMs lack time for strategic planning (Atlassian State of Product, vendor survey of 700 managers + 521 PMs); contested: Lenny's 2024 opinion piece rates strategy as most AI-exposed |
| Product / intent shaping | prototypes, problem statements | Medium-high for prototypes | Atlassian Loom -> work item -> coding agent flow; Meta VP: PRD replaced by a paragraph + prototype (eval set only for ML-heavy work); Product Talk roundup of 11 Lovable users (independent, candid on breakage) |
| PRD write and review | specs, edge-case lists | High for drafts; medium for review | Lenny survey: PRDs are top current AI use (21.5%); ChatPRD single-author test (low); Cowork PM plugin (no outcomes) |
| Prioritization and roadmap | scored backlogs, Now/Next/Later | Medium (agent prepares, human decides) | Mostly vendor tooling claims; no outcome evidence |
| Delivery management | tickets, unblock | High for aggregation/triage | Jira agent triages Slack bugs to a coding agent (talk) |
| Launch / GTM coordination | enablement, release notes | Medium-high for drafts | Ramp Glass emails customers when requested features ship (first-party post) |
| Stakeholder comms / exec updates | weekly updates, status | High | PM-built weekly-update agent at Atlassian (talk); CEO self-serves launch timing via Rovo (talk); Meta VP nightly decision punch list |
| Metrics review / experiments | dashboards, anomaly notes | Medium-high for pulls, medium for interpretation | Vendor claims (Amplitude, Mixpanel, Pendo); Anthropic PM's adoption-analytics use (first-party, single PM); no experimentation-specific source found |
| Post-launch feedback triage | clustered tickets, severity | High | Notion routing agent, Atlassian 900+ items, Enterpret/Unwrap vendor case claims |

Persona differences (file 01 sec. 4, 8): founder-PM/"AI builder" collapses roles (evidence thin: Gamma ~1 PM per 4 engineers, job posts); IC PM at large company mostly keeps "steering" roles and uses agents for comms, triage, prototyping; CPO/head-of-product consumes agent-produced context; product ops, platform PM, PMM evidence is mostly vendor blogs and job posts.

Survey data (all self-selected; directional): Lenny's survey (1,750, independent): 63% of PMs say they save 4+ hours/week, but only 4.7% use AI for user research despite the largest demand gap. Vendor surveys (Productboard, Productside, UXCam, Atlassian, Product Focus) show near-universal adoption but only ~1 in 4 with a strategy to show for it (Productside). The one telemetry-backed study (Microsoft, 885 PMs, single company) finds 62% daily use, concentrated in drafting; self-reports matched telemetry only moderately.

## Where PM-job agents have worked, with evidence quality (details and URLs in files 02-03)

| Org | What the agent does | PM job | Evidence | Quality |
|---|---|---|---|---|
| Atlassian | Rovo agent triages/categorizes 900+ feedback items; PM-built weekly-update agent; Jira agent in Slack triages bugs; Loom-to-coding-agent prototyping | Discovery synthesis, status comms, triage, prototyping | Primary transcript of CPO talk ([transcript note](../../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md)); numbers self-reported, no baseline | Med-low (first-party anecdote) |
| Ramp | Glass: feature-request capture from calls (~20k/month vs ~300 by hand), customer emails on ship, evidence-backed specs/prototypes from connected data; Gadget (a separate coordination agent, not Glass) credited with fully answering "85% of questions asked to PMs" | Intent shaping, feedback capture, comms, status Q&A | First-party launch post (CEO) and CPO talk transcript; all speaker-reported | Med / Med-low |
| Meta (one VP, personal system) | Review-doc drafting, 7am decision punch list, analytics agent; PRD replaced by a paragraph + prototype (+ eval set for ML-heavy work) | Review prep, status, metrics | Write-up by Nikhyl Singhal (The Skip), cross-posted by Lenny's Newsletter (ad block, not sponsored content); "six months in, it's accurate" from nightly self-checks; one brief dropped source links | Med (candid) |
| Anthropic | Managed-agents PM: adoption analytics, sentiment monitoring, spec-by-prototype; Cowork PM plugin | Metrics, discovery, spec, roadmap | First-party posts, no outcomes | Low-med |
| Notion | Custom Agents study with MeasuringU: 218 people, 93% vs 59% task success, 38% less time; most-used internal agent routes product feedback (co-founder-built) | Generic knowledge work incl. feedback routing | Vendor-published study, no method detail; launch post | Low (re-rated in audit: vendor-published) |
| Product Talk (Torres) | Lovable prototyping roundup (11 named users); AI interview-analysis experiments | Prototyping, discovery synthesis | Independent practitioner; reports failures | Med (roundup) / High (for limits) |
| Rovo customers (Procore, Tempo) | Roadmap-item drafting (Procore "1 hour to 15 minutes"); Tempo "30% faster" | PRD/roadmap items | Procore and "44% more accurate" figures come from Atlassian's own blog; Tempo is an Atlassian partner page, method not visible; practitioner accounts report hallucinations | Low (re-rated in audit) |
| Dovetail, Enterpret, Unwrap | Research/feedback synthesis (Instawork 1-2 h/project; GitHub Copilot team 4-5 h/week); Dovetail's Forrester TEI is Dovetail-commissioned; Unwrap's "$180k/yr" is a hypothetical calculation | Discovery synthesis | Vendor customer stories | Low |
| Productboard (Spark now GA), Amplitude, Pendo, Aha!, Linear (dogfooding post), Mixpanel, Zeda, Maze, ChatPRD (one-author 5-tool test, 2nd of 5; vendor customer stories) | Discovery, metrics, triage, PRD features | Various | Launch posts, docs, testimonials without method | Low (ChatPRD Low-med) |

## Failures and limits (file 03)

- NN/g (read directly, 2024): synthetic users over-optimistic, uncritical and shallow. Torres (three Product Talk pages): invented details and merged quotes in a 17-transcript ChatGPT error analysis; ~30% of direct quotes wrong or missing in another test; 15 interviews through ChatGPT and Claude in the podcast account (whether these are one experiment is not stated); she checks quotes against source and warns synthesis skills atrophy. Academic: an ISPOR poster (10 interviews, Copilot) reports 11-25% incorrect information and misattributed quotes (search summary only, unverified); a Turku replication (17 interviews, DeepSeek R1) found concepts kept but interpretive depth lost (abstract only); by contrast one arXiv paper on literature-review data extraction (not interviews) found LLM inaccuracies of 1.51% vs 4.37% for humans. A Stanford study in Science (2026) found 11 models affirmed users' actions ~49% more often than humans did, and users trusted the sycophantic answers more.
- Practitioner reports: AI PRDs that "read well but lack specificity" without org context (one CRO consultant's post, anecdotal); Linear's Saarinen (essay read directly): product changes are mostly additive and agent-made changes average the product into "Frankenstein's monster" (he does not use the phrase "additive drift"); Cagan (podcast, read): one-click AI PRDs that skip customers "speed up a bad process" and "product management theater" is his own 2024 SVPG post; prototypes that break as complexity grows and about half of teams moving on from Lovable (Product Talk roundup); hallucinations in Rovo output reported by practitioners and partners (file 02). A claim that CleverX warned about fabricated quotes was itself fabricated by the earlier pass and has been removed.
- Atlassian kept PMs out of production code on Jira ("can be kind of dangerous") and gave PMs an isolated repo for Confluence (transcript 09:32, 12:33).
- Macro statistics, not PM-specific: Gartner's "over 40% of agentic AI projects cancelled by end of 2027" is an analyst prediction with no stated method (press release, page returned 403). MIT NANDA's "95% get zero return" (primary now read) rests on self-reported success six months after pilots, from 52 interviews and 153 surveys, with selection bias acknowledged; its "bought tools reach deployment ~67% vs ~33% for internal builds" is called correlation, not causation. Fortune's reported sample figures do not match the report.

## What I could not verify

- Any independent, controlled evaluation of PM agents; any quality comparison of agent vs human PRDs/prioritization/updates.
- After the audit every reachable source was re-fetched. Still unverified and marked inline: ~16 items in file 01 (Haberlah blocked, ProductPlan gated, CustomerThink ODI figures, MindStudio 80%), ~35 in file 02 (G2, TrustRadius, TheCXLead, Gartner, several Atlassian customer/community pages blocked or moved), ~15 in file 03 (Microsoft feedback system and Punch List bodies, Intercom "100+ skills", Block PM use, Amazon Kiro, Turku beyond abstract, Gartner page).
- Shopify, Google, Duolingo, Figma, Stripe, Amazon (PRFAQ), Mercury: no first-party PM-agent write-up found.
- Source paywalls: Torres's podcast transcript and part of her AI article, Tal Raviv guide, Block episode, Lenny's "50 ways" piece; the Atlassian and Product Focus PDFs were read (one helper cached them locally in a tool cache outside the project, against the no-download rule; nothing was executed).
- The transcript is YouTube auto-captions (ASR errors; see file header), not an official transcript.
- Full gap lists: file 01 sec. 9, file 02 and 03 gap sections, and the three audit logs.

## Implications for concepts (suggestions, not decisions)

- Most defensible agent jobs to prototype first (unchanged by the audit, but now resting on self-reported cases only): feedback triage/synthesis with citations back to source quotes, status/update drafting from org context, "ask the org" launch/status Q&A, PRD first-draft-plus-gap-review. Reason: bounded, reviewable, with the most (still modest) first-party evidence.
- Treat strategy/opportunity selection and prioritization trade-offs as human-led with agent preparation.
- Design in the failure mitigations the evidence points to: grounding in org context, source-link/quote verification (Torres), human review gate, isolated environments for any code writing.
- Evidence gap is itself an opening: nobody publishes outcome measures; a concept that bakes in measurement would differentiate.

## Options by dimension

My findings are in the shared register, [options/DIMENSIONS.md](../../options/DIMENSIONS.md) (consolidated by the director on 2026-10-24; my original sections now sit as sub-choices under parents). Each ends with key questions. No winner is picked; leans are noted with what would change them.

- [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent): added options for a task-specific agent per PM job, a persona "PM agent", and a general harness plus PM skills (sub-choice work-structure), and the sub-choice agent-unit (persona vs job vs stage vs workflow chain). No source compares a task agent with a skill.
- [capability-format-portability](../../options/DIMENSIONS.md#capability-format-portability-capability-format-and-portability): how PM jobs are packaged today (Cowork PM plugin, Glass skills, PM-built Rovo agents) and a key question on skill vs deployed agent per job.
- [sequencing](../../options/DIMENSIONS.md#sequencing-which-jobs-first-and-which-layer-first), sub-choice pm-job-sequencing: which PM jobs to automate first. Lean: bounded, reviewable jobs (feedback triage, status/updates, spec first draft plus gap review); would change if user interviews show a different top pain or a trial shows review cost cancels the saving.
- [review-and-autonomy](../../options/DIMENSIONS.md#review-and-autonomy-review-and-autonomy), sub-choice review-gate-placement: human-every-time vs verifiers vs isolation vs risk-sloped.
- [context-and-memory](../../options/DIMENSIONS.md#context-and-memory-context-and-memory), sub-choice org-context-grounding-source: platform graph vs connectors/MCP vs context repo vs pasted.
- [target-user](../../options/DIMENSIONS.md#target-user-which-users-and-personas-we-serve-first-including-for-shared-agents): which personas to serve first (from the jobs map's persona work).
- [target-outcome](../../options/DIMENSIONS.md#target-outcome-which-outcome-or-value-we-target): time saved vs throughput vs quality vs outcomes.
- [pm-agent-evaluation](../../options/DIMENSIONS.md#pm-agent-evaluation-how-we-would-know-a-pm-agent-works): self-reported time vs throughput vs quality vs outcomes.

## Pattern classes

Added 2026-10-24 by teardowns-to-pattern-classes. This summary's examples are placed in the runtime pattern classes P1-P10 of the [taxonomy synthesis, B.2](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#b2-pattern-classes). Every placement is sourced and marked clear, partial or contested in [the mapping, section 2.6](../teardowns-to-pattern-classes/00-mapping.md).

- **Intercom, P1:** Claude Code for everyone, with plugins and hooks (clear).
- **Intercom, P6:** the Shrek reviewers (clear).
- **Intercom, partial:** the CI-watching agent and Buzz (P7), and the plugin marketplace (P10).
- **Evidence:** first-party.
- **Revised classes (2026-10-24):** Intercom's placements are unchanged. Fin and Operator are out of scope for P11 because they are products Intercom sells. See [the mapping, section 8](../../tasks/teardowns-to-pattern-classes/00-mapping.md#8-revised-classes-2026-10-24).
