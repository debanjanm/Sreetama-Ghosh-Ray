# Final Data Analysis Protocol

## Purpose

This protocol governs the final analysis after data collection closes. It does not contain final findings.

## 1. Freeze and Preserve Data

1. Record the collection closing date.
2. Preserve the original Google Forms export, paper questionnaire scans, and manual and digital JSON files without alteration.
3. Create a final master workbook with separate raw-data, eligibility-audit, cleaned-data, codebook, construct-score, table, and chart sheets.
4. Record paper and online responses separately before combining eligible records for analysis.

## 2. Eligibility and Missing-Data Rules

- Include only `Q1 = Yes` records.
- Exclude `Q1 = No` and blank-Q1 records.
- Code Likert responses as 1 = Strongly Disagree through 5 = Strongly Agree.
- For one blank or unclear Likert item in an otherwise eligible record, replace the item with the respondent’s arithmetic mean for the remaining items in that construct and flag it in the audit.
- Exclude records with two or more blank or unclear Likert items.
- Retain straight-line response patterns unless direct evidence shows that a response is invalid.
- Do not treat matching anonymous paper and online answers as duplicates without clear evidence.

## 3. Construct Scores

| Construct | Items | Score |
| --- | --- | --- |
| Hybrid Learning | Q5–Q11 | Arithmetic mean of seven items |
| Trainer Competence | Q12–Q17 | Arithmetic mean of six items |
| Learner Engagement | Q18–Q23 | Arithmetic mean of six items |
| Training Effectiveness | Q24–Q30 | Arithmetic mean of seven items |

## 4. Final Analysis

- Produce frequencies, percentages, bar charts, and short interpretations for Q2–Q30.
- Calculate item and construct means and standard deviations.
- Calculate Cronbach’s alpha for each construct.
- Test H1–H3 through Pearson correlation at the 5 per cent significance level.
- Run the two-predictor regression: Hybrid Learning and Trainer Competence in relation to Learner Engagement. Report model summary, ANOVA, coefficients, tolerance, and VIF.
- Run the simple regression: Learner Engagement in relation to Training Effectiveness. Report model summary, ANOVA, and coefficients.
- Verify final descriptive and inferential statistics in SPSS using the same cleaned dataset and coding.

## 5. Reporting Boundary

Report associations in the retained eligible sample. Do not claim causation, formal mediation, bank-wide representation, or organisation-level performance effects.
