# Chapter 4 — Data Analysis and Interpretation

This chapter presents the SPSS Statistics 23 results. The main analysis concerns the extent to which Hybrid Learning, Trainer Competence, and Learner Engagement jointly predict Training Effectiveness among the selected Union Bank respondents.

The SPSS output uses 102 valid cases for the construct-level exploration and multiple-regression model. Some item-level and pairwise outputs use 103 or 102 cases because SPSS applies the available-case rule for those procedures. Each table states the number of cases used for that analysis.

The results describe the selected respondent group. They show reported associations and prediction within this sample; they do not establish that one part of training causes another.

## 4.1 Descriptive Analysis

### 4.1.1 Construct-Level Results

SPSS *Explore* output was used to examine the four construct means together. All construct means are above the midpoint of the five-point response scale. Learner Engagement has the highest mean, followed by Training Effectiveness, Trainer Competence, and Hybrid Learning.

**Table 4.1: Construct-level descriptive statistics from SPSS Explore output**

| Construct | Valid N | Mean | Standard deviation | Minimum | Maximum | Skewness | Kurtosis |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Hybrid Learning | 102 | 4.148 | 0.859 | 1.000 | 5.000 | -1.818 | 4.058 |
| Trainer Competence | 102 | 4.158 | 0.863 | 1.000 | 5.000 | -2.109 | 5.583 |
| Learner Engagement | 102 | 4.317 | 0.793 | 1.000 | 5.000 | -2.131 | 6.236 |
| Training Effectiveness | 102 | 4.254 | 0.835 | 1.000 | 5.000 | -2.035 | 5.275 |

*Source: Supplied SPSS Statistics 23 output, Explore procedure.*

Responses were concentrated toward agreement and strong agreement, producing the negative skewness shown in Table 4.1. Fewer employees gave low ratings. The survey does not establish why they responded this way.

Hybrid Learning has the lowest construct mean, though it remains above the neutral point. This indicates that respondents generally viewed the mixed digital and face-to-face arrangement positively, while leaving more room for improvement than the other three areas. Learner Engagement has the highest mean. In practical terms, respondents generally reported attention, participation, and interest in the programme selected for the questionnaire.

### 4.1.2 Hybrid Learning Item Results

The seven Hybrid Learning items describe the connection between digital and face-to-face activities and access to the digital material. Table 4.2 reports their means from the SPSS item-descriptives output. These item results use 103 valid responses, while Table 4.1 uses the 102 cases available together across all four construct means.

**Table 4.2: Hybrid Learning item means**

| Question | Item focus | Valid N | Mean |
| --- | --- | ---: | ---: |
| Q5 | Digital and face-to-face parts planned as one experience | 103 | 4.107 |
| Q6 | Digital activities prepared the respondent for face-to-face sessions | 103 | 3.990 |
| Q7 | Face-to-face sessions clarified or applied digital learning | 103 | 4.165 |
| Q8 | Access to the digital platform | 103 | 4.184 |
| Q9 | Ease of platform navigation | 103 | 4.107 |
| Q10 | Availability of digital learning materials | 103 | 4.223 |
| Q11 | Access to digital material for revision | 103 | 4.262 |

*Source: SPSS Statistics 23 item descriptives; item wording is given in Appendix A.*

Q6 has the lowest mean among the seven Hybrid Learning items. It asks whether digital activities prepared the respondent for the face-to-face sessions. The mean of 3.990 remains positive, but it points to a part of the learning sequence that could be reviewed in future programmes.

### 4.1.3 Distribution Diagnostics

SPSS generated histograms, normal Q–Q plots and boxplots for the four construct means. The regression output also includes residual plots. Together with the negative skewness shown in Table 4.1, these graphics show that ratings were concentrated toward the higher end of the scale.

Normality tests in the Explore output are statistically significant for all four construct means, consistent with the negatively skewed ratings. The plots serve as distribution diagnostics. The regression results are interpreted in light of the bounded five-point scale and the concentration of positive responses.

