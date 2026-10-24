# Job stories S01–S10

One story per PM job in the [JTBD map](../research-pm-agents-jobs-to-be-done/01-jobs-to-be-done-map.md) (J1–J10). Format and evidence tags: [README](README.md). Cross-cutting stories: [stories-cross-cutting.md](stories-cross-cutting.md).

Reading note: *Today* = inconsistent Claude Code use with poor artifact management `[G]`. Cross-cutting pains that recur in every story (artifacts scattered across chat transcripts and local folders, context re-supplied each session, nothing shared) are written out in S11–S18 and only pointed to here.

Source shorthand: sources are in `../../research/sources/`; links go to the note, which states the evidence type.

---

### S01. Turn a batch of customer conversations into what we learned
Source job: J1   Span: multi-session

**NEED**
- Performer: whoever runs discovery (PM, designer or researcher); the product trio reads the result.
- Goal: understand what customers said and why, grounded in their words, without reading everything twice.
- Trigger and context: a set of interviews, calls or survey verbatims has just landed (e.g. 5–15 recordings or transcripts from the last weeks); a decision or an opportunity map is waiting on them.
- Done looks like: per-conversation snapshots and a cross-conversation set of themes, every claim traceable to a verbatim quote, filed where the team (and later work) can find them; the performer has read and corrected them.
- Success criteria: no invented or misattributed quotes; themes the performer would defend in a review; the performer's own understanding is better, not just a document existing; turnaround within the working week of the last interview; next time's synthesis can build on this one.

