---
title: Managed configuration (Codex / ChatGPT enterprise docs)
source_url: https://learn.chatgpt.com/docs/enterprise/managed-configuration
author: OpenAI
publisher: learn.chatgpt.com (redirected from developers.openai.com/codex/enterprise/managed-configuration)
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, harness-portability, skill-supply-chain-security, identity-delegation]
relevance: high
---

## Relevance to the project
This is OpenAI's admin-enforced policy layer for Codex (CLI, desktop app, IDE extension, cloud-managed paths): the closest analogue to Claude Code managed settings and to Copilot's enterprise `managed-settings.json`. For a regulated internal deployment it answers what a central owner can actually force on local agent runtimes (approvals, sandbox, network, MCP, hooks, plugin marketplaces), how it is delivered (cloud bundle per user/group, MDM, system file) and where enforcement stops. It bears on the governance-control-plane and capability-distribution-trust dimensions and on the "can governance be uniform across harnesses" question.

## Themes
- enterprise-admin-controls (proposed): two layers, "Requirements constrain what users and tasks can do. Defaults provide starting values." Requirements are delivered from Admin Console > Agent security with a "Workspace default" and "Overrides" for users, groups or roles, or by `/etc/codex/requirements.toml`, `%ProgramData%\OpenAI\Codex\requirements.toml`, or macOS MDM `requirements_toml_base64` (sections 1-3).
- enterprise-admin-controls: fail-closed on fetch: with no valid cache and a failed fetch the client "returns an error rather than silently starting without the cloud-managed requirements layer" (section 2).
- skill-supply-chain-security: `[marketplaces] restrict_to_allowed_sources = true` with `allowed_sources` of type `git`, `host_pattern` or `local`; the curated OpenAI catalog must be explicitly allowed; applies to ChatGPT/Codex desktop and Codex CLI, not web or mobile plugin use. Skills are not a managed key on this page.
- identity-delegation: `allowed_login_methods` and `allowed_chatgpt_workspaces` (workspace UUID allowlist, also applied to Codex access tokens) are local-only keys, ignored in cloud-managed requirements.
- harness-portability: the policy vocabulary (approval policies, permission profiles, `[rules] prefix_rules`, `[hooks]`, `[features]`) is Codex-specific; nothing here travels to Claude Code or Copilot.

## Key points
- Enforceable keys (section 4): `allowed_approval_policies` (omitting `never` blocks `--ask-for-approval never`); `allowed_approvals_reviewers` (`["auto_review"]` forces automatic review); `guardian_policy_config`; `allowed_sandbox_modes` (legacy) and `allowed_permission_profiles` / `default_permissions` (Codex 0.138.0+; 0.137.0 and earlier ignore them); `[permissions.filesystem] deny_read`; per-host `[[remote_sandbox_config]]`; `allowed_web_search_modes`; `[rules] prefix_rules` with `prompt` or `forbidden` only (most restrictive wins).
- MCP allowlist by identity, not just name: stdio servers match `command` or `executable` + ordered `args`; HTTP servers match `url`; `exact`, `prefix` or full-value `regex`; "If `mcp_servers` is present but empty, the local client disables all MCP servers." Structured rules do not inspect `cwd`, `env` or `env_vars`. Plugin MCP servers are addressed as `plugins.<plugin>.mcp_servers.<server>`.
- `[features]` can turn off `hooks`, `browser_use`, `computer_use`, `apps`, `plugins`, `in_app_browser` and others; conflicting user writes are rejected.
- Hooks: `[hooks]` with `managed_dir`; `allow_managed_hooks_only = true` skips user, project, session and plugin hooks. The runtime enforces hooks but does not distribute the scripts (use MDM). A `PreToolUse` callback error, timeout or malformed response "can fail the hook without blocking the tool" (fail-open hooks).
- Network: `[experimental_network]` (experimental, limited Windows support) with domain allow/deny, deny beats allow; "A deny-only policy does not implicitly allow the rest of the internet."
- Residency: `enforce_residency` in a cloud policy disables "Allow local computer access" for Work; the page says this key does not itself configure residency.
- Models: model pins are defaults, not enforced requirements; page notes GPT-5.5 retires from Codex with ChatGPT sign-in on 2026-10-14.
- Group targeting: "Test policies" shows which policies match but not the merged result or client enforcement; "Managed configuration does not grant a workspace seat or feature access."
- Precedence (low to high): system file, Agent Security cloud bundle, legacy `managed_config.toml` fields, macOS MDM. Managed values override CLI `--config` flags.
- A running cloud task "may not immediately use a changed policy".

## Could not verify
- No publish date on the page; content retrieved through a model-summarised fetch, so verbatim wording should be rechecked before quoting in the deck.
- Whether requirements are enforced for Codex cloud tasks in the same way as local clients (page says cloud environments have their own tabs; internet-access page says managed command allowlist and proxy apply on "supported managed Codex Cloud paths").
- No independent test of bypass resistance of the local requirements layer found.
