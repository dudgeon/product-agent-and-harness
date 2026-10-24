---
title: "Beyond Winning: Spotify's Experiments with Learning Framework"
source_url: https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework
author: Michael Bellato, Mårten Schultzberg, Sebastian Ankargren (Spotify data scientists)
publisher: Spotify Engineering
published: 2025-09-23
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [experiment-decision-rules, outcome-measurement-gap, metrics-review-agents, org-learning-loop]
relevance: high
---

## Relevance to the project
Spotify measures its experimentation program by "learning rate" (share of experiments that are valid and decision-ready) rather than win rate: ~64% learning vs ~12% wins in the two orgs running ~80% of experiments. The platform classifies every experiment and asks experimenters why they stopped. For the project this is a working example of turning "operate and learn" into a structured, machine-readable decision record (ship / abort / iterate), and of the platform itself being the place outcomes are stored.

## Themes
- experiment-decision-rules (proposed): an Experiment with Learning is valid (no sample ratio mismatch, metrics measured) and decision-ready: success leads to ship, regression to abort and iterate, powered-neutral to iterate, abandon, or ship if infra-only ("What counts as an Experiment with Learning?").
- outcome-measurement-gap: Spotify defines and measures experiment quality at org level; learning rate varies by team from 16% to 76% ("Spotify's learning rate").
- metrics-review-agents: Confidence automatically monitors key business metrics for regressions in every experiment; prompts users for a reason when they end a test, so "aborted" vs "unpowered" can be separated ("Aborted").
- org-learning-loop: adding experiment reviewers "can drastically impact learning rates" because ideas are scrutinised before tests start ("Improving practice and Confidence").

## Key points
- History: 2018 platform investment set the goal that every team with a user-facing mission should experiment regularly; an "engagement team" (internal customer success) grew regularly experimenting teams from ~40 to 200+ by end 2021 and ~300 a year later (authors' figures).
- "Experiment-Needs Pyramid": teams experiment only if technically able, know how, and are incentivised; managers and stakeholders were taught to expect experiments with new features.
- Experiments are also risk management for changes with only downside (refactors, infra), and for quantifying AI features whose costs must be weighed.
- Strict powering rule: a neutral test counts as learning only if every metric is powered.
- Scale: in one year 58+ teams ran 520 experiments on the mobile Home screen alone; testing bandwidth is "one of the true currencies for innovation speed", and EwL is used to triage which programs get traffic.
- Uses: a stable learning rate with falling win rate signals diminishing returns and a need for "bolder bets"; EwL is a productivity signal for the platform org alongside DevOps metrics; guardrails against gaming (win rate, volume, precision).

## Could not verify
- Full post read. Figures (64%, 12%, 16-76%, 300 teams, 520 experiments) are Spotify's own, with inclusion criteria stated but no raw data.
