---
title: "Accelerate: State of DevOps 2019"
source_url: https://dora.dev/publications/pdf/state-of-devops-2019.pdf
author: Nicole Forsgren, Dustin Smith, Jez Humble, Jessie Frazelle (DORA)
publisher: DORA / Google Cloud
published: 2019-08-21
retrieved: 2026-10-28
type: report
evidence: independent
filed_by: research-dependency-agent
themes: [process-governance-load, coordination-cost-and-waiting, risk-sloped-review, human-review-gates, governance-as-code, regulatory-drivers-of-process]
relevance: high
---

## Relevance to the project
DORA's 2019 survey found that formal external change approval (a change advisory board or senior manager) makes respondents 2.6 times more likely to be low performers, with no evidence that it lowers change failure, while a clearly understood approval process makes them 1.8 times more likely to be elite. For a dependency agent this is the most-cited quantitative case that governance gates cost speed without buying stability, and, just as important, that simply making the existing process legible to teams pays on its own. The report also names regulatory control and cross-team coordination as the two sources of change-management complexity in financial services, healthcare and government. Survey-based and correlational (evidence label: independent research programme run by Google Cloud).

## Themes
- process-governance-load: "formal change management processes that require the approval of an external body such as a change advisory board (CAB) or a senior manager for significant changes have a negative impact on software delivery performance"; respondents were "2.6 times more likely to be low performers" (p. 50, "Heavyweight change process").
- coordination-cost-and-waiting: complexity in change management comes from "the need for coordination between teams, and requirements of regulatory control, particularly in financial services, healthcare, and government" (p. 48); "In our work with large organizations, change management is consistently one of the biggest constraints" (p. 52).
- legible process as a lever (process-artifacts-as-coordination): "Survey respondents with a clear change process were 1.8 times more likely to be in elite performers"; clarity means teams "know the steps it takes to go from 'submitted' to 'accepted' every time for all the types of changes they typically make" (p. 52, "Clear change process").
- risk-sloped-review / human-review-gates: recommends moving away from external approval and "shift left" to peer review plus automation; the CAB's new role is "process architect and information beacon", coordinating and weighing business trade-offs (p. 51, "What happens to the CAB in the continuous delivery paradigm?").
- regulatory-drivers-of-process: segregation of duties is "often required by regulatory frameworks" (footnote cites PCI DSS and the NIST RMF); can be met by peer review recorded in a change management system with authenticated approval events (pp. 48-49, "Implementing segregation of duties").
- governance-as-code: version control as the source of truth makes "the review and submit process highly auditable" (p. 49).

## Key points
- No evidence that a more formal approval process is associated with lower change fail rates; the hypothesis that more approvals produce larger, less frequent, riskier batches was "supported in the data" (pp. 50-51).
- "Organizations often respond to problems with software releases by introducing additional process and more heavyweight approvals. Analysis suggests this approach will make things worse." (p. 51)
- Enterprises (>5,000 employees) were lower performers than smaller organisations, attributed to "heavyweight process and controls as well as tightly coupled architectures" (p. 18-19, "Industry velocity").
- No evidence that industry affected performance (except retail), so "highly regulated industries such as financial services and government, can achieve high levels of performance" (p. 18).
- The CAB finding extends the 2014 State of DevOps report's finding that heavyweight approvals did not reduce change failure (footnotes 22-23).
- Added by strand C: sample "almost 1,000" respondents in 2019 (over 31,000 across six years); "Our highest performers are twice as likely to meet or exceed their organizational performance goals (including profitability, productivity, and customer satisfaction)" (Executive summary). Elite versus low performers: 208 times more frequent deploys, 106 times faster lead time from commit to deploy, 2,604 times faster recovery, 7 times lower change failure rate (p. 21).
- Loosely coupled architecture is defined as teams that "can independently test, deploy, and change their systems on demand without depending on other teams for additional support, services, resources, or approvals, and with less back-and-forth communication"; its positive impact on continuous delivery was "revalidated" (p. 42, organisation-level capabilities).
- Internal search: those using internal knowledge sources (company knowledge bases, code repositories, ticketing systems, docs) "were 1.73 times more likely to be productive" (p. 52-53, Internal and external search).

## Notable quotes
- "There's a right way to handle the change approval process, and it leads to improvements in speed and stability and reductions in burnout." (Executive summary, p. 3)

## Could not verify
- Page numbers are the report's printed page numbers as extracted from the PDF; PDF page index differs by about one.
