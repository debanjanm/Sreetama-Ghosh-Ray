# Stage 1 Data Freeze

**Status:** Complete for guide review  
**Frozen dataset date:** 2026-09-24  
**Purpose:** Establish the auditable input dataset before Chapter 3 reporting and before any statistical analysis.

## Authoritative inputs

- [Verified manual JSON records](../02-collection-sources/json-records/imputed) — 70 paper questionnaires manually rectified and verified.
- [Original Google Forms export](<../02-collection-sources/online-export/Hybrid Learning and Training Effectiveness at Union Bank of India (Responses).xlsx>) — 62 online submissions.
- [Paper questionnaire scan](../02-collection-sources/paper-scan/QUESTIONNAIRE_SCAN.pdf) — source record for the manual forms.

The manual JSON files are the authoritative cleaned transcription of paper responses. The online JSON records were checked against every row and scored response in the original Google Forms workbook. The audit found **0 mismatch(es)**.

## Final response disposition

| Collection mode | Received | Profile-complete retained | Excluded |
|---|---:|---:|---:|
| Manual questionnaire | 70 | 54 | 16 |
| Google Forms | 62 | 49 | 13 |
| **Total** | **132** | **103** | **29** |

The final inclusion rule requires Q1 = Yes, completed age group, completed service length, completed job level, and all 26 scored answers. The 29 excluded records comprise 16 No responses, 11 forms with blank or unreadable eligibility responses, and 2 otherwise eligible manual records with a required profile field blank (Manual-25 and Manual-37).

## Files created in this freeze

- [Response register](response-register.csv): all 132 submissions, inclusion decision, source reference, exclusions, flags, and imputation metadata.
- [Eligible responses](eligible-responses.csv): the 103 profile-complete records, profile fields, and 26 numeric Likert values. No construct scores appear here yet.
- [Codebook](codebook.md): variable names, coding, constructs, and item wording.
- [Data-quality audit](data-quality-audit.md): reconciliation and structural checks.
- [Input fingerprint manifest](input-manifest.sha256): SHA-256 fingerprints of the original workbook, questionnaire scan, and all verified manual JSON files.

## Boundaries for the next stage

This freeze does not decide hypothesis outcomes or remove similar anonymous response patterns. Stage 2 will use these exact counts and rules to complete the actual data-collection and processing sections of Chapter 3. Stage 3 will calculate construct scores from eligible-responses.csv.
