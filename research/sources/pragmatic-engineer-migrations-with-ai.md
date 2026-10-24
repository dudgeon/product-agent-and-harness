---
title: "The Pulse: We need to talk about migrations with AI"
source_url: https://blog.pragmaticengineer.com/the-pulse-we-need-to-talk-about-migrations-with-ai/
author: Gergely Orosz
publisher: The Pragmatic Engineer
published: 2026-08-27
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-airbnb-spotify-product-practices
themes: [vendor-claims-vs-independent-evidence, harness-over-model, human-review-gates]
relevance: low
---

## Relevance to the project
Independent context for Airbnb's test-migration case among other AI migration claims (Asana with Codex, Uber JUnit, Bun Zig to Rust). The useful part is the critique: headline "years of work" baselines are often back-of-envelope or describe low-priority work that would have trickled for years, and successful migrations still needed engineers to plan the work and design verification loops.

## Themes
- vendor-claims-vs-independent-evidence: Asana's "5 years in 2 weeks" (OpenAI case study) rests on a $6M estimate the author calls inflated; Asana confirmed it was back-of-envelope.
- harness-over-model: all successful cases built verification loops and staged pipelines.
- human-review-gates: engineers stayed in the loop throughout, including Airbnb's manual last ~3%.

## Key points
- Repeats Airbnb's figures (3,500 files, six weeks, 1.5-year estimate, 75% in four hours, 97% after four days) and notes the work used early-2025 models.
- Argument: AI makes long-deferred migrations practical at all; the bigger gain is not maintaining two systems for years.

## Could not verify
- The author did not re-check Airbnb's numbers.
