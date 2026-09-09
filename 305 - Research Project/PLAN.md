# PLAN.md — Hybrid Learning and Training Effectiveness (Union Bank of India)

Base: [01-initial-analysis.md](chapter-1/version-0/02-initial-analysis.md). Updated per guide feedback ([02](chapter-1/version-0/03-guide-suggestion.md)) + lit review ([01](chapter-2/version-0/01-initial-literature-search.md)).

**Folder structure note:** exactly 5 chapters (`chapter-1` through `chapter-5`), matching the official Guidelines doc — no separate "chapter-0". Early scoping work (topic framing, guide feedback, atomic concepts, terminology glossary) lives inside `chapter-1/version-0/` as source material (files 02-05), since it isn't a submitted chapter of its own. `chapter-3` has two independent sub-tracks — `objectives-and-hypotheses/` and `questionnaire/` — since Chapter 3 (Methodology) covers both per the official Guidelines doc. `chapter-5` holds Conclusion content and also doubles as the first-rough-draft assembly point (per the Norms PDF schedule: "Submission of Chapter–V & First Rough draft," one deadline, two things). See [SEQUENCE.md](SEQUENCE.md) for the full structure and [CHAPTER-MAP.md](CHAPTER-MAP.md) for subsection-level detail and open gaps.

## Working Title

**"Hybrid Learning and Training Effectiveness: Making Digital and In-Person Learning Work Together"**
Status: **CONFIRMED** — matches official approved topic list, Topic 2 (verified against department document, word-for-word title match; description clauses "impact knowledge retention and performance" / "optimize training delivery across digital and classroom formats" both map onto current scope).

## Core Research Problem

Does well-designed blended learning improve knowledge retention + employee performance vs mainly digital or classroom training — and **through what mechanism**? (not just "is hybrid better")

## Conceptual Model

**LOCKED: Model-Alpha v1, with Trainer Competence** (current canonical: [chapter-3/objectives-and-hypotheses/version-1/01](chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md)):

```
Hybrid Learning ─────┐
                      ├──▶ Learner Engagement ──▶ Training Effectiveness ──▶ Knowledge Retention ──▶ Job Performance
Trainer Competence ───┘
```

v0 ([chapter-3/objectives-and-hypotheses/version-0/01](chapter-3/objectives-and-hypotheses/version-0/01-research-objectives-and-hypotheses.md)) is Model-Alpha without Trainer Competence — kept as history, no longer canonical. v1 adds Trainer Competence as a second, parallel antecedent to Engagement, closing the gap flagged in [08-base-paper.md](chapter-2/version-0/08-base-paper.md) sec 5 (base paper tests it directly). Organizational/Supervisor Support still excluded (full Model-Beta, checked and rejected). **Instrument (canonical): [chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md](chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md) — 30 Likert items**, compressed from v1's 55 to comply with the department's item-count cap (all 6 constructs kept, model unchanged; [chapter-3/questionnaire/version-1/01](chapter-3/questionnaire/version-1/01-model-alpha-questionnaire.md), 55 items, kept as history/source of item wording).

**Model-Beta checked and rejected for now** — [chapter-2/version-0/07-model-beta-chain-check.md](chapter-2/version-0/07-model-beta-chain-check.md): no published paper tests the full engagement+trainer-competence+org-support+retention/performance combination; 7-construct model also statistically risky at department's typical 80-130 sample size. Model-Alpha v1 adds trainer competence only, not org support — a smaller, precedented step short of full Model-Beta. Frame org support as future-research extension in Chapter 5 (Conclusion — Future Research Directions), not current scope.

## Research Objectives, Questions, Hypotheses

**Canonical version:** [chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md](chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md) — LOCKED to Model-Alpha v1, H1/H1b/H2-H4 chain path hypotheses + H5a-c serial mediation hypotheses + H6-H8 comparative. Do not edit objectives/RQs/hypotheses here anymore; edit that file and bump its version.

## Base Paper

**Locked: Saroj, Sahney & Sekar (2026)**, VJIKMS 56(2) — [chapter-2/version-0/08-base-paper.md](chapter-2/version-0/08-base-paper.md). Only workplace blended-learning paper in the matrix testing engagement as mediator; verified by direct fetch twice. Model-Alpha v1 now tests Trainer Competence directly (matching the base paper), still narrows Supervisor Support out, still extends the base paper's single "employee agility" endpoint into the TE→KR→JP chain.

## Dissertation Structure

