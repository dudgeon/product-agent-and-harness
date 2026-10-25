---
title: 'Product Manager Practices for Delegating Work to Generative AI: "Accountability must not be delegated to non-human actors"'
source_url: https://arxiv.org/abs/2510.02504
author: Mara Ulloa, Jenna L. Butler, Sankeerti Haniyur, Courtney Miller, Barrett Amos, Advait Sarkar, Margaret-Anne Storey
publisher: arXiv (cs.SE preprint; authors at Microsoft, some also Northwestern, CMU, University of Victoria)
published: 2025-10-02
retrieved: 2026-10-24
type: paper
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
filed_note: re-check 2026-10-24
themes: [pm-ai-usage-surveys, human-judgment-pm-jobs, pm-persona-role-expansion, prd-agents]
relevance: high
---

## Relevance to the project
The only empirical study in the set that both surveys a large PM population and checks self-report against telemetry, and it asks the question the jobs map needs: which PM tasks do PMs actually hand to GenAI, and why not the rest. It is first-party (Microsoft researchers studying Microsoft PMs at a company that sells Copilot and pushes adoption), so adoption rates are an upper bound, not a market norm. Its delegation framework (identity, accountability, social dynamics) is a usable design input for which PM-agent outputs need a human owner. Bears on the open question of automatable versus judgment-held PM jobs (J1, J4, J8).

## Themes
- **pm-ai-usage-surveys**: Survey of 885 of 5,111 PMs emailed (17%), telemetry for 731, 15 interviews, April to June 2025. 62% of ICs use GenAI daily or nearly daily; self-report correlates only moderately with telemetry (Spearman 0.37) (sections 3, 4.1).
- **human-judgment-pm-jobs**: Delegation is gated by accountability: low-accountability work (formatting meeting notes) is handed off, high-accountability work (specs, journey maps) is not (section 4.2).
- **pm-persona-role-expansion**: PMs report prototyping, writing SQL and scripts, and building agents; one participant describes PMs moving "down the stack" while engineers move up (sections 4.3, 5).
- **prd-agents**: Drafting or refining documents is the top IC use (73%), yet interviewees hold specs back as high-accountability work, which suggests AI drafts but PM owns (sections 4.1, 4.2).

## Key points
- Method (section 3): concurrent mixed methods inside one Microsoft division; survey branched for ICs and managers; pilot with 44 PMs; reflexive thematic analysis of interviews and open-ended responses; IRB-approved. Sample is 83% IC, 60% male, 66% US.
- IC task use (section 4.1): drafting or refining documents 73%, summarizing documents 52%, brainstorming 35%, writing emails or external comms 33%, user research or data analysis 22%, prototyping or code 12%, learning a skill 9%. Managers use it mainly for performance evaluations (summarizing peer feedback, checking bias), feedback tone, planning, meetings and presentations.
- Benefits (4.1): 81% of ICs say it often saves time; 72% think it improves quality, but 56% say their effort has not fallen.
- Barriers (4.1): output quality or inaccuracy 47%, no time to experiment 37%, no relevant use case 19%, unclear privacy guidance 14%, training 14%. Managers cite time to experiment 55%, accuracy or bias 54%, workflow integration 51%.
- Selective delegation framework (4.2): before delegating, PMs check identity (does this encroach on who I am; writing and communication are identity-linked), accountability (who owns the outcome), and emotional or social effect; the same three values operate at team level (peer norms, anti-AI peers) and organisational level (being "customer zero"; 1 in 4 managers cite leadership pressure, some use is performative).
- Role change (4.3): fear of being outpaced by AI-using peers outweighs fear of replacement; some PMs worry about losing product judgment as they take on engineering-like work.
- Limitations (6): single, strongly pro-AI company; self-report bias. The paper does not give per-task delegation percentages beyond the use-case list.

## Notable quotes
- "accountability must not be delegated to non-human actors" (participant P640, title and section 4.2)

## Could not verify
- Read the arXiv HTML full text up to the reference list; the last ~6,000 characters (likely references and appendix) were not read. No peer-reviewed venue is stated.
- The use-case list is "what PMs use GenAI for", not time share across jobs; it does not map cleanly onto J1-J10.
