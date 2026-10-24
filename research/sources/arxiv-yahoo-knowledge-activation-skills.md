---
title: "Knowledge Activation: AI Skills as the Institutional Knowledge Primitive for Agentic Software Development"
source_url: https://arxiv.org/abs/2603.14805
author: Gal Bakal (Yahoo; views stated as the author's own)
publisher: arXiv
published: 2026-03-16
retrieved: 2026-10-24
type: paper
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [tacit-knowledge-capture, skill-standards, compounding-context-repo, org-learning-loop]
relevance: high
---

## Relevance to the project

A rare full write-up of a curated-owner model: a platform team codifies institutional knowledge into 87 governance-annotated skills, maps the work explicitly onto SECI ("algorithmic externalization"), and reports both a survey result and the failure modes. Its limitations section is the best evidence in hand on where curated capture breaks: contribution access, staleness and authoring cost. The author led the deployment, so results are first-party and self-reported.

## Themes

- **tacit-knowledge-capture**: "algorithmic externalization" is "the conversion of tacit institutional knowledge into machine-executable form through deliberate, structured codification"; extraction via "structured interviews with domain experts, analysis of existing automation scripts" (§4.2.1, §4.5). Admits "some governance decisions require human judgment that resists codification" (§9.3).
- **compounding-context-repo**: 57 days from repo start to survey; 68 PRs merged; 26 skill-gap reports filed and closed; survey of 67 engineers: mean 2.6 hours saved per week, NPS +35 (§8).
- **org-learning-loop**: the maintaining team owned most contributions; outsiders hit repo-access, review-permission and entitlement barriers before they could open a PR (§8.7). Proposed fix: an InnerSource "knowledge commons" with trusted-committer review, whose "incentive alignment" the paper "theorizes but does not empirically validate" (§9.3, §9.5).
- **skill-standards**: Atomic Knowledge Units are a specialisation of the open Agent Skills standard, with a seven-part schema and validators as "governance-as-code" (§5, §7).

## Key points

- Thesis: the bottleneck is knowledge architecture, not model capability; human-written docs impose an "institutional knowledge tax" on senior engineers.
- Staleness: no session-start check compares installed skills with the canonical version, so drift is unmeasured; "Users running month-old corpus versions receive stale guidance"; detection is "an open engineering problem" (§8.7, §9.3).
- "skill authoring represents a significant organizational investment" (§9.3).
- Survey: 40 active users, 19 non-installers, 8 lapsed; voluntary, anonymous, May 1–15 2026; response rate unknown.

## Notable quotes

- "The bottleneck to effective agentic software development is not model capability but knowledge architecture."
- "the architecture's contribution model assumes low-friction access to the corpus repository"

## Could not verify

- Who authored individual skills and how long each took; invited population for the survey.
