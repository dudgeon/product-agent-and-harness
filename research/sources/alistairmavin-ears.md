---
title: "EARS: The Easy Approach to Requirements Syntax"
source_url: https://alistairmavin.com/ears/
author: Alistair Mavin
publisher: alistairmavin.com
published: unknown
retrieved: 2026-11-01
type: docs
evidence: first-party
filed_by: research-sdd-ready-intent
themes: [sdd-input-contracts, requirements-partitions, agent-ready-intent]
relevance: high
---

## Relevance to the project
EARS is the requirement notation Kiro's specs use, written up here by its lead author. It is the target form for the functional and conduct requirements the intent-shaping module hands to a spec-driven toolchain: five clause patterns, each with one system name and a "shall", that a coding agent can turn into tests and that Kiro turns into correctness properties. It also shows which of the project's requirements fit the notation (behaviour, states, unwanted cases) and which do not (process and evidence obligations, Q11 in 01).

## Themes
- sdd-input-contracts: the generic form "While <optional pre-condition>, when <optional trigger>, the <system name> shall <system response>"; ruleset of zero or many preconditions, zero or one trigger, one system name, one or many responses (section "Generic EARS syntax").
- requirements-partitions: the patterns are by behaviour type (ubiquitous, state, event, optional feature, unwanted), which lines up with 01's attribute axis (Q1, Q4, Q7) and not with the source axis.
- agent-ready-intent: claimed effects are fewer common natural-language requirement problems, little training, no specialist tool (opening section; author's claim).

## Key points
- Five patterns: Ubiquitous ("The <system> shall ..."); State driven ("While ..."); Event driven ("When ..."); Optional feature ("Where <feature is included> ..."); Unwanted behaviour ("If <trigger>, then the <system> shall ..."). Complex requirements combine keywords in fixed order.
- First published at the IEEE Requirements Engineering conference in 2009 (Mavin et al., Rolls-Royce); the page lists users including Airbus, Bosch, Honeywell, Intel, NASA, Rolls-Royce and Siemens (author's claim, not verified).
- Kiro uses only part of it in its docs' examples ("WHEN ... THE SYSTEM SHALL ...", see [Kiro specs](kiro-specs-docs.md)).

## Could not verify
- The 2009 paper itself was not read; the effect claims are the author's and were not checked against a study.
- Retrieved by HTML fetch and tag-stripping; pattern wording checked against the page text.
