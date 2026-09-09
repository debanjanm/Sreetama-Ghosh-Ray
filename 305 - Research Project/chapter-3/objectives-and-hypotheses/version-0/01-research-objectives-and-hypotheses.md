# 01 — Research Objectives, Questions, and Hypotheses (LOCKED — Model-Alpha, v0)

**Status: LOCKED to Model-Alpha.** Decision made: Hybrid Learning → Learner Engagement → Training Effectiveness → Knowledge Retention → Job Performance. No trainer competence, no organizational/supervisor support (that scope stays in Model B, not used here). The Path-1/Path-2 fork from [06-gap.md](../../../chapter-2/version-0/06-gap.md) sec 3.2 is resolved: Path 1 for engagement (added to the instrument, see [03-model-alpha-questionnaire.md](../../questionnaire/version-0/03-model-alpha-questionnaire.md)), but scoped down from full Model B — trainer competence and org support explicitly excluded.

---

## 1. Research Problem

Does a well-designed blended learning model improve knowledge retention and employee performance compared with relying mainly on digital or classroom training — and **through what mechanism**? Model-Alpha's answer: through learner engagement, sequentially driving training effectiveness, retention, and performance.

## 2. Research Objectives

1. Examine the impact of blended learning on employee knowledge retention.
2. Evaluate the effect of blended learning on workplace performance.
3. Compare the effectiveness of digital-only, classroom-only, and blended training approaches.
4. Examine learner engagement as the mechanism linking hybrid learning to training effectiveness. *(Narrowed from the original broader wording — trainer competence/organizational support dropped, since Model-Alpha doesn't include them.)*
5. Propose strategies for optimizing the digital/in-person balance.

## 3. Research Questions

- **RQ1:** How does blended learning affect knowledge retention compared with digital-only and classroom-only training?
- **RQ2:** Does blended learning improve employee performance after training?
- **RQ3:** Does learner engagement mediate the relationship between hybrid learning and training effectiveness? *(Narrowed from "which factors contribute most" — Model-Alpha tests one specific mechanism, not an open factor search.)*
- **RQ4:** How should organizations divide learning activities between digital and classroom formats?
- **RQ5:** What blended learning strategies can improve both retention and workplace application?

## 4. Hypotheses

### Chain hypotheses (core Model-Alpha path — sequential mediation)

| # | Hypothesis | Tested via |
|---|---|---|
| H1 | Hybrid Learning has a significant positive effect on Learner Engagement. | Regression Model 1, [03](../../questionnaire/version-0/03-model-alpha-questionnaire.md) |
| H2 | Learner Engagement has a significant positive effect on Training Effectiveness. | Regression Model 2 |
| H3 | Training Effectiveness has a significant positive effect on Knowledge Retention. | Regression Model 3 |
| H4 | Knowledge Retention has a significant positive effect on Job Performance. | Regression Model 4 |
| H5a | Learner Engagement mediates the relationship between Hybrid Learning and Training Effectiveness. | Mediation test (see [03](../../questionnaire/version-0/03-model-alpha-questionnaire.md) — Hayes PROCESS serial mediation) — this is the hypothesis that was CONDITIONAL/untestable before Section C (Engagement, EN1-5) was added to the instrument; now stable. |
| H5b | Training Effectiveness mediates the relationship between Learner Engagement and Knowledge Retention. | Same serial mediation model, second mediator in the chain — **added now**, was implied by H2+H3 but never stated as its own hypothesis until this revision. |
| H5c | Knowledge Retention mediates the relationship between Training Effectiveness and Job Performance. | Same serial mediation model, third mediator in the chain — **added now**, same gap as H5b. |

**Note on H5a-c:** Model-Alpha is a serial multiple-mediation chain, not a plain linear correlation path — Engagement, Training Effectiveness, and Knowledge Retention each act as a mediator for the pair of variables on either side of them. H1-H4 test the individual path coefficients; H5a-c test the mediation itself (whether removing the middle variable changes the direct-effect size). Both are needed — path significance alone doesn't establish mediation.

### Comparative / supplementary hypotheses (retained from original draft, renumbered)

| # | Hypothesis | Tested via |
|---|---|---|
| H6 | Employees receiving blended training demonstrate higher Knowledge Retention than employees receiving digital-only training. | Delivery-mode group comparison (t-test/ANOVA on Section A Q5/Q6 groupings) |
| H7 | Employees receiving blended training demonstrate higher Job Performance than employees receiving digital-only or classroom-only training. | Same as H6 |
| H8 | The integration of digital and classroom training (HL13-15) positively influences Knowledge Retention and Job Performance. | Correlation/regression using the Integration sub-dimension score |

**Mapping to original file 01 hypotheses**, for traceability: old H1→new H6, old H2 dropped (redundant with H6), old H3→new H7, old H4→new H5a (now stable, reworded as mediation not just "influences"), old H5→new H8. H5b/H5c have no file-01 ancestor — new, added when the serial-mediation gap was caught.

---

**Cross-references:** [01-initial-analysis.md](../../../chapter-0/version-0/01-initial-analysis.md) · [02-guide-suggestion.md](../../../chapter-0/version-0/02-guide-suggestion.md) · [03-literature-matrix.md](../../../chapter-2/version-0/03-literature-matrix.md) · [06-gap.md](../../../chapter-2/version-0/06-gap.md) · [03-model-alpha-questionnaire.md](../../questionnaire/version-0/03-model-alpha-questionnaire.md) · [PLAN.md](../../../PLAN.md)
