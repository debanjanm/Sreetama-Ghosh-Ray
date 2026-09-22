# 03 — Model-Alpha: Final Instrument (47 items)

**Model-Alpha definition:** Hybrid Learning → Learner Engagement → Training Effectiveness → Knowledge Retention → Job Performance. A single sequential mediation chain — Model A's Hybrid Learning→Engagement→Effectiveness core, extended with the Knowledge Retention and Job Performance tail you already built in [01-base-questionnaire-and-calculation.md](01-base-questionnaire-and-calculation.md)/[02-refined-questionnaire.md](02-refined-questionnaire.md). No trainer competence, no organizational/supervisor support — those stay out of scope (that's Model B, not this one).

This file is the clean, standalone instrument — 04/05 stay untouched as history of how the wording evolved. Item wording for HL/TE/KR/JP below is 05's refined version (already vetted); Section C (Engagement) is new.

---

## Response Scale

1 – Strongly Disagree · 2 – Disagree · 3 – Neither Agree nor Disagree · 4 – Agree · 5 – Strongly Agree

## Section A: Basic Information

Unchanged from [01](01-base-questionnaire-and-calculation.md) — age group, years of experience, job level, training frequency in last 12 months, % delivered digitally, % delivered face-to-face.

## Section B: Hybrid Learning (HL1–HL15)

Unchanged wording from [02-refined-questionnaire.md](02-refined-questionnaire.md) — Flexibility (HL1-3), Accessibility (HL4-6), Interaction (HL7-9), Technology (HL10-12), Integration (HL13-15).

## Section C: Learner Engagement (EN1–EN5) — NEW

**Construct basis:** dedication + absorption during training, per Safety Training Engagement Scale (STE-S — Italian validation study, 2022, 5 items) and Fredricks/Blumenfeld/Paris (2004) behavioural-emotional-cognitive engagement framework, both already sourced in [04-literature-summary.md](../../../../chapter-2/version-0/scratchpad/04-literature-summary.md). **Caution:** STE-S's own published item wording wasn't accessible in this research pass (source paywalled) — the 5 items below are researcher-adapted to the dedication/absorption constructs it measures, not a verbatim reproduction. State this explicitly in your methodology chapter, same as you already do for KR1-9.

EN1. I stay fully engaged and attentive during the training sessions, whether online or in-person.

EN2. I feel absorbed in the training activities rather than simply going through the motions.

EN3. I actively participate in discussions, exercises, or activities during the training.

EN4. I put genuine effort into understanding the training content, not just completing it.

EN5. I remain motivated to complete the training from start to finish.

## Section D: Training Effectiveness (TE1–TE9)

Unchanged wording from [02-refined-questionnaire.md](02-refined-questionnaire.md) — Relevance (TE1-3), Learning/Understanding (TE4-6), Application (TE7-9). *(Relettered from Section C to Section D — content identical.)*

## Section E: Knowledge Retention (KR1–KR9)

Unchanged wording from [02-refined-questionnaire.md](02-refined-questionnaire.md). *(Relettered from Section D to Section E — content identical.)*

## Section F: Job Performance (JP1–JP9)

Unchanged wording from [02-refined-questionnaire.md](02-refined-questionnaire.md). *(Relettered from Section E to Section F — content identical.)*

## Optional Final Questions

Unchanged from [01](01-base-questionnaire-and-calculation.md) — 3 open-ended questions on hybrid training experience.

---

## Scoring

Same averaging method as [01](01-base-questionnaire-and-calculation.md) sec 3-5, plus:

**Learner Engagement score** = average of EN1–EN5.

## Statistical Analysis — Updated for the Model-Alpha Chain

Same 6-step pipeline as [01](01-base-questionnaire-and-calculation.md) sec 9, with correlation and regression now covering 5 variables instead of 4:

### Correlation matrix (Test 3)

| Relationship | Expected direction |
|---|---|
| Hybrid Learning ↔ Learner Engagement | Positive |
| Learner Engagement ↔ Training Effectiveness | Positive |
| Training Effectiveness ↔ Knowledge Retention | Positive |
| Knowledge Retention ↔ Job Performance | Positive |

### Regression models (Test 4) — matches Model-Alpha's chain exactly

- **Model 1:** Learner Engagement = Hybrid Learning
- **Model 2:** Training Effectiveness = Hybrid Learning + Learner Engagement *(tests whether Engagement mediates — the core Model-Alpha claim)*
- **Model 3:** Knowledge Retention = Hybrid Learning + Learner Engagement + Training Effectiveness
- **Model 4:** Job Performance = Hybrid Learning + Learner Engagement + Training Effectiveness + Knowledge Retention

### Mediation tests — Model-Alpha is a serial (3-mediator) chain, not one mediation link

Model-Alpha has **three** mediators in sequence, not one — Learner Engagement, Training Effectiveness, and Knowledge Retention each sit between two other variables and mediate that relationship (see [01](../../../objectives-and-hypotheses/version-0/scratchpad/01-research-objectives-and-hypotheses.md) H5a-c):

```
HL → EN → TE → KR → JP
     ↑EN mediates    ↑TE mediates    ↑KR mediates
     HL→TE           EN→KR           TE→JP
```

Regression Models 1-4 above test whether each *path* is significant. They do **not**, by themselves, establish mediation — that needs a separate test per mediator:

- **Basic check (Baron & Kenny style):** for each mediator, compare the direct-effect regression (e.g. TE = HL alone) against the model with the mediator added (TE = HL + EN) — if HL's coefficient shrinks once the mediator is added, that's evidence of mediation.
- **Stronger, recommended test:** Hayes' PROCESS macro for SPSS, **Model 6 (serial multiple mediation)** — this is built specifically for a chain like yours (X → M1 → M2 → M3 → Y) and gives you bootstrapped indirect effects for each mediation step in one run, rather than four separate ad-hoc regression comparisons. Ask your supervisor whether PROCESS is available/approved for use — if not, the Baron & Kenny comparison above is the fallback, but state clearly in Chapter 3 that it's the simpler alternative, not the first-choice method.

---

**Cross-references:** [01-base-questionnaire-and-calculation.md](01-base-questionnaire-and-calculation.md) · [02-refined-questionnaire.md](02-refined-questionnaire.md) · [04-literature-summary.md](../../../../chapter-2/version-0/scratchpad/04-literature-summary.md) · [01-research-objectives-and-hypotheses.md](../../../objectives-and-hypotheses/version-0/scratchpad/01-research-objectives-and-hypotheses.md) · [SEQUENCE.md](../../../../SEQUENCE.md)
