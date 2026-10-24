---
title: Content exclusion for GitHub Copilot (concept page) and "Content exclusions generally available in Copilot app and CLI"
source_url: https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion
author: GitHub
publisher: GitHub Docs; GitHub Changelog
published: 2026-09-02
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, agent-failure-modes]
relevance: medium
---

## Relevance to the project
Content exclusion is the one Copilot control that limits what the model may read, as opposed to what the agent may do. For a regulated setting it matters which agent surfaces honour it. The concept page and the 2026-09-02 changelog (https://github.blog/changelog/2026-09-02-content-exclusions-generally-available-in-copilot-app-and-cli) show coverage arriving surface by surface, with the cloud agent and partner agents not mentioned at all. The `published` date is the changelog's; the concept page is undated.

## Themes
- enterprise-admin-controls (proposed): repository admins, organisation owners and enterprise owners can configure exclusions; "Content exclusions also apply to Copilot code review on the GitHub website" (concept page).
- agent-failure-modes: "Content exclusion is currently not supported in Edit and Agent modes of Copilot Chat in Visual Studio Code and other editors"; "It's possible that Copilot may use semantic information from an excluded file" via IDE type information or hovers; "content exclusions do not apply to symbolic links (symlinks) and repositories located on remote filesystems" (concept page).

## Key points
- Changelog 2026-09-02: "The GitHub Copilot app and Copilot CLI now respect content exclusion policies configured by enterprise, organization, and repository administrators." Business and Enterprise only.
- The concept page's support table lists chat and agent as supported on GitHub website, Mobile, Copilot app and CLI, but VS Code Edit/Agent, Xcode and Eclipse chat/agent unsupported.
- Neither page mentions Copilot cloud agent or the Claude/Codex partner agents. Older configuration docs (seen via search) said CLI, coding agent and IDE agent mode "do not support content exclusion"; the CLI part is now superseded.

## Could not verify
- Whether the cloud agent or partner agents honour exclusions today. Model-summarised fetch.
