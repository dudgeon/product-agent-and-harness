---
title: Custom subagents in Claude Code (docs)
source_url: https://code.claude.com/docs/en/sub-agents
author: Anthropic
publisher: code.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, single-agent-many-skills, skills-marketplace]
relevance: high
---

## Relevance to the project
Subagent definitions are the less-standardised sibling of skills: there is no cross-vendor spec, and this page is explicit that nothing in the format is marked portable. Relevant to the question "how far can a packaged subagent carry complexity": model, tool allowlist, permission mode, memory, worktree isolation, hooks and MCP servers can all be declared, but all bind to Claude Code features.

## Themes
- harness-portability: the docs note that fields (model values, tool names, permissionMode, memory, isolation, hooks) "depend on Claude Code features" and "documentation does not label any field as portable". Format = Markdown + YAML frontmatter, body = system prompt.
- skills-marketplace: precedence managed settings > `--agents` > project > user > plugin; plugin-shipped subagents have `hooks`, `mcpServers`, `permissionMode` ignored "for security", so a plugin cannot ship a fully privileged agent definition.
- single-agent-many-skills: subagents can spawn subagents up to three layers by default; 20 concurrent default; the `skills` field preloads up to 32 skills.

## Key points
- Required: name, description. Optional: tools, disallowedTools, model, permissionMode, maxTurns, skills, mcpServers, hooks, memory (user/project/local), isolation: worktree, background, effort.
- Delegation is description-matched by default in Claude Code.

## Could not verify
- Final ~16k characters of the page not read.

## Follow-up (2026-10-31)
Filed by research-agent-handoff-models. Re-read characters 0 to 100,000 for the handoff contract (the final ~16k characters, including the body of the fork section, were again not read).
- What a subagent receives: "Each subagent starts with a fresh, isolated context window. It doesn't see your conversation history, the skills you've already invoked, or the files Claude has already read. Claude composes a delegation message that summarizes the task." Initial context: its own system prompt plus environment details (not the Claude Code system prompt), the delegation message, CLAUDE.md hierarchy (not for Explore, Plan or `omitClaudeMd: true`), a git status snapshot, skills named in `skills`, and a sibling roster when it has SendMessage.
- What returns: the subagent "returns only the summary"; Claude receives its agent ID; background results arrive as a completion notification in a later turn. Before Claude reads a final report, Claude Code scans it for instruction-shaped text (it never removes text but may insert a marker).
- Full transcripts persist at `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`, unaffected by main-session compaction, deleted after `cleanupPeriodDays` (default 30). So the summary is what the parent reasons on, but a trace exists on disk for a person or a checker to inspect.
- Resume: `SendMessage` with the agent ID or name resumes a subagent "with full conversation history, including all previous tool calls, results, and reasoning"; Explore and Plan are one-shot; a subagent stopped at `maxTurns` returns output marked partial. Before v2.1.304 a subagent messaged right after finishing "could forget its most recent work".
- Identity and permissions: subagents count against the person's usage limits and inherit permission rules; in bypass, acceptEdits or auto mode the parent's mode overrides the subagent's `permissionMode`; background subagents surface every permission prompt in the main session; "no message from any agent counts as your approval".
- `memory: user | project | local` gives a subagent a persistent directory (`.claude/agent-memory/<name>/` for project) whose MEMORY.md (first 200 lines or 25KB) loads into its prompt: a subagent can carry state across sessions, though it is still the person's files.
- Verification: the page gives no guidance on checking a subagent's result beyond "If a rule must [reach the subagent], restate it in the prompt" and noting that the output scan "isn't a substitute for restricting what a subagent can reach".
