#!/usr/bin/env python3
"""Builds index.html: the product and software lifecycle laid against six agent ecosystems.

Everything on the page comes from the six per-ecosystem maps and the source notes they cite.
Run: python3 index.build.py  (writes index.html next to this file)
"""
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "index.html"
SRC = "../../research/sources/"
DIM = "../../options/DIMENSIONS.md"


def src(slug, label=None):
    return f'<a href="{SRC}{slug}.md">{escape(label or slug)}</a>'


def srcs(*pairs):
    return "; ".join(src(s, l) for s, l in pairs)


# ---------------------------------------------------------------- ecosystems
ECOS = [
    dict(
        key="stripe", name="Stripe", folder="../competitive-teardown-stripe-knowledge-agents/",
        mapfile="02-pdlc-agent-ecosystem-map",
        tagline="Named agent per task; the link between the research agent and the planning agent is not in the record.",
        seam_title="Between agents: Kai → Orbit",
        seam=("Kai's context is 'locked in' single-user sessions by Stripe's own account, and Orbit starts from intent a person types. "
              "No public source describes a Kai → Orbit handoff. What bridges them is people, the shared tool layer (Toolshed) and shared documents (Trailhead). "
              "At Stripe one person often researches and plans, so the missing link costs little there; it bites when the tasks sit with different people."),
        seam_src=[("stripe-meet-knowledge-ai-platform", "Kai post"), ("youtube-notmybusiness-inside-stripe-ships-fast", "Orbit video"), ("stripe-minions-part-2", "Minions part 2")],
        handoffs=dict(total=9, doc=7, inf=1, unk=1, note="7 documented includes one with the mechanism unknown and one partly roadmap; the map gives no counts, so these are ours"),
        evidence=dict(n=12, fp=11, vc=0, ind=1, an=0, span="Feb–Oct 2026, plus one 2024 culture piece", single="Orbit rests on one vendor-produced video and one tweet; how often one person does both research and planning is unmeasured"),
        unit="Many narrow agents, one per task: Kai (research), Harbor and Protodash (prototype), Orbit (plan), Minions (code), Gru (review), 100+ compliance agents",
        unit_src=[("stripe-meet-knowledge-ai-platform", "Kai"), ("stripe-harbor-ai-prototyping", "Harbor"), ("youtube-notmybusiness-inside-stripe-ships-fast", "Orbit, Gru"), ("stripe-minions-one-shot-coding-agents", "Minions")],
        iface="Kai: web app first, plus Slack, a Chrome extension and API embeds ('the agent is a service, not an application'). Minions start from a Slack emoji reaction. Harbor has its own app",
        iface_src=[("stripe-meet-knowledge-ai-platform", "Kai post"), ("howiai-stripe-minions-kaliski", "Kaliski"), ("stripe-harbor-ai-prototyping", "Harbor")],
        privacy="Kai sessions single-user and private; sharing across sessions and people is roadmap. Minion runs post to a public channel. Orbit workspaces share context across sessions",
        privacy_src=[("stripe-meet-knowledge-ai-platform", "Kai post"), ("howiai-stripe-minions-kaliski", "Kaliski"), ("youtube-notmybusiness-inside-stripe-ships-fast", "video")],
        bridge="Shared tools (Toolshed, ~500 MCP tools) and shared documents (Trailhead, Google Docs, Slack threads, tickets); a Slack thread can be a minion's prompt. No handoff artifact between research and plan",
        bridge_src=[("stripe-minions-part-2", "Minions part 2"), ("stripe-minions-one-shot-coding-agents", "part 1")],
        review="A person on every PR plus Gru; CI capped at two rounds; 1% canary with auto-pause on release",
        review_src=[("youtube-notmybusiness-inside-stripe-ships-fast", "video"), ("stripe-minions-part-2", "part 2")],
        classes="Kai P5b (company agent service); Minions P3, P7 and P9 with a P8e watch-only run channel; Orbit P8f (shared plan workspace, partial); Kai projects P4 front-door dispatcher (partial); Harbor over MCP P6 (partial); Kai skills, Agent Studio and Toolshed P10 (partial); Claude Code and Cursor P1",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#23-stripe",
    ),
    dict(
        key="ramp", name="Ramp", folder="../competitive-teardown-ramp-glass/",
        mapfile="07-pdlc-agent-ecosystem-map",
        tagline="Stage agents on one harness; the define → build 'contract' is named but its transport is not described.",
        seam_title="Between sessions owned by different people",
        seam=("Charles names what define hands to build: data, 'the actual requirements that they can use for their coding agents, and a prototype', 'the next contract'. "
              "No source shows how that bundle moves from a PM's Glass session to an engineer's Inspect session. Where Ramp does carry context across people it carries the session itself "
              "(shared Glass sessions, multiplayer Inspect). For small work an agent runs the whole loop and the people boundary disappears."),
        seam_src=[("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles"), ("x-eglyman-introducing-glass-learn-things-once", "Glyman"), ("ramp-builders-why-we-built-background-agent", "Inspect post")],
        handoffs=dict(total=19, doc=14, inf=2, unk=3, note="14 documented = 11 with mechanism plus 3 documented as a sequence with one link's mechanism unknown"),
        evidence=dict(n=13, fp=10, vc=3, ind=0, an=0, span="Jul 2025–Oct 2026", single="Review Buddy, Testo, Gadget and the insight agent appear only in one talk; every figure is Ramp's own; no deploy step described"),
        unit="One agent per stage, all on one harness (Laminar): insight agent, Glass (define), Inspect (build), Review Buddy, Testo, Gadget, OCA",
        unit_src=[("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles"), ("ramp-builders-building-laminar", "Laminar post")],
        iface="Glass is its own desktop app; Inspect is reached from Slack, web, a Chrome extension and PR comments; Ramp Research answers in Slack threads",
        iface_src=[("x-sebgoddijn-glass-article", "Goddijn"), ("ramp-builders-why-we-built-background-agent", "Inspect post"), ("ramp-builders-meet-ramp-research", "Ramp Research")],
        privacy="Glass private by default with share-session; every Inspect session multiplayer with prompts attributed per person; PRs opened under the requester's identity",
        privacy_src=[("x-eglyman-introducing-glass-learn-things-once", "Glyman"), ("ramp-builders-why-we-built-background-agent", "Inspect post")],
        bridge="The session itself (shared or multiplayer); Glass memory rebuilt every 24 h from Slack, Notion and Calendar; Notion, Linear and Slack as the 'formal record' Gadget reads; Dojo skills",
        bridge_src=[("x-sebgoddijn-glass-article", "Goddijn"), ("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")],
        review="Review Buddy on '93% of our PRs', which also reads the prompts behind the code and picks the human reviewer; senior engineers on the hard 7%; nothing OCA proposes merges without a human",
        review_src=[("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles"), ("ramp-builders-how-we-built-oca", "OCA post")],
        classes="Glass P5a (per-employee workspace) on a P3 harness (Laminar), plus P7, P8c (private, shared on demand) and P10 (Dojo); Inspect P7 and P8d (multiplayer control plane); Ramp Research a P8b-related chat form; OCA P4, P6 and P9 (partial); the earlier Notion custom agents P11",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#21-ramp",
    ),
    dict(
        key="shopify", name="Shopify", folder="../competitive-teardown-shopify-river/",
        mapfile="01-pdlc-agent-ecosystem-map",
        tagline="One general agent in one public place; the break is at the thread's edges: the formal process, the durable artifact, and private work.",
        seam_title="Between the conversation and its formal process (GSD)",
        seam=("Inside a public Slack thread, research, intent, plan and code happen in one place with one agent, and people hand off by joining the thread. "
              "The break is at the edges: no documented link between a GSD project (Proposal, Prototype, Build, Release, Results) and its River threads; no structured intent or plan object; "
              "how a Quick prototype becomes production code is not described; and River refuses DMs and private channels, so sensitive work never enters the shared context."),
        seam_src=[("shopify-engineering-under-the-river", "Under the River"), ("lenny-how-shopify-builds-product", "GSD (2023)"), ("venturebeat-beyond-the-pilot-farhan-thawar", "Thawar")],
        handoffs=dict(total=20, doc=14, inf=2, unk=4, note="most documented handoffs rest on a single first-party source"),
        evidence=dict(n=14, fp=14, vc=0, ind=0, an=0, span="Jul 2023–Oct 2026; GSD evidence is 2023 and 2025", single="GSD rests on one 2023 interview (partly paywalled) and a 2025 memo; thread reuse is claimed, never measured; two first-party sources disagree on whether Quick sites can be restricted"),
        unit="One general agent (River) with profiles, used by 7,000+ people, plus narrow pipelines for structured jobs (Helix migration, Dispatch scanning, PR-review profile)",
        unit_src=[("shopify-engineering-under-the-river", "Under the River"), ("shopify-engineering-agentic-harness-outlasts-model", "Dispatch")],
        iface="Slack only, public channels, @-mention in thread; Quick sites and Remote Dev Live Preview as companion web surfaces for rich output",
        iface_src=[("x-tobi-river-replies-may-2026", "Tobi replies"), ("shopify-engineering-quick", "Quick"), ("shopify-engineering-remote-dev", "Remote Dev")],
        privacy="Public by default, no private mode: River refuses DMs and private channels; all Quick sites open to all employees (a 'secure version' is mentioned once)",
        privacy_src=[("venturebeat-beyond-the-pilot-farhan-thawar", "Thawar"), ("shopify-engineering-quick", "Quick"), ("x-tobi-learning-on-the-shop-floor", "Shop floor")],
        bridge="The public thread, searchable later; channel and per-person memory injected at session start; World (code, skills, AGENTS.md, 'intent documents'); nightly 'dreaming' and corpus mining rewrite skills",
        bridge_src=[("shopify-engineering-under-the-river", "Under the River"), ("fs-knowledge-project-tobi-lutke-ai-agents", "Knowledge Project")],
        review="A human reviewer on every PR ('now becoming a big bottleneck') plus a PR-review profile; merge queue; a freshness-gated queue for security merges",
        review_src=[("bvp-inside-shopifys-ai-first-engineering-playbook", "BVP"), ("shopify-engineering-under-the-river", "Under the River"), ("shopify-engineering-river-vulnerability-remediation", "vuln remediation")],
        classes="River on Aquifer P5b (company agent service) and P3; River P8a (public by default, chat-native) and P7; Dispatch and Roast P9; Helix P9 (partial); PR-review profile P6 (partial); profiles and World skills P10 (partial); engineers' local tools P1",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#22-shopify",
    ),
    dict(
        key="anthropic", name="Anthropic", folder="../research-claude-resources-articles/",
        mapfile="02-pdlc-agent-ecosystem-map",
        tagline="Open channels with a resident agent stand in for handoff artifacts; the customer playbook's intent.md chain is not shown in internal use.",
        seam_title="'The channel is the context'",
        seam=("Work defaults to open Slack channels with Claude Tag in them; agents read threads, past decisions and code instead of receiving a handoff document, and course corrections happen in the thread. "
              "Pods are one or a few people, so research, intent and plan usually sit with one person and the prototype is the spec. "
              "Where Anthropic names a break it is between meetings and documents, and between personal agents ('fleets of personal AIs ... fracturing the team's context'). "
              "No source shows a research artifact handed into another person's plan mode. The playbook's intent.md → spec.md → plan.md chain is a prescription for customers, not shown internally."),
        seam_src=[("claude-building-effective-human-agent-teams", "human-agent teams"), ("claude-dev-claude-code-team-code-review", "code review post"), ("claude-ai-native-sdlc-playbook", "playbook")],
        handoffs=dict(total=20, doc=15, inf=3, unk=2, note="the two unknowns are research → another person's plan, and the playbook's committed chain"),
        evidence=dict(n=27, fp=27, vc=0, ind=0, an=0, span="Jun 2025–Oct 2026", single="all self-reported by an AI lab whose users are its own builders; the internal Claude Tag PR share is known only from secondary coverage; how metrics readouts are produced is unstated"),
        unit="A general harness (Claude Code, Claude Tag, Cowork) with skills and plugins, plus engineered review agents (Code Review with voting, security review, risk classifiers) and per-component monitoring agents",
        unit_src=[("claude-dev-claude-code-team-code-review", "code review post"), ("claude-securing-ai-native-sdlc-at-anthropic", "securing the SDLC")],
        iface="Open Slack channels with Claude Tag (channel memory); Claude Code in the terminal and IDE; Cowork for non-engineers; Claude Design for designers",
        iface_src=[("claude-how-anthropic-uses-claude-tag", "Tag"), ("lenny-podcast-boris-cherny-after-coding", "Cherny"), ("claude-guide-deploying-cowork-across-org", "Cowork guide")],
        privacy="Channels public by default within the org, 'generous access first', a handful of workspace-level boundaries; Cowork sessions and Claude Code projects persist in the cloud with a single owner",
        privacy_src=[("claude-building-effective-human-agent-teams", "human-agent teams"), ("claude-cowork-web-mobile-handoff", "Cowork web"), ("claude-code-projects-redesigned", "projects")],
        bridge="Public channels and threads; CLAUDE.md, REVIEW.md and skills in repos; a shared eval repository; Claude-written explainers; lessons.md promoted to skills",
        bridge_src=[("claude-dev-claude-code-team-code-review", "code review post"), ("lenny-podcast-dianne-penn-evals-prds", "Penn"), ("claude-tag-ci-cd-first-responder", "CI on-call")],
        review="Agents first, people by risk tier (none, one or two humans); the person who directed the agent counts as a reviewer; blocking security review; incidents become reviewer evals",
        review_src=[("claude-dev-claude-code-team-code-review", "code review post"), ("claude-code-review-ga", "Code Review GA")],
        classes="Claude Code and Cowork with plugins P1; Claude Tag P8b (channel-scoped, own identity); Code Review P6; cloud sessions P7 and Managed Agents P7 as a hosted harness service; the org plugin marketplace and skill sync P10; the review stack P9 (partial)",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#24-anthropic",
    ),
    dict(
        key="atlassian", name="Atlassian", folder="../user-story-mapping/",
        mapfile="01-pdlc-agent-ecosystem-map",
        tagline="An object at every step and links between most of them; the work item carries the what, not the why. Mostly product capability, not internal practice.",
        seam_title="Artifacts as the handoff medium",
        seam=("Ideas, goals, specs, work items and PRs are linked objects, and any of five coding agents takes the same work item. "
              "But research stays in Rovo Chat (Confluence export is a vendor claim); what crosses from idea to work item is an optional copy of the description; "
              "an agent started by automation runs in a restricted mode that 'won't read Confluence content'; and no lifecycle record joins research → idea → spec → work item → PR. "
              "Internally, Atlassian made the PM's intent executable (a Loom talk track becomes work items, moving one to In Progress starts a coding agent) rather than carrying the evidence behind it."),
        seam_src=[("atlassian-jpd-link-idea-to-work-item", "JPD link"), ("atlassian-jira-coding-agent-generate-code", "coding agent"), ("lenny-podcast-tamar-yehoshua-roles-expanding", "Yehoshua talk")],
        handoffs=dict(total=27, doc=20, inf=2, unk=5, note="6 of the 20 documented rest on a vendor claim or a speaker report only; 2 have a partly unknown mechanism"),
        evidence=dict(n=22, fp=14, vc=5, ind=0, an=3, span="support docs undated; blogs Jan–Aug 2026", single="all internal-use claims come from one CPO talk (auto-captions) and one engineer's post; Jira Planner exists only in an Early Access launch blog; PR cycle-time figures (−30.8% paper, −45% blog) are unreconciled; the three independent reviews are anecdotes and don't cover the coding or planning agents"),
        unit="Narrow agents attached to platform objects: Jira Coding Agent, Jira Planner (Early Access), Rovo Dev reviewer, Ops Expert, Delivery Agent; third-party coding agents (Claude, Cursor, Copilot, Codex) assignable from the same work item",
        unit_src=[("atlassian-jira-manage-agents-in-space", "agents in a space"), ("atlassian-blog-introducing-jira-planner", "Planner"), ("atlassian-rovo-ops-expert-agent", "Ops Expert")],
        iface="Embedded in the system of record: Jira, Confluence, Loom, Bitbucket; Rovo Chat; a Jira agent in Slack; deep links into local coding tools",
        iface_src=[("atlassian-jira-coding-agent-generate-code", "coding agent"), ("atlassian-jira-open-work-item-in-coding-tool", "open in coding tool"), ("lenny-podcast-tamar-yehoshua-roles-expanding", "Yehoshua talk")],
        privacy="Platform permissions (spaces, page restrictions) govern visibility; interactive agents read as the user; automation-started agents run in a restricted mode without Confluence",
        privacy_src=[("atlassian-jira-coding-agent-generate-code", "coding agent")],
        bridge="Work items (summary, description, acceptance criteria, links), Confluence pages, JPD ideas, Goals; Teamwork Graph returns pairwise links; copying an idea into the work item is the only documented way its content reaches the agent",
        bridge_src=[("atlassian-rovo-jira-delivery-agent", "Delivery Agent"), ("atlassian-jpd-link-idea-to-work-item", "JPD link"), ("atlassian-goals-what-is-a-goal", "Goals")],
        review="A person reviews the draft PR plus Rovo Dev checks it against the work item's acceptance criteria (no check if the description is empty); review comments don't yet flow back to the agent automatically",
        review_src=[("atlassian-rovo-dev-acceptance-criteria-code-review", "AC review"), ("atlassian-blog-rovo-dev-in-jira", "Rovo Dev in Jira")],
        classes="Rovo agents (Chat, Deep Research, Delivery Agent, Ops Expert, Loom Record for agent, Planner) P11 (SaaS-embedded); Jira Coding Agent and third-party agents started from a work item P7; the Rovo A2A gateway P6; work-item dispatch to several agents P4 front-door dispatcher (partial); automation triggers P9 (partial)",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#25-atlassian",
    ),
    dict(
        key="intercom", name="Intercom", folder="../research-pm-agents-jobs-to-be-done/",
        mapfile="04-pdlc-agent-ecosystem-map",
        tagline="One general harness for everyone, with skills and hooks; intent is captured at the pull request and checked in review, and left to people upstream.",
        seam_title="Intent re-captured downstream, at the PR",
        seam=("A hook forces a create-pr skill that asks why the change exists and writes the answer into the PR description; review agents check the diff against that stated intent; "
              "at launch a 'what we built' doc feeds the support agent's readiness gate. Upstream, no source describes how the research team's syntheses reach the designers, PMs or engineers who shape and plan; "
              "the plan lives in a Claude Code session (5–20 plan-mode turns) and is not persisted. The first durable statement of intent is the PR description, which comes after planning."),
        seam_src=[("ideas-fin-how-we-use-claude-code-today", "Scanlan"), ("intercom-ai-approving-pull-requests", "AI approving PRs"), ("ideas-fin-nobody-changed-their-title", "Church")],
        handoffs=dict(total=14, doc=9, inf=2, unk=3, note="one documented handoff (plan → code) is anecdote-level"),
        evidence=dict(n=17, fp=15, vc=0, ind=0, an=2, span="Aug 2025–Aug 2026", single="Intercom sells Fin and an AI-native engineering story; the only in-depth outside interview is paywalled; no PRD, brief or ticket template was found; goal-setting is known only at company level"),
        unit="One general harness (Claude Code, MDM-installed for ~1,000 non-engineers too) with 13 plugins and 267 skills; the only named custom agents are the reviewer (Shrek) and Operator",
        unit_src=[("ideas-fin-how-we-use-claude-code-today", "Scanlan"), ("intercom-we-gave-claude-code-to-everyone", "Yakovenko"), ("intercom-ai-approving-pull-requests", "AI approving PRs")],
        iface="Claude Code in the terminal for engineers, designers, PMs and researchers; GitHub for review; Slack for notices; a read-only production console over MCP",
        iface_src=[("ideas-fin-how-we-use-claude-code-today", "Scanlan"), ("ideas-fin-how-we-design-when-code-writes-itself", "Moriarty")],
        privacy="Local sessions, private by default; research reports published with access control (Snowflake, Streamlit); the PR description is the shared record; SessionEnd hook mines transcripts for missing skills",
        privacy_src=[("ideas-fin-nobody-changed-their-title", "Church"), ("ideas-fin-how-we-use-claude-code-today", "Scanlan")],
        bridge="The PR description (why), skills and plugins (267, auto-installed), the Surge design system encoded as skills, a release tracker's 'what we built' doc; a queryable skill built from 60+ interviews",
        bridge_src=[("ideas-fin-how-we-use-claude-code-today", "Scanlan"), ("ideas-fin-eight-people-hold-the-bar", "de Róiste"), ("intercom-fin-npi-agent-readiness", "Fin NPI")],
        review="Specialised review sub-agents (Shrek) check the diff against the stated intent; ~19% of PRs auto-approved by risk and size; a person on about 80%; repo owners set the requirement",
        review_src=[("intercom-ai-approving-pull-requests", "AI approving PRs"), ("ideas-fin-webinar-qa-3x-rd-output", "webinar Q&A")],
        classes="Claude Code with plugins and hooks P1; Shrek reviewers P6; the CI-watching agent and Buzz P7 (partial); the plugin marketplace P10 (partial). Fin and Operator are products Intercom sells, so out of scope",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#26-intercom",
    ),
    dict(
        key="airbnb", name="Airbnb", folder="../research-airbnb-spotify-product-practices/",
        mapfile="01-pdlc-airbnb",
        tagline="The PM role split four ways and the CEO put in the gap; prototypes carry intent, evals carry evidence for AI features, decisions stay unwritten.",
        seam_title="A person in the gap: the CEO in every review",
        seam=("Airbnb split the PM's tasks across a product marketer (story), program manager (plan), designer (prototype) and business lead (model), so research → intent → plan crosses people by design. "
              "The bridge is the CEO, who reviews every project every 1–12 weeks; principles are deliberately unwritten ('one shared consciousness'). Since 2026 a short agent-drafted concept brief (Pascal) and many prototypes replace the spec, "
              "and Airbnb names the drift itself: the brief isn't updated after prototyping, reviews go out of order, and an 'AI project coordinator' to keep brief, prototypes and Jira in sync is only proposed. "
              "Where evidence does travel by artifact it travels as evals, for AI features only."),
        seam_src=[("dx-airbnb-beyond-the-cli-airchat", "DX talk"), ("verge-decoder-chesky-founder-mode-2024", "Decoder 2024"), ("airbnb-tech-eval-driven-development", "eval-driven development")],
        handoffs=dict(total=18, doc=14, inf=2, unk=2, note="2 of the 14 documented have the mechanism unknown (Pascal's brief, Everest)"),
        evidence=dict(n=24, fp=23, vc=0, ind=1, an=0, span="2016–Oct 2026; most 2023–26", single="Pascal, Everest, the prototyping tool and the AI coordinator are each known from one talk; code-share figures are defined inconsistently (59%, 60%, 'coauthored'); no independent check of any AI figure"),
        unit="An internal harness run as a product (AirChat: a CLI over Claude Code and Codex, SDK apps, Remote) plus narrow agents: Insight Miner (research), Pascal (brief), validation and critique loops, on-call agents, the support agent. None sets the goal or plans",
        unit_src=[("dx-airbnb-beyond-the-cli-airchat", "DX talk"), ("airbnb-tech-insight-miner-agent-harness", "Insight Miner")],
        iface="AirChat spans IDE plugins, a CLI over vendor agents, SDK web apps, Slack and a remote web UI; adoption organic through champions with no quotas, while the CEO tracks token use",
        iface_src=[("dx-airbnb-beyond-the-cli-airchat", "DX talk"), ("latent-space-airbnb-al-dahle-inside-out-ai", "Latent Space")],
        privacy="Not described for sessions. Decisions are kept unwritten on purpose; Everest, an LLM-built org context graph across the codebase, has unpublished inputs",
        privacy_src=[("verge-decoder-chesky-founder-mode-2024", "Decoder 2024"), ("latent-space-airbnb-al-dahle-inside-out-ai", "Latent Space")],
        bridge="The CEO in every review; one roadmap; Everest (code- and project-oriented); for AI features, taxonomies, seed queries and PM-labelled golden sets become evals; brief, prototypes and Jira drift after prototyping",
        bridge_src=[("lenny-podcast-brian-chesky-new-playbook", "Lenny's Podcast"), ("airbnb-tech-eval-driven-development", "eval-driven development"), ("dx-airbnb-beyond-the-cli-airchat", "DX talk")],
        review="The CEO reviews every project on a 1–12 week cadence with green/yellow/red scoring; engineers must be able to explain AI-written PRs; validation loops and a critic model run before the PR",
        review_src=[("lenny-podcast-brian-chesky-new-playbook", "Lenny's Podcast"), ("deepview-al-dahle-airbnb", "Deep View"), ("airbnb-tech-llm-test-migration", "test migration")],
        classes="AirChat (CLI and gateway over Claude Code and Codex) P4, clear on the definition but with no sub-shape for an in-house governed wrapper; engineers and non-engineers in Claude Code and Codex P1; AirChat Remote P7 and on-call agents P7 (partial); the migration framework P9 and @generateMock P9 (partial); Insight Miner P3 (partial); the AirChat marketplace P10 (partial). Pascal, Everest, the eval stack and the AI coordinator fit no class",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#29-airbnb",
    ),
    dict(
        key="spotify", name="Spotify", folder="../research-airbnb-spotify-product-practices/",
        mapfile="02-pdlc-spotify",
        tagline="The best-built systems context layer of the nine, and it stops at the code; the bet's evidence travels in the VP who pitches it.",
        seam_title="The VP carries the evidence; the catalog carries systems, not reasons",
        seam=("Agents get rich context about systems from the Backstage/Portal catalog (owners, lineage, standards, docs, skills as owned entities over MCP), and Xirp sessions write back to it. "
              "The why behind a bet travels in people: about 14 VPs pitch bets and the co-CEOs stack-rank 30–50 every six months, with VPs explaining the details in a weekly E-Team. "
              "Spotify built evidence-carrying intent artifacts (DIBB brief 2016, Thoughtful Execution tree 2020, Understand It Brief and Scorecard 2021), kept them optional and off the platform, and at least one has lapsed. "
              "No link exists from a bet to the prompts, PRs or A/B tests that serve it; Spotify says it is building one. Engineering intent, by contrast, is agent-ready: versioned prompts with done defined as tests."),
        seam_src=[("spotify-portal-blog-introducing-xirp", "Xirp"), ("colossus-ilb-gustav-soderstrom-how-spotify-thinks", "Invest Like the Best"), ("claude-customers-spotify-office-hours", "office hours")],
        handoffs=dict(total=18, doc=15, inf=1, unk=2, note="3 of the 15 documented describe 2016–21 practice whose current use is unknown"),
        evidence=dict(n=36, fp=33, vc=2, ind=1, an=0, span="2012–Oct 2026; agent evidence 2025–26", single="adoption figures conflict across Spotify's own sources (99%+, 96%, 76%, 73%, 60%); the 2025 bets-process details come from a third-party machine transcript; whether the 2020–21 intent artifacts are still used is unknown (one page now 404); nothing on prototype-to-ship conversion"),
        unit="Many agents, one context layer: Honk (background coder on the Claude Agent SDK), Xirp (multi-agent sessions across vendor CLIs), Vedder and AiKA (data and knowledge), Fleetshift (deterministic targeting), Confidence (experiments); no agent sets the goal or carries the bet",
        unit_src=[("spotify-engineering-honk-part-1-1500-prs", "Honk part 1"), ("spotify-portal-blog-introducing-xirp", "Xirp"), ("spotify-engineering-vedder-context-layer", "Vedder")],
        iface="Slack is the front door for Honk; AiKA is both an MCP client and an MCP server; Xirp is a multi-session workspace across vendor agents; PMs and designers prototype in Cursor; for big APIs a CLI is preferred over MCP",
        iface_src=[("spotify-engineering-honk-part-1-1500-prs", "Honk part 1"), ("spotify-portal-blog-aika-data-plugins", "AiKA"), ("spotify-portal-blog-introducing-xirp", "Xirp")],
        privacy="Not described for sessions. Xirp transcripts and metadata flow back to Portal; bet pitches and E-Team discussion happen in the room; the 2016 bets board was open",
        privacy_src=[("spotify-portal-blog-introducing-xirp", "Xirp"), ("colossus-ilb-gustav-soderstrom-how-spotify-thinks", "Invest Like the Best"), ("kniberg-spotify-rhythm", "Rhythm")],
        bridge="The Backstage/Portal catalog over MCP (owners, lineage, standards, TechDocs, skills as AiResource entities); Google Docs, Figma and MURAL for the 2020–21 intent artifacts, none linked to the catalog; no object for a bet or brief, and no link from bet to prompt, PR or test (being built)",
        bridge_src=[("backstage-docs-ai", "Backstage AI docs"), ("spotify-portal-docs-mcp", "Portal MCP"), ("claude-customers-spotify-office-hours", "office hours")],
        review="Deterministic verifiers in the stop hook and a verification service that runs real CI before any PR exists; code owners; auto-merge for safe fleet changes; an LLM judge was dropped; 'the next constraint became our ability to verify it'",
        review_src=[("spotify-engineering-honk-part-3-feedback-loops", "Honk part 3"), ("spotify-engineering-quality-at-higher-velocity", "Quality at Higher Velocity"), ("spotify-engineering-coding-no-longer-constraint", "Coding Is No Longer the Constraint")],
        classes="Honk P2 (Agent SDK inside Spotify's harness), P7 (background PRs) and P9 (inside Fleet Management), with P6 over MCP (partial) and P8 shared sessions in v2 (partial, sub-type unknown); Xirp P4 (clear, no sub-shape fits); Portal AiResource entities and Xirp's marketplace P10; Portal MCP Actions and Vedder P6 (partial); AiKA P5b (partial); engineers and PMs in Claude Code P1. Confidence and the eval funnel fit no class",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#28-spotify",
    ),
    dict(
        key="block", name="Block", folder="../research-block-product-practices/",
        mapfile="01-pdlc-block",
        tagline="A general harness for everyone (goose) with shared stage services on top; Block removes the people boundary rather than carrying context across it.",
        seam_title="No handoff to build: role collapse, and a ticket or thread into Builderbot",
        seam=("Research happens in a person's own local goose session against governed data MCPs; recipes and skills are shared but carry method, not findings, and no source shows a session or its findings handed to another person. "
              "The one documented shared handoff is a Linear or Jira ticket or a Slack thread into Builderbot, which researches, plans, codes and opens the PR while teammates steer: it is told what to build, not why. "
              "Block bridges the gap by role collapse: one DRI owns idea to scale, squads of 1–6, PMs and designers ship PRs, prototypes replace decks. The company 'world model' that would generate the backlog is a published plan, not a system in use. "
              "Staff say every change still needs a human approver and about 95% of AI changes needed edits."),
        seam_src=[("block-builderbot-rollout", "Builderbot"), ("block-from-hierarchy-to-intelligence", "essay"), ("guardian-block-workers-ai-cant-do-their-jobs", "Guardian")],
        handoffs=dict(total=17, doc=11, inf=2, unk=4, note="2 of the 11 documented have an upstream link or mechanism unknown"),
        evidence=dict(n=26, fp=23, vc=2, ind=1, an=0, span="Aug 2025–Oct 2026", single="no first-person account from a Block or Square PM; whether goose sessions can be shared is unknown; Builderbot numbers, the 90% review share and the 3x feature count are Block's own with no method; the Guardian's 95% figure is one anonymous staffer"),
        unit="One general agent per person (goose, with a curated bundle from ~150 MCP services), task agents as recipes and skills inside it, and shared stage services built on it: Builderbot for plan, code and review; Query Expert and the Data MCP for data. Engineers also buy seven coding harnesses",
        unit_src=[("lenny-podcast-block-dhanji-goose", "CTO"), ("block-builderbot-rollout", "Builderbot"), ("block-eng-ai-assisted-development-at-block", "AI-assisted dev")],
        iface="goose desktop and CLI, local and single-user; Builderbot from a Slack thread or a Linear/Jira ticket, steered in the thread; App Kit internal apps (1,000+ in a quarter, 80% of users outside engineering); Buzz as a shared workspace",
        iface_src=[("lenny-podcast-block-dhanji-goose", "CTO"), ("block-builderbot-rollout", "Builderbot"), ("block-eng-buzz", "Buzz")],
        privacy="goose sessions are local and nothing shows one shared; the Slack thread is the shared session for Builderbot; a human approver on every change, and AI use mandatory and monitored (staff, via the Guardian)",
        privacy_src=[("block-builderbot-rollout", "Builderbot"), ("guardian-block-workers-ai-cant-do-their-jobs", "Guardian")],
        bridge="A ticket or Slack thread (what, not why); prototypes and PRs in place of decks and docs; one MCP catalogue, a skills marketplace, AGENTS.md and an ai-rules generator across harnesses carry method, not findings; a company 'world model' is proposed, not shown",
        bridge_src=[("block-builderbot-rollout", "Builderbot"), ("block-eng-3-principles-agent-skills", "skills"), ("block-from-hierarchy-to-intelligence", "essay")],
        review="Builderbot reviewed 90%+ of change requests (Q1 2026); a person makes the final push on every change; headless goose drafts fixes for CI failures; compliance headcount 'basically not touched'",
        review_src=[("block-q1-2026-shareholder-letter", "Q1 2026 letter"), ("block-eng-actionable-ci", "Actionable CI"), ("a16z-owen-jennings-block-all-in-on-ai", "Jennings")],
        classes="goose P3 (own open-source harness) and, company-wide with a curated MCP bundle, P1 (partial); engineers' seven coding harnesses P1; Builderbot P7, in Slack threads P8 (sub-type unknown), as a service on goose P3 (partial); Buzz P8b and P4 (partial); Berd P5a (partial, one sentence); Actionable CI P9 and recipes P9 (partial); the Data MCP and Query Expert P6 (partial); the skills marketplace and ai-rules P10. Managerbot, Moneybot, App Kit and the proposed world model fit no class",
        classes_href="../teardowns-to-pattern-classes/00-mapping.md#27-block",
    ),
]

