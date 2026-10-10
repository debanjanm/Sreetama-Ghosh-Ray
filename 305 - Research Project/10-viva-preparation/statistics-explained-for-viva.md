# The statistics in this thesis, explained from scratch

For Sreetama. This guide follows the 90-page `hybrid-learning-training-effectiveness-third-draft-final-v4.pdf`. It explains the methods reported there in everyday language. Some sections below are data-preparation steps or ways of reading a result, rather than separate statistical tests.

**The data sources matter.** SPSS reported the principal construct summaries, correlations, one overall 26-item reliability result, exploratory component analysis, and the main regression. The respondent-profile table and supplementary item and group comparisons were prepared from a selected 102-record scored file. Some SPSS item means and pairwise correlations used 103 available cases. The thesis identifies these sources beside its tables; without the matching SPSS data file, their person-by-person agreement has not been verified. The **hypothesis decision comes only from the 102-case SPSS multiple regression**.

### Complete technique list

| Purpose | Techniques actually reported |
| --- | --- |
| Describe respondents and answers | Frequencies, percentages, minimum and maximum, mean, standard deviation, item distributions, and charts |
| Inspect score shape | Skewness, kurtosis, histograms, boxplots, Q–Q plots, and normality tests |
| Check the questionnaire | Cronbach’s alpha; exploratory Principal Component Analysis with varimax rotation, KMO, and Bartlett’s test |
| Examine relationships and the main hypothesis | Pearson correlation and three-predictor multiple regression, including R², adjusted R², F-test, coefficients, *t*-tests, and *p*-values |
| Supplementary comparisons | One-sample *t*-tests, paired *t*-tests, Welch’s two-group *t*-test, and one-way ANOVA |
| Check whether a categorical test is usable | Crosstabs, expected cell counts, and Pearson chi-square; the reported tables were too sparse for a reliable chi-square conclusion |

Sampling, eligibility screening, coding, construct averages, and listwise deletion are also explained below because they determine which answers entered each calculation.

---

## The whole story in four steps

1. **Collect** opinions from bank employees on a 1–5 scale.
2. **Describe** them: who answered, and what is the typical answer?
3. **Check the questionnaire**: do the questions behave like a sensible measuring tool?
4. **Test the idea**: do connected learning (Hybrid Learning), a good trainer (Trainer Competence) and personal involvement (Learner Engagement) go together with feeling that training worked (Training Effectiveness)?

Everything below belongs to one of those steps.

---

## A. Getting the data ready

### 1. Likert scale and coding
- **What it is:** a rating question ("Strongly disagree" to "Strongly agree"), turned into numbers 1 to 5.
- **Picture:** a restaurant feedback card with five smileys. We give each smiley a number so it can be averaged.
- **In your study:** 26 statements (Q5–Q30) were scored 1–5.
- **Say:** "Each answer was coded from 1 for strongly disagree to 5 for strongly agree."

### 2. Construct score (the average of the questions)
- **What it is:** one score per idea, made by averaging the questions that measure it. Hybrid Learning is the average of 7 questions, Trainer Competence of 6, Learner Engagement of 6, Training Effectiveness of 7.
- **Picture:** your semester result is the average of several subject marks. One mark per subject would be too many to talk about.
- **Tiny calculation:** if the seven Hybrid Learning answers were 4, 5, 4, 3, 4, 5 and 4, the construct score would be (4 + 5 + 4 + 3 + 4 + 5 + 4) ÷ 7 = **4.14**. This is only an illustration, not a quoted respondent.
- **Say:** "Each construct score is the arithmetic mean of its items."

### 3. Purposive (non-probability) sampling and eligibility
- **What it is:** choosing people because they fit a condition, not at random.
- **Picture:** to judge a workshop, you ask only the people who attended it. Asking everyone in the bank would not make sense.
- **In your study:** only employees who attended a programme that had both online and classroom parts could answer. 132 forms came in, 103 were complete, and 102 were used in the main test.
- **Say:** "Because the sample is not random, the results describe these respondents and cannot be generalised to the whole Bank."

