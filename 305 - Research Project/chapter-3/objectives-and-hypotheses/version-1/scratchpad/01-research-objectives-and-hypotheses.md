# 01 — Research Objectives, Questions, and Hypotheses (LOCKED — Model-Alpha v1, with Trainer Competence)

**Status: LOCKED to Model-Alpha v1.** Decision made: Hybrid Learning + Trainer Competence → Learner Engagement → Training Effectiveness → Knowledge Retention → Job Performance. Trainer Competence added as a second antecedent to Engagement, per [08-base-paper.md](../../../../chapter-2/version-0/scratchpad/08-base-paper.md) sec 5 — the base paper (Saroj, Sahney & Sekar, 2026) tests it directly, and leaving it out was the single most likely defense question. Organizational/Supervisor Support still excluded — that remains out of scope (full Model-Beta, checked and rejected in [07-model-beta-chain-check.md](../../../../chapter-2/version-0/scratchpad/07-model-beta-chain-check.md)).

**v0 → v1 change log:** v0 (still on disk, [chapter-3/objectives-and-hypotheses/version-0/01](../../version-0/scratchpad/01-research-objectives-and-hypotheses.md)) had no Trainer Competence. This version adds it as a direct antecedent to Engagement (new H1b), instrument gains 8 items (TC1-8, see [03-model-alpha-questionnaire.md v1](../../../questionnaire/version-2/scratchpad/01-model-alpha-questionnaire.md)).

---

## 1. Research Problem

Does a well-designed blended learning model improve knowledge retention and employee performance compared with relying mainly on digital or classroom training — and **through what mechanism**? Model-Alpha v1's answer: through learner engagement — driven by both the hybrid learning design itself and trainer competence — sequentially producing training effectiveness, retention, and performance.

## 2. Research Objectives

1. Examine the impact of blended learning on employee knowledge retention.
2. Evaluate the effect of blended learning on workplace performance.
3. Compare the effectiveness of digital-only, classroom-only, and blended training approaches.
4. Examine learner engagement as the mechanism linking hybrid learning and trainer competence to training effectiveness. *(Broadened from v0 — trainer competence reinstated; organizational support still excluded.)*
5. Propose strategies for optimizing the digital/in-person balance.

## 3. Research Questions

