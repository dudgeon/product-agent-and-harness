---
title: "Working with databases (Notion API docs)"
source_url: https://developers.notion.com/docs/working-with-databases
author: Notion
publisher: developers.notion.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [work-structure-spectrum, legible-org-for-agents]
relevance: high
---

## Relevance to the project

Notion's object model: a database is a container, a data source holds the schema, pages are rows with typed properties. PM artifacts in Notion (roadmaps, specs, customer calls) are usually pages in databases, which is the Ramp Glass 'formal record' described by Geoff Charles. Shows how a schema-first primitive differs from file-based ones.

## Themes

- work-structure-spectrum: databases give typed structure, pages give free-form body, in the same object.
- legible-org-for-agents: schema lives on the data source so an agent can read property types.

## Key points

- Database = container holding data sources and views; does not carry the schema in current API versions.
- Data source = schema (property names, types, settings) and parent of its pages.
- Page belongs to a data source via parent.data_source_id; properties match the schema; content blocks form the body. Exactly one title property per data source.
- View = a way of displaying a database (table, etc.). Linked database shows an existing data source elsewhere without creating pages. Wiki databases support page verification and cannot hold multiple data sources.

## Could not verify

The page says little about views. No statement about 'project' as a first-class Notion object; projects are a template/convention built on databases (from general knowledge, not this page).

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.
