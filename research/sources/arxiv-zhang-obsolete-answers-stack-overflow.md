---
title: "An Empirical Study of Obsolete Answers on Stack Overflow"
source_url: https://arxiv.org/abs/1903.12282
author: Haoxiang Zhang, Shaowei Wang, Tse-Hsun (Peter) Chen, Ying Zou, Ahmed E. Hassan
publisher: IEEE Transactions on Software Engineering (arXiv preprint)
published: 2019-03-28
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms, stale-records-mislead-agents]
relevance: high
---

## Relevance to the project
The strongest measured evidence that community correction does not, by itself, keep written knowledge current: once a Stack Overflow answer was flagged obsolete in a comment, only about a fifth were ever updated, it took months on average, and most obsolescence was spotted by someone other than the author. It bears on "trust by use with corrections" versus owner-verified or expiry-based mechanisms: readers notice staleness, but the flag rarely reaches the record. It also shows that accepted status (an asker's endorsement) does not protect against obsolescence.

## Themes
- context-trust-mechanisms: 58.4% of obsolete answers were probably already obsolete when posted; only 20.5% of answers observed as obsolete were ever updated; average 118 days for users to react to an observed obsolete answer (abstract; RQ1 summary, section 4.1).
- stale-records-mislead-agents: 44.1% of the obsolete answers studied were accepted answers; even accepted ones were updated only 30.7% of the time after being flagged, against 24.8% for non-accepted answers (section 4.1.1).

## Key points
- Data: 52,177 obsolete answers identified from comments noting obsolescence (section 4.1). Base rate is low per tag: the most obsolete-prone tag, node.js, has 0.36% of answers flagged obsolete, ajax 0.34%, android and objective-c 0.32% (RQ2 results). These are flagged rates, a lower bound.
- Time to correction: 227 days on average to the first update after obsolescence is noted in a comment; 198 days to the first new answer (section 4.1.1). Upper-bound estimate: 49.8% of obsolete answers got either an update or a new answer.
- Who notices: most obsolete answers were not observed by the original answerer, and most observations came with evidence (a version, a reference, updated information) (RQ4). The signal is cheap and well-evidenced; the bottleneck is acting on it.
- Cause: mainly evolution of languages, libraries, APIs and frameworks (RQ3). The enterprise analogue is a platform changing its intake or lead time.
- Authors' recommendations: automated detection of obsolete answers, even by keyword search, and badges or reputation to reward maintenance by the whole community, not just the author (section 1).

## Notable quotes
- "Most users did not update obsolete answers or add new answers to address the observed obsolescence." (RQ1 summary)
