# The value: what doing dependency management well is worth, and what doing it badly costs

Date: 2026-10-28. Part of the dependency-agent research (see [00-summary.md](00-summary.md)). This document sets out the evidence that good dependency management and platform onboarding pay, the evidence on what the alternative costs, and an honest account of how thin the evidence is where it is thin. Every figure comes from a source note in `../../research/sources/`, with its evidence label: **independent** (peer-reviewed, an auditor, or a researcher with no stake), **first-party** (an organisation about its own results), **vendor claim** (a vendor or consultancy about its product or a customer), or **anecdote**. Reasoning beyond the evidence is marked.

## 1. The short version

- **The cost of bad coordination is well evidenced and independent.** Each extra party adds calendar time; large programmes overrun with fat tails; auditors name unrecorded interdependencies and late-arriving components as causes; engineers measurably spend their time chasing status and finding information.
- **The payoff of specific fixes is plausible but rests on first-party and vendor numbers.** Every figure for onboarding time, developer-portal return, catalogue value and flow-efficiency gains comes from the organisation or vendor that built the thing, usually with no control group.
- **The independent platform evidence cuts both ways.** Platforms raise reported productivity and cut throughput and stability in the same survey, and the feature most associated with gains is developer independence from the platform team.
- **Priority churn is a bigger named cause of failure than dependencies.** Two independent sources say so. A dependency agent that only tracks dependencies, without surfacing priority conflicts between teams, misses the larger cause.

A funding case should lead with the cost side and present benefit figures as labelled illustrations. That is this research's recommendation from the evidence below.

## 2. Where the time goes: waiting at the junctions

**Each extra party adds calendar time.** The best-measured anchor is Herbsleb and Mockus at Lucent: work items spanning sites took about 2.5 times as long as single-site items, and the explanation was the number of people involved, not distance as such ([Herbsleb and Mockus](../../research/sources/herbsleb-mockus-speed-communication-distributed-development.md), independent). The boundary they studied was geographic; the mechanism transfers to organisational boundaries, and the multiplier may not. Coordination gaps relative to technical dependencies raised failure-proneness by 18.6% and 7.6% in two commercial projects ([Cataldo and Herbsleb](../../research/sources/cataldo-herbsleb-coordination-breakdowns.md), independent), although a 25-project open-source replication found no quality effect ([Mauerer et al.](../../research/sources/arxiv-mauerer-socio-technical-congruence.md), independent).

**The chasing job is measured once.** In a survey of 775 Microsoft engineers: 49% frequently chase the teams they depend on for status; only 34% get status without asking; 67% see work they depend on change without being told; 60% say commitments are misaligned ([Microsoft Research](../../research/sources/microsoft-research-coordination-large-scale-development.md), independent, 2009, 31% response rate). This is the closest description in the library of the job a dependency agent would take over.

**Finding information is the top waste.** 53% of professional developers say waiting on answers disrupts their workflow, 45% say knowledge silos block ideas, and most spend over half an hour a day searching ([Stack Overflow 2024](../../research/sources/stackoverflow-dev-survey-2024-professional-developers.md), independent, self-selected, about 28,700 respondents). Those using internal knowledge sources were 1.73 times more likely to be productive ([DORA 2019](../../research/sources/dora-state-of-devops-2019.md), independent, correlational). Vendor surveys point the same way with larger numbers: half of developers lose ten or more hours a week to organisational inefficiency and "finding information about services, docs and APIs" tops the friction list ([Atlassian 2025](../../research/sources/atlassian-state-of-devex-2025.md), vendor survey, 3,500 developers); 78% wait a day or more for platform help ([Port 2025](../../research/sources/port-state-of-internal-developer-portals-2025.md), vendor survey).

**Flow efficiency.** The most specific case is a consultancy's account of Maersk Line: one feature needed 82 hours of development and test inside a 46-week journey, with over 38 weeks of waiting, 29 of them before work started; the delay was priced at about $210,000 a week ([Black Swan Farming](../../research/sources/blackswanfarming-maersk-cost-of-delay.md), vendor claim). Planview's data from 3,600 value streams says completed code "commonly idles for three or more months before it's released" and bottlenecks form "in the junctions where work from multiple contributors converges"; 87% of respondents say dependencies or shared-service handoffs slow them ([Planview 2023](../../research/sources/planview-project-to-product-state-of-industry-2023.md), vendor claim). No independent enterprise flow-efficiency benchmark was found.

**The "each dependency halves your odds" figure is a teaching model.** It comes from Troy Magennis's 2015 conference slides: one in two to the power of n, assuming each dependency is a coin flip ([Magennis](../../research/sources/magennis-entangled-team-dependencies.md), anecdote). The one data-based test found says the drop is real but shallower: 50% to 80% on time at three dependencies, against the model's 12.5% ([Quantify](../../research/sources/quantify-why-dependencies-kill-deadlines.md), vendor claim). Use the direction, not the numbers.

## 3. Governance at speed: the one place regulated firms have measured

