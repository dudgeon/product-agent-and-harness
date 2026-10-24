---
title: "Cloud-origin agents have no 'Move to Machine' option (Cursor forum)"
source_url: https://forum.cursor.com/t/cloud-origin-agents-have-no-move-to-machine-option-in-agents-window-glass-cant-hand-off-to-local/162470
author: jbescoyez (user); reply from Cursor staff
publisher: Cursor community forum
published: 2026-06-04
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, shared-persistent-sessions]
relevance: medium
---
## Relevance to the project
Independent user evidence that session portability between cloud and local is asymmetric in a shipping product: local to cloud works; cloud-origin to local needs a matching local agent or a fresh chat that loses history. Same shape as Claude Code's one-way teleport. Supports treating handoff as a first-class design requirement.

## Themes
- harness-portability: staff (2026-06-05) called cloud-to-local for cloud-origin sessions a 'known limitation', 'not being actively built out right now'; workaround is a local agent on the same repo or continuing in the cloud
- shared-persistent-sessions: related thread reports local to cloud handoff failing for GitLab repos with 'Background composer not found' (search snippet only)

## Key points
- Cursor 3.7 changelog (via search snippet) says environments are captured in reusable snapshots, shareable by committing .cursor/environment.json; cloud subagents each get their own VM and branch.
- Alternative without history: git fetch the agent's branch and start a fresh chat.

## Could not verify
- Cursor docs and changelog not read directly; GitLab report is from a search snippet.
