---
title: "Scaling Knowledge at Airbnb"
source_url: https://medium.com/airbnb-engineering/scaling-knowledge-at-airbnb-875d73eff091
author: Chetan Sharma and Jan Overgoor (Airbnb)
publisher: The Airbnb Tech Blog (Medium)
published: 2016-02-25
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [compounding-context-repo, docs-as-code-prd, research-synthesis-agents, human-review-gates, memory-architecture]
relevance: medium
---

## Relevance to the project
Airbnb's Knowledge Repo (later open-sourced) is an early, concrete design for how research findings get recorded, peer-reviewed and found again: notebooks and Markdown committed to Git with front-matter (authors, tags, TLDR), reviewed through pull requests, rendered as an internal blog with topic subscriptions. This is close to what this project calls a compounding, inspectable context repo for research evidence. It predates 2020, so it shows the data team's decision-record culture rather than the post-2020 product model.

## Themes
- compounding-context-repo: the stated problem is "scaling knowledge": an insight found by one person should transfer "across teams and across time"; heuristic "if it could potentially be useful to someone in the future, post it!"
- docs-as-code-prd: "At the core there is a Git repository"; every post starts with structured metadata including a TLDR; validated by a script; reviewed by GitHub pull request.
- research-synthesis-agents: open problem named: "the synthesis of the work that is done by individuals... weave them into a shared understanding of Airbnb's ecosystem" (Future section).
- human-review-gates: "No piece of research should be shared without being reviewed for correctness and precision"; review combines code review with academic peer review.
- memory-architecture: tags give "many-to-one topic inheritance"; posts browsable by time, topic, author; subscriptions notify on new posts.

## Key points
- Five tenets: reproducibility, quality, consumability, discoverability, learning.
- The "Jennifer" story: a new data scientist gets a "mixed bag of presentations, emails, and Google Docs", stale code, and redoes the work, "perpetuating the cycle".
- Content: deep dives, experiment analyses not covered by the experiment reporter, methods write-ups, tutorials, public blog posts.
- Planned: adoption by qualitative researchers who don't use GitHub, via an in-browser Markdown editor with review; topic proposal and upvoting; forking posts.

## Could not verify
- No source found on whether Knowledge Repo is still used at Airbnb in 2026 or whether research from user researchers ever went in.
