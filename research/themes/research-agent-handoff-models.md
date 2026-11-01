# Themes: research-agent-handoff-models

Written only by the task research-agent-handoff-models (2026-10-31). Bullets from four research tracks on agent-to-agent handoff and orchestration models ([synthesis](../../tasks/research-agent-handoff-models/01-synthesis.md)). Seven new slugs carry a description (handoff-context-transfer, relay-information-loss, delegation-return-contract, durable-external-waits, blackboard-coordination, through-line-context-budget, event-triggered-agents); existing slugs reuse the register heading.

## handoff-context-transfer: What crosses a handoff
What actually moves when one agent passes work to another: full transcript, filtered transcript, final message, typed task object or shared state keys, and whether the person's conversation moves with it. The choice decides fidelity, cost, audit and need-to-know more than topology does.
- [Handoffs (OpenAI Agents SDK)](sources/openai-agents-sdk-handoffs.md): by default "the receiving agent gets to see the entire previous conversation history"; input filters and an opt-in history collapse narrow it, and neither redacts (research-agent-handoff-models)
- [Tools: agents as tools (OpenAI Agents SDK)](sources/openai-agents-sdk-agents-as-tools.md): a tool agent gets one string `input` or a typed schema, and "the parent run's conversation state is not inherited automatically" (research-agent-handoff-models)
- [openai/swarm (README)](sources/github-openai-swarm.md): at a handoff "the system prompt will change, but the chat history will not" (research-agent-handoff-models)
- [Orchestrating Agents: Routines and Handoffs](sources/openai-cookbook-orchestrating-agents.md): handoff defined as passing "an active conversation", like a phone transfer (research-agent-handoff-models)
- [Multi-Agent Systems in ADK (archived 1.x page)](sources/google-adk-multi-agent-systems.md): three media: shared `session.state` via `output_key`, `transfer_to_agent`, and `AgentTool` returning the final response plus state changes (research-agent-handoff-models)
- [Build collaborative agent teams (ADK 2.0)](sources/google-adk-collaborative-workflows.md): `chat`/`task`/`single_turn` modes fix who talks to the user and whether control returns automatically (research-agent-handoff-models)
- [Multi-agent (LangChain docs)](sources/langchain-docs-multi-agent.md): subagents "start fresh" and never talk to the user; handoff agents do (research-agent-handoff-models)
- [Handoffs (LangChain multi-agent docs)](sources/langchain-docs-multi-agent-handoffs.md): pass the handoff call and ToolMessage, "not the full subagent history" (research-agent-handoff-models)
- [Subagents (LangChain multi-agent docs)](sources/langchain-docs-multi-agent-subagents.md): isolated, forked or custom input; "the supervisor only sees the final output" (research-agent-handoff-models)
- [langgraph-supervisor-py (README)](sources/github-langgraph-supervisor.md): `output_mode` full_history vs last_message; `forward_message` sends sub-agent replies verbatim; library archived (research-agent-handoff-models)
- [langgraph-swarm-py (README)](sources/github-langgraph-swarm.md): one shared `messages` key; a checkpointer remembers the active agent (research-agent-handoff-models)
- [Microsoft Agent Framework Workflows Orchestrations - Handoff](sources/microsoft-agent-framework-handoff-orchestration.md): handoff vs agent-as-tools on control, ownership and context; user and agent messages broadcast, tool calls stripped (research-agent-handoff-models)
- [Processes and Tasks (CrewAI docs)](sources/crewai-docs-processes-and-tasks.md): "the output of one task is automatically relayed into the next one" as raw or Pydantic output after guardrails (research-agent-handoff-models)
- [Multi-Agents: What's Actually Working](sources/cognition-multi-agents-whats-working.md): reviewer gets the diff with no shared context; "smart friend" gets a fork of the full context (research-agent-handoff-models)
- [How Agents Manage Other Agents: Four Subagents Patterns in 2026](sources/philschmid-subagent-patterns-2026.md): inline tool, fan-out, pool, teams, ordered by what context each agent keeps (research-agent-handoff-models)

## relay-information-loss: Information loss across agent relays
Measured and claimed loss when work passes through several agents (the "telephone game"), and the conditions that make it worse or better: prose versus structure, model strength, access to the source, and a central verifier.
- [On the Reliability Limits of LLM-Based Multi-Agent Planning](sources/arxiv-ao-reliability-limits-multi-agent-planning.md): accuracy 90.7% → 22.5% over five prose relay stages; structured messages lose about 2.8 points per stage vs 8.5 (research-agent-handoff-models)
- [Faithful, Not Corrective](sources/arxiv-zeng-faithful-not-corrective-relays.md): strong relays near lossless over six hops (recall ≥0.973) but carry injected errors 83-100% (research-agent-handoff-models)
- [Towards a Science of Scaling Agent Systems](sources/arxiv-kim-towards-science-scaling-agent-systems.md): multi-agent "intrinsic information fragmentation"; -39% to -70% on sequential planning (research-agent-handoff-models)
- [Single-Agent LLMs Outperform Multi-Agent Systems ... Equal Thinking Token Budgets](sources/arxiv-tran-kiela-single-agent-equal-thinking-budgets.md): sequential multi-agent weakest at most budgets (research-agent-handoff-models)
- [Benchmarking Multi-Agent Architectures](sources/langchain-benchmarking-multi-agent-architectures.md): supervisor "translation" errors likened to telephone; fixes gave nearly 50% (research-agent-handoff-models)
- [When to use multi-agent systems (and when not to)](sources/claude-building-multi-agent-systems-when-how.md): problem-type splits create a "telephone game" (research-agent-handoff-models)
- [LLM as a Broken Telephone: Iterative Generation Distorts Information](sources/arxiv-mohamed-llm-broken-telephone.md): factual distortion accumulates over iterative regeneration; constrained prompts and low temperature reduce it (research-agent-handoff-models)
- [When LLMs Play the Telephone Game](sources/arxiv-perez-llms-telephone-game.md): iterated transmission drifts text toward attractors, more under open-ended instructions (research-agent-handoff-models)
- [LLMs Get Lost In Multi-Turn Conversation](sources/arxiv-laban-llms-lost-multi-turn.md): piecemeal requirements cost 39% on average; consolidated into one instruction about 95% of full; authors advise summarising into a fresh conversation (research-agent-handoff-models)
- [Choose a Planning Path (BMad Method docs)](sources/bmad-docs-choose-a-planning-path.md): "Dividing work can lose information: a requirement weakens, a constraint disappears" (research-agent-handoff-models)
- [BMad Knowledge Base (BMAD-METHOD v4)](sources/bmad-v4-knowledge-base.md): fresh chat required between SM, Dev and QA agents; the story file is the only carrier (research-agent-handoff-models)
- [Ralph Wiggum as a "software engineer"](sources/ghuntley-ralph-wiggum-software-engineer.md): each loop starts fresh and "will not have the reasoning", so reasons must be written into code and docs (research-agent-handoff-models)
- [ChatDev: Communicative Agents for Software Development](sources/arxiv-chatdev.md): only phase solutions cross phase seams, not dialogue, because of context limits; cost of the split unmeasured (research-agent-handoff-models)

## delegation-return-contract: What a delegated agent receives and gives back
What crosses a delegation in each direction (prompt, forked transcript, skills; summary, typed result, trace pointer) and how the caller can verify it. Matters for audit and for the telephone-game failure in any through-line design.
- [Custom subagents in Claude Code](sources/anthropic-claude-code-subagents-docs.md): fresh context plus a delegation message in; "only the summary" out; full transcript on disk for 30 days (research-agent-handoff-models)
- [Subagents (Codex docs)](sources/openai-codex-subagents-docs.md): summary and results back to the main thread; prompts should say what summary to return (research-agent-handoff-models)
- [Subagents (Cursor docs)](sources/cursor-docs-subagents.md): a clean context in, "a final message" out, an agent ID to resume (research-agent-handoff-models)
- [Orchestrate subagents at scale with dynamic workflows](sources/anthropic-claude-code-dynamic-workflows-docs.md): `agent()` with a schema returns validated JSON; unverifiable claims are listed as unverified (research-agent-handoff-models)
- [Message your other Claude Code sessions](sources/anthropic-claude-code-cross-session-messaging.md): plain text only, "never the sender's conversation history or files" (research-agent-handoff-models)

## through-line-context-budget: The through-line session's context budget
How long one person's general-purpose session can carry a piece of work before compaction and context rot erode it, and what vendors do about it (compaction that re-injects files, memory files, coordinator conversations over threads). Matters for whether model B (through line) can hold a weeks-long feature without a records layer.
- [Explore the context window](sources/anthropic-claude-code-context-window-compaction.md): compaction re-injects CLAUDE.md, auto memory and the plan from disk; conversation and path-scoped rules are summarised away (research-agent-handoff-models)
- [Let Claude coordinate ongoing work with Projects](sources/anthropic-claude-code-projects-docs.md): coordinator works from recent messages, threads and project memory, "Put anything that must never be dropped in project memory" (research-agent-handoff-models)
- [Context Rot](sources/chroma-context-rot.md): 18 models do much better on a focused ~300-token prompt than a ~113k-token chat history (research-agent-handoff-models)
- [Long-running work (Codex)](sources/openai-codex-long-running-work.md): OpenAI's advice is to keep related work in one chat "so ChatGPT keeps its context"; no compaction guidance on the page (research-agent-handoff-models)

## blackboard-coordination: Blackboard and shared-record coordination
Agents coordinate only by reading and writing a shared board or record, never by messaging; the open design choice is who decides which agent acts next (a control unit, volunteering specialists, a hook, a person). Matters for whether the feature repo or a shared record can be the only integration point between the person's harness and the two modules.
- [Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture](sources/arxiv-han-zhang-llm-blackboard-bmas.md): agents communicate solely through the board; an LLM control unit picks agents per round; removing it roughly triples tokens with similar accuracy (research-agent-handoff-models)
- [LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science](sources/arxiv-salemi-llm-blackboard-information-discovery.md): broadcast-and-volunteer beats master-slave assignment by 13-57% relative at about 1.8x cost, because an orchestrator must model every agent's capabilities (research-agent-handoff-models)
- [Blackboard system](sources/wikipedia-blackboard-system.md): the classic model has three parts, knowledge sources, blackboard and a control shell; opportunistic control chooses each cycle (research-agent-handoff-models)
- [Hook types (Kiro docs)](sources/kiro-docs-hook-types.md): file hooks "respond only to changes made by the agent", so the spec files are not a cross-party wake-up channel (research-agent-handoff-models)
- [Ontology MCP: Sample architecture (Palantir Foundry docs)](sources/palantir-ontology-mcp-sample-architecture.md): typed object reads via SQL, writes only via action types; the ontology stays the system of record while specialised agents take tasks (research-agent-handoff-models)

## event-triggered-agents: Agents woken by a change to a shared record
Agents that start when a record, page, ticket, message or log entry changes, rather than when a person prompts them. It matters because it makes the system of record the coordination medium, and the trigger often does not carry who changed the record.
- [A Distributed State of Mind: Event-Driven Multi-Agent Systems](sources/confluent-event-driven-multi-agent-systems.md): four multi-agent patterns rebuilt on Kafka topics with log replay; no human, identity or audit treatment (research-agent-handoff-models)
- [What are Custom Agents? (Notion Help Center)](sources/notion-help-custom-agents.md): database page added, updated or removed, comment, meeting-note, Slack and schedule triggers; no documented approval gate (research-agent-handoff-models)
- [Automating Rovo agents (Atlassian support)](sources/atlassian-rovo-agents-in-automations.md): a Confluence "DACI" page publish triggers an agent review posted as a comment (research-agent-handoff-models)

## durable-external-waits: Holding an ask open for an outside answer
How durable engines and persistent agents hold a wait open for days or weeks, survive restarts, remind and escalate, and what they record about who answered. It matters because a delivery dependency ask outlives every session, and the engines solve persistence but not answerer identity.
- [Build a human-in-the-loop document approval Workflow (Temporal docs)](sources/temporal-docs-reliable-document-approvals.md): 24h reminders, SLA, escalation and auto-reject in code; approver email is a payload field not checked against the sender; 51,200-event history cap (research-agent-handoff-models)
- [Human-in-the-loop (HITL) (Inngest durable agents docs)](sources/inngest-durable-agents-human-in-the-loop.md): `waitForEvent` with id matching, no compute while waiting; `respondedBy` filled in by your handler (research-agent-handoff-models)
- [Human-in-the-loop (Restate AI patterns docs)](sources/restate-ai-human-in-the-loop.md): an awakeable callback id resolvable over HTTP by whoever holds it; timer and promise survive restarts (research-agent-handoff-models)
- [Human-in-the-Loop (DBOS AI docs)](sources/dbos-ai-human-in-the-loop.md): deadline and message stored in Postgres; an inbox endpoint lists agents pending approval (research-agent-handoff-models)
- [Human in the loop (Cloudflare Agents SDK docs)](sources/cloudflare-agents-human-in-the-loop.md): the approval gate "can continue for months"; waitForEvent up to 365 days with early events buffered; recommended audit table (research-agent-handoff-models)

## single-agent-many-skills: One agent with many skills, not many agents
- [Towards a Science of Scaling Agent Systems](sources/arxiv-kim-towards-science-scaling-agent-systems.md): coordination returns diminish above about 45% single-agent baseline; tool-heavy tasks pay overhead (research-agent-handoff-models)
- [Single-Agent LLMs Outperform Multi-Agent Systems ... Equal Thinking Token Budgets](sources/arxiv-tran-kiela-single-agent-equal-thinking-budgets.md): single agent matches or beats five multi-agent designs at equal thinking budgets (research-agent-handoff-models)
- [When to use multi-agent systems (and when not to)](sources/claude-building-multi-agent-systems-when-how.md): 3-10x tokens; only three cases justify multi-agent (research-agent-handoff-models)
- [Handoffs (LangChain multi-agent docs)](sources/langchain-docs-multi-agent-handoffs.md): "single agent with middleware for most handoffs use cases" (research-agent-handoff-models)
- [Multi-Agents: What's Actually Working](sources/cognition-multi-agents-whats-working.md): "writes stay single-threaded and the additional agents contribute intelligence rather than actions" (research-agent-handoff-models)
- [Subagents (Agentic Engineering Patterns)](sources/simonwillison-guide-subagents.md): the root agent can review or debug its own output given tokens; subagents protect root context (research-agent-handoff-models)

## process-artifacts-as-coordination: Process artifacts as the coordination layer
- [Magentic-One](sources/arxiv-magentic-one.md): removing the task and progress ledgers cost 31% on GAIA validation (research-agent-handoff-models)
- [Microsoft Agent Framework Workflows Orchestrations - Magentic](sources/microsoft-agent-framework-magentic-orchestration.md): ledger events and stall-triggered replanning shipped as an orchestration (research-agent-handoff-models)
- [Flows (CrewAI docs)](sources/crewai-docs-flows.md): crews don't share state; typed flow state is the medium, persisted and resumable by id (research-agent-handoff-models)
- [Autonomous Development Loops (BMad Method docs)](sources/bmad-docs-autonomous-development-loops.md): "a ticket's status lives in its plan"; the builder never picks the next ticket; an orchestrator reads statuses from files (research-agent-handoff-models)
- [Plan Inside an Organization (BMad Method docs)](sources/bmad-docs-plan-inside-an-organization.md): one owned PRD anchors all derived documents; "Nothing downstream reinterprets the PRD" (research-agent-handoff-models)
- [Using PLANS.md for multi-hour problem solving](sources/openai-cookbook-codex-exec-plans.md): the plan is a self-contained living document; restart must be possible from the plan alone (research-agent-handoff-models)
- [My LLM codegen workflow atm](sources/harper-reed-llm-codegen-workflow.md): spec.md, prompt_plan.md and todo.md relay work across sessions and models; breaks with more than one person (research-agent-handoff-models)
- [What are Custom Agents? (Notion Help Center)](sources/notion-help-custom-agents.md): a database property change wakes an agent, so the record is the bus (research-agent-handoff-models)
- [A Distributed State of Mind: Event-Driven Multi-Agent Systems](sources/confluent-event-driven-multi-agent-systems.md): the blackboard becomes a shared topic, and keys record which agent originated each event (research-agent-handoff-models)

## human-review-gates: Human review gates on agent output
- [Microsoft Agent Framework Workflows Orchestrations - Magentic](sources/microsoft-agent-framework-magentic-orchestration.md): plan sign-off on by default in .NET, off in Python (research-agent-handoff-models)
- [Microsoft Agent Framework Workflows Orchestrations - Handoff](sources/microsoft-agent-framework-handoff-orchestration.md): approval-required tools pause; checkpoints allow approval "hours or days later" (research-agent-handoff-models)
- [Multi-agent workflow patterns (ADK)](sources/google-adk-workflow-patterns.md): PolicyEngine plus SecurityPlugin returns CONFIRM to pause tool calls (research-agent-handoff-models)
- [Plan Inside an Organization (BMad Method docs)](sources/bmad-docs-plan-inside-an-organization.md): five named sign-offs each block a next step and leave a written result usable as an audit trail (research-agent-handoff-models)
- [Autonomous Development Loops (BMad Method docs)](sources/bmad-docs-autonomous-development-loops.md): plan and done checkpoints are read by the orchestrator; the builder "never moves a ticket to done" (research-agent-handoff-models)
- [Custom agents in VS Code](sources/vscode-custom-agents-handoffs.md): handoff buttons with a pre-filled prompt the person reviews and sends; `send: true` removes the gate (research-agent-handoff-models)
- [Orchestrate subagents at scale with dynamic workflows](sources/anthropic-claude-code-dynamic-workflows-docs.md): no mid-run user input; sign-off between stages means one workflow per stage (research-agent-handoff-models)
- [Advanced capabilities: Managed Devins](sources/devin-docs-advanced-capabilities-managed-devins.md): child sessions auto-approved by default (research-agent-handoff-models)
- [Automatic approvals and Pre-merge checks (CodeRabbit docs)](sources/coderabbit-docs-automatic-approvals-pre-merge-checks.md): a reviewer agent that can request changes and fail natural-language checks in `error` mode; override can be restricted to requested reviewers (research-agent-handoff-models)

## agent-failure-modes: Recurring agent failure modes in PM work
- [Magentic-One](sources/arxiv-magentic-one.md): repeated failing login until account suspension; agents tried to recruit humans (research-agent-handoff-models)
- [How Agents Manage Other Agents](sources/philschmid-subagent-patterns-2026.md): models "lose track of which agent has which context"; team failures "cascade" (research-agent-handoff-models)

## one-job-per-agent: One job per agent
- [Devin can now Manage Devins](sources/cognition-devin-manage-devins.md): manager splits scoped child sessions in separate VMs; human can message any child directly (research-agent-handoff-models)

## decision-rationale-records: Decision rationale records
- [Using PLANS.md for multi-hour problem solving](sources/openai-cookbook-codex-exec-plans.md): mandatory Decision Log with reasoning, dated and attributed, plus Surprises & Discoveries and Progress sections (research-agent-handoff-models)

## org-context-grounding: Agents work when grounded in organisation context
- [From idea to deployment: The complete lifecycle of AI on display at Ignite 2025](sources/microsoft-ignite-2025-work-iq.md): Work IQ, Fabric IQ and Foundry IQ are shared read-context layers for agents; no agent-to-agent work handoff described (research-agent-handoff-models)

## capability-packaging-layers: Choosing the layer a capability lives in
- [Extend Claude Code](sources/anthropic-claude-code-extend-features-overview.md): Anthropic's feature table and triggers: CLAUDE.md for always-on rules, skills for method, MCP for systems, subagents for isolation, hooks for enforcement, plugins for distribution (research-agent-handoff-models)
- [Orchestrate subagents at scale with dynamic workflows](sources/anthropic-claude-code-dynamic-workflows-docs.md): "who holds the plan" table: Claude turn by turn (subagents, skills), a lead (teams), a script (workflows) (research-agent-handoff-models)
- [Meet the A2A CLI](sources/a2a-project-introducing-a2a-cli.md): A2A reaches Claude Code, Cursor and Codex as a skill wrapping a CLI, not as a native client (research-agent-handoff-models)

## remote-agent-invocation: Remote agent invocation
- [Run agents in parallel](sources/anthropic-claude-code-run-agents-in-parallel.md): every agent in Claude Code's multi-agent modes is a Claude session; "To involve a different tool, expose it to Claude as an MCP server" (research-agent-handoff-models)
- [Advanced capabilities: Managed Devins](sources/devin-docs-advanced-capabilities-managed-devins.md): Devin MCP lets any MCP-compatible agent create, message, wait on and terminate Devin sessions (research-agent-handoff-models)
- [MCP Tasks and Events, Explained](sources/upstash-mcp-tasks-and-events.md): October 2026 table lists no Tasks support in Claude Code, Codex or Cursor and Events as pre-spec; conflicts with Claude Code docs (research-agent-handoff-models)
- [Subagents (Cursor docs)](sources/cursor-docs-subagents.md): cloud subagents use team MCP servers at cursor.com/agents, not local ones (research-agent-handoff-models)

## identity-delegation: Identity and delegation (on-behalf-of)
- [Subagents (Codex docs)](sources/openai-codex-subagents-docs.md): subagents inherit the parent's sandbox, approvals, MCP servers and skills, and custom agents cannot override them (research-agent-handoff-models)
- [Let Claude coordinate ongoing work with Projects](sources/anthropic-claude-code-projects-docs.md): "A project is yours alone ... it uses your own GitHub access and connectors" (research-agent-handoff-models)
- [Tutorial: Hand off work between agents in VS Code](sources/vscode-agents-handoff-tutorial.md): the selected model determines provider and billing; which identity carries over a handoff is not stated (research-agent-handoff-models)
- [Devin in Slack](sources/devin-docs-slack-integration.md): each Slack user must link to a Devin account with a matching email (research-agent-handoff-models)
- [Model AI Governance Framework for Agentic AI, Version 1.5](sources/imda-mgf-agentic-ai-v1-5.md): agent identity tied to a supervisor, the capacity it acts in recorded, delegations "clearly recorded" and bounded by the grantor's rights (research-agent-handoff-models)
- [Agent 365 identity (Microsoft Learn)](sources/microsoft-learn-agent-365-identity.md): S2S, OBO (user as subject, agent as actor) and Agentic-User modes; logs separate credential source, actor and subject; mandatory sponsor (research-agent-handoff-models)
- [Notion 3.8 release notes (October 13, 2026)](sources/notion-releases-2026-10-13.md): page and database version history attributes changes to people and agents; per-property permissions per person or agent (research-agent-handoff-models)

## human-relay-removed: The session or channel replaces the person as relay
- [Message your other Claude Code sessions](sources/anthropic-claude-code-cross-session-messaging.md): Claude passes findings between one person's sessions "instead of you copy-pasting between terminals" (research-agent-handoff-models)

## agent-protocol-security: Security of agent-to-agent and agent-to-tool protocols
- [Message your other Claude Code sessions](sources/anthropic-claude-code-cross-session-messaging.md): a peer message cannot approve, change configuration or run commands; inbound accept, hold or refuse (research-agent-handoff-models)

## task-context-isolation: Isolation by task context, not only by user permission
- [Subagents in VS Code](sources/vscode-subagents-docs.md): the delegated task "must be self-contained"; each Local invocation is stateless (research-agent-handoff-models)

## harness-portability: Harness portability
- [Subagents (Cursor docs)](sources/cursor-docs-subagents.md): Cursor reads subagent files from `.claude/agents/` and `.codex/agents/` as well as `.cursor/agents/` (research-agent-handoff-models)
- [Subagents in VS Code](sources/vscode-subagents-docs.md): one editor delegates through Local, Copilot, Claude and Codex subagent systems (research-agent-handoff-models)

## regulatory-drivers-of-process: Regulation prescribes the record and the independence, not the meeting
- [2026 FINRA Annual Regulatory Oversight Report: GenAI (including AI agents)](sources/finra-2026-oversight-report-genai.md): agent risks of autonomy, scope and authority, and auditability; firms to decide where human-in-the-loop is needed and how to track agent actions (research-agent-handoff-models)
- [Model AI Governance Framework for Agentic AI, Version 1.5](sources/imda-mgf-agentic-ai-v1-5.md): checkpoints enforced "through system-level controls ... vs prompt-layer guardrails"; audit approvers through override rate and response time (research-agent-handoff-models)

## gate-judge-separation: Where a gate fires vs who judges it
- [Automatic approvals and Pre-merge checks (CodeRabbit docs)](sources/coderabbit-docs-automatic-approvals-pre-merge-checks.md): the check's mode (`off`/`warning`/`error`) is set separately from its natural-language judge; "Inconclusive" never blocks (research-agent-handoff-models)

## prd-agents: PRD and spec writing/review as an agent job
- [Automating Rovo agents (Atlassian support)](sources/atlassian-rovo-agents-in-automations.md): the only documented document-reviewer trigger found: a decision page published, reviewed and commented on (research-agent-handoff-models)
