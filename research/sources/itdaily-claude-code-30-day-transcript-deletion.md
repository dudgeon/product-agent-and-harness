---
title: "Claude Code deletes conversation history after 30 days by default"
source_url: https://itdaily.com/news/cloud/claude-code-deletes-conversation-history-after-30-days-by-default/
author: ITdaily
publisher: ITdaily
published: 2026-07-01
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [memory-architecture, harness-portability, shared-persistent-sessions]
relevance: medium
---
## Relevance to the project
Independent news report that local session transcripts are auto-deleted after 30 days by default, with Anthropic defending it as a security default and users losing decisions and reasoning. Evidence that transcript storage and retention is a real design axis: local private sessions are ephemeral by default, and cloud sessions rely on vendor-held transcripts.

## Themes
- memory-architecture: cleanupPeriodDays defaults to 30, run on each startup; users say there is no warning or recovery; deletion keys on file modification time so backups or sync can trigger removal of active files (per GitHub discussions cited)
- harness-portability: Anthropic's stated reason is that plain-text transcripts can hold code and credentials, i.e. retention conflicts with auditability

## Key points
- See also the Anthropic cloud docs: cloud sessions store transcripts server-side and restore history on reopen.

## Could not verify
- Anthropic's statement is relayed by ITdaily; the official docs page was not read for the current default.
