# Director state

The director's working memory for this project, kept current on every change. **After a restart or compaction, read this first**, then PROJECT.md (Decisions, Director rules), then `log.md`. Task notes in `tasks/` are the record of each piece of work; this file is the live view across them.

Last updated: 2026-10-24 by director-project-agent-and-harness (Claude Code desktop session "Duo Director project research"; Duo app not running).

## How workers are started and reached

- **Start:** `claude --bg -n <name> --model <model> --remote-control <name> -- "<brief>"` from the project folder (Geoff, 2026-10-24: not the app's session tool, whose cards need a click on the Mac). `duo2 director start … --background` prints the same command when Duo is running.
- **Model:** Opus 5.5 by default, Fable 5.1 for complex synthesis/strategy/audits, Sonnet 5.5 only for pure execution. Always pass `--model`.
- **Reach:** `SendMessage` to the worker's name (background sessions) or its `local_…` id (app sessions). Log each send in the task's Progress.
- **Hear back:** app sessions send a turn-finished note; background (`--bg`) sessions don't, so a Monitor polls `claude agents --json` for state changes. Re-arm it when it expires.
- **No git worktrees** in this project: committed copies strip third-party full text, so a worktree has incomplete notes. Tell workers to edit the main folder only.

## Workers

| Worker | Id | Started via | Model | Task | State |
|---|---|---|---|---|---|
| Research: product agent and harness | local_8a840fd4-9a6b-4127-b4cc-1a5745fb6fff | app session | Opus 5.5 | [research-product-agent-and-harness](tasks/research-product-agent-and-harness.md) | idle; done, awaiting lint and acceptance |
| Teardown: Ramp Glass | local_dabad5f3-9c2e-4de2-a436-011942aa0ba0 | app session | Opus 5.5 (audited on Fable) | [competitive-teardown-ramp-glass](tasks/competitive-teardown-ramp-glass.md) | idle; done, awaiting lint and acceptance |
| Research: PM agents and jobs to be done | local_84be37e8-1851-4195-9cb6-21c6f8b3ce5b | app session | Opus 5.5 (audited on Fable) | [research-pm-agents-jobs-to-be-done](tasks/research-pm-agents-jobs-to-be-done.md) | idle; done, awaiting lint and acceptance |
| Research: taxonomy of agent runtime patterns | local_2ee18572-3463-43af-b06d-0ee8b5960ba9 | app session | Opus 5.5 | [research-agent-runtime-patterns-taxonomy](tasks/research-agent-runtime-patterns-taxonomy.md) | idle; done (Geoff's section I answers recorded), awaiting lint and acceptance |
| User story mapping: modular PM stories | local_8ebd568e-df86-4849-8b4a-81ae6863d7ca | app session | Opus 5.5 (audited on Fable) | [user-story-mapping](tasks/user-story-mapping.md) | idle; done, awaiting lint and acceptance |
| teardown-shopify-river | 36a0d56f | claude --bg | Opus 5.5 | [competitive-teardown-shopify-river](tasks/competitive-teardown-shopify-river.md) | idle; reports done, to check |
| teardown-stripe-agents | 3d45fbd1 | claude --bg | Opus 5.5 | [competitive-teardown-stripe-knowledge-agents](tasks/competitive-teardown-stripe-knowledge-agents.md) | reopened: Geoff's doc, Trailhead, context-creation-agent hypothesis; report goes to story-and-film |
| research-follow-up-round | a36bf408 | claude --bg | Opus 5.5 | [research-runtime-patterns-follow-up-round](tasks/research-runtime-patterns-follow-up-round.md) | stopped (stalled); its results merged from the worktree by the director; no addendum, no register rows |
| story-and-film | 0bd16627 | claude --bg | Fable 5.1 | [strategy-story-and-explainer-video](tasks/strategy-story-and-explainer-video.md) | working; checkpoints A (outline), B (prototype look), C (Script Doc) go to Geoff |
| sweep-lennys | db172d7f | claude --bg | Opus 5.5 | [research-lennys-newsletter-archive](tasks/research-lennys-newsletter-archive.md) | working; options go to options/contributions/ for the director to merge |
| sweep-dept-of-product | 2c0b10cc | claude --bg | Opus 5.5 | [research-department-of-product-knowledge-series](tasks/research-department-of-product-knowledge-series.md) | working; same |

Stopped: research-product-agent-and-harness-968c23 (6b54ecd9, login expired, never ran); user-story-mapping-1 (613dd94f, duplicate of the card session).

## Queue (what starts when)

1. **Storytelling and film** running. Checkpoints A, B, C are the worker's questions to Geoff in its own session.
2. **Lint** runs per task as Geoff accepts it (LINTING.md); the pre-story sweep was skipped on Geoff's "enough side quests".
3. **Acceptance:** accept/not-yet questions per finished task, then done and archive on his yes.
4. **Push:** local commits since 2ff3417 wait for Geoff's "push".

## Needs Geoff

- Push the local commits since 2ff3417: waiting for his yes.
- Answer the story worker's checkpoints A, B, C in its session.
- Acceptance of finished tasks (after lint).

## Open issues

- Edit is blocked in `claude --bg` sessions (it demands a worktree, since the folder became a git repo). Workers now put register proposals in options/contributions/<task>.md and the director merges them; find the root cause after the film.

- Some Today sections and synthesis rows cite PM-agent notes that the Fable audit relabelled; the lint sweep and the story's claim check cover this.
- Monitor output includes the director's own row; ignore it.

- The follow-up round's worktree is still at .claude/worktrees/followup-round (gitignored, all results merged). Remove it with `claude rm a36bf408` once Geoff agrees.
- Lesson: making the folder a git repo changed `claude --bg` trust and let a subagent create a worktree. Check side effects before changing project infrastructure.
