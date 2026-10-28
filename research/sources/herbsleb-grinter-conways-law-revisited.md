---
title: "Splitting the Organization and Integrating the Code: Conway's Law Revisited"
source_url: https://herbsleb.org/web-pubs/pdfs/herbsleb-splitting-1999.pdf
author: James D. Herbsleb and Rebecca E. Grinter (Bell Laboratories, Lucent Technologies)
publisher: Proceedings of ICSE 1999
published: 1999-05-01
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [dependency-knowledge-carriers, tacit-knowledge-capture, coordination-cost-and-waiting, stale-records-mislead-agents]
relevance: high
---

## Relevance to the project
A case study of a multi-site Lucent project in which integration was the hardest part, because informal communication broke down across sites. Its section "Knowing who to contact about what" is the clearest early description of the dependency-knowledge problem: developers could not find who owned a component at the other site, used names at the bottom of specification web pages and system architects as directories, and came to rely on people who had visited the other site as "liaisons". It also documents undocumented interface agreements discovered only at integration. Both are the problems a dependency agent's ownership and context layer would address.

## Themes
- dependency-knowledge-carriers: architects "were known to have a very broad knowledge of the system and who was doing what" and became the routing service; returning visitors became "contact people" or "liaisons" (section 4.2.2).
- tacit-knowledge-capture: an informal agreement that one component would validate data for another was unknown to testers, who filed bugs against it; "Much time was wasted with this and similar problems with undocumented interface refinements" (section 4.1).
- coordination-cost-and-waiting: questions to the other site often had to "wait at least until the next business day" (section 4.2).
- stale-records-mislead-agents: the integration plan assumed components would be ready on schedule; they were not (section 4.1.1).

## Key points
- Abstract: "Coordination problems were greatly exaggerated across sites, largely because of the breakdown of informal communication channels."
- Stable plans, processes and specifications helped, but the unpredictable parts of a project "require communication channels that can be invoked spontaneously".
- Differences in assumptions between the product and its substrate persisted because no one was using the real substrate; resolved by hosting a substrate developer on site, which also gave product developers contacts in other divisions.
- About half a dozen UK developers spent months at the German integration site; relationships and speed improved after face-to-face work.
