---
title: "SAFe transformation in a large financial corporation"
source_url: https://doi.org/10.1007/s10664-023-10420-w
author: Abheeshta Putta, Maria Paasivaara, Casper Lassenius
publisher: Empirical Software Engineering, vol. 29, article 27 (Springer); open access, CC BY 4.0
published: 2023-12-16
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [dependency-types-and-practices, coordination-cost-and-waiting, dependency-knowledge-carriers, process-governance-load, dependency-value-evidence]
relevance: high
---

## Relevance to the project
The full, peer-reviewed account of a SAFe transformation at PFA, a Danish pension and insurance company (1,300 staff, about 300 in software development in 32 teams), from 24 interviews with 27 people in 2018, which finds that the most significant challenge was aligning release trains with value streams: trains were built on the old silos for political and skills reasons, "which led to cross-release train dependencies and coordination overhead, inhibiting agility", and projects and project managers were kept, "which led to priority clashes and coordination overhead". It is the regulated-firm first-person account of dependency practice the research round had not found, and its central finding for a dependency agent is stated twice: SAFe gave the firm "better dependency management" in the sense that "teams could identify the dependencies during PIs. Unfortunately, they were not capable of managing them", so project managers kept coordinating between the four trains. Discovery without resolution is exactly the gap between the crawl and walk stages of the maturity model. The paper also supplies the only predictability figures in the library from a regulated firm (trains delivered 70% of what they promised; 95% of estimated story points completed), labelled by the authors as the organisation's own, unaudited.

## Themes
- dependency-types-and-practices: release trains "retained the old organizational structure instead of aligning them to value streams. This led to a situation in which there were significant dependencies between the trains" (4.4.1); the pension and insurance systems were tightly coupled with the same specialists on both, and the firm would not re-skill or add people; projects spanned several trains; third-party suppliers "could not work as a part of the release trains, which created a high overhead in coordination" and did not understand SAFe (4.4.1, "Dependencies with Third Parties"); project and train release cycles were unsynchronised (monthly vs per increment).
- coordination-cost-and-waiting: after the other trains formed, "each ART had to wait until other ARTs finished their tasks, similar to handovers in the waterfall model" (4.4.1, "Being Agile in Waterfall World"); the pilot train "had a lot of dependencies with other parts of the organization, which were not in a position to change their way of working"; prioritisation across trains was lacking because the portfolio level was not implemented, so project tasks "ended up having different priorities in different release trains"; interviewees asked for a common prioritisation forum.
- dependency-knowledge-carriers: "The teams could identify the dependencies between the release trains but were not capable of managing them. To manage these dependencies, the organization used the role of a project manager" (4.4.1); about 80% of project managers' work moved to teams, the rest were placed in a centre of excellence and many felt "left in the air" or left; communication now ran through product owners who "missed many details", and a project manager said "there is a lot of know-how going lost in all that communication".
- process-governance-load: before the transformation PRINCE2 delivery took six months to three years; the firm had 14 software development models; before SAFe "there were no clear discussions on these priorities"; a prioritisation council of all directors was the fix (4.3.1); SAFe events were felt to take more time than the work (4.4.2).
- dependency-value-evidence: benefits claimed as "better dependency management", shorter time to market (working code in production within a ten-week increment), predictability (70% of promised delivered; 95% of estimated story points completed), employee survey 9 of 10 for train members; the authors could not capture metrics ("most of the reported benefits were qualitative") and collected no before-and-after data on lead time or productivity (5.1).

## Key points
- Case: PFA, established 1917; four trains at the end of the study: DCE (50 people, 7 teams), DBI (40, 5), IP (120, 11), DM (80, 9); six centres of excellence; development in Denmark with Polish subcontractors (3.3).
- Method: 24 semi-structured interviews, 27 people, Feb-Apr 2018, with observation of PI planning; open and axial coding; a feedback session with 15 attendees agreed the findings and asked above all "how to map the value streams when having tightly coupled systems" (3.4-3.6).
- 17 reasons for adoption (shorter time to market, collaboration, a well-described framework, popularity in the financial sector); 13 benefits; 16 challenges (4.1-4.4, Tables 3, 5, 6).
- The three departures from SAFe's roadmap: no value streams identified; projects and project managers kept; basic agile training added (5, RQ2).
- Implications for practice: "Getting value streams right"; "Working with projects": combining projects with trains "can create dependencies and clashes with the delivery cycles"; "Role of project managers" (5.2).
- External validity: the authors hypothesise the findings transfer to "a large, departmental organized organization, with a traditional development process and tightly coupled legacy systems" (5.1).

## Notable quotes
- "Failing with this led to cross-release train dependencies and coordination overhead, inhibiting agility." (abstract)
- "Unfortunately, they were not capable of managing them." (5, RQ4, on the dependencies teams could identify)
- "There is a lot of know-how going lost in all that communication." (a project manager, 4.4.1)

## Could not verify
- Tables 1 to 6 and Figures 4 to 5 were not readable as text; counts come from the body. The predictability figures are the organisation's own reports to the researchers, not measured by them.