for e in ECOS:
    e["map_md"] = e["folder"] + e["mapfile"] + ".md"
    e["map_html"] = e["folder"] + e["mapfile"] + ".html"
    e["map_handoffs"] = e["map_md"] + "#every-handoff-task-to-task"
    e["map_tasks"] = e["map_md"] + "#the-lifecycle-task-by-task"
    e["map_cnv"] = e["map_md"] + "#could-not-verify"

# ---------------------------------------------------------------- tasks
TASKS = [
    ("spot", "Spot the opportunity", ""),
    ("talk", "Talk to customers", ""),
    ("research", "Research the problem", "read the data"),
    ("goal", "Set the goal", ""),
    ("intent", "Shape the intent", "prototype, spec"),
    ("plan", "Plan the change", ""),
    ("code", "Write the code", ""),
    ("review", "Review the change", ""),
    ("test", "Test", "row added by the Ramp map"),
    ("release", "Release", ""),
    ("operate", "Operate and learn", ""),
]

# status keys: doc (documented), inf (inferred), unk (unknown)
# A cell: agents, who, artifact, presence (agent / tool / none / na), handoffs = [(target, status, note, [sources])]
C = {e["key"]: {} for e in ECOS}

# ---- Stripe
C["stripe"]["spot"] = dict(
    agents="None named", who="Leaders, PMs, engineers wearing the 'product hat'", artifact="Not described", presence="none",
    handoffs=[("talk / goal", "unk", "no row in the map", [("pragmaticengineer-inside-stripe-engineering-culture-part-2", "Pragmatic Engineer")])])
C["stripe"]["talk"] = dict(
    agents="People; Kai does account research before calls", who="Engineers ('close to users'), PMs, researchers, account executives", artifact="Not shown (the whiteboard's 'customer conversations')", presence="tool",
    handoffs=[("shape intent", "inf", "people; not in any tool shown", [("youtube-notmybusiness-inside-stripe-ships-fast", "video"), ("stripe-meet-knowledge-ai-platform", "Kai post")])])
