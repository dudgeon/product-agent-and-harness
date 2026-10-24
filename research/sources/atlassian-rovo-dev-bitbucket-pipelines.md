---
title: Work with Rovo Dev in Bitbucket Pipelines
source_url: https://support.atlassian.com/rovo/docs/work-with-rovo-dev-in-bitbucket-pipelines/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [agent-factory-sdlc, status-update-agents, enterprise-admin-controls]
relevance: low
---

## Relevance to the project
The only first-party doc found for the "release" step with an agent: Rovo Dev in Bitbucket Pipelines (beta) summarises what changed from commits, Jira work items and deployment data, and explains failed builds. Release notes from Jira work items are also offered by a Rovo out-of-the-box agent. Compass scorecards and deployment tracking with agents were not found documented.

## Themes
- `agent-factory-sdlc`: "Rovo Dev can parse commits, Jira work items, and other deployment data to create detailed summaries of what's changed and how it affects your customers. Plus, Rovo Dev can analyze failed build steps and explain why they broke down in plain language, while suggesting fixes."
- `status-update-agents`: release summaries; related [Release Notes Drafter](https://www.atlassian.com/software/rovo/use-cases/agent-release-notes-drafter) agent "Generates release notes from up to 20 Jira issues", groups by theme in a problem-solution format (product page, vendor-claim). An earlier search summary said it drafts in Confluence; not confirmed on the page read.
- `enterprise-admin-controls`: "Rovo Dev in Bitbucket Pipelines isn't controlled by the Atlassian Administration AI early access toggle yet"; controlled only by the workspace Rovo Dev toggle and "can't be disabled separately from other Rovo Dev features (like code reviews)."

## Key points
- **Documented:** activate under Workspace settings > AI > Rovo Dev > "Use Rovo Dev in this workspace".
- See also the [Jira Delivery Agent note](atlassian-rovo-jira-delivery-agent.md) for progress reporting after release.
- **Not found:** Compass scorecards tied to agents. Search results said Compass scorecards and catalog are transitioning into the DX app; not verified.
- **Community answer (not first-party staff confirmation checked):** some version/release fields are not reachable by the "Run Rovo Agent" automation action.

## Could not verify
- Where the Pipelines summary is posted (PR, deployment, Jira); Compass agent features.