### 4. Valid cases and listwise deletion
- **What it is:** if a record lacks a value required for one analysis, SPSS omits that record from that analysis. It can still appear in a different analysis that has all the values it needs.
- **Picture:** a bank loan calculation may need income and existing debt. A record missing debt cannot enter that calculation, even though its age can still be counted in an age table.
- **In your study:** SPSS used 102 cases for the main model because one record had no Trainer Competence score in the analysis file. Some item-level tables use 103.
- **Say:** "The regression ran on 102 valid cases after SPSS dropped one record with a missing construct mean."

---

## B. Describing the data

### 5. Frequency and percentage
- **What it is:** how many people gave each answer, and what share of the group that is.
- **Picture:** counting how many classmates prefer tea, coffee or juice.
- **Tiny calculation:** 56 of 102 respondents were aged 35–44, so 56 ÷ 102 × 100 = **54.9%**.
- **In your study:** age 35–44 was the largest group, 56 people or 54.9%. Officers were 56 people (54.9%), clerical 20 (19.6%) and managerial 26 (25.5%).
- **Say:** "Just over half the respondents were aged 35–44 and were officers."

### 6. Mean (the average)
- **What it is:** add everything up and divide by how many there are.
- **Picture:** if 5 friends share chocolates equally, the mean is what each one gets.
- **In your study:** Learner Engagement **4.317**, Training Effectiveness **4.254**, Trainer Competence **4.158**, and Hybrid Learning **4.148** in the SPSS construct summary. All are above the middle response value of 3.
- **Say:** "All four constructs were rated positively, with Learner Engagement the highest."

### 7. Standard deviation (how spread out the answers are)
- **What it is:** a measure of how spread out the answers are around the mean. It is calculated from squared differences, so it is not literally the average distance.
- **Picture:** two cricket teams each have five scores averaging 40. Team A scores 40, 40, 40, 40, 40. Team B scores 0, 20, 40, 60, 80. The means match, but Team B's scores are far more spread out. Standard deviation tells the teams apart.
- **In your study:** the four construct standard deviations were .793 to .863. Their ratings were not identical, even though the means were all high.
- **Say:** "The standard deviations, around 0.8, show that responses varied around each construct's average."

### 8. Minimum and maximum
- **What it is:** the lowest and highest observed scores. The SPSS construct summary lists 1 and 5 for each of the four construct means. These endpoints do not tell us how *many* respondents were there.

### 9. Skewness (is the pile lopsided?)
- **What it is:** whether answers bunch up on one side.
- **Picture:** a very easy exam where nearly everyone scores 90 or more and a few score low. The long thin tail points left. That is **negative skew**.
- **In your study:** skewness is between −1.8 and −2.1 for all constructs, because most people chose 4 or 5.
- **Say:** "The negative skewness reflects ratings clustered at the agree end of the scale."

### 10. Kurtosis (how tall and pointy the pile is)
- **What it is:** a summary of the shape of a distribution, especially its concentration and tails, compared with a normal curve. It is not simply a measure of how tall the centre is.
- **Picture:** two queues may have similar average wait times, but one has most waits close together and a few extreme waits. Kurtosis helps describe that difference in shape.
- **In your study:** the SPSS construct kurtosis values are 4.058 to 6.236. Read them together with the histograms and skewness rather than as a separate finding about effectiveness.

### 11. Charts: histogram, boxplot, Q–Q plot
- **Histogram:** bars showing how many people gave each score, like a classroom heights chart.
- **Boxplot:** a box holding the middle half of the answers, with a line for the median. Dots outside are unusual answers (outliers).
- **Q–Q plot:** dots that fall on a straight line mean the data look bell-shaped. Dots that bend away mean they do not.
- **In your study:** SPSS drew all three for the four construct scores.

