---
title: "Accelerating your DevOps change process (DevOps Change Velocity)"
source_url: https://www.servicenow.com/docs/r/QykF2iRSIs6VXztArCSo3w/1IOGCXHTnX02RprvPaB2wg
author: ServiceNow
publisher: ServiceNow product documentation
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [governance-as-code, agent-originated-requests, risk-sloped-review, decision-rationale-records]
relevance: high
---

## Relevance to the project
The most widely deployed pattern of a machine (a CI pipeline) submitting a change request to a regulated change-management process and getting it approved by policy: the pipeline opens the change, a change approval policy evaluates collected evidence, and the change is auto-approved, auto-rejected or routed to people. This is the template a dependency agent would follow: the requester is non-human, the checks are codified, humans keep the policy and the exceptions, and the record is kept.

## Themes
- governance-as-code: "Change requests can be approved automatically by configuring conditions in a change approval policy"; inputs include work items, commits, code coverage, code security, risk scores and test results.
- agent-originated-requests: change control on a pipeline job opens a change request in Assess state, pausing the job; "change receipts" record a change without pausing.
- risk-sloped-review: conditions met = auto-approve; not met = auto-reject; conditions requiring a person notify approvers, then the pipeline resumes at Implement (community guides show low risk to automation, moderate/high to CAB; search summaries).
- decision-rationale-records: the change links commits, work items, artifact versions, test, quality and security summaries; up to 5 KB of task execution log per step goes to work notes.
- governance-as-code (default posture): the manual approval flow is enabled by default and the automated flows apply only to automatically created changes (or with receipts disabled); the "DevOps risk" condition using a committer risk score is inactive by default; docs recommend only one DevOps flow active at a time (DE-language docs page t~YvqQkg2oQX4L7ySrpyuQ, read 2026-10-28).

## Could not verify
- Release version of this doc; how widely regulated customers enable auto-approval.
