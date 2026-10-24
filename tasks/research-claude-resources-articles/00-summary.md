# Summary: claude.com/resources (AI-native SDLC playbook and related)

Task: [research-claude-resources-articles](../research-claude-resources-articles.md). Triage: [01-triage.md](01-triage.md). Theme evidence: [research/themes/research-claude-resources-articles.md](../../research/themes/research-claude-resources-articles.md). Options for the director to merge: [options/contributions/research-claude-resources-articles.md](../../options/contributions/research-claude-resources-articles.md).

**What was done (2026-10-24).** I read the [AI-native SDLC playbook](../../research/sources/claude-ai-native-sdlc-playbook.md) in full and triaged every English page on claude.com under `/resources/` and `/customers/`: 695 items from the sitemap, with guides counted once (145 guide pages in all). 29 came out high and 66 medium; they are filed as 95 source notes (`claude-*`, `filed_by: research-claude-resources-articles`), with companion pages folded in. 9 items were already in the library and were not re-filed. Webinar pages are event listings with no transcripts, so all of them were triaged low. Every source here is Anthropic's own publication. Notes label Anthropic describing itself as **first-party** and customer stories and commissioned surveys as **vendor claim**. **None of the 95 reports a controlled outcome.**

## 1. What these pages add, by theme

**opportunity-to-code-chain / agent-factory-sdlc (the biggest addition).** The playbook is the most explicit vendor version yet of the chain the project has been tracing from Stripe and Ramp. Every stage commits one artifact that the next stage reads: intent.md → spec.md → plan.md → diff and tests → PR with review findings → incident record → a new intent.md. In the playbook's words, the chain of commits "is also the audit trail". Three things differ from the Stripe whiteboard chain:
- **It starts at intent.** Problem and proposed outcome are fields inside intent.md. Any employee writes it with Claude in claude.ai or Cowork, and a git connector commits the file for them. The opportunity, problem and goal stages that Stripe keeps human are folded into one originator-written artifact. Anthropic's trends report goes further and compresses requirements and design into "express intent (minutes)" ([trends](../../research/sources/claude-2026-agentic-coding-trends.md)).
- **The product owner reviews and does not write.** "The product owner reviews that spec, but doesn't write it." Claude drafts the spec under the organisation's skills and flags conflicts between policies for named policy owners.
- **The loop closes on its own.** A deterministic monitor writes the next intent.md when a metric breaches its control band, so "a loop can begin and end without anyone starting it".

Customer and internal pages fill in the stages:
- Front end, from feedback to an actionable list: Rakuten, Anthropic's own Claude Tag consolidation, ABC Legal ([rakuten](../../research/sources/claude-customers-rakuten-every-employee-builder.md), [how-anthropic-uses-tag](../../research/sources/claude-how-anthropic-uses-claude-tag.md), [abc-legal](../../research/sources/claude-abc-legal-managed-agents-builders.md)).
- A plan layer between request and coding agent: CodeRabbit ([coderabbit](../../research/sources/claude-coderabbit-plan-orchestration.md)).
- The maintain stage closing back into code: Sentry, Anthropic CI on-call ([sentry](../../research/sources/claude-customers-sentry-bug-fixing-agents.md), [tag-ci-cd](../../research/sources/claude-tag-ci-cd-first-responder.md)).

**agent-led-intent-shaping / intent-factory-before-discovery.** The evidence is first-party and practical:
- The Fable field guide's "blind spot pass" and one-question-at-a-time interview ([fable-finding-unknowns](../../research/sources/claude-fable-finding-unknowns.md)).
- The founders' playbook's adversarial pressure-test before any prototype ([founders-playbook](../../research/sources/claude-founders-playbook.md)).
- The Claude Design designer's view that as building gets cheap, "the work that matters most moves earlier in the process" ([design-designer-workflow](../../research/sources/claude-design-designer-workflow.md)).
- The strongest support for intent-first is Asana's: automated feedback-to-PR loops "bloated cycles" until planning and decisions were gated ([asana-coach](../../research/sources/claude-asana-agents-you-can-coach.md)).

