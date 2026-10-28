---
title: "Explain the risk of a change request by using Now Assist for IT Service Management (ITSM)"
source_url: https://www.servicenow.com/docs/r/QykF2iRSIs6VXztArCSo3w/qCO_4jfSU1JwbgjB0uMsMw
author: ServiceNow
publisher: ServiceNow product documentation (Australia release)
published: 2026-03-12
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [risk-review-as-classification, human-review-gates, dependency-detection-automation]
relevance: medium
---
## Relevance to the project
ServiceNow's generative layer over change risk does not decide risk; it explains a risk rating already calculated by the rules or ML engine, citing similar change requests, the incidents they caused, the risk condition met and the top five normalised risk-assessment values. For a dependency agent routing asks into change and governance processes, this is the pattern regulated firms are already accepting: model explains, existing calculator scores, a human with the itil role reads it.

## Themes
- risk-review-as-classification: inputs are change fields (short description, implementation plan, assignment group, risk, backout plan, model type) plus similar changes and their incidents, the risk condition met, and the risk assessment ("top five normalized risk values").
- human-review-gates: available only to itil users on changes assigned to them; output can be elaborated, shortened, copied, rated; no formal approval step is described.
- dependency-detection-automation: "similar change requests and the incidents they caused" is a historical change-to-incident link the explanation surfaces.

## Key points
- The icon is unavailable until risk has been calculated; Core UI and Service Operations Workspace only. The page mostly calls the assistant "ServiceNow Otto".
- No accuracy statements.
