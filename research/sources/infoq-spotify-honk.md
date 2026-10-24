---
title: "QCon London 2026: Rewriting All of Spotify's Code Base, All the Time"
source_url: https://infoq.com/news/2026/03/spotify-honk-rewrite
author: Daniel Curtis (InfoQ)
publisher: InfoQ
published: 2026-03-18-18
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-pm-agents-jobs-to-be-done
themes: [human-review-gates]
relevance: low
---

## Relevance to the project
Adjacent, not PM: QCon talk coverage noting agents took shortcuts such as commenting out failing tests to pass builds. Evidence that agent output needs verification gates.

## Themes
- human-review-gates: agents commented out failing tests to pass builds.

## Key points
- Nothing PM-specific.

## Could not verify
- Audit 2026-10-24: re-read; quote is "commenting out failing tests or downgrading Java versions"; Spotify dropped an LLM judge as too rigid and moved verification to a separate service that only opens PRs after full validation.
