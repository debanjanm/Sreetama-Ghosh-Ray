# CHAPTER-MAP.md — Chapter Subsection Detail & Open Gaps

**Purpose, updated.** Top-level folders now match the official chapter numbers directly — exactly 5, `chapter-1` through `chapter-5`, no "chapter-0" (see [SEQUENCE.md](SEQUENCE.md)) — so this file no longer needs to translate folder names. What it still does: break each chapter down to the *subsection* level per the official Guidelines doc, show which file covers which subsection, and — most importantly — keep flagging what hasn't been written anywhere yet. Chapter 3 in particular still spans two sub-folders (`objectives-and-hypotheses/` and `questionnaire/`) since the official Methodology chapter covers both in one chapter; this file is where that gets tracked at the subsection level.

**Source of truth for the official structure:** [university-files/MSSW - Project Guidelines.docx](university-files/MSSW%20-%20Project%20Guidelines.docx) — 5 chapters.

---

## Chapter 1 — Introduction

Files 01-06 are working/source material (03 is a direct quote from the guide's own feedback — never rewrite it). **`chapter-1/version-0/07-chapter1-draft-academic-prose.md` is the actual submission-voice draft**, audited to remove AI-generated tells (see SEQUENCE.md entry 29) — this is the file to adapt for the real chapter.

| Official subsection | Source | Status |
|---|---|---|
| 1.1 Background and Context | `07-chapter1-draft-academic-prose.md` sec 1.1 (drafted from `02-initial-analysis.md`, `03-guide-suggestion.md`) | **Done, submission-voice** |
| 1.2 Key Concepts and Definitions | `07-chapter1-draft-academic-prose.md` sec 1.2 (drafted from `04-atomic-concepts.md`, `05-key-terminology-glossary.md`) | **Done, submission-voice** |
| 1.3 Need, Scope & Significance | `07-chapter1-draft-academic-prose.md` sec 1.3 (drafted from `chapter-2/version-0/06-gap.md`) | **Done, submission-voice** — same source also feeds Ch2.4, each written in its own voice, not duplicated |
| 1.4 Statement of the Problem | `07-chapter1-draft-academic-prose.md` sec 1.4 | **Done, submission-voice** |
| 1.5 Industry Profile and Company Profile | `07-chapter1-draft-academic-prose.md` sec 1.5 (drafted from `06-industry-company-profile.md`) | **Done, submission-voice** — branch/zone-specific detail left as an explicit placeholder, needs student's own input |
| 1.6 Chapterization | `07-chapter1-draft-academic-prose.md` sec 1.6 | **Done, submission-voice** |

## Chapter 2 — Review of Literature

`chapter-2/version-0/` holds 9 files: 01-08 are working/decision-log material (search process, matrix, gap analysis — keep for Chapter 3 justification, don't submit as-is), **09-chapter2-draft-academic-prose.md is the actual submission-voice draft** — third-person, cited, flowing prose, audited to remove AI-generated tells (see SEQUENCE.md entry 25). This is the file to adapt for the real chapter.

| Official subsection | Source | Status |
|---|---|---|
| 2.1 Overview of Relevant Review | `09-chapter2-draft-academic-prose.md` sec 2.1 (drafted from `01-initial-literature-search.md`, `02-deep-research-report.md`, `03-literature-matrix.md`) | **Done, submission-voice** |
| 2.2 Theoretical Framework & Research Review | `09-chapter2-draft-academic-prose.md` sec 2.2 (drafted from `03-literature-matrix.md` Part 2 + `08-base-paper.md`) | **Done, submission-voice** |
| 2.3 Case Study | — | **Ambiguous, needs supervisor clarification, left as an explicit placeholder in 09.** Could mean a case study of Union Bank's own training practices, or reference to case-study-design papers already in the matrix — the guidelines doc doesn't define this term. |
| 2.4 Gaps in the study | `09-chapter2-draft-academic-prose.md` sec 2.4 (drafted from `06-gap.md`) | **Done, submission-voice** |

`04-literature-summary.md`, `05-past-dissertation-summary.md`, and `07-model-beta-chain-check.md` also live here — all lit-adjacent, primarily support Chapter 3's methodology justification (see below) even though they're filed as Chapter 2 material.

## Chapter 3 — Research Methodology

Two sub-folders, each independently versioned, plus **`chapter-3/01-chapter3-draft-academic-prose.md` — the actual submission-voice draft covering all 9 subsections**, audited to remove AI-generated tells (see SEQUENCE.md entry 27). This is the file to adapt for the real chapter; the sub-folder files remain working/decision-log material.

| Official subsection | Source | Status |
|---|---|---|
| 3.1 Objectives of the study | `01-chapter3-draft-academic-prose.md` sec 3.1 | **Done, submission-voice** |
| 3.2 Hypothesis of the study | `01-chapter3-draft-academic-prose.md` sec 3.2 | **Done, submission-voice** |
| 3.3 Definition of Variables | `01-chapter3-draft-academic-prose.md` sec 3.3 (newly synthesized from chapter-1 glossary + chapter-2 literature summary) | **Done, submission-voice** |
| 3.4 Research Design | `01-chapter3-draft-academic-prose.md` sec 3.4 | **Done, submission-voice** |
| 3.5 Sampling Methods | `01-chapter3-draft-academic-prose.md` sec 3.5 | **Done, submission-voice** |
| 3.6 Data Collection Procedures | `01-chapter3-draft-academic-prose.md` sec 3.6 | **Still an explicit placeholder** — needs student-specific info (which branch/zone, distribution method) not available anywhere in project materials |
| 3.7 Research questions | `01-chapter3-draft-academic-prose.md` sec 3.7 | **Done, submission-voice** |
| 3.8 Data Analysis Techniques | `01-chapter3-draft-academic-prose.md` sec 3.8 | **Done, submission-voice** |
| 3.9 Pilot Study, Reliability and Validity | `01-chapter3-draft-academic-prose.md` sec 3.9 | **Done, submission-voice** (definitions only — real numbers need pilot data) |
| Appendix — Questionnaire | `questionnaire/version-2/02-appendix-questionnaire-clean.md` | **Done, respondent-facing** — 30 items, no citation tags/version history |

## Chapter 4 — Data Analysis and Interpretation

**Real content not started** — needs real survey data first: descriptive stats, inferential tests (regression/mediation per `chapter-3/questionnaire/`'s plan), interpretation, comparison with the literature in `chapter-2/`. Two files exist: [chapter-4/version-0/01-data-analysis-dummy-worked-example.md](chapter-4/version-0/01-data-analysis-dummy-worked-example.md) is a **teaching tool** — real synthetic dataset, every statistic genuinely computed and several shown fully hand-worked (Cronbach's alpha, Pearson r, simple regression, Baron & Kenny mediation, t-test/ANOVA), every number fake, deliberately second-person/tutorial in voice since that's appropriate for teaching. [chapter-4/version-0/02-chapter4-template-academic-prose.md](chapter-4/version-0/02-chapter4-template-academic-prose.md) is the **clean submission-voice skeleton** — third person, bracketed placeholders, no fake numbers — this is the one to actually fill in once real data exists.

## Chapter 5 — Conclusion (also the first-rough-draft assembly point)

**Real content not started** — depends on Chapter 4's real results: summary of findings, contributions/limitations, future research directions (Model-Beta gets named here as a future-research extension per `chapter-2/version-0/07-model-beta-chain-check.md`'s recommendation), and the final conclusion. Per the Norms PDF schedule, "Chapter–V & First Rough draft" share one deadline — once this chapter's content is written, this is also where Chapters 1-5 get compiled into the full first rough draft. Two files exist, same split as Chapter 4: [chapter-5/version-0/01-conclusion-dummy-worked-example.md](chapter-5/version-0/01-conclusion-dummy-worked-example.md) is the **teaching example** (built on chapter-4's dummy results, deliberately tutorial in voice), [chapter-5/version-0/02-conclusion-template-academic-prose.md](chapter-5/version-0/02-conclusion-template-academic-prose.md) is the **clean submission-voice skeleton** to fill in once real findings exist.