**Matches the official department document** ([university-files/MSSW - Project Guidelines.docx](university-files/MSSW%20-%20Project%20Guidelines.docx)) — **5 chapters.** Folders now match this 1:1 at the top level (`chapter-1` through `chapter-5`); full subsection-level mapping: [CHAPTER-MAP.md](CHAPTER-MAP.md). **Target: 100 pages** (the figure shared by both officially-conflicting page-count ranges, 80-100 and 100-130 — student's decision, pending supervisor confirmation).

1. Introduction ([chapter-1/](chapter-1/version-0/01-introduction-notes.md)) — background/context, key concepts, need/scope/significance, statement of problem, industry & company profile (Union Bank of India — closed, see [chapter-1/version-0/06-industry-company-profile.md](chapter-1/version-0/06-industry-company-profile.md)), chapterization.
2. Review of Literature ([chapter-2/](chapter-2/version-0/)) — overview of review, theoretical framework, case study (meaning TBD — ask supervisor), gaps in the study.
3. Research Methodology ([chapter-3/](chapter-3/)) — objectives, hypotheses, definition of variables, research design, sampling methods, data collection procedures, research questions, data analysis techniques, pilot study, reliability & validity.
4. Data Analysis and Interpretation ([chapter-4/](chapter-4/version-0/01-data-analysis-dummy-worked-example.md)) — descriptive analysis, inferential analysis, interpretation of results, comparison with previous studies, theoretical/practical implications. **Real content not started — needs real data.** A full dummy-data worked example exists (step-by-step Cronbach's alpha, correlation, regression ×4, mediation ×3, t-test/ANOVA) for teaching purposes — every number in it is fake, replace once real data is collected.
5. Conclusion ([chapter-5/](chapter-5/version-0/01-conclusion-dummy-worked-example.md)) — summary of findings, contributions & limitations, future research directions (Model-Beta belongs here as a named future-research extension), conclusion. **Also the first-rough-draft assembly point** — Norms PDF schedule bundles "Chapter–V & First Rough draft" at one deadline; when Chapter 4 is done, compile Chapters 1-5 into the full draft here. **Real content not started** — a dummy-data worked example exists, built on chapter-4's dummy results, template only.

## Status by Phase

| Phase | Status | Ref |
|---|---|---|
| Topic framing | Done | [01](chapter-1/version-0/02-initial-analysis.md) |
| Concept breakdown (mediator/moderator logic) | Done | [03](chapter-1/version-0/04-atomic-concepts.md) |
| Guide variable feedback | Received | [02](chapter-1/version-0/03-guide-suggestion.md) |
| Draft questionnaire (51 items, 4-var model) + stats plan | Done (superseded by Model-Alpha instrument) | [01](chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md) |
| Questionnaire wording refinement | Done (9.5/10) | [02](chapter-3/questionnaire/version-0/02-refined-questionnaire.md) |
| Lit search — mechanism variables | Done, Tier 1 papers found | [01](chapter-2/version-0/01-initial-literature-search.md) |
| Deep evidence report (effect sizes, design principles, KPIs) | Done | [02](chapter-2/version-0/02-deep-research-report.md) |
| Systematic lit matrix (30-50 papers) | Done (36 papers/instruments + foundational + validated-scale sections) | [03](chapter-2/version-0/03-literature-matrix.md) |
| Finalize conceptual model + title | **Model-Alpha v0 locked** (HL→Engagement→TE→KR→JP) | [01 v0](chapter-3/objectives-and-hypotheses/version-0/01-research-objectives-and-hypotheses.md) |
| Add Engagement items to instrument (EN1-5) | Done | [03 v0](chapter-3/questionnaire/version-0/03-model-alpha-questionnaire.md) |
| Map 42 original items to published scales | Done | [04](chapter-2/version-0/04-literature-summary.md) |
| Serial-mediation hypotheses (H5a-c) + PROCESS Model 6 test | Done | [01 v0](chapter-3/objectives-and-hypotheses/version-0/01-research-objectives-and-hypotheses.md), [03 v0](chapter-3/questionnaire/version-0/03-model-alpha-questionnaire.md) |
| Base paper selected + narrows/extends comparison | Done | [08](chapter-2/version-0/08-base-paper.md) |
| Trainer competence added — **Model-Alpha v1 locked** | Done | [01 v1](chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md), [01 v1](chapter-3/questionnaire/version-1/01-model-alpha-questionnaire.md) |
| Compressed to 30 items — **v2 canonical** | Done | [01 v2](chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md) |
| Page count / sample size — 2 open decisions | Resolved by student: 100 pages, ~80 sample | [CHAPTER-MAP.md](CHAPTER-MAP.md), [SEQUENCE.md](SEQUENCE.md) |
| Switch from work-type stages to chapter-numbered folders | Done | [SEQUENCE.md](SEQUENCE.md) entry 19 |
| Expert review + pilot test | Not started | — |
| Data collection | Not started | — |
| Analysis (descriptives → Cronbach's α → correlation → regression → t-test/ANOVA → mediation test) | Not started (real data) — dummy-data worked example done | [chapter-4/version-0/01](chapter-4/version-0/01-data-analysis-dummy-worked-example.md) |
| Chapter 4/5 dummy-data teaching examples (step-by-step math) | Done | [chapter-4/version-0/01](chapter-4/version-0/01-data-analysis-dummy-worked-example.md), [chapter-5/version-0/01](chapter-5/version-0/01-conclusion-dummy-worked-example.md) |

## Next Steps (priority order)

1. Supervisor/expert review of Model-Alpha instrument ([01 v2](chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md)) — 30 items, department-compliant. Flag explicitly: (a) Trainer Competence and Engagement sections are researcher-adapted, not verbatim published wording; (b) most Hybrid Learning sub-dimensions are down to 1 item, so per-dimension scoring is no longer statistically supportable — construct-level only.
2. ~~Close Chapter 1's Industry/Company Profile gap~~ — **Done.** [chapter-1/version-0/06-industry-company-profile.md](chapter-1/version-0/06-industry-company-profile.md) profiles Union Bank of India (history, scale, ownership, training structure, digital-learning initiatives), referenced from [chapter-1/version-0/01-introduction-notes.md](chapter-1/version-0/01-introduction-notes.md) sec 1.5. Still needs student's own input: specific branch/zone studied, and confirming a couple of figures (employee count, learning-academy count) directly with her internship/HR contact rather than public sources.
3. Pilot test → Cronbach's α check per section — Trainer Competence at only 3 items is the tightest, watch it specifically.
4. Full data collection (Union Bank employees, **target ~80 respondents**).
5. Run analysis pipeline per [01 v2](chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md) (descriptives → reliability → correlation → regression Models 1-4 → serial mediation test → t-test/ANOVA) — this becomes chapter-4's content.
6. Turn findings into HR strategy scorecard — construct-level only (adapted since dimension-level breakdown no longer applies) — feeds chapter-5.
