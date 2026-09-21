# Data-Derivation Guide
## How the Preliminary Results Were Produced

> Purpose: This guide explains the calculation path from Google Forms responses to the Chapter 4 tables. It uses the first export of 24 submitted records.

## 1. Preserve the Raw Export

The original downloaded Google Forms workbook is not edited. A preserved copy of the 24 records appears in the Raw Export sheet of the companion analysis workbook. This makes the Chapter 4 tables traceable to original response labels.

## 2. Screen for Eligibility

| Eligibility response | Treatment |
| --- | --- |
| Yes | Retain for analysis |
| No | Retain in raw export but exclude from analysis |

The export contains 24 records: 22 Yes and 2 No. Every calculation in the preliminary chapters uses the 22 Yes records.

## 3. Convert Labels to Numbers

| Text response | Code |
| --- | ---: |
| 1 - Strongly Disagree | 1 |
| 2 - Disagree | 2 |
| 3 - Neither Agree nor Disagree | 3 |
| 4 - Agree | 4 |
| 5 - Strongly Agree | 5 |

The Analysis Data sheet stores a numeric value for every Likert item from Q5 to Q30. The original text response remains in the Raw Export sheet.

## 4. Calculate Four Construct Scores

| Construct | Calculation |
| --- | --- |
| Hybrid Learning | Sum of Q5-Q11 divided by 7 |
| Trainer Competence | Sum of Q12-Q17 divided by 6 |
| Learner Engagement | Sum of Q18-Q23 divided by 6 |
| Training Effectiveness | Sum of Q24-Q30 divided by 7 |

For example, a Hybrid Learning total of 28 becomes 28 divided by 7, or 4.00. A higher score represents a more positive response.

## 5. Derive Percentages and Statistics

Percentage equals the frequency in one category divided by 22 eligible respondents, multiplied by 100. For example, 11 respondents aged 35-44 gives 11 divided by 22 multiplied by 100, or 50.0 per cent.

The workbook then calculates each construct mean and standard deviation. Cronbach's alpha shows whether the assigned items move together in the interim dataset. Alpha does not prove that the questionnaire is a fully validated bank-specific scale. The small sample and five same-answer patterns may contribute to the very high alpha values.

## 6. Derive Correlation and Regression

Pearson correlation compares two construct-score columns. A positive value means that high scores on one construct tend to occur with high scores on the other.

The first regression uses Hybrid Learning and Trainer Competence together to estimate Learner Engagement. The R squared of .836 means the two predictors together are associated with 83.6 per cent of variation in engagement scores. However, the predictors correlate at .983 and their Variance Inflation Factor is 29.571. This is severe multicollinearity. The current data cannot separate the individual relationship of each predictor with engagement reliably.

The second regression uses Learner Engagement to estimate Training Effectiveness. Its R squared of .633 means engagement is associated with 63.3 per cent of variation in reported training effectiveness. This is an association, not a causal conclusion.

## 7. Review Response Quality

| Check | Result |
| --- | ---: |
| Missing Likert responses in eligible records | 0 |
| Invalid numerical codes | 0 |
| Exact duplicates | 0 |
| Same-answer patterns across all 26 items | 5 |

The five same-answer records are retained. Four used Strongly Agree throughout and one used Strongly Disagree throughout. There is no objective evidence that they are invalid. Their presence is disclosed so the guide can interpret the interim findings with appropriate caution.

## 8. Suggested Explanation for the Guide

“I first retained only employees who confirmed that they attended a hybrid programme. I converted each Likert response from 1 to 5, grouped the relevant questions into four construct averages, and then calculated frequencies, means, reliability, correlations, and regressions. Because the first 22 eligible responses show unusually high similarity between Hybrid Learning and Trainer Competence, I am treating the results as a preliminary demonstration of the method, not final findings.”

The final analysis will repeat these steps with the complete eligible sample.
