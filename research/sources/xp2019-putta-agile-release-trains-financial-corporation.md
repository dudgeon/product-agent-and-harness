---
title: "How Are Agile Release Trains Formed in Practice? A Case Study in a Large Financial Corporation"
source_url: https://doi.org/10.1007/978-3-030-19034-7_10
author: Abheeshta Putta, Maria Paasivaara, Casper Lassenius (Aalto University; IT University of Copenhagen; Simula)
publisher: Springer, XP 2019 proceedings (LNBIP 355, pp. 154-170); open-access reprint via Aalto ACRIS
published: 2019-01-01
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [dependency-types-and-practices, coordination-cost-and-waiting, dependency-knowledge-carriers, platform-onboarding-friction, process-governance-load]
relevance: high
---

## Relevance to the project
An independent, peer-reviewed case study of how a large financial corporation (pension and insurance; 1,300 staff, 300 in software development across 32 teams; named as PFA in the authors' 2024 follow-up) formed its agile release trains, which found that tightly coupled systems with "a significant amount of cross-system dependencies" made value streams impossible to separate, that the trains were sliced along old silos for political acceptance, and that every feature then had "lots of dependencies outside the trains" and between trains. It is the first-person regulated-firm account of dependency practice the research round had not found: the authors interviewed 27 people in 24 interviews and observed two PI planning events. Its sharpest finding for a dependency agent is that after SAFe the coordination of dependencies "was pushed down to the team level. Teams were good at identifying the dependencies, but they were not good at acting on them", and project managers outside the trains kept doing the coordination. That is the gap between discovery and resolution the agent is meant to close. CC BY 4.0.

## Themes
- dependency-types-and-practices: the case could not identify separable value streams "due to the presence of tightly coupled systems with a significant amount of cross-system dependencies", with the same specialists working on several systems; pension and insurance were put into one joint train (section 4.1, "Difficulties in Identifying and Separating Value Streams"). Trains were "almost vertically sliced" to retain silos and win directors' buy-in (4.1).
- coordination-cost-and-waiting: "every task or feature that was supposed to be delivered by a release train had lots of dependencies outside the trains"; operations and testing were separated into centres of excellence, "which created further delays and dependencies between the trains and CoEs"; "these dependencies between the trains and external units caused a lot of delays to the deliveries" (4.2, "External Dependencies"). Front-end and back-end sat in different trains and "most tasks required data from the back-end to change something in the front end", so finishing a task in one increment "was challenging" (4.2, "Inter-train Dependencies").
- dependency-knowledge-carriers: before SAFe "there were project managers to coordinate the dependencies"; after SAFe coordination was pushed to teams, who "were good at identifying the dependencies, but they were not good at acting on them"; project managers outside the trains kept coordinating; a project manager: "A lot of these coordination things has been done by a project manager, before it hits the train. It is a lot bigger challenge, when you have to do it on the fly" (4.2). Some interviewees asked for SAFe's portfolio and large-solution layers to handle cross-train coordination.
- process-governance-load: before agile the firm ran PRINCE2, was "siloed and hierarchical with a command and control leadership style", had about 30 projects running in parallel with the trains, and moved from quarterly to monthly releases (3.2).
- platform-onboarding-friction: operations, testing, integration and SAP were pulled out of the trains into six centres of excellence (Project and Program, DevOps, Lean and Agile, SAP, Integration and BPM, Test), which the trains then depended on (3.2, 4.2).

## Key points
- Case: one of the largest Danish corporations to adopt SAFe; 1,300 staff, about 300 in software development in 32 teams, two sites (Denmark and about 10-15% consultants in Poland). Four release trains at the time of study plus six centres of excellence; about 30 projects running alongside the trains (3.2).
- Method: 24 semi-structured interviews with 27 people (developers, product and project managers, product owners, CoE members, scrum masters, release train engineers, a requirements analyst, an SOA specialist), Feb-Apr 2018, 1-2 hours each; two PI planning events observed; open and axial coding in NVivo (3.3-3.4).
- ART formation (RQ1): a pilot train of experienced front-end teams; then workshops to identify stakeholders for the second train; team members chose teams by skills and interests; the last two trains were formed in Lego workshops. The organisation avoided a radical restructuring and accepted silo-based trains to gain political acceptance (4.1, 5.1).
- Challenges (RQ2): existing projects and project managers continued and created priority clashes and coordination overhead between trains; external dependencies on units outside the trains and on the CoEs; inter-train dependencies from the front-end/back-end split (4.2).
- Discussion: SAFe's own roadmap warns that shortcutting value-stream identification is "putting your foot on the brake at the same time you are trying to accelerate"; the authors find this borne out, while noting the compromise bought acceptance and business resources (5.1). "Managing dependencies between the four silo based release trains was a significant challenge, which created coordination overhead" (5.2). "SAFe is not a silver bullet"; organisations developing "multiple and tightly coupled systems" struggle to form value-stream-based trains (6).

## Notable quotes
- "Teams were good at identifying the dependencies, but they were not good at acting on them." (4.2)
- "If you have full-stack, then it is internal ... but when you have the silos, you have to talk across. And that is a challenge." (a project manager, 4.2)

## Could not verify
- Figure 1 (organisational structure after SAFe) and Table 1 were not legible in the text extraction; counts of teams per train come from the 2024 follow-up note.
