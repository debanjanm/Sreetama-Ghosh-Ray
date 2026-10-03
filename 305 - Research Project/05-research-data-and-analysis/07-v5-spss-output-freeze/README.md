# Version 5 SPSS Output Freeze

## Purpose

This folder preserves the SPSS output used as the Version 5 analytical result source. It is an output freeze, not a reconstructed case-level dataset.

## Preserved Source

- [SPSS output archive](source/ANALYSISS RESEARCH FINAL ONE.spv.zip)
- [SHA-256 fingerprint](source/SHA256SUMS.txt)

The output was created by SPSS Statistics 23 on 3 October 2026.

## Confirmed Analytical Model

- **Dependent variable:** `TETMEAN` — Training Effectiveness
- **Independent variables:** `HLTMEAN` — Hybrid Learning; `TCTMEAN` — Trainer Competence; `LETMEAN` — Learner Engagement
- **Regression sample:** 102 valid cases
- **Model summary:** R = .779699; R² = .607931; adjusted R² = .595929; standard error = .530877
- **ANOVA:** F(3, 98) = 50.651988; p < .001

## Data Boundary

The earlier verified CSV contains 103 profile-complete response records. The supplied SPSS output uses 102 cases because one record had a missing Trainer Competence mean in the SPSS analysis file. This folder does not replace or modify the original 103-record CSV, raw questionnaire records, or Version 4 analysis.

## Reliability Boundary

The supplied output contains one 26-item reliability analysis: Cronbach’s alpha = .980239. It does not contain four separate construct-specific reliability analyses. Version 5 will describe this result only as overall questionnaire consistency.
