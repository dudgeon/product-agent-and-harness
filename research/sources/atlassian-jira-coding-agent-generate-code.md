---
title: Generate code from a work item in Jira (Jira Coding Agent)
source_url: https://support.atlassian.com/rovo/docs/generate-code-from-a-work-item-in-jira/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [agent-factory-sdlc, opportunity-to-code-chain, human-review-gates, identity-delegation, task-context-isolation]
relevance: high
---

## Relevance to the project
This is the authoritative doc for the "write the code" step in Atlassian's stack: the Jira Coding Agent (the renamed Rovo Dev in Jira) takes a Jira work item and returns a draft pull request linked back to it. It states exactly what the agent can read and write and what comes back, which the lifecycle map needs. It also shows a split worth noting for the harness: run by hand, the agent can read Confluence through the user's permissions; run from automation, it cannot.

## Themes
- `agent-factory-sdlc`: start from the work item's "Agent sessions" section ("Start work") or "assign a work item to Jira Coding Agent"; one session per selected repository (Generate code from a work item).
- `opportunity-to-code-chain`: the agent "generates code based on the work item and any extra context you added"; including the work item key in the commit message or PR description links the PR to the work item automatically (Create a pull request).
- `human-review-gates`: "It will always create a draft pull request on your behalf"; "It doesn't merge pull requests" (What can the Jira Coding Agent access?).
- `identity-delegation`: "acts strictly on behalf of the initiating user"; the user is listed as PR author and commit author; "It is an autonomous agent and may perform these actions without asking for confirmation each time."
- `task-context-isolation`: clones only the selected repository into a sandbox that only the initiating user can access; sessions expire after 7 days of inactivity.

## Key points
- **Documented (Before you begin):** needs AI features on in the space, Rovo credits, a Standard or Premium plan, and Bitbucket Cloud or GitHub Cloud connected.
- **Documented (Generate code):** inputs are the work item, the chosen repo(s), and a free-text or saved prompt "from the repository" (code standards, file paths, examples). A Settings panel configures code and environment.
- **Documented (Edit generated code):** a chat panel to ask for changes; the user can highlight lines and edit diffs directly, then "Create pull request" with a commit message.
- **Documented (access section):** the agent can create, read, update and search (not delete) in Jira and Confluence as the user; read/write only the selected repository; run Bash or PowerShell in the sandbox. It "doesn't connect to third-party data sources using Model Context Protocol (MCP)."
- **Documented, related page** ([What is the Jira Coding Agent?](https://support.atlassian.com/jira-software-cloud/docs/what-is-the-jira-coding-agent/)): "uses your work item and your team's knowledge directly from Jira, Confluence, your codebase, and more"; sandbox can be given secrets and environment variables; consumes Rovo credits.
- **Documented, related page** ([Work with Jira Coding Agent in automations](https://support.atlassian.com/jira-software-cloud/docs/work-with-jira-coding-agent-in-automations/)): automation = trigger + conditions + "Use Jira Coding Agent" action (repo or "Infer repository from work item", branch settings, prompt with smart values such as `{{issue.labels}}`). It "runs in a restricted mode in automations and doesn't use Atlassian Teamwork Graph context. This means that the Jira Coding Agent won't read Confluence content." Sessions belong to the automation's connection owner, whose credits are used; output smart values `{{jiracodingagent.codeGeneration.jobId}}` and `.repoUrl`; runs show in the audit log.
- **Not stated:** whether the agent reads comments, linked Confluence pages or JPD ideas by default (only that it can read Jira and Confluence). Whether it posts a comment back on the work item is also not stated. The PR shows in the work item's Development section and Agent sessions section.

## Notable quotes
- "it won't merge the draft pull request directly, but will hand it back to your team for review and merge." (Edit generated code)

## Could not verify
- Which fields of the work item go into the agent's starting context. No published date on the page.
