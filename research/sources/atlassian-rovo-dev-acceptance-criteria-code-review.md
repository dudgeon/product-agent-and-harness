---
title: Check acceptance criteria in a code review (Rovo Dev)
source_url: https://support.atlassian.com/rovo/docs/check-acceptance-criteria-in-a-code-review/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [opportunity-to-code-chain, agent-ready-intent, human-review-gates, agent-factory-sdlc]
relevance: high
---

## Relevance to the project
This is the documented loop-back from "review the change" to "shape the intent": Rovo Dev code review reads acceptance criteria from the linked Jira work item and reports whether the PR meets them. It spells out which fields count as acceptance criteria and how the PR is matched to a work item (branch name key). That is a concrete, checkable contract a PM intent artifact could be written to.

## Themes
- `opportunity-to-code-chain`: "Rovo Dev can compare the code in your pull request to requirements listed in your linked Jira work items."
- `agent-ready-intent`: criteria are read from the description or custom fields labelled "Acceptance Criteria", "AC", "ACs", "Business Requirements", "Functional Requirements", "Requirements", "Definition of Done", "DoD" (Where to write acceptance criteria).
- `human-review-gates`: it reports criteria that "Are missing from the code"; it comments, it does not block.

## Key points
- **Documented:** checks summary, description and custom fields of the linked work item; "won't search work items for acceptance criteria if the work item description is empty."
- **Documented (How Rovo Dev checks the correct work item):** looks for a key in the branch name first, then commit messages; if more than one key is in commit messages it uses none. Advice: one work item key in the branch name.
- **Documented:** on by default in Bitbucket; repo admin can toggle; GitHub uses Rovo Dev app settings. Needs Rovo Dev Standard on the Jira site connected to the Bitbucket workspace or GitHub org.
- **Documented, related page** ([Activate code reviews in your repository](https://support.atlassian.com/rovo/docs/activate-code-reviews-in-your-repository/)): workspace-level and repo-level activation in Bitbucket, org/repo toggles in GitHub; run on PR creation, on every commit, or manually ("Analyze code"); credits come from the PR author; around 10 PRs a minute per workspace; may not comment on PRs over 10,000 changed lines or repos over 20GB; supported languages Java, JavaScript, Python, C++, Go, Ruby, PHP, TypeScript, Kotlin, Swift.
- **Advice in the doc:** write criteria that are short, unambiguous, measurable, and reuse a template.

## Could not verify
- Output format of the check (comment structure) beyond "missing" findings; the full list of result categories was truncated in retrieval.
