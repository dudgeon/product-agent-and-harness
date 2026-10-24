# Research library

Every agent in this project files its research here, whatever task it's working on. Task folders (`tasks/<slug>/`) hold task deliverables (briefs, teardown summaries); the sources and themes those deliverables draw on live here, and the deliverables link to them.

```
research/
  README.md        this rule
  INDEX.md         one line per source note (append-only)
  THEMES.md        the theme register: each theme, what it means, which sources support it
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
  - `## Relevance to the project`: 2–5 sentences on why this matters for the product agent and harness project (research, concepts / strategy deck, prototypes, teardowns), and which open question it bears on.
  - `## Themes`: each theme it supports, one bullet each, with the specific claim or evidence and a timestamp, quote location or section.
  - `## Key points`: the substance, in your words, with timestamps or section refs.
  - `## Notable quotes` (optional): short verbatim quotes with timestamps.
  - `## Full text`: the full transcript or post text, verbatim, when the task asked for it. Long transcripts may instead go in `sources/<slug>.transcript.md` (same `source_url` at the top) and be linked from here.
  - `## Could not verify` (optional): what you couldn't retrieve or confirm.

## 2. `INDEX.md`: one line per source, append-only

`- [<title>](sources/<slug>.md) · <type> · <published> · relevance <high|medium|low> · <one-line gist> · <source_url>`

Append your line; never rewrite or reorder others' lines.

## 3. `THEMES.md`: the theme register

Themes are the recurring ideas pulled out across sources. Each theme is a section:

```markdown
## <theme-slug>: <Theme name>
<One or two sentences: what the theme is, and why it matters to the project.>
- [<source title>](sources/<slug>.md): <the specific evidence, one line> (<filed_by task>)
```

- **Reuse before inventing.** Read THEMES.md first; use an existing theme slug if it fits. Add a new theme only for a genuinely new idea.
- **Add evidence by appending a bullet** under the theme. Don't rewrite another agent's theme description or bullets; if you think one is wrong or two themes should merge, say so in your report to the director instead.
- Several agents write here at once: make small appends with Edit, re-reading the file just before each edit.

## 4. Task deliverables

Briefs and summaries stay in the task's own folder and link to the source notes (`../../research/sources/<slug>.md`) instead of copying their content. Sources already saved in a task folder are moved here and the brief's links updated.
