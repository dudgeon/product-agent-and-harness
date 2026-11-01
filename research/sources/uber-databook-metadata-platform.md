---
title: "Databook: Turning Big Data into Knowledge with Metadata at Uber"
source_url: https://www.uber.com/blog/databook/
author: Luyao Li, Kaan Onuk, Lauren Tindal (Uber Data Knowledge Platform)
publisher: Uber Engineering blog
published: 2018-08-03
retrieved: 2026-10-31
type: article
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms, stale-records-mislead-agents]
relevance: medium
---

## Relevance to the project
Uber replaced hand-maintained static HTML catalogue pages, which could not keep up, with a metadata platform that collects most metadata automatically (crawlers, Kafka events for freshness and lineage) and leaves only meaning (descriptions) to people. It bears on which trust mechanism to use: the most trusted fields are the ones derived from the systems themselves, and human-written fields are the residue. For the project's platform cards, it suggests deriving what can be derived (owner from on-call or repo, lead time from tickets) and asking people only for the rest.

## Themes
- context-trust-mechanisms: metadata collected three ways: scheduled crawlers (usage statistics, sample data), event streams for near-real-time lineage and freshness changes, and manual UI input for table and column descriptions (architecture sections).
- stale-records-mislead-agents: in 2015 the catalogue was manually maintained static HTML, which could not keep pace with growth; and by design, if collection is down, "outdated metadata will still be served" (background and architecture sections).

## Key points
- Fields held: owners, freshness, SLAs, schema, descriptions, sample data, statistics, lineage, personal-data categorisation (overview).
- Freshness trade-off stated: "most use cases require fresh metadata, they do not need to see metadata changes in real time", so periodic crawling suffices for most fields; events only where near-real-time matters (architecture section). Freshness requirements differ per field.
- Serving outdated metadata during a collection outage is a deliberate availability-over-freshness choice. Unless the age is shown, a reader cannot tell.
- The post does not describe how human-entered descriptions are checked, nor any staleness or accuracy measure.
