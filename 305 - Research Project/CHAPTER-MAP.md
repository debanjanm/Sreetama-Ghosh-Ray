# CHAPTER-MAP.md — Chapter Subsection Detail & Open Gaps

**Purpose, updated.** Top-level folders now match the official chapter numbers directly (`chapter-0` through `chapter-5` — see [SEQUENCE.md](SEQUENCE.md)), so this file no longer needs to translate folder names. What it still does: break each chapter down to the *subsection* level per the official Guidelines doc, show which file covers which subsection, and — most importantly — keep flagging what hasn't been written anywhere yet. Chapter 3 in particular still spans two sub-folders (`objectives-and-hypotheses/` and `questionnaire/`) since the official Methodology chapter covers both in one chapter; this file is where that gets tracked at the subsection level.

**Source of truth for the official structure:** [university-files/MSSW - Project Guidelines.docx](university-files/MSSW%20-%20Project%20Guidelines.docx) — 5 chapters.

---

## Chapter 0 — Informal, not a submitted chapter

Everything in `chapter-0/` is scoping/foundation work — topic framing, guide feedback, first-principles concept breakdown, terminology glossary. None of it is a chapter on its own, but nearly all of Chapter 1 draws from it.

## Chapter 1 — Introduction

Full detail now lives in [chapter-1/version-0/01-introduction-notes.md](chapter-1/version-0/01-introduction-notes.md) — summary here:

| Official subsection | Source | Status |
|---|---|---|
| 1.1 Background and Context | `chapter-0/version-0/01-initial-analysis.md`, `02-guide-suggestion.md` | Draft material exists, needs writing up in formal prose |
| 1.2 Key Concepts and Definitions | `chapter-0/version-0/03-atomic-concepts.md`, `04-key-terminology-glossary.md` | **Strong match** |
| 1.3 Need, Scope & Significance | `chapter-2/version-0/06-gap.md` | Draft material exists (same source also feeds 2.4 — write each chapter's version separately, don't duplicate) |
| 1.4 Statement of the Problem | `PLAN.md` "Core Research Problem" line | Written, one paragraph — needs expanding |
| 1.5 Industry Profile and Company Profile | — | **Not written anywhere. Real gap**, unresolved. |
| 1.6 Chapterization | — | Trivial once other chapters exist |

## Chapter 2 — Review of Literature

`chapter-2/version-0/` holds all 8 literature files, mapping almost entirely onto this chapter:

| Official subsection | Source | Status |
|---|---|---|
| 2.1 Overview of Relevant Review | `01-initial-literature-search.md`, `02-deep-research-report.md`, `03-literature-matrix.md` | **Strong match**, most-developed part of the whole project |
| 2.2 Theoretical Framework & Research Review | `03-literature-matrix.md` Part 2 (foundational papers) + `08-base-paper.md` | **Strong match** |
| 2.3 Case Study | — | **Ambiguous, needs supervisor clarification.** Could mean a case study of Union Bank's own training practices, or reference to case-study-design papers already in the matrix — the guidelines doc doesn't define this term. |
| 2.4 Gaps in the study | `06-gap.md` | **Direct match** |

`04-literature-summary.md`, `05-past-dissertation-summary.md`, and `07-model-beta-chain-check.md` also live here — all lit-adjacent, primarily support Chapter 3's methodology justification (see below) even though they're filed as Chapter 2 material.

## Chapter 3 — Research Methodology

Two sub-folders, each independently versioned:

| Official subsection | Source | Status |
|---|---|---|
| 3.1 Objectives of the study | `objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md` sec 2 | Done |
| 3.2 Hypothesis of the study | Same file, sec 4 | Done |
| 3.3 Definition of Variables | `chapter-0/version-0/04-key-terminology-glossary.md` + this chapter's model diagram + `chapter-2/version-0/04-literature-summary.md` | Scattered across chapters 0/2/3 — needs consolidating into one Chapter 3 subsection when writing |
| 3.4 Research Design | — | **Partial.** Cross-sectional design and convenience sampling mentioned in passing, never written as your own one-paragraph design statement |
| 3.5 Sampling Methods | `chapter-2/version-0/05-past-dissertation-summary.md` sec 9.1 (department norms) | Informs, not yet written as your own methodology text |
| 3.6 Data Collection Procedures | — | **Not written anywhere.** How the survey will actually be distributed isn't specified |
| 3.7 Research questions | `objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md` sec 3 | Done |
| 3.8 Data Analysis Techniques | `questionnaire/version-2/01-model-alpha-questionnaire.md` Statistical Analysis section | Done |
| 3.9 Pilot Study | — | Planned as next step in `PLAN.md`, not yet conducted |
| 3.9 Reliability and Validity | `chapter-0/version-0/04-key-terminology-glossary.md` (definitions only) | Definitions exist; real Cronbach's alpha needs pilot data |

## Chapter 4 — Data Analysis and Interpretation

**Not started.** `chapter-4/` reserved, empty. Needs real survey data first — descriptive stats, inferential tests (regression/mediation per `chapter-3/questionnaire/`'s plan), interpretation, comparison with the literature in `chapter-2/`.

## Chapter 5 — Conclusion

**Not started.** `chapter-5/` reserved, empty. Depends on Chapter 4's results — summary of findings, contributions/limitations, future research directions (Model-Beta gets named here as a future-research extension per `chapter-2/version-0/07-model-beta-chain-check.md`'s recommendation), and the final conclusion.

## References & Appendix

- **References** — pull from `chapter-2/version-0/03-literature-matrix.md` and `08-base-paper.md`; format per the citation style in the Guidelines docx.
- **Appendix — Questionnaire** — `chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md`, 30 items, department-compliant. Ready pending supervisor/pilot review.

---

## Open items this mapping surfaced

1. ~~Page-count conflict~~ — **Resolved: 100 pages** (student decision, PLAN.md).
2. **Chapter 1's Industry/Company Profile — still a genuine blank spot.** Every other subsection has at least draft material; this one has none.
3. **Chapter 2.3 "Case Study"** — undefined term in the guidelines doc, needs supervisor clarification.
4. **Chapter 3.6 Data Collection Procedures** — not specified (Google Forms? paper? which employee groups?).

---

**Cross-references:** [PLAN.md](PLAN.md) · [SEQUENCE.md](SEQUENCE.md) · [chapter-1/version-0/01-introduction-notes.md](chapter-1/version-0/01-introduction-notes.md) · [university-files/](university-files/) · [references/](references/)