C["stripe"]["research"] = dict(
    agents="Kai: data analysis (5,000+ sessions a day), docs, email digests; 'ask data' over Hubble", who="Anyone: sales, finance, ops, engineers, PMs", artifact="Kai dashboards, reports, docs (single-user)", presence="agent",
    handoffs=[("shape intent (Harbor)", "doc", "Harbor's tools over internal MCP; a Kai analysis became a clickable prototype", [("stripe-harbor-ai-prototyping", "Harbor")]),
              ("plan (Orbit)", "unk", "not described; carried in one person's head and docs, or via docs, Slack, prototypes", [("stripe-meet-knowledge-ai-platform", "Kai post"), ("youtube-notmybusiness-inside-stripe-ships-fast", "video")]),
              ("other agents", "doc", "Kai 'invoke[s] more specialized agents'; mechanism unknown", [("stripe-meet-knowledge-ai-platform", "Kai post")])])
C["stripe"]["goal"] = dict(
    agents="None named", who="People (not shown in any tool)", artifact="Not described", presence="none",
    handoffs=[("shape intent", "inf", "people; not in any tool shown", [("youtube-notmybusiness-inside-stripe-ships-fast", "video")])])
C["stripe"]["intent"] = dict(
    agents="Harbor (12,000 prototypes); Protodash; Google Docs PRDs; agent-drafted specs reviewed as GitHub issues", who="Designers, PMs (Protodash's largest group), engineers, finance, account executives", artifact="Prototype URL with anchored comments; PRD; spec issue", presence="agent",
    handoffs=[("write code", "doc", "coding agents pull a prototype's file tree into a repo; a Protodash PR became an engineer's source of truth", [("stripe-harbor-ai-prototyping", "Harbor"), ("howiai-stripe-protodash-owen-williams", "Protodash")]),
              ("plan (Orbit)", "unk", "Orbit starts from intent a person types; no link from the prototype or PRD is described", [("youtube-notmybusiness-inside-stripe-ships-fast", "video")])])
C["stripe"]["plan"] = dict(
    agents="Orbit: reads code and Trailhead; 'Workspaces share context across sessions'", who="Engineers first; teammates comment", artifact="Shareable, commented plan", presence="agent",
    handoffs=[("write code (Minions)", "doc", "one button: devbox, plan and instructions; up to 12 hours; pauses to ask", [("youtube-notmybusiness-inside-stripe-ships-fast", "video")])])
C["stripe"]["code"] = dict(
    agents="Minions (~1,300 PRs a week); Claude Code, Cursor; the payment-method factory", who="Agents, started by engineers and increasingly by non-engineers from Slack", artifact="Branch and pull request", presence="agent",
    handoffs=[("review", "doc", "a person on every PR plus Gru; CI capped at two rounds (task row, not a handoff row)", [("stripe-minions-part-2", "part 2"), ("youtube-notmybusiness-inside-stripe-ships-fast", "video")])])
C["stripe"]["review"] = dict(
    agents="Gru; CI capped at two rounds", who="A person on every PR, plus an agent", artifact="Approved PR", presence="agent",
    handoffs=[("release", "doc", "1% canary, auto-pause and rollback (task row)", [("youtube-notmybusiness-inside-stripe-ships-fast", "video")])])
C["stripe"]["test"] = dict(na="Not split out; CI runs inside review")
C["stripe"]["release"] = dict(
    agents="1% canary, auto-pause and rollback", who="Automated", artifact="Live change", presence="tool",
    handoffs=[("operate", "unk", "no row in the map", [])])
C["stripe"]["operate"] = dict(
    agents="Kai (incident triage, digests); 100+ compliance agents; factory learning logs; Kai skill reflection (roadmap)", who="Ops, finance, compliance analysts, engineers", artifact="Answers, digests, improved prompts and skills", presence="agent",
    handoffs=[("shared knowledge", "doc", "factory learning and decision logs update prompts; Kai skill reflection is roadmap", [("stripe-payment-method-factory", "factory"), ("stripe-meet-knowledge-ai-platform", "Kai post"), ("aws-stripe-compliance-agents", "AWS")])])