- **RQ1:** How does blended learning affect knowledge retention compared with digital-only and classroom-only training?
- **RQ2:** Does blended learning improve employee performance after training?
- **RQ3:** Does learner engagement mediate the relationship between hybrid learning and training effectiveness, and does trainer competence also predict engagement? *(Broadened from v0's single-antecedent framing.)*
- **RQ4:** How should organizations divide learning activities between digital and classroom formats?
- **RQ5:** What blended learning strategies can improve both retention and workplace application?

## 4. Hypotheses

### Chain hypotheses (core Model-Alpha path — sequential mediation)

**Added below (department convention requires H0 stated first, always negating with "no significant [relationship/effect]" — see [MSSW-PROJECT-LAYOUT-AND-WORDINGS.md](../../../../MSSW-PROJECT-LAYOUT-AND-WORDINGS.md) Part 1 #4): no version bump, this completes standard reporting convention without changing any tested relationship.**

| # | Null hypothesis (H0) | Alternative hypothesis | Tested via |
|---|---|---|---|
| H1 | Hybrid Learning has no significant effect on Learner Engagement. | Hybrid Learning has a significant positive effect on Learner Engagement. | Regression Model 1, [01 v1](../../../questionnaire/version-2/scratchpad/01-model-alpha-questionnaire.md) |
| H1b | Trainer Competence has no significant effect on Learner Engagement. | Trainer Competence has a significant positive effect on Learner Engagement. | Same Regression Model 1 (now two predictors) — **NEW in v1**, matches the base paper's own tested instructor-competence→engagement path |
| H2 | Learner Engagement has no significant effect on Training Effectiveness. | Learner Engagement has a significant positive effect on Training Effectiveness. | Regression Model 2 |
| H3 | Training Effectiveness has no significant effect on Knowledge Retention. | Training Effectiveness has a significant positive effect on Knowledge Retention. | Regression Model 3 |
| H4 | Knowledge Retention has no significant effect on Job Performance. | Knowledge Retention has a significant positive effect on Job Performance. | Regression Model 4 |
| H5a | Learner Engagement does not mediate the relationship between Hybrid Learning and Training Effectiveness. | Learner Engagement mediates the relationship between Hybrid Learning and Training Effectiveness. | Mediation test (see [01 v1](../../../questionnaire/version-2/scratchpad/01-model-alpha-questionnaire.md) — Hayes PROCESS serial mediation) — this is the hypothesis that was CONDITIONAL/untestable before Section C (Engagement, EN1-5) was added to the instrument; now stable. |
| H5b | Training Effectiveness does not mediate the relationship between Learner Engagement and Knowledge Retention. | Training Effectiveness mediates the relationship between Learner Engagement and Knowledge Retention. | Same serial mediation model, second mediator in the chain — was implied by H2+H3 but never stated as its own hypothesis until v0's revision. |
| H5c | Knowledge Retention does not mediate the relationship between Training Effectiveness and Job Performance. | Knowledge Retention mediates the relationship between Training Effectiveness and Job Performance. | Same serial mediation model, third mediator in the chain — same as H5b. |

**Note on H1b:** Trainer Competence is a **parallel antecedent** alongside Hybrid Learning, not a further step in the chain — both feed Engagement directly, they don't feed each other. This is a multiple-predictor regression (2 IVs → Engagement), not a 6-step serial chain. Don't test Trainer Competence for mediation the way H5a-c test the other three — it isn't positioned as a mediator, it's positioned the same way Hybrid Learning is.

**Note on H5a-c:** Model-Alpha is a serial multiple-mediation chain, not a plain linear correlation path — Engagement, Training Effectiveness, and Knowledge Retention each act as a mediator for the pair of variables on either side of them. H1/H1b-H4 test the individual path coefficients; H5a-c test the mediation itself (whether removing the middle variable changes the direct-effect size). Both are needed — path significance alone doesn't establish mediation.

### Comparative / supplementary hypotheses (retained from original draft, renumbered)

| # | Null hypothesis (H0) | Alternative hypothesis | Tested via |
|---|---|---|---|
| H6 | There is no significant difference in Knowledge Retention between employees receiving blended training and employees receiving digital-only training. | Employees receiving blended training demonstrate significantly higher Knowledge Retention than employees receiving digital-only training. | Delivery-mode group comparison (t-test/ANOVA on Section A Q5/Q6 groupings) |
| H7 | There is no significant difference in Job Performance between employees receiving blended training and employees receiving digital-only or classroom-only training. | Employees receiving blended training demonstrate significantly higher Job Performance than employees receiving digital-only or classroom-only training. | Same as H6 |
| H8 | The integration of digital and classroom training (HL13-15) has no significant influence on Knowledge Retention and Job Performance. | The integration of digital and classroom training (HL13-15) has a significant positive influence on Knowledge Retention and Job Performance. | Correlation/regression using the Integration sub-dimension score |

**Mapping to original file 01 hypotheses**, for traceability: old H1→new H6, old H2 dropped (redundant with H6), old H3→new H7, old H4→new H5a (now stable, reworded as mediation not just "influences"), old H5→new H8. H5b/H5c have no file-01 ancestor — added in v0 when the serial-mediation gap was caught. H1b has no file-01 ancestor either — added in v1 when Trainer Competence was reinstated.

---

**Cross-references:** [01-initial-analysis.md](../../../../chapter-1/version-0/scratchpad/02-initial-analysis.md) · [02-guide-suggestion.md](../../../../chapter-1/version-0/scratchpad/03-guide-suggestion.md) · [03-literature-matrix.md](../../../../chapter-2/version-0/scratchpad/03-literature-matrix.md) · [06-gap.md](../../../../chapter-2/version-0/scratchpad/06-gap.md) · [08-base-paper.md](../../../../chapter-2/version-0/scratchpad/08-base-paper.md) · [03-model-alpha-questionnaire.md v1](../../../questionnaire/version-2/scratchpad/01-model-alpha-questionnaire.md) · [PLAN.md](../../../../PLAN.md)
