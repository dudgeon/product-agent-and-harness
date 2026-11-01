---
title: Devin can now Manage Devins
source_url: https://cognition.com/blog/devin-can-now-manage-devins
author: Cognition
publisher: Cognition blog
published: 2026-03-19
retrieved: 2026-10-31
type: article
evidence: vendor-claim
filed_by: research-agent-handoff-models
themes: [one-job-per-agent, shared-persistent-sessions, human-review-gates]
relevance: medium
---

## Relevance to the project
A shipped manager-and-children pattern in which each child is a full session in its own VM with its own link: the human can open any child and message it directly, or go through the manager. The manager reads child trajectories, sends corrections mid-task, schedules follow-ups to itself, and compiles results. It is a concrete case of the through line held by a coordinating agent while the person can still reach the children.

## Themes
- one-job-per-agent: scoped children (one page, one package, one batch), each verifying its own changes before reporting.
- shared-persistent-sessions: each child has its own session link; the manager can "send instructions, context, or corrections to any managed Devin mid-task".
- human-review-gates: manager "resolves any conflicts, and compiles the results", e.g. into a set of PRs for review.

## Key points
- The manager monitors spend (ACUs) and can pause or terminate children.

## Could not verify
- Child payload format and merge mechanism.
