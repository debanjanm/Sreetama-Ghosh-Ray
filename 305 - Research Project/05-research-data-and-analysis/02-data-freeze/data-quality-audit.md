# Stage 1 Data Quality Audit

## Scope

This audit freezes the cleaned paper-questionnaire records in chapter-3/appendix/imputed/ and reconciles the online records with the original Google Forms workbook. It does not calculate construct scores, reliability, correlations, or regressions.

## Reconciliation result

| Check | Result |
|---|---:|
| Verified manual JSON records | 70 |
| Google Forms workbook records | 62 |
| Digital JSON records reconciled to workbook rows | 62 |
| Digital JSON/workbook mismatches | 0 |
| Total submitted records | 132 |
| Eligible retained records | 105 |
| Excluded records | 27 |

## Eligibility disposition

| Collection mode | Q1 = Yes / retained | Q1 = No / excluded | Q1 blank or illegible / excluded | Total |
|---|---:|---:|---:|---:|
| Manual | 56 | 3 | 11 | 70 |
| Google Forms | 49 | 13 | 0 | 62 |
| **Total** | **105** | **16** | **11** | **132** |

## Retained-record checks

| Check | Result |
|---|---:|
| Retained records with all 26 item fields | 105 |
| Invalid retained Likert values | 0 |
| Missing retained profile values: age / service / job level | 2 / 1 / 0 |
| Retained records with documented imputation | 2 |
| Exact 26-item response-pattern groups with more than one record | 3 |
| Records within those repeated patterns | 19 |

## Imputation log

| Record | Item | Value used | Basis |
|---|---|---:|---|
| Manual-25 | HL6 | 3.333 | Arithmetic mean of the respondent’s remaining six Hybrid Learning items. |
| Manual-46 | HL4 | 4.000 | Arithmetic mean of the respondent’s remaining six Hybrid Learning items. |

## Interpretation

All retained records meet the Stage 1 structural requirements: Q1 eligibility is Yes, the 26 scored items are present, and their values fall within the permitted 1–5 scale. The two documented imputed values follow the pre-specified within-construct mean rule.

Repeated anonymous answer patterns are recorded for later sensitivity review but are not removed at this stage. They may represent genuine similar responses and cannot be treated as duplicate respondents without identifying evidence.

The 13 Google Forms exclusions and the 14 manual exclusions remain in response-register.csv; they are not included in eligible-responses.csv.
