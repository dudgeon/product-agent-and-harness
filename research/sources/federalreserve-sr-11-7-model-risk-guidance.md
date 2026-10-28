---
title: "Supervisory Guidance on Model Risk Management (SR 11-7, attachment)"
source_url: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
author: Board of Governors of the Federal Reserve System; Office of the Comptroller of the Currency
publisher: Federal Reserve
published: 2011-04-04
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [regulatory-drivers-of-process, process-governance-load, human-review-gates, gate-judge-separation, stale-records-mislead-agents, dependency-knowledge-carriers]
relevance: high
---

## Relevance to the project
SR 11-7 (issued jointly with the OCC as Bulletin 2011-12) is why any US bank feature that touches a quantitative model, including a vendor model or an AI component, picks up a model-risk dependency: validation before first use, scaled to risk, by people independent of the developers, recorded in a firm-wide model inventory. It defines the gate a product team must satisfy and the record a dependency agent would read: the inventory of models, their owners, inputs, uses and validation status. Its "effective challenge" principle is also a design constraint on any agent that prepares validation evidence: the challenger must be independent of the builder.

## Themes
- regulatory-drivers-of-process: "The range and rigor of validation activities conducted prior to first use of a model should be in line with the potential risk presented by use of the model. If significant deficiencies are noted ... use of the model should not be allowed or should be permitted only under very tight constraints" (Validation section, p. 10).
- gate-judge-separation: "effective challenge" is "critical analysis by objective, informed parties"; incentives are stronger "when there is greater separation of that challenge from the model development process" (p. 4).
- dependency-knowledge-carriers / stale-records-mislead-agents: banks "should maintain a comprehensive set of information for models implemented for use, under development for implementation, or recently retired"; a specific party should maintain "a firm-wide inventory of all models"; the inventory should list "the type and source of inputs used by a given model and underlying components" (Model Inventory, p. 20).
- process-governance-load: vendor products are in scope: "Banks are expected to validate their own use of vendor products" and should require vendors to provide developmental evidence (Validation of Vendor and Other Third-Party Products, p. 15).

## Key points
- Definition of a model: "a quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates" (p. 3). Broad enough to catch many product features.
- Three elements of a sound framework: robust development, implementation and use; a sound validation process; governance with policies, controls and roles (pp. 4-5).
- Validation framework has three core elements: evaluation of conceptual soundness, ongoing monitoring, outcomes analysis (p. 11).
- If validation cannot be done before use because of data paucity, "that fact should be documented and communicated in reports to users, senior management, and other relevant parties" (p. 10).
- Internal audit assesses the overall framework; accuracy and completeness of the model inventory is one of the things it checks (Governance, pp. 18-19).
- Banks should have contingency plans for when a vendor model is no longer available (p. 15).

## Notable quotes
- "Effective challenge depends on a combination of incentives, competence, and influence." (p. 4)

## Could not verify
- The federalreserve.gov srletters HTML page returned 404 at retrieval; the attachment PDF at the boarddocs path was read in full (text extracted locally). Page numbers are PDF page indices.
