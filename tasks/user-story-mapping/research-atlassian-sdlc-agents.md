# Atlassian's agent ecosystem by lifecycle task

Research for `user-story-mapping`, filed 2026-10-24. Each row says what exists, what it consumes and produces, the documented handoff, and what is unverified. "Documented" means a support.atlassian.com page; "claimed" means a blog or product page (vendor-claim). Source notes are in `../../research/sources/`.

Naming: "Rovo Dev in Jira" (April 2026 blog) is now documented as the **Jira Coding Agent**. Rovo Dev remains the name for the CLI, IDE, code review and Pipelines features. "Rovo Ops" is now **Ops Expert**.

## 1. Spot the opportunity
- **Exists:** JPD ideas (existing note [JPD ideas](../../research/sources/atlassian-jira-product-discovery-ideas.md)). Loom bug reports from video ([Loom note](../../research/sources/atlassian-loom-record-for-agent.md), related "Use AI workflows").
- **Consumes / produces:** a recording, giving a Jira (or Linear) work item with "a short description, steps to reproduce, and a link to your video".
- **Unverified:** an agent that creates JPD ideas from recordings or feedback. A public feature request asks for it; nothing shipped was found.

## 2. Talk to customers
- **Exists:** Loom meetings connected to a Jira space ([Loom note](../../research/sources/atlassian-loom-record-for-agent.md), related page). The CPO talk's JSM review of 900+ insight videos stays an anecdote ([transcript](../../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.transcript.md)).
- **Handoff (documented):** "Rovo analyzes the meeting transcript and recommends updates such as reassigning work items, changing priority or status, or adding a comment". The meeting owner accepts or discards each one on the board.
- **Unverified:** new work items or ideas made from customer calls. Only updates to existing items are documented.

## 3. Research the problem
- **Exists:** Rovo Deep Research ([note](../../research/sources/atlassian-rovo-deep-research.md)).
- **Consumes:** "organizational knowledge, connected 3P sources, or context added to your prompt like a file, a smart link, or an @mention".
- **Produces:** a cited report in Rovo Chat.
- **Handoff:** the 2025 engineering blog says it "can be effortlessly exported to your Confluence page". The support doc does not mention export, so this is a claim only.
- **Unverified:** whether any downstream agent (Planner, Coding Agent) reads a saved research page.

## 4. Set the goal
- **Exists:** Atlassian Goals in Home ([note](../../research/sources/atlassian-goals-what-is-a-goal.md)). The agentic guide says the goal stays human: "Set the goal (people decide what and why; Jira turns it into a plan)" ([guide](../../research/sources/atlassian-jira-agentic-engineering-guide.md)).
- **Artifact:** a goal with name, owner, date, status and a monthly human update. It links sub-goals, projects, epics and work items, and Teamwork Graph has a `JiraWorkItemContributesToAtlassianGoal` relationship.
- **Handoff:** documented as links only.
- **Read path:** the Delivery Agent can read "project, epic, or goal context" ([note](../../research/sources/atlassian-rovo-jira-delivery-agent.md)).
- **Unverified:** a link from JPD ideas to Goals, and any agent that drafts goals or goal updates.

## 5. Shape the intent
- **Exists:** Jira Planner, in Early Access and covered only by a blog ([note](../../research/sources/atlassian-blog-introducing-jira-planner.md)). Loom Record for agent, in open beta and documented ([note](../../research/sources/atlassian-loom-record-for-agent.md)).
- **Planner:** turns a rough idea into a Confluence Live Doc spec through clarifying questions and a readiness check (claimed).
- **Loom:** turns narration plus screen into an "agent prompt" whose tasks each have a title, bullets, a transcript quote, keyframes and timestamps. With "Create in Jira" it makes work items "for agents to act on" (documented).
- **JPD idea to work item:** "Embed the idea description and fields into the work item" (documented, [note](../../research/sources/atlassian-jpd-link-idea-to-work-item.md)). This is the only documented way idea content gets inside the item an agent reads.

## 6. Plan the change
- **Exists:** Jira Planner breaks the plan "into Jira work items, sequenced with dependencies and milestones, with each one carrying its own acceptance criteria" (claimed).
- **Internal anecdote:** Rovo Dev wrote plans and options onto subtasks ([note](../../research/sources/atlassian-blog-rovo-dev-in-jira.md)). The April 2026 blog says the agent "proposes a concrete plan you can review and refine" before it executes. The current support doc has no plan step, so that is unverified.
- **Older:** a 2025 "Technical Code Planning agent" Team '25 session (listing only, not read).

