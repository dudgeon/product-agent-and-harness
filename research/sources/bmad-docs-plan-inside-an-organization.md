---
title: "Plan Inside an Organization (BMad Method docs)"
source_url: https://docs.bmad-method.org/plan/plan-inside-an-organization/
author: BMad Code
publisher: docs.bmad-method.org
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, human-review-gates, docs-as-code-prd, decision-rationale-records]
relevance: high
---

## Relevance to the project
A rare first-party treatment of a document relay inside an organisation: one owned anchor document (the PRD), one owner and one writing skill per document, five named human sign-off points that each block a next step and leave a written result usable as an audit trail, and trackers (Jira, Linear) kept as the reporting home but never as build state. It is close to the shape the intent-shaping module would need under model A, and it says how change propagates over weeks.

## Themes
- process-artifacts-as-coordination: planning documents "are contracts between people first and input to the skills second"; "The PRD is the document the organization owns"; "Nothing downstream reinterprets the PRD."
- human-review-gates: five decision points: PRFAQ verdict, PRD validation, architecture spine review, ticket-breakdown approval, retrospective verdict; reviewers request changes in the source document, not copies.
- docs-as-code-prd: existing PRDs in Confluence or Notion can be validated as input; derived documents can be regenerated from the PRD, so edits belong in the PRD.
- decision-rationale-records: replanning logs each reason; requirement IDs stay stable through updates; historical plans are kept.

## Key points
- Ownership table (roles, not headcount): PM owns the PRD; designer owns DESIGN.md and EXPERIENCE.md; tech lead owns the architecture spine; one engineer per epic owns the epic file, its tickets.toml and verdict; whoever tracks the whole owns the ticket tree and plan statuses via Sofia.
- Conflict rule: if a ticket needs an answer the PRD lacks, update the PRD first and re-run Sofia; if a ticket's requirements conflict with the PRD, Sofia flags it for a human decision.
- Trackers: Jira or Linear stays the planning and reporting home; "Tracker status is mirrored separately and never makes a build skip work."
- Long-lived work: several engineers on separate epics; the spine records shared decisions (API style, data ownership); a parent initiative holds shared requirements for multi-product programmes; changes flow outward from the PRD.
- Gap for the project (my reading): no notion of owners outside the team who must act (platform, risk, gate owners); "organization" here means internal reviewers and approvers of the feature's own documents.

## Could not verify
- Page undated; retrieved via WebFetch (model-summarised), quotes to be re-checked.
