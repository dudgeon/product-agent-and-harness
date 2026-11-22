# Scripts

| Script | What it does | When to run it |
|---|---|---|
| [public-check.sh](public-check.sh) | Checks what would be published, from the git index: no do-not-name terms, no working-note wording, no tracked transcripts, no unstripped `## Full text` sections. Prints `public check: ok` and exits 0 when clean. | After staging, before every commit: `bash scripts/public-check.sh`. Read its output bare; piping it through `head` or `tail` hides a FAIL. |
| [strip-full-text.py](strip-full-text.py) | Replaces the body of each `## Full text` section in a source note with a pointer to `source_url`, reading stdin and writing stdout. The commit filter applies the same strip. | Rarely by hand; to see what a note's public copy will hold, run `python3 scripts/strip-full-text.py < research/sources/<slug>.md`. |

The research library has its own build script, [research/build.py](../research/build.py) (see [research/README.md](../research/README.md)).
