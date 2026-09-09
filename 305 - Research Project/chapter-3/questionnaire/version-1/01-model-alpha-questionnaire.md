# 01 — Model-Alpha v1: Final Instrument, with Trainer Competence (55 items)

**Model-Alpha v1 definition:** Hybrid Learning + Trainer Competence → Learner Engagement → Training Effectiveness → Knowledge Retention → Job Performance. Trainer Competence added as a second, parallel antecedent to Engagement (alongside Hybrid Learning) — per [08-base-paper.md](../../../chapter-2/version-0/08-base-paper.md) sec 5, since the base paper (Saroj, Sahney & Sekar, 2026) tests instructor competence directly and its absence was the sharpest open gap. Organizational/Supervisor Support still excluded (full Model-Beta, checked and rejected in [07-model-beta-chain-check.md](../../../chapter-2/version-0/07-model-beta-chain-check.md)).

**v0 → v1 change:** [chapter-3/questionnaire/version-0/03](../version-0/03-model-alpha-questionnaire.md) had 47 items, no Trainer Competence. This version adds Section C: Trainer Competence (TC1-8), 47→55 items total. Everything else — HL, Engagement, TE, KR, JP wording — unchanged from v0.

This file is the clean, standalone instrument — 04/05 (original draft) and v0 (pre-Trainer-Competence Model-Alpha) stay untouched as history. Item wording for HL/TE/KR/JP below is 05's refined version (already vetted); Sections C (Trainer Competence) and D (Engagement) are new/carried from v0.

---

## Response Scale

1 – Strongly Disagree · 2 – Disagree · 3 – Neither Agree nor Disagree · 4 – Agree · 5 – Strongly Agree

## Section A: Basic Information

Unchanged from [01](../version-0/01-base-questionnaire-and-calculation.md) — age group, years of experience, job level, training frequency in last 12 months, % delivered digitally, % delivered face-to-face.

## Section B: Hybrid Learning (HL1–HL15)

Unchanged wording from [02-refined-questionnaire.md](../version-0/02-refined-questionnaire.md) — Flexibility (HL1-3), Accessibility (HL4-6), Interaction (HL7-9), Technology (HL10-12), Integration (HL13-15).

## Section C: Trainer Competence (TC1–TC8) — NEW in v1

**Construct basis:** content, technical, process, and motivation competence — the 4-dimension structure used in the "Faculty online competence" study (2021, doi.org/10.1080/10528008.2021.1965891), the shorter 8-item alternative already sourced in [03-literature-matrix.md](../../../chapter-2/version-0/03-literature-matrix.md) Part 3 (chosen over the 32-item Open Praxis scale specifically to limit instrument length given your sample-size constraint — [05-past-dissertation-summary.md](../../../chapter-2/version-0/05-past-dissertation-summary.md) sec 9.1). **Caution:** same as Engagement — exact published item wording wasn't accessible in this research pass, items below are researcher-adapted to the four named dimensions, not verbatim. State this explicitly alongside your Engagement-section disclosure in the methodology chapter.

TC1. The trainer/facilitator has strong knowledge of the training subject matter.

TC2. The trainer explains concepts clearly and accurately.

TC3. The trainer is comfortable using the digital tools and platforms involved in the training.

TC4. The trainer resolves technical issues during training sessions effectively.

TC5. The trainer organizes and paces the training sessions well.

TC6. The trainer encourages interaction and participation during sessions.

TC7. The trainer motivates me to actively participate in the training.

TC8. The trainer shows enthusiasm that makes the training more engaging.

## Section D: Learner Engagement (EN1–EN5)

**Construct basis:** dedication + absorption during training, per Safety Training Engagement Scale (STE-S — Italian validation study, 2022, 5 items) and Fredricks/Blumenfeld/Paris (2004) behavioural-emotional-cognitive engagement framework, both already sourced in [04-literature-summary.md](../../../chapter-2/version-0/04-literature-summary.md). **Caution:** STE-S's own published item wording wasn't accessible in this research pass (source paywalled) — the 5 items below are researcher-adapted to the dedication/absorption constructs it measures, not a verbatim reproduction. State this explicitly in your methodology chapter, same as you already do for KR1-9.

EN1. I stay fully engaged and attentive during the training sessions, whether online or in-person.

EN2. I feel absorbed in the training activities rather than simply going through the motions.

EN3. I actively participate in discussions, exercises, or activities during the training.

EN4. I put genuine effort into understanding the training content, not just completing it.

EN5. I remain motivated to complete the training from start to finish.

*(Relettered from Section C in v0 to Section D in v1 — content identical, Trainer Competence inserted before it.)*

## Section E: Training Effectiveness (TE1–TE9)