## References & Appendix

- **References** — pull from `chapter-2/version-0/03-literature-matrix.md` and `08-base-paper.md`; format per the citation style in the Guidelines docx.
- **Appendix — Questionnaire** — `chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md`, 30 items, department-compliant. Ready pending supervisor/pilot review.

---

## Open items this mapping surfaced

1. ~~Page-count conflict~~ — **Resolved: 100 pages** (student decision, PLAN.md).
2. ~~Chapter 1's Industry/Company Profile — still a genuine blank spot.~~ **Resolved:** [chapter-1/version-0/06-industry-company-profile.md](chapter-1/version-0/06-industry-company-profile.md) now covers it, cited throughout. Residual: a couple of figures (current employee count, learning-academy count) vary across public sources and should be confirmed by the student directly with her internship/HR contact.
3. **Chapter 2.3 "Case Study"** — undefined term in the guidelines doc, needs supervisor clarification.
4. **Chapter 3.6 Data Collection Procedures** — not specified (Google Forms? paper? which employee groups?).

---

**Cross-references:** [PLAN.md](PLAN.md) · [SEQUENCE.md](SEQUENCE.md) · [chapter-1/version-0/01-introduction-notes.md](chapter-1/version-0/01-introduction-notes.md) · [university-files/](university-files/) · [references/](references/)
