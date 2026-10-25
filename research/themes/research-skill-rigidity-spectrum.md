# Themes: research-skill-rigidity-spectrum

Written only by the task research-skill-rigidity-spectrum (2026-10-25). Theme bullets from five research tracks (A vendor control flow and gates; B form of the standard and improvement loops; C stance toward the human, over-reliance and deskilling; D process artifacts and multi-party sessions; E practitioner skill files). New slugs carry a one-sentence description; existing slugs reuse the register heading.

## deterministic-scaffold-model-nodes: Deterministic scaffold, model-judged nodes
Rigid and loose parts are combined by nesting: code fixes the sequence and hard checks while the model works inside bounded nodes, or the reverse, with code islands inside a model-chosen flow. It matters because a PM skill can fix the parts that must hold (required sections, sign-offs) without scripting the parts that need judgment.
- [Minions: Stripe's one-shot, end-to-end coding agents, Part 2](sources/stripe-minions-part-2.md): blueprints mix deterministic nodes (lint, push; "don't invoke an LLM at all") with agentic nodes ("Implement task", "Fix CI failures"); "putting LLMs into contained boxes" (research-skill-rigidity-spectrum)
- [Design topics as mini-agents (Copilot Studio)](sources/microsoft-copilot-studio-topics-as-mini-agents.md): "keep deterministic logic inside the topic and leave user communication to the orchestration layer" (research-skill-rigidity-spectrum)
- [Agent orchestration (OpenAI Agents SDK)](sources/openai-agents-sdk-multi-agent-orchestration.md): code patterns are route-on-structured-output, chain (research → outline → draft → critique → revise), evaluator loop, parallel (research-skill-rigidity-spectrum)
- [12-Factor Agents, factor 8](sources/humanlayer-12-factor-agents-own-your-control-flow.md): the model returns the next-step intent, a code switch decides whether to execute and loop or break for human approval (research-skill-rigidity-spectrum)
- [Writing effective tools for agents](sources/anthropic-writing-tools-for-agents.md): consolidate multi-step procedures into one tool (`schedule_event`); tools are "a contract between deterministic systems and non-deterministic agents" (research-skill-rigidity-spectrum)
- [Of course you can build dynamic AI agents with Temporal](sources/temporal-dynamic-ai-agents.md): orchestration deterministic, the plan and tool calls "completely non-deterministic"; the model's choices are replayed from history (research-skill-rigidity-spectrum)
- [Agent Development Kit (ADK) documentation](sources/google-adk-docs.md): workflow agents run sub-agents "without consulting an AI model"; ADK 2.0 graphs combine "AI reasoning with deterministic code logic" (research-skill-rigidity-spectrum)
- [Interrupts (LangGraph)](sources/langchain-langgraph-interrupts.md): the human gate is a code-placed `interrupt()` node over a durable checkpoint (research-skill-rigidity-spectrum)

## gate-judge-separation: Where a gate fires vs who judges it
The enforcement point of a check (a fixed hook event, tripwire or graph node, fail-open or fail-closed) is a separate choice from its judge (script, model, human). It matters because "make it a hook" settles that the check runs, not how it decides.
- [Automate actions with hooks (Claude Code)](sources/anthropic-claude-code-hooks-guide.md): command hooks give "deterministic control"; prompt and agent hooks hand the decision to a model at the same lifecycle point; a Stop hook asks "are all tasks complete?" (research-skill-rigidity-spectrum)
- [Hooks reference (Claude Code)](sources/anthropic-claude-code-hooks-reference.md): decisions allow/deny/ask/defer; only `exit 2` blocks; fail-open unless `onFailure: block` (research-skill-rigidity-spectrum)
- [Configure permissions (Claude Agent SDK)](sources/anthropic-agent-sdk-permissions.md): ordered stack hooks → deny → ask → mode (incl. model-classifier auto) → allow → `canUseTool` callback (research-skill-rigidity-spectrum)
- [Guardrails (OpenAI Agents SDK)](sources/openai-agents-sdk-guardrails.md): the same tripwire can be driven by a cheap agent, a classifier or a function; parallel by default, blocking opt-in (research-skill-rigidity-spectrum)
- [Demystifying evals for AI agents](sources/anthropic-demystifying-evals-ai-agents.md): code graders "where possible", model "where necessary", human "sparingly for validation"; grade the outcome, not the path (research-skill-rigidity-spectrum)
- [Graders (OpenAI)](sources/openai-graders-guide.md): string check → similarity → Python → model judge "when code falls short"; calibrate against experts; watch for grader hacking (research-skill-rigidity-spectrum)
- [Define outcomes (Claude Managed Agents)](sources/anthropic-managed-agents-define-outcomes.md): the harness sets up a grader in a separate context; per-criterion markdown rubric; iterate to `satisfied` or `max_iterations` (research-skill-rigidity-spectrum)
- [Design topics as mini-agents (Copilot Studio)](sources/microsoft-copilot-studio-topics-as-mini-agents.md): Power Fx and entity validation "as reliable as code, so business rules and compliance constraints are respected even when the rest of the plan is generated" (research-skill-rigidity-spectrum)
- [LLM Evaluators Recognize and Favor Their Own Generations](sources/arxiv-llm-evaluators-favor-own-generations.md): the drafting model should not be the judging model (research-skill-rigidity-spectrum)
- [Define success criteria and build evaluations](sources/claude-platform-define-success-and-evaluations.md): code-based "fastest and most reliable", human "avoid if possible", LLM "test to ensure reliability first, then scale" (research-skill-rigidity-spectrum)
- [Claude Code permission modes](sources/anthropic-claude-code-permission-modes-docs.md): auto-mode classifier sees user messages, tool calls and CLAUDE.md but not tool results; pauses after 3 consecutive or 20 total blocks (research-skill-rigidity-spectrum)
- [VS Code agent approvals](sources/vscode-copilot-agent-approvals-and-permissions.md): Assisted permissions LLM judge "can make mistakes in its risk assessment"; terminal auto-approval "not a security boundary" (research-skill-rigidity-spectrum)

## work-structure-spectrum: Work structure spectrum (unstructured exploration to task-specific workflow)
- [Orchestrate agent behavior with generative AI (Copilot Studio)](sources/microsoft-copilot-studio-generative-orchestration.md): one toggle between classic (trigger-phrase dialog trees, author-written questions) and generative (model picks topics, tools and knowledge; generates questions); generative is the default; admins can force classic (research-skill-rigidity-spectrum)
- [What is an AI agent? (LangChain)](sources/langchain-what-is-an-agent.md): agent = LLM "decide[s] the control flow"; "Autonomy is a spectrum" across the step's output, the next step, and the available steps (research-skill-rigidity-spectrum)
- [Build skills (OpenAI Codex)](sources/openai-codex-skills-docs.md): "Prefer instructions over scripts unless you need deterministic behavior or external tooling" (research-skill-rigidity-spectrum)
- [I think "agent" may finally have a widely enough agreed upon definition](sources/simonwillison-agents-definition.md): "runs tools in a loop to achieve a goal", with a stopping condition rather than a step list (research-skill-rigidity-spectrum)

## human-review-gates: Human review gates on agent output
- [Minions Part 2](sources/stripe-minions-part-2.md): after the second CI run "we send the branch back to its human operator"; all PRs human-reviewed (research-skill-rigidity-spectrum)
- [Interrupts (LangGraph)](sources/langchain-langgraph-interrupts.md): four human-gate patterns (approve/reject, edit state, review tool call, validate input) (research-skill-rigidity-spectrum)
- [Microsoft Agent Framework overview](sources/microsoft-agent-framework-overview.md): approval-required tools "pause the workflow for human review before execution" (research-skill-rigidity-spectrum)
- [Configure permissions (Claude Agent SDK)](sources/anthropic-agent-sdk-permissions.md): plan mode sends every edit to the callback, and subagents inherit it "so that handing work to one doesn't get around reviewing the plan first" (research-skill-rigidity-spectrum)
- [About protected branches](sources/github-docs-protected-branches.md): required approvals, code-owner review, stale-approval dismissal, approval from someone other than the last pusher, conversation resolution (research-skill-rigidity-spectrum)
- [Hooks (Kiro docs)](sources/kiro-hooks-docs.md): the same trigger can run a shell command (deterministic) or inject an agent prompt (advisory) (research-skill-rigidity-spectrum)
- [Orchestrate teams of Claude Code sessions](sources/anthropic-claude-code-agent-teams.md): TaskCreated/TaskCompleted hooks can block with exit 2; teammate plan approval is automatic by default, not a human gate (research-skill-rigidity-spectrum)
- [Risks and mitigations for GitHub Copilot cloud agent](sources/github-copilot-cloud-agent-risks.md): requester cannot approve own agent PR; workflows need "Approve and run" by a human (research-skill-rigidity-spectrum)
- [Agent Interaction Guidelines](sources/linear-agent-interaction-guidelines.md): "the final responsibility should always remain with a human"; delegated issue names a responsible human (research-skill-rigidity-spectrum)
- [Agent Skills (Osmani)](sources/addyosmani-agent-skills.md): "Sounds good" and "whatever you think is best" are listed as not-yes (research-skill-rigidity-spectrum)
- [Superpowers skills](sources/obra-superpowers-skills.md): no code, scaffolding or dependencies until the design doc is approved (research-skill-rigidity-spectrum)
- [Harness engineering for coding agent users](sources/fowler-bockeler-harness-engineering.md): humans run a steering loop that improves guides and sensors when issues recur (research-skill-rigidity-spectrum)
- [Large Language Models are not Fair Evaluators](sources/arxiv-llms-are-not-fair-evaluators.md): escalate to a human only where the judge's verdict is unstable across orderings (research-skill-rigidity-spectrum)
- [Knowledge (Devin docs)](sources/devin-docs-knowledge.md): every agent-proposed lesson passes through the user before it is saved (research-skill-rigidity-spectrum)

## evals-autonomy-trust: Evals, autonomy sliders and earned trust
- [Configure permissions (Claude Agent SDK)](sources/anthropic-agent-sdk-permissions.md): `setPermissionMode()` mid-session to "loosen permissions as trust builds" (research-skill-rigidity-spectrum)
- [Demystifying evals for AI agents](sources/anthropic-demystifying-evals-ai-agents.md): capability evals "graduate" into regression suites at a near-100% pass rate (research-skill-rigidity-spectrum)
- [Permission modes](sources/anthropic-claude-code-permission-modes-docs.md): six modes; auto mode runs rules, then built-in approvals, then a classifier; pauses after 3 consecutive or 20 total blocks (research-skill-rigidity-spectrum)
- [Devin 2.1](sources/cognition-devin-2-1-confidence.md): green/yellow/red self-rating; clarifying questions below green; vendor claims green doubles merged-PR odds (research-skill-rigidity-spectrum)
- [Using LLM-as-a-Judge](sources/hamel-llm-as-judge-guide.md): binary pass/fail with critiques; over 90% expert agreement in three rounds (Honeycomb) (research-skill-rigidity-spectrum)
- [Superpowers: How I'm using coding agents](sources/fsck-jesse-vincent-superpowers.md): quiz tests gave perfect scores and no insight; pressure scenarios found failures (research-skill-rigidity-spectrum)
- [Agent Skills (Osmani)](sources/addyosmani-agent-skills.md): `/build auto` approves the plan once and removes stepping between tasks, not verification (research-skill-rigidity-spectrum)
- [Inside the Development Workflow of Claude Code's Creator](sources/infoq-claude-code-creator-workflow.md): plan mode, then auto-accept; pre-approved safe commands instead of skipping permissions (research-skill-rigidity-spectrum)
- [Skill authoring best practices](sources/anthropic-skill-authoring-best-practices.md): evaluation-driven development: baseline without the skill, three scenarios, minimal instructions (research-skill-rigidity-spectrum)
- [Judging LLM-as-a-Judge](sources/arxiv-zheng-judging-llm-as-a-judge.md): GPT-4 agrees with experts 85% vs human-human 81% on MT-Bench (research-skill-rigidity-spectrum)
- [Define success criteria and build evaluations](sources/claude-platform-define-success-and-evaluations.md): "prioritize volume over quality" in automated grading (research-skill-rigidity-spectrum)

## policy-enforcement-fail-open: Agent policy layers that fail open
- [Hooks reference (Claude Code)](sources/anthropic-claude-code-hooks-reference.md): a timed-out hook "doesn't block the tool call"; exit 1 is non-blocking; "If your hook is meant to enforce a policy, use exit 2" (research-skill-rigidity-spectrum)
- [Configure permissions (Claude Agent SDK)](sources/anthropic-agent-sdk-permissions.md): checks in `canUseTool` are "silently bypassed" for auto-approved tools (research-skill-rigidity-spectrum)
- [Guardrails (OpenAI Agents SDK)](sources/openai-agents-sdk-guardrails.md): with parallel guardrails, the agent may already have run tools before the tripwire fires (research-skill-rigidity-spectrum)

## process-artifacts-as-coordination: Process artifacts as the coordination layer
Decision logs, assumption registers, task lists, checklists and change folders are what let several people and agents hold one quality bar over days or weeks. Their content is judgment; their structure is where deterministic gates attach.
- [Context Graphs: AI's Trillion-Dollar Opportunity](sources/foundationcapital-context-graphs.md): defines a context graph as decision traces (inputs, policy version, exceptions, precedents, approver) captured at decision time; no data offered (research-skill-rigidity-spectrum)
- [Documenting Architecture Decisions](sources/nygard-documenting-architecture-decisions.md): ADRs exist so rotating contributors neither blindly accept nor blindly reverse past decisions; six to ten developers found them useful (research-skill-rigidity-spectrum)
- [Design Docs at Google](sources/industrialempathy-design-docs-at-google.md): design docs serve consensus, knowledge spread and organisational memory; revisited a year or two later (research-skill-rigidity-spectrum)
- [Assumption Testing](sources/producttalk-torres-assumption-testing.md): each assumption test logged with six fields including pre-set success criteria and how the team acted (research-skill-rigidity-spectrum)
- [Orchestrate teams of Claude Code sessions](sources/anthropic-claude-code-agent-teams.md): shared task list with dependency blocking and file-locked claiming; docs admit task status can lag (research-skill-rigidity-spectrum)
- [MetaGPT](sources/arxiv-metagpt.md): structured PRD, then design, then task handoffs; full role team 4.0 executability vs 1.0 for a lone engineer agent (research-skill-rigidity-spectrum)
- [Agent interaction (Linear)](sources/linear-developers-agent-interaction.md): agent runs as sessions on issues with typed elicitation activities and a checklist plan humans can watch (research-skill-rigidity-spectrum)
- [OpenSpec](sources/github-openspec-readme.md): per-change folder (proposal, spec deltas, design, tasks) archived into canonical specs (research-skill-rigidity-spectrum)
- [The 2020 Scrum Guide](sources/scrumguides-scrum-guide-2020.md): Definition of Done gives everyone a shared understanding of what is complete; no Definition of Ready in the guide (research-skill-rigidity-spectrum)
- [An insider look at Amazon's culture and processes](sources/aboutamazon-insider-look-working-backwards.md): PR/FAQ review minutes circulated after each meeting; document stays live after approval (research-skill-rigidity-spectrum)

## checklist-implementation-fidelity: Checklists work through the behaviour they force
A checklist's effect depends on whether the team actually does what it demands; mandated or ticked-off checklists show little effect.
- [A surgical safety checklist to reduce morbidity and mortality](sources/nejm-haynes-surgical-safety-checklist.md): deaths 1.5% to 0.8% and complications 11.0% to 7.0% across 8 hospitals (before/after) (research-skill-rigidity-spectrum)
- [Introduction of surgical safety checklists in Ontario](sources/nejm-urbach-ontario-surgical-checklists.md): mandated adoption in 101 hospitals, about 215k procedures, no significant change in mortality or complications (research-skill-rigidity-spectrum)
- [Multiple interacting factors influence adherence](sources/plosone-gagliardi-checklist-adherence.md): checklists "often inaccurately documented as complete" and modified until key interactions vanished (research-skill-rigidity-spectrum)
- [Do explicit review strategies improve code review performance?](sources/emse-goncalves-explicit-review-strategies.md): checklist and guided-checklist effects on code review were weak and task-dependent (research-skill-rigidity-spectrum)
- [A systematic review of validity evidence for checklists versus global rating scales](sources/medu-ilgen-checklists-vs-global-rating-scales.md): "each task requires a separate checklist" while a rating scale spans tasks (research-skill-rigidity-spectrum)
- [Human Factors of Flight-Deck Checklists](sources/nasa-degani-wiener-flight-deck-checklists.md): non-use and improper use cited as probable cause in accidents; production pressure degrades use (research-skill-rigidity-spectrum)

## stale-records-mislead-agents: Stale process records become wrong instructions
Once agents read decision records as instructions, an outdated record misleads them; record sets need freshness controls.
- [Coding agents love decision records](sources/duncandavidson-coding-agents-love-decision-records.md): agent kept an obsolete abstraction an ADR marked mandatory; agents bloated ADRs when asked to update them (research-skill-rigidity-spectrum)
- [Stale docs are prompt injection you wrote yourself](sources/codeminer42-stale-docs-prompt-injection.md): CI structure and drift checks, AI code-vs-record review and human attestation; 24 code comments pointed to the wrong record before controls (research-skill-rigidity-spectrum)

## decision-rights-for-agents: Decision-rights schemes applied to agents
RAPID, DACI and risk-owner schemes place agents as recommenders, inputs or performers, with a named human as decider.
- [RAPID Decision Making](sources/bain-rapid-decision-making.md): one decider, one recommender; Agree is not a veto; no evidence offered (research-skill-rigidity-spectrum)
- [The Four Big Risks](sources/svpg-four-big-risks.md): each risk has a named human owner, which gives a risk register its owner column (research-skill-rigidity-spectrum)
- [Why Do Multi-Agent LLM Systems Fail?](sources/arxiv-why-multi-agent-llm-systems-fail.md): clearer role specs (including the CEO agent's final say) gave +9.4% task success in ChatDev (research-skill-rigidity-spectrum)
- [Claude Code permission modes](sources/anthropic-claude-code-permission-modes-docs.md): six modes; auto mode substitutes a classifier for the human; deny rules bind in every mode; admins lock modes via managed settings; auto is now the interactive default (research-skill-rigidity-spectrum)
- [VS Code agent approvals](sources/vscode-copilot-agent-approvals-and-permissions.md): Manual, LLM-judge Assisted, Allow all; approvals scoped to use, session, workspace or global; sandbox independent of level (research-skill-rigidity-spectrum)
- [People + AI Guidebook: User Needs](sources/pair-guidebook-user-needs-automate-vs-augment.md): automate what people want to delegate, augment what they want to keep; preview, edit, undo even when automating (research-skill-rigidity-spectrum)
- [When combinations of humans and AI are useful](sources/arxiv-vaccaro-when-human-ai-combinations-are-useful.md): give the decision to whichever party is better alone; blend only on creation tasks (research-skill-rigidity-spectrum)
- [The bar raiser program](sources/metaview-bar-raiser-program.md): the reviewer's authority comes from not owning the deadline; objections and overrides are recorded (research-skill-rigidity-spectrum)

## red-team-stance: Structured critique as a procedure
Fixed rituals for open critique (premortem, silent-read reviews) that a PM agent can run or prompt.
- [Performing a Project Premortem](sources/hbr-klein-project-premortem.md): assume the project failed and list reasons; supporting research is thin (about 30% more reasons generated, not better accuracy, per secondary critiques) (research-skill-rigidity-spectrum)
- [An insider look at Amazon's culture and processes](sources/aboutamazon-insider-look-working-backwards.md): silent reading, senior attendees speak last, most PR/FAQs not approved (research-skill-rigidity-spectrum)
- [LLM-Powered Devil's Advocate](sources/acm-chiang-llm-powered-devils-advocate-iui2024.md): advocates arguing against the AI's recommendation promoted appropriate reliance without raising workload; interactive ones rated higher (research-skill-rigidity-spectrum)
- [The bar raiser program](sources/metaview-bar-raiser-program.md): independence from the deadline and written answers to objections matter more than the veto; no outcome data exists (research-skill-rigidity-spectrum)
- [How we built our multi-agent research system](sources/anthropic-multi-agent-research-system.md): no runtime critic; LLM judge is offline; critique is aimed at the agent's own prompts and tools (research-skill-rigidity-spectrum)

## verification-capacity-gap: Verification capacity is the new limit
- [Why Do Multi-Agent LLM Systems Fail?](sources/arxiv-why-multi-agent-llm-systems-fail.md): about 24% of failure labels are verification failures; an objective-level verification step gave +15.6% (research-skill-rigidity-spectrum)
- [Multiple interacting factors influence adherence](sources/plosone-gagliardi-checklist-adherence.md): little organisational monitoring or feedback on whether checklists were really done (research-skill-rigidity-spectrum)
- [Harness engineering for coding agent users](sources/fowler-bockeler-harness-engineering.md): no sensor reliably catches misdiagnosis, unnecessary features or misunderstood instructions (research-skill-rigidity-spectrum)

## decision-rationale-records: Decision rationale records
- [Documenting Architecture Decisions](sources/nygard-documenting-architecture-decisions.md): original ADR format and supersede-never-edit rule (research-skill-rigidity-spectrum)
- [Design Docs at Google](sources/industrialempathy-design-docs-at-google.md): "alternatives considered" called one of the most important sections (research-skill-rigidity-spectrum)
- [Stale docs are prompt injection you wrote yourself](sources/codeminer42-stale-docs-prompt-injection.md): index generated from frontmatter, leaves out superseded records; CI warns above 800 words (research-skill-rigidity-spectrum)

## docs-as-code-prd: PRDs and specs as files in the repo
- [Steering (Kiro docs)](sources/kiro-steering-docs.md): product.md, tech.md, structure.md with always, fileMatch, manual and auto inclusion modes (research-skill-rigidity-spectrum)
- [Tessl documentation](sources/tessl-docs-overview.md): Tessl now presents a skills registry with governance scoring and with/without-context evals, not spec-as-source (research-skill-rigidity-spectrum)

## shared-persistent-sessions: Shared, persistent, multi-user agent sessions
- [Orchestrate teams of Claude Code sessions](sources/anthropic-claude-code-agent-teams.md): lead plus teammates with mailboxes; no session resumption for in-process teammates; one team per session (research-skill-rigidity-spectrum)
- [Agent interaction (Linear)](sources/linear-developers-agent-interaction.md): session states set from the agent's last activity; 10-second first-response rule (research-skill-rigidity-spectrum)

## rules-vs-judgment-encoding: Encoding standards as rules vs as reasons and judgment
How skills, rule files and model specs choose between fixed rules, scripts and checks on one side and explained criteria and judgment on the other, and which steps practitioners make rigid. Matters for which PM-skill standards become hard gates and which stay as guidance.
- [Skill authoring best practices](sources/anthropic-skill-authoring-best-practices.md): match specificity to "fragility and variability": high, medium and low freedom; narrow bridge vs open field (research-skill-rigidity-spectrum)
- [skill-creator SKILL.md](sources/anthropics-skills-skill-creator-skill-md.md): all-caps ALWAYS/NEVER and "super rigid structures" are "a yellow flag"; explain the why (research-skill-rigidity-spectrum)
- [Claude's new constitution](sources/anthropic-claude-new-constitution.md): judgment with reasons by default; rules only as hard constraints; a box-ticking rule can generalise badly (research-skill-rigidity-spectrum)
- [docx SKILL.md](sources/anthropics-skills-docx.md): low-freedom end: exact unpack, edit, validate commands with XSD script gates, still with reasons (research-skill-rigidity-spectrum)
- [frontend-design SKILL.md](sources/anthropics-skills-frontend-design.md): taste encoded as persona, five named AI-default clusters to avoid, and plan-review-critique (research-skill-rigidity-spectrum)
- [Superpowers skills](sources/obra-superpowers-skills.md): mandatory invocation, an "iron law" and rationalisation tables where the model is tempted to skip discipline (research-skill-rigidity-spectrum)
- [Superpowers: How I'm using coding agents](sources/fsck-jesse-vincent-superpowers.md): Cialdini persuasion principles in skill wording; pressure-scenario tests replaced quizzes (research-skill-rigidity-spectrum)
- [vercel-labs/agent-skills](sources/vercel-labs-agent-skills-repo.md): 70 impact-ranked rules with incorrect/correct examples; thin skills fetch a central rule list each run (research-skill-rigidity-spectrum)
- [awesome-cursorrules](sources/patrickjs-awesome-cursorrules.md): roughly 210 always-on rule files of bare imperatives; newer files encode stance ("warn once, then comply") (research-skill-rigidity-spectrum)
- [knowledge-work-plugins PM skills](sources/anthropics-kwp-pm-plugin-skills.md): PM skills hold all standards as prose criteria; no script or schema gate (research-skill-rigidity-spectrum)
- [Agent Skills (Osmani)](sources/addyosmani-agent-skills.md): "the judgement moves out of your head and into checks"; CONSTRAINTS.md with chosen numbers and diff watch (research-skill-rigidity-spectrum)
- [Harness engineering for coding agent users](sources/fowler-bockeler-harness-engineering.md): guides vs sensors x computational vs inferential; skills appear as both inferential guides and sensors (research-skill-rigidity-spectrum)
- [12-Factor Agents factors 2 and 8](sources/humanlayer-12-factor-agents-own-your-control-flow.md): model proposes a tool intent, code decides continue, pause or approve by tool risk (research-skill-rigidity-spectrum)
- [Claude Skills are awesome](sources/simonwillison-claude-skills-bigger-than-mcp.md): loose instructions plus a validator script for the hard limit (Slack GIF size) (research-skill-rigidity-spectrum)
- [Using LLM-as-a-Judge](sources/hamel-llm-as-judge-guide.md): criteria drift: experts find their standard while grading, so rubrics are grown from critiques (research-skill-rigidity-spectrum)
- [Inside the Development Workflow of Claude Code's Creator](sources/infoq-claude-code-creator-workflow.md): deterministic PostToolUse format hook takes a class of errors out of model judgment (research-skill-rigidity-spectrum)

## human-thinking-skills: Skills designed to make the human think
Skills whose output is better human judgment (questions, critique, reflection prompts) rather than a deliverable, and the design rules they share. Bears on the "up-level the PM" job.
- [discernment-nudge SKILL.md](sources/anthropics-skills-discernment-nudge.md): two or three specific follow-up questions on a consequential answer; once per conversation; "silence is the right default" (research-skill-rigidity-spectrum)
- [doc-coauthoring SKILL.md](sources/anthropics-skills-doc-coauthoring.md): per section: 5-10 questions, options, user curates with reasons; reader test with a fresh Claude (research-skill-rigidity-spectrum)
- [knowledge-work-plugins PM skills](sources/anthropics-kwp-pm-plugin-skills.md): product-brainstorming: "Your job is not to generate deliverables"; four modes; named PM anti-patterns (research-skill-rigidity-spectrum)
- [Superpowers skills](sources/obra-superpowers-skills.md): brainstorming: one question at a time, two or three approaches with trade-offs, hard gate before building (research-skill-rigidity-spectrum)
- [Agent Skills (Osmani)](sources/addyosmani-agent-skills.md): interview-me: hypothesis plus confidence number, one question with a guess attached, explicit-yes gate (research-skill-rigidity-spectrum)
- [Generative AI without guardrails can harm learning](sources/pnas-bastani-generative-ai-can-harm-learning.md): the same model with tutor prompts (hints, not answers) protected learning; stance, not presence, decided the outcome (research-skill-rigidity-spectrum)
- [Do People Engage Cognitively with AI?](sources/arxiv-gajos-mamykina-ai-assistance-incidental-learning.md): explanation without recommendation produced learning and better decisions; recommendation plus explanation produced no learning (research-skill-rigidity-spectrum)
- [Don't Just Tell Me, Ask Me](sources/acm-danry-dont-just-tell-me-ask-me-chi2023.md): N=204; AI-framed questions beat causal explanations for spotting flawed logic, even vs an always-correct AI (research-skill-rigidity-spectrum)
- [Tutor CoPilot](sources/arxiv-wang-tutor-copilot-rct.md): RCT, 900 tutors; +4 points mastery, +9 for weaker tutors; tutors asked more guiding questions, gave fewer answers; about $20 per tutor per year (research-skill-rigidity-spectrum)
- [SocraticLM](sources/neurips-liu-socraticlm.md): Socratic stance fine-tuned on 35K dialogues and scored on a five-dimension pedagogy rubric; beats GPT-4 by 12% on teaching (research-skill-rigidity-spectrum)
- [Scaling AI in Education: Khanmigo](sources/aiengineer-jansepar-khanmigo-case-study.md): no intervention before submission, infer the student's path first, refuse to write the next paragraph; costs are latency, eval coverage, 70% grader accuracy (research-skill-rigidity-spectrum)
- [Homogenization Effects of LLMs on Creative Ideation](sources/arxiv-anderson-homogenization-effects-llm-ideation.md): ChatGPT users felt less responsible for their ideas (research-skill-rigidity-spectrum)
- [Modes for Creative Human-Computer Collaboration](sources/iccc-kantosalo-toivonen-alternating-cocreativity.md): alternating vs task-divided co-creativity as the two ways to share an artifact (research-skill-rigidity-spectrum)
- [Human-AI Interaction Designs for Co-Creative Systems](sources/arxiv-rezwana-maher-human-ai-interaction-designs-cocreative.md): N=38; an AI that explains its contributions is seen as more reliable and raises engagement (research-skill-rigidity-spectrum)

## prd-agents: PRD and spec writing/review as an agent job
- [knowledge-work-plugins PM skills](sources/anthropics-kwp-pm-plugin-skills.md): write-spec: 5-step flow, 8-section PRD, P0/P1/P2 with acceptance criteria, open questions tagged by owner (research-skill-rigidity-spectrum)
- [doc-coauthoring SKILL.md](sources/anthropics-skills-doc-coauthoring.md): offers a structured PRD/RFC workflow or freeform; human picks; sub-agent reader test (research-skill-rigidity-spectrum)

## agent-led-intent-shaping: Agents shape intent, not only execute it
- [Agent Skills (Osmani)](sources/addyosmani-agent-skills.md): "If you didn't have to justify this to anyone, what would you actually want?" (research-skill-rigidity-spectrum)
- [Devin 2.1](sources/cognition-devin-2-1-confidence.md): low self-confidence triggers clarifying questions before work (research-skill-rigidity-spectrum)

## human-judgment-pm-jobs: PM jobs that stay human-led
- [discernment-nudge SKILL.md](sources/anthropics-skills-discernment-nudge.md): skip the nudge for takes ("weighed, not fact-checked") and user-supplied material; avoid paternalism (research-skill-rigidity-spectrum)

## tacit-knowledge-capture: Capturing tacit knowledge from people for agents
- [Using LLM-as-a-Judge](sources/hamel-llm-as-judge-guide.md): one principal expert's critiques, detailed enough for a new hire, become judge examples (research-skill-rigidity-spectrum)
- [doc-coauthoring SKILL.md](sources/anthropics-skills-doc-coauthoring.md): info dump asks for team dynamics, past incidents, politics and rejected alternatives (research-skill-rigidity-spectrum)
- [HealthBench](sources/arxiv-openai-healthbench.md): 262 physicians' judgment captured as 48,562 written criteria; consensus filter for the contested part (research-skill-rigidity-spectrum)

## org-learning-loop: One person's win becomes everyone's baseline
- [Inside the Development Workflow of Claude Code's Creator](sources/infoq-claude-code-creator-workflow.md): shared CLAUDE.md in git (~2.5k tokens) updated from mistakes and PR learnings (research-skill-rigidity-spectrum)
- [Superpowers: How I'm using coding agents](sources/fsck-jesse-vincent-superpowers.md): skills mined from a book and about 2,249 past memory files (research-skill-rigidity-spectrum)

## risk-sloped-review: Human review sloped to risk
- [Permission modes](sources/anthropic-claude-code-permission-modes-docs.md): deny rules hold in every mode; broad allow rules are dropped when a classifier approves (research-skill-rigidity-spectrum)
- [awesome-cursorrules](sources/patrickjs-awesome-cursorrules.md): "Match Verification to Risk": syntax check, manual trace, or written scenario by change type (research-skill-rigidity-spectrum)

## identity-delegation: Identity and delegation (on-behalf-of)
- [Agent Interaction Guidelines](sources/linear-agent-interaction-guidelines.md): agents disclose agent status and use the same actions a human would (research-skill-rigidity-spectrum)

## skill-standards: Skill standards
- [Skill authoring best practices](sources/anthropic-skill-authoring-best-practices.md): SKILL.md under 500 lines; references one level deep; scripts "solve, don't defer" (research-skill-rigidity-spectrum)
- [Claude Skills are awesome](sources/simonwillison-claude-skills-bigger-than-mcp.md): Markdown plus YAML plus optional scripts; portable across Codex CLI and Gemini CLI (research-skill-rigidity-spectrum)

## standard-form-spectrum: The form a standard takes
How a quality bar is written down: completeness checklist, rubric of criteria needing judgment, exemplars and references, explained principles, or left as unencoded taste; and how the form changes what a model or human judge can do with it.
- [A systematic review of validity evidence for checklists versus global rating scales in simulation-based assessment](sources/medu-ilgen-checklists-vs-global-rating-scales.md): 45 studies; inter-rater reliability equal (0.81 checklist vs 0.78 rating scale) but rating scales more internally consistent (0.92 vs 0.66) and reusable across tasks; use both (research-skill-rigidity-spectrum)
- [TICKing All the Boxes](sources/arxiv-tick-checklist-evaluation.md): generated yes/no checklists raised judge-human agreement 46.4% to 52.2% and human inter-rater agreement 0.194 to 0.256 (research-skill-rigidity-spectrum)
- [Rubrics as Rewards](sources/arxiv-rubrics-as-rewards.md): four rubric rules (expert-grounded, comprehensive with pitfalls, importance-weighted, self-contained); holistic reading of checkable items beat fixed weighted sums; reference-grounded rubrics beat reference-free (35.9% vs 32.0%) (research-skill-rigidity-spectrum)
- [HealthBench](sources/arxiv-openai-healthbench.md): 262 physicians wrote 48,562 weighted (-10..+10) criteria for 5,000 conversations; model grader F1 0.709, matching physician-physician agreement; Consensus subset keeps only majority-agreed criteria (research-skill-rigidity-spectrum)
- [PaperBench](sources/arxiv-openai-paperbench.md): weighted rubric trees with pass/fail leaves for partial credit; "multiple weeks per paper" to write with the author; judge F1 0.83 at ~$66 per paper (research-skill-rigidity-spectrum)
- [Judging LLM-as-a-Judge](sources/arxiv-zheng-judging-llm-as-a-judge.md): a reference exemplar cut judge math-grading failures 70% to 15% vs 30% for chain-of-thought (research-skill-rigidity-spectrum)
- [Prometheus](sources/arxiv-prometheus-fine-grained-evaluation.md): evaluator performs best given both a score rubric and a reference answer; 0.897 Pearson with humans on 45 custom rubrics (research-skill-rigidity-spectrum)
- [G-Eval](sources/arxiv-g-eval.md): one-line criterion expanded by the model into evaluation steps; 0.514 Spearman on summarisation (research-skill-rigidity-spectrum)
- [Check-Eval](sources/arxiv-check-eval.md): second checklist-generation evaluator reporting higher human correlation than G-Eval (research-skill-rigidity-spectrum)
- [Prompting best practices (Use examples effectively)](sources/claude-platform-prompting-best-practices-examples.md): examples are "one of the most reliable ways to steer ... format, tone, and structure"; 3-5, relevant, diverse, tagged (research-skill-rigidity-spectrum)
- [Define success criteria and build evaluations](sources/claude-platform-define-success-and-evaluations.md): rubric lines as checkable statements with a consequence; several rubrics per criterion; grading ladder code, LLM, human (research-skill-rigidity-spectrum)
- [Graders (OpenAI API docs)](sources/openai-graders-guide.md): rubric in the grader prompt with step-by-step instructions and many examples, numeric range and pass threshold (research-skill-rigidity-spectrum)
- [frontend-design SKILL.md](sources/anthropics-skills-frontend-design.md): taste encoded as persona, a few hard rules, named anti-patterns and a forced-choice process; no rubric, no exemplars (research-skill-rigidity-spectrum)
- [Claude's new constitution](sources/anthropic-claude-new-constitution.md): explained principles over rules because rules "can be applied poorly in unanticipated situations"; few hard constraints; priority order (research-skill-rigidity-spectrum)
- [3 Principles for Designing Agent Skills](sources/block-eng-3-principles-agent-skills.md): "write a constitution, not a suggestion" as an explicit-constraint list beside scripted binary checks (research-skill-rigidity-spectrum)
- [Taste for Makers](sources/paulgraham-taste-for-makers.md): fourteen criteria of good design that need judgment to apply and are acquired by practice (research-skill-rigidity-spectrum)
- [Human Factors of Flight-Deck Checklists](sources/nasa-degani-wiener-flight-deck-checklists.md): the checklist as a designed artifact shaped by regulator, manufacturer, airline culture and production pressure (research-skill-rigidity-spectrum)

## model-judge-biases: Known biases of model judges and their mitigations
Position, verbosity, self-preference and weak reasoning grading in LLM judges, and the procedural fixes (order swapping, length control, judge separation, references, escalation) that a model-judged gate needs.
- [Judging LLM-as-a-Judge](sources/arxiv-zheng-judging-llm-as-a-judge.md): position consistency GPT-4 65%, Claude-v1 23.8%; repetitive-list attack fooled two of three judges 91.3%; self-favouring +10 and +25 points; swap-and-tie, few-shot (65% to 77.5%, 4x cost), reference grading (research-skill-rigidity-spectrum)
- [Large Language Models are not Fair Evaluators](sources/arxiv-llms-are-not-fair-evaluators.md): order swap let Vicuna-13B beat ChatGPT 66 of 80; entropy across orderings triggers human review (research-skill-rigidity-spectrum)
- [LLM Evaluators Recognize and Favor Their Own Generations](sources/arxiv-llm-evaluators-favor-own-generations.md): self-preference tracks self-recognition; grade with a different model (research-skill-rigidity-spectrum)
- [Length-Controlled AlpacaEval](sources/arxiv-length-controlled-alpacaeval.md): regressing out length raised Arena correlation 0.94 to 0.98 (research-skill-rigidity-spectrum)
- [G-Eval](sources/arxiv-g-eval.md): authors flag bias toward model-written text (research-skill-rigidity-spectrum)
- [Rubrics as Rewards](sources/arxiv-rubrics-as-rewards.md): structured rubrics reduce variance across judge sizes vs Likert scoring (research-skill-rigidity-spectrum)
- [HealthBench](sources/arxiv-openai-healthbench.md): grader meta-evaluated on 60,896 physician-graded items; agreement ceiling equals expert-expert agreement (research-skill-rigidity-spectrum)
- [PaperBench](sources/arxiv-openai-paperbench.md): judge F1 ranges 0.59 to 0.84 across models; cost 0.83 F1 at $66 vs 0.84 at $830 (research-skill-rigidity-spectrum)
- [TICKing All the Boxes](sources/arxiv-tick-checklist-evaluation.md): checklists steady human raters too (0.194 to 0.256 agreement) (research-skill-rigidity-spectrum)

## skill-improvement-loops: How skills and agent instructions get better
The mechanisms by which a skill, prompt or instruction file changes over time: static, curated from human corrections, driven by an eval, or rewritten by the agent itself; and the signal each depends on.
- [Agentic Context Engineering](sources/arxiv-agentic-context-engineering.md): names brevity bias and context collapse in whole-file rewrites; incremental deltas from generate/reflect/curate roles; +10.6% on AppWorld without labels (research-skill-rigidity-spectrum)
- [Dynamic Cheatsheet](sources/arxiv-dynamic-cheatsheet.md): self-curated memory took GPT-4o on Game of 24 from 10% to 99%; limits: self-curation without labels, persisted errors, weak-model gains small, tokens 370 to 1,831 (research-skill-rigidity-spectrum)
- [Reflexion](sources/arxiv-reflexion.md): stored verbal reflection between trials; 91% vs 80% on HumanEval; needs a feedback signal (research-skill-rigidity-spectrum)
- [Voyager](sources/arxiv-voyager-skill-library.md): ever-growing library of verified executable skills; transfers to new worlds; 15.3x faster milestones (research-skill-rigidity-spectrum)
- [GEPA](sources/arxiv-gepa-reflective-prompt-evolution.md): prose diagnosis of trajectories beats RL by 6% average with up to 35x fewer rollouts; still eval-driven (research-skill-rigidity-spectrum)
- [DSPy](sources/arxiv-dspy.md): prompts compiled against a metric; bootstrapped demonstrations beat expert-written by 5-46% (research-skill-rigidity-spectrum)
- [autoresearch](sources/github-karpathy-autoresearch.md): fixed evaluator file, one mutable work file, human edits only program.md; ~100 experiments overnight (research-skill-rigidity-spectrum)
- [Knowledge (Devin docs)](sources/devin-docs-knowledge.md): agent proposes a Knowledge item from chat corrections; user edits, saves or dismisses; Knowledge migrating to Skills (research-skill-rigidity-spectrum)
- [Claude Code /insights](sources/vincentqiao-claude-code-insights.md): transcript analysis with friction categories and proposed CLAUDE.md lines; third-party description only (research-skill-rigidity-spectrum)
- [TICKing All the Boxes](sources/arxiv-tick-checklist-evaluation.md): Self-TICK checklist self-refinement +7.8% absolute (research-skill-rigidity-spectrum)
- [A Survey of Self-Evolving Agents](sources/arxiv-survey-self-evolving-agents.md): what/when/how taxonomy; intra- vs inter-test-time; scalar vs textual feedback (research-skill-rigidity-spectrum)

## taste-and-homogenisation: Whether taste can be encoded, and the convergence cost of model help
Where practitioners say taste lives, how far it can be written into a skill, and the evidence that model-assisted work raises the floor while narrowing the range.
- [Generative AI enhances individual creativity but reduces the collective diversity of novel content](sources/sciadv-doshi-hauser-generative-ai-creativity.md): AI story ideas raised ratings most for weaker writers; stories more similar to each other; "social dilemma" (research-skill-rigidity-spectrum)
- [Homogenization Effects of Large Language Models on Human Creative Ideation](sources/arxiv-anderson-homogenization-effects-llm-ideation.md): 36 participants; ChatGPT ideas more detailed but less distinct across users; less felt ownership (research-skill-rigidity-spectrum)
- [Does Writing with Language Models Reduce Content Diversity?](sources/arxiv-padmakumar-he-content-diversity.md): diversity loss with InstructGPT not base GPT-3, driven by the model's contributions (research-skill-rigidity-spectrum)
- [frontend-design SKILL.md](sources/anthropics-skills-frontend-design.md): the skill exists to fight the model's default aesthetic; encodes taste as named defaults to refuse (research-skill-rigidity-spectrum)
- [Taste for Makers](sources/paulgraham-taste-for-makers.md): taste is not purely subjective and is learned by practice; "very exacting taste, plus the ability to gratify it" (research-skill-rigidity-spectrum)
- [Taste is the new AI moat](sources/brighteye-guerin-taste-is-the-new-ai-moat.md): the practitioner claim that judgment and brand remain when building is cheap; no data; an anonymous counter-post says taste is clonable and distribution is the moat (research-skill-rigidity-spectrum)
- [Generative AI enhances creativity but reduces the diversity of novel content](sources/arxiv-doshi-hauser-genai-creativity-reduces-diversity.md): stories more creative (most for weaker writers) but more similar to each other (research-skill-rigidity-spectrum)
- [Homogenization Effects of LLMs on Creative Ideation](sources/arxiv-anderson-homogenization-effects-llm-ideation.md): N=36; less semantically distinct ideas across ChatGPT users than with another creativity tool (research-skill-rigidity-spectrum)
- [How People Can Create and Destroy Value with Generative AI](sources/bcg-how-people-create-and-destroy-value-with-gen-ai.md): GPT-4 users' ideas 41% less diverse (research-skill-rigidity-spectrum)
- [Your Brain on ChatGPT](sources/arxiv-kosmyna-your-brain-on-chatgpt.md): within-group homogeneity of entities and topics in LLM essays (research-skill-rigidity-spectrum)

## overreliance-and-deskilling: Overreliance and deskilling
AI assistance breeds automation bias and erodes human skill unless the design works against it; the effect grows as the AI improves. Matters because every "up-level the human" job in the project is fighting this default.
- [To Trust or to Think](sources/arxiv-bucinca-cognitive-forcing-functions.md): cognitive forcing designs cut overreliance vs explainable AI (N=199) but were least liked and helped high need-for-cognition people most (research-skill-rigidity-spectrum)
- [The Impact of Generative AI on Critical Thinking](sources/microsoft-research-lee-genai-critical-thinking-chi2025.md): 319 workers, 936 examples; confidence in GenAI predicts less critical thinking, task self-confidence more; thinking shifts to verification, integration, stewardship (research-skill-rigidity-spectrum)
- [Generative AI without guardrails can harm learning](sources/pnas-bastani-generative-ai-can-harm-learning.md): unrestricted GPT-4 +48% on practice, -17% on the unassisted exam; GPT Tutor +127% practice and most harm removed (research-skill-rigidity-spectrum)
- [How People Can Create and Destroy Value with Generative AI](sources/bcg-how-people-create-and-destroy-value-with-gen-ai.md): 758 consultants; +40% quality inside the frontier, 23 points worse outside; training made it worse (research-skill-rigidity-spectrum)
- [Falling Asleep at the Wheel](sources/hbs-dellacqua-falling-asleep-at-the-wheel.md): 181 recruiters; a 75%-accurate AI beat an 85% one because people kept checking the weaker tool (research-skill-rigidity-spectrum)
- [Endoscopist deskilling risk after exposure to AI](sources/lancet-budzyn-endoscopist-deskilling-after-ai.md): ADR in non-AI colonoscopies 28.4% to 22.4% within three months of AI; OR 0.69 (research-skill-rigidity-spectrum)
- [When combinations of humans and AI are useful](sources/arxiv-vaccaro-when-human-ai-combinations-are-useful.md): 100+ experiments; combinations averaged worse than the better party alone; losses on decision tasks, gains on creation (research-skill-rigidity-spectrum)
- [Your Brain on ChatGPT](sources/arxiv-kosmyna-your-brain-on-chatgpt.md): 54-person EEG preprint; lowest ownership and inability to quote own essay in the LLM group; weak evidence (research-skill-rigidity-spectrum)
- [Does the Whole Exceed its Parts?](sources/arxiv-bansal-does-the-whole-exceed-its-parts.md): explanations raised acceptance of AI answers including wrong ones and added no complementary gain (research-skill-rigidity-spectrum)
- [Explanations Can Reduce Overreliance](sources/arxiv-vasconcelos-explanations-can-reduce-overreliance.md): N=731; engagement is a cost-benefit choice; explanations help when they make checking cheaper (research-skill-rigidity-spectrum)
- [In Search of Verifiability](sources/arxiv-fok-weld-in-search-of-verifiability.md): explanations help only when they enable verification; most tasks resist cheap verification (research-skill-rigidity-spectrum)
- [Humans and Automation: Use, Misuse, Disuse, Abuse](sources/sage-parasuraman-riley-humans-and-automation-use-misuse-disuse-abuse.md): 1997 taxonomy: misuse (overreliance), disuse (ignored after false alarms), abuse (automation designed without regard to the human's role) (research-skill-rigidity-spectrum)

## levels-of-automation-frameworks: Levels-of-automation frameworks applied to agents
Human-factors and HCI models (Sheridan-Verplank, Parasuraman et al., Shneiderman, Horvitz, HAX) that predate LLMs and already split autonomy by task stage and separate automation from human control.
- [A model for types and levels of human interaction with automation](sources/ieee-parasuraman-sheridan-wickens-types-and-levels-of-automation.md): automate acquisition, analysis, decision and action separately; evaluate on workload, awareness, complacency, skill degradation (research-skill-rigidity-spectrum)
- [Human-Centered AI: Reliable, Safe and Trustworthy](sources/ijhci-shneiderman-human-centered-ai-reliable-safe-trustworthy.md): human control and automation are two axes; aim for high on both (research-skill-rigidity-spectrum)
- [Principles of mixed-initiative user interfaces](sources/acm-horvitz-principles-of-mixed-initiative-user-interfaces.md): act, ask or stay quiet per moment from uncertainty and expected cost/benefit (research-skill-rigidity-spectrum)
- [Guidelines for Human-AI Interaction](sources/microsoft-hax-guidelines-for-human-ai-interaction.md): 18 guidelines incl. efficient invocation, dismissal, correction, scope services when in doubt (research-skill-rigidity-spectrum)
- [smolagents: agency levels](sources/huggingface-smolagents-agency-levels.md): six-row agency table; default to coded workflow unless it falls short too often (research-skill-rigidity-spectrum)
- [Humans and Automation: Use, Misuse, Disuse, Abuse](sources/sage-parasuraman-riley-humans-and-automation-use-misuse-disuse-abuse.md): abuse = automation designed without regard to the human's remaining role (research-skill-rigidity-spectrum)