Unchanged wording from [02-refined-questionnaire.md](../version-0/02-refined-questionnaire.md) — Relevance (TE1-3), Learning/Understanding (TE4-6), Application (TE7-9). *(Relettered from Section D in v0 to Section E in v1 — content identical.)*

## Section F: Knowledge Retention (KR1–KR9)

Unchanged wording from [02-refined-questionnaire.md](../version-0/02-refined-questionnaire.md). *(Relettered from Section E in v0 to Section F in v1 — content identical.)*

## Section G: Job Performance (JP1–JP9)

Unchanged wording from [02-refined-questionnaire.md](../version-0/02-refined-questionnaire.md). *(Relettered from Section F in v0 to Section G in v1 — content identical.)*

## Optional Final Questions

Unchanged from [01](../version-0/01-base-questionnaire-and-calculation.md) — 3 open-ended questions on hybrid training experience.

---

## Scoring

Same averaging method as [01](../version-0/01-base-questionnaire-and-calculation.md) sec 3-5, plus:

**Trainer Competence score** = average of TC1–TC8.
**Learner Engagement score** = average of EN1–EN5.

## Statistical Analysis — Updated for the Model-Alpha v1 Chain

Same 6-step pipeline as [01](../version-0/01-base-questionnaire-and-calculation.md) sec 9, with correlation and regression now covering 6 variables instead of 5:

### Correlation matrix (Test 3)

| Relationship | Expected direction |
|---|---|
| Hybrid Learning ↔ Learner Engagement | Positive |
| Trainer Competence ↔ Learner Engagement | Positive — **new in v1** |
| Learner Engagement ↔ Training Effectiveness | Positive |
| Training Effectiveness ↔ Knowledge Retention | Positive |
| Knowledge Retention ↔ Job Performance | Positive |

### Regression models (Test 4) — matches Model-Alpha v1's structure exactly

- **Model 1:** Learner Engagement = Hybrid Learning + Trainer Competence *(now 2 predictors — tests H1 and H1b together)*
- **Model 2:** Training Effectiveness = Hybrid Learning + Trainer Competence + Learner Engagement *(tests whether Engagement mediates — the core Model-Alpha claim)*
- **Model 3:** Knowledge Retention = Hybrid Learning + Trainer Competence + Learner Engagement + Training Effectiveness
- **Model 4:** Job Performance = Hybrid Learning + Trainer Competence + Learner Engagement + Training Effectiveness + Knowledge Retention

### Mediation tests — Model-Alpha v1 is a serial (3-mediator) chain with 2 parallel antecedents, not one mediation link

Learner Engagement, Training Effectiveness, and Knowledge Retention each sit between two other variables and mediate that relationship (see [01 v1](../../objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md) H5a-c). Trainer Competence is a **parallel antecedent alongside Hybrid Learning**, not a further mediator — it feeds Engagement directly, same position as Hybrid Learning, not tested for mediation itself:

```
Hybrid Learning ─────┐
                      ├──▶ EN ──▶ TE ──▶ KR ──▶ JP
Trainer Competence ───┘    ↑EN mediates  ↑TE mediates  ↑KR mediates
                            HL/TC→TE      EN→KR         TE→JP
```

Regression Models 1-4 above test whether each *path* is significant. They do **not**, by themselves, establish mediation — that needs a separate test per mediator:

- **Basic check (Baron & Kenny style):** for each mediator, compare the direct-effect regression (e.g. TE = HL alone) against the model with the mediator added (TE = HL + EN) — if HL's coefficient shrinks once the mediator is added, that's evidence of mediation.
- **Stronger, recommended test:** Hayes' PROCESS macro for SPSS, **Model 6 (serial multiple mediation)** — this is built specifically for a chain like yours (X → M1 → M2 → M3 → Y) and gives you bootstrapped indirect effects for each mediation step in one run, rather than four separate ad-hoc regression comparisons. Ask your supervisor whether PROCESS is available/approved for use — if not, the Baron & Kenny comparison above is the fallback, but state clearly in Chapter 3 that it's the simpler alternative, not the first-choice method.

---

**Cross-references:** [01-base-questionnaire-and-calculation.md](../version-0/01-base-questionnaire-and-calculation.md) · [02-refined-questionnaire.md](../version-0/02-refined-questionnaire.md) · [03-literature-matrix.md](../../../chapter-2/version-0/03-literature-matrix.md) · [04-literature-summary.md](../../../chapter-2/version-0/04-literature-summary.md) · [08-base-paper.md](../../../chapter-2/version-0/08-base-paper.md) · [01-research-objectives-and-hypotheses.md v1](../../objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md) · [SEQUENCE.md](../../../SEQUENCE.md)
