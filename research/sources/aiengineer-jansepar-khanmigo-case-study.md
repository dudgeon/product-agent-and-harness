---
title: "Scaling AI in Education: A Khanmigo case study"
source_url: https://www.ai.engineer/talks/scaling-ai-in-education-a-khanmigo-case-study
author: Shawn Jansepar (Director of AI and Learning, Khan Academy)
publisher: AI Engineer World's Fair 2024 (talk page with transcript and updates)
published: 2024-06
retrieved: 2026-10-25
type: video
evidence: vendor-claim
filed_by: research-skill-rigidity-spectrum
themes: [human-thinking-skills, rules-vs-judgment-encoding, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
The most detailed first-party account of how a Socratic stance is engineered in a shipped product: Khanmigo does not intervene until the student submits, infers how the student reached their answer before deciding how to tutor, delegates arithmetic to code, and refuses to write the next paragraph of an essay until there is a strong thesis. It also shows the costs: latency from chained calls, uneven eval coverage, AI graders catching maths errors only about 70% of the time, and no measured learning gains reported. A PM harness that wants an "ask, don't draft" mode has a worked template and a list of what it will have to build.

## Themes
- human-thinking-skills: side-by-side example where ChatGPT accepted a wrong distribution of -4(2-x) and solved on, while Khanmigo flagged the step and asked a question to steer back; writing coach "refuses to write the next paragraph" until the thesis is strong (talk).
- rules-vs-judgment-encoding: the stance is implemented as staged prompting (infer the student's path, then a separate call decides how to tutor), hard guardrails (no essay writing; flag sudden 50-word pastes), and code delegation for maths; a mix of model judgment and deterministic checks (talk).
- evals-autonomy-trust: a tutoring-accuracy dashboard tracks quality across prompt and model changes; test coverage was deep for maths and thin elsewhere; model-graded evals in progress (talk).

## Key points
- Tutoring is embedded in exercises; after an incorrect submission the student can ask for help and Khanmigo receives the question, the worked solution and the student's entry.
- Teachers can review conversation history; inappropriate conversations notify the teacher.
- Operational: dedicated OpenAI capacity provisioned for peak, idle at night; added UI to show work in progress because chained calls slowed responses.
- Third-party critiques (search snippets only, not verified): Dan Meyer's 2024 analysis of a slope/intercept example where Khanmigo asked a generic question instead of acknowledging the correct part; reports of students abandoning sessions when denied direct answers.
- My judgment: Khanmigo's "do not intervene before submission" is the tutoring analogue of Buçinca's "human decides first, then AI" forcing function.

## Could not verify
- Talk date beyond "2024"; the last 5,000 characters of the page; the third-party critiques (pages rate-limited).