# ---- Ramp
C["ramp"]["spot"] = dict(
    agents="Customer insight agent: ETL, vector search and clustering over Gong, Zendesk, LogRocket, surveys; Slack agent, dashboard, a daily channel and podcast", who="PMs, leaders; anyone reading the feeds", artifact="Clustered, traceable insight; daily digest", presence="agent",
    handoffs=[("talk to customers", "doc", "insight is traceable, so a PM can see 'exactly which customers to talk to'", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")])])
C["ramp"]["talk"] = dict(
    agents="Glass saved prompt pulls feature requests from calls (≈300 → ≈20,000 a month); earlier, Notion custom agents triaged sales feedback", who="Account managers, sales, PMs", artifact="Feature-request records; prioritised list", presence="agent",
    handoffs=[("records → prioritised list → customer email on ship", "doc", "sequence documented; how 'shipped' is detected is unknown", [("x-eglyman-introducing-glass-learn-things-once", "Glyman"), ("x-karimatiyeh-glass-feature-requests", "Atiyeh")]),
              ("research / intent", "unk", "no row in the map", [])])
C["ramp"]["research"] = dict(
    agents="Ramp Research (Slack data agent: 1,476 questions in four weeks vs 66 in the human channel); Glass with Snowflake; Gadget for 'ask the org'", who="Anyone: sales, ops, finance, PMs, engineers", artifact="Threaded Slack answers with CSV previews; Glass sessions", presence="agent",
    handoffs=[("scoping (project channels)", "doc", "teams add Ramp Research to channels 'to scope out new features'", [("ramp-builders-meet-ramp-research", "Ramp Research")]),
              ("shape intent (Glass)", "inf", "connected tools in every Glass install; carrying a thread's answers into a define session is not shown", [("x-sebgoddijn-glass-article", "Goddijn")])])
C["ramp"]["goal"] = dict(
    agents="None named; Glass 'understands our product strategy'", who="People (not shown)", artifact="Not described", presence="none",
    handoffs=[("shape intent", "unk", "not described", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")])])
C["ramp"]["intent"] = dict(
    agents="Glass as the define-stage agent: Snowflake, user research, strategy, spec conventions, design system and code base; 'AI is your tech lead'", who="PMs; others with Glass", artifact="'The next contract': data, requirements for coding agents, a working prototype", presence="agent",
    handoffs=[("plan", "inf", "inside Glass; no separate plan artifact", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")]),
              ("write code (Inspect, another person)", "unk", "the contract's contents are documented; how it travels between sessions or people is not", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")]),
              ("another person (shared session)", "doc", "share the Glass session; Inspect sessions are multiplayer", [("x-eglyman-introducing-glass-learn-things-once", "Glyman"), ("ramp-builders-why-we-built-background-agent", "Inspect post")])])
C["ramp"]["plan"] = dict(
    agents="No named planning agent; inside Glass or the small loops; Inspect sub-sessions for research across repos", who="PM in Glass, or an agent with a Slack sign-off", artifact="Not described as a separate artifact", presence="tool",
    handoffs=[("write code", "inf", "no row; the small loops are documented as a sequence (plan, Slack check, code)", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles"), ("ramp-builders-why-we-built-background-agent", "Inspect post")])])
C["ramp"]["code"] = dict(
    agents="Inspect (≈30% of merged PRs in Jan, >50% in Mar, '75%' in Sept; 1M sessions); Glass builds Glass", who="Engineers and non-engineers from Slack, web, Chrome extension, PR comments", artifact="Branch and PR opened under the requester's identity", presence="agent",
    handoffs=[("review (Review Buddy, human)", "doc", "Review Buddy reads the code and the prompts behind it, and picks the human reviewer", [("ramp-builders-why-we-built-background-agent", "Inspect post"), ("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")])])
C["ramp"]["review"] = dict(
    agents="Review Buddy: codebase, quality and security checks, 'all the prompts that led you to build that code'; '93% of our PRs'", who="A human reviewer the agent picks; senior engineers on the hard 7%", artifact="Reviewed PR", presence="agent",
    handoffs=[("test (Testo)", "doc", "sequence documented; routing of Testo's feedback back to code is unknown", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")])])
C["ramp"]["test"] = dict(
    agents="Testo: browser QA agent; runs the product in '100 different combinations' from production data; 425 bugs in 30 days", who="Agents; PMs give instructions", artifact="Bug and design-quality feedback 'back through the loop'", presence="agent",
    handoffs=[("release", "unk", "deploy and rollout not described in any source", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")])])
C["ramp"]["release"] = dict(
    agents="Deploy not described. Gadget writes help-center articles, blog posts, customer emails, updates the roadmap; a Glass prompt emails customers when their request ships (5,000+)", who="PMs; Gadget", artifact="Launch content; roadmap and status updates", presence="agent",
    handoffs=[("launch content and the record", "doc", "Gadget reads Notion, Linear, Slack and tickets", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles"), ("x-eglyman-introducing-glass-learn-things-once", "Glyman")]),
              ("operate", "unk", "no row in the map", [])])
C["ramp"]["operate"] = dict(
    agents="OCA (575 of 1,220 fix PRs assisted in four weeks); small-loop agents (feedback → backlog → code → KB); Glass issue channel triaged to tickets; Ramp Research in alert channels", who="On-call engineers, support, ops; agents for small loops", artifact="Incident reports, fix PRs, tickets, knowledge-base updates", presence="agent",
    handoffs=[("write code (OCA → Inspect → human merge)", "doc", "OCA reports at ~5 and ~13 minutes, asks Inspect for a PR; nothing merges without a human", [("ramp-builders-how-we-built-oca", "OCA post")]),
              ("small loops to code and KB", "doc", "sequence documented; each link's mechanism unknown; '60% of UX issues ... fixed within 24 hours'", [("lenny-podcast-geoff-charles-product-when-coding-solved", "Charles")]),
              ("every Glass session; everyone (Dojo)", "doc", "24-hour memory pipeline; publishing a skill is a reviewed Git change (323 people, 6,500+ edits)", [("x-sebgoddijn-glass-article", "Goddijn")])])

# ---- Shopify
C["shopify"]["spot"] = dict(
    agents="No agent for River. A Roast workflow aggregates competitive intelligence from the web and CRM conversations (2025)", who="Tobi sets ~6 yearly themes from the merchant's view; leaders", artifact="Yearly themes; aggregated intel (form not described)", presence="tool",
    handoffs=[("set goal", "doc", "themes → team objectives → six-month roadmap (2023, no agent)", [("lenny-how-shopify-builds-product", "Lenny (2023)")]),
              ("research / goal (Roast intel)", "inf", "where the output goes isn't stated", [("shopify-engineering-introducing-roast", "Roast")])])
C["shopify"]["talk"] = dict(
    agents="None named", who="Not described in any source", artifact="Not described", presence="none",
    handoffs=[("research", "unk", "not described in any source", [])])
C["shopify"]["research"] = dict(
    agents="River: reads code, the data warehouse, production traces, the PM system; 'go research papers on this topic'", who="Anyone (7,000+ people), in public channels", artifact="Public, searchable Slack thread with River's findings", presence="agent",
    handoffs=[("shape intent (same thread)", "doc", "ask River to summarise, create a ticket, make a diagram or a prototype", [("fs-knowledge-project-tobi-lutke-ai-agents", "Knowledge Project")]),
              ("write code (same thread)", "doc", "River 'usually offers to go fix it'; proposes a PR", [("x-tobi-river-replies-may-2026", "Tobi replies")]),
              ("the next person's research", "doc", "'starts from this thread'; channel and per-person memory; reuse rate unmeasured", [("shopify-engineering-under-the-river", "Under the River")])])
C["shopify"]["goal"] = dict(
    agents="None named", who="Teams turn themes into objectives; six-month roadmap; GSD Proposal reviewed by directors (OK1) and leadership (OK2)", artifact="Team objectives; GSD proposal, often with a short PM video", presence="tool",
    handoffs=[("shape intent (GSD Prototype gate)", "doc", "process (2023/2025), no agent link; Prototype phase 'dominated by AI exploration'", [("lenny-how-shopify-builds-product", "Lenny (2023)"), ("x-tobi-reflexive-ai-usage-memo", "memo")]),
              ("River thread (GSD ↔ thread)", "unk", "River can read the PM system; whether threads link to GSD records is not described", [("venturebeat-beyond-the-pilot-farhan-thawar", "Thawar")])])
C["shopify"]["intent"] = dict(
    agents="River in the thread (ticket, diagram, prototype); Quick sites (50,000+); Remote Dev Live Preview; 'intent documents' in World", who="PMs, designers, engineers, anyone; GSD Prototype phase", artifact="Ticket; diagram; Quick site URL; GSD prototype; intent docs", presence="agent",
    handoffs=[("plan / write code (same thread)", "doc", "River proposes a PR in the thread", [("x-tobi-river-replies-may-2026", "Tobi replies")]),
              ("write code (Quick prototype → PR in World)", "unk", "Quick sites are separate from World; anything reaching merchants needs a human engineer", [("shopify-engineering-quick", "Quick"), ("venturebeat-beyond-the-pilot-farhan-thawar", "Thawar")]),
              ("plan / code (intent documents)", "inf", "River works against intent documents in World; who writes them isn't stated", [("shopify-engineering-under-the-river", "Under the River")])])
C["shopify"]["plan"] = dict(
    agents="River 'occasionally pushes back on a plan it thinks is bad'; Helix checkpoints (migration); Dispatch partitions (security scans)", who="Engineers and others in the thread", artifact="The thread; Helix checkpoints; Dispatch partition files; no standalone plan artifact for River work", presence="agent",
    handoffs=[("write code", "doc", "same thread, same agent", [("shopify-engineering-under-the-river", "Under the River"), ("shopify-engineering-agentic-harness-outlasts-model", "Dispatch")])])
C["shopify"]["code"] = dict(
    agents="River (~1 in 8 merged PRs coauthored, May 2026; 3,536 in 30 days; 6%→61% of mobile PRs); Remote Dev Macs; Dispatch fix-author agents; Roast/Boba; local Claude Code, Cursor", who="Anyone from Slack; overnight automated workflows", artifact="Pull request in World, coauthored by River", presence="agent",
    handoffs=[("review", "doc", "River-coauthored PR 'reviewed by us'; a PR-review profile woken by an external system; Live Preview and recordings for non-engineers", [("x-tobi-learning-on-the-shop-floor", "Tobi article"), ("shopify-engineering-remote-dev", "Remote Dev")])])
C["shopify"]["review"] = dict(
    agents="PR-review profile on Aquifer; Remote Dev before/after recordings and explainer videos; Helix gates", who="A human reviewer on every PR, 'now becoming a big bottleneck'", artifact="Approved PR; recordings", presence="agent",
    handoffs=[("release", "doc", "merge queue; freshness-gated queue for security merges", [("shopify-engineering-under-the-river", "Under the River"), ("shopify-engineering-river-vulnerability-remediation", "vuln remediation")])])
C["shopify"]["test"] = dict(na="Not split out")
C["shopify"]["release"] = dict(
    agents="Merge queue ('load-bearing'); deploy or canary mechanics not described", who="Automated; GSD Release phase", artifact="Merged change on World's head", presence="tool",
    handoffs=[("operate", "unk", "no row in the map", [])])
C["shopify"]["operate"] = dict(
    agents="River: production traces (log line → commit), security remediation from a ledger, crash triage; Roast SRE scans. Learning loop: nightly 'dreaming', corpus mining, the Jev classifier", who="Engineers, security, SRE, code owners; GSD Results phase", artifact="Verified fixes; updated skills, memory and AGENTS.md", presence="agent",
    handoffs=[("write code (finding → PR → owner → verify)", "doc", "one thread per finding; 'the smallest question'; verified at head after merge", [("shopify-engineering-river-vulnerability-remediation", "vuln remediation")]),
              ("research (production signal)", "doc", "from a log line in production back to the commit", [("shopify-engineering-under-the-river", "Under the River")]),
              ("every task's context (learn loop)", "doc", "dreaming rewrites skills; sessions leave skill and AGENTS.md diffs in World", [("fs-knowledge-project-tobi-lutke-ai-agents", "Knowledge Project"), ("shopify-engineering-remote-dev", "Remote Dev")])])

# ---- Anthropic
C["anthropic"]["spot"] = dict(
    agents="Claude as strategy critic ('roast me', research mode); revisiting features with each model", who="A tech lead with a 3–6 month view; PMs; anyone noticing latent demand", artifact="Not described as an artifact; themes, prototypes", presence="tool",
    handoffs=[("shape intent", "inf", "latent demand noticed by people; side-quest sprints; no tool or artifact shown", [("lenny-podcast-cat-wu-anthropic-product-team", "Wu"), ("lenny-podcast-fiona-fung-after-coding-solved", "Fung")])])
C["anthropic"]["talk"] = dict(
    agents="Reading consented trajectories; Claude Tag consolidating feature requests from sales channels (≈24 accounts in ≈26 min)", who="PMs, including tenured hires; engineers via dogfooding", artifact="Classified failure descriptions; consolidated request lists", presence="agent",
    handoffs=[("research (failure classes)", "doc", "each failure classified, which routes it to a team", [("lenny-podcast-dianne-penn-evals-prds", "Penn"), ("claude-how-anthropic-uses-claude-tag", "Tag")])])
C["anthropic"]["research"] = dict(
    agents="Analytics skills over a governed semantic layer (95% of business queries automated, Anthropic's figure); Claude Tag for ad-hoc data; a PM's adoption-analytics agent; automated morning feedback summary; a proactive loop on a feedback channel", who="PMs, analysts, anyone (self-service)", artifact="Answers with provenance; readouts; summaries; triaged issues", presence="agent",
    handoffs=[("shape intent (eval)", "doc", "'the failure description becomes an eval' in a shared eval repository", [("lenny-podcast-dianne-penn-evals-prds", "Penn")]),
              ("shape intent (Cowork PRD)", "doc", "stacked plugins (usage data, customer quotes, PRD framework) draft the PRD in one session", [("claude-guide-deploying-cowork-across-org", "Cowork guide")]),
              ("set goal", "inf", "weekly metrics readouts; whether agents produce them is not stated", [("lenny-podcast-cat-wu-anthropic-product-team", "Wu")]),
              ("plan (another person's plan mode)", "unk", "not described; across people the inferred carriers are public channels, prototypes and explainers", [("claude-building-effective-human-agent-teams", "human-agent teams")])])
C["anthropic"]["goal"] = dict(
    agents="No goal-setting tool shown; weekly metrics readouts (agent-produced: inferred)", who="People: humans 'always set the north star'; PM plus team principles; monthly JIT planning on a short sheet", artifact="Written team principles; JIT planning sheet", presence="none",
    handoffs=[("shape intent", "inf", "six-monthly themes and a monthly sheet; people choose; no artifact link shown", [("claude-building-effective-human-agent-teams", "human-agent teams"), ("lenny-podcast-fiona-fung-after-coding-solved", "Fung")])])
C["anthropic"]["intent"] = dict(
    agents="Claude Code prototypes; Claude Design; Cowork PRD drafts; HTML specs; evals (30–40 cases) as 'test-driven development for PMs'; PRDs for big cross-functional alignment; Opus project security review on design docs", who="PMs, designers, engineers; anyone with a 'side quest'", artifact="Working prototype for internal users; design artifact; eval set; PRD (sometimes); PSR risk rating", presence="agent",
    handoffs=[("plan / write code", "doc", "'send [the spec] to Claude Code and see if it can build it'; prototypes go to internal users, then become the build", [("claude-pm-on-the-ai-exponential", "PM on the AI exponential"), ("claude-design-designer-workflow", "Claude Design")]),
              ("plan (security check)", "doc", "PSR reads design docs against an org-wide index; low-risk projects self-approve", [("claude-securing-ai-native-sdlc-at-anthropic", "securing the SDLC")]),
              ("intent.md → spec.md → plan.md", "unk", "prescribed by the playbook for customers; no Anthropic team shown using it", [("claude-ai-native-sdlc-playbook", "playbook")])])
C["anthropic"]["plan"] = dict(
    agents="Claude Code plan mode (Cherny starts ~80% of tasks there); interview-style unknowns pass; PSR at Plan", who="The engineer or PM who will build it; low-risk projects self-approve", artifact="A plan inside the session (plan.md as a committed file is the playbook's prescription, not shown internally)", presence="agent",
    handoffs=[("write code", "doc", "plan mode tells the model not to write code yet; then auto-accept edits once the plan is right", [("lenny-podcast-boris-cherny-after-coding", "Cherny")])])
C["anthropic"]["code"] = dict(
    agents="Claude Code (parallel sessions, worktrees, auto mode); an internal Claude Tag that merges more than half of code; Claude writes ~80% of merged code company-wide, ~90% of Claude Code's own", who="Agents directed by engineers, PMs and others; often started from a Slack thread", artifact="Branch and PR", presence="agent",
    handoffs=[("review", "doc", "self-verification, a fresh-context subagent, AI review against stated intent, blocking security review, CI, risk classifier", [("claude-dev-claude-code-team-code-review", "code review post")]),
              ("from any Slack thread", "doc", "a change can start from a Claude session in Slack; humans 'directing, setting intent, and owning final approval'", [("claude-securing-ai-native-sdlc-at-anthropic", "securing the SDLC")])])
C["anthropic"]["review"] = dict(
    agents="Self-verification; fresh-context subagent; Code Review agents with voting; blocking security review; CI; risk-tier classifiers; Antique (internal review surface)", who="Agents first; people by risk tier (none, one, two); the person who directed the agent counts as a reviewer", artifact="Approved PR with resolved findings", presence="agent",
    handoffs=[("release", "doc", "merge queue or post-merge testing; flags to employees first; latest then stable", [("claude-dev-claude-code-team-code-review", "code review post"), ("anthropic-redesigning-source-control-scion", "Scion")]),
              ("shape intent (change direction)", "doc", "in the channel thread someone asks why or cites an earlier decision; the author closes or reshapes the PR", [("claude-dev-claude-code-team-code-review", "code review post")])])
C["anthropic"]["test"] = dict(na="Not split out; CI and the fresh-context subagent sit inside review")
C["anthropic"]["release"] = dict(
    agents="Merge queue (Claude Code repos) or post-merge and pre-deploy testing (monorepo, Scion); feature flags to employees first; latest then stable; evergreen launch room", who="Automated; launch comms by PMM and DevRel the next day", artifact="Live change behind a flag; announcement", presence="tool",
    handoffs=[("operate", "doc", "weekly on-call; component superfans; Claude Tag CI first responder; dashboards", [("claude-tag-ci-cd-first-responder", "CI on-call"), ("anthropic-redesigning-source-control-scion", "Scion")])])
C["anthropic"]["operate"] = dict(
    agents="Claude Tag CI first responder (lessons.md promoted to skills); per-component 'superfan' agents; an alert agent that root-causes and writes the fix but cannot deploy; incidents become reviewer evals", who="Weekly on-call; CI team; security engineers 'monitoring loops'", artifact="Post-mortem, fix PR, lessons log, new evals, CLAUDE.md edits", presence="agent",
    handoffs=[("write code", "doc", "the alert agent's fix goes through review; it cannot deploy", [("claude-securing-ai-native-sdlc-at-anthropic", "securing the SDLC")]),
              ("shared knowledge", "doc", "lessons.md read first and promoted into skills; repeat findings go into CLAUDE.md, REVIEW.md or lint", [("claude-tag-ci-cd-first-responder", "CI on-call"), ("claude-dev-claude-code-team-code-review", "code review post")]),
              ("research (feedback consolidation)", "doc", "Tag consolidates weekly issues; a morning summary runs automatically; an hourly proactive loop", [("claude-how-anthropic-uses-claude-tag", "Tag"), ("claude-loop-engineering", "loops")])])

# ---- Atlassian
C["atlassian"]["spot"] = dict(
    agents="JPD ideas with custom types (user problem, bet, opportunity, solution) and attached insights; Loom AI turns a recording into a bug report", who="No internal account; JPD is the product for it", artifact="JPD idea; Jira bug work item", presence="tool",
    handoffs=[("delivery work item", "doc", "delivery link from the idea; optional 'embed the idea description and fields into the work item'", [("atlassian-jpd-link-idea-to-work-item", "JPD link")]),
              ("coding agent (embedded copy)", "inf", "the agent reads the work item description, so an embedded copy reaches it; no agent shown following the idea link", [("atlassian-jira-coding-agent-generate-code", "coding agent")]),
              ("set goal", "unk", "a 'Goals' field on ideas is reported; whether it is the Goals object is unverified", [])])
C["atlassian"]["talk"] = dict(
    agents="Loom meetings connected to a Jira space: Rovo suggests updates to existing work items. Internal: a Rovo agent triaged 900+ customer-insight items", who="Internal: the Jira team ran user studies; PMs steered", artifact="Suggested status, priority, comment or description changes; triaged insight list", presence="agent",
    handoffs=[("existing work items", "doc", "the owner accepts or discards each suggestion", [("atlassian-loom-record-for-agent", "Loom")]),
              ("engineering (triaged insight)", "unk", "'then we knew what to send to engineering'; how it was sent is not said", [("lenny-podcast-tamar-yehoshua-roles-expanding", "Yehoshua talk")])])
C["atlassian"]["research"] = dict(
    agents="Rovo Chat; Rovo Deep Research (plans, retrieves from Teamwork Graph, writes a cited report)", who="Internal: anyone, up to the CEO, who asked Rovo for a launch date instead of the PM; PMs 'not compiling research by hand'", artifact="Cited report in Rovo Chat; Confluence export claimed only", presence="agent",
    handoffs=[("shape intent / plan", "unk", "report stays in Rovo Chat; no source has Planner, JPD or a PRD consuming it", [("atlassian-rovo-deep-research", "Deep Research")]),
              ("Confluence page", "doc", "'effortlessly exported' in a 2025 engineering blog only; not in the support doc (vendor claim)", [("atlassian-rovo-deep-research", "Deep Research")])])
C["atlassian"]["goal"] = dict(
    agents="Atlassian Goals (Home): owner, date, status, monthly update, OKR scoring; Delivery Agent can read goal context", who="People: 'people decide what and why'", artifact="Goal linked to sub-goals, projects, epics, work items", presence="tool",
    handoffs=[("work items", "doc", "Goals field; Teamwork Graph edge work item → goal; Delivery Agent reads goal context", [("atlassian-goals-what-is-a-goal", "Goals"), ("atlassian-rovo-jira-delivery-agent", "Delivery Agent")]),
              ("JPD idea", "unk", "unverified", [])])
C["atlassian"]["intent"] = dict(
    agents="Loom Record for agent (narration → action plan → work items 'for agents to act on'); coding agents for prototypes; Figma MCP; Confluence PRD templates; Jira Planner (Early Access)", who="Internal: PMs and designers prototype; a Confluence PM fixed UX in code (26 PRs in a month); Rovoclaw's PM and designer built the alpha", artifact="Loom action plan; work items; prototype code in the real front-end repo; Confluence PRD or Live Doc spec", presence="agent",
    handoffs=[("work items", "doc", "Record for agent → action plan → 'Create in Jira'", [("atlassian-loom-record-for-agent", "Loom"), ("lenny-podcast-tamar-yehoshua-roles-expanding", "Yehoshua talk")]),
              ("prototype by coding agent", "doc", "internal: moving the item to In Progress 'automatically kicks off a coding agent' in the front-end repo", [("lenny-podcast-tamar-yehoshua-roles-expanding", "Yehoshua talk"), ("atlassian-jira-agentic-engineering-guide", "guide")]),
              ("developers (prototype)", "doc", "'the handoff to developers was much faster' (speaker); how they took it over is not described", [("lenny-podcast-tamar-yehoshua-roles-expanding", "Yehoshua talk")]),
              ("plan (Jira Planner)", "doc", "idea → clarifying questions → Live Doc spec → sequenced work items with acceptance criteria (vendor claim, Early Access)", [("atlassian-blog-introducing-jira-planner", "Planner")])])
C["atlassian"]["plan"] = dict(
    agents="Jira Planner: sequenced work items with dependencies, milestones, acceptance criteria (claimed); Coding Agent's plan step claimed in a blog, not in the support doc", who="Claimed audience: tech leads, senior engineers, EMs, PMs. Internal: an engineer had Rovo Dev write 'plans and options on subtasks'", artifact="Work items with acceptance criteria; Live Doc spec", presence="agent",
    handoffs=[("write code (any assigned agent)", "doc", "assign, @mention or automation rule; Claude, Cursor, Copilot, Codex or the Jira Coding Agent", [("atlassian-jira-coding-agent-generate-code", "coding agent"), ("atlassian-jira-manage-agents-in-space", "agents in a space")]),
              ("from JPD idea, goal or research page", "inf", "Planner 'pulls in context from Teamwork Graph'; no source says it reads them", [("atlassian-blog-jira-ai-native-software-development", "launch post")]),
              ("Confluence spec → coding agent", "doc", "interactive: reads Confluence as the user; automation: restricted mode, no Confluence; default reading of linked pages unknown", [("atlassian-jira-coding-agent-generate-code", "coding agent")])])
C["atlassian"]["code"] = dict(
    agents="Jira Coding Agent (Rovo Dev); Claude Agent for Jira, Cursor, GitHub Copilot, Codex assignable from the same work item; Rovo Dev CLI; deep link to local tools", who="Engineers (internal: 'probably 95% or more of my dev work'); PMs on Confluence, not on Jira", artifact="Branch and draft PR, the user as author; agent session listed on the work item", presence="agent",
    handoffs=[("review", "doc", "work item key in the branch name links PR to item; Rovo Dev checks against acceptance criteria", [("atlassian-rovo-dev-acceptance-criteria-code-review", "AC review")])])
C["atlassian"]["review"] = dict(
    agents="Rovo Dev code reviewer in Bitbucket and GitHub; checks the PR against the work item's acceptance criteria", who="A person reviews the draft PR, plus an agent", artifact="Review comments; acceptance-criteria check", presence="agent",
    handoffs=[("release (Pipelines)", "doc", "summaries 'from commits, Jira work items, and other deployment data' (beta)", [("atlassian-rovo-dev-bitbucket-pipelines", "Pipelines")]),
              ("back to the coding agent", "doc", "documented as a gap: not automatic yet; the engineer returns to the Jira session", [("atlassian-blog-rovo-dev-in-jira", "Rovo Dev in Jira")])])
C["atlassian"]["test"] = dict(na="Not split out")
C["atlassian"]["release"] = dict(
    agents="Rovo Dev in Bitbucket Pipelines (beta): deployment summaries, failed-build explanations; release-notes drafter agent", who="Not shown", artifact="Deployment summary; release notes", presence="agent",
    handoffs=[("operate", "unk", "no row in the map; Pipelines summaries' destination not stated", [])])
C["atlassian"]["operate"] = dict(
    agents="Ops Expert (alerts, similar incidents, /create-pir); Delivery Agent (space health, stakeholder status); a Jira agent in Slack triaging internal feedback to a coding agent", who="Incident responders; internal: a PM's own weekly-update agent; the CEO self-serving status", artifact="Post-incident review as a work item or page; PIR action items as work items; status reports", presence="agent",
    handoffs=[("backlog (PIR action items)", "doc", "'Create Jira tickets for action items in this PIR'", [("atlassian-rovo-ops-expert-agent", "Ops Expert")]),
              ("write code (alert + bug)", "doc", "automation starts a coding agent fed telemetry over the Teamwork Graph MCP (vendor claim); internal: Slack feedback sent to the coding agent (speaker)", [("atlassian-rovo-ops-expert-agent", "Ops Expert"), ("lenny-podcast-tamar-yehoshua-roles-expanding", "Yehoshua talk")]),
              ("the next spec", "unk", "'results feed back into the next spec'; no mechanism", [("atlassian-jira-agentic-engineering-guide", "guide")])])

# ---- Intercom
C["intercom"]["spot"] = dict(
    agents="None named", who="Leadership, top-down: the CEO narrowed the company to customer service and bet on AI", artifact="Not described", presence="none",
    handoffs=[("set goal", "unk", "not described", [("lenny-podcast-mccabe-intercom-ai-bet", "McCabe")])])
C["intercom"]["talk"] = dict(
    agents="AI-moderated interviews for churn studies, pilots and well-defined topics (tool not named); early discovery stays human", who="Research and data science (RAD) researchers", artifact="Interview transcripts; a 60+ interview study turned into a queryable skill", presence="agent",
    handoffs=[("research", "doc", "studies become a searchable repository with a queryable skill; existing evidence synthesised first", [("ideas-fin-nobody-changed-their-title", "Church"), ("ideas-fin-talk-to-the-bot-ai-interviewer", "Bridi")])])
C["intercom"]["research"] = dict(
    agents="Claude Code with Claude4Data (30+ analytics skills) and company-metric guidance skills; Cockpit (LLM clustering of feedback); sources: sales calls, win/loss, churn surveys, Salesforce, Slack", who="Researchers, data scientists, PMs, sales reps", artifact="HTML reports; Snowflake/Streamlit reports with access control; daily win/loss feed; fortnightly leadership deal briefing", presence="agent",
    handoffs=[("shape intent", "unk", "not described; no source says how findings reach designers, PMs or engineers", [("ideas-fin-nobody-changed-their-title", "Church")]),
              ("set goal", "unk", "not described", [])])
C["intercom"]["goal"] = dict(
    agents="None named", who="Not described (the CTO names company measures: release throughput, idea-to-release time)", artifact="Not described", presence="none",
    handoffs=[("shape intent", "inf", "people; no tool shown", [("ideas-fin-webinar-qa-3x-rd-output", "webinar Q&A")])])
C["intercom"]["intent"] = dict(
    agents="Claude Code prototypes on production components and live data; Surge design system and playground; 'vibe' prototypes, then structured specs for edge cases; Figma as whiteboard", who="Designers (primarily in code), PMs; work 'closer to customers'", artifact="Prototypes (the 'new wireframe'); 'tighter briefs'; no PRD or brief template found", presence="agent",
    handoffs=[("plan / build", "doc", "prototypes convey intent, interaction and tone; 'tighter briefs at the start, fast review cycles, and clear criteria' replace fixed handoffs", [("ideas-fin-to-vibe-code-or-not", "Mahar"), ("ideas-fin-how-we-design-when-code-writes-itself", "Moriarty")]),
              ("write code (designer or PM codes it)", "inf", "the same person uses Claude Code; no ticket or spec hop described", [("ideas-fin-how-we-design-when-code-writes-itself", "Moriarty"), ("ideas-fin-webinar-qa-3x-rd-output", "webinar Q&A")])])
C["intercom"]["plan"] = dict(
    agents="Claude Code plan mode: 5–20 turns before building", who="Engineers, who 'take responsibility for the shape of the solution'", artifact="A plan held in the session; not persisted", presence="agent",
    handoffs=[("write code", "doc", "same Claude Code session; the plan stays in session memory (anecdote)", [("ideas-fin-what-were-learning-from-engineers", "Walker")])])
C["intercom"]["code"] = dict(
    agents="Claude Code (13 plugins, 267 skills from 153 contributors, MDM-installed); cloud agents a small share; ~93–94% of PRs agent-driven", who="Engineers; also designers, PMs and TPMs", artifact="Pull request whose description states why (create-pr skill, hook-enforced)", presence="agent",
    handoffs=[("review", "doc", "hook-enforced create-pr writes why; a GitHub webhook triggers the Shrek reviewers; a background agent watches CI", [("ideas-fin-how-we-use-claude-code-today", "Scanlan"), ("intercom-ai-approving-pull-requests", "AI approving PRs")]),
              ("from the design system", "doc", "skills encode Surge/React standards; component reuse 7% → 96%", [("ideas-fin-eight-people-hold-the-bar", "de Róiste")])])
C["intercom"]["review"] = dict(
    agents="'Shrek': specialised review sub-agents (Claude and Codex) in short-lived containers, triggered by GitHub webhooks, with their own evals; ~19% of PRs auto-approved by risk and size; QA sessions turned into GitHub issues", who="A person on about 80% of PRs; repo owners set review requirements", artifact="Approved, labelled and logged PR; GitHub issues from QA", presence="agent",
    handoffs=[("release", "doc", "auto- or human-approved merge triggers automatic deploy; non-approved PRs go to a person with a Slack notice", [("intercom-ai-approving-pull-requests", "AI approving PRs"), ("ideas-fin-webinar-qa-3x-rd-output", "webinar Q&A")])])
C["intercom"]["test"] = dict(na="Not split out; QA sessions sit under review, Fin's replayed-conversation tests under release")
C["intercom"]["release"] = dict(
    agents="Automatic deploys (313 in a day; merge to production ~12 min). Fin's own changes: replayed-conversation tests with AI judges, A/B tests, staged rollout. Operator turns a 'what we built' doc into gap analysis, draft articles and FAQ tests", who="The shipping engineer owns monitoring and rollback; an NPI manager owns support readiness", artifact="Live change; for launches, updated and tested support content and sign-off", presence="agent",
    handoffs=[("support knowledge (Fin)", "doc", "PMs and engineers submit a 'what we built' doc to the release tracker; the NPI manager signs off", [("intercom-fin-npi-agent-readiness", "Fin NPI")]),
              ("operate", "unk", "no row in the map (launch monitors for 2–4 weeks appear in the task row)", [("intercom-fin-npi-agent-readiness", "Fin NPI")])])
C["intercom"]["operate"] = dict(
    agents="Read-only production console over MCP; incident skill (Honeycomb, Datadog, Snowflake logs); launch monitors for 2–4 weeks; SessionEnd hook mines transcripts for missing skills; weekly CLAUDE.md fact-check", who="Engineers; support engineers, design managers and PM leaders among top console users", artifact="Answers; GitHub issues for new skills; updated CLAUDE.md; post-launch support metrics", presence="agent",
    handoffs=[("harness learning", "doc", "SessionEnd → Haiku classifies gaps → Slack post with a pre-filled GitHub issue → new skills; promoted to the base plugin at 50 weekly users", [("ideas-fin-how-we-use-claude-code-today", "Scanlan"), ("ideas-fin-webinar-qa-3x-rd-output", "webinar Q&A")]),
              ("own research and roadmap (Fin data)", "unk", "Fin Insights is documented only as a customer product", [("ideas-fin-working-with-a-black-box-fin-insights", "Fin Insights")])])

# ---- Airbnb
C["airbnb"]["spot"] = dict(
    agents="None named. Inputs: 20M support calls, social posts, Minerva metrics; Insight Miner taxonomies", who="The CEO and the top 30–70 leaders; product marketing; the business (CBO) organisation", artifact="One rolling two-year roadmap ('If it's not on the roadmap, it can't ship'); the 'Airbnb Blueprint' storyboard and prioritised fix map", presence="tool",
    handoffs=[("roadmap (with set goal)", "doc", "everything shipped must be on the one roadmap; the CEO adds and cuts items", [("figma-config-2023-brian-chesky", "Config 2023"), ("lenny-podcast-brian-chesky-new-playbook", "Lenny's Podcast")])])
C["airbnb"]["talk"] = dict(
    agents="No agent seen", who="Researchers, designers; the CEO ('talk to normal people we don't pay'); leaders embedded in Paris for experiences", artifact="Findings (format not described); ~500 seed queries for AI search", presence="none",
    handoffs=[("shape intent (AI search)", "doc", "~500 seed queries from user research ground the synthetic training queries", [("airbnb-tech-castle-nl-search", "CASTLE")]),
              ("research (product work)", "inf", "people; no tool shown", [])])
C["airbnb"]["research"] = dict(
    agents="Insight Miner: a chat agent wrapped in a shared method package, used by dozens of teams; Datako for data questions; Minerva (12,000+ certified metrics); ERF experiments", who="Data science, product-insights and operations teams; more non-technical users than technical", artifact="Taxonomies, prevalence estimates, datasets; Knowledge Repo posts (2016–21)", presence="agent",
    handoffs=[("shape intent (AI support)", "doc", "taxonomy and prevalence of support situations turned into datasets and evals before launch", [("airbnb-tech-insight-miner-agent-harness", "Insight Miner")]),
              ("shape intent (Pascal brief)", "doc", "Pascal drafts a concept brief from market research, the roadmap and business objectives; whether it cites sources is not described (mechanism unknown)", [("dx-airbnb-beyond-the-cli-airchat", "DX talk")]),
              ("plan (research evidence)", "unk", "nothing found carries research evidence into the brief, the Jira tickets or the plan", [])])
C["airbnb"]["goal"] = dict(
    agents="None named", who="The CEO with the CFO and business lead; mission teams with one mandate ('Project Hawaii'); for AI features, an eval decision-maker", artifact="Roadmap entry; revenue targets; eval goals and gates set up front", presence="none",
    handoffs=[("shape intent (goals and gates)", "doc", "for AI features a decision-maker fixes goals and eval gates up front; PMs label golden sets", [("airbnb-tech-eval-driven-development", "eval-driven development")]),
              ("shape intent (business brief)", "doc", "a product marketer pairs with a business counterpart; the business model and the 'product marketing brief' go to supply and international teams", [("verge-decoder-chesky-founder-mode-2024", "Decoder 2024")])])
C["airbnb"]["intent"] = dict(
    agents="Pascal drafts the concept brief; a designer prototyping tool; the CTO feeds image-model mockups to coding agents; @generateMock fills prototypes with realistic data from the design URL", who="Product marketer, designer and CEO; PMs and designers in smaller pods", artifact="Story or press release; short concept brief; 5–10 high-fidelity prototypes; PM-labelled golden sets", presence="agent",
    handoffs=[("plan", "unk", "the gap is documented: prototypes replace long specs, the brief isn't updated after prototyping, reviews go out of order; an AI coordinator is only proposed", [("dx-airbnb-beyond-the-cli-airchat", "DX talk")]),
              ("write code", "doc", "a prototype's design URL goes into the mock generator; the CTO feeds image-model mockups to coding agents", [("airbnb-tech-graphql-generatemock", "@generateMock"), ("deepview-al-dahle-airbnb", "Deep View")])])
C["airbnb"]["plan"] = dict(
    agents="A proposed 'AI project coordinator' (not built); Everest gives cross-codebase context so generalists can plan in specialist areas", who="Program managers (timelines, coordination); smaller pods", artifact="Central project list with a review schedule; Jira; release calendar", presence="tool",
    handoffs=[("review (CEO cadence)", "doc", "fixed cadence of CEO reviews with green/yellow/red scoring by the head program manager", [("lenny-podcast-brian-chesky-new-playbook", "Lenny's Podcast")])])
C["airbnb"]["code"] = dict(
    agents="AirChat: Airbnb's internal harness; the CLI wraps Claude Code and Codex behind one gateway, with default MCPs, a plugin and skill marketplace, an SDK with ~40 apps, and AirChat Remote for async runs; a migration framework (validate, transform, validate)", who="Engineers, plus managers and non-engineers", artifact="Pull requests; '60% of code' AI-written or co-authored (definitions vary)", presence="agent",
    handoffs=[("review", "doc", "validation loops before a PR; one model critiques another; a person must be able to explain the PR", [("airbnb-tech-llm-test-migration", "test migration"), ("latent-space-airbnb-al-dahle-inside-out-ai", "Latent Space"), ("deepview-al-dahle-airbnb", "Deep View")])])
C["airbnb"]["review"] = dict(
    agents="Validation loops (tests, lint, types, schema checks); one model generates and another critiques; experiment guardrails escalate ~25 experiments a month (2021)", who="The CEO, on a 1–12 week cadence; design reviews must discuss impact; engineers must be able to explain AI-written PRs", artifact="Review decisions (not recorded); approved PRs", presence="agent",
    handoffs=[("release", "doc", "staged traffic slices and toggles; canary with auto-rollback for model patches; guardrails measured in shadow mode first", [("airbnb-earnings-q2-2026", "Q2 2026 letter"), ("airbnb-tech-llm-eval-weeks-to-a-day", "eval speed"), ("qconsf-2026-airbnb-guardrails-support-agent", "QCon SF")]),
              ("later work (review decisions)", "inf", "not written down; held in leaders' heads ('shared consciousness')", [("verge-decoder-chesky-founder-mode-2024", "Decoder 2024")])])
C["airbnb"]["test"] = dict(na="Not split out; validation loops sit inside review")
C["airbnb"]["release"] = dict(
    agents="Small traffic slices, opt-in toggles, staged rollout by language, canary with auto-rollback for model patches", who="Product marketing and comms run launches; the CEO keynote", artifact="Two releases a year until 2025; from 2026 'we ship the moment it's ready', with May as a showcase", presence="tool",
    handoffs=[("operate", "unk", "no row in the map", [])])
C["airbnb"]["operate"] = dict(
    agents="Production evals on 5% of traffic daily; Agent-in-the-Loop weekly retraining from support agents' choices; async on-call agents that triage alerts and propose PRs; the AI support agent (~45% of issues resolved without a human, Airbnb's figure)", who="Data science; PMs in a weekly eval review; human support agents", artifact="Dashboards, experiment results, new evals, retrained models", presence="agent",
    handoffs=[("evals", "doc", "production failures become new evals in a weekly PM review", [("airbnb-tech-eval-driven-development", "eval-driven development")]),
              ("model", "doc", "support agents' in-workflow choices feed weekly model updates", [("arxiv-airbnb-agent-in-the-loop", "Agent-in-the-Loop")]),
              ("next build (Everest)", "doc", "learnings said to cut a later project from 9 months to ~6 weeks; how they enter Everest is not described (mechanism unknown)", [("latent-space-airbnb-al-dahle-inside-out-ai", "Latent Space"), ("airbnb-earnings-q2-2026", "Q2 2026 letter")]),
              ("spot the opportunity (Blueprint)", "doc", "20M support calls, social posts and a storyboard of every screen and policy, combined into a prioritised fix map", [("figma-config-2023-brian-chesky", "Config 2023")])])

# ---- Spotify
C["spotify"]["spot"] = dict(
    agents="None named. Confidence is pitched as a 'product intelligence layer'; LLMs are proposed for screening weak ideas", who="VPs and their teams (bottom-up bets, e.g. the AI DJ from the personalisation team); insights teams", artifact="Bet pitch; DIBB data and insights (2016 form)", presence="none",
    handoffs=[("set goal, plan (VP bet)", "doc", "pitch, then a global stack rank by the co-CEOs, then top-down staffing (2025)", [("colossus-ilb-gustav-soderstrom-how-spotify-thinks", "Invest Like the Best")])])
C["spotify"]["talk"] = dict(
    agents="No agent found; diary studies and interviews", who="User researchers (Product Insights)", artifact="Research findings", presence="none",
    handoffs=[("research", "doc", "diary studies and behavioural logs on the same users at the same time (one team, 2019)", [("spotify-design-simultaneous-triangulation", "Simultaneous Triangulation")])])
C["spotify"]["research"] = dict(
    agents="Vedder: expert-curated context clusters; AiKA: internal knowledge Q&A since Dec 2023 (1,000+ daily users); the data assistant has 2,100+ users; behavioural proxies size qualitative findings", who="Data scientists with researchers, and PMs; more than a quarter of data-assistant users had never written SQL", artifact="Answers with SQL and sources; sized opportunity statements", presence="agent",
    handoffs=[("shape intent (tree, brief, Scorecard)", "doc", "Thoughtful Execution tree, then Understand It Brief, then Scorecard (2020–21); current use unknown", [("spotify-design-thoughtful-execution-framework", "Thoughtful Execution"), ("spotify-design-scorecards-alignment", "Scorecards")]),
              ("spot, set goal (DIBB brief)", "doc", "a two-page bet brief on an open bets board (2016); current form unknown", [("kniberg-spotify-rhythm", "Rhythm")]),
              ("bet and plan (research evidence)", "unk", "not described as an artifact; VPs carry it and must explain it themselves in the E-Team", [("colossus-ilb-gustav-soderstrom-how-spotify-thinks", "Invest Like the Best")])])
C["spotify"]["goal"] = dict(
    agents="An internal planning tool; the bets board", who="The co-CEOs (co-presidents until 2025) rank bets; VPs write area strategy; teams set measurable goals", artifact="Six-month stack rank of 30–50 bets; 'definitions of done'", presence="tool",
    handoffs=[("shape intent", "unk", "no row in the map", []),
              ("agent work, and back (bet → prompts, PRs, A/B tests)", "unk", "no link from a bet to the work that serves it; linking PRs to work items and user value is still being built", [("claude-customers-spotify-office-hours", "office hours")])])
C["spotify"]["intent"] = dict(
    agents="Cursor and Claude Code prototypes in the real apps, shared in an internal app store; offline LLM evals pick treatments before A/B tests", who="The product, design and engineering trio; everyone up to the co-CEOs prototypes", artifact="Thoughtful Execution tree, Understand It Brief and Scorecard (2020–21); prototypes; versioned migration prompts", presence="agent",
    handoffs=[("plan", "doc", "a prototyping phase before each cycle exposes conflicts between bets", [("colossus-ilb-gustav-soderstrom-how-spotify-thinks", "Invest Like the Best")]),
              ("write code", "doc", "PMs propose small changes through Honk from Slack; prototypes run in the real apps; prototype-to-ship conversion not reported; Figma specs named inconsistent in 2021", [("spotify-engineering-honk-part-1-1500-prs", "Honk part 1"), ("claude-customers-spotify-office-hours", "office hours"), ("spotify-design-productivity-blueprint", "Design Productivity Blueprint")]),
              ("A/B test → fix (evaluation funnel)", "doc", "evals pick treatments, experiments validate them, judge findings become fixes", [("spotify-engineering-llm-evals-funnel", "evaluation funnel")])])
C["spotify"]["plan"] = dict(
    agents="Fleetshift targeting (deterministic); Backstage lineage; code search", who="Co-CEOs and VPs (bets, staffing); migration and library owners; advisory boards of 5–6 senior engineers choose 'golden' technologies", artifact="Six-month plan; target lists; golden-tech standards; RFCs and ADRs", presence="tool",
    handoffs=[("write code (migrations)", "doc", "Backstage lineage → code search → Fleetshift scope → a context file with mapping tables → Honk", [("spotify-engineering-honk-part-4-dataset-migrations", "Honk part 4")])])
C["spotify"]["code"] = dict(
    agents="Honk: a Claude Agent SDK background agent started from Slack, GitHub or Jira (1,500+ merged PRs by Nov 2025); Claude Code; Xirp: multi-agent sessions on Claude Code, Gemini CLI and Codex", who="Engineers supervising agents; PMs for small changes", artifact="Pull requests. Figures disagree: 73% of PRs AI-authored (early 2026); PR frequency up 76% (Jun 2026)", presence="agent",
    handoffs=[("review", "doc", "verifiers in the stop hook, then a verification service runs real CI, and only then a PR goes to code owners", [("spotify-engineering-honk-part-3-feedback-loops", "Honk part 3"), ("infoq-qcon-spotify-ai-codebase-migration-agent", "QCon talk")]),
              ("from a thread, ticket or PR comment", "doc", "an interactive agent gathers task details, then hands a prompt to Honk", [("spotify-engineering-honk-part-1-1500-prs", "Honk part 1")]),
              ("catalog → session → catalog (Xirp)", "doc", "sessions start with catalog context; transcripts and metadata flow back to Portal", [("spotify-portal-blog-introducing-xirp", "Xirp")])])
C["spotify"]["review"] = dict(
    agents="Hidden verifiers in the stop hook; a verification service runs real CI before any PR exists; an LLM judge vetoed ~25% of sessions and was later dropped", who="Code owners; the migration driver, who sometimes approves their own PRs; Scorecard evaluators by role (2021)", artifact="Validated PR", presence="agent",
    handoffs=[("release", "doc", "auto-merge for safe fleet changes; after an auto-merged upgrade broke production, safeguards and owners'-hours scheduling were added", [("spotify-engineering-quality-at-higher-velocity", "Quality at Higher Velocity")])])
C["spotify"]["test"] = dict(na="Not split out; verifiers and the verification service sit inside review")
C["spotify"]["release"] = dict(
    agents="Auto-merge for safe fleet changes (2.5M+ merged fleet PRs); release trains, toggles and gradual rollout; builds pushed to phones from Slack", who="Owning teams", artifact="Merged change; app build", presence="tool",
    handoffs=[("learn", "doc", "Confidence's default ship rule; every experiment labelled ship, abort or iterate", [("spotify-engineering-risk-aware-product-decisions", "Risk-aware decisions"), ("spotify-engineering-experiments-with-learning", "Experiments with Learning")])])
C["spotify"]["operate"] = dict(
    agents="Confidence: a default ship rule and Experiments-with-Learning labels (~12% of tests win, ~64% yield learning); regression monitoring; monthly retros that tag AI's part", who="Experimenters; platform and SRE teams; data science", artifact="Shipping recommendation with reasons; ship, abort or iterate label; incident retros", presence="agent",
    handoffs=[("shared knowledge", "doc", "AiKA usage leads teams to improve their docs; fewer repeat questions", [("spotify-portal-blog-aika-data-plugins", "AiKA")]),
              ("next six-month plan", "inf", "learning rates reallocate testing bandwidth; whether results feed the next bets cycle is not described", [("spotify-engineering-experiments-with-learning", "Experiments with Learning")])])

# ---- Block
C["block"]["spot"] = dict(
    agents="None internal. Proposed: customer agents (Managerbot, Moneybot) and the intelligence layer's failures as roadmap signal", who="Leaders; DRIs; customers, through customer agents", artifact="A backlog of seller-requested features; 'failure signal' as roadmap (proposed)", presence="none",
    handoffs=[("write code (seller-request backlog → Builderbot)", "doc", "features sellers had waited months for shipped 'in days'; how the list was produced is not said (upstream link unknown)", [("block-builderbot-rollout", "Builderbot")]),
              ("from customer agents", "doc", "customers request automations before features ship, said to 'align with our roadmap'; mechanism unknown", [("block-q1-2026-shareholder-letter", "Q1 2026 letter"), ("block-from-hierarchy-to-intelligence", "essay")])])
C["block"]["talk"] = dict(
    agents="No tool named. Dorsey: conversational interfaces replace inferred research", who="PMs (the role still asks for customer research), designers", artifact="Not described", presence="none",
    handoffs=[("research or intent", "unk", "no tool or artifact described", [])])
C["block"]["research"] = dict(
    agents="goose with the Block Data MCP (1,100+ governed metrics) and Query Expert (2.1K monthly users); Snowflake, Looker, Tableau, Glean and Drive MCPs", who="Anyone: PMs, growth managers ('without waiting on an analyst'), sales, finance, risk, engineers", artifact="Analyses, reports, internal dashboards and apps (App Kit: 1,000+ apps)", presence="agent",
    handoffs=[("shape intent (prototype)", "inf", "likely the same person in the same or a later goose session; report → product prototype is not documented", [("lenny-podcast-block-dhanji-goose", "CTO"), ("block-eng-app-kit-localhost-to-launched", "App Kit")]),
              ("plan (Builderbot or an engineer), across people", "unk", "goose sessions are local; recipes and skills carry method, not findings; what crosses is a prototype, a PR, a thread or a ticket", [])])
C["block"]["goal"] = dict(
    agents="No tool shown. Proposed: a company 'markdown file' of values, metrics and non-goals", who="DRIs (own a customer problem, e.g. for 90 days); growth managers own goal and experiment backlog", artifact="Not described (the markdown file is proposed)", presence="none",
    handoffs=[("shape intent", "inf", "the DRI holds both; the company markdown file is proposed", [("block-from-hierarchy-to-intelligence", "essay"), ("a16z-owen-jennings-block-all-in-on-ai", "Jennings")])])
C["block"]["intent"] = dict(
    agents="goose, Claude Code, Cursor, V0, Figma Make; App Kit for internal apps. No PRD agent or recipe found", who="PMs, designers, engineers; DRIs decide", artifact="A prototype or demo ('Friday demos'), often a PR; prototypes replace decks and Google Docs", presence="agent",
    handoffs=[("decision (DRI, leaders)", "doc", "people bring a prototype they built instead of a deck or Google Doc; Friday demos", [("sequoia-dorsey-every-company-mini-agi", "Dorsey"), ("dive-club-cam-worboys-ai-native-design-org", "Worboys")]),
              ("write code (the same PM or designer)", "doc", "the same person ships the PR, via a sandbox-to-production programme with engineers pairing", [("dive-club-cam-worboys-ai-native-design-org", "Worboys"), ("a16z-owen-jennings-block-all-in-on-ai", "Jennings")])])
C["block"]["plan"] = dict(
    agents="Builderbot researches and plans from a ticket or thread; engineers use RPI (research, plan, implement) in separate sessions; goose's own repo uses 'Ready' issues", who="Engineers; teammates steer in the thread", artifact="Linear or Jira ticket; Slack thread; a 'Ready' issue with agreed design and verification", presence="agent",
    handoffs=[("write code (inside Builderbot; RPI)", "doc", "one agent researches, plans, branches and codes; RPI keeps the three steps in separate sessions", [("block-builderbot-rollout", "Builderbot"), ("block-eng-ai-assisted-development-at-block", "AI-assisted dev")]),
              ("from any Slack thread or ticket", "doc", "tag @builderbot with a short description, or it picks up the Linear or Jira ticket; teammates steer in the thread", [("block-builderbot-rollout", "Builderbot")])])
C["block"]["code"] = dict(
    agents="Builderbot (~1,500 merged PRs a week, ~15% of changes); seven harnesses ('We buy them all'); goose recipes such as Goose Janitor", who="Agents started by engineers; PMs and designers ship PRs", artifact="Branch and pull request", presence="agent",
    handoffs=[("review", "doc", "AI reviewed 90%+ of change requests; a human makes the final push", [("block-q1-2026-shareholder-letter", "Q1 2026 letter")])])
C["block"]["review"] = dict(
    agents="Builderbot reviewed 90%+ of change requests (Q1 2026); headless goose in CI drafts fixes", who="A person makes the final push on every change; staff say about 95% of AI changes needed edits", artifact="Approved PR", presence="agent",
    handoffs=[("release", "unk", "deploy mechanics not described; only outcome metrics", []),
              ("fix (CI failure → headless goose)", "doc", "failing CI becomes a draft-PR fix", [("block-eng-actionable-ci", "Actionable CI")])])
C["block"]["test"] = dict(na="Not split out; Gosling UI tests are noted under operate")
C["block"]["release"] = dict(
    agents="Not described. Outcome claims: post-change incidents down 70%+; Square shipped 130 features in H1 2026 (3x+)", who="Not described", artifact="Live change", presence="none",
    handoffs=[("operate", "unk", "no row in the map", [])])
C["block"]["operate"] = dict(
    agents="Overnight agents that scan vulnerabilities and draft patches from bug tickets; Gosling UI tests; red-team fixes upstreamed; skills marketplace (100+ skills); Buzz agents with memory", who="Engineers, security, support; customers via support bots", artifact="Patches, skills, product signal", presence="agent",
    handoffs=[("write code (bug tickets, vulnerabilities)", "doc", "background agents draft patches overnight for engineers to review in the morning", [("lenny-podcast-block-dhanji-goose", "CTO")]),
              ("shared capability", "doc", "red-team findings become upstream goose fixes; skills are PR-reviewed into the marketplace; ~50 AI Champions", [("block-eng-red-teamed-own-ai-agent", "red team"), ("block-eng-3-principles-agent-skills", "skills")]),
              ("every task (company 'world model')", "unk", "proposed in the essay as what replaces management's information routing; not shown in use", [("block-from-hierarchy-to-intelligence", "essay")])])

# ---------------------------------------------------------------- rendering helpers
STATUS_LABEL = dict(doc="documented", inf="inferred", unk="unknown")


SYMBOLS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
           '<symbol id="g-doc" viewBox="0 0 34 12"><path d="M1 6h26"/><path d="M23 1.5l5 4.5-5 4.5"/></symbol>'
           '<symbol id="g-inf" viewBox="0 0 34 12"><path d="M1 6h26" stroke-dasharray="4 3"/><path d="M23 1.5l5 4.5-5 4.5"/></symbol>'
           '<symbol id="g-unk" viewBox="0 0 34 12"><path d="M1 6h20" stroke-dasharray="1.5 3.5"/><circle cx="27" cy="6" r="4"/></symbol></svg>')


def glyph(status):
    return f'<svg class="hs hs-{status}" aria-hidden="true"><use href="#g-{status}"/></svg>'


def handoff_html(eco, h):
    target, status, note, sources = h
    links = " · ".join(src(s, l) for s, l in sources)
    tail = f' <span class="hsrc">{links}</span>' if links else ""
    return (f'<li class="ho ho-{status}">{glyph(status)}<span class="hostat">{STATUS_LABEL[status]}</span> '
            f'<span class="hot">→ {escape(target)}</span>'
            f'<span class="hon">{escape(note)}.{tail} <a class="hmap" href="{eco["map_handoffs"]}" title="This ecosystem\'s handoff table">map</a></span></li>')


def cell_html(eco, tkey, mode):
    c = C[eco["key"]][tkey]
    if "na" in c:
        return f'<div class="cell cell-na"><span class="na">{escape(c["na"])}</span></div>'
    hos = "".join(handoff_html(eco, h) for h in c["handoffs"])
    return (f'<div class="cell">'
            f'<p class="ag">{escape(c["agents"])}</p>'
            f'<p class="who"><span class="k">who</span> {escape(c["who"])}</p>'
            f'<p class="art"><span class="k">artifact</span> {escape(c["artifact"])}</p>'
            f'<ul class="hos">{hos}</ul>'
            f'</div>')


def task_label(t, with_sub=True):
    key, label, sub = t
    s = f'<span class="sub">{escape(sub)}</span>' if (sub and with_sub) else ""
    return f'<span class="tl">{escape(label)}</span>{s}'


def matrix_html():
    head = "".join(
        f'<th scope="col" class="eco-h"><a href="{e["map_md"]}">{e["name"]}</a><span class="eco-sub">{escape(e["tagline"])}</span>'
        f'<span class="eco-links"><a href="{e["map_html"]}">visual map</a> · <a href="{e["map_cnv"]}">could not verify</a></span></th>'
        for e in ECOS)
    rows = []
    for t in TASKS:
        cls = ' class="row-intent"' if t[0] in ("goal", "intent") else ""
        cells = "".join(f'<td>{cell_html(e, t[0], "matrix")}</td>' for e in ECOS)
        rows.append(f'<tr{cls}><th scope="row" class="task-h">{task_label(t)}</th>{cells}</tr>')
    seam_cells = "".join(
        f'<td><div class="cell cell-seam"><p class="ag">{escape(e["seam_title"])}</p><p class="seamtxt">{escape(e["seam"])}</p>'
        f'<p class="hsrc">{srcs(*e["seam_src"])} · <a href="{e["map_md"]}">map</a></p></div></td>' for e in ECOS)
    rows.append(f'<tr class="row-seam"><th scope="row" class="task-h"><span class="tl">Where context breaks</span><span class="sub">the seam each map found</span></th>{seam_cells}</tr>')
    return (f'<div class="matrix-wrap" tabindex="0" aria-label="Lifecycle tasks against six ecosystems; scrolls sideways">'
            f'<table class="matrix"><thead><tr><th scope="col" class="corner">Task ↓ · Ecosystem →</th>{head}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


def byeco_html():
    out = []
    for e in ECOS:
        items = []
        for t in TASKS:
            cls = ' class="row-intent"' if t[0] in ("goal", "intent") else ""
            items.append(f'<div class="eco-row"{cls}><div class="eco-task">{task_label(t)}</div>{cell_html(e, t[0], "eco")}</div>')
        hc = e["handoffs"]
        out.append(
            f'<article class="eco-card" id="eco-{e["key"]}">'
            f'<header class="eco-card-h"><h3><a href="{e["map_md"]}">{e["name"]}</a></h3><p class="lede-s">{escape(e["tagline"])}</p>'
            f'<p class="meta"><a href="{e["map_html"]}">visual map</a> · <a href="{e["map_handoffs"]}">handoff table</a> · '
            f'{hc["total"]} handoffs: {hc["doc"]} documented, {hc["inf"]} inferred, {hc["unk"]} unknown · <a href="{e["map_cnv"]}">could not verify</a></p></header>'
            f'<div class="eco-seam"><p class="ag">Where context breaks: {escape(e["seam_title"])}</p><p>{escape(e["seam"])}</p><p class="hsrc">{srcs(*e["seam_src"])}</p></div>'
            f'<div class="eco-rows">{"".join(items)}</div></article>')
    return '<div class="eco-list">' + "".join(out) + "</div>"


# ---------------------------------------------------------------- presence table
PRES = dict(agent=("●", "named agent or agent workflow"), tool=("◐", "a tool, object or process, no agent"), none=("○", "nothing named or not described"), na=("–", "not a separate task in this map"))


def presence_html():
    head = "".join(f'<th scope="col"><a href="{e["map_md"]}">{e["name"]}</a></th>' for e in ECOS)
    rows = []
    for t in TASKS:
        cells = []
        n_agent = 0
        n_app = 0
        for e in ECOS:
            c = C[e["key"]][t[0]]
            p = "na" if "na" in c else c["presence"]
            if p != "na":
                n_app += 1
                n_agent += p == "agent"
            g, title = PRES[p]
            cells.append(f'<td class="p-{p}" title="{escape(title)}"><span aria-hidden="true">{g}</span><span class="vh">{escape(title)}</span></td>')
        cls = ' class="row-intent"' if t[0] in ("goal", "intent") else ""
        rows.append(f'<tr{cls}><th scope="row">{task_label(t, False)}</th>{"".join(cells)}<td class="p-count">{n_agent} of {n_app}</td></tr>')
    legend = " · ".join(f'<span class="p-{k}">{g}</span> {escape(t)}' for k, (g, t) in PRES.items())
    return (f'<div class="tablewrap"><table class="presence"><thead><tr><th scope="col">Task</th>{head}<th scope="col">Agents</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div><p class="legend">{legend}. Counted from the task tables of the six maps; a tool that an agent merely reads (Atlassian Goals) counts as a tool.</p>')


# ---------------------------------------------------------------- dimensions table
DIMS = [
    ("Agent unit", "one general agent vs many narrow ones", f"{DIM}#sub-choice-agent-unit--persona-job-or-stage-as-the-unit-of-an-agent", "unit"),
    ("Interface", "Slack, own app, IDE, embedded", f"{DIM}#agent-interface-agent-interface-own-app-chat-or-embedded", "iface"),
    ("Sharing and privacy defaults", "who sees a session, and whether private work is allowed", f"{DIM}#trust-privacy-defaults-trust-and-privacy-defaults-for-sessions-and-context", "privacy"),
    ("Context bridge", "shared docs, public threads, sessions, artifacts", f"{DIM}#session-persistence-sharing-session-persistence-sharing-and-handoff", "bridge"),
    ("Review gating", "human every time, sloped to risk, or upstream", f"{DIM}#sub-choice-review-gating--how-human-review-of-agent-output-is-gated", "review"),
]


def dims_html():
    head = "".join(f'<th scope="col"><a href="{e["map_md"]}">{e["name"]}</a></th>' for e in ECOS)
    rows = []
    for name, sub, href, key in DIMS:
        cells = "".join(f'<td><p>{escape(e[key])}</p><p class="hsrc">{srcs(*e[key + "_src"])}</p></td>' for e in ECOS)
        extra = ""
        if key == "bridge":
            extra = (f' · <a href="{DIM}#context-and-memory-context-and-memory">context-and-memory</a>'
                     f' · <a href="{DIM}#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found">artifact-and-project-structure</a>')
        rows.append(f'<tr><th scope="row"><span class="tl">{escape(name)}</span><span class="sub">{escape(sub)}</span><span class="sub"><a href="{href}">register section</a>{extra}</span></th>{cells}</tr>')
    # pattern classes row (from the teardowns-to-pattern-classes mapping, revised classes)
    cl_cells = "".join(f'<td><p>{escape(e["classes"])}</p><p class="hsrc"><a href="{e["classes_href"]}">mapping entry</a></p></td>' for e in ECOS)
    rows.append(f'<tr><th scope="row"><span class="tl">Runtime pattern classes</span><span class="sub">P1–P11 with P5a/b and P8a–f, as revised on 2026-10-24</span>'
                f'<span class="sub"><a href="../research-agent-runtime-patterns-taxonomy/01-synthesis.md#b2-pattern-classes">synthesis B.2</a> · '
                f'<a href="../teardowns-to-pattern-classes/00-mapping.md#8-revised-classes-2026-10-24">mapping §8</a></span></th>{cl_cells}</tr>')
    # evidence row
    ev_cells = []
    for e in ECOS:
        v = e["evidence"]
        parts = [f"{v['fp']} first-party"]
        if v["vc"]:
            parts.append(f"{v['vc']} vendor claim")
        if v["ind"]:
            parts.append(f"{v['ind']} independent")
        if v["an"]:
            parts.append(f"{v['an']} anecdote")
        ev_cells.append(f'<td><p><strong>{v["n"]} source notes</strong>: {", ".join(parts)}. {escape(v["span"])}.</p><p class="hsrc"><a href="{e["map_cnv"]}">what the map could not verify</a></p></td>')
    rows.append(f'<tr><th scope="row"><span class="tl">Evidence quality</span><span class="sub">who says so, and how many of them</span>'
                f'<span class="sub"><a href="../research-agent-runtime-patterns-taxonomy/01-synthesis.md#h-evidence-quality-gaps-and-inconsistencies">synthesis §H</a> · '
                f'<a href="{DIM}#pm-agent-evaluation-how-we-would-know-a-pm-agent-works">pm-agent-evaluation</a></span></th>{"".join(ev_cells)}</tr>')
    return f'<div class="tablewrap"><table class="dims"><thead><tr><th scope="col">Dimension</th>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


# ---------------------------------------------------------------- evidence table
def evidence_html():
    rows = []
    for e in ECOS:
        v, h = e["evidence"], e["handoffs"]
        mix = []
        for n, lab in ((v["fp"], "first-party"), (v["vc"], "vendor claim"), (v["ind"], "independent"), (v["an"], "anecdote")):
            if n:
                mix.append(f"{n} {lab}")
        bar = "".join(f'<i class="eb eb-{k}" style="flex:{v[k]}" title="{lab}"></i>' for k, lab in (("fp", "first-party"), ("vc", "vendor claim"), ("ind", "independent"), ("an", "anecdote")) if v[k])
        rows.append(
            f'<tr><th scope="row"><a href="{e["map_md"]}">{e["name"]}</a></th>'
            f'<td><div class="ebar" aria-hidden="true">{bar}</div><span class="small">{v["n"]} notes: {", ".join(mix)}</span></td>'
            f'<td class="small">{escape(v["span"])}</td>'
            f'<td><span class="small">{h["total"]}: {glyph("doc")} {h["doc"]} · {glyph("inf")} {h["inf"]} · {glyph("unk")} {h["unk"]}</span><br><span class="small muted">{escape(h["note"])}</span></td>'
            f'<td class="small">{escape(v["single"])}. <a href="{e["map_cnv"]}">The map&#8217;s own list</a></td></tr>')
    return (f'<div class="tablewrap"><table class="evid"><thead><tr><th scope="col">Ecosystem</th><th scope="col">Sources cited by the map</th><th scope="col">Dates</th>'
            f'<th scope="col">Handoffs (documented · inferred · unknown)</th><th scope="col">Rows on a single source, and what could not be verified</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


# ---------------------------------------------------------------- strategy section
GAPS = [
    dict(
        title="Research → shaped intent, across people, with the evidence attached",
        where="Undocumented in all nine maps. Stripe: Kai → Orbit unknown. Ramp: the define → build contract's transport unknown. Shopify: documented only inside one thread; nothing links it to GSD or a durable artifact. Anthropic: research → another person's plan mode unknown. Atlassian: Deep Research stays in chat. Intercom: research → shape intent unknown. Airbnb: research evidence → plan unknown, and intent → plan drifts after prototyping. Spotify: research evidence → bet unknown; VPs carry it. Block: one person's goose session → plan across people unknown.",
        options=[
            ("A shared place where the next person starts from the thread or session", "Shopify's public thread, Anthropic's open channel, Ramp's shared session", "openness by default, one chat platform, a leadership-modelled culture; Shopify and Anthropic both say the corpus is what agents learn from"),
            ("A handoff artifact that carries evidence and acceptance criteria", "Ramp's named contract (data, requirements, prototype); Atlassian's work item with acceptance criteria; Anthropic's playbook chain (prescribed, not shown)", "a team-agreed spec standard; someone to keep it; it is slower for small work (Ramp runs small loops without one)"),
            ("One person does research, intent and plan", "Stripe's 'product hat' engineers, Anthropic's one-engineer pods, Intercom's coding designers, Block's DRI who owns idea to scale with PMs shipping PRs", "engineers close to customers, tiny pods, hiring for it; none of these is a tooling decision"),
            ("A senior person carries it", "Airbnb's CEO in every 1–12 week review with principles unwritten; Spotify's VPs pitching bets the co-CEOs rank", "a leader with the time and standing to be in every review; it is the least transferable bridge of the nine and records nothing"),
            ("An agent that carries research into planning", "Airbnb's Pascal drafts a concept brief from market research, the roadmap and objectives (whether it cites evidence is not described); Harbor reading Kai output goes to a prototype. Neither reaches a plan", "a research artifact an agent can read, and a planning agent to read it; Airbnb's proposed 'AI project coordinator' is the only named candidate and is not built"),
        ],
        questions=[
            "How split are research, intent and planning across people in the target org, compared with the role-blurred companies mapped here?",
            "When a PM finishes shaping and an engineer starts planning, what exactly should move: a session link, a ticket, a document, a prototype PR, an eval set?",
            "Is a prototype or an eval set acceptable as the spec of record in a regulated setting, or must a reviewable document exist?",
        ],
        links=[("intent-shaping-and-spec", f"{DIM}#intent-shaping-and-spec-intent-shaping-mode-and-spec-standard"), ("session-persistence-sharing", f"{DIM}#session-persistence-sharing-session-persistence-sharing-and-handoff"), ("story S05", "../user-story-mapping/stories-jobs.md#s05-write-and-ratify-a-spec-engineers-can-act-on"), ("theme: opportunity-to-code-chain", "../../research/THEMES.md#opportunity-to-code-chain-opportunity--problem--goal--intent--plan--code")],
    ),
    dict(
        title="Goal → intent: no agent anywhere, and the goal is rarely an object an agent can read",
        where="No map names an agent that sets a goal, and the goal → intent handoff is inferred or unknown in six of nine. The goal exists as a readable object only at Atlassian (Goals, with a graph edge to work items), as a reviewed process at Shopify (GSD Proposal, 2023 evidence) and Spotify (30–50 bets stack-ranked every six months, with no object for a bet in the catalog), and as eval goals and gates set up front at Airbnb for AI features. This is the band where Geoff's reference workload, intent shaping, sits.",
        options=[
            ("Leave goal-setting to people and start the agent at intent", "All six, in practice", "nothing; but then the shaping agent cannot check intent against the goal"),
            ("Make the goal a readable object agents ground on", "Atlassian Goals and the work item → goal edge; Shopify's GSD proposal; Anthropic's written team principles; Airbnb's one roadmap and eval gates; Spotify's bets board (the map suggests a bet as a catalog kind; nobody has built it); Block's proposed company markdown file", "a system of record for goals that is kept current; at Atlassian no source says Planner reads it, and at Spotify the catalog holds systems, not bets"),
            ("A shaping agent that interrogates rough intent against goals and constraints", "Jira Planner's clarifying questions (Early Access); Anthropic's 'send the spec to Claude Code' test; Airbnb's Pascal drafting the concept brief; Geoff's reference workload", "a question set the team agrees on, and access to the constraints (risk, dependencies, data) that answer it"),
        ],
        questions=[
            "Where do goals live in the target org today, and can an agent read them with current access?",
            "What are the universal questions every piece of intent must answer here, and where is the source for each answer?",
        ],
        links=[("intent-shaping-mode", f"{DIM}#sub-choice-intent-shaping-mode--who-shapes-intent-and-how"), ("work-structure", f"{DIM}#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent"), ("Geoff's answer Q8", "../research-agent-runtime-patterns-taxonomy/01-synthesis.md#geoffs-answers-2026-10-24")],
    ),
    dict(
        title="The plan: a shared artifact in two ecosystems, a session or a thread in the other four",
        where="Stripe's Orbit produces a shareable, commented plan in a workspace; Atlassian's Planner produces work items with acceptance criteria (claimed); Block's Builderbot plans from a ticket inside its own run and goose's repo uses 'Ready' issues. Anthropic and Intercom hold the plan in a Claude Code session; Shopify holds it in the thread; Ramp has no planning step of its own. Airbnb names the drift between brief, prototypes and Jira, and Spotify's engineering intent (a versioned prompt with done defined as tests) is agent-ready where its product intent is not. Intercom re-captures intent later, in the PR description.",
        options=[
            ("No plan artifact; capture the why at the PR", "Intercom's hook-enforced create-pr skill, checked in review", "cheap and enforceable; captures intent after planning, so it cannot stop a well-built wrong thing"),
            ("A plan that lives in a shared workspace", "Stripe Orbit workspaces", "evidence is one vendor video"),
            ("Plan as work items with acceptance criteria that the reviewer checks", "Atlassian Planner and the acceptance-criteria review", "Early Access; an empty description means no check"),
            ("A committed plan file", "Anthropic's playbook (prescription); Spotify's Git-versioned migration prompts with end state, preconditions, examples and done-as-tests (engineering only); Block's 'Ready' issues with agreed design and verification", "discipline to write it; shown only for engineering changes, not product intent"),
            ("An agent that keeps brief, prototypes and tickets in sync", "Airbnb's proposed 'AI project coordinator', 'early days'", "not built anywhere; depends on the brief, prototypes and tickets being readable by one agent"),
        ],
        questions=[
            "Does a regulated reviewer accept a PR description or a session transcript as the decision record, or is a plan artifact mandatory?",
            "Does a plan artifact slow small work enough that teams route around it, as Ramp's small loops do?",
        ],
        links=[("spec-standard", f"{DIM}#sub-choice-spec-standard--what-counts-as-agent-ready-intent"), ("artifact-and-project-structure", f"{DIM}#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found")],
    ),
    dict(
        title="Review sloped to risk, on top of a human somewhere",
        where="Every ecosystem keeps a human in review. Four slope it: Anthropic's risk tiers (none, one or two humans), Intercom's ~19% auto-approval, Ramp's Review Buddy on 93% with seniors on the hard 7%, Spotify's auto-merge for safe fleet changes behind deterministic verifiers. Stripe, Shopify, Atlassian and Block keep a person on every PR; Shopify calls that 'a big bottleneck', Spotify says 'the next constraint became our ability to verify it', and Airbnb's platform lead predicts 'overwhelming code review'. Airbnb's review is the CEO's, on a fixed cadence, and records nothing.",
        options=[
            ("A person on every change plus an agent", "Stripe (Gru), Shopify (PR-review profile), Atlassian (acceptance-criteria check)", "easy to defend; the bottleneck grows with agent volume"),
            ("Risk-scored routing with partial auto-approval", "Anthropic's classifiers, Intercom's size-and-risk rule, Ramp's reviewer that picks the human, Spotify's auto-merge for 'safe' fleet changes (which once broke production and gained safeguards)", "a trusted scorer, strong CI and test suites, an audit trail; all figures are self-reported"),
            ("Deterministic verification before any PR exists", "Spotify's stop-hook verifiers and verification service (its LLM judge was dropped); Airbnb's validation loops and critic model; Block's headless goose on CI failures", "a test suite the verifiers can run; Spotify says verification capacity is now the limit"),
            ("Review against stated intent, not only the diff", "Intercom's reviewers read the PR's why; Ramp's Review Buddy reads the prompts; Atlassian checks acceptance criteria; Airbnb requires the engineer to explain an AI-written PR", "intent must be written somewhere the reviewer can read"),
        ],
        questions=[
            "Who certifies the risk scorer in a regulated org, and what audit trail does an auto-approved change need?",
            "Is the test coverage that makes Minions, Inspect and Intercom's auto-deploys safe present in the target codebases?",
        ],
        links=[("review-gating", f"{DIM}#sub-choice-review-gating--how-human-review-of-agent-output-is-gated"), ("autonomy-calibration", f"{DIM}#sub-choice-autonomy-calibration--who-sets-how-much-autonomy-an-agent-gets-and-how-it-changes")],
    ),
    dict(
        title="Learning loops that depend on transcripts being available",
        where="Eight of nine write back: Shopify's nightly 'dreaming' and corpus mining, Intercom's SessionEnd hook, Anthropic's lessons.md and incidents-as-evals, Ramp's 24-hour memory and Dojo edits, Stripe's factory logs, Airbnb's production evals and weekly retraining, Spotify's ship/abort/iterate record and Xirp transcripts flowing back to Portal, Block's PR-reviewed skills and upstreamed red-team fixes. Atlassian's 'results feed back into the next spec' has no mechanism. The strongest loops read transcripts, which public-by-default makes available; the bridge from a learning record to the next goal is described nowhere (Spotify's and Airbnb's maps both say so).",
        options=[
            ("Mine transcripts into skills and memory", "Shopify, Intercom, Ramp; Spotify's Xirp transcripts into Portal", "transcripts retained and readable; redaction before reuse; retention rules may forbid it"),
            ("Owner-edited shared knowledge", "Ramp's 6,500+ edits by 323 people; Anthropic's CLAUDE.md and REVIEW.md; Block's PR-reviewed skills marketplace; Spotify's AiKA driving doc fixes", "people who maintain it; no transcript access needed"),
            ("Write-back as a duty of every agent", "Intercom's 'what we built' doc gating support readiness; Anthropic's alert agent that writes the fix; Airbnb's production failures becoming evals in a weekly PM review", "a place to write to that the next agent reads"),
            ("A structured decision record from experiments", "Spotify's Confidence labels every test ship, abort or iterate, with reasons", "an experimentation platform with a default ship rule; the record's link to the next bet is not described"),
        ],
        questions=[
            "Can session transcripts be retained and mined under the target org's retention, privacy and works-council rules?",
            "Does visibility itself drive the learning, or the mining? If mining, a private default with an opt-in corpus may capture most of the value.",
        ],
        links=[("context-and-memory", f"{DIM}#context-and-memory-context-and-memory"), ("trust-privacy-defaults", f"{DIM}#trust-privacy-defaults-trust-and-privacy-defaults-for-sessions-and-context")],
    ),
]


def gaps_html():
    out = []
    for g in GAPS:
        opts = "".join(f'<tr><td>{escape(o)}</td><td>{escape(ex)}</td><td>{escape(cond)}</td></tr>' for o, ex, cond in g["options"])
        qs = "".join(f"<li>{escape(q)}</li>" for q in g["questions"])
        links = " · ".join(f'<a href="{h}">{escape(l)}</a>' for l, h in g["links"])
        out.append(
            f'<article class="gap"><h3>{escape(g["title"])}</h3><p class="where">{escape(g["where"])}</p>'
            f'<div class="tablewrap"><table class="opts"><thead><tr><th>Option seen in the maps</th><th>Where</th><th>Conditions it depends on (which a regulated org may lack)</th></tr></thead><tbody>{opts}</tbody></table></div>'
            f'<p class="kq-h">Key questions (unranked)</p><ol class="kq">{qs}</ol><p class="hsrc">Register: {links}</p></article>')
    return "".join(out)


# ---------------------------------------------------------------- page
CSS = r"""
:root{
  --paper:#f6f6f2; --surface:#ffffff; --ink:#1d2228; --muted:#5d6670; --rule:#d6d9d6; --accent:#b4580c; --accent-soft:#f5e3d2; --lite:#f1f3f1; --band:#fbf3ea;
  --serif:Charter, "Iowan Old Style", Georgia, "Times New Roman", serif; --sans:system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif; --mono:ui-monospace, Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--paper:#15181b; --surface:#1d2125; --ink:#e7e9e6; --muted:#a3abb2; --rule:#343a40; --accent:#f0a35e; --accent-soft:#3a2a1c; --lite:#22272b; --band:#241f1a; color-scheme:dark}}
:root[data-theme="dark"]{--paper:#15181b; --surface:#1d2125; --ink:#e7e9e6; --muted:#a3abb2; --rule:#343a40; --accent:#f0a35e; --accent-soft:#3a2a1c; --lite:#22272b; --band:#241f1a; color-scheme:dark}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%; scroll-behavior:smooth}
body{margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:16px; line-height:1.55}
a{color:inherit; text-decoration-color:var(--rule); text-underline-offset:2px}
a:hover{text-decoration-color:var(--accent)}
.wrap{max-width:1180px; margin:0 auto; padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); padding-block:36px 72px; display:grid; grid-template-columns:minmax(0,1fr); gap:40px}
.wrap > *, .views > *, section > *, .gap > *, .eco-card > *, .card > *{min-width:0}
header.top{display:grid; gap:12px; max-width:76ch}
.eyebrow{font-family:var(--mono); font-size:12.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted)}
h1{font-family:var(--serif); font-weight:600; font-size:clamp(30px,4.4vw,46px); line-height:1.08; margin:0; text-wrap:balance}
h2{font-family:var(--serif); font-weight:600; font-size:26px; margin:0 0 6px; text-wrap:balance}
h3{font-family:var(--serif); font-weight:600; font-size:20px; margin:0 0 6px; text-wrap:balance}
p{margin:0; max-width:76ch}
.lede{font-size:18px}
.muted{color:var(--muted)}
.small{font-size:13.5px}
.vh{position:absolute; width:1px; height:1px; margin:-1px; padding:0; overflow:hidden; clip:rect(0 0 0 0); white-space:nowrap; border:0}
nav.toc{font-size:14px; color:var(--muted); display:flex; flex-wrap:wrap; gap:6px 14px}
nav.toc a{white-space:nowrap}
.answer{background:var(--surface); border:1px solid var(--rule); border-left:4px solid var(--accent); border-radius:6px; padding:20px 22px; display:grid; gap:12px}
.answer ol{margin:0; padding-left:22px; display:grid; gap:10px; max-width:78ch}
section{display:grid; gap:14px}
section > p{max-width:78ch}
.legend{font-size:13.5px; color:var(--muted); display:flex; flex-wrap:wrap; gap:6px 18px; align-items:center; max-width:none}
.legend .hs{vertical-align:middle}
/* handoff glyphs: form carries the status, colour only helps */
.hs{width:34px; height:12px; vertical-align:-1px; margin-right:4px; fill:none; stroke-width:1.8; stroke-linecap:round; stroke-linejoin:round; flex:none}
.hs-doc{stroke:var(--ink)}
.hs-inf{stroke:var(--muted)}
.hs-unk{stroke:var(--accent)} .hs-unk circle{fill:var(--paper)}
/* view toggle (CSS only) */
.views{display:grid; gap:16px}
.seg{display:inline-flex; border:1px solid var(--rule); border-radius:999px; overflow:hidden; background:var(--surface); font-size:14px}
.seg label{padding:7px 16px; cursor:pointer; color:var(--muted)}
.seg label:first-child{border-right:1px solid var(--rule)}
#v-matrix:checked ~ .views .seg label[for="v-matrix"], #v-eco:checked ~ .views .seg label[for="v-eco"]{background:var(--ink); color:var(--paper)}
#v-matrix:focus-visible ~ .views .seg label[for="v-matrix"], #v-eco:focus-visible ~ .views .seg label[for="v-eco"]{outline:2px solid var(--accent); outline-offset:-2px}
#v-eco:checked ~ .views .matrix-view{display:none}
#v-matrix:checked ~ .views .eco-view{display:none}
/* matrix */
.matrix-wrap{overflow:auto; max-height:min(84vh, 1100px); border:1px solid var(--rule); border-radius:6px; background:var(--surface); overscroll-behavior:contain}
.matrix-wrap:focus-visible{outline:2px solid var(--accent)}
table.matrix{border-collapse:separate; border-spacing:0; width:max-content; min-width:100%; font-size:13.5px; line-height:1.45}
table.matrix th, table.matrix td{text-align:left; vertical-align:top; border-bottom:1px solid var(--rule); border-right:1px solid var(--rule); padding:0}
table.matrix td{min-width:250px; max-width:300px; width:280px}
table.matrix thead th{position:sticky; top:0; z-index:3; background:var(--paper); padding:12px 14px; font-weight:500}
table.matrix thead th.corner{left:0; z-index:5; font-family:var(--mono); font-size:11.5px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); min-width:150px; width:150px}
.eco-h > a{font-family:var(--serif); font-size:19px; font-weight:600; text-decoration:none; display:block}
.eco-sub{display:block; font-size:12.5px; color:var(--muted); margin-top:4px; line-height:1.4}
.eco-links{display:block; font-family:var(--mono); font-size:11px; color:var(--muted); margin-top:6px}
th.task-h{position:sticky; left:0; z-index:2; background:var(--paper); padding:12px 14px; min-width:150px; width:150px; max-width:150px; font-weight:600}
.tl{display:block; font-family:var(--serif); font-size:15.5px; line-height:1.25}
.sub{display:block; font-size:12px; color:var(--muted); font-weight:400; margin-top:3px; line-height:1.35}
tr.row-intent td, tr.row-intent th.task-h{background:var(--band)}
tr.row-intent th.task-h{box-shadow:inset 3px 0 0 var(--accent)}
tr.row-seam td, tr.row-seam th.task-h{background:var(--lite)}
.cell{padding:12px 14px; display:grid; gap:6px}
.cell-na{color:var(--muted); font-style:italic}
.cell .ag{font-weight:600; max-width:none}
.cell .who,.cell .art{color:var(--muted); font-size:12.5px; max-width:none}
.k{font-family:var(--mono); font-size:10.5px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); margin-right:3px}
.hos{list-style:none; margin:4px 0 0; padding:8px 0 0; border-top:1px dashed var(--rule); display:grid; gap:6px}
.ho{display:grid; grid-template-columns:auto auto 1fr; column-gap:6px; align-items:baseline; font-size:12.5px}
.ho .hs{align-self:center}
.hostat{font-family:var(--mono); font-size:10.5px; letter-spacing:.04em; text-transform:uppercase; color:var(--muted)}
.ho-unk .hostat{color:var(--accent)}
.hot{font-weight:600}
.hon{grid-column:2 / -1; color:var(--muted)}
.hsrc{font-size:12px; color:var(--muted); max-width:none}
.hsrc a, .hmap{color:var(--muted)}
.hmap{font-family:var(--mono); font-size:10.5px}
.seamtxt{font-size:12.5px; max-width:none}
/* by-ecosystem view */
.eco-list{display:grid; gap:22px}
.eco-card{background:var(--surface); border:1px solid var(--rule); border-radius:6px; overflow:hidden}
.eco-card-h{padding:18px 18px 14px; border-bottom:1px solid var(--rule); display:grid; gap:6px}
.eco-card-h h3{font-size:24px; margin:0}
.eco-card-h h3 a{text-decoration:none}
.lede-s{color:var(--muted)}
.meta{font-size:13px; color:var(--muted); font-family:var(--mono)}
.eco-seam{padding:14px 18px; background:var(--lite); border-bottom:1px solid var(--rule); display:grid; gap:6px; font-size:14px}
.eco-seam p{max-width:none}
.eco-rows{display:grid}
.eco-row{display:grid; grid-template-columns:170px minmax(0,1fr); border-bottom:1px solid var(--rule); font-size:13.5px}
.eco-row:last-child{border-bottom:none}
.eco-row.row-intent{background:var(--band); box-shadow:inset 3px 0 0 var(--accent)}
.eco-task{padding:12px 14px; font-weight:600; border-right:1px solid var(--rule)}
@media (max-width:640px){.eco-row{grid-template-columns:1fr} .eco-task{border-right:none; border-bottom:1px dashed var(--rule); padding-bottom:8px} .eco-task .tl{display:inline} .eco-task .sub{display:inline; margin-left:6px}}
/* generic tables */
.tablewrap{position:relative; overflow-x:auto; border:1px solid var(--rule); border-radius:6px; background:var(--surface)}
.tablewrap table{border-collapse:collapse; width:100%; font-size:14px}
.tablewrap th,.tablewrap td{text-align:left; vertical-align:top; padding:10px 14px; border-bottom:1px solid var(--rule)}
.tablewrap thead th{font-family:var(--mono); font-size:11.5px; font-weight:500; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); background:var(--paper)}
.tablewrap tbody tr:last-child td, .tablewrap tbody tr:last-child th{border-bottom:none}
.tablewrap tbody th{font-weight:600; background:var(--paper)}
table.presence{min-width:640px; text-align:center}
table.presence td{text-align:center; font-size:20px; line-height:1}
table.presence td.p-count{font-family:var(--mono); font-size:12.5px; color:var(--muted); white-space:nowrap}
table.presence th[scope=row]{text-align:left; white-space:nowrap}
table.presence tr.row-intent th, table.presence tr.row-intent td{background:var(--band)}
.p-agent{color:var(--ink)} .p-tool{color:var(--muted)} .p-none{color:var(--accent)} .p-na{color:var(--rule)}
table.dims{min-width:1180px}
table.dims td{width:16%; font-size:13.5px}
table.dims th[scope=row]{min-width:170px; width:170px}
table.dims p{max-width:none}
table.evid{min-width:980px}
table.evid td{font-size:13.5px}
.ebar{display:flex; height:8px; border-radius:4px; overflow:hidden; background:var(--lite); margin-bottom:6px; max-width:220px}
.eb{display:block; height:100%}
.eb-fp{background:var(--ink)} .eb-vc{background:var(--muted); background-image:repeating-linear-gradient(135deg, transparent 0 3px, var(--paper) 3px 4px)} .eb-ind{background:var(--accent)} .eb-an{background:var(--rule)}
/* seams and gaps */
.cards{display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:14px}
.card{background:var(--surface); border:1px solid var(--rule); border-radius:6px; padding:16px 18px; display:grid; gap:8px; align-content:start; font-size:14px}
.card h3{font-size:18px}
.card p{max-width:none}
.card .eco-k{font-family:var(--mono); font-size:11.5px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted)}
.pattern{background:var(--surface); border:1px solid var(--rule); border-left:4px solid var(--accent); border-radius:6px; padding:18px 20px; display:grid; gap:10px}
.pattern ul{margin:0; padding-left:20px; display:grid; gap:8px; max-width:80ch}
.gap{background:var(--surface); border:1px solid var(--rule); border-radius:6px; padding:18px 20px; display:grid; gap:10px}
.gap .where{color:var(--muted); font-size:14.5px; max-width:none}
.gap table.opts{min-width:720px; font-size:13.5px}
.gap table.opts td:first-child{font-weight:600; width:28%}
.kq-h{font-family:var(--mono); font-size:11.5px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); margin-top:4px}
ol.kq{margin:0; padding-left:22px; display:grid; gap:6px; max-width:80ch; font-size:14.5px}
.foot{font-size:13.5px; color:var(--muted); max-width:86ch; display:grid; gap:8px}
@media (max-width:640px){
  .wrap{gap:30px; padding-block:24px 56px}
  h2{font-size:22px}
  .answer{padding:16px}
  table.matrix td{min-width:230px; width:240px}
  th.task-h, table.matrix thead th.corner{min-width:120px; width:120px; max-width:120px}
  .matrix-wrap{max-height:80vh}
}
@media print{.matrix-wrap{max-height:none; overflow:visible} .seg{display:none}}
"""


def page():
    n_eco = len(ECOS)
    total_handoffs = sum(e["handoffs"]["total"] for e in ECOS)
    total_doc = sum(e["handoffs"]["doc"] for e in ECOS)
    total_inf = sum(e["handoffs"]["inf"] for e in ECOS)
    total_unk = sum(e["handoffs"]["unk"] for e in ECOS)
    total_src = sum(e["evidence"]["n"] for e in ECOS)
    total_ind = sum(e["evidence"]["ind"] for e in ECOS)
    maps_list = " · ".join(f'<a href="{e["map_md"]}">{e["name"]}</a>' for e in ECOS)

    seam_cards = "".join(
        f'<article class="card"><span class="eco-k">{e["name"]}</span><h3>{escape(e["seam_title"])}</h3><p>{escape(e["seam"])}</p>'
        f'<p class="hsrc">{srcs(*e["seam_src"])} · <a href="{e["map_md"]}">map</a></p></article>' for e in ECOS)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Lifecycle Across Ecosystems</title>
<meta name="description" content="The product and software lifecycle, task by task, laid against nine agent ecosystems (Stripe, Ramp, Shopify, Anthropic, Atlassian, Intercom, Airbnb, Spotify, Block): agents, artifacts, handoffs marked documented, inferred or unknown, the seams, and what it means for the strategy deck.">
<style>{CSS}</style>
</head>
<body>
{SYMBOLS}
<div class="wrap">
<header class="top">
  <div class="eyebrow">Cross-ecosystem map · lifecycle by task · 24 Oct 2026</div>
  <h1>The product lifecycle across nine agent ecosystems, task by task</h1>
  <p class="lede">Nine maps in one frame: {maps_list}. Rows are tasks, not job titles; columns are the companies whose agent ecosystems the project mapped. Each cell shows the agents or tools, who does the task, the artifact, and each handoff out of the task marked <strong>documented</strong> (a source says it happens), <strong>inferred</strong> (consistent with the sources, not stated) or <strong>unknown</strong> (not described). Every figure and claim comes from the six maps and the source notes they cite, and links to them.</p>
  <nav class="toc" aria-label="Sections"><a href="#answer">Short answer</a><a href="#matrix">The matrix</a><a href="#seams">Where context breaks</a><a href="#dimensions">By dimension</a><a href="#strategy">For the strategy deck</a><a href="#evidence">Evidence</a><a href="#method">Method</a></nav>
</header>

<div class="answer" id="answer">
  <h2>Downstream of intent the handoffs are documented everywhere; upstream, research → intent → plan across people is documented nowhere</h2>
  <ol>
    <li><strong>Agents sit at the same tasks in all nine.</strong> Research, shape the intent, write the code, review and operate have a named agent or agent workflow in every ecosystem. Code → review → release is documented in all nine, mostly with a mechanism.</li>
    <li><strong>No ecosystem has an agent that sets the goal,</strong> and the goal → intent handoff is inferred or unknown in six of nine. The goal is a readable object only at Atlassian (Goals), a reviewed process at Shopify (GSD, 2023 evidence) and Spotify (the six-month bets board), and eval gates set up front at Airbnb, for AI features only. This band is where Geoff's reference workload, intent shaping, sits.</li>
    <li><strong>Research → shaped intent or plan, across people, with the evidence attached, is undocumented in all nine.</strong> Each ecosystem closes the gap another way: one person does all three tasks (Stripe, Anthropic, Intercom, Block), a shared place stands in for a handoff (Shopify's thread, Anthropic's channel, Ramp's session, Block's Builderbot thread), a senior person carries it (Airbnb's CEO in every review, Spotify's VP pitching the bet), or an object carries the <em>what</em> without the <em>why</em> (Atlassian's work item, Intercom's PR description, Spotify's catalog). The nearest thing to an agent carrying research into intent is Airbnb's Pascal, which drafts a brief from research with a mechanism nobody describes.</li>
    <li><strong>The practices that close the gap depend on conditions a regulated org may lack:</strong> public-by-default sessions, engineers close to customers, tiny pods, a CEO in every review, strong test suites behind auto-approval, and transcripts available to mine. The evidence is first-party and self-reported in {total_src - total_ind} of {total_src} source notes.</li>
  </ol>
</div>

<input type="radio" name="view" id="v-matrix" class="vh" checked>
<input type="radio" name="view" id="v-eco" class="vh">
<div class="views" id="matrix">
  <section>
    <h2>The matrix: tasks against ecosystems</h2>
    <p>Ten tasks shared by all nine maps, plus <em>Test</em>, which the Ramp map split out for its QA agent. The last row is the seam each map found. The band marks goal → intent, the intent-shaping handoff. Scroll sideways inside the table; row and column labels stay put. On a phone the by-ecosystem view reads top to bottom.</p>
    <div class="legend" role="note">
      <span>{glyph("doc")}<strong>documented</strong> solid</span>
      <span>{glyph("inf")}<strong>inferred</strong> dashed</span>
      <span>{glyph("unk")}<strong>unknown</strong> dotted, hollow end</span>
      <span>“no row in the map” means the map's handoff table has no entry for that pair, so we show it as unknown.</span>
      <span class="seg" role="group" aria-label="View"><label for="v-matrix">Matrix</label><label for="v-eco">By ecosystem</label></span>
    </div>
  </section>
  <div class="matrix-view">{matrix_html()}</div>
  <div class="eco-view">{byeco_html()}</div>
</div>

<section id="seams">
  <h2>Where context breaks, and the shared pattern</h2>
  <p>Each map answered the same question: where does context break between research, intent and plan, across people? Nine different places, one pattern.</p>
  <div class="cards">{seam_cards}</div>
  <div class="pattern">
    <h3>The shared pattern</h3>
    <ul>
      <li><strong>Documented handoffs cluster downstream.</strong> Of {total_handoffs} handoffs across the nine maps, {total_doc} are documented, {total_inf} inferred and {total_unk} unknown, and the unknowns sit almost entirely upstream of code: research → plan (Stripe, Anthropic, Atlassian, Intercom, Airbnb, Block), goal → intent (Ramp, Spotify), define → build across people (Ramp), intent → plan after prototyping (Airbnb), bet → agent work (Spotify), the formal process ↔ the thread (Shopify), plus release and deploy mechanics that four maps could not find.</li>
      <li><strong>Where handoffs work, something shared is doing the carrying,</strong> or someone senior, not an agent: Stripe's documents and tool layer, Ramp's shared session, Shopify's public thread, Anthropic's open channel, Atlassian's work item, Intercom's PR description, Block's ticket or thread into Builderbot, Spotify's catalog and its pitching VPs, Airbnb's CEO in every review. The agent reads the shared thing; nobody hands the agent a research result.</li>
      <li><strong>The <em>why</em> is the first thing lost.</strong> Atlassian's work item carries the what; Intercom captures the why only at the PR; Ramp names the contract (data, requirements, prototype) but not its format; Anthropic's eval set carries examples without the reasoning; Spotify's catalog carries systems, not reasons; Builderbot is told what to build, not why; Airbnb keeps review decisions unwritten on purpose. Shopify's thread keeps the why but only inside Slack, and not for private work.</li>
      <li><strong>Role blur is doing silent work.</strong> Stripe, Anthropic, Intercom and Block all say the same tasks are done by one person more often than their titles suggest, and Block has gone furthest (one DRI from idea to scale, PMs shipping PRs). Airbnb went the other way, splitting the PM into four roles, and needed the CEO to bridge them. It is the norm in the target org that decides whether the seam costs a lot.</li>
    </ul>
  </div>
  <h3>Which tasks have agents, where</h3>
  {presence_html()}
</section>

<section id="dimensions">
  <h2>The six ecosystems by the dimensions that matter here</h2>
  <p>Each row links to its section in the options register, where the options and key questions live, or, for the pattern classes, to the synthesis and the teardown mapping. These cells are descriptions from the maps and the mapping, not recommendations. The Airbnb, Spotify and Block placements use the revised classes; the other six keep the mapping's original rows plus its section 8 re-placements.</p>
  {dims_html()}
</section>

<section id="strategy">
  <h2>What it means for the strategy deck</h2>
  <p>The deck informs a resource request and keeps the choice open, so each common gap below is framed as options seen in the maps, the conditions each depends on, and the key questions that would decide. Nothing here is a recommendation; the register sections hold the full menus.</p>
  {gaps_html()}
</section>

<section id="evidence">
  <h2>Evidence: who says so</h2>
  <p>Of {total_src} source notes cited across the nine maps, {total_ind} are independent (a 2024 piece on Stripe's culture, a 2020 critique of Spotify's squad model, a 2026 Semafor piece on Airbnb, and the Guardian on Block's staff), and none of them checks an AI figure. The rest are the companies describing themselves, their executives on podcasts, their product docs, or anecdotes. Several rows rest on one source. Treat every figure as a vendor claim until something outside the company confirms it.</p>
  {evidence_html()}
  <p class="legend"><span><i class="eb eb-fp" style="display:inline-block;width:14px;height:8px;border-radius:2px"></i> first-party</span><span><i class="eb eb-vc" style="display:inline-block;width:14px;height:8px;border-radius:2px"></i> vendor claim</span><span><i class="eb eb-ind" style="display:inline-block;width:14px;height:8px;border-radius:2px"></i> independent</span><span><i class="eb eb-an" style="display:inline-block;width:14px;height:8px;border-radius:2px"></i> anecdote</span><span>Tags are the ones on each source note's frontmatter (<a href="../../research/README.md">research/README.md</a>). Counts are distinct source notes linked from each map.</span></p>
</section>

<section id="method">
  <h2>Method and sources</h2>
  <div class="foot">
    <p><strong>Built from</strong> the nine task-anchored lifecycle maps, each made in the frame of the Stripe map: {maps_list}. The <a href="README.md">companion README</a> lists the method, the sources and what is open. Nothing was added that is not in a map or a source note the map cites; where this page counts something (handoffs, sources), it says so.</p>
    <p><strong>Rows:</strong> the ten tasks every map used, from Stripe's whiteboard chain (Opportunity → Problem → Goal → Intent → Plan, then Code) extended with review, release and operate, plus Test from the Ramp map. Where a map placed something inside an existing row (Intercom's QA sessions under review, Anthropic's evals under intent, Atlassian's Planner across intent and plan, Spotify's verifiers and Block's Gosling tests under review and operate), this page follows the map.</p>
    <p><strong>Handoffs:</strong> taken from each map's handoff table. A pair with no row is shown as unknown and says “no row in the map”. The Stripe map has no counts; the counts here are ours (nine handoffs: seven documented, one inferred, one unknown).</p>
    <p><strong>Related:</strong> <a href="../research-agent-runtime-patterns-taxonomy/01-synthesis.md">runtime-patterns synthesis</a> (patterns and Geoff's answers) · <a href="{DIM}">options register</a> · <a href="../../research/THEMES.md#opportunity-to-code-chain-opportunity--problem--goal--intent--plan--code">theme: opportunity-to-code chain</a> · <a href="../user-story-mapping/INDEX.md">user stories</a> (S05 is the reference workload) · <a href="../teardowns-to-pattern-classes/00-mapping.md">teardowns mapped to pattern classes</a> · <a href="../pdlc-maps-per-ecosystem.md">the maps' task note</a> · the <a href="../research-airbnb-spotify-product-practices/00-brief.md">Airbnb and Spotify brief</a> and the <a href="../research-block-product-practices/00-brief.md">Block brief</a>.</p>
    <p>Standalone HTML, inline styles, no scripts, no web fonts. Generated by <code>index.build.py</code> in this folder.</p>
  </div>
</section>
</div>
</body>
</html>
"""
    return html


if __name__ == "__main__":
    OUT.write_text(page(), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")
