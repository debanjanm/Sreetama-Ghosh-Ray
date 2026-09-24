# Stage 5 — Inferential Analysis: Derivation Record

## Dataset Used

All calculations use the 105 eligible records in the Stage 3 scored dataset. Construct scores are the arithmetic means already defined in the approved analysis plan. No respondent was removed for a repeated response pattern. The two documented single-item imputations remain in the scored dataset.

## How the Results Were Calculated

- **Cronbach’s alpha:** calculated separately for the assigned items in each construct: 7 Hybrid Learning items, 6 Trainer Competence items, 6 Learner Engagement items, and 7 Training Effectiveness items.
- **Pearson correlation:** calculated from the four construct-score columns. Each p value is two-tailed at the 5% significance level.
- **Multiple regression:** Learner Engagement is the dependent variable; Hybrid Learning and Trainer Competence are entered together. Tolerance and VIF are reported for the two predictors.
- **Simple regression:** Training Effectiveness is the dependent variable and Learner Engagement is the predictor.

## Reproducibility

The companion [SPSS syntax](../03-scored-dataset/final-analysis-spss-syntax.sps) imports the same final CSV and specifies the same four reliability tests, correlation matrix, and regression models. It is provided for guide review and SPSS cross-checking; this record does not state that SPSS itself was run.

## Main Results

- Internal-consistency coefficients ranged from 0.958 to 0.971.
- H1: Hybrid Learning and Learner Engagement: r = 0.715, p < .001.
- H2: Trainer Competence and Learner Engagement: r = 0.726, p < .001.
- H3: Learner Engagement and Training Effectiveness: r = 0.765, p < .001.
- The two-predictor model had R² = 0.572, F(2, 102) = 68.218, p < .001. VIF was 3.005 for both predictors.
- The simple model had R² = 0.585, F(1, 103) = 145.452, p < .001.

## Reporting Boundary

The results identify associations in this selected, cross-sectional, self-report sample. They do not show that one construct caused another, establish a formal mediation effect, or represent all employees of Union Bank of India.