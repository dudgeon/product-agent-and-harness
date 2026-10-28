---
title: "The State of DevOps in Banking: Report from DOES London 2018"
source_url: https://www.infoq.com/articles/state-devops-banking/
author: Helen Beal (reviewed by Daniel Bryant)
publisher: InfoQ
published: 2018-08-23
retrieved: 2026-10-28
type: article
evidence: independent
filed_by: research-dependency-agent
themes: [coordination-cost-and-waiting, process-governance-load, regulatory-drivers-of-process, dependency-knowledge-carriers, dependency-types-and-practices]
relevance: medium
---

## Relevance to the project
A journalist's report of the bank talks at the 2018 DevOps Enterprise Summit in London (Standard Chartered, ABN AMRO, KeyBank, Barclays, RBS, Nomura, Lloyds Banking Group, UBS and one large US bank), which reports inter-team and system dependencies, manual change control and regulation as the constraints banks named on their own delivery. It is a citable secondary source for first-person bank accounts whose videos sit behind a login, and it supplies specific figures: a 35-step manual change process, thirteen teams involved in one incident, about 60 regulator relationships and 250 security controls to map per environment at one bank, and a year to get a line of code to production at another. For the dependency agent it adds the banks' own prescriptions: break dependencies rather than manage them, move the PMO to "dependency and release management", and raise governance constraints early in the work tracker. The talks are first-party; the report is the journalist's, so it is labelled independent.

## Themes
- coordination-cost-and-waiting: Standard Chartered (Shaun Norris): no teams had APIs, so coordination ran on email and meetings; "We are seeing Conway's Law in action; we can see thirteen teams involved in an incident"; "Very few people have the full end-to-end view on how things work". Barclays' release path still had waits for monthly integration testing, quarterly user-acceptance testing and quarterly release scheduling (Jonathan Smart, paraphrased). Lloyds previously took 365 days to get a line of code into production.
- process-governance-load: Standard Chartered's change process "has thirty-five steps; it's manual, in Remedy, and prone to delays", with outcomes depending on relationships; "Our processes have been optimised for compliance, not speed". KeyBank would need to retrain its PMO to fit continuous integration into waterfall governance. Nomura replaced a 35-page business case with a one-page lean one to get budget.
- regulatory-drivers-of-process: segregation of duties means development teams cannot deploy to production, so Barclays embedded an operations representative in teams; Standard Chartered has regulators in every country, about 60 relationships to manage and roughly 250 security controls to map for each new environment, leading to two releases a year; regulators pushed it toward relationships with all three major cloud providers to reduce operating risk; outsourcing created SLA, contract, budgeting, timezone and skills challenges.
- dependency-knowledge-carriers: Barclays' PMO shifted to "more advisory and consultative with a focus on dependency and release management" (Morag McCall); its "Lean Control" initiative (Nick Funnell) used a control team to avoid "governance theatre" and raised constraints early in Jira.
- dependency-types-and-practices: Barclays' Smart recommends organisations "aim to break dependencies rather than manage them" (paraphrased), with high cohesion and low coupling; ABN AMRO, Lloyds and others cited microservices, APIs, SOA and InnerSource as ways to loosen coupling; cross-functional teams with testers, operations, security and business members reduce external dependencies.

## Key points
- Figures: Standard Chartered about two-thirds agile, 35 change steps, 13 teams in one incident, about 60 regulatory relationships, 250 security controls, two releases a year; ABN AMRO three to four years for its transformation and much less project-management overhead after it; Barclays 48 million customers, 80,000 employees, 20,000 in technology, over 2,000 community members, business outcomes every three months, 18 to 24 months in the "fuzzy front end"; RBS one team cut a 14-week deployment cycle to hours; KeyBank about 10% of work agile; Lloyds 365 days for a line of code previously.
- A separate passage attributes to Standard Bank (not Standard Chartered) over 200 teams on a DevOps toolchain, 6,000 builds a week and a 90% reduction in turnaround time; the article does not say whether these are the same organisation, and they are not.
- Legacy: a private cloud as a stopgap at Standard Chartered; a failed earlier "bimodal" attempt there; a tooling change replaced a manual requirement that managers record team work for auditors.
- One large US bank's talk (business staff struggling to get commitment from tech leads) is in the article; it is not named in this note because of the project's public-material rules.

## Notable quotes
- "Our change process has thirty-five steps; it's manual, in Remedy, and prone to delays." (Shaun Norris, Standard Chartered)
- "Our processes have been optimised for compliance, not speed." (Shaun Norris, Standard Chartered)
- "The PMOs are more advisory and consultative with a focus on dependency and release management." (Morag McCall, Barclays)

## Could not verify
- The talk videos are behind the IT Revolution library login; figures are as the journalist reported them.