### 12. Normality tests
- **What it is:** a test asking "do these scores follow the classic bell curve?" If the result is significant (p < .05), the answer is **no, they do not**.
- **Picture:** holding a bell-shaped cardboard cut-out over your histogram to see whether it fits.
- **In your study:** the reported tests were significant, agreeing with the visibly skewed scores. A normality test does not decide whether the training was effective; it only checks a distributional assumption.
- **Say:** "The construct scores depart from a normal bell shape, with many ratings near the favourable end of the five-point scale."

---

## C. Checking the questionnaire

### 13. Cronbach's alpha (do the questions hang together?)
- **What it is:** a measure of how consistently a set of questions varies across respondents. High alpha means people who rate some items highly also tend to rate the others highly. It does **not** prove that the questions measure the right concept.
- **Picture:** several thermometers rise and fall together when the room changes temperature. That consistency is useful, but if all are wrongly calibrated, agreement alone does not make them accurate.
- **Rule of thumb:** values around .70 are often treated as workable, but context matters; a value near 1 can indicate overlapping or repetitive questions.
- **In your study:** α = .980 for **all 26 questions pooled together** in the SPSS output. The 20-person pilot had separate preliminary block alphas from .879 to .929, but the final SPSS output did not report four separate construct alphas.
- **Important limit:** the .980 value is overall internal consistency for a mixed four-construct instrument. It does not establish the reliability or validity of each construct separately.
- **Say:** "The overall alpha of .980 shows very high internal consistency, but it is not a separate reliability value for each construct."

### 14. Principal Component Analysis (PCA) with varimax rotation, KMO and Bartlett's test
- **What it is:** PCA summarises many related item responses into a smaller number of components. Varimax rotation is a mathematical turn of the component axes that can make item patterns easier to read.
- **Picture:** imagine sorting 26 mixed documents into a few folders by how their contents tend to occur together. Rotation helps make the folder labels clearer; it does not guarantee that every document belongs in the intended folder.
- **KMO (.929):** checks whether the item correlations are suitable for this type of analysis. A high value supports proceeding.
- **Bartlett's test:** tests whether the correlation matrix differs from one with no relationships among items. It was significant here, χ²(325) = 3664.340, *p* < .001.
- **In your study:** SPSS extracted four components. That is consistent with the planned four-construct structure, but the thesis does not use this exploratory check as full validation of the questionnaire.
- **Say:** "The exploratory PCA extracted four components, but I do not claim it fully validates the four scales."

---

## D. Testing relationships

### 15. Hypothesis: the null and the alternative
- **Null hypothesis (H₀):** "nothing is going on." Here: the three predictors do not jointly predict Training Effectiveness.
- **Alternative hypothesis (H₁):** "something is going on." Here: they do.
- **Picture:** a courtroom. H₀ is "innocent until proven guilty". The data must give strong enough evidence to reject it.
- **In your study:** H₀ was rejected, so H₁ is supported.

### 16. Significance level (.05) and the p-value
- **p-value:** assuming the null hypothesis and the test assumptions hold, it tells us how unusual a result at least this extreme would be. It is **not** the probability that the null hypothesis is true.
- **Picture:** you toss a coin 10 times and get 10 heads. That would be very surprising for a fair coin, so you doubt the coin. A small p-value makes you doubt "no relationship".
- **Rule:** this thesis uses .05 as its decision threshold. If *p* is below .05, the result is called **statistically significant**; this does not tell us whether the relationship is important in practice.
- **In your study:** the reported correlations and overall regression have *p* < .001. Under the null model, results this extreme would be rare.
- **Say:** "A result is significant when p is below .05."

