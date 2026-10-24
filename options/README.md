# Options register

Why this exists: the project's deliverable is a strategy deck that informs a **resource request** to go and do the hard work of picking the right pattern. It is not a PRD for one implementation. So the research is aggregated as a **menu of options, split by dimension**, with the **key questions** that would have to be answered to choose among them. Research that only recommends one answer, or only describes a landscape, is incomplete.

Where it sits: `research/` holds sources and themes (what we found). `options/` holds the menu (what we could choose, and what we'd need to know to choose). Findings link up from here to `research/sources/`.

```
options/
  README.md        this rule
  DIMENSIONS.md    the register: one section per dimension
```

## Terms

- **Dimension:** a choice axis the strategy will eventually have to take a position on, where the research shows more than one viable approach. Test: "could a sensible team go either way, and does the choice change what we build or fund?" Dimensions cover both **architecture/runtime** choices (where the agent runtime lives; who owns the harness; how capability is packaged; session persistence and sharing; how review is gated) and **user and product** choices (which users we serve; which jobs to automate first; how structured the work is; what outcome or value we target; how adoption happens). Dimensions come from the research, they aren't imposed on it; add one when a source or track surfaces a choice that isn't covered, and merge or split them as understanding improves.
- **Option:** one distinct way to go on a dimension (e.g. "meta-harness above existing harnesses"). Each option names real examples, what it gives you, what it costs or risks, and its maturity.
- **Key questions:** the unanswered questions whose answers would tell us which option is right *for us*: facts to establish (adoption, cost, security posture), user needs to learn, constraints to confirm, prototypes or tests that would settle it. Write them as concrete questions, with who or what could answer each (a user interview, a prototype, a vendor trial, a policy owner).
- **Not a recommendation.** Do not pick a winner. A lean may be noted ("evidence so far favours X, because Y") but the register's job is to make the choice well-informed and the cost of finding out visible. Say what would change the lean.

## `DIMENSIONS.md` format

One section per dimension:

```markdown
## <dimension-slug>: <Dimension name>
**Choice:** <the decision, in one sentence>
**Why it matters to the strategy:** <1-2 sentences>
**Related themes:** [[theme-slug]], ...   **Related dimensions:** [[dimension-slug]], ...

### Options
| Option | What it is | Examples | Gives you | Costs / risks | Maturity | Evidence |
|---|---|---|---|---|---|---|
| <name> | ... | ... | ... | ... | emerging / early-adopter / mainstream | [source](../research/sources/x.md) (vendor claim / independent / first-party) |

### Key questions to choose
1. <question> — *answered by:* <interview / prototype / trial / policy owner / more research> — *affects:* <which options>
2. ...

### Current lean (optional) and what would change it
### Added by: <task slug> on <date>
```

## Rules for every agent

1. **Read `DIMENSIONS.md` before you start and before you report.** Use an existing dimension and option before inventing one; the same idea under two names fragments the menu.
2. **Append, don't rewrite.** Add options, evidence rows and key questions to a dimension. If you think a dimension should be merged, split, renamed, or another agent's entry is wrong, say so in your report to the director. Several agents write here at once: make small Edits and re-read just before each.
3. **Every option needs evidence** linking to a source note in `research/sources/`, marked vendor claim, independent or first-party. An option with no source goes in under "Unsourced / to verify".
4. **Every dimension you touch must end with key questions**, not only a description. If you can't say what we'd need to learn to choose, say that explicitly as the first key question.
5. **Your deliverable has an "Options by dimension" section** that points at the dimension sections you added to (links, not copies), plus a short list of any new dimensions you propose.
6. **Cross-cutting questions** (a question that bears on several dimensions) go in the `## Cross-cutting key questions` section at the end of `DIMENSIONS.md`.
7. The director keeps `DIMENSIONS.md` coherent (merges, renames, a contents list at the top) and brings the decisions about structure to Geoff.
