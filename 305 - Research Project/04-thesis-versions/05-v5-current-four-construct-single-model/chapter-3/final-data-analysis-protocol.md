# Version 5 SPSS Analysis Protocol

## Purpose

This protocol records the analytical procedures evidenced in the supplied SPSS Statistics 23 output. It does not recalculate or replace any SPSS result.

## Model

```text
Hybrid Learning ────────┐
Trainer Competence ─────┼──→ Training Effectiveness
Learner Engagement ────┘
```

- **Dependent variable:** `TETMEAN` — Training Effectiveness
- **Independent variables:** `HLTMEAN` — Hybrid Learning; `TCTMEAN` — Trainer Competence; `LETMEAN` — Learner Engagement
- **Regression cases:** 102 valid cases

## Procedures Evidenced in the SPSS Output

1. Item descriptives for the 26 Likert-scale items, including skewness and kurtosis.
2. Explore output for construct means, including histograms, Q–Q plots, boxplots, and normality tests.
3. One reliability analysis covering all 26 items.
4. Principal Component Analysis with varimax rotation.
5. Crosstabs and chi-square tests, t-tests, and one-way ANOVA with Duncan post-hoc output.
6. Pearson correlations among `HLTMEAN`, `TCTMEAN`, `LETMEAN`, and `TETMEAN`.
7. One multiple regression with `TETMEAN` as the outcome and the other three construct means entered together.

## Reporting Rules

- Report the regression as an association and prediction model, not as proof of causation or mediation.
- Treat the factor, chi-square, t-test, and ANOVA output as supporting diagnostics unless directly relevant to a stated descriptive question.
- Report the 26-item alpha of .980239 as overall questionnaire consistency only. Do not use it as separate construct-level reliability evidence.
- Use the supplied SPSS output as the Version 5 result source. The original 103-record dataset remains preserved as a separate earlier analytical record.