### 17. Pearson correlation (r)
- **What it is:** a number from −1 to +1 showing whether two things rise and fall together.
- **Picture:** ice-cream sales and temperature. When one goes up, so does the other (positive r). Umbrellas sold and sunny days move in opposite directions (negative r).
- **Strength:** values closer to −1 or +1 show a stronger straight-line relationship. Labels such as “weak” or “strong” are rough guides, not universal rules.
- **In your study:** all reported pairs are positive and significant. The strongest with Training Effectiveness is Learner Engagement (*r* = .765, pairwise N = 103). Hybrid Learning and Trainer Competence are strongly linked with each other (*r* = .818, pairwise N = 102). The different N values reflect available cases in those SPSS pairwise calculations.
- **Important:** correlation shows things go together. It does not show that one causes the other. Ice-cream does not cause sunburn. Both go up in summer.
- **Say:** "Learner Engagement has the strongest relationship with perceived effectiveness, but this is an association, not proof of cause."

---

## E. The main test: multiple regression

### 18. Multiple regression
- **What it is:** a method that relates one outcome to several predictors at the same time. It estimates each predictor's association after accounting for the others; a one-time survey cannot turn that association into a causal effect.
- **Picture:** predicting a student's exam score from study hours, attendance and interest in the subject. Regression says how well the three together predict the score, and which one matters most once the others are counted.
- **In your study:** the outcome is Training Effectiveness. The three predictors are Hybrid Learning, Trainer Competence and Learner Engagement.

The numbers it gives, one by one:

| Number | Plain meaning | Your value |
| --- | --- | --- |
| **R²** | The share of *observed variation in the outcome scores* accounted for by the fitted model within this sample. It is not a percentage of effectiveness caused by the predictors. | .608, so 60.8% |
| **Adjusted R²** | R² adjusted for the number of predictors and sample size; it reduces the automatic gain from adding variables. | .596 |
| **F-test** | "Do the predictors as a team do better than just guessing the average for everyone?" | F(3, 98) = 50.652, p < .001. Yes |
| **Degrees of freedom (3, 98)** | The first number is the three predictors. The second is the residual degrees of freedom: 102 cases − 3 predictors − 1 intercept = 98. | 3 and 98 |
| **B** (unstandardised) | The model's estimated difference in the outcome score for a one-point higher predictor score, *holding the other two predictor scores fixed*. It is an association, not a guaranteed change for a person. | Learner Engagement .560 |
| **β (beta, standardised)** | The estimated association after putting predictors on standard-deviation units so their coefficients can be compared. It is not a percentage. | LE .532, HL .194, TC .113 |
| **t and p for each predictor** | Tests whether that predictor's adjusted coefficient differs detectably from zero in this model. | Only Learner Engagement is individually significant (*p* < .001) |

- **What the result means in plain words:** the model accounts for 60.8% of the variation in reported effectiveness scores among these 102 cases. Only Learner Engagement has an individually significant coefficient after all three predictors are entered. Hybrid Learning (*p* = .096) and Trainer Competence (*p* = .346) do not meet the .05 threshold in that joint model.
- **Why might the two coefficients be nonsignificant?** The predictors share information. Hybrid Learning and Trainer Competence correlate at *r* = .818, so it is harder to separate their adjusted contributions. Think of two cooks who usually prepare the same dishes together: the meal's rating may be related to both, but one dinner cannot reveal each cook's distinct contribution. **Overlap is a plausible explanation, not a proven sole cause** of the two *p*-values; sampling variation also matters.
- **Multicollinearity and VIF:** multicollinearity means predictors are strongly related to each other. VIF is one diagnostic for how this can affect coefficient precision. The saved SPSS regression output did not report VIF, so the thesis relies on the observed predictor correlation and does not claim a VIF value.
- **Say:** "The overall model is significant and accounts for 60.8% of the score variation. Learner Engagement is the only individually significant predictor. The other predictors are related to the outcome in pairwise tests, but their separate adjusted contributions are uncertain in this model."

---

## F. Supplementary tests (exploratory, not the main test)

These were run on the 102-case scored file as extra checks. They do not decide the main hypothesis.

### 19. One-sample t-test
- **What it is:** compares an average with a fixed number.
- **Picture:** the pass mark is 3. Is the class average really above the pass mark, or only by chance?
- **In your study:** each construct average was compared with the neutral midpoint of 3. All four are clearly above (p < .001).

