---
title: "docx SKILL.md"
source_url: https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md
author: Anthropic
publisher: GitHub (anthropics/skills)
published: 2026-07-17
retrieved: 2026-10-25
type: other
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, skill-standards]
relevance: medium
---

## Relevance to the project
The low-freedom end of Anthropic's own skill set: a short (91-line) file that is mostly exact commands and format gotchas, with validation scripts as gates. It shows that even Anthropic's "explain the why" house style turns into fixed commands and schema checks when the artifact is a file format with hard rules. For PM work the analogue is anything with a machine-checkable shape (ticket fields, a PRD schema, a CSV export).

## Themes
- rules-vs-judgment-encoding: exact command sequence for edits: unpack, `merge_runs.py`, edit XML "in place — do NOT reformat or pretty-print", then `validate.py out.docx --original doc.docx` with XSD checks and `--auto-repair` (section "Editing existing documents").
- skill-standards: tracked-change edits are verified by script: `--author` reports "any text you changed without a <w:ins>/<w:del> around it, which is easy to do by accident and invisible in the accepted view" (Tracked changes).

## Key points
- Classification: control flow fixed sequence per job (create via docx-js, edit via unpack-edit-validate-pack); gates = scripts (schema validation, render to PDF to verify); standard form = gotcha list; stance = do.
- Reasons still accompany rules (why runs must be merged: Word splits text across many runs so a visible phrase is often not a contiguous string). Even the rigid file explains its rules.
- A "Verify the output" step converts to PDF so the model can check rendering.

## Could not verify
- No eval data in the file.
