# Research library

Every agent in this project files its research here, whatever task it's working on. Task folders (`tasks/<slug>/`) hold task deliverables (briefs, teardown summaries); the sources and themes those deliverables draw on live here, and the deliverables link to them.

```
research/
  README.md        this rule
  build.py         generates INDEX.md and THEMES.md; run it after you file
  INDEX.md         GENERATED from source-note frontmatter (never edit)
  THEMES.md        GENERATED from themes/ (never edit)
  themes/          one file per task: <task-slug>.md, written only by that task
  sources/         one note per primary source
```

## 1. One note per primary source: `research/sources/<slug>.md`

A primary source is anything you read or watched: a video, a podcast, an X post or thread, an article, a paper, a docs page, a company write-up, a report.

- **Slug:** `<publisher-or-author>-<short-title>`, lowercase, hyphens, e.g. `ramp-introducing-glass`, `x-sebgoddijn-glass-article`, `lenny-podcast-geoff-charles`. Before writing, check `sources/` and `INDEX.md`: if a note for the same source exists, add to it rather than making a second one.
- **Frontmatter (all required unless marked):**

```yaml
---
title: <the source's own title>
source_url: <the link to the original; required, never omitted>
author: <person or organisation>
publisher: <channel, site, account>
published: <YYYY-MM-DD, or "unknown">
retrieved: <YYYY-MM-DD>
type: video | podcast | x-post | article | paper | docs | report | other
evidence: first-party | independent | vendor-claim | anecdote   # what kind of evidence this is
filed_by: <task slug that filed it>
themes: [<theme-slug>, ...]      # slugs from THEMES.md
relevance: high | medium | low
---
```

- **Body, in this order:**
  - `## Relevance to the project`: 2–5 sentences on why this matters for the product agent and harness project (research, concepts, prototypes, teardowns), and which open question it bears on.
  - `## Themes`: each theme it supports, one bullet each, with the specific claim or evidence and a timestamp, quote location or section.
  - `## Key points`: the substance, in your words, with timestamps or section refs.
  - `## Notable quotes` (optional): short verbatim quotes with timestamps.
  - `## Full text`: the full transcript or post text, verbatim, when the task asked for it. Long transcripts may instead go in `sources/<slug>.transcript.md` (same `source_url` at the top) and be linked from here.
  - `## Could not verify` (optional): what you couldn't retrieve or confirm.

## 2. `INDEX.md` is generated

Don't edit it. Your note's frontmatter (title, type, published, relevance, source_url) and the first sentence of its "Relevance to the project" make its index line. After filing, run `python3 research/build.py`; fix any warning it prints for your notes.

## 3. Themes: write only your task's file

Themes are the recurring ideas pulled out across sources. `THEMES.md` is **generated**; never edit it. Each task writes only `research/themes/<task-slug>.md`, so no agent can overwrite another's work:

```markdown
## <theme-slug>: <Theme name>
<One or two sentences: what the theme is, and why it matters to the project. Only when your task introduces the theme.>
- [<source title>](sources/<slug>.md): <the specific evidence, one line> (<filed_by task>)
```

- **Reuse before inventing.** Read the generated THEMES.md first; use an existing slug if it fits (add your bullets under the same `## slug: Name` heading in your own file, without a description).
- Merges, renames and splits of themes across tasks are done only in a separate consolidation pass, one at a time.
- Then run `python3 research/build.py`.

**Shared files, generally:** never rewrite a file another agent also writes (no Write tool, no script that rewrites it whole). Use small Edits on the current version. `options/DIMENSIONS.md` is the one shared hand-edited file: append only, with Edit.

## 4. Task deliverables

Briefs and summaries stay in the task's own folder and link to the source notes (`../../research/sources/<slug>.md`) instead of copying their content. Sources already saved in a task folder are moved here and the brief's links updated.