**harness-over-model, with a decay clause.** Anthropic now states it directly: the harness "determines how Claude Code performs more than the model alone" ([large-codebases](../../research/sources/claude-code-large-codebases.md)). It pairs this with an upkeep rule: scaffolding that encodes model weaknesses goes stale and should be pruned on each release ([harness-design-three-patterns](../../research/sources/claude-harness-design-three-patterns.md), [pm-on-the-ai-exponential](../../research/sources/claude-pm-on-the-ai-exponential.md)). Ramp builds "for the model that doesn't exist yet" ([ramp-office-hours](../../research/sources/claude-customers-ramp-office-hours.md)).

**Skills, plugins, subagents and harness steering.** The steering menu has seven mechanisms, and "instructions are not guardrails" ([steering](../../research/sources/claude-steering-claude-code.md)). The playbook's rule is that a skill is an advisory control and needs a hook behind it. Anthropic's newest guidance is to **fold subagents back into one loop with progressively disclosed skills**, with subagents only for context bloat, parallel throwaway work or tool conflicts ([fold-subagents](../../research/sources/claude-fold-subagents-into-main-loop.md), 2026-10-22). Skill sprawl is now a reported failure mode: Brainlabs reached about 400 skills in four weeks, and Miro found over-built skills "less reliable, not more" ([brainlabs](../../research/sources/claude-customers-brainlabs-cowork-skills.md), [miro](../../research/sources/claude-customers-miro-champions.md)).

**Shared and persistent sessions; identity.**
- Claude Tag is Anthropic's answer for the shared agent. Its identity model runs the agent as itself per channel, because act-as-user breaks under autonomy, and its stated default is "generous access first" ([agent-identity-access-model](../../research/sources/claude-agent-identity-access-model.md)).
- Personal connectors are a new hybrid: the channel identity covers shared and unattended work, and the requester's own identity covers reads they start ([tag-personal-connectors](../../research/sources/claude-tag-personal-connectors.md)).
- Cowork and the new Claude Code projects persist in the cloud, but each has a **single owner**. Cyera's call to "graduate" a personal agent into a team agent is unmet ([cyera](../../research/sources/claude-customers-cyera-cowork-front-door.md), [projects-redesigned](../../research/sources/claude-code-projects-redesigned.md)).
- Automations now start more sessions than people do at Ramp, and account for 90% of agent turns at Notion (vendor claims).

**Context and knowledge.** Anthropic's analytics agent gives the most rigorous first-party evidence so far that **curated, governed context beats raw retrieval** ([self-service-analytics](../../research/sources/claude-anthropic-self-service-analytics.md)):
- Grep over thousands of past queries moved accuracy by less than 1 point.
- Metric definitions written by an LLM made results worse.
- Skills left un-updated drifted from about 95% to about 65% accuracy in a month.

The CLAUDE.md "correction log" rule ("mistake twice → CLAUDE.md") and the lessons.md-to-skill promotion loop give compounding-context-repo concrete mechanics.

**Governance in regulated settings.**
- The playbook includes a worked managed-settings file for a regulated enterprise.
- Inference hooks add inline DLP, enforced server-side ([inference-hooks](../../research/sources/claude-enterprise-inference-hooks.md)).
- The apps gateway is a self-hosted control point for Claude Code ([apps-gateway](../../research/sources/claude-apps-gateway.md)).
- The CISO guide offers a four-question risk test ([ciso-guide](../../research/sources/claude-ciso-guide-agentic-ai.md)).
- The Deputy CISO's account shows **upstream risk classification at shaping time running in production**: an Opus-powered project security review lets teams self-approve low-risk launches ([securing-sdlc](../../research/sources/claude-securing-ai-native-sdlc-at-anthropic.md)).
- Regulated customers wall regulated data off from the agent environment (League, Tennr, Insight Health).

**Adoption.** Anthropic's Cowork maturity ladder runs from chat to deliverable, skill, scheduled bundle and department plugin, led by champions ([deploying-cowork](../../research/sources/claude-guide-deploying-cowork-across-org.md)). Customers describe several other patterns:
- Forcing events: League went live over one weekend.
- Open tokens: Ramp and DoorDash set no budgets.
- PM peer showcases: HubSpot, Slack.
- Builder steering committees: ABC Legal.

Anthropic's own scaling guide is engineer-only, with one line on PMs ([scaling-agentic-coding](../../research/sources/claude-guide-scaling-agentic-coding.md)).

