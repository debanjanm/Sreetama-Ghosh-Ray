# Chapter 4 — Data Analysis and Interpretation

## 4.1 Introduction

This chapter presents the results recorded in the supplied SPSS Statistics 23 output. The main analysis concerns the extent to which Hybrid Learning, Trainer Competence, and Learner Engagement jointly predict Training Effectiveness among the selected Union Bank respondents.

The SPSS output uses 102 valid cases for the construct-level exploration and multiple-regression model. Some item-level and pairwise outputs use 103 or 102 cases because SPSS applies the available-case rule for those procedures. The number reported beside each table is therefore retained exactly as it appears in the output.

The results describe the selected respondent group. They show reported associations and prediction within this sample; they do not establish that one part of training causes another.

## 4.2 Construct-Level Descriptive Results

SPSS *Explore* output was used to examine the four construct means together. All construct means are above the midpoint of the five-point response scale. Learner Engagement has the highest mean, followed by Training Effectiveness, Trainer Competence, and Hybrid Learning.

**Table 4.1: Construct-level descriptive statistics from SPSS Explore output**

| Construct | Valid N | Mean | Standard deviation | Minimum | Maximum | Skewness | Kurtosis |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Hybrid Learning | 102 | 4.148 | 0.859 | 1.000 | 5.000 | -1.818 | 4.058 |
| Trainer Competence | 102 | 4.158 | 0.863 | 1.000 | 5.000 | -2.109 | 5.583 |
| Learner Engagement | 102 | 4.317 | 0.793 | 1.000 | 5.000 | -2.131 | 6.236 |
| Training Effectiveness | 102 | 4.254 | 0.835 | 1.000 | 5.000 | -2.035 | 5.275 |

*Source: Supplied SPSS Statistics 23 output, Explore procedure.*

The scores are concentrated toward agreement and strong agreement. This produces the negative skewness values shown in Table 4.1. The result is understandable in a voluntary, self-report study of employees who had completed a recent hybrid-training programme, but it also means that the sample contains fewer low ratings than high ratings.

Hybrid Learning has the lowest construct mean, though it remains above the neutral point. This indicates that respondents generally viewed the mixed digital and face-to-face arrangement positively, while leaving more room for improvement than the other three areas. Learner Engagement has the highest mean. In practical terms, respondents generally reported attention, participation, and interest in the programme selected for the questionnaire.

## 4.3 Distribution Diagnostics and SPSS Figures

The SPSS output contains histograms, normal Q–Q plots, detrended Q–Q plots, and boxplots for all four construct means. It also contains a regression residual histogram, normal P–P plot, and residual scatterplot. These are native SPSS graphics and are retained in the frozen output archive.

Normality tests in the Explore output are statistically significant for all four construct means. This is consistent with the visibly negatively skewed five-point ratings. The graphics were reviewed as distribution diagnostics rather than as evidence that the results represent a normally distributed population. The main regression results are therefore interpreted cautiously and together with the bounded Likert-scale nature of the data.

The figure locations are listed in the [SPSS figure index](spss-output-figure-index.md). The figures should be exported directly from the saved SPSS output if they are inserted into a Word thesis. No chart in this Version 5 chapter was redrawn from a different data file.

## 4.4 Overall Questionnaire Consistency and Exploratory Structure Check

The SPSS reliability output reports one Cronbach’s alpha for the full set of 26 Likert-scale questions. The output includes 102 valid cases and excludes one case from this reliability run.

**Table 4.2: Overall questionnaire consistency**

| Item set | Number of items | Valid cases | Excluded cases | Cronbach’s alpha |
| --- | ---: | ---: | ---: | ---: |
| All scored questionnaire items | 26 | 102 | 1 | .980 |

*Source: Supplied SPSS Statistics 23 reliability output.*

The alpha value indicates very high internal consistency for the complete questionnaire item set. It should not be read as four separate reliability values because the supplied output contains only one combined reliability analysis. The high value also suggests that several items are closely related, which is useful for consistency but should be considered when interpreting relationships between constructs measured in the same response form.

An exploratory Principal Component Analysis with varimax rotation was also included in the SPSS output. The Kaiser–Meyer–Olkin value is .929, and Bartlett’s test of sphericity is statistically significant, χ²(325) = 3664.340, *p* < .001. SPSS extracted four components. This output is treated as a supporting structural check because the questionnaire was designed from the four theory-based constructs. It is not used to rename constructs, claim full scale validation, or change the stated study model.