### 4.1.4 Overall Questionnaire Consistency and Exploratory Structure Check

The reliability analysis reports one Cronbach’s alpha for the full set of 26 Likert-scale questions. The output includes 102 valid cases and excludes one case from this reliability run.

**Table 4.3: Overall questionnaire consistency**

| Item set | Number of items | Valid cases | Excluded cases | Cronbach’s alpha |
| --- | ---: | ---: | ---: | ---: |
| All scored questionnaire items | 26 | 102 | 1 | .980 |

*Source: Supplied SPSS Statistics 23 reliability output.*

The alpha value indicates very high internal consistency for the complete questionnaire item set. It should not be read as four separate reliability values because the supplied output contains only one combined reliability analysis. The high value also suggests that several items are closely related, which is useful for consistency but should be considered when interpreting relationships between constructs measured in the same response form.

Principal Component Analysis with varimax rotation provided an exploratory check of the item structure. The Kaiser–Meyer–Olkin value is .929, and Bartlett’s test of sphericity is statistically significant, χ²(325) = 3664.340, *p* < .001. SPSS extracted four components. This output is treated as a supporting structural check because the questionnaire was designed from the four theory-based constructs. It is not used to rename constructs, claim full scale validation, or change the stated study model.

## 4.2 Inferential Analysis

### 4.2.1 Correlation Analysis

Pearson correlations describe the direction and strength of association between the construct means. All reported correlations are positive and statistically significant.

**Table 4.4: Pearson correlations among study constructs**

| Pair of constructs | Pearson’s *r* | Valid N | Significance |
| --- | ---: | ---: | ---: |
| Hybrid Learning and Trainer Competence | .818 | 102 | < .001 |
| Hybrid Learning and Learner Engagement | .713 | 103 | < .001 |
| Hybrid Learning and Training Effectiveness | .659 | 103 | < .001 |
| Trainer Competence and Learner Engagement | .746 | 102 | < .001 |
| Trainer Competence and Training Effectiveness | .668 | 102 | < .001 |
| Learner Engagement and Training Effectiveness | .765 | 103 | < .001 |

*Source: Supplied SPSS Statistics 23 correlation output.*

The strongest association with Training Effectiveness is Learner Engagement (*r* = .765). Employees who reported greater attention, participation, and involvement also tended to report stronger perceived training effectiveness. Hybrid Learning and Trainer Competence are themselves strongly associated (*r* = .818). This suggests that respondents often experienced well-connected hybrid learning and effective trainer facilitation together. It also means that their separate contributions must be assessed with care when all three predictors are entered into one regression model.

### 4.2.2 Multiple Regression Analysis

The main hypothesis was tested through a multiple regression model with Training Effectiveness as the dependent variable and Hybrid Learning, Trainer Competence, and Learner Engagement as the three predictors.

**Table 4.5: Overall multiple-regression model**

| R | R² | Adjusted R² | Standard error of estimate | F | df | Significance |
| ---: | ---: | ---: | ---: | ---: | --- | ---: |
| .780 | .608 | .596 | .531 | 50.652 | 3, 98 | < .001 |

*Source: Supplied SPSS Statistics 23 regression output; dependent variable: Training Effectiveness; valid N = 102.*

The overall regression model is statistically significant, *F*(3, 98) = 50.652, *p* < .001. Together, Hybrid Learning, Trainer Competence, and Learner Engagement account for 60.8 per cent of the variation in reported Training Effectiveness within the 102 cases. The alternative hypothesis is therefore supported at the model level.

**Table 4.6: Predictor coefficients for Training Effectiveness**

| Predictor | Unstandardised B | Standard error | Standardised beta | *t* | Significance |
| --- | ---: | ---: | ---: | ---: | ---: |
| Constant | .599 | .301 | — | 1.991 | .049 |
| Hybrid Learning | .188 | .112 | .194 | 1.681 | .096 |
| Trainer Competence | .109 | .115 | .113 | .947 | .346 |
| Learner Engagement | .560 | .105 | .532 | 5.346 | < .001 |

