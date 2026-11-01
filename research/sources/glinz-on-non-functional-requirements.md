---
title: "On Non-Functional Requirements"
source_url: https://files.ifi.uzh.ch/rerg/amadeus/publications/papers/RE07_Glinz.pdf
author: Martin Glinz (University of Zurich)
publisher: 15th IEEE International Requirements Engineering Conference (RE 2007)
published: 2007-10-01
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: define-shaping-and-dependency-agents
themes: [requirements-partitions, standard-form-spectrum]
relevance: high
---

## Relevance to the project
The clearest statement in the requirements-engineering literature of why a requirements taxonomy by quality attribute leaks. Glinz surveys the definitions of "non-functional requirement" and finds three problems: definition (the same words mean different things), classification (the same requirement can be stated as a function, a quality or a constraint, so the class depends on how it is written), and representation (how a requirement is written decides how it can be verified, not what kind it is). His remedy is a faceted classification: kind, representation, satisfaction and role as separate facets, with project and process requirements split off at the root. For the taxonomy work this is direct evidence that a single-axis partition will have items landing in two classes, and that a hybrid (source × attribute, or kind × representation) is the standard answer in the field.

## Themes
- requirements-partitions: "there is still no consensus in the requirements engineering community what non-functional requirements are" (abstract); the classification problem is that a requirement's kind depends on representation, e.g. the same security need can be written as a function, a quality or a constraint (section 3.2 to 3.3); the proposed partition is functional requirements, performance requirements, specific quality requirements and constraints, with "attribute" covering the middle two (section 4.2, definitions).
- standard-form-spectrum: Table 2, "Representation determines verification": operational representations are verified by review, test or formal verification; quantitative by measurement; qualitative by stakeholder judgement, prototypes or derived metrics; declarative by review (section 4.1).

## Key points
- Section 2: functional requirements are defined consistently (what the system must do); non-functional requirements are defined inconsistently as properties, attributes, qualities, constraints or performance.
- Section 3.1 definition problems: "attribute" and "constraint" each carry a broad and a narrow meaning across the standard texts (IEEE 830, Wiegers, Davis, Antón).
- Section 3.2 classification problems: existing schemes mix the concepts of kind, representation and satisfaction (hard versus soft).
- Section 4.1: a faceted classification separating kind, representation, satisfaction and role; the author reports that dropping the terms "functional" and "non-functional" altogether "is too radical" in practice.
- Section 4.2: a concern-based taxonomy; project and process requirements "should be distinguished at the root level and not in a sub-category such as non-functional requirements". The figure's constraint sub-kinds include physical, legal, cultural, environmental, design and implementation, and interface.
