---
title: Enterprise managed settings (GitHub Copilot reference) and "MCP allowlists in enterprise managed settings"
source_url: https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/enterprise-administrators/enterprise-managed-settings
author: GitHub
publisher: GitHub Docs; GitHub Changelog
published: 2026-08-06
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, harness-portability, skill-supply-chain-security]
relevance: high
---

## Relevance to the project
Copilot's client-side policy file (`managed-settings.json`) for the Copilot CLI, VS Code and the GitHub Copilot app. Its key names and semantics (`permissions.allow/ask/deny`, `disableBypassPermissionsMode`, `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`, `allowedMcpServers`/`deniedMcpServers` with name/URL/command matchers, `sandbox`, OTel `telemetry`) closely mirror Claude Code's managed settings: evidence that the admin-policy vocabulary for local agent harnesses is converging, though the files are still per vendor. Date anchor: the changelog dated 2026-08-06 (https://github.blog/changelog/2026-08-06-mcp-allowlists-in-enterprise-managed-settings); the reference page itself is undated. Also read: the public-preview registry enforcement page (https://docs.github.com/en/copilot/reference/enterprise-administrators/mcp-allowlist-enforcement).

## Themes
- harness-portability: key names match Claude Code's (`enabledPlugins` with `PLUGIN@MARKETPLACE`, `strictKnownMarketplaces` where "An empty array means complete lockdown", `allowedMcpServers`, `deniedMcpServers`, `permissions.deny/ask/allow`): convergent vocabulary, separate files (reference page).
- skill-supply-chain-security: MCP matchers `serverUrl` (wildcards, canonicalised "to prevent evasion"), `serverCommand` ("exact command and arguments"), `serverName` (user label, "a convenience, not a security control"); "Policies fail closed"; "a server must pass every layer" (changelog).
- enterprise-admin-controls (proposed): delivered from `copilot/managed-settings.json` in the source org's `.github-private` repo (server-managed, with enterprise-team overrides for keys marked overridable), or by MDM, Windows registry, macOS managed preferences.

## Key points
- Precedence: `allowedMcpServers` and `permissions.allow` intersect across sources; `deniedMcpServers` unions; deny > ask > allow; "A managed ask rule can't be satisfied by bypass mode."
- `permissions.disableBypassPermissionsMode` suppresses `--yolo`/`--allow-all`, VS Code global auto-approve and the app's "Allow all".
- `sandbox` sets minimum local sandbox restrictions (commands, filesystem, network, credentials, local MCP/LSP servers) with `failIfUnavailable`; older clients are blocked from Copilot when `sandbox` is set (minimums VS Code 1.141.0, CLI 1.0.93, app 1.1.26).
- `forceRemoteSettingsRefresh` makes clients fail closed until a fresh server fetch succeeds.
- `telemetry` routes OTel to the customer's collector; `capture` of `prompts`, `responses`, `toolArguments`, `toolOutput` defaults to false: content capture is opt-in.
- MCP allowlists are "currently enforced on the GitHub Copilot app, Copilot CLI and VS Code" (changelog). The older registry-based "Registry only" policy is public preview, "based only on server name/ID matching, which can be bypassed by editing configuration files", and not supported for Copilot cloud agent (enforcement page).
- No managed `hooks` key is defined.

## Could not verify
- Cloud-agent and JetBrains support per key appears only in a table the fetch did not render. Model-summarised fetch.
