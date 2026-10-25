---
title: "Claude's new constitution"
source_url: https://www.anthropic.com/news/claude-new-constitution
author: Anthropic
publisher: Anthropic
published: 2026-01-22
retrieved: 2026-10-25
type: article
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, standard-form-spectrum, human-judgment-pm-jobs]
relevance: medium
---

## Relevance to the project
Anthropic's explanation of why Claude's constitution favours cultivated judgment and explained reasons over rules, keeping rules only as a short list of hard constraints. It is the model-training analogue of the skill-authoring question and gives the clearest stated criteria for when a rule is worth its cost: severe error costs, unreliable judgment, or a need for firm commitments against manipulation. Those criteria transfer directly to deciding which PM-skill standards should be hard gates.

## Themes
- rules-vs-judgment-encoding: rules give predictability, transparency and testability but "can also be applied poorly in unanticipated situations or when followed too rigidly"; judgment adapts and weighs competing considerations at the cost of up-front predictability.
- rules-vs-judgment-encoding: rules are reserved for "hard constraints" (example: never give serious uplift to a bioweapons attack); per the constitution text (via search summary), clear rules make most sense "when the costs of errors are severe enough that predictability and evaluability become critical".
- rules-vs-judgment-encoding: rules can generalise badly into character: a footnote example says training "always recommend professional help" on emotional topics risks teaching the model to value ticking boxes over helping.

## Key points
- Stated aim (constitution text via search summary): understand situations well enough that Claude "could construct any rules we might come up with itself".
- Priority order for conflicts: broadly safe, broadly ethical, compliant with Anthropic's guidelines, genuinely helpful.
- Not meant as "a rigid legal document".
- Transfer to skills (my judgment): a skill that lists rules without reasons may teach the box-ticking behaviour the footnote warns about; reasons let the model apply the standard to unanticipated cases.

## Could not verify
- The full constitution text was not read; criteria for when rules make sense are from a search-result summary of the constitution page (anthropic.com/constitution), not read directly.

## Merged from a duplicate note of the same source (research-skill-rigidity-spectrum, 2026-10-25)

The same page was filed twice by two subagents; the second note is folded in here.

### Relevance to the project
The most prominent example of choosing explained principles over rules as the form of a standard, with the reasons stated. Anthropic says rules "can also be applied poorly in unanticipated situations or when followed too rigidly" and illustrates with a rule ("Always recommend professional help when discussing emotional topics") that would teach box-ticking over helping. It keeps a few bright-line hard constraints for the highest stakes and a priority order for conflicts. As a specimen for dimension 3 it is the far-right form: a long document of reasoning and heuristics, few hard rules, no scoring, and the expectation that the reader generalises. The same shape appears in Block's "write a constitution, not a suggestion" skill principle, though Block's version is a list of explicit constraints.

### Themes
- standard-form-spectrum: models should understand "why we want them to behave in certain ways", apply broad principles that generalise, and not follow rules mechanically; a hard-constraint list remains for "especially high-stakes behaviors" (named: no significant uplift to a bioweapons attack) (article).
- standard-form-spectrum: conflict ordering, broadly safe, broadly ethical, compliant with guidelines, genuinely helpful, with the reason that current models can err through mistaken beliefs or limited context (article).
- human-judgment-pm-jobs: the implicit claim is that judgment encoded as reasons transfers to new situations better than judgment encoded as rules (my reading).

### Key points
- The article offers "advice for how to deal with difficult situations and tradeoffs" and "heuristics" rather than worked cases; it does not show decisions step by step.
- Not framed as a legal document; the "brilliant friend" image is used for helpfulness.
- First-party description of a document whose effect on behaviour is not measured in the article.

### Could not verify
- The full constitution PDF was not read; worked examples it may contain are not confirmed.
