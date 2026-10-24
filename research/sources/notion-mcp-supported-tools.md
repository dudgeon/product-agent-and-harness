---
title: "Notion MCP supported tools"
source_url: https://developers.notion.com/guides/mcp/mcp-supported-tools
author: Notion
publisher: developers.notion.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [harness-portability, skill-standards, shared-persistent-sessions]
relevance: high
---

## Relevance to the project

The broadest first-party MCP surface among the PM platforms checked: pages, databases and views, comments, teams and groups, meeting notes, saved agent memories, Skills, and Custom Agent sessions can all be driven externally. For a meta-harness it shows one platform treating 'skills' and 'agent sessions' as ordinary workspace objects.

## Themes

- skill-standards: tools to convert a page to a Skill, upload/download Skills; enabled-skill lists capped at 30; uploads up to 20 MiB compressed / 1,000 files.
- shared-persistent-sessions: notion-spawn-session, wait-session, send-message-to-session, read-session-event let an outside agent start and observe Custom Agent sessions.
- harness-portability: companion overview page says it is a hosted remote MCP using OAuth, with Claude Code, Cursor, Codex as examples; Enterprise plan needed to restrict which clients members may connect.

## Key points

- Search (up to 50 results), connector search across Slack/Drive/GitHub, memory search over saved agent memories.
- Pages: fetch, create (templates, Skills, async), update (search-and-replace), move, duplicate, delete/restore (max 20 items; destructive tools need user_confirmed), folders, backlinks.
- Databases: create database with initial data source and view, update data source, create/update views (table, board, list, calendar, timeline, gallery, form, chart, map, dashboard), query data sources (100 rows max, no cursor), SQL across 2-100 data sources on Business/Enterprise with Notion AI.
- Comments and discussions; teams, permission groups (max 25), users; meeting notes; calendar (user-authorised connections only).

## Could not verify

Many tools are plan-gated (Business/Enterprise with Notion AI). I did not verify tool behaviour by calling it.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.
