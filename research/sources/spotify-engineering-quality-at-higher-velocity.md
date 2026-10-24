---
title: "AI Changed How Spotify Builds. What We Learned (and Fixed) About Quality at Higher Velocity"
source_url: https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity
author: Tyson Singer (SVP, Head of Technology and Platforms, Spotify)
publisher: Spotify Engineering blog
published: 2026-09-16
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [verification-capacity-gap, outcome-measurement-gap, risk-sloped-review, agent-failure-modes]
relevance: high
---

## Relevance to the project
Spotify's first public account of quality problems after the AI speed-up. Its claim is that AI-written code was not the cause; the volume of change outran verification, rollout and monitoring. Merged changes more than doubled year over year (about 8,100 to 17,000 in August), and an automated dependency upgrade passed checks but broke production for users. For the project, this is first-party evidence that the next limit after code generation is verification and release control, not authoring.

## Themes
- verification-capacity-gap: "The next constraint became our ability to verify it"; change volume outpaced some verification controls (monthly incident retros now ask whether AI code or change volume contributed).
- outcome-measurement-gap: rework rate rebuilt to separate real rework from new work; no rise found (Spotify claim, Sep 2026), against FAROS 2026's industry-wide churn rise; PR size and complexity rising, meaning unclear.
- risk-sloped-review: automated fleet changes mostly auto-merge after safety checks; after the bad upgrade, Spotify added safeguards, more rollback capacity, and runs automated changes in owning teams' working hours.
- agent-failure-modes: mobile regressions build up below monitored signals while releases look healthy; fix: broader signals and long-term trends in release decisions.

## Key points
- Merged PR mix (Aug, year over year): quality/optimisation 27% to 31%; maintenance/config 31% to 25%.
- Other incidents: content processing delays (June 24), compute shortages linked to industry AI demand.
- Cites DORA 2025: AI adoption linked to higher throughput but lower stability.
- Says plainly "AI slop isn't among those" problem areas.
- Process changes: the monthly incident retrospective now also asks whether AI-authored code contributed and whether change volume strained review and rollout; automated changes are scheduled in owning teams' working hours; the mobile quality cycle is "ship fast, then broaden guardrails"; complexity and PR-size thresholds were deliberately left unchanged.

## Could not verify
- Incident counts are not given; the "not material" finding is Spotify's own review.