## 7. Write the code
- **Exists:** Jira Coding Agent ([note](../../research/sources/atlassian-jira-coding-agent-generate-code.md)).
- **Third-party agents:** Claude Agent for Jira (Forge app on Claude Managed Agents), Cursor, GitHub Copilot, and Codex. Codex is "coming soon" in the July post but listed as available on the product pages ([note](../../research/sources/atlassian-blog-jira-ai-native-software-development.md)).
- **Local agents:** a deep link to local tools ([note](../../research/sources/atlassian-jira-open-work-item-in-coding-tool.md)).
- **Admin view:** the space Agents page ([note](../../research/sources/atlassian-jira-manage-agents-in-space.md)).
- **Consumes (documented):** the work item, a chosen repo and a prompt. Interactively, the agent can CRUD Jira and Confluence as the user. In automations it runs in a "restricted mode ... won't read Confluence content".
- **Consumes (claimed):** Claude reads "acceptance criteria, target repository, and relevant design/engineering standards". The deep link passes "summary and description" in the support doc, but "summary, description, and linked docs" in the blog.
- **Produces:** a branch and a draft PR, with the user as author. Adding the work item key links the PR to the item. The session is listed under Agent sessions. Claude also "streams real-time status updates directly back to the Jira work item" (claimed).
- **Triggers:**
  - documented: assign, @mention, automation rule;
  - claimed: workflow transition or board column ([guide](../../research/sources/atlassian-jira-agentic-engineering-guide.md)).
  - The workflow-transition trigger matches the CPO's "move to In Progress" description.

## 8. Review the change
- **Exists:** Rovo Dev code review in Bitbucket and GitHub ([note](../../research/sources/atlassian-rovo-dev-acceptance-criteria-code-review.md)).
- **Handoff (documented):** it reads acceptance criteria from the description or custom fields named AC, Requirements or DoD on the work item. It finds the item from "your branch name for work item keys". If the description is empty, there is no check.
- **Figures (vendor-claim, [note](../../research/sources/arxiv-rovodev-code-reviewer-icse26.md)):** ICSE 2026 paper (all authors Atlassian-affiliated): PR cycle time -30.8%, human comments -35.6%, 38.70% of comments resolved. A separate blog claims -45% PR cycle time and an 18-hour first-review wait "cut to 0". These two figures are not reconciled.
- **Gap (internal anecdote):** PR review comments and CI failures are not yet fed back to the coding agent automatically.

## 9. Release
- **Exists:** Rovo Dev in Bitbucket Pipelines, in beta ([note](../../research/sources/atlassian-rovo-dev-bitbucket-pipelines.md)). It summarises changes "from commits, Jira work items, and other deployment data" and explains failed builds. There is also a Release Notes Drafter agent that works from up to 20 Jira issues.
- **Unverified:** where the summaries are posted, and any Compass scorecard or deployment-tracking agent. Search results said Compass scorecards are moving into DX; not checked.

## 10. Operate
- **Exists:** Ops Expert ([note](../../research/sources/atlassian-rovo-ops-expert-agent.md)).
- **Consumes:** alerts (natural language to AQL), past incidents, runbooks and Slack history, plus New Relic over MCP.
- **Produces:** a PIR as a Jira work item or Confluence page (`/create-pir`), and suggested severity, priority and problem tickets.
- **Claimed:** auto-PIR when an incident closes, and ML alert grouping (AIOps guide).
- **Claimed:** a JSM alert plus a bug triggers a coding agent through automation, which gets telemetry "Through the Teamwork Graph MCP" and attaches an investigation summary.

## 11. Learn
- **Documented loop back to the backlog:** Ops Expert can "Create Jira tickets for action items in this PIR", and it summarises past PIRs for new incidents.
- **Reporting:** the Delivery Agent reports on space health and stakeholder status.
- **Claimed:** "results feed back into the next spec", with no mechanism described.

## Context flow between steps
- **Documented traversal:** the Delivery Agent's "get work-item context in twg" returns "related pull requests, commits, branches, pages, and hierarchy". The user summary covers "work items, Confluence pages, pull requests, Loom videos, and Atlas projects or goals".
- **Documented links:**
  - idea to work item (JPD Delivery tab);
  - work item to PR (key in branch name or commit);
  - work item to goal (Goals field);
  - PIR to action-item work items.
- **Documented per-space context:** agent "Sources" (Confluence pages, Loom recordings) and instructions.
- **Inferred only:**
  - Planner or Coding Agent reading JPD ideas, Goals or Deep Research pages;
  - third-party agents getting Teamwork Graph context without the Rovo MCP;
  - any single object that ties the whole chain together. The Teamwork Graph links pairs of objects; no "lifecycle" record exists.
