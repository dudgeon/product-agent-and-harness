---
title: "Volere Requirements Specification Template, Edition 13"
source_url: https://www.cs.uic.edu/~i440/VolereTemplate.pdf
author: James Robertson and Suzanne Robertson (Atlantic Systems Guild)
publisher: Atlantic Systems Guild (copy hosted by the University of Illinois Chicago)
published: 2007-08-01
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [requirements-partitions, standard-form-spectrum]
relevance: high
---

## Relevance to the project
The most widely used practitioner requirements template, and the one that comes closest to a complete category list of what a feature carries: 27 numbered sections covering project drivers, constraints, functional and data requirements, nine families of non-functional requirement, and project issues. Two things matter for the taxonomy work. First, its non-functional families mix quality attributes (performance, security, usability) with obligation sources (legal requirements split into compliance with the law and compliance with standards, "an internal law imposed by your company"), which is the same two-axis tension the project's partition comparison is about. Second, every requirement carries a fit criterion, "a measure that lets you test whether the solution meets it", and the legal and standards sections name who validates: a lawyer's opinion, "the appropriate standard-keeper certifies".

## Themes
- requirements-partitions: section list: 9 functional and data; 10 look and feel; 11 usability and humanity (including 11e accessibility); 12 performance (speed, safety-critical, precision, reliability, capacity); 13 operational and environmental (including interfacing with adjacent systems, release); 14 maintainability and support; 15 security (access, integrity, privacy, audit, immunity); 16 cultural and political; 17 legal (17a compliance, 17b standards); 18 to 27 project issues including open issues, off-the-shelf solutions, new problems, migration, risks, costs, documentation and training, waiting room.
- standard-form-spectrum: each requirement has a fit criterion; 17b's fit criterion is "the appropriate standard-keeper certifies that the standard has been adhered to"; 17b's considerations: "it is not always apparent that there are applicable standards because their existence is often taken for granted".

## Key points
- Edition 13, August 2007; the template may be copied and adapted with attribution but not sold.
- Section 4 mandated constraints: solution constraints, implementation environment, partner applications, off-the-shelf software, workplace environment, schedule, budget.
- Section 17a compliance: "to comply with the law so as to avoid later delays, lawsuits, and legal fees"; the considerations list names data protection, Sarbanes-Oxley, HIPAA, Gramm-Leach-Bliley, pending legislation, tax and labour law.
- Section 17b standards: "this does not refer to the law of the land; think of it as an internal law imposed by your company"; considerations ask about industry bodies, codes of practice, watchdogs and ombudsmen.
- Section 19 off-the-shelf solutions and 19b reusable components anticipate the reuse-versus-build question at requirement level.
