---
title: "Entangled: Solving the Hairy Problem of Team Dependencies"
source_url: https://www.hanssamios.com/dokuwiki/_media/agile_2015_-_entangled_-_solving_the_hairy_problem_of_team_dependencies_troy_magennis_.pdf
author: Troy Magennis (Focused Objective)
publisher: Agile 2015 conference (slides hosted on Hans Samios' wiki)
published: 2015-08-01
retrieved: 2026-10-28
type: other
evidence: anecdote
filed_by: research-dependency-agent
themes: [dependency-value-evidence, coordination-cost-and-waiting]
relevance: high
---

## Relevance to the project
The original of the often-quoted claim that "each dependency halves your chance of on-time delivery". The slides show it is a teaching model, not a measurement: if each of n teams has an even chance of being on time, the chance that all are on time is 1 in 2^n (1 in 16 for four people meeting for dinner, 1 in 128 for seven team dependencies). It is a powerful illustration of why dependency count matters and should be cited as an illustrative model by a forecasting practitioner, never as an empirical rate (see quantify-why-dependencies-kill-deadlines for a vendor's data suggesting real drops are smaller).

## Themes
- dependency-value-evidence: "1 in 2n" (2 to the n) chance all dependencies are on time; "7 dependencies: 1 chance in 128" (slides 28-29); take-away: "Every dependency removed double your chance of on-time delivery" (slide 61).
- coordination-cost-and-waiting: "Delays are NOT CAUSED by the item being delayed, its caused by other factors that are unknowable (and unquantifiable) in advance. It's the start time we struggle to compute" (slide 31).

## Key points
- Defines dependency after Strode and Huff (2012): "progress of one action relies upon the timely output of a previous action, or the presence of some specific thing"; uses their knowledge, task and resource dependency types.
- Assumption behind the arithmetic: each dependency independently has a 50% chance of being on time.
- Other take-aways: "A single dependency reduce order options 50%, < 1% with 4"; prefer teams of up to 15 people "if it avoids even a single dependency"; visualise dependencies; manage team skill balance to avoid constraints.
- A worked example estimates 7 sequential sprint-long dependencies at 21 weeks and notes "50% teams will miss the expected time".

## Notable quotes
- "Every dependency removed double your chance of on-time delivery" (slide 61)

## Could not verify
- Conference date is approximate (Agile 2015, August). The slide deck is a third-party-hosted copy that the wiki attributes to Magennis's own resource link (bit.ly/SimResources); not checked against his site.
