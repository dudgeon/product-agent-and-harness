---
title: "How JPMorgan Chase built a data mesh architecture to drive significant value to enhance their enterprise data platform"
source_url: https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform
author: Anu Jain, Graham Person, Paul Conroy (JPMorgan Chase); Nivas Shankar (AWS)
publisher: AWS Big Data Blog
published: 2021-05-05
retrieved: 2026-10-28
type: article
evidence: first-party
filed_by: research-dependency-agent
themes: [platform-onboarding-friction, process-governance-load, legible-org-for-agents, dependency-knowledge-carriers]
relevance: medium
---

## Relevance to the project
A large regulated bank describing how a product team gets data from a data platform: find it in an enterprise catalogue, request it, and the owning domain decides; data is shared in place, not copied, with column, row and value-level restrictions and tokenisation of sensitive values; a separate mesh catalogue records which lakes share with which consumers. The framing is the regulated-org paradox: data is worth more the more it is shared, and sharing raises risk. For a dependency agent, the catalogue plus the record of who consumes what is the kind of legible dependency data an agent could read; the access decision stays with the data owner.

## Themes
- process-governance-load: the stated goal is to make data easy to share while keeping appropriate control in a regulated industry (introduction).
- platform-onboarding-friction: consumers find data in a catalogue and request it; the owning domain decides, which the post says "minimizes the consumption team's wait time" (no timings given).
- dependency-knowledge-carriers: before the mesh, data exchanges were system-to-system or via queues with no central, automated record of flows, so owners could not see where their data went.
- legible-org-for-agents: the mesh catalogue "does have visibility of which lakes are sharing data with which data consumers".

## Key points
- Each data product lives in its own lake; physical separation between lakes.
- "There are no copies of the untokenized data outside of the lake to create a control gap."
- AWS services (Glue Data Catalog, Lake Formation, Athena) are offered as options ("one could use"), not confirmed as the JPMC stack.
- Claimed results are qualitative: lower storage cost, fewer discrepancies between producing and consuming systems, one point of visibility into data flows.

## Could not verify
- Any lead times or approval steps in practice; the post gives none.