*Source: Supplied SPSS Statistics 23 regression coefficients table; dependent variable: Training Effectiveness; valid N = 102.*

When the three predictors are considered together, Learner Engagement is the only individually statistically significant predictor of Training Effectiveness (*β* = .532, *p* < .001). Its positive coefficient means that higher reported engagement is associated with higher reported training effectiveness after the overlap with Hybrid Learning and Trainer Competence is considered.

Hybrid Learning and Trainer Competence have positive coefficients, but their individual coefficients are not statistically significant in this combined model. This does not show that either area is unimportant. Both are strongly related to the other constructs in the correlation results, particularly to each other. The regression result simply shows that, in this respondent group and with all three predictors entered at the same time, Learner Engagement has the clearest unique association with perceived Training Effectiveness.

The regression output did not include VIF or tolerance statistics. The strong Hybrid Learning–Trainer Competence correlation is shown in Table 4.4 and considered when interpreting the coefficient pattern.

## 4.3 Interpretation of Results

Respondents who were more actively involved in their selected programme also reported stronger learning relevance, confidence, and work application. In a bank setting, active involvement can include asking questions, practising a process, following a live or classroom session, revisiting material, and connecting the programme with regular work responsibilities.

Hybrid Learning received positive ratings and was positively associated with Training Effectiveness. Table 4.2 shows where respondents were least positive: preparation through digital activities before a face-to-face session. For a bank employee, this could mean starting the live session without enough time or guidance to use the earlier material. The survey does not identify the exact reason; it identifies a useful question for programme review.

The correlation and regression findings should be read together. Correlation shows that each construct moves positively with Training Effectiveness. Regression asks a narrower question: which predictor still makes a distinct statistical contribution after the other two are already in the model? Here, Learner Engagement provides that distinct contribution.

## 4.4 Comparison with Previous Studies

Sosnova et al. (2025) examined hybrid methods and learning effectiveness among higher-education students. The positive ratings in the present study are broadly compatible with their interest in connected learning activities, but the two studies used different populations and outcome measures. The Union Bank survey did not compare a hybrid group with a classroom-only group.

Kim (2022) found that training delivery, instructor involvement and programme design mattered in automotive sales training. Kim also reported that the hybrid group did not outperform the traditional group in every comparison. The present findings similarly suggest that the quality of the learning experience deserves attention: Hybrid Learning and Trainer Competence were positively correlated with Training Effectiveness, while Learner Engagement had the clearest separate coefficient in the combined model. These are employee perceptions from one banking sample, so they cannot reproduce Kim's comparison of delivery methods.

Bahl, Kiran and Sharma (2024) showed the value of evaluating training among Indian bank employees through Kirkpatrick's framework. The present study adds a narrower view of one hybrid programme, with employees reporting understanding, relevance and use of learning in their own roles. It did not measure Kirkpatrick's full results level or objective work performance. Mulaudzi's (2021) workplace study also highlights access and practical barriers; the lower digital-preparation item in Table 4.2 makes that issue worth examining in the Bank's training process.

## 4.5 Theoretical and Practical Implications

The three predictors had a significant joint relationship with perceived Training Effectiveness. This supports examining programme design, trainer support and employee involvement together in workplace hybrid learning. Their high correlations also show why a positive pairwise relationship should not be confused with a separate contribution after the other predictors are entered into the regression. The findings do not establish a causal order among the three predictors.

For the Bank, the most immediate review point is the handover from digital preparation to the face-to-face session. Programme coordinators could check when preparatory material reaches employees, how the trainer refers to it, and whether employees can make time to use it. Trainers could also give employees practical chances to ask questions and practise. These suggestions follow the response pattern, especially Q6 and the strong association of Learner Engagement with Training Effectiveness; they have not been tested as interventions in this study.
