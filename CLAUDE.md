# CLAUDE.md

Guidance for anyone, person or Claude session, working in this repository. It points to the files that hold the rules rather than repeating them; when this file and one of those disagree, the other file wins.

## What the project is

Research and strategy on **agent harnesses for product work**: how product managers, and anyone else in a product role, could work with agents in sessions that are persistent and shareable rather than local and private, with common product jobs handed to standardised task agents, without being tied to one vendor's tool. The reference job is **intent shaping**: turning an opportunity into a spec that coding agents can act on, in a regulated setting where audit matters.

**The deliverable is a menu, not an answer.** The work builds a **menu of options split by dimension**, with the **key questions** that would decide among the options in each, in [options/DIMENSIONS.md](options/DIMENSIONS.md). It is not a PRD for one implementation. Don't pick a winner; a lean is fine when the evidence and what would change it are written down. Dimensions cover runtime and architecture choices and user and product choices (which users, which jobs, what outcome, how adoption happens).

**The story is told through ambition and opportunity.** Coding is already scaling; the opportunity is to scale problem discovery, intent definition and shaping alongside it. Write it as optimistic and opportunistic, not as "keeping up with faster coding" or fixing a problem.

[README.md](README.md) is the newcomer's tour: what has been found, and where each deliverable is.

## Layout

| Path | What lives there | Rules |
|---|---|---|
| [research/](research/) | The shared research library: one note per primary source in `sources/`, one theme file per piece of work in `themes/`, and the generated `INDEX.md` and `THEMES.md` | [research/README.md](research/README.md) |
| [options/](options/) | The options register, [DIMENSIONS.md](options/DIMENSIONS.md) | [options/README.md](options/README.md) |
| [tasks/](tasks/) | One folder per piece of work (`tasks/<slug>/`), holding only that work's deliverables: briefs, summaries, syntheses, lifecycle maps and their `.build.py` generators, standalone HTML pages | Deliverables link to source notes; they don't copy them |
| [films/](films/) | The rendered explainer films shown on the site | Draft films carry a "Draft · not yet reviewed" mark |
| [scripts/](scripts/) | Repository checks and filters | [scripts/README.md](scripts/README.md) |
| [index.html](index.html) | The GitHub Pages site, served from `main` at `/` ([dudgeon.org/product-agent-and-harness](https://dudgeon.org/product-agent-and-harness/)) | Links into `tasks/` and `films/` by relative path; keep them working when files move |

Every date in the repo is 2026 unless it says otherwise.

## Working rules

1. **File all research in `research/`**, exactly as [research/README.md](research/README.md) says: one note per primary source (check `INDEX.md` for an existing note first), `source_url` always, an evidence label (first-party, vendor claim, independent, anecdote), and themes written only to your own `research/themes/<task-slug>.md`.
2. **Rebuild the library after filing:** `python3 research/build.py`, and fix every warning it prints for your notes (the target is 0). `INDEX.md` and `THEMES.md` are generated; never edit them by hand. `python3 research/build.py --check` reports without writing.
3. **Add options, don't converge.** Append options, evidence rows and key questions to `options/DIMENSIONS.md` with small edits, per [options/README.md](options/README.md); every option links to a source note and every dimension you touch ends with key questions.
4. **Shared files get small edits only.** Several sessions may write at once: re-read just before each edit, and never rewrite a file another piece of work also writes.
5. **The repository is public when pushed.** Before any commit, stage your own paths and run `bash scripts/public-check.sh`, read bare (don't pipe it through `head` or `tail`, which hides a FAIL); it must print `public check: ok`. Don't commit or push unless you have been asked to.
6. **Third-party text stays out of the public copy.** Verbatim transcripts go in `research/sources/<slug>.transcript.md` (gitignored), full post text under a `## Full text` heading (stripped on commit by a git filter). Each note links to its original instead.
7. **Not everything in the folder is public.** Working notes used to run the project are local only. Before writing about, linking to or moving a file, check `.gitignore` and `.git/info/exclude`; don't describe local-only files in public documents. Links to them are removed from the committed copy.
8. **No git worktrees.** The commit filter strips text from the committed copy, so a worktree checks out incomplete notes. Edit the main folder.
9. **Numbers come from source notes**, with vendor and first-party claims labelled as such.

If a `CLAUDE.local.md` exists beside this file, read it too: it holds the local working arrangements.