## 4.5 Correlation Analysis

Pearson correlations describe the direction and strength of association between the construct means. All reported correlations are positive and statistically significant.

**Table 4.3: Pearson correlations among study constructs**

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

## 4.6 Multiple Regression Analysis

The main hypothesis was tested through a multiple regression model with Training Effectiveness as the dependent variable and Hybrid Learning, Trainer Competence, and Learner Engagement as the three predictors.

**Table 4.4: Overall multiple-regression model**

| R | R² | Adjusted R² | Standard error of estimate | F | df | Significance |
| ---: | ---: | ---: | ---: | ---: | --- | ---: |
| .780 | .608 | .596 | .531 | 50.652 | 3, 98 | < .001 |

*Source: Supplied SPSS Statistics 23 regression output; dependent variable: Training Effectiveness; valid N = 102.*

The overall regression model is statistically significant, *F*(3, 98) = 50.652, *p* < .001. Together, Hybrid Learning, Trainer Competence, and Learner Engagement account for 60.8 per cent of the variation in reported Training Effectiveness within the 102 SPSS cases. The alternative hypothesis is therefore supported at the model level.

**Table 4.5: Predictor coefficients for Training Effectiveness**

| Predictor | Unstandardised B | Standard error | Standardised beta | *t* | Significance |
| --- | ---: | ---: | ---: | ---: | ---: |
| Constant | .599 | .301 | — | 1.991 | .049 |
| Hybrid Learning | .188 | .112 | .194 | 1.681 | .096 |
| Trainer Competence | .109 | .115 | .113 | .947 | .346 |
| Learner Engagement | .560 | .105 | .532 | 5.346 | < .001 |

*Source: Supplied SPSS Statistics 23 regression coefficients table; dependent variable: Training Effectiveness; valid N = 102.*

When the three predictors are considered together, Learner Engagement is the only individually statistically significant predictor of Training Effectiveness (*β* = .532, *p* < .001). Its positive coefficient means that higher reported engagement is associated with higher reported training effectiveness after the overlap with Hybrid Learning and Trainer Competence is considered.

Hybrid Learning and Trainer Competence have positive coefficients, but their individual coefficients are not statistically significant in this combined model. This does not show that either area is unimportant. Both are strongly related to the other constructs in the correlation results, particularly to each other. The regression result simply shows that, in this respondent group and with all three predictors entered at the same time, Learner Engagement has the clearest unique association with perceived Training Effectiveness.

The supplied regression command does not include collinearity statistics. Therefore, this chapter does not report VIF or tolerance values. The strong Hybrid Learning–Trainer Competence correlation is instead shown directly in Table 4.3 and considered when interpreting the coefficient pattern.

## 4.7 Interpretation of the Main Finding

The key result is not that a digital platform or a trainer alone determines training effectiveness. Rather, respondents who were more actively involved in their selected programme also reported stronger learning relevance, confidence, and work application. In a bank setting, active involvement can include asking questions, practising a process, following a live or classroom session, revisiting material, and connecting the programme with regular work responsibilities.

Hybrid Learning still matters in the result pattern. Its mean is positive, it is positively associated with Training Effectiveness, and it is closely linked with Trainer Competence and Learner Engagement. The lower Hybrid Learning mean points to practical review areas such as clear digital preparation before a session, access to material, and the connection between online content and trainer-led activity. These are areas for training review, not proven interventions.

The correlation and regression findings should be read together. Correlation shows that each construct moves positively with Training Effectiveness. Regression asks a narrower question: which predictor still makes a distinct statistical contribution after the other two are already in the model? In this output, Learner Engagement provides that distinct contribution.

## 4.8 Chapter Summary

The SPSS output shows positive ratings across the four constructs and a statistically significant three-predictor model for Training Effectiveness. The model explains 60.8 per cent of the variation in reported Training Effectiveness among the 102 valid SPSS cases. Learner Engagement is the only individually significant predictor after Hybrid Learning and Trainer Competence are entered together. Chapter 5 discusses the contribution, practical implications, limitations, and suggestions arising from these findings.