The clearest independent finding is about change approval. Respondents whose changes needed external approval were 2.6 times more likely to be low performers, with no evidence that formal approval lowered change failure; a clearly understood change process made respondents 1.8 times more likely to be elite ([DORA 2019](../../research/sources/dora-state-of-devops-2019.md), independent, about 1,000 respondents). DORA found no industry effect, so regulated firms can be elite; it found enterprises over 5,000 staff performed worse, attributed to heavyweight process and tightly coupled architecture. The UK regulator's own review of over a million changes found that smaller, more frequent releases succeeded more often and that boards approved over 90% of major changes ([FCA](../../research/sources/fca-implementing-technology-change.md), regulator).

First-party accounts from banks and insurers point the same way and carry no method:

| Organisation | Claim | Label | Source |
|---|---|---|---|
| Commonwealth Bank | Control attributes assured went from about 2,500 a year to more than 12,000 a month; changes to production doubled; incident resolution halved | first-party via press | [CBA](../../research/sources/itnews-cba-production-more-often-fewer-incidents.md) |
| National Australia Bank | "No form to fill in, there's no change board" on controlled paths; about 5,000 changes across 120 applications logged in a month | first-party via press | [NAB](../../research/sources/itnews-nab-cast-cloud-controls.md) |
| Nationwide (US insurer) | Share of work needing a request to another team fell from 100% to 0% after self-service provisioning | first-party, conference slides | [Nationwide at DOES16](../../research/sources/itrevolution-nationwide-does16-accelerated-delivery.md) |
| ING | Releases moved to every two or three weeks; each tribe's quarterly review must name the other tribes it depends on | first-party, consultancy interview | [McKinsey and ING](../../research/sources/mckinsey-ing-agile-transformation.md) |
| JPMorgan Chase | A policy engine "abstracts controls" across regulatory environments; audits save "days and weeks"; "two-fold" stability | first-party, sponsored | [MIT Tech Review](../../research/sources/mit-tr-jpmorgan-world-class-engineering-platform.md), [JPMC](../../research/sources/jpmorganchase-driving-enterprise-software-delivery.md) |

A large US bank reported twenty times more releases after cutting manual change approvals with no rise in incidents, in a vendor case study; that source is excluded from this project's public material and is mentioned here only as a direction. None of these organisations publishes an onboarding lead time.

## 4. Platforms and portals: the independent picture is mixed

**DORA 2024** (nearly 3,000 respondents; 15.7% financial services, 4.6% healthcare and pharma, 3.9% government, 2.4% insurance) found that platform users reported 8% higher individual productivity, 10% higher team performance and 6% higher organisational performance, but 8% lower throughput and 14% lower change stability. DORA's hypothesis is that platforms add handoffs, with a J-curve over time. The sub-finding that matters most for onboarding: being able to work "without relying on an enabling team" gave a 5% productivity gain, and mandating exclusive platform use went with 6% lower throughput ([DORA 2024](../../research/sources/dora-accelerate-state-of-devops-2024.md), independent; [TechTarget's reading](../../research/sources/techtarget-pariseau-dora-2024-platform-engineering-caveats.md)). That is the closest independent support for self-service, agent-compatible onboarding, and it comes with a warning.

**The academic base is thin.** A 2026 multivocal review of 88 sources found only two top-tier papers with platform engineering as their primary topic, no longitudinal or quasi-experimental studies, and no peer-reviewed evidence for scorecards ([Anjum et al.](../../research/sources/frontiers-anjum-platform-engineering-mlr.md), independent).

**Portal and catalogue benefits are first-party or vendor:**

| Claim | What was measured | Label | Source |
|---|---|---|---|
| Time to a new engineer's tenth pull request fell from over 60 days to 20 | Internal, no method | first-party | [Spotify](../../research/sources/spotify-engineering-backstage-made-developers-more-effective.md) |
| Frequent portal users 2.3 times more active on GitHub, 17% shorter cycle time, twice the deploys, 5% better retention | Matched pre-post, no control group, which Spotify says itself | first-party | [Spotify](../../research/sources/spotify-backstage-measuring-backstage-roi.md) |
| A US insurer's portal, integrated with its CMDB: onboarding 40% faster, 35% more deploys | None stated | vendor claim | [Infosys at CNCF](../../research/sources/cncf-infosys-insurance-backstage.md) |
| Incidents linked to a catalogued service resolved 36% faster | 50,000 incidents on one platform, association | vendor claim | [FireHydrant](../../research/sources/firehydrant-two-ways-resolve-incidents-faster.md) |
| 93% of top performers use a platform team's platform | 1,053 teams, self-report | vendor claim | [Humanitec](../../research/sources/humanitec-devops-benchmarking-2023.md) |
| 68% report faster velocity from platform engineering | Sample not stated; a vendor sponsored | vendor claim | [Puppet 2023](../../research/sources/perforce-puppet-state-of-devops-2023-platform-engineering.md) |

