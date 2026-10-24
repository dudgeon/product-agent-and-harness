---
title: omnigent-ai/omnigent (README, docs site and open issues)
source_url: https://github.com/omnigent-ai/omnigent
author: Databricks AI team, Neon and contributors
publisher: GitHub / omnigent.ai
published: 2026-10-24
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness, harness-portability, shared-persistent-sessions]
relevance: high
---

## Relevance to the project
The code and docs behind the Omnigent claim, plus the live issue tracker, which is the nearest thing to independent evidence on how it behaves. Shows a broad harness list, a runner/server split, many sandbox providers, and real alpha-stage reliability and sharing-security issues.

## Themes
- [[meta-harness]]: README tagline 'The open-source meta-harness for all your AI agents'; runner wraps an agent in a uniform session, server adds policies and shared history.
- [[harness-portability]]: harnesses listed: Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, Antigravity, GitHub Copilot, Devin, Kiro, Grok Build, Goose, OpenClaw, plus custom YAML agents (README + docs).
- [[shared-persistent-sessions]]: live sharing, `omnigent attach` co-driving, `run --fork`; issue #11413 (2026-10-23, P1) says session sharing does not separate chat access from host access to terminals and files.

## Key points
- Alpha badge; Apache-2.0; about 11k stars, 1.8k forks, 892 open issues, 5,377 commits on main at retrieval (README page figures).
- Architecture per docs: a runner wraps any agent in a uniform session and can run on your machine, Modal or Daytona; a server adds policies and shared history; clients are terminal, web, native and mobile apps, REST API. Server storage Postgres/SQLite and OIDC per Atlan's explainer.
- Policies at three levels: server-wide, per-agent, per-session. Agent definitions are short YAML files (prompt, Python/MCP tools, sub-agents). Built-in agents: Polly (coding orchestrator), Debby (model debate).
- Sandbox providers listed: Modal, Daytona, Blaxel, Islo, E2B, Gensee, CoreWeave, Kubernetes, OpenShell, Boxlite, microsandbox, Databricks.
- Requires Python 3.12+, Node 22+, tmux (bubblewrap on Linux). Terminal agents run inside tmux panes wrapped by the web UI (Goose/Hermes/Devin native TUI in a pane). `omnigent import` converts local Claude Code/Codex transcripts into Omnigent sessions.
- Limitations stated: Windows degraded (no tmux wrappers or sandboxing); telemetry on by default; Grok Build and Devin depend on vendor CLI logins.
- Open issues on the first page (all opened 2026-10-23/24): OIDC login failing with Microsoft Entra ID (#11417); sessions stuck 'running' or 'failed' after turns end (#11418, #11437, #11484); auth failures with opaque errors (#11470, #11488); terminal double-reply bugs (#11497); users cannot use their own ChatGPT/Claude subscription in managed sandboxes (#11493); side chats not allowed on a shared session on another user's host (#11414). These are open issues, not a failure rate.

## Could not verify
- Which harnesses are fully supported vs community-maintained (Atlan reports tiers) was not confirmed on the repo itself.
- Last commit date not shown on the fetched page.

## Follow-up (2026-10-24)
Added by research-runtime-patterns-follow-up-round, read-only via the GitHub API on 2026-10-24. These are adoption and activity signals, not quality measures.

- **Stars:** 11,020 stars, 1,800 forks. Repo created 2026-06-11. Earlier data points from other sources: about 8,000 at the Berkeley RDI summit (early August, second-hand) and about 10.8k on 2026-10-12 ([SSD Nodes](ssdnodes-omnigent-multi-agent-harness.md)). Growth has slowed to roughly 200 stars in the last two weeks. The stargazer timeline API was not available, so the trend rests on these three points.
- **Release cadence:** 22 releases, from v0.2.0 (2026-06-19) to v0.19.1 (2026-10-21), roughly weekly, none marked pre-release. Still 0.x, and minor releases have broken documented commands (SSD Nodes).
- **Commit activity:** 200 to 500 commits a week in every week since launch, with 414 in the week of 2026-10-18. Activity is not tapering.
- **Issues and PRs:** 2,576 issues in total (892 open), 5,369 merged PRs, 1,499 open PRs. Issues created per month: June 311, July 381, August 574, September 635, October 1–24 675. 321 merged PRs are authored by `omni-resolve-agent[bot]`. A bot triages and prioritises issues, and much of the maintenance is agent-assisted.
- **Who files issues:** of about 1,350 issues updated since 2026-09-24, 377 distinct authors, 264 of them with no prior association to the repo. In October, about half of new issues came from seven core accounts and half from everyone else.
- **Contributors:** 281 contributor accounts. The top ten by commits (PattaraS, serena-ruan, TomeHirata, dbczumar, yaoharry, fanzeyi, dhruv0811, daniellok-db, SabhyaC26, btli) are Databricks or MLflow staff, judged by profile company fields, `-db` handles and known MLflow maintainers; this is our inference, not a declaration. hzub, a consultant with 181 commits, is the largest apparently external contributor. Profiles also list DoorDash, Apple, Shopify, IBM, Microsoft and Carnegie Mellon, each with 4 to 17 commits; employer fields do not show the work was sponsored. Zaharia's launch-week claim that about half of merged PRs came from outside Databricks ([Latent Space](latent-space-databricks-zaharia-xin.md)) does not describe the commit distribution now.
- **What issues are about now (2026-10-23/24 sample of about 40 open issues):** most concern the Claude-native and Codex-native terminal bridges: tmux pane state, stuck "running" sessions, auth failures that report only an exit status, outdated Claude Code diagnosis, double replies from the web terminal. Others ask for sharing and identity controls (#11411–#11414), Windows parity, Entra ID OIDC (#11417), Unity Gateway request tagging and span metadata (#11381, #11382), and the subscription broker (#11493). Harness components carry tier labels (`comp:harness-t1`, `comp:harness-t2`). The upkeep cost of tracking vendor CLIs is visible in this volume.
- **Security:** 13 published advisories, 4 of them critical, and several reproduced policy fail-open bugs. See [github-omnigent-security-advisories](github-omnigent-security-advisories.md).
- **Identity and audit gaps raised by evaluators:** see [github-omnigent-identity-audit-issues](github-omnigent-identity-audit-issues.md).
- **Discussions:** 12 in total. The project runs on its issue tracker.
