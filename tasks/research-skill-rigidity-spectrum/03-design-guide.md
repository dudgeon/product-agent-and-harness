# Designing a product-work skill or agent at a chosen point

Date: 2026-10-25. Filed by research-skill-rigidity-spectrum. A short practical guide, derived from [01-synthesis.md](01-synthesis.md); every recommendation there has a source, and the labels (first-party, independent, anecdote) carry over. This guide is this task's judgment about how to apply that evidence to product-management skills; nothing in it has been tested on PM work. Use with [02-dimensions.html](02-dimensions.html) to record the profile you choose.

## 0. Before you start: three declarations

1. **Which job is this skill doing?** Produce or act, enforce a standard, or up-level the person. The designs are opposite (deliver the answer vs withhold it), so a skill that tries to do all three does none well. If the work needs all three, that is two or three skills, or one skill with clearly separate steps. (Bastani's two arms; Track C.)
2. **What is the unit?** Walk the job as steps (gather, interrogate, draft, classify, decide). You will set the dimensions per step. A single rigidity setting for the whole skill will be wrong at most steps. (Anthropic's skill guide; Parasuraman's four stages; Track 6.)
3. **Where is this step relative to the model's competence, and does the person alone beat the model alone?** Inside the frontier and model-better: automate and audit. Outside the frontier or human-better: keep the person deciding and make the agent ask. Revisit on every model release. (BCG; Vaccaro.)

## 1. Path: set it per step

- **Write code for any step whose sequence must always hold** (collect sources before drafting, run the completeness check before asking for ratification). Make the model's steps nodes inside that scaffold. Give each loop an iteration cap and say what happens at the cap (hand back to a named person). (Stripe blueprints; Managed Agents outcomes.)
- **Leave the path to the model where it cannot be written down** (which sources to read, how to cluster feedback, what follow-up question matters). Give it a stopping condition rather than a step list. (Willison; Codex guidance.)
- **Consolidate a fiddly multi-step procedure into one tool or script** rather than describing it in prose, when it has to run the same way every time. (Anthropic tool guidance; Block's scripted scores.)
- **Expect the compensating structure to go stale.** Mark which steps are fixed because the work demands it (audit, permission, repeatability) and which are fixed because the model needed help; re-run the latter without the scaffold when the model changes. (Runtime synthesis F.2; Ramp Policy Agent.)

## 2. Check: decide where it fires, who judges, and whether it can fail open

- **Attach deterministic checks to the process artifact, not the content.** Required sections present, every claim has a source link, an owner is named on each open question, the decision record is current. These are cheap, honest and scriptable. (Protected branches; Codeminer42; agent teams.)
- **Build enforced checks fail-closed and before the side effect.** A hook that only warns, times out, or runs in parallel is advice, not a gate. Decide explicitly: blocking or advisory, before or after. (Hooks reference; OpenAI guardrails; LangGraph.)
- **Use a model judge for content, in a fresh context, with hygiene.** Give it the rubric and a reference example, swap order if comparing, use a different model family than the author, and route unstable verdicts to a person. Grade the outcome, not the path. (Managed Agents outcomes; Zheng; self-preference study; Anthropic evals post.)
- **Reserve the human for what only a human can judge, and make verification cheap.** Show the exact line and its source; batch the questions; keep review time per output within what the PM accepts. A review nobody can do is a gate that fails open. (Fok and Weld; Vasconcelos; human-agent teams.)
- **Let code decide when the human steps in,** keyed to action type (writes, publishes, commits money), an iteration cap or a risk category. Do not key it to the model's confidence score; a few self-rated categories are what shipped systems use. (12-factor; Devin; Ramp.)

## 3. Standard: pick the form by what you are protecting

- **For completeness and compliance:** checkable items, each pass/fail, with its reason attached. Scriptable where the artifact has a shape; otherwise a model check. (Ilgen; TICK.)
- **For quality:** criteria the judge reads holistically, written as self-contained statements and tagged by importance, with pitfall items for the things that look fine and are not. Do not sum weights. (Rubrics as Rewards; HealthBench.)
- **Do not write the rubric first.** Collect five to ten past artifacts the team agrees are good and bad; grade them pass/fail with written reasons; the criteria emerge from the reasons ("criteria drift"). Then write the items. Keep a consensus filter: criteria most reviewers agree on become the standard, contested ones stay as prompts for discussion. (Hamel; HealthBench Consensus.)
- **For disciplines the model skips** (ask before drafting, check the register before inventing a question, never write the ratification): short non-negotiable rules, with the model's own likely excuses rebutted. For everything else, explain the why; all-caps MUSTs on content are a yellow flag. (Superpowers; skill-creator; constitution.)
- **For taste:** anti-exemplars and forced choices, not positive exemplars. Name the defaults to refuse ("reads well but says nothing", "every goal a metric with no owner") and make the agent state what it changed and why. Positive exemplars converge the portfolio. (frontend-design; Doshi and Hauser; Anderson.)
- **Budget the encoding.** A graded rubric costs expert hours and tops out at expert-expert agreement. Prefer more cheap checks with slightly lower signal to one expensive one. (PaperBench; Anthropic "volume over quality".)

## 4. Rights: set them by task class, and separate duties

- **Name the Decider for each step,** and keep it a person for anything irreversible, accountable or outside the frontier. The agent is Recommender or Performer. (RAPID; Cagan's risk owners; Linear AIG.)
- **Separate shaper from ratifier.** Whoever asked the agent cannot approve its output alone; the authoring agent never grades its own work. (Copilot cloud agent; SDLC playbook.)
- **Start the agent on suggestions and earn autonomy with labels.** A weekly labelled sample of its calls, a slider raised when accuracy holds, tiered by environment or artifact state (draft vs published). (Ramp; SDLC playbook.)
- **Expect drift toward autonomy** from experienced users and vendor defaults. Design the engagement in (the questions, the forcing functions, the attest step) rather than relying on people keeping a manual mode. (Autonomy study; Dell'Acqua.)
- **State the headless fallback.** If the skill needs a live person (an interrogation, a ratification), say what it does when none is present: stop, or run to a stated floor and flag it. (Osmani.)

## 5. Stance: choose it by job, and write the asking rules down

- **Produce or act:** do, self-check in context, then a fresh-context reader; ask only below a confidence category; batch questions. (frontend-design; doc-coauthoring; Devin.)
- **Enforce:** check and challenge; point to the line; write the finding as the smallest question the owner has to answer. Aim a second critic at the first agent's recommendation, not at the person. (River; Chiang.)
- **Up-level:** ask before the person commits and ask after as questions, not conclusions; give hints and reasons, not the answer, while the goal is the person's judgment; coach with the expert move at the moment it applies. (Bastani; Danry; Gajos and Mamykina; Tutor CoPilot.)
- **Rules for asking that the good skills share:** one question at a time, with a guess and a confidence attached; every question tied to something specific in the work; an explicit stop or yes rule ("sounds good" is not yes); never ask what you can read; a written list of cases where asking would be paternalistic, and what the skill does instead. (discernment-nudge; Superpowers; Osmani.)
- **Slope friction to stakes.** Forcing functions (recommendation on demand, delay, decide-first) work and are disliked; use them only at the steps whose error cost justifies them. (Buçinca; Vasconcelos.)
- **Measure the stance, not only the output.** An up-level skill needs its own eval: did the person's answers change, did they catch what the agent planted, did the open-question register shrink. (SocraticLM's pedagogy rubric; Track C.)

## 6. Record: decide what the skill leaves behind and how it stays true

- **Produce the four roles explicitly:** the outcome (the spec), the why (decisions with reasons), the open (questions and assumptions with owners and blocking flags), and done (the definition of ready and the required checks). Put the deterministic checks on these, not on the prose. (Track D; PM write-spec; Torres.)
- **Keep decision records small, numbered, immutable and superseded rather than edited;** generate the index and leave superseded ones out so agents load less and read nothing stale. Mark accepted records binding and proposed ones as context. (Nygard; Davidson; Codeminer42.)
- **Add a freshness mechanism to every standing reference:** an owner, a revisit date, a drift check in CI, "AI checks, humans attest". A stale rule read by an agent is a wrong instruction. (Codeminer42; Google design docs.)
- **Check the work, not the ticks.** Somewhere a step verifies that the behaviour the checklist demands happened (the interview occurred, the source says that, the risk owner saw it), independent of the record of it. (Urbach; MAST.)
- **Fix the ritual, free the content.** Silent read, senior speaks last, alternatives required, a pre-mortem before ratification: these procedures are rigid and the content is open, and that is the pairing that lets a team hold a quality bar without scripting judgment. (Amazon; Google; Klein.)

## 7. Loop: pick the signal and the writer

- **Start with curated corrections, human-written:** a shared instruction file of mistakes, with the why. Then let the agent propose lines from transcripts and corrections, with a person approving. (Claude Code team; Devin; `/insights`; Warp.)
- **Add evals as soon as there is a standard:** ten to twenty trigger queries, five to ten graded examples, a regression suite the eval graduates into; re-run on every model release. (skill-creator; Anthropic evals; Ramp's five examples.)
- **Prefer prose diagnosis to scalar scores** as the improvement signal; the explanation of why is what makes feedback usable. (GEPA; Warp.)
- **Do not let the skill rewrite itself whole.** If an agent edits a skill or playbook, make the edits incremental deltas with a separate reflect and curate step, and keep a person on the merge. (ACE; Dynamic Cheatsheet's own limits.)
- **Keep the run-level loop and the skill-level loop apart.** "Iterate until the grader passes" is a gate; "the skill got better" needs an eval across runs.

## 8. Three reference profiles

| | Spec completeness checker (enforce) | Shaping interrogator (up-level) | Feedback triage (act) |
|---|---|---|---|
| Path | Fixed stages, applied at a pause point | Code-fixed question set, model follow-ups, human drives | Code scaffold, model nodes, iteration cap |
| Check | Fail-closed hook on sections, owners, sources; fresh-context grader on content | Human judges; agent lowers verification cost | Script and schema; model grader with hygiene; human sample |
| Standard | Checkable items read holistically, consensus-filtered, reasons attached | Stance as the standard; anti-exemplars for weak answers | Exemplars and references for the grader; thresholds |
| Rights | Policy per class; shaper cannot ratify | Human decides; agent recommends | Earned from labelled accuracy; sandbox |
| Stance | Check and challenge; smallest question | Ask before, ask after, coach; withhold | Do; ask below a category; batch |
| Record | Definition of ready; required checks | Open-question register; assumption map; decisions with reasons | Decision trace per item; generated index |
| Loop | Standard owner labels a sample; regression suite | Stance eval; team grading sessions | Execution feedback; eval set; weekly labels |

## 9. What to test first, if this were funded

1. Grade twenty past PRDs with three PMs, pass/fail with reasons, and see whether a checkable-items-read-holistically rubric reaches PM-PM agreement (the ceiling in HealthBench and MT-Bench). *Decides whether a PRD standard is encodable.*
2. Run the same shaping skill two ways on five live initiatives: deliver the draft vs interrogate first and withhold; measure the PM's changes and the open-question count. *Decides whether the up-level stance pays in product work, where no evidence exists.*
3. Build one gate both ways: a skill plus a fail-closed hook on the process artifact, and a deployed reviewer. Compare adherence and review time. *Answers Track 6's unmeasured question.*
