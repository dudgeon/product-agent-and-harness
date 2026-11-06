---
title: "anthropics/claude-for-legal: A suite of plugins for legal workflows (product-legal and regulatory-legal plugins)"
source_url: https://github.com/anthropics/claude-for-legal
author: Anthropic
publisher: GitHub
published: 2026-04-21
retrieved: 2026-11-06
type: docs
evidence: first-party
filed_by: design-requirements-agent
themes: [launch-readiness-review, risk-review-as-classification, compounding-context-repo, ai-synthesis-hallucination-risk, human-review-gates]
relevance: high
---

## Relevance to the project
The closest public, inspectable analogue to the requirements agent's obligation step: Anthropic's product-counsel plugin reads a PRD or tracker ticket, walks a launch-review framework category by category (contractual commitments, privacy, security, IP, third party, regulatory, marketing claims, AI governance), each with a key question and an explicit auto-skip condition, and calibrates each finding against a "risk calibration table" learned from the company's ten most recent launch reviews (what actually blocked versus shipped). A scheduled launch-watcher scans the tracker daily for launches in the next 30 days that need review, and a PM-facing "is this a problem?" skill gives same-minute triage. The companion regulatory-legal plugin watches regulator feeds and diffs changes against the policy library. Read files: README, product-legal README, launch-review SKILL.md, eight-category framework reference, cold-start-interview SKILL.md, launch-watcher agent, regulatory-legal README.

## Themes
- launch-readiness-review: launch-review steps: load calibration; get PRD, spec, marketing plan, launch date and ticket comments; "understand what's launching" in plain English (who uses it, what is new versus already reviewed, new data, vendors, claims, jurisdictions); run AI detection before the framework walk; walk every category; output a memo a PM can act on (launch-review SKILL.md).
- risk-review-as-classification: each category has a key question and an "Auto-skip if" condition, e.g. Privacy skipped only if "No data changes"; Regulatory skipped only if same users, sectors and jurisdictions (framework reference).
- compounding-context-repo: "The calibration table is the whole thing. If it's wrong, every review is wrong"; re-run setup "when your risk posture changes (new regulator, new consent decree, new GC)" (product-legal README).
- ai-synthesis-hallucination-risk: "No silent supplement": if the research tool returns thin results, report and stop rather than fill from web or model knowledge; every citation tagged by source and tier (`[settled]`, `[verify]`, `[verify-pinpoint]`, `[platform policy — verify against live docs]`) (launch-review SKILL.md).
- human-review-gates: "Every output is a draft for attorney review"; consequential actions gated behind explicit confirmation (README).

## Key points
- Cold start: connects to Jira or Linear, reads ten past launch reviews, builds the calibration table, asks for confirmation; a shared company profile (industry, jurisdictions, regulators, risk appetite, escalation names) is written once and reused by all legal plugins.
- Launch-watcher trigger keywords: new data or tracking; children and teen terms; health; personal data; unapproved vendor names; terms or policy changes; country names (jurisdictional expansion); beta-to-GA; AI and model terms.
- Feature risk assessment is reserved for the roughly 10% of launches that need depth; the README warns against generating paperwork for the rest.
- Integration honesty: a connector is reported as working only if a tool call actually succeeded.
- Regulatory-legal: cold-start builds a regulator watchlist, indexes the policy library and learns a materiality threshold; skills diff a regulation against policies, track gaps and draft policy redlines; "Materiality filtering is the value."
- Repo created 21 April 2026; about 9,900 stars on 6 November 2026; launch-review skill last changed 12 May 2026.

## Notable quotes
- "The calibration table is the whole thing. If it's wrong, every review is wrong." (product-legal README)

## Could not verify
- These are reference implementations, not a deployment account: no usage, accuracy or time-saved figures are published. The `/ai-governance-legal:use-case-triage` skill and the privacy-legal PIA skill that launch review hands off to were not read.