**Evals.** The playbook adds **evals on the agent's own configuration**: an eval suite runs in CI whenever CLAUDE.md, skills or hooks change, and every incident becomes an eval. Other eval ideas from the pages:
- Draft-retention rate as a pilot metric ([financial-guide](../../research/sources/claude-guide-financial-industry.md), [epic](../../research/sources/claude-customers-epic-internal-adoption.md)).
- Chat reactions harvested as labels (ABC Legal).
- Rubric-graded outcomes ([dreaming-outcomes](../../research/sources/claude-managed-agents-dreaming-outcomes.md)).
- Anthropic's admission that PRs are "an incomplete measure" ([contribution-metrics](../../research/sources/claude-code-contribution-metrics.md)).

## 2. By dimension (details in the contributions file)

| Dimension | What's new |
|---|---|
| intent-shaping-and-spec | Committed artifact chain; product owner reviews an agent-written spec; spec as a verified contract (Datadog); validate before build; comprehension gate before merge |
| artifact-and-project-structure | One system of record per artifact (repo / legacy tool / linkage), the playbook's answer for orgs whose auditors accept Jira; project as a coordinator over parallel threads |
| review-and-autonomy | Gate at the accepted artifact rather than the action (users reject 39% of plans vs 3% of permission prompts); autonomy tiered by environment; per-channel autonomy; control-band tiers for unattended runs |
| pm-agent-evaluation | Evals on agent config in CI; draft-retention; harvested labels; rubric grader; four-axis builder eval |
| work-structure | Fold-in (one loop, many skills) as Anthropic's current default; a loop taxonomy; model-generated workflows |
| agent-identity-delegation | Hybrid channel/requester identity; single-purpose service identity; per-user authz inside tools |
| governance-control-plane | Server-side inline DLP; agents-as-code; tiered intake (Jamf); central core plus domain-owned skills |
| capability-distribution-trust | Policy-owner sign-off on skills; peer quality pass plus skill auditor; one canonical skill repo synced to every surface |
| context-and-memory | CLAUDE.md as correction log; lessons log promoted into skills; scheduled memory consolidation |
| adoption-model, sequencing, harness-upkeep | Peer showcase; open tokens; forcing events; dependency-ordered plays; plan CI capacity first; skills edited in the same PR as the data they describe |

No new dimension is proposed.

## 3. Where these agree with or contradict what's filed

**Agree / reinforce**
- harness-over-model (now stated first-party), risk-sloped-review, human-review-gates at the PR, and compounding-context-repo.
- intent-factory-before-discovery: Asana's bloated cycles, and the playbook's "the bottleneck moves to the steps to the left and right of the build phase".
- The Stripe and Ramp teardowns:
  - Stripe's knowledge-agent "one front door" pattern applies to knowledge agents, not coding tools. Stripe runs six coding assistants side by side ([stripe](../../research/sources/claude-customers-stripe-claude-code-rollout.md)).
  - Ramp's office-hours transcript confirms the Inspect, automation and "agents for every stage" picture.

