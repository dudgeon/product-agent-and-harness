---
title: "Community Wisdom: Quarterly planning and AI, cash vs. equity comp, paying for interview exercises, AI-powered outbound, compliance startup opportunities, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-quarterly-planning
author: Lenny's Newsletter community (digest compiled by Kiyani)
publisher: Lenny's Newsletter
published: 2026-07-04
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [agent-ready-intent, org-context-grounding, compounding-context-repo, outcome-measurement-gap, human-review-gates, risk-review-as-classification, intent-factory-before-discovery, memory-architecture]
relevance: medium
---

## Relevance to the project
Two threads matter. One is a PM at a Series E company (1,500+ employees) building a spec-driven AI SDLC for the R&D org, where PMs, designers and engineers hand off through agents; replies converge on context governance (not prompts) as the hard part and on rework, not speed, as the KPI. That is close to the intent-shaping problem in a large org and gives concrete candidate measures for pm-agent-evaluation. The other asks whether AI has killed quarterly planning; the strongest answer is that planning moves "downstream of the evidence" while cross-team coordination and customer change-absorption keep it alive in large orgs. A compliance thread adds a regulated-setting view: the open problems are judgment-heavy decisions that a regulator or sponsor bank can reject, not evidence collection. All of it is community anecdote.

## Themes
- agent-ready-intent: the spec-driven SDLC thread (thread 6) lists what an agent-ready handoff needs: "Source-of-truth hierarchy, clean handoff packets, explicit decision records, acceptance criteria, verification gates", plus separation between the agent that plans, the one that executes, and the checker. Inspired by BMAD but adapted for org-level standardization with team-specific context.
- org-context-grounding: "the prompt is rarely the hard part. Context governance is." Agents fail when they can't tell "current vs. stale, canonical vs. just-discussed, decided vs. still-needs-a-human" (thread 6, a solo builder). The original poster confirms context engineering was "the first hurdle we've run into as well".
- compounding-context-repo / memory-architecture: the poster plans to try Google's "Open Knowledge Format" (OKF): a folder of Markdown files, one concept per file (table, API, metric, playbook, process), YAML front matter (type, title, description, tags, links), cross-linked into a navigable graph (thread 6). Another reply: keep personas, design guides and critical workflows "well documented and well governed".
- outcome-measurement-gap: proposed KPI is rework, not speed: "clarification loops, reopened tickets, spec/design mismatches, review burden, first-pass acceptance" (thread 6).
- intent-factory-before-discovery: when build cost drops to a day, "You stop forecasting what's worth building and start deciding what's worth keeping"; planning "moved downstream of the evidence instead of upstream of it" (thread 1, someone running an "agent-led studio"). Counterpoints in the same thread: large-org planning is mostly cross-group coordination, and enterprise customers ration how much change they will absorb.
- human-review-gates: in AI outbound, the one marketer reviews every email before sending and checks responses before the system updates the CRM: "Human oversight is still necessary at the key decision points" (thread 5).
- risk-review-as-classification: a compliance veteran (15+ years at large banks) says tools like Vanta have solved evidence collection for mapped frameworks; the burning problems are judgment calls (KYC/KYB decisioning, AML alert and SAR dispositioning, model governance under new "SR 26-2" guidance) "where the answer requires reasoning rather than evidence collection" and a regulator or counterparty can say no (thread 2).

## Key points
- Thread 1 (planning): a fractional designer reports a lead dev saying a team of 5 now does the work of 20; even when a PM drafts a prototype it still goes to design and dev for anything non-trivial. The quarterly cycle is described as a batching mechanism for expensive builds; what dies is "roadmap-as-forecast", not strategy.
- Thread 2 (compliance): a startup with no enterprise experience prompted Claude to write compliance documents that were "sometimes correct and often not", which lengthened enterprise due diligence; a contributor had to build packaged workstreams for procurement, CRO and CCO reviewers.
- Thread 5 (outbound): AI drafting helps a human scale but does not replace them; one contributor built a Claude research-and-lead workflow in Slack whose insights were used but whose outbound emails rarely were sent as-is.
- Thread 6 (spec-driven SDLC): the effort was engineering-led; leadership then asked for product, design and security representation. The PM owns PM and design agent handoff steps, milestones, KPIs and an org-wide adoption plan. Adoption advice: teams adopt when they trust the system to stay oriented: "what I used, what changed, what I think is true, and how to verify it" beats a demo.
- Other threads (cash vs equity, paid interview exercises) are off-topic and not filed.

## Notable quotes
- "the prompt is rarely the hard part. Context governance is." (thread 6)
- "The KPI I'd watch isn't speed. It's rework" (thread 6)
- "Planning didn't disappear, it just moved downstream of the evidence instead of upstream of it." (thread 1)

## Could not verify
- Read in full; only threads 1, 2, 5 and 6 filed. Contributors are community members; claims are personal experience. The most detailed thread-6 advice comes from someone who says they have not done it at 1,500-person scale.
- "Google's OKF" and "SR 26-2" are as named by contributors; not checked against primary sources here.
- The thread-6 linked article on agent-first development at scale is not named in the text.
