---
title: "In Search of Socio-Technical Congruence: A Large-Scale Longitudinal Study"
source_url: https://arxiv.org/abs/2105.08198
author: Wolfgang Mauerer, Mitchell Joblin, Damian A. Tamburri, Carlos Paradis, Rick Kazman, Sven Apel
publisher: arXiv / IEEE Transactions on Software Engineering
published: 2021-05-17
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [dependency-detection-automation, ownership-inference, vendor-claims-vs-independent-evidence]
relevance: medium
---
## Relevance to the project
The main check on socio-technical congruence (STC), the idea from Cataldo, Herbsleb and Carley (ESEM 2008) that you can derive who needs to talk to whom from technical dependencies, and that teams whose communication matches those "coordination requirements" resolve work faster. Across 25 large open-source projects, this longitudinal replication found its congruence measure "not related to project quality measures" (bugs and churn). For the dependency agent: inferring coordination needs from code is feasible, but evidence that closing the gap pays off is mixed.

## Themes
- dependency-detection-automation: STC computes coordination requirements from task assignments and file/logical dependencies; this study's motif-based variant (STMC) counts how often developers working on the same or related files need to communicate.
- ownership-inference: the method doubles as "who should be talking to whom" inference from code.
- vendor-claims-vs-independent-evidence: the original Cataldo et al. result (resolution time of modification requests "significantly reduced" when coordination matched needs; logical dependencies mattered more than call or data dependencies) did not replicate as a quality effect here; the authors suggest congruence's effect "lies elsewhere".

## Key points
- 25 projects, mixed-methods, modelled on earlier influential work; to appear in IEEE TSE.
- The Cataldo/Herbsleb TSE 2013 paper ("Coordination Breakdowns and Their Impact on Development Productivity and Software Failures") linked coordination gaps to more failures (search summary only).

## Could not verify
- Effect sizes; the original Cataldo et al. 2008 paper was not opened (abstract seen via search results only).
