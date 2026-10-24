---
title: "A2ABreak: Systematic Security Analysis of the A2A Protocol"
source_url: https://arxiv.org/abs/2609.10871
author: Alireza Lotfi, Mirza Masfiqur Rahman, Imtiaz Karim, Elisa Bertino
publisher: arXiv (cs.CR, cs.SE)
published: 2026-09-09
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-protocol-security, identity-delegation]
relevance: medium
---

## Relevance to the project
The first systematic, specification-level security analysis of A2A found. It reports 11 new vulnerabilities exploitable by a fully spec-compliant adversary, including "credential harvesting via multi-hop identity loss in delegation chains", which matches Eon's production report that the asker's identity is lost across hops ([Eon](aaif-eon-a2a-into-production.md)). Only the abstract page was read.

## Themes
- `agent-protocol-security` (proposed): Builds a finite-state model of the spec (37 states, 76 transitions from 929 formalised statements) and reasons adversarially; named examples: cross-client context injection via unprotected context identifiers; credential harvesting via multi-hop identity loss in delegation; exfiltration through rogue agents advertising unattested capability claims.
- `identity-delegation`: Identity loss across delegation hops is a spec-level issue, not just an implementation one.

## Key points
- v1 2026-09-09, revised v2 2026-10-13. Tool precision 73.3%, F1 84.6% against expert review; a zero-shot LLM baseline found nothing confirmed.
- An HN commenter (item 49669375, 2026-09-12) argued several of the findings (skills, signature, identity) cannot be fixed by the protocol alone and fall to agent owners or third parties.

## Could not verify
- Full paper not read: which spec version (likely v1.0 but not stated in the abstract), full vulnerability list, disclosure status, mitigations. Affiliations not shown on the abstract page.
