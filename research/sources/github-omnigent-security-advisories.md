---
title: omnigent-ai/omnigent security advisories and policy-bypass issues
source_url: https://github.com/omnigent-ai/omnigent/security/advisories
author: Omnigent maintainers (Databricks); reporters include external researchers and an autonomous security agent
publisher: GitHub
published: 2026-10-14
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, policy-enforcement-fail-open, shared-persistent-sessions, identity-delegation]
relevance: high
---

## Relevance to the project
The strongest evidence found on how Omnigent's governance layer behaves under attack. The maintainers published 13 advisories in four months (4 critical), and several reproduced issues show policies silently failing open: when the policy server errored, when a harness ran shell inside its own process, for sub-agents, and for unparsed shell forms. For a regulated setting this is the central question about any "policy above the harness" design: enforcement is only as good as the seam it hooks, and the defaults were allow. All were fixed or closed quickly, which is itself a responsiveness signal. Published date is that of the latest advisory.

## Themes
- [[policy-enforcement-fail-open]] (proposed): #536 (2026-06-17, P0, closed next day): native-harness PreToolUse/PostToolUse hook returned exit 0 with no output on every error path, so a slow, erroring or unreachable policy server silently disabled all DENY/ASK for Claude Code and Codex. #5455 (2026-08-25, P0, v0.10.0): the `blast_radius` policy was enforced for `claude-native` but silently not for the direct `codex` harness, whose shell runs inside the Codex process; a `git push --force` succeeded with no error or policy event. #7316 (2026-09-13, P1): sub-agent sessions with no own policies short-circuited to ALLOW and skipped the root session's inherited policies. #3557 (2026-07-30, P0): shell-policy gates bypassed by wrappers with flags (`sudo -u`, `env -i`, `command -p`). #3852: built-in write policies missed Claude Code's `MultiEdit`/`NotebookEdit`.
- [[meta-harness]]: the interception seam differs per harness (hook subprocess for native CLIs, tool_call events for SDK harnesses), so identical policy produces different outcomes by harness (#5455).
- [[shared-persistent-sessions]]: GHSA-rqfc-q7j9-5v59 (critical, 2026-10-13) session imports could use another user's host without authorisation.
- [[identity-delegation]]: GHSA-x6v6-fg8x-997h (critical, 2026-10-14) default header authentication trusted a client-controlled `X-Forwarded-Email`, enabling remote user impersonation.

## Key points
Advisories listed via the GitHub API on 2026-10-24 (ID, severity, published, summary):
- GHSA-jrrm-9hc7-2v3h, critical, 2026-06-29: shared agent bundle overwrite leads to authenticated runner RCE.
- GHSA-756x-9hf6-q4h4, high, 2026-06-29: uploaded agent bundle allows runner RCE via Python callable tools.
- GHSA-p8rw-8qj3-hf33, high, 2026-06-29: unvalidated `os_env.cwd` gives arbitrary host filesystem access.
- GHSA-7mqg-cx4g-x2rf, high, 2026-06-29: guardrail policy bypass, shell parser fails open (CWE-184); CVE-2026-62676.
- GHSA-598r-29w2-g93q, critical, 2026-09-16: per-terminal `os_env.cwd` bypasses workspace guard, unconfined host shell.
- GHSA-q5jc-8hqr-9hm4, high, 2026-09-16: YAML function policy key bypasses handler allowlist, import-and-call RCE.
- GHSA-p5x3-3gqh-x44g, high, 2026-09-16: sub-agent `os_env.cwd` escapes workspace containment.
- GHSA-h6vq-3549-mppq, high, 2026-10-13: git commands can bypass repository and branch policies.
- GHSA-m3m2-42jg-grrv, high, 2026-10-13: shell commands can bypass configured agent policies.
- GHSA-v3vj-mch3-x6c2, high, 2026-10-13: sandbox launcher isolation failure permits host-level code execution.
- GHSA-jw77-57v9-jmcm, high, 2026-10-13: uploaded source tools execute with runner privileges.
- GHSA-rqfc-q7j9-5v59, critical, 2026-10-13: session imports use another user's host without authorisation.
- GHSA-x6v6-fg8x-997h, critical, 2026-10-14: header auth trusts client `X-Forwarded-Email`.
- Also issue #157 (2026-06-15, closed 2026-06-17): authenticated host RCE via unvalidated `model_override` on PATCH injected into Codex `config.toml` `auth.command`.
- Pattern: policy and bypass bugs reported mostly by outside contributors (author association NONE/CONTRIBUTOR), triaged P0/P1 and closed in 1 to 11 days. Fixes moved toward deny-by-default (v0.3.0 for the shell parser).
- An issue search on 2026-10-24 returned 23 issues matching "policy bypass", 125 matching "security"; these are text matches, not confirmed vulnerabilities.

## Could not verify
- Whether any advisory was exploited; no incident reports found.
- Whether the Databricks-managed Beta shared each vulnerability (the managed version disallows custom Python policies, which removes some RCE paths).
