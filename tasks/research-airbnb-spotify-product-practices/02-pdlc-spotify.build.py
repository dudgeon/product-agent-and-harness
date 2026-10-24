"""Build 02-pdlc-spotify.html. Run: python3 02-pdlc-spotify.build.py (from this folder or anywhere)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mapkit import page

S = '../../research/sources/'
def a(slug, label):
    return f'<a href="{S}{slug}.md">{label}</a>'

d = dict(
    page_title="Spotify Lifecycle Map",
    eyebrow="Airbnb and Spotify research · lifecycle map by task · 24 Oct 2026",
    h1="Where Spotify’s people and agents sit in the product lifecycle, task by task",
    lede="Anchored on tasks, not job titles: Spotify moved from autonomous squads (2012) to VP-level bets ranked by the co-CEOs every six months (2023 on). Engineers supervise agents, and PMs and designers build prototypes in the real apps. Each handoff is marked documented, inferred or unknown. Almost every figure is Spotify’s own.",
    answer_h2="Spotify’s context layer carries systems, not reasons",
    answer_items=[
        "<strong>Agents get rich context about systems.</strong> The Backstage/Portal catalog (owners, lineage, standards, docs, even skills as owned entities) is exposed to agents over MCP. Xirp sessions start with catalog context, and transcripts flow back (Spotify Engineering and Portal blogs, 2025–26).",
        "<strong>The why behind a bet travels in people.</strong> About 14 VPs pitch bets “as if … a VC”, and the co-CEOs stack-rank 30–50 of them every six months. VPs must explain details themselves in a weekly E-Team (Söderström, May 2025). No source shows a written evidence brief in today’s bets process.",
        "<strong>Spotify had evidence-carrying intent artifacts, but kept them optional and off the platform.</strong> The DIBB bet brief (2016), the Thoughtful Execution tree (2020), and the Understand It Brief and Scorecard (2021) live in Google Docs, Figma and MURAL. None is linked into Backstage, the code or the bets record.",
        "<strong>The engineering intent artifact is strong; the product one is missing.</strong> A fleet change is a versioned prompt with the end state, preconditions, examples and “done” as tests (Honk, Nov 2025). Linking PRs to work items, A/B tests and user value is “what we’re trying to build right now” (chief architect, early 2026).",
    ],
    answer_note="<strong>Across people:</strong> since 2023 Spotify has put the research → intent → plan seam at the VP level. The VP is the carrier, and the six-month bets board is the commitment. The squads that research, shape and build sit below it. Leadership says plans are now the constraint (“when you have productivity on tap, what you need to have are very good plans”, Feb 2026), but its tooling investment is in systems context and verification, not in product rationale.",
    diagram=dict(
        title="Spotify’s product lifecycle by task, with the humans, agents and shared tools at each task and the handoffs between them",
        humans={0: ["~14 VPs", "pitch bets"], 1: ["user", "researchers"], 2: ["data science,", "research, PMs;", "non-SQL users"], 3: ["co-CEOs", "stack-rank", "30–50 bets"],
                4: ["PM, design,", "eng trio;", "all prototype"], 5: ["VPs staff;", "migration and", "library owners"], 6: ["engineers", "supervise; PMs", "small changes"], 7: ["code owners;", "migration", "driver"], 8: ["owning", "teams"], 9: ["experimenters;", "platform", "teams"]},
        human_accent=[1, 3],
        agents={2: ["Vedder (data);", "AiKA", "(knowledge)"], 4: ["Cursor, Claude", "Code prototypes;", "offline evals"], 6: ["Honk", "(Agent SDK);", "Xirp sessions"], 7: ["verifiers;", "verification", "service"], 9: ["Confidence", "ship rule;", "EwL labels"]},
        auto={5: ["Fleetshift +", "lineage", "(deterministic)"], 8: ["auto-merge", "if safe;", "toggles"]},
        shared="Backstage / Portal catalog (owners, lineage, standards, TechDocs, skills as entities) · MCP actions · Confidence · bet briefs and trees in Google Docs, Figma · Slack · Jira",
        links=[(5, 6, "doc", ""), (6, 7, "doc", ""), (7, 8, "doc", ""), (4, 6, "doc", "Slack → Honk; prototype app store"), (2, 5, "gap", "evidence → bet")],
        people_use=[2, 4, 6],
        up=[(6, "catalog context")],
        down=[(9, "decision records")],
        legend_doc="documented by Spotify",
        legend_gap="research evidence → bet and plan: carried by VPs, not artifacts",
        caption="Column headers are tasks; the row below them is the opportunity-to-code chain. Accent: tasks still done by people with no tool shown. Our own diagram, not Spotify’s UI.",
    ),
    tasks=[
        ("Spot the opportunity", "VPs and their teams (bottom-up bets); insights teams; leadership", "None named; Confidence sold as a “product intelligence layer”; LLMs proposed for screening weak ideas", "Bet pitch; DIBB data and insights (2016 form)"),
        ("Talk to customers", "User researchers (Product Insights)", "No agent found; diary studies, interviews", "Research findings"),
        ("Research the problem, read the data", "Data scientists with researchers; PMs; 2,100+ data-assistant users, a quarter non-SQL", "<strong>Vedder</strong> (expert-curated context clusters); <strong>AiKA</strong> (internal knowledge Q&amp;A since Dec 2023); behavioural proxies", "Answers with SQL and sources; sized opportunity statements"),
        ("Set the goal", "Co-CEOs (formerly co-presidents) rank bets; VPs write area strategy; teams set measurable goals", "Internal planning tool; bets board", "Six-month stack rank of 30–50 bets; “definitions of done”"),
        ("Shape the intent", "Product, design and engineering trio; everyone up to the co-CEOs prototypes", "Cursor and Claude Code prototypes in the real apps, shared in an internal app store; offline LLM evals pick treatments", "Thoughtful Execution tree, Understand It Brief, Scorecard (2020–21); prototypes; versioned migration prompts"),
        ("Plan the change", "Co-CEOs and VPs (bets, staffing); migration and library owners; advisory boards on golden tech", "Fleetshift targeting (deterministic); Backstage lineage; code search", "Six-month plan; target lists; golden-tech standards; RFCs and ADRs"),
        ("Write the code", "Engineers supervising agents; PMs for small changes", "<strong>Honk</strong> (Claude Agent SDK background agent, from Slack, GitHub, Jira); Claude Code; <strong>Xirp</strong> multi-agent sessions", "Pull requests (73–76% AI-authored or more PRs, Spotify’s figures)"),
        ("Review the change", "Code owners; Scorecard evaluators by role (2021)", "Hidden verifiers in the stop hook; a verification service runs real CI before any PR; an LLM judge (later dropped)", "Validated PR"),
        ("Release", "Owning teams", "Auto-merge for safe fleet changes; release trains, toggles, gradual rollout; builds to phones from Slack", "Merged change; app build"),
        ("Operate and learn", "Experimenters, platform and SRE teams, data science", "<strong>Confidence</strong> ship rule and Experiments-with-Learning labels; regression monitoring; monthly retros that tag AI’s part", "Shipping recommendation with reasons; ship/abort/iterate label; retros"),
    ],
    handoffs=[
        ("Talk to customers → research", "Diary studies and behavioural logs on the same users at the same time (one team, 2019)", "documented", False),
        ("Research → shape intent", "Thoughtful Execution tree (goal, insights, opportunities, hypotheses, solutions, learnings), then Understand It Brief, then Scorecard (2020–21); current use unknown", "documented", False),
        ("Research, insight → spot the opportunity, set the goal", "DIBB two-page bet brief on an open bets board (2016); current form unknown", "documented", False),
        ("Spot (VP bet) → set the goal, plan", "Pitch, then a global stack rank by the co-CEOs, then top-down staffing (2025)", "documented", False),
        ("Shape intent (prototype) → plan", "A prototyping phase before each cycle exposes conflicts between bets", "documented", False),
        ("<strong>Research evidence → bet and plan</strong>", "Not described as an artifact; VPs carry it and must “explain it yourself” in the E-Team", "unknown", True),
        ("<strong>Plan (bet) → agent work and back</strong>", "No link from a bet to the prompts, PRs or A/B tests that serve it; linking PRs to work items and user value is still being built", "unknown", True),
        ("Shape intent → write code", "PMs propose small changes through Honk from Slack; prototypes run in the real apps and are shared in an app store; prototype-to-ship conversion not reported", "documented", False),
        ("Shape intent (design) → write code", "Figma specs; named in 2021 as inconsistent, with motion hard to code", "documented", False),
        ("Plan (lineage) → write code (migrations)", "Backstage lineage → code search → Fleetshift scope → context file with mapping tables → Honk", "documented", False),
        ("Thread, ticket, PR comment → write code", "An interactive agent gathers task details, then hands a prompt to Honk", "documented", False),
        ("Shared catalog → agent session → catalog", "Xirp sessions start with catalog context; transcripts and metadata flow back to Portal", "documented", False),
        ("Write code → review", "Verifiers in the stop hook; a verification service runs real CI; only then a PR to code owners", "documented", False),
        ("Review → release", "Auto-merge for safe fleet changes; after an incident, more safeguards and changes scheduled in owners’ working hours", "documented", False),
        ("Release → learn", "Confidence’s default ship rule; every experiment labelled ship, abort or iterate", "documented", False),
        ("Shape intent (offline evals) → A/B test → fix", "An evaluation funnel: evals pick treatments, experiments validate, judge findings become fixes", "documented", False),
        ("Operate → shared knowledge", "AiKA usage leads teams to improve docs; fewer repeat questions", "documented", False),
        ("Learn → next six-month plan", "Learning rates reallocate testing bandwidth; whether results feed the next bets cycle is not described", "inferred", False),
    ],
    counts="Counts: 18 handoffs: 15 documented (three from 2016–21 with current use unknown), 1 inferred, 2 unknown.",
    implications=[
        "<strong>The best-built context layer in the eight maps, and it stops at the code.</strong> Catalog, lineage, standards and skills are owned entities agents can query. Product rationale (why this bet, on what evidence) is not one of them. A bet or brief as a catalog kind with an owner and lifecycle is the obvious extension, and nobody has built it.",
        "<strong>Spotify’s own history is a menu of intent artifacts.</strong> DIBB brief, Thoughtful Execution tree, Understand It Brief, Scorecard. All were optional “reminders” in an autonomy culture, which is a warning for any spec standard an agent would enforce.",
        "<strong>Engineering intent is agent-ready: end state, preconditions, examples, done as tests, versioned in Git.</strong> That is the strongest evidence for a spec standard with a verification contract.",
        "<strong>Verification, not generation, is now the limit.</strong> Merged changes roughly doubled year over year, and Spotify says “the next constraint became our ability to verify it”. Autonomy is earned by deterministic checks; the LLM judge was dropped.",
    ],
    foot=("Sources: " + "; ".join([
        a("lenny-podcast-gustav-soderstrom-scaling-spotify", "Söderström on Lenny’s Podcast (May 2023)"), a("colossus-ilb-gustav-soderstrom-how-spotify-thinks", "Invest Like the Best (May 2025)"),
        a("kniberg-spotify-rhythm", "Spotify Rhythm (2016)"), a("spotify-design-thoughtful-execution-framework", "Thoughtful Execution (2020)"), a("spotify-design-scorecards-alignment", "Scorecards (2021)"),
        a("jeremiahlee-failed-squad-goals", "Jeremiah Lee (independent, 2020)"), a("spotify-engineering-honk-part-1-1500-prs", "Honk parts 1–4 (Nov 2025–Apr 2026)"),
        a("infoq-qcon-spotify-ai-codebase-migration-agent", "QCon London talk (Mar 2026)"), a("spotify-engineering-coding-no-longer-constraint", "Coding Is No Longer the Constraint (Jun 2026)"),
        a("spotify-engineering-quality-at-higher-velocity", "Quality at Higher Velocity (Sep 2026)"), a("spotify-portal-blog-introducing-xirp", "Xirp (Aug 2026)"),
        a("spotify-engineering-vedder-context-layer", "Vedder (Jun 2026)"), a("spotify-engineering-risk-aware-product-decisions", "Confidence ship rule (2024)"),
        a("spotify-engineering-llm-evals-funnel", "evaluation funnel (May 2026)"), a("claude-customers-spotify-office-hours", "Anthropic office hours (vendor claim)"),
        a("spotify-q4-2025-earnings-call", "Q4 2025 call"), a("spotify-q3-2026-earnings-call", "Q3 2026 call"), a("heise-spotify-top-developers-no-code", "heise (independent, Feb 2026)"),
    ]) + ". Full notes: 02-pdlc-spotify.md in this folder."),
)
page(d, os.path.join(HERE, '02-pdlc-spotify.html'))
