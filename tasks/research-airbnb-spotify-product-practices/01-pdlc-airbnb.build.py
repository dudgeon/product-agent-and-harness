"""Build 01-pdlc-airbnb.html. Run: python3 01-pdlc-airbnb.build.py (from this folder or anywhere)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mapkit import page

S = '../../research/sources/'
def a(slug, label):
    return f'<a href="{S}{slug}.md">{label}</a>'

d = dict(
    page_title="Airbnb Lifecycle Map",
    eyebrow="Airbnb and Spotify research · lifecycle map by task · 24 Oct 2026",
    h1="Where Airbnb’s people and agents sit in the product lifecycle, task by task",
    lede="Anchored on tasks, not job titles: since 2020 Airbnb has had no classic PM. Product marketers, program managers, designers, a business counterpart and the CEO split the PM’s tasks between them. Each handoff is marked documented, inferred or unknown. Almost every figure is Airbnb’s own.",
    answer_h2="The prototype carries intent forward; the evidence and the decisions stay with people",
    answer_items=[
        "<strong>Intent starts as a story and a short brief.</strong> Product marketing writes the story or press release “months ahead” and the CEO edits it (Lenny’s Podcast, Nov 2023; Config, June 2023). Since 2026 a short “concept brief”, drafted by an AirChat app called Pascal from market research, the roadmap and business objectives, comes before many prototypes (DX talk, June 2026). Whether the brief cites its evidence is not described.",
        "<strong>Prototypes replace specs, and Airbnb names the drift itself.</strong> After prototyping, “the doc isn’t updated” and reviews happen out of order. A proposed “AI project coordinator” to keep brief, prototypes and Jira in sync is “early days” (DX talk).",
        "<strong>Decisions are made in reviews and kept unwritten on purpose.</strong> Every project is reviewed every 1–12 weeks and scored green, yellow or red. Leadership principles live in “one shared consciousness” of 60–70 people; there is no written list (Decoder, Oct 2024).",
        "<strong>Where evidence does travel by artifact, it travels as evals.</strong> For AI features, Insight Miner’s taxonomy of support situations became datasets and evals before launch; user-research seed queries became search training data; PMs label golden sets and gates are fixed up front (Airbnb Tech Blog, Jul–Oct 2026).",
    ],
    answer_note="<strong>Across people:</strong> Airbnb split the PM’s tasks across more people than Stripe or Intercom (product marketer, program manager, designer, business lead), so research → intent → plan is a cross-person handoff by design. Its bridge is not an artifact but a person: the CEO in every review. Everest, an org context graph, is the candidate machine carrier, but its inputs are not published.",
    diagram=dict(
        title="Airbnb’s product lifecycle by task, with the humans, agents and shared tools at each task and the handoffs between them",
        humans={0: ["CEO + top", "30–70 leaders"], 1: ["researchers,", "designers,", "the CEO"], 2: ["data science,", "ops, product", "insights"], 3: ["CEO, CFO,", "business lead;", "mission teams"],
                4: ["product mktg,", "designers,", "PMs, CEO"], 5: ["program", "managers;", "small pods"], 6: ["engineers,", "managers,", "non-engineers"], 7: ["CEO reviews;", "engineer must", "explain the PR"], 8: ["product mktg", "+ comms run", "the launch"], 9: ["data science;", "PM weekly", "eval review"]},
        human_accent=[1, 3],
        agents={2: ["Insight Miner", "research", "harness"], 4: ["Pascal brief;", "prototype", "tools"], 6: ["AirChat", "(Claude Code,", "Codex)"], 7: ["validation", "loops; model", "critiques model"], 9: ["evals 5%/day;", "on-call agents;", "support agent"]},
        lite={5: ["“AI project", "coordinator”", "(proposed)"]},
        auto={8: ["traffic slices,", "toggles,", "canary"]},
        shared="Everest org context graph · AirChat MCPs, skills and plugin marketplace · Minerva certified metrics · ERF experiments · Jira · Figma · one roadmap",
        links=[(2, 4, "doc", "taxonomy → datasets + evals"), (4, 6, "doc", "design URL → mocks; mockups → coding agents"), (6, 7, "doc", ""), (7, 8, "doc", ""), (4, 5, "gap", "brief, Jira drift"), (2, 5, "gap", "")],
        people_use=[2, 4, 6],
        up=[(6, "MCPs, skills")],
        down=[(9, "failures → new evals")],
        legend_doc="documented by Airbnb",
        legend_gap="research → plan and intent → plan: no carrier described",
        caption="Column headers are tasks; the row below them is the opportunity-to-code chain. Accent: tasks still done by people with no tool shown. Our own diagram, not Airbnb’s UI.",
    ),
    tasks=[
        ("Spot the opportunity", "CEO and top leaders; product marketing; the business (CBO) organisation", "None named. Inputs: support calls, social posts, Minerva metrics; Insight Miner taxonomies", "One rolling two-year roadmap (“if it’s not on the roadmap, it can’t ship”); the “Airbnb Blueprint” storyboard and fix map"),
        ("Talk to customers", "Researchers, designers, the CEO (“normal people we don’t pay”); leaders embedded in Paris for experiences", "No agent seen", "Research findings (format not described); ~500 seed queries for AI search"),
        ("Research the problem, read the data", "Data science, product-insights and operations teams, often non-technical", "<strong>Insight Miner</strong> (chat agent wrapped in a shared method package; dozens of teams); Datako for data questions; Minerva and ERF", "Taxonomies, prevalence estimates, datasets; Knowledge Repo posts (2016–21)"),
        ("Set the goal", "CEO with CFO and the business lead; mission teams with one mandate (“Project Hawaii”); an eval decision-maker for AI features", "None named", "Roadmap entry; revenue targets; eval goals and gates fixed up front"),
        ("Shape the intent", "Product marketer, designer and CEO; PMs and designers in pods", "<strong>Pascal</strong> drafts the concept brief; a designer prototyping tool; image-model mockups fed to coding agents; @generateMock fills prototypes with data", "Story or press release; short concept brief; 5–10 high-fidelity prototypes; PM-labelled golden sets"),
        ("Plan the change", "Program managers (timelines, coordination); smaller pods", "A proposed “AI project coordinator” (not built); Everest gives cross-codebase context", "Central project list with a review schedule; Jira; release calendar"),
        ("Write the code", "Engineers, plus managers returning to code and non-engineers", "<strong>AirChat</strong> CLI wrapping Claude Code and Codex; AirChat Remote for async runs; migration framework (validate, transform, validate)", "Pull requests; ~60% of code AI-authored (Airbnb, 2026)"),
        ("Review the change", "The CEO on a 1–12 week cadence; design reviews must discuss impact; engineers must explain AI PRs", "Validation loops (tests, lint, types, schema checks); one model generates, another critiques; ERF guardrails escalate ~25 experiments a month", "Review decisions (not recorded); approved PRs"),
        ("Release", "Product marketing and comms; the CEO keynote", "Small traffic slices, opt-in toggles, staged rollout by language, canary with auto-rollback", "Twice-yearly releases to 2025; since 2026 “we ship the moment it’s ready”, May as a showcase"),
        ("Operate and learn", "Data science; PMs in a weekly eval review; support agents", "Production evals on 5% of traffic daily; Agent-in-the-Loop weekly retraining; async on-call agents; the AI support agent (~45% resolved, Aug 2026)", "Dashboards, experiment results, new evals, retrained models"),
    ],
    handoffs=[
        ("Operate → spot the opportunity (Blueprint)", "20M support calls, social posts and a storyboard of every screen and policy combined into a prioritised fix map", "documented", False),
        ("Spot the opportunity, set the goal → roadmap", "Everything shipped must be on the one roadmap; the CEO adds and cuts items", "documented", False),
        ("Set the goal → shape intent (goal and gates)", "For AI features a decision-maker fixes goals and eval gates up front; PMs label golden sets", "documented", False),
        ("Set the goal → shape intent (business brief)", "A product marketer pairs with a business counterpart; the business model and product-marketing brief go to supply and international teams", "documented", False),
        ("Research (Insight Miner) → shape intent (AI support)", "Taxonomy and prevalence of support situations turned into datasets and evals before the 2025 launch", "documented", False),
        ("Talk to customers → shape intent (AI search)", "~500 seed queries from user research ground the synthetic training queries", "documented", False),
        ("Research, roadmap → shape intent (Pascal)", "Pascal drafts a concept brief from market research, the roadmap and business objectives; whether it cites sources is not described", "documented / mechanism unknown", False),
        ("Talk to customers → research (product work)", "People; no tool shown", "inferred", False),
        ("<strong>Shape intent → plan</strong>", "Prototypes replace long specs; Airbnb says the brief isn’t updated after prototyping and reviews go out of order; an AI coordinator is only proposed", "unknown", True),
        ("<strong>Research evidence → plan</strong>", "Nothing found carries research evidence into the brief, the Jira tickets or the plan", "unknown", True),
        ("Shape intent → write code", "A prototype’s design URL goes into the mock generator; the CTO feeds image-model mockups to coding agents", "documented", False),
        ("Plan → review", "Fixed cadence of CEO reviews with green, yellow or red scoring by the head program manager", "documented", False),
        ("Review decisions → later work", "Not written down; held in leaders’ heads (“shared consciousness”)", "inferred", False),
        ("Write code → review", "Validation loops before a PR; one model critiques another; a person must be able to explain the PR", "documented", False),
        ("Review → release", "Staged traffic slices and toggles; canary with auto-rollback for model patches; guardrails measured in shadow mode", "documented", False),
        ("Operate → evals", "Production failures become new evals in a weekly PM review", "documented", False),
        ("Operate → model", "Support agents’ in-workflow choices feed weekly model updates", "documented", False),
        ("Operate → next build (Everest)", "Groceries’ learnings said to make airport pickup take ~6 weeks; how learnings enter Everest is not described", "documented / mechanism unknown", False),
    ],
    counts="Counts: 18 handoffs: 14 documented (two with the mechanism unknown), 2 inferred, 2 unknown.",
    implications=[
        "<strong>The PM’s tasks can be split four ways and still need one carrier.</strong> Product marketer (story), program manager (plan), designer (prototype), business lead (model and pricing). A single “PM agent” would serve several people; a task agent per row fits better.",
        "<strong>The intent bundle is story + short brief + prototypes + evals, not a PRD.</strong> That favours the prototype-first and eval-as-spec options under intent-shaping-and-spec, with brief-to-prototype sync as the named open need.",
        "<strong>The review is the decision point, and it is unrecorded.</strong> An agent that prepares each review and records what was decided and why would fill a real gap, against a culture that prefers unwritten principles.",
        "<strong>AI-feature work already carries evidence by artifact (taxonomies → evals).</strong> That is the clearest pattern for carrying research into a plan, and it exists only where the product is itself an AI feature.",
    ],
    foot=("Sources: " + "; ".join([
        a("lenny-podcast-brian-chesky-new-playbook", "Chesky on Lenny’s Podcast (Nov 2023)"), a("figma-config-2023-brian-chesky", "Config 2023"),
        a("verge-decoder-chesky-founder-mode-2024", "Decoder (Oct 2024)"), a("verge-decoder-chesky-2021-functional-org", "Decoder (Nov 2021)"),
        a("lenny-podcast-vlad-loktev-airbnb", "Vlad Loktev (Sep 2024, ex-insider)"), a("dx-airbnb-beyond-the-cli-airchat", "DX talk on AirChat (Jun 2026)"),
        a("latent-space-airbnb-al-dahle-inside-out-ai", "Al-Dahle on Latent Space (Oct 2026)"), a("airbnb-tech-insight-miner-agent-harness", "Insight Miner (Sep 2026)"),
        a("airbnb-tech-eval-driven-development", "eval-driven development (Jul 2026)"), a("airbnb-tech-castle-nl-search", "CASTLE (Oct 2026)"),
        a("airbnb-tech-graphql-generatemock", "@generateMock (Nov 2025)"), a("arxiv-airbnb-agent-in-the-loop", "Agent-in-the-Loop (Oct 2025)"),
        a("airbnb-tech-designing-experimentation-guardrails", "experiment guardrails (2021)"), a("airbnb-earnings-q4-2025", "Q4 2025 call"), a("airbnb-earnings-q2-2026", "Q2 2026 letter"),
        a("cutler-perri-tbm-255-new-airbnb", "Cutler and Perri (independent, Nov 2023)"), a("semafor-chesky-new-blueprint-2026", "Semafor (independent, Oct 2026)"),
    ]) + ". Independent coverage is thin: press repeats Airbnb’s numbers unchecked. Full notes: 01-pdlc-airbnb.md in this folder."),
)
page(d, os.path.join(HERE, '01-pdlc-airbnb.html'))
