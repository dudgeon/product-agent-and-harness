---
title: "Build-Run Teams and Segregation of Responsibility"
source_url: https://curvelogic.github.io/software-delivery/devops/audit/risk/2020/02/05/build-run-risk.html
author: Greg Hawkins
publisher: Curve Logic
published: 2020-02-05
retrieved: 2026-10-28
type: article
evidence: anecdote
filed_by: research-dependency-agent
themes: [process-governance-load, risk-sloped-review]
relevance: medium
---

## Relevance to the project
A practitioner essay on the collision between "you build it, you run it" and segregation of responsibility, the control auditors and regulators expect so that no one person can make and release a harmful change. It lays out a spectrum of controls from strongest to weakest (separate reporting lines, assumed-role peer review, pairing, automation, access controls, reversibility and visibility) and argues the choice should start from the risk, not from absolutes. For a dependency agent this frames governance dependencies: which control a change needs is a classification question, and the heavyweight option makes everything slow.

## Themes
- process-governance-load: "SoR makes it hard to do bad things by making it hard to do anything." Strong segregation by department is effective but heavyweight and prone to rubber-stamping.
- risk-sloped-review: "Always start with the risk"; acceptable risk depends on the organisation's size and circumstances; controls are chosen to fit.

## Key points
- "Auden" stands for anyone representing risk (auditors, regulators, security); their job is to assess risk, not design controls.
- Automation reduces human involvement but raises the question of who controls the automation and whether it can be bypassed.
- Corrective and detective controls (kill switches, reversibility, high visibility) count: "You can do anything you can undo!"
- Cites UK challenger banks Starling and Monzo as build-run cultures operating under heavy regulation.
- "toxic combination": complementary responsibilities that let error or fraud go undetected.
