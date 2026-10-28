---
title: "Coordination Breakdowns and Their Impact on Development Productivity and Software Failures"
source_url: https://herbsleb.org/web-pubs/pdfs/Cataldo-Coordination-2013.pdf
author: Marcelo Cataldo and James D. Herbsleb
publisher: IEEE Transactions on Software Engineering 39(3)
published: 2013-03-01
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [coordination-cost-and-waiting, dependency-knowledge-carriers, legible-org-for-agents]
relevance: medium
---

## Relevance to the project
Tests socio-technical congruence in two large commercial projects from two companies: where developers' actual coordination fell short of the coordination their technical dependencies required, software failures rose, and higher congruence went with faster resolution of modification requests. It supports the idea that dependency knowledge (who must talk to whom, derived from what depends on what) has value, and that gaps are measurable. Read alongside the 2021 open-source replication that found no quality effect (arxiv-mauerer-socio-technical-congruence).

## Themes
- coordination-cost-and-waiting: "higher levels of congruence are associated with improved development productivity" (Abstract), measured as resolution time of modification requests (section 7).
- dependency-knowledge-carriers: "the gaps between coordination requirements and the actual coordination activities carried out by the developers significantly increased software failures" (Abstract).
- legible-org-for-agents: coordination requirements can be computed from technical dependencies and compared with actual communication, a method an agent could run.

## Key points
- Two projects with different product and process maturity; result held in both mature and novel settings.
- Effect sizes on failure: in project A, moving structural congruence from its minimum (0.156) to maximum (0.421) observed value cut the estimated probability of a file's failure by 18.6%; in project B (0.009 to 0.891), by 7.6% (section 6 results).
- Builds on the "dynamic view of coordination": modularity alone does not remove work dependencies.

## Could not verify
- The productivity effect sizes were not extracted; only the failure-proneness figures above were read in the text.