### 20. Paired t-test
- **What it is:** compares two scores from the same person.
- **Picture:** weighing the same people before and after a diet, or comparing one student's maths and science marks.
- **In your study:** each person's Training Effectiveness score was compared with their own Hybrid Learning, Trainer Competence and Learner Engagement scores. None differed significantly (p = .110, .169, .263).
- **Caution:** these are different ideas on the same form, not "before and after". This is not a time comparison.

### 21. Welch's independent-samples t-test
- **What it is:** compares the averages of two separate groups. The Welch version does not assume the two groups are equally spread out, so it is the safer choice.
- **Picture:** comparing the average marks of two different classes.
- **In your study:** officers (M = 4.163, n = 56) and managers (M = 4.220, n = 26) did not differ significantly (t = −0.270, p = .788). Clerical staff were not in this comparison.

### 22. One-way ANOVA
- **What it is:** compares the averages of three or more groups in one go.
- **Picture:** comparing sales in three branches. Doing three separate two-group tests would raise the chance of a false alarm, so ANOVA does it together.
- **In your study:** clerical (4.550), officers (4.163) and managers (4.220) were compared on Training Effectiveness. The ANOVA result was not significant, *F*(2, 99) = 1.629, *p* = .201. The thesis mentions Duncan as a possible follow-up comparison but makes no Duncan-based claim that the job-level groups differ.

### 23. Chi-square test and crosstabs (and why they were not used)
- **What it is:** a test of association between **two categorical variables**, such as job level and an answer category. A crosstab first counts how many people fall in each combination. Chi-square then compares the observed counts with counts expected if the variables were unrelated.
- **Picture:** a seating chart showing which people sit where. The test needs enough people in every seat to say anything.
- **In your study:** the construct means produced many distinct values, leaving almost every crosstab cell nearly empty (98.8–99.3% had an expected count below 5). The reported chi-square numbers are therefore a **suitability check**, not evidence for or against the main hypothesis.

---

## G. Cautions to be able to say

- **Association, not cause:** correlation and regression show that things go together. They do not prove one causes the other.
- **Self-report:** the same person rated everything, which can make relationships look stronger.
- **Not random:** purposive sampling means the results describe this group only.
- **One snapshot:** the survey was taken once, so it cannot show change over time.
- **102 vs 103:** the tables say which number of cases each uses. SPSS used 102 for the main model.

---

## One-page cheat sheet

| Technique | Question it answers | Your result |
| --- | --- | --- |
| Frequency and percentage | Who answered? | 102 respondents, mostly 35–44 and officers |
| Mean | What is the typical rating? | 4.15 to 4.32, all positive |
| Standard deviation | How much do opinions differ? | About 0.8 |
| Skewness, kurtosis | Is the pile lopsided or peaked? | Leaning to "agree" |
| Normality test | Is it bell-shaped? | No, as expected for ratings |
| Cronbach's alpha | Do item responses vary consistently? | .980 for all 26 items pooled; no final per-construct alphas reported |
| PCA, KMO, Bartlett | Are item correlations suitable for an exploratory component check? | Four components extracted; KMO .929; not full scale validation |
| Pearson *r* | Do two scores move together? | .659 to .818, all reported pairs significant; pairwise N varies |
| Multiple regression | Do the three predictors jointly relate to effectiveness? | Yes, R² = .608 for 102 cases; only Learner Engagement has an individually significant adjusted coefficient |
| One-sample t-test | Is the average above 3? | Yes, for all four |
| Paired t-test | Does one person's two scores differ? | No |
| Welch t-test | Do officers and managers differ? | No |
| One-way ANOVA | Do the three job-level means differ detectably? | No significant difference; Duncan is not used for a group claim |
| Chi-square | Can the construct-mean crosstabs support a categorical association test? | No reliable inference: expected cell counts are too small |