The only figure on the value of accurate records (FireHydrant's) is an association on one vendor's data. No study measured what stale ownership or CMDB data costs, and none measured "time to find the owner".

## 5. The cost of the alternative

**Overruns are fat-tailed.** Across 1,471 IT projects the average cost overrun was 27%, but one in six was a "black swan" averaging about 200% cost overrun and almost 70% schedule overrun ([Flyvbjerg and Budzier](../../research/sources/flyvbjerg-budzier-it-project-riskier.md), independent; 92% public agencies). McKinsey and Oxford's 5,400-project study put large projects 45% over budget with 56% less value than predicted ([McKinsey](../../research/sources/mckinsey-delivering-large-scale-it-projects.md), consultancy).

**Late-discovered dependencies are named causes.** The same McKinsey study describes a bank whose finance department was engaged months before go-live, costing three months and $8 million. HealthCare.gov never completed end-to-end testing "because the component pieces arrived too late" ([HHS Inspector General](../../research/sources/hhs-oig-healthcare-gov-case-study.md), independent). The UK National Audit Office says departments "do not have a good understanding of their IT estate and its interdependencies" and lists managing interdependencies and integration with legacy among the features of programmes that missed their dates, with billion-pound cost increases ([NAO 2021](../../research/sources/nao-challenges-implementing-digital-change.md), independent); its review framework ties Crossrail's late cost surprise to a plan that did not reflect interdependencies ([NAO framework](../../research/sources/nao-framework-to-review-programmes.md), independent). The FCA's most consistent change-failure factor was dependence on other projects ([FCA](../../research/sources/fca-implementing-technology-change.md), regulator). Charette's classic list of why software fails includes integration of "systems of systems" and poor communication ([Charette](../../research/sources/ieee-spectrum-charette-why-software-fails.md), independent).

**Regulatory sanction.** Swedbank's SEK 850 million fine followed a change that bypassed the board, the risk assessment and the supplier ([Finansinspektionen](../../research/sources/fi-swedbank-change-management-sanction.md), regulator). The cost of a skipped gate is now a number.

**Two cautions.** Standish CHAOS "success" rates measure forecasting bias, not value, and should not be quoted alone ([Eveleens and Verhoef](../../research/sources/ieee-software-eveleens-verhoef-chaos-figures.md), independent). And both PMI's survey ([PMI 2018](../../research/sources/pmi-pulse-of-the-profession-2018.md), vendor, individual cause percentages unconfirmed) and DORA 2024 rank shifting priorities above dependencies as a cause of failure; DORA finds the effect of unstable priorities "highly resistant to mitigation" ([DORA 2024](../../research/sources/dora-accelerate-state-of-devops-2024.md)). A platform's priority churn is what a consumer's request waits behind.

## 6. How thin is it

| Claim | Strength | Basis |
|---|---|---|
| Coordination across people and boundaries adds calendar time and defects | Strong | Herbsleb and Mockus; Cataldo and Herbsleb (independent) |
| Large programmes overrun with fat tails, and interdependencies, legacy integration and late components are named causes | Strong | Flyvbjerg and Budzier; NAO; HHS OIG; FCA (independent and regulator) |
| Heavyweight external change approval goes with worse delivery and no better stability | Strong, correlational | DORA 2019 (independent, long-running); FCA |
| Engineers spend real time chasing status and finding information | Strong in direction | Microsoft Research; Stack Overflow; vendor surveys agree |
| Platforms raise reported productivity but can cut throughput and stability; developer independence is the feature most associated with gains | Moderate | DORA 2024 (independent, correlational, one year) |
| Portals, catalogues and self-service onboarding cut onboarding time and improve delivery | Weak | Spotify, an insurer, FireHydrant, Nationwide (first-party or vendor, no controls) |
| Good records cut incident and onboarding time | Weak | One vendor association |
| Dependency management practice improves outcomes | Absent | No controlled or longitudinal study found |
| A team-to-platform onboarding lead time in a regulated organisation | Absent | Nobody publishes one |

## 7. What this means for a funding case

Three points follow (this research's reasoning):

1. **Lead with the cost of the status quo**, which is independently evidenced: waiting at junctions, chasing, late discovery, fat-tailed overruns, and sanction for a bypassed gate.
2. **Treat benefit figures as illustrations**, labelled with their source, and expect to generate your own: the first thing a dependency agent can give an organisation is the measurement nobody has, which is the intake-to-production time per platform and the share of elapsed time spent waiting on which party. [05-maturity-model.md](05-maturity-model.md) builds on that.
3. **Measure priority conflicts as well as dependencies.** The independent evidence says unstable priorities are the larger cause; a dependency agent that reports "waiting on the rating platform, whose roadmap moved" is reporting the cause the evidence points to.

## What could not be established

Not read: Standish CHAOS reports, Reinertsen's and Kersten's books, Gartner's platform-engineering predictions, the DX Core 4 papers, the full Puppet PDFs. Unconfirmed: PMI 2018 cause percentages, Planview's sample size, the 2024 Atlassian and DX sample. Not found: named UK bank or healthcare provider portal results with method; later independent assessments of ING; any measured team-to-platform onboarding time; any study of the cost of stale ownership data.
