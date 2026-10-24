# Cross-cutting stories S11–S18

These eight exist because of the baseline pain Geoff described (inconsistent Claude Code use, poor artifact management `[G]`), not because they are PM jobs in their own right. Each is a need that appears *inside* most job stories S01–S10. They are written once here so the job stories can point to them. Format and evidence tags: [README](README.md).

Performers are whoever is doing a PM job (PM, analyst, designer, engineer).

---

### S11. Pick up where I (or someone else) left off, and find the artifacts
Source job: all jobs   Span: multi-session

**NEED**
- Performer: anyone resuming work started earlier by themselves or a teammate, days or weeks later.
- Goal: get back to the state of the work (what was decided, what evidence was used, what's still open) and find the files and outputs it produced, without reconstructing them.
- Trigger and context: returning to a task after a gap; picking up someone else's work; being asked "where did that analysis come from?"; moving between laptop, phone and other devices.
- Done looks like: the performer can state what was decided and why, open the artifacts, and continue; the work's outputs live in a place others can find and the record of how they were made is kept.
- Success criteria: time to get back up to speed is short (minutes, not a re-do); nothing important is lost silently; someone who did not do the work can find it and trust its provenance; moving device or harness does not lose the thread.

**TODAY**
- Steps: scroll or search old Claude Code sessions; resume a session if it still exists; hunt through local folders and download directories; ask chat to reconstruct; sometimes re-do the work. `[G]`
- Tools: local session history, Finder/folders, notes tools, chat apps, screenshots.
- Pain: outputs and reasoning are scattered across sessions and local folders `[G]`; local session transcripts are auto-deleted after 30 days by default, users report losing decisions and reasoning with no warning (independent news report) [E: itdaily-claude-code-30-day-transcript-deletion](../../research/sources/itdaily-claude-code-30-day-transcript-deletion.md); structure comes only from the user's own folders and naming (anecdote) [E: hn-ask-claude-code-non-coding-workflows](../../research/sources/hn-ask-claude-code-non-coding-workflows.md); context is scattered across private docs and people [E: geoff-building-accelerating-intent-factory](../../research/sources/geoff-building-accelerating-intent-factory.md). Artifacts sit in several kinds of home at once (local files, docs tools, work trackers, research repositories, analytics tools, and increasingly git repos) with no common way to ask "what artifacts exist for project X" [E: findings §1](research-artifacts-standardization.md); connectivity to those homes is uneven: Amplitude, Dovetail and Notion have hosted OAuth MCP servers [E: amplitude](../../research/sources/amplitude-mcp-claude-code-docs.md), [E: dovetail](../../research/sources/dovetail-mcp-server-docs.md), [E: notion](../../research/sources/notion-mcp-developer-docs.md), while Snowflake needs an admin to create the server [E: snowflake](../../research/sources/snowflake-managed-mcp-server-docs.md) and Looker a self-run toolbox with client credentials (read via search summary only) [E: looker](../../research/sources/google-looker-mcp-toolbox-docs.md). PRDs are moving into the project's GitHub repo for some teams, inconsistently `[G]`; the nearest published evidence is PMs drafting PRDs with a coding agent over the real codebase and pushing them to Confluence or Notion (anecdote) [E: Lenny/Cursor](../../research/sources/lenny-cursor-better-product-manager.md), and spec-driven development tools that keep feature specs in git; Böckeler's independent review finds those tools' file layouts diverge and few keep the spec authoritative after the first build [E: fowler-bockeler-sdd-kiro-speckit-tessl](../../research/sources/fowler-bockeler-sdd-kiro-speckit-tessl.md). No adoption share for PRDs in repos was found.
- Hand-offs: to future self, to teammates.
- Time cost: not established. `[A]` Minutes to hours per resumption, more when it fails.

**VARIANTS**
- V1 Files as the record: every task writes its outputs, evidence and decisions into a project folder or repo that survives any session; the session itself is disposable. Varies by: context-and-memory/context-location, context-and-memory/memory-design, session-persistence-sharing/session-handoff-portability. Hinges on: whether performers will keep to a convention, and whether a convention can be applied without effort (agent-enforced).
- V2 Sessions as the record: sessions are durable, searchable and attributable; resuming a session resumes the work. Varies by: session-persistence-sharing, durability-substrate, runtime-location. Hinges on: retention policy and who may read old sessions.
- V3 Auto-curated work log: an agent keeps a running index of work (what was done, artifacts, decisions) and the performer asks it for a catch-up. Varies by: context-and-memory/memory-design, review-and-autonomy/autonomy-calibration. Hinges on: whether the log is trusted and who can read it.
- V4 Project descriptor with an artifact index: each piece of work belongs to a project with a short descriptor (owner, sources, instructions) that lists its artifacts wherever they live (files, repo, platform); resuming means opening the project. Varies by: artifact-and-project-structure, context-and-memory/context-location. Hinges on: whether performers keep the index current or an agent does.
- V5 Platform is the record: artifacts are created inside the team's existing platform objects and found through its search and the agent's connector to it. Varies by: artifact-and-project-structure, context-and-memory/org-context-grounding-source. Hinges on: connector coverage and permissions for the artifact types that matter.
- V6 Typed artifacts in a harness-defined project: the harness defines artifact kinds (spec, evidence, decision, status update...) and lifecycle states, so "find the last ratified spec" is a query. Varies by: artifact-and-project-structure, governance-control-plane. Hinges on: who owns the schema and whether teams accept it (see S16).

---

### S12. Get the agent to know our product and organisation
Source job: all jobs   Span: recurring

**NEED**
- Performer: anyone starting a PM task; also whoever maintains what "our context" is.
- Goal: have the agent start with the right product knowledge (customers, strategy, past decisions, terms, standards, systems) and have corrections to that knowledge stick for everyone.
- Trigger and context: the start of any task; a correction the performer wants remembered; a new joiner.
- Done looks like: the task starts with the relevant context already available, with its source and age visible; corrections the performer makes reach the shared context; the performer can inspect what the agent believes.
- Success criteria: the performer spends little time re-explaining; generic output caused by missing context becomes rarer; wrong context is findable and fixable; one person's correction improves the next person's work.

**TODAY**
- Steps: paste background into each session; keep a personal CLAUDE.md or notes; attach documents; re-explain. `[G]` `[A]`
- Tools: personal context files, docs, Slack, connectors where set up.
- Pain: generic PRDs trace to missing context (anecdote) `[E: atticusli-ai-prd-generation](../../research/sources/atticusli-ai-prd-generation.md)`; agents work when grounded in organisation context `[E: THEMES org-context-grounding](../../research/THEMES.md#org-context-grounding-agents-work-when-grounded-in-organisation-context)`; scattered context is the status quo `[E: geoff-building-accelerating-intent-factory](../../research/sources/geoff-building-accelerating-intent-factory.md)`; a wrong-source error is reported at Intercom `[E: intercom-we-gave-claude-code-to-everyone](../../research/sources/intercom-we-gave-claude-code-to-everyone.md)`.
- Hand-offs: domain owners hold facts; PMs hold judgement.
- Time cost: not established.

**VARIANTS**
- V1 Personal context file: each performer maintains their own. Varies by: context-and-memory/context-location, context-and-memory/memory-design. Hinges on: performer discipline.
- V2 Shared context repo with owners: plain-text, harness-agnostic, each topic has an owner and an "evidence versus fact" status; outputs write back. Varies by: context-and-memory/context-location, context-and-memory/org-context-grounding-source. Hinges on: governance and engineering permission.
- V3 Connectors to systems of record: the agent queries the tools where facts already live. Varies by: context-and-memory/org-context-grounding-source, governance-control-plane. Hinges on: retrieval quality and access scope.
- V4 Mined memory: a background process builds an inspectable profile from the performer's accounts and past work; read-only in session. Varies by: context-and-memory/memory-design. Hinges on: privacy and the performer's ability to correct it.
- V5 Project-scoped context: context is attached to a project (descriptor, instructions, linked sources, project memory) rather than to a person, so everyone working on the project starts from the same base. Varies by: artifact-and-project-structure, context-and-memory/context-location, context-and-memory/memory-design. Hinges on: whether a project is defined well enough to attach context to (S16); Cowork-style project memory is local-only today [E: Cowork projects](../../research/sources/anthropic-cowork-projects-docs.md).

---

### S13. Hand work to a teammate and get their input
Source job: all jobs (especially J3, J4, J8)   Span: multi-session

**NEED**
- Performer: the person who has the work in hand; the recipient is an engineer, designer, PM peer, leader or PMM who must read, add to or approve it.
- Goal: give another person what they need to continue or review (the work, the evidence, the open questions) and get their input back into the work.
- Trigger and context: a review request, a feasibility question, a hand-over, a request for approval, or "can you look at this?"
- Done looks like: the recipient has what they need without a live walkthrough, their input is recorded in the work itself, and the performer sees what changed and who said it; access is limited to what the recipient should see.
- Success criteria: recipient's time to understand is short; their input is not lost in chat; the performer does not become a manual relay; sensitive material is not exposed beyond the intended people.

**TODAY**
- Steps: export or copy output into a doc; share a link or paste into Slack; explain in a call; collect comments across Slack, doc and email; transcribe into the work. `[G]` `[A]`
- Tools: docs, Slack, email, screenshots, shared drives.
- Pain: artifacts live in different systems with different access, so a hand-off often means copying (project structure is not shared); 80% of teams do not involve engineers in early shaping `[E: mindtheproduct-atlassian-state-of-product-2026-takeaways](../../research/sources/mindtheproduct-atlassian-state-of-product-2026-takeaways.md)`; Claude Code sessions are local, private and hard to share by default (the project's own premise) `[A]`; vendor cloud sessions share by link, as a snapshot rather than a live view `[E: anthropic-claude-code-cloud-sessions](../../research/sources/anthropic-claude-code-cloud-sessions.md)`; shared agents in a channel turn channel membership into an access boundary `[E: tenable-claude-tag-slack-access-model](../../research/sources/tenable-claude-tag-slack-access-model.md)`.
- Hand-offs: this story *is* the hand-off.
- Time cost: not established.

**VARIANTS**
- V1 Share the outputs: the performer sends artifacts; the recipient reviews in their usual tools; the performer folds comments back. Varies by: session-persistence-sharing/session-handoff-portability, context-and-memory/context-location. Hinges on: whether artifacts carry enough evidence.
- V2 Share the session: the recipient opens the performer's session, sees reasoning and evidence, and adds input there (snapshot or live). Varies by: session-persistence-sharing, agent-identity-delegation. Hinges on: the permission model for what a session exposes.
- V3 Address a deployed agent: people ask a shared agent in a place they already work (e.g. a chat channel) and it brings in the relevant work. Varies by: runtime-location, capability-format-portability, agent-identity-delegation. Hinges on: whose identity it acts as and who can direct it.
- V4 Share the project: the recipient is added to the project and sees its descriptor and artifact index with each artifact's status and provenance, with access mirrored from the source systems. Varies by: artifact-and-project-structure, agent-identity-delegation. Hinges on: the permission model when artifacts live in several systems with different ACLs.

---

### S14. Have recurring work happen without me prompting
Source job: all recurring jobs (S02, S03, S07, S09, S10)   Span: recurring

**NEED**
- Performer: the person responsible for a recurring output (a digest, a status, a watch) and its recipients.
- Goal: get the output on a rhythm or when something happens, ready for review, without having to remember to start it.
- Trigger and context: a cadence (weekly), a calendar event, or a signal (a new ticket cluster, a competitor launch).
- Done looks like: the output appears where it should, on time, marked with what it was based on, waiting for approval if approval is needed; failures are visible.
- Success criteria: it runs when the performer is away; a failed or missed run is noticed; it does not take actions the performer has not approved; cost and effort stay bounded.

**TODAY**
- Steps: do it by hand each time; set reminders; occasionally run a saved prompt. `[G]` `[A]`
- Tools: calendar, notes, saved prompts, sometimes a scheduled automation tool.
- Pain: scheduled tasks exist in Claude Code but belong to one account and are not shared with teammates; a green run status does not mean the work succeeded `[E: anthropic-claude-code-scheduled-tasks](../../research/sources/anthropic-claude-code-scheduled-tasks.md)`; the desktop-app model "turns your laptop into a server", so it depends on the laptop being on (implied by the source, not discussed) `[E: x-sebgoddijn-glass-article](../../research/sources/x-sebgoddijn-glass-article.md)`; the inconsistent-use baseline means most routines are not set up `[G]`.
- Hand-offs: recipients; whoever owns the credentials.
- Time cost: the recurring effort is the cost; not established.

**VARIANTS**
- V1 Laptop schedule: runs on the performer's machine while it is on, output to their files or chat. Varies by: runtime-location. Hinges on: how often laptops are off at the trigger time.
- V2 Cloud schedule owned by the performer: runs in a vendor cloud under the performer's identity. Varies by: runtime-location, agent-identity-delegation. Hinges on: data and policy limits on cloud sessions.
- V3 Team-owned service: a deployed agent with its own scoped identity runs and posts, with a named owner. Varies by: runtime-location, session-persistence-sharing, agent-identity-delegation, governance-control-plane. Hinges on: who operates it.

---

### S15. Know whether I can trust what came back
Source job: all jobs   Span: sitting

**NEED**
- Performer: the person who is accountable for the output and will put their name on it.
- Goal: be able to check agent output cheaply, see what it was based on, catch errors before others do, and decide how much to rely on it next time.
- Trigger and context: every time an agent produces something that will be used, shared or acted on.
- Done looks like: the performer has seen the sources behind each key claim, seen what the agent did not look at, corrected what was wrong, and made a conscious decision to accept; a record of that exists if others need it.
- Success criteria: errors are caught by the performer, not later by reviewers; checking takes less time than doing the work; the performer's reliance on the agent matches its measured accuracy; reviewers can see that review happened.

**TODAY**
- Steps: skim the output; spot-check a few facts; ask the chat to double check itself; accept by default when short on time. `[G]` `[A]`
- Tools: the output itself; source docs; memory.
- Pain: "expert + AI" beats either alone and AI synthesis must be reviewed against source quotes (Torres) `[E: producttalk-torres-customer-interview-analysis-podcast](../../research/sources/producttalk-torres-customer-interview-analysis-podcast.md)`; fabricated quotes and invented facts, with the design principle that AI sifts and sorts while humans understand and decide `[E: producttalk-ai-hallucination-glossary](../../research/sources/producttalk-ai-hallucination-glossary.md)`; synthetic users over-optimistic and approve concepts uncritically `[E: nngroup-synthetic-users](../../research/sources/nngroup-synthetic-users.md)`; 85% of PMs validate AI output with their own expertise (search summary) `[E: productfocus-industry-survey-2026](../../research/sources/productfocus-industry-survey-2026.md)`; a Meta brief dropped all source links `[E: lenny-newsletter-meta-chawla-pm-leader-agents](../../research/sources/lenny-newsletter-meta-chawla-pm-leader-agents.md)`; there is no published accuracy audit of any PM-facing agent at a named company `[E: 03-in-practice-cases-and-failures](../research-pm-agents-jobs-to-be-done/03-in-practice-cases-and-failures.md)`.
- Hand-offs: reviewers and recipients rely on the performer's check.
- Time cost: not established. Checking effort is the hidden cost behind "hours saved".

**VARIANTS**
- V1 Performer reviews everything, with evidence attached: every claim links to its source passage; the performer checks what they choose. Varies by: review-and-autonomy/review-gating, capability-format-portability. Hinges on: citation quality.
- V2 Automated checker plus spot checks: a verifier (e.g. quote checking, a second agent) checks outputs; the performer samples and handles flags. Varies by: review-and-autonomy/review-gate-placement, work-structure. Hinges on: checker accuracy, measured against the performer's own labels.
- V3 Trust earned over time: autonomy rises as measured accuracy holds and falls on errors, per task type. Varies by: review-and-autonomy/autonomy-calibration, pm-agent-evaluation. Hinges on: a way to measure accuracy on real tasks.

---

### S16. Start a piece of work with a defined project and the right artifacts
Source job: all jobs (especially J2–J4)   Span: sitting (the project it creates then lives for weeks)

**NEED**
- Performer: whoever starts a new initiative, investigation or feature effort (PM, designer, engineer); collaborators will join later.
- Goal: set up the work so it has a clear identity, an owner, the sources it draws on, the kinds of artifacts it will produce, and the people who need to see it, without a long setup chore.
- Trigger and context: a new opportunity is chosen, a new investigation begins, or an existing effort needs to be split or merged.
- Done looks like: the project has a name, owner, purpose, status, linked sources, the artifact types expected (for example research synthesis, spec, decision log, status updates), and a known home for each; collaborators can see what the project is and what it contains; agents working on it get this same picture.
- Success criteria: setup takes minutes; a newcomer can understand the project in minutes without asking; artifacts made later land in the expected places; the structure fits how the team already talks about its work (not a rival taxonomy); it can change as the work changes.

**TODAY**
- Steps: make a local folder or a new chat/session; maybe a doc or a ticket or epic; paste background; name things from memory. Teams that use repos may create a feature folder; others create a space or page in their docs tool. `[G]` `[A]`
- Tools: folders, docs tool, work tracker, repo, chat.
- Pain: "project" means different things even inside one vendor: Atlassian alone has a Jira space, a Confluence space and a Home project [E: Jira space](../../research/sources/atlassian-jira-space-definition.md), [E: Confluence space](../../research/sources/atlassian-confluence-space-definition.md); Linear separates initiative, project and issue [E: linear-initiatives-docs](../../research/sources/linear-initiatives-docs.md); spec-driven development tools use a per-feature folder with different files [E: Spec Kit](../../research/sources/github-spec-kit-sdd.md), [E: Kiro](../../research/sources/kiro-specs-docs.md); Backstage defines Domain > System > Component for software catalogues [E: backstage-descriptor-format](../../research/sources/backstage-descriptor-format.md). Atlassian's own answer to "where do PRDs and decisions live" is page templates in a Confluence space (PRD, project poster, DACI decision) linked to Jira by embedded issue links rather than typed relationships [E: Confluence PRD template](../../research/sources/atlassian-confluence-prd-template.md), [E: project poster](../../research/sources/atlassian-confluence-project-poster-template.md), [E: DACI](../../research/sources/atlassian-confluence-daci-decision-template.md); its graph API publishes object types for Confluence, Home goals and projects and 29 external kinds but still no idea, PRD, spec or decision type [E: Teamwork Graph scopes](../../research/sources/atlassian-teamwork-graph-scopes.md). Nothing defines a project of typed PM artifacts [E: findings §3–4](research-artifacts-standardization.md). Pragmatic Institute and product-operations taxonomy writing was not located as first-party. Starting without structure is cheap but is what makes S11 and S17 hard `[A]`.
- Hand-offs: collaborators who join later; product ops if they own the tool stack [E: product ops](../../research/sources/parallelhq-what-does-product-operations-do.md).
- Time cost: setup is minutes; the cost lands later (re-finding, re-explaining). Not established.

**VARIANTS**
- V1 Convention only: a documented folder layout and file names (and frontmatter) that people follow by hand. Varies by: artifact-and-project-structure (repo-native). Hinges on: compliance without a checker.
- V2 Agent scaffolds from a template: the agent creates the layout, descriptor and first artifacts from a few answers, using the team's template. Varies by: artifact-and-project-structure, capability-format-portability, adoption-model. Hinges on: a team template existing and being maintained.
- V3 Project created in the platform: a space/project/initiative is made in the team's platform and the agent attaches to it. Varies by: artifact-and-project-structure (platform-owned), context-and-memory/org-context-grounding-source. Hinges on: which of the platform's several "project" objects applies.
- V4 Harness-defined project: the harness offers a project object with typed artifact slots, lifecycle and permissions; platform objects are linked in. Varies by: artifact-and-project-structure (meta-harness-defined), agent-identity-delegation, governance-control-plane. Hinges on: whether teams will accept a project definition from outside their tools.

---

### S17. Find and reuse an earlier artifact across tools
Source job: all jobs   Span: sitting

**NEED**
- Performer: anyone who knows, or half-remembers, that something relevant was made before (a spec, a research synthesis, a decision, a dashboard, a prototype), possibly by someone else.
- Goal: locate the right earlier artifact, judge whether it is current and trustworthy, and build on it instead of redoing it.
- Trigger and context: starting a related piece of work, answering a question like "did we decide this before?", an onboarding question, or a reviewer asking where a claim comes from.
- Done looks like: the performer has the artifact (or the right part of it) in hand, knows its owner, status, version and sources, and has either reused it or consciously decided not to.
- Success criteria: found within minutes; the version found is the current ratified one or the performer can see that it is not; stale or superseded artifacts are visible as such; permissions are respected (the performer only sees what they may see); reuse is traceable.

**TODAY**
- Steps: search one tool at a time (docs tool, tracker, Slack, drive, repo, local files); ask colleagues; ask Claude Code about the local folder; give up and redo. `[G]` `[A]`
- Tools: each tool's own search; Slack; repo search; sometimes an enterprise search product.
- Pain: no common way to ask "what exists for project X" across tools [E: findings §1](research-artifacts-standardization.md); each tool's agent access is per-tool OAuth with different limits (Dovetail: no update/delete tools; Notion: client allow-listing needs Enterprise; Snowflake: tools only, responses truncated at 250 KB) [E: dovetail](../../research/sources/dovetail-mcp-server-docs.md), [E: notion](../../research/sources/notion-mcp-developer-docs.md), [E: snowflake](../../research/sources/snowflake-managed-mcp-server-docs.md); enterprise context layers infer entities across tools but are vendor claims [E: Glean (vendor claim)](../../research/sources/glean-enterprise-graph-product-page.md); Atlassian's graph types are generic (work item, document, project, space) with no spec or decision type [E: atlassian-teamwork-graph-object-types](../../research/sources/atlassian-teamwork-graph-object-types.md); Ramp's "gadgets" connect questions to "the formal record, the road map in Notion, the specs in Notion, the customer calls in Notion, Slack, Linear" (11:43), with 85% of PM-directed questions claimed answered (speaker-reported) [E: Charles on Lenny](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md).
- Hand-offs: the original author, who knows where it went.
- Time cost: not established. `[A]` minutes when it works, hours or a redo when it does not.

**VARIANTS**
- V1 Ask one connected agent: the agent searches the connected tools and returns candidates with source, author and date. Varies by: context-and-memory/org-context-grounding-source, agent-identity-delegation. Hinges on: connector coverage and whether results mirror the asker's permissions.
- V2 Look in the project index: the project descriptor lists its artifacts wherever they live, so search starts from the project. Varies by: artifact-and-project-structure (descriptor). Hinges on: how the index is kept current.
- V3 Typed query: artifacts carry type, status, version and provenance, so the performer asks for "the ratified spec for X" or "decisions on Y since March". Varies by: artifact-and-project-structure (meta-harness-defined), context-and-memory/memory-design. Hinges on: the typing being applied at creation, not retrofitted.
- V4 Inferred graph: an enterprise graph infers related entities and surfaces candidates without anyone maintaining structure. Varies by: artifact-and-project-structure (inferred layer). Hinges on: precision, staleness handling and cost.

---

### S18. Share an artifact with a multi-party team and keep it correct
Source job: all jobs (especially J4, J8, J7)   Span: multi-session

**NEED**
- Performer: the artifact's owner, with collaborators from several roles and possibly several teams (engineering, design, risk, PMM, leadership).
- Goal: make one artifact (a spec, a synthesis, a plan) the shared reference that several people read, comment on and rely on, with a clear owner, a visible status, a trace of what changed and who agreed, and access only for those who should have it.
- Trigger and context: an artifact is ready for others, or others need to contribute; multiple parties already hold their own copies or summaries.
- Done looks like: one canonical artifact, discoverable from the project, with owner, status, version, reviewers' sign-offs, change history and a clear link to its sources; derived copies point back to it.
- Success criteria: people work from the same version; contributions land in the artifact, not in side channels; a reader can tell what changed since they last looked; confidential material is not exposed; people who never touched the original tool can take part.

**TODAY**
- Steps: share a link or paste into chat; copies diverge; comments arrive in Slack, email, doc and PR; the owner reconciles by hand; sign-offs are chat messages. `[G]` `[A]`
- Tools: docs tool, repo/PR, Slack, email, tracker.
- Pain: 80% of teams do not involve engineers in ideation or problem definition [E: Mind the Product on Atlassian](../../research/sources/mindtheproduct-atlassian-state-of-product-2026-takeaways.md); spec-driven tools treat specs like change requests with branches and heavy review, and it is unclear whether they serve product people [E: fowler-bockeler-sdd-kiro-speckit-tessl](../../research/sources/fowler-bockeler-sdd-kiro-speckit-tessl.md); shareable claude.ai projects hold files only while the richer Cowork project is local and not shareable [E: Claude Projects](../../research/sources/anthropic-claude-projects-support.md), [E: Cowork projects](../../research/sources/anthropic-cowork-projects-docs.md); shared agents in a channel make channel membership an access boundary [E: tenable-claude-tag-slack-access-model](../../research/sources/tenable-claude-tag-slack-access-model.md).
- Hand-offs: this story is a hand-off with many receivers.
- Time cost: not established.

**VARIANTS**
- V1 Git as the shared home: the artifact is a file in the project repo; collaborators comment on a PR; history and approvals are the PR's. Varies by: artifact-and-project-structure (repo-native), session-persistence-sharing/session-handoff-portability. Hinges on: whether non-engineers participate in a PR.
- V2 Platform page as the shared home: the artifact lives in a platform page or work item with that platform's permissions and history; the agent edits it over the platform's connector. Varies by: artifact-and-project-structure (platform-owned), agent-identity-delegation. Hinges on: connector write coverage (some tools are read-only to agents).
- V3 Harness-held canonical copy with synced views: the harness holds the typed artifact and syncs views to repos and platforms for people who prefer them. Varies by: artifact-and-project-structure (meta-harness-defined), session-persistence-sharing. Hinges on: sync fidelity and who wins on conflict.
- V4 Agent-mediated: collaborators address a shared agent that applies their input to the artifact and reports changes. Varies by: runtime-location, session-persistence-sharing, agent-identity-delegation. Hinges on: whose identity the agent acts as.