**TODAY**
- Steps: get transcripts out of the call tool; paste or upload a few into Claude (or chat); ask for summaries or themes; copy outputs into a doc or Notion; hand-fix; re-do when new interviews arrive because earlier chat context is gone. `[G]` `[A]`
- Tools: call recorder/transcriber, a chat window or Claude Code session, notes app or doc, spreadsheet for tagging.
- Pain: pasting transcripts is no shortcut and AI helps only when interviews are strong and context is supplied (Torres) `[E: producttalk-torres-customer-interview-analysis-podcast](../../research/sources/producttalk-torres-customer-interview-analysis-podcast.md)`. Fabricated quotes and invented facts in AI synthesis `[E: producttalk-ai-hallucination-glossary](../../research/sources/producttalk-ai-hallucination-glossary.md)`; 11–25% incorrect information reported in a small thematic-analysis poster (10 interviews; poster read only via search summary) `[E: ispor-2025-ai-thematic-analysis-payer-interviews](../../research/sources/ispor-2025-ai-thematic-analysis-payer-interviews.md)`. AI for user research is only 4.7% of PM AI use yet the biggest demand gap `[E: lennys-newsletter-ai-tools-overdelivering-results](../../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md)`. Each synthesis starts from scratch; outputs end up in scattered chat history and local files `[G]`.
- Hand-offs: designer/engineers read the result; sales/CS supply some inputs.
- Time cost: not established. `[A]` hours per interview-batch of manual work; the survey sources report hours saved per week or task but not for this job.
- Before agents: manual snapshot per interview (Torres' one-page snapshot) and affinity grouping.

**VARIANTS**
- V1 Performer-driven in a personal session: the performer loads transcripts into their own harness and drives analysis with a saved routine; output is files on their machine; they check quotes themselves. Varies by: runtime-location, capability-format-portability, review-and-autonomy/review-gating. Hinges on: whether quote verification can be made cheap enough that people actually do it.
- V2 Pipeline-prepared, performer-reviewed: when a transcript lands, an agent drafts snapshots and a first theme map and files them in a shared place; the performer is notified, edits and ratifies. Varies by: session-persistence-sharing, work-structure, review-and-autonomy/review-gate-placement, context-and-memory/context-location. Hinges on: whether transcripts are reachable from where the agent runs (policy, recording-tool access).
- V3 Interrogation-led: the agent asks the performer what they expected to hear and what decision this is for, then tests the data against that; the performer synthesises first and the agent challenges. Varies by: intent-shaping-and-spec/intent-shaping-mode, review-and-autonomy/autonomy-calibration. Hinges on: whether performers accept being questioned (Torres: synthesise yourself first, then use AI).
- V4 Synthesis filed in the project: snapshots and the theme map are typed research artifacts in the product's project, each quote linked to its transcript, so the trio reads them where the spec and decisions will later sit and the next batch builds on them. Varies by: artifact-and-project-structure, context-and-memory/context-location. Hinges on: whether transcripts may be stored or linked where the project lives (recording-tool and privacy policy).

---

### S02. Triage incoming feedback into ranked themes
Source job: J10 (with J1)   Span: recurring

**NEED**
- Performer: PM, product ops or support-liaison; the PM and team consume the ranked themes.
- Goal: know what customers are complaining about and asking for across channels, ranked by frequency, severity and strategic fit, without reading every ticket.
- Trigger and context: a steady inflow (tickets, NPS verbatims, reviews, sales and CS notes, usage data), or a release that just shipped and needs a read on reaction.
- Done looks like: a ranked, deduplicated theme list for the period, each theme linked to its raw items, with bugs routed to owners and strategically important themes fed to discovery; the previous period's list is comparable.
- Success criteria: the performer agrees with the top themes after sampling raw items; no theme is dropped silently; items are not double-counted; time to spot a new theme is shorter than the period length; the performer trusts counts enough to quote them.

**TODAY**
- Steps: export tickets/NPS to CSV or copy from tools; paste batches into a chat or Claude session to cluster; copy results to a sheet or doc; discuss in a weekly meeting; mostly each period starts over. `[G]` `[A]`
- Tools: support desk, survey tool, CRM, spreadsheet, chat.
- Pain: volume across channels; no single source of truth (product ops aim for one) `[E: parallelhq-what-does-product-operations-do](../../research/sources/parallelhq-what-does-product-operations-do.md)`; one vendor claims 80% of feedback is never analysed (unverified) `[E: mindstudio-ai-agents-for-product-managers](../../research/sources/mindstudio-ai-agents-for-product-managers.md)`; community skills exist for feedback clustering `[E: claudepluginhub-feedback-triage-skills](../../research/sources/claudepluginhub-feedback-triage-skills.md)`. Agent-categorised feedback is already in use at Atlassian (a Rovo agent categorised 900+ items; speaker-reported, no accuracy data) `[E: lenny-podcast-tamar-yehoshua-roles-expanding](../../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md)`; Ramp reports feature-request *capture* rising from about 300 to 20,000 a month from a saved prompt (volume only, Ramp's own number) `[E: x-eglyman-introducing-glass-learn-things-once](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md)`.
- Hand-offs: support/CS supply data; engineering receives bugs; the PM's discovery work receives themes.
- Time cost: not established.
- Before agents: manual tagging in the support tool, or not done.

**VARIANTS**
- V1 On-demand: the performer runs a triage routine in their own session when they have time; output is a file they keep. Varies by: runtime-location, capability-format-portability. Hinges on: access to the feedback sources from the performer's machine.
- V2 Scheduled: the routine runs on a schedule and posts the ranked list where the team already is (chat, doc); the performer reviews exceptions. Varies by: runtime-location, session-persistence-sharing, review-and-autonomy/autonomy-calibration. Hinges on: where unattended jobs can run (laptop-must-be-on versus deployed) and who owns credentials.
- V3 Always-on intake: new items are classified as they arrive and themes update continuously; the performer asks questions of the live theme set. Varies by: work-structure, session-persistence-sharing, governance-control-plane. Hinges on: classification accuracy being measured against the performer's own judgement (see S15).
- V4 Theme records in the project: the agent files each period's ranked list as a typed artifact in the product's project, linked to the raw items it clustered; the performer approves it there, and next period's run starts by reading the last one so the lists compare like with like. Varies by: artifact-and-project-structure, review-and-autonomy/review-gate-placement. Hinges on: a stable theme record format the team will keep.

---

### S03. Form a view of the market and competitors
Source job: J2   Span: multi-session

**NEED**
- Performer: PM or head of product preparing strategy input; sometimes an analyst.
- Goal: know what competitors and the market are doing and what it implies for our choices, with sources, fast enough to be current.
- Trigger and context: a strategy cycle, a competitor launch, a board or exec question, or a standing need to track a set of competitors.
- Done looks like: a competitor/market brief (and a tracked competitor set) stating what changed, what it may mean, and what is unverified; every claim linked to a source; filed where the strategy work picks it up.
- Success criteria: claims are checkable; vendor claims are separated from independent evidence; coverage gaps are stated; the performer can defend the implications in a room; the brief can be refreshed without starting over.

**TODAY**
- Steps: web search and reading by hand; ask a chat for summaries; paste competitor pages into sessions; assemble a doc or deck; repeat each cycle with little reuse. `[G]` `[A]`
- Tools: browser, chat/Claude Code, docs, slide tools, competitor-tracking tools (e.g. a similarity-data service).
- Pain: strategy time is squeezed by reactive work and strategy slips `[E: atlassian-state-of-product-2026-webinar-event](../../research/sources/atlassian-state-of-product-2026-webinar-event.md)` (vendor); competitive research is among the largest time-savers in a vendor survey (about 4 hours per task, vendor) `[E: productboard-ai-in-product-management-report](../../research/sources/productboard-ai-in-product-management-report.md)`; speed amplifies the cost of a wrong direction `[E: reforge-more-valuable-less-protected](../../research/sources/reforge-more-valuable-less-protected.md)`; vendor-biased claims are hard to separate from independent evidence (seen in this very project's research notes) `[A]`.
- Hand-offs: leaders receive the brief; PMM contributes positioning views.
- Time cost: not established; the Productboard figure is vendor-reported.
- Before agents: analyst or PM reading and slide-writing.

**VARIANTS**
- V1 Research session on demand: the performer directs a research session that files each source as a note and produces the brief; the library grows. Varies by: capability-format-portability, context-and-memory/context-location. Hinges on: whether the performer or a shared owner maintains the library.
- V2 Watch agent: a standing agent monitors named competitors and posts changes; the performer reads digests and escalates. Varies by: runtime-location, session-persistence-sharing, review-and-autonomy/review-gate-placement. Hinges on: the cost and false-alarm rate of unattended watching.
- V3 Collaborative brief: several people contribute to one live brief that an agent keeps current with sources. Varies by: session-persistence-sharing, session-persistence-sharing/session-handoff-portability. Hinges on: whether people will contribute to a shared artifact rather than private notes (S11, S13).
- V4 Typed research notes in the project: each source is filed as a note with provenance and the brief points to notes, so a refresh re-reads the notes, not the web. Varies by: artifact-and-project-structure, context-and-memory/context-location. Hinges on: who maintains the structure.

---

### S04. Explore solution options and make something to react to
Source job: J3   Span: multi-session

**NEED**
- Performer: PM, designer or engineer shaping a solution (the trio); customers or stakeholders react to the result.
- Goal: turn a prioritised opportunity into two or three credible solution options with a prototype or mock that someone can react to, and know which risk each option tests.
- Trigger and context: an opportunity is chosen; assumptions are known; time to test a solution direction.
- Done looks like: option write-ups naming the four risks (value, usability, feasibility, viability) for each, one or more prototypes people can click or read, and a recorded choice of what to test first; engineering has been consulted on feasibility.
- Success criteria: someone outside the author can react to the prototype within a day of the request; feasibility questions reach engineers before the plan solidifies; the chosen test addresses the biggest risk; the prototype and its reasoning remain findable.

**TODAY**
- Steps: sketch or write options; ask Claude Code (or a prototyping tool) for a prototype; iterate in a local folder or tool; screenshots or links shared in chat; reasoning stays in the session. `[G]` `[A]`
- Tools: prototyping tools, Claude Code, Figma, docs.
- Pain: prototyping is the most-wanted future AI use (19.8% to 44.4%) `[E: lennys-newsletter-ai-tools-overdelivering-results](../../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md)`; 80% of teams do not involve engineers in ideation, problem definition or roadmap creation (vendor survey via a practitioner summary) `[E: mindtheproduct-atlassian-state-of-product-2026-takeaways](../../research/sources/mindtheproduct-atlassian-state-of-product-2026-takeaways.md)`, and SVPG warns against a PM judging feasibility without engineers (companion post seen only in a search summary) `[E: svpg-four-big-risks](../../research/sources/svpg-four-big-risks.md)`; limits of prototyping agents `[E: THEMES prototyping-agents-limits](../../research/THEMES.md#prototyping-agents-limits-prototyping-agents-and-their-limits)`; prototype and its rationale are lost when the session ends `[G]`.
- Hand-offs: engineers on feasibility; designers on usability; customers for reactions.
- Time cost: not established.
- Before agents: wait for design/engineering capacity.

**VARIANTS**
- V1 Solo exploration: the performer runs option generation and prototype building in their own session and shares the output by link or file. Varies by: runtime-location, capability-format-portability. Hinges on: how prototypes are hosted so non-authors can open them.
- V2 Parallel options: several prototype variants are generated in parallel in isolated workspaces and compared side by side. Varies by: runtime-location, work-structure. Hinges on: cost and who decides when to stop.
- V3 Engineer-in-the-loop: the prototype session is shared with an engineer who answers feasibility questions inside it. Varies by: session-persistence-sharing, session-persistence-sharing/session-handoff-portability. Hinges on: whether engineers will join sessions rather than reviewing documents.
- V4 Prototype as a project artifact: the prototype, its option write-ups and the four-risk assessment are registered in the project so they stay findable after the session ends. Varies by: artifact-and-project-structure. Hinges on: where prototypes are hosted.

---

### S05. Write and ratify a spec engineers can act on
Source job: J4   Span: multi-session

**NEED**
- Performer: PM (sometimes designer or engineer); engineering lead, designer and others review and ratify.
- Goal: turn a chosen solution into a spec complete enough for delivery (goals, non-goals, behaviour, edge cases, metrics, acceptance criteria) that engineering and design agree with.
- Trigger and context: a solution direction has passed discovery; delivery cannot start without the spec; reviewers have limited time.
- Done looks like: an agreed spec in the team's agreed form, with open questions closed or owned, reviewer sign-offs recorded, and its supporting evidence linked; the spec is stored where delivery work and later specs can read it.
- Success criteria: reviewers find few gaps in the first review; fewer questions come back from engineering mid-delivery; the spec meets the team's completeness standard if one exists; time from decision to ratified spec; evidence behind each requirement is traceable.

**TODAY**
- Steps: gather research and prior decisions by hand; prompt for a PRD draft in chat or Claude Code; edit; paste into a doc; circulate; collect comments in several places; revise; context for the next spec must be gathered again. `[G]` `[A]`
- Tools: doc tool, chat/Claude Code, ticket tool, prior specs, Slack.
- Pain: PRD is the most common PM AI use (21.5%) and among the biggest time savers, yet "produce" is easier than "think" `[E: lennys-newsletter-ai-tools-overdelivering-results](../../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md)`, `[E: productboard-ai-in-product-management-report](../../research/sources/productboard-ai-in-product-management-report.md)`; generic template PRDs trace to missing context rather than the model (anecdote) `[E: atticusli-ai-prd-generation](../../research/sources/atticusli-ai-prd-generation.md)`; refinement is bespoke each time, context is scattered, PRDs are vague, agent use is inconsistent `[E: geoff-building-accelerating-intent-factory](../../research/sources/geoff-building-accelerating-intent-factory.md)`. One Meta org replaced the PRD for ML work with a problem statement, prototype and eval set (first-person account, sponsored) `[E: lenny-newsletter-meta-chawla-pm-leader-agents](../../research/sources/lenny-newsletter-meta-chawla-pm-leader-agents.md)`.
- Hand-offs: engineering lead, designer, risk/legal reviewers; downstream, ticket creation.
- Time cost: not established; Intent Factory notes only 1–2 sprints of shovel-ready intent exist against years of goals (framing, not a measurement).
- Before agents: PM writes the PRD alone.

**VARIANTS**
- V1 Personal draft and reviewed by people: the performer drafts with an agent in their session and circulates a document to reviewers who comment as they do today. Varies by: runtime-location, review-and-autonomy/review-gating. Hinges on: whether reviewers need to see sources and the reasoning.
- V2 Shared review in the session: reviewers (human and a spec-review agent) see the draft and its evidence in one shared place and resolve gaps there. Varies by: session-persistence-sharing, capability-format-portability, review-and-autonomy/review-gate-placement. Hinges on: reviewers' willingness to leave their own tools.
- V3 Agent-led shaping: an agent interrogates the performer against a spec standard until the intent is complete, drafts the spec, and a separate check validates it before human review. Varies by: intent-shaping-and-spec/intent-shaping-mode, intent-shaping-and-spec/spec-standard, work-structure. Hinges on: whether a team-agreed standard exists.

- V4 Spec as a typed artifact in a defined project: the spec has a type, owner, status and version, the project lists its evidence and reviewers, and the home may be a repo, a platform page or a harness-held record. Varies by: artifact-and-project-structure, intent-shaping-and-spec/spec-standard. Hinges on: which home the reviewers will use (see S16, S18).

Worked derivation of this story: [worked-derivation-s05.md](worked-derivation-s05.md).

---

### S06. Decide what's next: prioritise and maintain the roadmap
Source job: J5   Span: recurring

**NEED**
- Performer: PM or head of product; stakeholders and engineering input; leaders approve.
- Goal: choose and explain what the team works on next given goals, evidence, effort and capacity, and keep the roadmap current as things change.
- Trigger and context: a planning cycle, a new top-down ask, a capacity or scope change, or new evidence that moves an earlier decision.
- Done looks like: a ranked backlog or roadmap view with stated rationale and trade-offs, the key assumptions and what would change the order, shared with those affected.
- Success criteria: the rationale holds up when challenged; changes after a disruption are made quickly and visibly; stakeholders find the reasoning, not just the result; the PM retains the decision.

**TODAY**
- Steps: collect inputs from tools; weigh them in a spreadsheet or doc; ask a chat for scoring or scenarios; adjust after escalations; update roadmap in the planning tool and slides. `[G]` `[A]`
- Tools: roadmap tool, ticket tool, spreadsheets, docs, slides.
- Pain: leadership escalations override prioritisation frameworks in over 60% of cases (marketing summary) `[E: productplan-state-of-product-management-2026](../../research/sources/productplan-state-of-product-management-2026.md)`; the exec-sets-strategy, PM-curates-roadmap model is breaking down `[E: reforge-more-valuable-less-protected](../../research/sources/reforge-more-valuable-less-protected.md)`; only 1.1% use AI for roadmap ideas though roadmap creation appears among top savers in another survey (not comparable) `[E: lennys-newsletter-ai-tools-overdelivering-results](../../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md)`, `[E: productboard-ai-in-product-management-report](../../research/sources/productboard-ai-in-product-management-report.md)`.
- Hand-offs: engineering (effort), leadership (approval), stakeholders (asks).
- Time cost: not established.

**VARIANTS**
- V1 Input assembly: the agent gathers evidence, effort and dependencies and presents scenarios; the performer decides and writes the rationale. Varies by: work-structure, review-and-autonomy/review-gate-placement, context-and-memory/org-context-grounding-source. Hinges on: access to planning and ticket systems.
- V2 Re-plan on disruption: when a trigger fires (a scope change or escalation), the agent proposes the revised order and impacts; the performer approves and the change is announced. Varies by: session-persistence-sharing, review-and-autonomy/autonomy-calibration. Hinges on: whether the agent is allowed to see escalation channels.
- V3 Transparent rationale log: every decision's inputs and trade-offs are kept as an inspectable record others can query. Varies by: context-and-memory/context-location, context-and-memory/memory-design. Hinges on: whether stakeholders will read a log rather than ask.
- V4 Decision records: when the performer makes a call, the agent writes a decision record (inputs, options, trade-off, who decided) into the project and links it from the roadmap item; stakeholders who ask "why" are pointed at the record instead of the PM. Varies by: artifact-and-project-structure, context-and-memory/memory-design. Hinges on: whether the roadmap tool can hold or link such records and whether people will read them.

---

### S07. Know where delivery stands and unblock it
Source job: J6   Span: recurring

**NEED**
- Performer: PM, delivery lead or engineering manager; the team and stakeholders consume status.
- Goal: know what is shipped, in progress, blocked and at risk, and why, and get blockers moving.
- Trigger and context: sprint start, daily or weekly cadence, a stand-up, or a stakeholder asking "where is X?"
- Done looks like: a current status with blockers named and owned, tickets groomed to match the approved spec, sprint plan agreed; the PM knows what to chase today.
- Success criteria: status matches reality when checked against tickets and code; blockers are surfaced before they cost a sprint; ticket drafting no longer consumes the PM's week; engineering estimates are not overridden by the agent.

**TODAY**
- Steps: read ticket boards, PRs and Slack; write tickets by hand or paste a spec into chat; compile a standup or sprint note; chase people. `[G]` `[A]`
- Tools: ticket tool, Slack, code host, docs.
- Pain: ticket and story paperwork `[E: productboard-ai-in-product-management-report](../../research/sources/productboard-ai-in-product-management-report.md)`; tracking what is blocked and why on cross-functional projects is a human skill agents don't yet supply `[E: reforge-more-valuable-less-protected](../../research/sources/reforge-more-valuable-less-protected.md)`; status and "ask the org" Q&A agents are already in use at Atlassian and Ramp (speaker-reported) `[E: THEMES status-update-agents](../../research/THEMES.md#status-update-agents-status-updates-and-ask-the-org-qa-as-an-agent-job)`.
- Hand-offs: engineers update tickets; PM relays status to leaders (S09).
- Time cost: not established.

**VARIANTS**
- V1 Pull: the performer asks for status when needed and the agent reads the systems of record. Varies by: context-and-memory/org-context-grounding-source, runtime-location. Hinges on: connectors with enough access.
- V2 Push: a scheduled or event-triggered agent posts status and flags blockers to the team channel. Varies by: runtime-location, session-persistence-sharing, review-and-autonomy/autonomy-calibration. Hinges on: who owns the identity it acts as.
- V3 Ticket generation from an approved spec: the agent drafts tickets that point back to spec sections; engineering reviews them. Varies by: work-structure, review-and-autonomy/review-gate-placement. Hinges on: a spec standard (S05) that is machine-readable enough.

---

### S08. Get a launch ready
Source job: J7   Span: multi-session

**NEED**
- Performer: PM or PMM; engineering, sales, support, legal contribute.
- Goal: ship with the right audience told, supported and ready: launch tier, messaging, enablement material, release notes, FAQs and a measurement plan.
- Trigger and context: a release date is set or a feature is about to ship.
- Done looks like: a launch plan with tier and timeline, approved messaging, enablement one-pagers, release notes, FAQ and readiness checklist done, with a plan to measure results.
- Success criteria: no function is surprised; materials match what actually shipped; the launch is measured; the decision rights between PM and PMM were clear when disagreements arose.

**TODAY**
- Steps: copy shipped scope from tickets; ask a chat for release notes or FAQs; paste into docs; chase approvals in Slack; update decks. `[G]` `[A]`
- Tools: docs, slides, ticket tool, Slack, CRM or enablement tool.
- Pain: the PM/PMM line varies by company and no source settles decision rights `[E: productschool-launch-checklist-product-marketers](../../research/sources/productschool-launch-checklist-product-marketers.md)`; no survey in the library reports AI use in launch work, so pain here rests on the nature of the task `[A]`; Ramp reports a shipped-feature email skill (5,000+ emails; volume only) `[E: x-eglyman-introducing-glass-learn-things-once](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md)`.
- Hand-offs: engineering (scope), PMM (messaging), sales/CS (enablement), legal.
- Time cost: not established.

**VARIANTS**
- V1 Drafts from shipped scope: the agent drafts release notes, FAQ and enablement material from tickets and specs; the performer edits. Varies by: work-structure, context-and-memory/org-context-grounding-source. Hinges on: spec/ticket quality.
- V2 Checklist run: a launch-readiness check polls each function's status and flags gaps. Varies by: session-persistence-sharing, review-and-autonomy/autonomy-calibration. Hinges on: each function's state living somewhere the agent can read.
- V3 Multi-party review room: PM, PMM, sales and support review the same materials with the agent applying edits. Varies by: session-persistence-sharing, agent-identity-delegation. Hinges on: who may approve what.
- V4 Launch kit as project artifacts: release notes, FAQ and enablement material are typed artifacts in the project, each pointing at the shipped scope it describes, so sales and support find the current version and stale copies are visible as superseded. Varies by: artifact-and-project-structure. Hinges on: whether the receiving teams will look in the project rather than their own drives.

---

### S09. Tell stakeholders where we stand
Source job: J8   Span: recurring

**NEED**
- Performer: PM or head of product; execs, partner teams and customers read.
- Goal: give each audience a short, accurate update they can act on, in the form they read, and raise the decisions and risks that need them.
- Trigger and context: a weekly/monthly cadence, a milestone, a risk, or an exec request.
- Done looks like: an update per audience (exec brief, engineering detail, customer-facing) sent through the right channel, with decisions needed highlighted; sent only after the performer approved it.
- Success criteria: facts match the sources; tone fits the audience; the performer decides what to escalate; effort is a fraction of writing each from scratch; no one is surprised by something known earlier.

**TODAY**
- Steps: gather status from tickets and Slack; ask a chat for a draft; rework; paste into email, Slack or slides; repeat for each audience. `[G]` `[A]`
- Tools: chat/Claude Code, docs, slides, email, Slack.
- Pain: communication is the third most common PM AI use (18.5%); presentations are a top time-saver (vendor survey) `[E: lennys-newsletter-ai-tools-overdelivering-results](../../research/sources/lennys-newsletter-ai-tools-overdelivering-results.md)`, `[E: productboard-ai-in-product-management-report](../../research/sources/productboard-ai-in-product-management-report.md)`; alignment on priorities remains a persistent challenge `[E: atlassian-bottleneck-keeps-shifting-gamma](../../research/sources/atlassian-bottleneck-keeps-shifting-gamma.md)`; a Meta brief dropped all source links in early use `[E: lenny-newsletter-meta-chawla-pm-leader-agents](../../research/sources/lenny-newsletter-meta-chawla-pm-leader-agents.md)`.
- Hand-offs: leaders, partners, customer-facing teams.
- Time cost: not established.

**VARIANTS**
- V1 Draft for approval: the agent drafts per-audience versions from status data; the performer approves each before sending. Varies by: review-and-autonomy/review-gating, capability-format-portability. Hinges on: who may send on the performer's behalf.
- V2 Standing update: on schedule the agent prepares the update and parks it for the performer's approval. Varies by: runtime-location, session-persistence-sharing, review-and-autonomy/autonomy-calibration. Hinges on: runtime for unattended jobs.
- V3 Pull-based answers: stakeholders query a live view of status and decisions rather than receiving updates. Varies by: session-persistence-sharing, agent-identity-delegation, context-and-memory/context-location. Hinges on: what stakeholders may see (permissions) and whether they trust it.
- V4 Updates as artifacts: the sent update is also kept as a typed artifact in the project with the status sources it drew on; the performer approves once, and later updates or a reviewer's "what did we say last month?" start from the kept copy. Varies by: artifact-and-project-structure. Hinges on: where updates are sent versus kept, and whether the kept copy is the one people trust.

---

### S10. Read the metrics and decide
Source job: J9   Span: recurring

**NEED**
- Performer: PM or analyst; the team and leaders use the decision.
- Goal: understand what the numbers say about a product or experiment, what drove changes, and what to do (ship, iterate, kill, dig deeper).
- Trigger and context: a metrics review cycle, a spike or drop, an experiment readout, or a decision that needs data.
- Done looks like: a readout that states what changed, the likely drivers, confidence, the decision taken or recommended, and what to measure next; the queries and numbers behind it are reproducible.
- Success criteria: numbers are correct and reproducible; interpretation is the performer's; anomalies are noticed early; human validation catches what automated evals miss.

**TODAY**
- Steps: open dashboards; export or query data; paste into chat to interpret; write up; sometimes ask an analyst. `[G]` `[A]`
- Tools: analytics tools, SQL/BI, spreadsheets, chat.
- Pain: data literacy is the top rising skill and few measure AI ROI by business outcomes `[E: productboard-ai-in-product-management-report](../../research/sources/productboard-ai-in-product-management-report.md)`; Gamma's A/B tests showed evals missed a customer preference `[E: atlassian-bottleneck-keeps-shifting-gamma](../../research/sources/atlassian-bottleneck-keeps-shifting-gamma.md)`; no experimentation-specific workflow was found in the library `[E: THEMES metrics-review-agents](../../research/THEMES.md#metrics-review-agents-metrics-review-and-analytics-agents)`.
- Hand-offs: analysts, data engineers, leadership.
- Time cost: not established.

**VARIANTS**
- V1 Guided analysis: the performer asks questions of the data in a session; the agent shows its queries; the performer interprets. Varies by: capability-format-portability, context-and-memory/org-context-grounding-source. Hinges on: read access to analytics and definitions of metrics.
- V2 Anomaly watch: a scheduled agent flags changes and drafts a short explanation for review. Varies by: runtime-location, review-and-autonomy/autonomy-calibration. Hinges on: false-alarm rates.
- V3 Shared readout: the readout, queries and data are kept together and open to the team for questions. Varies by: session-persistence-sharing, context-and-memory/memory-design. Hinges on: data permissions across the team.
- V4 Metric readouts with their queries: the readout is stored with the queries and data definitions, so it can be rerun. Varies by: artifact-and-project-structure, context-and-memory/org-context-grounding-source. Hinges on: BI and analytics connectors; hosted MCP exists for some tools (Amplitude) but others need admin work (Snowflake, Looker).

