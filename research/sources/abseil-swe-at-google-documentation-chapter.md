---
title: "Software Engineering at Google, Chapter 10: Documentation"
source_url: https://abseil.io/resources/swe-book/html/ch10.html
author: Tom Manshreck (in Winters, Manshreck and Wright, eds.)
publisher: O'Reilly / abseil.io (free online edition)
published: 2020-03
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms, stale-records-mislead-agents]
relevance: high
---

## Relevance to the project
Google's first-party account of why its open internal wiki failed and what replaced it: documents without owners went stale, so docs moved into source control with owners, code review, bug tracking, and "freshness dates" that trigger reminders after a set period. It bears directly on the owner-verified and expiry-and-re-verification mechanisms, and on cost to the owner: re-verifying is a one-line date change that still goes through review. It also admits that accuracy and freshness are not yet measured by tools.

## Themes
- context-trust-mechanisms: freshness dates record when a document was last reviewed; metadata sends email reminders when a document has not been touched for a set period such as three months; a visible "Last reviewed by" byline increased adoption (section on documentation freshness / "Documentation is like code").
- stale-records-mislead-agents: the GooWiki audit found "around 90% of the documents had no views or updates" in the prior few months; "Because there were no true owners for documents, many became obsolete" (sections on GooWiki and on treating documentation like code).

## Key points
- Ownership is the root mechanism: "Documents without owners become stale and difficult to maintain." Ownership also lets docs flow through bug trackers and code review.
- Docs as code: documentation should be under source control, have owners, undergo review for changes and "change with the code it documents", have tracked issues, and be periodically evaluated. Moving wiki content into source control (g3doc, Markdown beside the code) brought review and bug reporting to docs and quality improved.
- Freshness check is cheap and reviewed: updating the date requires a code review, a low-cost way to confirm a document is still looked at. Note the weakness: a reviewer can approve a date bump without reading the document.
- Deprecation: for a document that no longer serves a purpose, "either remove it or identify it as obsolete"; a note saying it is outdated is better than nothing.
- Review types: technical (accuracy), audience (clarity), writing (consistency); readers' bug reports act as an implicit audience review.
- Measurement gap: docs should ideally be measured for "accuracy, freshness, etc." but "tools have still not caught up here"; quality is judged by the reader, not the writer.

## Notable quotes
- "Documents without owners become stale and difficult to maintain."
