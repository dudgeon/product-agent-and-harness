---
title: "Microsoft Responsible AI Impact Assessment Template"
source_url: https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf
author: Microsoft Office of Responsible AI
publisher: Microsoft
published: 2022-06-21
retrieved: 2026-11-06
type: docs
evidence: first-party
filed_by: design-requirements-agent
themes: [launch-readiness-review, risk-review-as-classification, requirements-partitions, agent-led-intent-shaping]
relevance: high
---

## Relevance to the project
The externally released form Microsoft teams complete "early in the system's development, typically when defining the product vision and requirements" (per the Standard's A1.1) is a working example of an obligation-discovery instrument: it starts from the feature (purpose, features, geographies and languages, deployment mode, intended uses), walks stakeholders, benefits and harms per intended use, then makes the team decide, Goal by Goal, whether each enterprise requirement applies, with a written reason for every "No". That applicability table with mandatory "none, because" is the same mechanism the intent-shaping brief's check step specifies. It also shows the trigger questions for escalated review (Restricted Uses, Sensitive Uses).

## Themes
- launch-readiness-review: section 5.3: complete the appropriate reviews and secure all approvals "before beginning development"; section 1.1 names the reviewers up front.
- risk-review-as-classification: section 3.6 lists Sensitive Use triggers (yes/no), e.g. significant physical or psychological injury; 3.1 lists uses under legal or internal policy restriction; 2.5 to 2.8 force single-choice ratings of technology readiness, task complexity, role of humans and deployment environment complexity.
- requirements-partitions: section 5.2 "Goal Applicability": for each Goal (Accountability, Transparency, Fairness, Reliability & Safety, Privacy & Security, Inclusiveness) mark Yes or No; "If you indicate that a Goal does not apply to the system, explain why"; if it applies, its requirements must be completed during development.
- agent-led-intent-shaping: the structure (system profile, intended uses repeated per use, stakeholders, harms, data requirements, summary of impact mapping each harm to a Goal) is an interview script an agent could run and pre-fill from documents.

## Key points
- Section 1: system name, team, authors, reviewers; lifecycle stage and planned release dates; plain-language description with links to specs, decks and architecture diagrams; purpose; existing versus upcoming features; relation to other systems; geographic areas and languages (now, next release, future); deployment modes; intended uses ("who will use the system, for what task or purpose, and where").
- Section 2 (repeated per intended use): fitness for purpose; up to ten stakeholders with benefits and harms; stakeholders required by specific Goals (A5 human oversight, T1 intelligibility for decisions, T2 communication, T3 disclosure of AI interaction); fairness goals F1 to F3 with prioritised demographic groups.
- Section 3: restricted uses, unsupported uses, known limitations, predictable failures (false positives and negatives), misuse, sensitive-use triggers.
- Section 4: data requirements and suitability of existing data sets.
- Section 5: harms table mapped to Goals, Goal applicability with reasons, sign-off by reviewer role.

## Notable quotes
- "If you indicate that a Goal does not apply to the system, explain why" (5.2)

## Could not verify
- Downloaded from the URL above, which redirects to msblogs.thesourcemediaassets.com; read as extracted PDF text. Publication day taken from the Responsible AI Standard v2 release (June 2022); the PDF says only "June 2022". The companion Impact Assessment Guide was not read.
