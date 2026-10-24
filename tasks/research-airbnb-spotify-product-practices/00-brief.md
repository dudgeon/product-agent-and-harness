# How Airbnb and Spotify run product, and where agents sit in it

Date: 2026-10-24. Worker brief for [research-airbnb-spotify-product-practices](../research-airbnb-spotify-product-practices.md).

Built from 90 new source notes in [`research/sources/`](../../research/sources/) (themes in [research/themes/research-airbnb-spotify-product-practices.md](../../research/themes/research-airbnb-spotify-product-practices.md)) plus five Spotify notes filed earlier by other tasks. Companion files:
- [01-pdlc-airbnb.md](01-pdlc-airbnb.md) / [.html](01-pdlc-airbnb.html): Airbnb lifecycle map.
- [02-pdlc-spotify.md](02-pdlc-spotify.md) / [.html](02-pdlc-spotify.html): Spotify lifecycle map.
- [options/contributions/research-airbnb-spotify-product-practices.md](../../options/contributions/research-airbnb-spotify-product-practices.md): register proposals.

**Evidence labels.** Each claim carries one of these labels and a date:
- **FP**: first-party. The company describes itself (blogs, earnings calls, leaders' interviews).
- **VC**: vendor claim. A vendor's customer story, or a talk hosted by a vendor.
- **IND**: independent (journalism, critics).
- **ANEC**: anecdote (one ex-insider).

About 80% of the notes are FP. No independent source checks any AI adoption or outcome figure for either company.

## 1. The short version

1. **Both companies pulled decisions up after a period of team autonomy.**
   - Airbnb did it in 2020: one roadmap, a functional org, the CEO as "chief editor".
   - Spotify did it in 2023: autonomy moved from squads to VPs, and the co-presidents (co-CEOs from 2026) stack-rank 30–50 bets every six months.
   - In both, the research → intent → plan seam is carried by a senior person, not an artifact. At Airbnb it is the CEO in every review; at Spotify it is the VP who pitches the bet.
2. **Both are deep into agents for building, and thin on agents for deciding.**
   - Airbnb claims ~60% of code AI-written or co-authored (2026, FP); Spotify claims 73–76% AI-authored PRs or more PRs (2026, FP/VC).
   - Each runs its own harness over vendor agents (AirChat; Honk and Xirp).
   - Neither has an agent that sets goals or carries a bet's evidence into the work. Both name the gap themselves.
3. **Each has a distinctive asset the other mapped ecosystems lack.**
   - **Spotify: a systems context layer.** Backstage/Portal makes owners, lineage, standards, docs and even skills into owned entities that agents query (2025–26, FP).
   - **Airbnb: evidence carried by evals.** Research taxonomies become datasets and evals for AI features, and PMs label golden sets (2026, FP).
4. **The intent artifact differs sharply.**
   - **Airbnb** starts from a story (press release, keynote) and, since 2026, a short agent-drafted concept brief plus many prototypes.
   - **Spotify** built a sequence of evidence-carrying artifacts (DIBB brief 2016, Thoughtful Execution tree 2020, Understand It Brief and Scorecard 2021). It kept them optional, and they don't appear in today's process.
   - **Spotify's best agent-ready intent is on the engineering side**: versioned prompts with "done" defined as tests.
5. **Verification, not generation, is the new limit,** and both say so.
   - Spotify's merged changes roughly doubled year over year, and "the next constraint became our ability to verify it" (Sep 2026, FP).
   - Airbnb's platform lead predicts "overwhelming code review" (Jun 2026, FP).

## 2. Airbnb

### Operating model and roles: who decides what

| When | What changed | Evidence |
|---|---|---|
| Before 2020 | About 10 divisions, "very much run by product managers"; many A/B tests; teams differed | [Decoder 2021](../../research/sources/verge-decoder-chesky-2021-functional-org.md) (FP, Nov 2021); [Config 2023](../../research/sources/figma-config-2023-brian-chesky.md) (FP) |
| 2020 | COVID: business fell 80% in eight weeks; 25% layoff; divisions closed; functional org (design, engineering, product marketing, marketing, comms, ops); 10–20% of projects kept; one roadmap | [Decoder 2021](../../research/sources/verge-decoder-chesky-2021-functional-org.md); [Lenny's Podcast](../../research/sources/lenny-podcast-brian-chesky-new-playbook.md) (FP, Nov 2023) |
| 2020–23 | The classic PM role removed. Senior PMs became product marketers ("product management minus program management plus some outbound marketing"); most others became program managers. Design led by an ex-Apple creative lead; UX writing a separate function | [Config 2023](../../research/sources/figma-config-2023-brian-chesky.md); [Decoder 2024](../../research/sources/verge-decoder-chesky-founder-mode-2024.md) (FP, Oct 2024) |
| 2024 | A business counterpart to each product marketer (model, pricing, countries) in the Chief Business Officer's org. "Founder mode": all VPs dual-report to the CEO, who is co-hiring manager | [Decoder 2024](../../research/sources/verge-decoder-chesky-founder-mode-2024.md); [Paul Graham](../../research/sources/paulgraham-founder-mode.md) (IND, Sep 2024) |
| 2024–26 | "Project Hawaii": small mission teams with one metric mandate ship hundreds of small changes. This became the company "blueprint" | [Q4 2025 call](../../research/sources/airbnb-earnings-q4-2025.md) (FP, Feb 2026) |
| 2026 | New CTO (Ahmad Al-Dahle, ex-Meta Llama lead, from January). "Inside-out" AI: change how Airbnb builds first. Smaller pods, organised by outcome. The engineer–product line may disappear. The CEO is still "editor-in-chief" (Oct 2026) and is reportedly starting a separate AI lab | [Latent Space](../../research/sources/latent-space-airbnb-al-dahle-inside-out-ai.md) (FP, Oct 2026); [Al-Dahle essay](../../research/sources/medium-al-dahle-future-of-software-engineering.md) (FP, Feb 2026); [Semafor](../../research/sources/semafor-chesky-new-blueprint-2026.md) (IND, Oct 2026); [Fortune](../../research/sources/fortune-chesky-new-ai-lab.md) (IND, Jun 2026, anonymous sources) |

**How decisions are made.**
- Leaders speak first, the CEO decides, and he agrees "ninety percent of the time".
- Under the "golf instructor" model, he watches every swing and lets go as trust builds; press releases went from ~70 revisions to ~3 ([Decoder 2024](../../research/sources/verge-decoder-chesky-founder-mode-2024.md)).
- Principles are not written. They live in "one shared consciousness" of the top 60–70 people (same source).
- An ex-insider says it was less top-down than it looks, because the CEO asked questions and changed his mind. But requiring senior people in every detail "could slow it down" ([Loktev](../../research/sources/lenny-podcast-vlad-loktev-airbnb.md), ANEC, Sep 2024).
- Critics ask whether wartime practices work in peacetime, and who tells the CEO when they stop working ([Cutler and Perri](../../research/sources/cutler-perri-tbm-255-new-airbnb.md), IND, Nov 2023).

### Process and artifacts

- **Planning.**
  - A rolling two-year roadmap kept by the CEO: "If it's not on the roadmap, it can't ship".
  - Annual planning shrank to "just a budgeting cycle"; metrics are "subordinate to the calendar" ([Config 2023](../../research/sources/figma-config-2023-brian-chesky.md); [Lenny's Podcast](../../research/sources/lenny-podcast-brian-chesky-new-playbook.md)).
- **Reviews.**
  - Every project is reviewed every 1, 2, 4, 8 or 12 weeks, and the head program manager scores it green, yellow or red.
  - The CEO sees a weekly "semi-assembly" of the product ([Lenny's Podcast](../../research/sources/lenny-podcast-brian-chesky-new-playbook.md) 28:39).
  - Design reviews must discuss impact ([Teo Connor](../../research/sources/designweek-teo-connor-new-airbnb-app.md), FP, May 2025).
- **Intent artifacts.**
  - The story, keynote or press release, worked "months ahead" with comms ("the story will often dictate the product").
  - The "Airbnb Blueprint" storyboard of every screen and policy, combined with 20M support calls into a fix map.
  - Since 2026, a short "concept brief" drafted by the AirChat app Pascal, followed by 5–10 high-fidelity prototypes ([DX talk](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md), FP/VC venue, Jun 2026).
- **Launch.**
  - Two releases a year (May and autumn) from 2021 to 2025 packaged about 80% of product work ([Config 2023](../../research/sources/figma-config-2023-brian-chesky.md)).
  - From 2026: "We ship the moment it's ready", with May kept as a showcase ([Q4 2025 call](../../research/sources/airbnb-earnings-q4-2025.md)).
  - AI features roll out by traffic slice, opt-in toggle, then expansion ([Q2 2026 letter](../../research/sources/airbnb-earnings-q2-2026.md)).
- **Measurement and records.**
  - Minerva: 12,000+ certified metrics defined in GitHub, feeding experiments and executive reports ([Minerva](../../research/sources/airbnb-tech-minerva-metric-consistency.md), FP, 2021).
  - Experiment guardrails: about 25 escalations a month, about 5 stopped ([guardrails](../../research/sources/airbnb-tech-designing-experimentation-guardrails.md), FP, 2021).
  - The Knowledge Repo: research posts in Git, peer-reviewed by pull request ([Knowledge Repo](../../research/sources/airbnb-tech-scaling-knowledge-knowledge-repo.md), FP, 2016).
  - Leadership decisions are not recorded.

### AI and agents across the lifecycle

| Tool | Task | What it is | Numbers (who claims, when) |
|---|---|---|---|
| **AirChat** | Write code; also SDK apps for all functions | Internal harness: IDE plugins, a CLI wrapping Claude Code and Codex behind one gateway, default MCPs, a plugin/skill marketplace, an SDK (~40 apps), AirChat Remote for async runs in isolated cloud workspaces; multi-model (one model generates, another critiques) | 97% weekly / 90% daily agentic use; PR throughput +65%; 59% of code "primarily AI-authored" against a ~27% vendor benchmark; ~6 h a week saved; agentic users ≈ 2× the ~2,000 developers (Airbnb via DX, Jun 2026, FP/VC) |
| **Insight Miner** | Research the problem | A chat agent wrapped in a shared method package (extract, embed, cluster, hard-example mining). Each run can improve the package | Dozens of teams; more non-technical users than technical; months of work become days (Sep 2026, FP) |
| **Pascal** | Shape intent | Drafts a concept brief from market research, roadmap and objectives | No numbers; no technical detail (Jun 2026, FP) |
| **Everest** | Plan, operate | LLM- and embedding-built org context graph across the codebase | Groceries' learnings said to cut airport pickup to ~6 weeks from 9 months (Oct 2026, FP) |
| Migration framework | Write code | Validate, transform, validate loop; grew from the Enzyme→RTL test migration | ~3,500 files in 6 weeks vs a 1.5-year estimate (Mar 2025, FP); "dozens" of migrations, ~5× faster (Jun 2026) |
| @generateMock | Shape intent, test | Gemini inside GraphQL codegen fills prototypes and tests with realistic data from a design URL | 700+ mocks merged (Nov 2025, FP) |
| Eval stack | Set the goal, operate | Goals and gates fixed up front; PM-labelled golden sets; calibrated judges; 5% of production sampled daily; weekly PM review; evals from weeks to a day | (Jul 2026, FP) |
| AI support agent | Operate | Customer-facing; built on 13 models, heavy use of open models (Qwen) | Resolved without a human: ~1/3 (Feb 2026) → >40% (May) → ~45% (Aug) → "roughly half" (Oct); support cost per booking −16% (Q2 2026). All Airbnb's own, with the base changing over time |
| Agent-in-the-Loop | Operate → model | Human support agents' in-workflow choices retrain the model weekly (from ~3 months) | +11.7% recall, +8.4% helpfulness (Oct 2025, FP paper) |

**Company-level claims.**
- Features shipped up ~80% in H1 2026.
- Concept-to-launch up to 60% faster on key initiatives ([Q2 2026 letter](../../research/sources/airbnb-earnings-q2-2026.md), FP, Aug 2026).
- "AI writes 60% of its code" ([TechCrunch](../../research/sources/techcrunch-airbnb-ai-writes-60-percent-code.md), IND, May 2026, repeating Airbnb).
- Over 80% of engineers use AI tools, which the CEO calls a "vanity metric" (Feb 2026).

**Adoption model.**
- The platform team says AirChat spread organically: champions, train-the-trainer, no quotas, no performance-review link ([DX talk](../../research/sources/dx-airbnb-beyond-the-cli-airchat.md)).
- The CEO says he told the company "AI is an existential risk to us", tracks token use, and says AI winners will run in "founder mode" ([Q2 2026](../../research/sources/airbnb-earnings-q2-2026.md); [Fortune](../../research/sources/fortune-chesky-ai-60-percent-code-founder-mode.md), IND, Aug 2026).
- Mandate and organic spread coexist.

## 3. Spotify

### Operating model and roles: who decides what

| When | What changed | Evidence |
|---|---|---|
| 2012–14 | Squads of fewer than 8, each a "mini-startup". The product owner owns "what", the chapter lead "how"; tribes ~100 people. "Aligned autonomy": leaders say what and why, squads decide how | [Kniberg and Ivarsson](../../research/sources/kniberg-ivarsson-scaling-agile-spotify.md) (FP, 2012); [Engineering Culture](../../research/sources/kniberg-spotify-engineering-culture-part-1.md) (FP, 2014) |
| 2014–16 | A study finds misalignment and work-in-progress overload. "Spotify Rhythm": bets argued with DIBB, stack-ranked on open boards (company quarterly, product every 6 weeks) | [Rhythm](../../research/sources/kniberg-spotify-rhythm.md) (FP, 2016); [Don't Copy the Spotify Model](../../research/sources/infoq-dont-copy-spotify-model.md) (IND, 2016) |
| 2016–22 | Critics: the model was aspirational; PMs had no accountable engineering peer; no cross-team process; the alignment half "was never written" | [Jeremiah Lee](../../research/sources/jeremiahlee-failed-squad-goals.md) (IND, ex-PM, 2020) |
| 2023 | Most product and engineering centralised under Söderström (co-president, CPO/CTO) because teams spent "far too much time syncing on slightly different strategies". Three layoff rounds, the last ~17%. "Moved away" from squads: teams 2–3× larger, autonomy at VP level, an Apple-like centralised model so the app doesn't "ship the org chart" | [Jan 2023 changes](../../research/sources/spotify-newsroom-january-2023-org-changes.md) (FP); [Ek memo](../../research/sources/spotify-ek-memo-december-2023-layoffs.md) (FP); [Lenny's Podcast](../../research/sources/lenny-podcast-gustav-soderstrom-scaling-spotify.md) (FP, May 2023) |
| 2025 | About 14 VPs pitch bets "as if … a VC"; the co-presidents stack-rank 30–50 (44 that cycle); teams staff from the top down. A weekly 3-hour E-Team; nobody blocked more than ~2.5 days. Six months of prototyping before each cycle | [Invest Like the Best](../../research/sources/colossus-ilb-gustav-soderstrom-how-spotify-thinks.md) (FP, May 2025; third-party transcript) |
| 2026 | Söderström and Norström co-CEOs, Ek executive chairman. "We're retooling the entire company"; "when you have productivity on tap, what you need to have are very good plans". Still six-month cycles (Oct 2026) | [newsroom](../../research/sources/spotify-newsroom-ek-executive-chairman.md) (FP); [Q4 2025 call](../../research/sources/spotify-q4-2025-earnings-call.md) (FP, Feb 2026); [Q3 2026 call](../../research/sources/spotify-q3-2026-earnings-call.md) (FP, Oct 2026) |

What changed for PMs after 2023 is not documented. No source covers ladders, titles or ratios. The signals:
- "fewer overhead roles";
- PMs and designers prototyping in Cursor and Claude Code;
- PMs making small changes through Honk;
- a platform PM saying strategy is set centrally and teams are "autonomous with how" ([DX podcast](../../research/sources/dx-podcast-nils-loodin-platform-pm-spotify.md), FP, undated).

### Process and artifacts

- **Planning.** Six-month bets with about two weeks of planning; an internal planning tool (2023–26, FP).
- **Intent artifacts, by era:**
  - the DIBB two-page bet brief, with sponsor, success metrics and related bets ([Rhythm](../../research/sources/kniberg-spotify-rhythm.md), 2016);
  - the Thoughtful Execution tree: goal → data and insights → opportunities → hypotheses → solutions → learnings. It was the only mandatory step in Growth ([Thoughtful Execution](../../research/sources/spotify-design-thoughtful-execution-framework.md), 2020; the page now 404s);
  - the Understand It Brief and a Scorecard with role-owned gates ([Scorecards](../../research/sources/spotify-design-scorecards-alignment.md), 2021).
  - All lived in Google Docs, Figma and MURAL. None appears in the 2025 account of the bets process.
- **Engineering decisions.** RFC then ADR, used by "a handful of teams" in 2020 ([ADR post](../../research/sources/spotify-engineering-when-to-write-adr.md)). Docs as code in TechDocs, tied to catalog ownership ([TechDocs](../../research/sources/backstage-announcing-techdocs.md), 2020).
- **Experiments.**
  - Confidence encodes a default ship rule: the success metric up, guardrails non-inferior, quality checks passing ([risk-aware](../../research/sources/spotify-engineering-risk-aware-product-decisions.md), FP, 2024).
  - Every test is labelled ship, abort or iterate. About 12% win and about 64% yield learning; experimenting teams grew from ~40 to ~300 ([Experiments with Learning](../../research/sources/spotify-engineering-experiments-with-learning.md), FP, Sep 2025).
- **Launch.** Release trains, toggles and gradual rollout ([Engineering Culture](../../research/sources/kniberg-spotify-engineering-culture-part-1.md)). Auto-merge for safe fleet changes.

### AI and agents across the lifecycle

| Tool | Task | What it is | Numbers (who claims, when) |
|---|---|---|---|
| **Honk** | Write code | Background coding agent on the Claude Agent SDK, replacing the script step of Fleet Management; started from Slack, GitHub, Jira; three tools only (verify, restricted git, allowlisted bash); hidden verifiers and a verification service before any PR; v2 adds shared sessions and team projects | 1,500+ merged PRs (Nov 2025, FP); 650+ a month and "up to 90%" time saved (VC, undated); 1,000 PRs took 3 months, later 10 days (QCon, Mar 2026, FP); LLM judge vetoed ~25% of sessions, later dropped |
| Fleet Management / Fleetshift | Plan, release | Deterministic targeting, scheduling, tracking; auto-merge | ~half of all PRs since mid-2024; 2.5M+ merged, most with no human (FP) |
| **Backstage / Portal** | Shared context | Software catalog: owners, lineage, standards, TechDocs; `AiResource` entities for skills and rules; MCP servers as API entities; MCP actions for agents | Portal GA Oct 2025 ([SD Times](../../research/sources/sdtimes-spotify-portal-ga.md), IND) |
| **AiKA** | Research, operate | Internal knowledge assistant since Dec 2023; MCP client and server | 1,000+ daily users, 25% of employees weekly (Apr 2025, FP); 86%+ of engineers weekly (undated marketing) |
| **Vedder** | Research, read data | Data assistant on expert-curated context clusters with health scores (filed earlier) | 2,100+ users, a quarter non-SQL (Jun 2026, FP) |
| **Xirp** | Write code, plan | Vendor-neutral multi-agent sessions (Claude Code, Gemini CLI, Codex); catalog context in, transcripts back to Portal; model routing by price | "Thousands" of engineers, 36,000+ sessions (Aug 2026, FP; a trade report says 1,300+) |
| Prototypes and app store | Shape intent | End-to-end prototypes in the real apps by anyone up to the co-CEOs; Cursor and MCP for PMs and designers | "An hour or two" per prototype; no conversion data (VC, early 2026) |
| Confidence + LLM evals | Shape, operate | Evaluation funnel: offline evals pick treatments, A/B tests validate; LLMs can't replace users in A/B tests except under narrow assumptions (~39% of the effect recovered) | (May and Aug 2026, FP) |

**Adoption claims** (all Spotify's or Anthropic's; they conflict):
- 99%+ of engineers use AI weekly and PR frequency is up 76% ([Coding Is No Longer the Constraint](../../research/sources/spotify-engineering-coding-no-longer-constraint.md), FP, Jun 2026).
- 73% of PRs are AI-authored ([office hours](../../research/sources/claude-customers-spotify-office-hours.md), VC, early 2026).
- "Best developers haven't written a line of code since December" ([Q4 2025 call](../../research/sources/spotify-q4-2025-earnings-call.md); [TechCrunch](../../research/sources/techcrunch-spotify-best-developers-no-code.md), IND, repeating it; [heise](../../research/sources/heise-spotify-top-developers-no-code.md), IND, calls the framing promotional).
- Lines of code and PRs up ~100% with flat headcount ([Q3 2026 call](../../research/sources/spotify-q3-2026-earnings-call.md)).
- In May 2025 Söderström put the developer speed-up at only ~7% ([Invest Like the Best](../../research/sources/colossus-ilb-gustav-soderstrom-how-spotify-thinks.md)). The step change both Spotify and Anthropic cite is Dec 2025.

**Quality.**
- Merged changes went from about 8,100 to about 17,000 (August, year over year), and an auto-merged upgrade broke production.
- AI-written code was not found to be a material cause. The fixes were safeguards, rollback and changes scheduled in owners' hours ([Quality at Higher Velocity](../../research/sources/spotify-engineering-quality-at-higher-velocity.md), FP, Sep 2026).

**Productisation.** In October 2026 Spotify began selling Confidence, Portal and Xirp together as "Spotify Technology", an "R&D operating system" ([Spotify Technology](../../research/sources/spotify-engineering-introducing-spotify-technology.md), FP). Treat later Spotify posts as part marketing.

## 4. Where the two agree and differ

| | Airbnb | Spotify | Agree / differ |
|---|---|---|---|
| Who decides | CEO as chief editor; all projects reviewed by him on a cadence | VPs pitch; co-CEOs rank bets every six months; VPs explain in a weekly E-Team | **Agree**: decisions pulled up after a period of autonomy. **Differ**: one reviewer vs a ranked portfolio |
| PM role | Removed in 2020 and split into product marketer, program manager, business lead and designer | Trio of product, design and engineering; the PM is one evaluator among five; post-2023 changes undocumented | **Differ**: Airbnb redesigned the role; Spotify shrank overhead and kept the trio |
| Intent artifact | Story or press release; since 2026 a concept brief plus prototypes; evals for AI features | Historic evidence trees and briefs, kept optional; versioned prompts with tests for agent work; prototypes | **Agree**: prototypes now lead. **Differ**: narrative vs evidence tree |
| Cadence | Two releases a year → continuous shipping (2026) | Six-month bets, continuous shipping | **Agree**: continuous delivery under a slower commitment cycle |
| Context layer | Everest (LLM-built graph); Minerva metrics; decisions unwritten | Backstage/Portal catalog with owners and health; Vedder clusters; ADRs | **Differ**: Spotify's is curated and owned; Airbnb's is inferred and unpublished |
| Coding agents | AirChat over Claude Code and Codex; migration framework | Honk on the Agent SDK; Xirp over three vendors | **Agree**: own harness over vendor agents; Slack and remote async runs |
| Review | Engineer must explain the PR; one model critiques another; CEO reviews product | Hidden deterministic verifiers; LLM judge dropped; auto-merge for safe classes | **Differ**: Airbnb adds model critique; Spotify removed the judge in favour of tests |
| Research and data agents | Insight Miner (method harness), Datako | Vedder, AiKA | **Agree**: curated and owned beats mined (Vedder rejected 87.5% of mined examples; Insight Miner encodes expert method) |
| Evidence → plan | Through the CEO and through evals (AI features) | Through VPs; bet-to-PR linking "being built" | **Agree**: no artifact carries research evidence into the product plan |
| Adoption | "No mandate" (platform team) alongside CEO pressure | Mandate ("retooling the entire company") plus years of standardisation | **Agree**: top-down pressure plus a branded platform |
| Productisation | Knowledge Repo open-sourced (2016) | Portal, Confidence, Xirp sold (2025–26) | **Differ**: Spotify now sells its harness and context layer |

## 5. Contrasts with the other six mapped ecosystems

The six maps: [Stripe](../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md), [Ramp](../competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md), [Shopify](../competitive-teardown-shopify-river/01-pdlc-agent-ecosystem-map.md), [Anthropic](../research-claude-resources-articles/02-pdlc-agent-ecosystem-map.md), [Atlassian](../user-story-mapping/01-pdlc-agent-ecosystem-map.md), [Intercom](../research-pm-agents-jobs-to-be-done/04-pdlc-agent-ecosystem-map.md). The cross-ecosystem view is in [pdlc-cross-ecosystem-map](../pdlc-cross-ecosystem-map/README.md).

| Ecosystem | How the research → intent → plan seam is closed | Airbnb / Spotify contrast |
|---|---|---|
| **Stripe** | Role blur ("product hat" engineers); one named agent per task (Kai, Harbor, Orbit, Minions); Kai → Orbit undocumented | Both have named task agents too (Insight Miner, Pascal; Vedder, Honk). Neither relies on role blur: **Airbnb split roles further; Spotify kept the trio**. Spotify's Backstage plays the part Stripe's Toolshed and Trailhead play, but with ownership and lineage built in |
| **Ramp** | Shared multiplayer sessions on one harness (Glass, Inspect); the define → build "contract" named but not shown | Xirp is Spotify's closest analogue (sessions across vendors, transcripts back to the catalog). Airbnb's AirChat Remote is async but not described as shared. Like Ramp, Airbnb names its gap (brief drift) without a mechanism |
| **Shopify** | The public Slack thread is the handoff; public-by-default agent | Both use Slack as an agent front door (Honk; AirChat Remote triggers), but neither makes the thread the record. Spotify's record is the catalog; Airbnb's is the room |
| **Anthropic** | Public-by-default channels with a resident agent; one person carries research → plan | Airbnb's "shared consciousness" is the human version: a small group in the room instead of an open channel. Neither company is public-by-default for decisions |
| **Atlassian** | Linked work objects (ideas, goals, specs, work items); the work item carries the what, not the why | **Spotify is Atlassian's mirror image**: strong objects for *systems* (catalog), none for *work* (no idea, spec or goal object). Airbnb has the opposite of both: few objects, strong reviews |
| **Intercom** | One general harness plus hundreds of skills; intent re-captured at the PR ("why" in the description) and checked by reviewers | Spotify's prompt standard (end state, preconditions, done as tests) is the upstream counterpart to Intercom's PR "why". Airbnb requires the engineer to explain the PR, a human version of Intercom's check |

**What the two add to the cross-ecosystem picture.**
1. **A new seam location.** In the other six, the seam sits between peers (a researcher and a planner). At Airbnb and Spotify it sits at a leader: the CEO reviewing, or VPs pitching. That matters for regulated, hierarchical orgs, which look more like these two than like Stripe or Shopify.
2. **Spotify's catalog is the strongest "make the org legible" asset in the eight,** and it stops at the code.
3. **Airbnb's evals-as-evidence pattern** is the only documented artifact path from research to shaped intent in the eight. It exists only for AI features.
4. **Both are n=1 and CEO-shaped.** Cutler and Perri's "one company, one founder" warning applies to both.

## 6. Findings by project dimension

Each links to the register section; proposals are in the [contributions file](../../options/contributions/research-airbnb-spotify-product-practices.md).

- **[Intent shaping](../../options/DIMENSIONS.md#intent-shaping-and-spec-intent-shaping-mode-and-spec-standard).** Three intent forms are on show:
  - narrative-first (Airbnb);
  - an evidence tree with role-owned gates (Spotify 2020–21, kept optional);
  - a short brief plus prototypes plus evals (Airbnb 2026).

  Spotify's agent prompt standard is the most agent-ready spec in either company. *Proposed options:* narrative-first intent; opportunity tree as the intent record; agent-drafted concept brief plus prototypes.
- **[Context and memory](../../options/DIMENSIONS.md#context-and-memory-context-and-memory).** Spotify shows a software catalog as the agent context layer: owned, health-scored, queried over MCP, fed by session transcripts. Airbnb shows an LLM-built org graph (Everest) and a method package as shared memory (Insight Miner). Both leave product rationale and decisions out.
- **[Artifact and project structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found).**
  - The natural containers are the ranked bet (Spotify) and the roadmap row with a review schedule (Airbnb).
  - Experiment decision records are already structured in both.
  - Airbnb names brief-prototype-ticket drift as a live problem.
- **[Agent interface](../../options/DIMENSIONS.md#agent-interface-agent-interface-own-app-chat-or-embedded).** Both use many surfaces over one harness: IDE, CLI, Slack, a web app for async sessions, and MCP both ways.
  - Spotify prefers a CLI over MCP for large APIs.
  - Airbnb's leaders prefer visual, demo-able outputs to chat.
- **[Trust and privacy defaults](../../options/DIMENSIONS.md#trust-privacy-defaults-trust-and-privacy-defaults-for-sessions-and-context).**
  - Both isolate agent runtimes: Spotify's containers can't push; Airbnb's workspaces are network-isolated and production samples de-identified.
  - Gaps: Spotify's actions registry leaves permission checks to each tool, and Airbnb's CTO calls connector security for email and Slack unsolved.
  - Session-sharing defaults are not described for either.
- **[Review and autonomy](../../options/DIMENSIONS.md#review-and-autonomy-review-and-autonomy).**
  - Spotify: autonomy earned by hidden deterministic verifiers (judge dropped); auto-merge for safe classes, with fixes after an incident.
  - Airbnb: staged autonomy for AI features; the engineer must explain the PR; the CEO's review cadence for product.
  - Both: verification capacity is the new limit (new theme).
- **[Adoption](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model).**
  - Mandate and organic spread coexist at Airbnb.
  - Spotify's agents work because of years of standardisation done for humans: golden tech, catalog ownership.
  - Both had a three-year runway and a step change after a model release around December 2025.
- **[Target user](../../options/DIMENSIONS.md#target-user-which-users-and-personas-we-serve-first-including-for-shared-agents).**
  - Airbnb's "PM" is four people.
  - Spotify's seam owner is a VP.
  - Builders now include PMs, designers, managers, finance and ops (Airbnb: agent users ≈ 2× the number of developers).
  - Program managers' tracking and review prep may be the most automatable product work, but no source shows an agent doing it.

## 7. Could not verify, and gaps

- **No independent check of any AI number** for either company. Press (TechCrunch, Fortune) repeats company claims. Only heise questions Spotify's framing.
- **Definitions drift.**
  - Airbnb's "60%" is code share in one source and concept-to-launch time in another.
  - Its support-resolution base changes between quarters.
  - Spotify's adoption figures differ by source and date (73%, 76% and 60%; 99% and 96%).
- **Thin evidence on Airbnb's newest tools.** Pascal, Everest, the designer prototyping tool and the AI project coordinator have no technical detail. Each comes from one talk or interview.
- **Spotify's current product process.** The 2025 bets numbers come from a third-party machine transcript of a login-walled podcast. No source from 2024–26 covers PM role changes. Whether the Thoughtful Execution tree, Understand It Brief or Scorecard survive is unknown.
- **No source on AI in user research or customer interviews** at either company, beyond Airbnb's seed queries for search.
- **Not read:** Chesky's YC talk (not recorded); Söderström on Decoder (blocked); Spotify Design's newer posts (the blog now redirects); Into Design Systems on Spotify's Encore (paywalled; not subscribed).
- **Possible fix to another task's note** (not edited): [claude-customers-spotify-office-hours](../../research/sources/claude-customers-spotify-office-hours.md) is probably from January–February 2026, and its figures differ from Spotify's June 2026 post.
