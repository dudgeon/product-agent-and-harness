# Linting pass

After every task completes, the director starts a **lint worker** (Opus 5.5) scoped to that task. Its job is to keep the project's shared knowledge coherent as findings land: reconcile, link, and propose what should happen next. It does not do new research beyond a quick check, and it does not start work.

One lint worker runs at a time. It is the only agent allowed to edit across other tasks' theme files and the register's structure, so two lint passes must never overlap.

## Input

- The finished task's note (`tasks/<slug>.md`: Request, done_when, Progress) and its deliverables folder.
- Everything the task filed: its source notes (`filed_by: <slug>`), its theme file (`research/themes/<slug>.md`), and its rows in `options/DIMENSIONS.md`.
- The rest of the project, read for context: `PROJECT.md`, `research/`, `options/`, other tasks' deliverables.

## Checklist

1. **Library integrity.** Run `python3 research/build.py --check`. Fix what it reports for this task's notes: missing frontmatter, missing `source_url`, a theme in frontmatter with no evidence. Find duplicate notes (the same URL or the same source under two slugs): merge them into one, repoint links, and record the merge in this pass's log. Then run `python3 research/build.py` to rebuild `INDEX.md` and `THEMES.md`.
2. **Reconcile findings.** Compare the task's findings with what other tasks found. Where they agree, link them. Where they conflict (different numbers for the same thing, a claim that another task's audit corrected, a newer source superseding an older one), record the conflict and which is better supported, and fix the weaker side where the evidence is clear. Otherwise list it as an open conflict.
3. **Themes.** Merge themes that are the same idea under two slugs: keep one slug, move the bullets, and note the alias. Split a theme that has become two ideas. Add a theme where several tasks' findings share an idea no theme names yet. Keep each description to one or two sentences.
4. **Options register.** Check the task's options and key questions sit in the right dimension. Merge duplicate options. Every option must have evidence; every dimension it touched must end with key questions. Add "see also" links between dimensions the task connected. Propose new dimensions, merges and splits, but don't apply structural changes (those go to the director to bring to Geoff).
5. **Cross-task links.** Add `Related:` links in task notes and "see also" lines in deliverables where tasks bear on each other: a teardown that supports a taxonomy pattern, a story that depends on a dimension, a finding that answers another task's open question.
6. **Follow-ups.** List the logical next steps the findings raise:
   - a follow-up for an existing worker (which worker, and the exact message to send);
   - a new task (title, the words that raised it, and where it was found);
   - a question only Geoff can answer.

   Don't send or start anything yourself. Write them in the log; the director files new tasks as `status: suggested`, sends follow-ups, and brings questions to Geoff.
7. **Public-safety check.** Make sure nothing in the task's files matches a term in `.public-check-terms` (a local, untracked list of names that must not appear) or contains private material, and that verbatim third-party text sits only under `## Full text` or in `*.transcript.md` files (both stay out of the public repo).

## Output

- `tasks/<slug>/lint-<date>.md`: what was checked, what was changed (file by file), the conflicts, and the follow-ups.
- A dated line in the task note's `## Progress`.
- A final report to the director: the changes in a few lines, then the follow-ups and questions for Geoff, each ready to act on.
