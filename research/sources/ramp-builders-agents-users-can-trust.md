---
title: How To Build Agents Users Can Trust
source_url: https://builders.ramp.com/post/how-to-build-agents-users-can-trust
author: CJ Enright, Will Koh, Felix Zhang
publisher: Ramp Builders (builders.ramp.com)
published: 2025-07-10
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-ramp-glass
themes: [evals-autonomy-trust, human-review-gates, org-context-grounding]
relevance: medium
---

## Relevance to the project

Ramp's design principles for its customer-facing Policy Agent (expense approvals). Not part of Ramp's internal product lifecycle, but it is the clearest first-party statement of the trust pattern Ramp reuses: reasoning with citations, an "unsure" escape hatch, categories instead of confidence scores, user-editable context, an autonomy slider and suggestions before actions. Bears on review-and-autonomy and on how a PM agent should defer.

## Themes

- **evals-autonomy-trust**: "suggestions → acting on subsets → full autonomy"; golden datasets reviewed by Ramp because users are lenient; user-flagged errors become eval cases (Start with suggestions; Evals).
- **human-review-gates**: Approve / Reject / Needs review categories; deterministic hard stops (dollar limits, blocklists) layered over the agent; autonomy set in the existing workflow builder (Confidence scores; Autonomy slider).
- **org-context-grounding**: the expense policy moved into Ramp as editable context that users fix when they disagree with the agent (Context should be collaborative).

## Key points

- More than 65% of approvals at Ramp fully handled by the policy agent (self-reported).
- Every decision cites the policy section it relies on.

## Could not verify

Figure self-reported; no external evaluation.

## Added by research-skill-rigidity-spectrum (2026-10-25)
- Contrast: Cognition's Devin 2.1 ships a green/yellow/red self-confidence rating and asks clarifying questions below green, claiming green doubles merged-PR likelihood (cognition-devin-2-1-confidence, vendor claim). Ramp chose categories (Approve / Reject / Needs review) over confidence scores; both converge on a small set of categories rather than a numeric score shown to users. Theme: evals-autonomy-trust.
