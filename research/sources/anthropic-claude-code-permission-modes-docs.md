---
title: "Claude Code docs: Configure permissions and Permission modes"
source_url: https://code.claude.com/docs/en/permission-modes
author: Anthropic
publisher: code.claude.com docs (also https://code.claude.com/docs/en/permissions)
published: unknown (current as of retrieval; cites versions up to v2.1.302)
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [decision-rights-for-agents, risk-sloped-review, evals-autonomy-trust, enterprise-admin-controls, gate-judge-separation, human-review-gates]
relevance: high
---

## Relevance to the project
The autonomy slider of the harness this project builds on, in detail. Six modes (Manual, acceptEdits, plan, auto, dontAsk, bypassPermissions) layer under allow/ask/deny rules and hooks; auto mode replaces the human prompt with a separate classifier model that reviews non-read-only actions and is shielded from tool results; some actions are never auto-approved in any mode; admins can lock modes via managed settings. It is a worked instance of dimension 2 (gate type: human prompt vs model classifier vs deterministic rule) and dimension 4 (who decides, who can lock), and it shows the default moving toward autonomy (auto is the default for interactive terminal sessions since v2.1.283).

## Themes
- decision-rights-for-agents: modes set the baseline; rules layer on top; deny rules block in every mode including bypass; `permissions.defaultMode` in managed settings sets the organisation's starting mode and `disableAutoMode`/`disableBypassPermissionsMode` remove modes from the cycle (Permission modes, Managed settings).
- risk-sloped-review: acceptEdits auto-approves in-directory edits and common filesystem commands but not shell or network; auto mode blocks by default piping downloads to a shell, production deploys, force pushes, mass cloud deletion, IAM changes and exfiltration, while allowing local file ops, declared dependency installs and pushes to the repo's branches (Permission modes).
- gate-judge-separation: in auto mode "a classifier reviews actions instead of you"; it sees user messages, non-read-only tool calls and CLAUDE.md but tool results are stripped so hostile content cannot steer it; subagents are checked at spawn, during execution and on report (Permission modes).
- evals-autonomy-trust: three classifier blocks in a row or 20 in total pause auto mode and resume prompting; "Auto mode doesn't guarantee safety" (Permission modes).
- enterprise-admin-controls: `auto` and `bypassPermissions` set in a project's `.claude/settings.json` are ignored; they must be set in user or managed settings; HIPAA configuration forces Manual (Which mode a session starts in).

## Key points
- Mode table: default/Manual prompts on first use of each tool; acceptEdits; plan reads and explores and blocks edits until a plan is approved; auto; dontAsk auto-denies anything that would prompt (for CI and scripts); bypassPermissions skips prompts except actions no mode auto-approves (isolated containers only).
- Never auto-approved in any mode: explicit ask rules, connector tools an organisation set to ask, tools requiring user interaction (AskUserQuestion), recognised critical-path `rm` removals, cross-session messaging safeguards.
- Protected paths (`.git`, `.claude`, shell rc files, `.mcp.json`, lockfile configs) are prompted in Manual and acceptEdits, routed to the classifier in auto, denied in dontAsk, allowed only in bypass.
- Entering auto mode drops broad allow rules such as `Bash(*)` and `Agent` while keeping narrow ones such as `Bash(npm test)`.
- Defaults: terminal and VS Code start in auto (v2.1.283+, all plans); `claude -p` and the Agent SDK start in default with prompts denied unless allowed.
- Related behavioural data already in the library: anthropic-measuring-agent-autonomy (auto-approve-all rises from about 20% of sessions for new users to over 40% with experience, while interrupts also rise).

## Could not verify
- Page dates; the last 6,000 characters of the permission-modes page.

## Merged from a duplicate note of the same source (research-skill-rigidity-spectrum, 2026-10-25)

The same page was filed twice by two subagents; the second note is folded in here.

### Relevance to the project
Claude Code's permission modes are the most concrete shipped autonomy slider: six modes from Manual (asks before most actions) to Bypass, with an auto mode where "a second model, the classifier, reviews actions instead of you". The decision order (deterministic rules first, then built-in approvals, then the model classifier) is a working example of layering deterministic gates under model judgment and above human approval, which is the design question for PM agents acting on tickets, docs and roadmaps.

### Themes
- evals-autonomy-trust: modes and what runs without asking: Manual (reads only), Accept edits (edits and common filesystem commands in the working directory), Plan (reads; edits blocked until a plan is approved), Auto (everything, with classifier checks), Don't ask (only pre-approved; anything else denied), Bypass ("Isolated containers and VMs only").
- human-review-gates: auto mode order: allow/ask/deny rules resolve first; built-in approvals for reads and in-directory edits; everything else to the classifier; if blocked, Claude gets the reason.
- risk-sloped-review: circuit breaker: after 3 consecutive or 20 total classifier blocks, auto mode pauses and asks to resume; protected paths (.git, .claude, .mcp.json) are prompted, classified or denied depending on mode; deny rules hold in every mode including bypass.

### Key points
- Classification: control flow model-chosen; gates = deterministic rules + hooks (a PreToolUse hook can return allow, but not for critical-path rm) + model classifier + human prompt; decision rights shift by mode, cycled with Shift+Tab.
- In auto mode, broad allow rules that grant arbitrary code execution (`Bash(*)`) are dropped on entry; narrow ones (`Bash(npm test)`) stay: the system distrusts a human's own blanket pre-approval when a model is the approver.
- Plan mode is a human gate on intent (approve the plan) rather than on each action.

### Could not verify
- The last ~6% of the page (hook precedence detail) was not read.
