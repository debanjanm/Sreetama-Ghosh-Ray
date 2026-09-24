# Final Analysis Dataset Codebook

## Dataset scope

The dataset contains 105 eligible, anonymous response records. It preserves the two previously documented within-construct item imputations. Age group and service-length blanks remain blank and are not imputed. Dash variants in age and service categories are standardised only in this analysis copy; the Stage 1 freeze retains the original entries.

## Response coding

| Value | Meaning |
|---:|---|
| 1 | Strongly Disagree |
| 2 | Disagree |
| 3 | Neither Agree nor Disagree |
| 4 | Agree |
| 5 | Strongly Agree |

## Construct-score rules

| Variable | Items | Calculation | Interpretation |
|---|---|---|---|
| Hybrid_Learning | HL1, HL2, HL3, HL4, HL5, HL6, HL7 | Arithmetic mean of assigned items | Higher score = more positive reported perception |
| Trainer_Competence | TC1, TC2, TC3, TC4, TC5, TC6 | Arithmetic mean of assigned items | Higher score = more positive reported perception |
| Learner_Engagement | LE1, LE2, LE3, LE4, LE5, LE6 | Arithmetic mean of assigned items | Higher score = more positive reported perception |
| Training_Effectiveness | TE1, TE2, TE3, TE4, TE5, TE6, TE7 | Arithmetic mean of assigned items | Higher score = more positive reported perception |

## Variables

| Variable | Description |
|---|---|
| response_id | Anonymous source record identifier. |
| source | Collection mode: manual or digital. |
| age_group | Respondent-selected age category, standardised only for dash variants; blank values are retained as missing. |
| service_length | Respondent-selected Union Bank service category, standardised only for dash variants and one omitted word; blank values are retained as missing. |
| job_level | Respondent-selected job-level category. |
| imputation_count | Number of documented item imputations in the record. |
| flag_count | Number of retained record flags. |
| HL1 | The digital and face-to-face parts were one connected learning experience. |
| HL2 | Digital activities prepared the respondent for face-to-face sessions. |
| HL3 | Face-to-face sessions clarified or applied digital learning. |
| HL4 | The digital platform was accessible without much difficulty. |
| HL5 | The digital platform was easy to navigate. |
| HL6 | Digital learning materials were available when needed. |
| HL7 | Digital modules or materials could be revisited for revision. |
| TC1 | The trainer had good subject knowledge. |
| TC2 | The trainer explained content clearly. |
| TC3 | The trainer explained how digital and face-to-face activities connected. |
| TC4 | The trainer used programme digital tools effectively. |
| TC5 | The trainer encouraged questions and participation. |
| TC6 | The trainer gave helpful feedback. |
| LE1 | The respondent stayed attentive during training activities. |
| LE2 | The respondent made a serious effort to understand the content. |
| LE3 | The respondent participated actively in activities. |
| LE4 | The respondent felt involved in the learning process. |
| LE5 | The respondent asked questions or sought clarification. |
| LE6 | The respondent remained interested in completing the programme. |
| TE1 | The respondent understood the main knowledge or skills. |
| TE2 | The training provided useful knowledge or skills for the current role. |
| TE3 | The programme content was relevant to Bank work. |
| TE4 | The respondent felt capable of using the taught knowledge or skills. |
| TE5 | The respondent applied learning in day-to-day work. |
| TE6 | The programme helped with relevant work tasks or problems. |
| TE7 | The programme improved confidence in relevant work responsibilities. |