**Contradict / sharpen**
1. **Subagents.** Anthropic's October fold-in guidance cuts against its own April multi-agent patterns, its trends report's "multi-agent hierarchies" prediction, and the one-job-per-agent evidence filed earlier (Cloudflare's specialist reviewers, 12-Factor). The lint pass should weigh one-job-per-agent against single-agent-many-skills.
2. **Who edits skills.** The playbook requires a named policy owner to sign off skill changes. Notion's self-updating skills, and Netflix keeping corrections in Managed Agents memory "instead of" editing skills, bypass review.
3. **Advisory vs enforced policy.** The scaling guide calls security rules in CLAUDE.md "policy-as-code"; the playbook says such guidance is advisory and needs a hook behind it.
4. **Cost.** Ramp and DoorDash run with no token budgets. Anthropic's own advice is to gate access, then cap. Ramp's "no budget" also sits awkwardly with the budget-overrun origin story of Glass ([ramp-introducing-glass](../../research/sources/ramp-introducing-glass.md)); scope or timing may differ.
5. **Claude Tag identity.** The filed docs say "everyone in the channel gets the same capability". That no longer holds for personal-connector requests.
6. **Compliance API.** The July CISO guide says Cowork is not captured in the Compliance API; the August note on Compliance API coverage says it is. The gap is probably closed.
7. **Harness vs model.** Delivery Hero says new models, not tooling, drove its gains: one customer's counterpoint.
8. **Rollout order.** The financial-industry guide starts with skills and add-ins and brings Cowork in last; the Cowork maturity ladder starts in Cowork.
9. **Shifting customer numbers.** Zapier's adoption moved from 89% and 800+ agents (January) to 97% and "thousands". Some customer pages contradict themselves on titles and timelines (Twilio, League, the PM app, Jamf), which the notes record.

## 4. For the strategy story (tasks/strategy-story-and-explainer-video/)

- **A vendor-backed spine.** The playbook's committed artifact chain, with Anthropic's name on it, is close to the opportunity-to-code story and Helm's hand-offs:
  - "Analyst agents in" matches intent arriving from monitoring.
  - "Coding agents out" matches spec, plan and PR.
  - "Monitoring after launch" matches the control-band loop that writes the next intent.md.
- **The gap Helm can own.** The playbook (and Anthropic's trends report even more) starts at an already-formed intent: "express intent (minutes)". Opportunity, problem and goal shaping, and choosing what enters the cycle, are left to the originator plus one product-owner review. That is the space the story's product agent fills. Asana's "automated feedback-to-PR loops bloated cycles" is the supporting evidence that it matters.
- **Usable lines** (first-party, short):
  - "The bottleneck moves to the steps to the left and right of the build phase."
  - "The product owner reviews that spec, but doesn't write it."
  - "The agent may act up to the production gate and cannot pass it."
  - "The skill makes violations rare and the hook makes them close to impossible."
- **Scale facts** (first-party, Anthropic about itself): Claude writes about 80% of merged code; CI jobs rose 25x in six months ([ci-test-impact](../../research/sources/claude-ci-test-impact-analysis.md), [securing-sdlc](../../research/sources/claude-securing-ai-native-sdlc-at-anthropic.md)).
- **Customer claims, label them as such:** Ramp says automations now start more agent sessions than humans; Notion says 90% of agent turns come from automations.
- **A shepherd in practice.** Claude Tag in a channel (Anthropic CI on-call; Carvana alerts to fixes; Tennr's per-channel autonomy) is a working example of the "shepherd and accept" persona. Its open problem is identity: the agent runs as itself, and personal connectors are bolted on.
- **Caveats for the film.** Everything here is vendor material with no outcome data. Claude Design, Claude Tag, Claude Security and several loop features are beta or research preview. Anthropic's own guidance changed within months (subagents; chat vs Cowork). DoorDash also says the new bottleneck is cross-functional alignment ("do we even need to have product review?"), which the story could use as the complication.

## Could not verify / follow-ups

- The two pieces linked from the playbook ("How the Claude Code team does code review" and "Redesigning source control at Anthropic") were filed later for the PDLC map: [claude-dev-claude-code-team-code-review](../../research/sources/claude-dev-claude-code-team-code-review.md), [anthropic-redesigning-source-control-scion](../../research/sources/anthropic-redesigning-source-control-scion.md). See also the Anthropic lifecycle map: [02-pdlc-agent-ecosystem-map.md](02-pdlc-agent-ecosystem-map.md).
- Webinar recordings (e.g. "How Anthropic works with Claude Tag in Slack", whose blurb claims Claude Tag "opens roughly 65% of our pull requests"; "Measuring AI Fluency"; "Evals for AI agents") would need a transcript pass.
- Gated guides were filed from their landing pages only: the CIO pilot-to-production blueprint's tier contents and the six-month Cowork rollout framework.

## Pattern classes

Added 2026-10-24 by teardowns-to-pattern-classes. This summary's examples are placed in the runtime pattern classes P1-P10 of the [taxonomy synthesis, B.2](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#b2-pattern-classes). Every placement is sourced and marked clear, partial or contested in [the mapping, section 2.4](../teardowns-to-pattern-classes/00-mapping.md).

- **P1:** Claude Code and Cowork with plugins (clear).
- **P6:** Code Review is a deployed reviewer called on pull requests (clear).
- **P7:** cloud sessions, Managed Agents and the ABC Legal fleet (clear).
- **P8:** Claude Tag shared channel sessions (clear).
- **P10:** the org plugin marketplace and skill sync (clear).
- **Contested:** Managed Agents as a P4 meta-harness, since it hosts one vendor's loop.
- **Evidence:** first-party.
- **Revised classes (2026-10-24):** Managed Agents moves from contested P4 to P7, as a hosted harness service. Claude Tag is P8b: channel-scoped, with the agent's own identity. See [the mapping, section 8](../../tasks/teardowns-to-pattern-classes/00-mapping.md#8-revised-classes-2026-10-24).
