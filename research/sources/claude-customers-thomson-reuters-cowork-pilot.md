---
title: Thomson Reuters CTO on piloting Cowork with Claude Enterprise
source_url: https://claude.com/customers/thomson-reuters-qa
author: Anthropic (Q&A with Joel Hron, CTO, Thomson Reuters)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [metrics-review-agents, human-review-gates, enablement-by-product, skills-marketplace, enterprise-admin-controls]
relevance: medium
---

## Relevance to the project
The CTO of a trust-sensitive, professional-services company describes piloting Cowork with a small group of sophisticated Claude users, connected to live Microsoft 365 data rather than a sandbox, with least-privilege approved connectors and human validation of consequential outputs. The one worked workflow is a PM-adjacent one: an NPS spreadsheet plus comments turned into themes and a draft leadership readout that teams then validate. The next step he names is moving from person-by-person skills to shared plugins and standard workflows, which bears on adoption-model, capability-distribution-trust and target-user. Pilot-stage, no metrics; the CTO's account.

## Themes
- metrics-review-agents: input an Excel file of NPS scores and comments plus a prompt to compare quarters, find themes and draft a leadership summary; output is a "reviewable draft"; "It is not publish-without-review" (Q&A, workflow answer).
- human-review-gates: teams "validate the numbers and refine the narrative"; human validation required for "consequential outputs" (Q&A, workflow and guardrails answers).
- enablement-by-product: pilot with a small group already sophisticated with Claude, then advice to start with capable early adopters on consequential use cases (Q&A, first and last answers).
- skills-marketplace: "The next step is to systematize it: shared plugins, standard workflows for common tasks", with lightweight mechanisms likened to code review (Q&A, untapped potential).
- enterprise-admin-controls: Claude Enterprise valued for data isolation, security controls and admin oversight; least privilege via approved connectors (Q&A, guardrails answer).

## Key points
- **Approach.** Cowork piloted as an extension of Claude Enterprise, not rolled out enterprise-wide; judged on "real conditions" against live documents.
- **Non-developer use.** Product, operations and business teams already heavy users of Claude Enterprise; Cowork adds "structured workflow capability", letting a PM describe a workflow, attach files and get a first-draft structure or analysis.
- **Scale effect.** Tailoring survey insights for different audiences was limited by manual effort; Cowork parallelises it; the human role is "validation, refinement, and decision-making".
- **Governance stance.** "Governance is not an afterthought. It is part of adoption"; guardrails framed as what lets them move faster.
- **Measurement advice.** Measure beyond time saved: higher-quality work and newly practical workflows. No numbers given.
- **Limits.** Pilot only; no usage counts, error rates or examples of rejected output; the NPS workflow carries known synthesis risk (theme extraction from free text), handled only by "teams validate".

## Notable quotes
- "The human role does not disappear. It moves up the stack." (Joel Hron)
- "Governance is not an afterthought. It is part of adoption." (Joel Hron)

## Could not verify
- Publication date; pilot size and duration.
