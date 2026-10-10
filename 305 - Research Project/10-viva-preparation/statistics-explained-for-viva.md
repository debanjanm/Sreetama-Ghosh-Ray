# Statistics in my thesis — explained one step at a time

This guide is for Sreetama's viva. It follows the [final-v4 thesis PDF](../08-thesis-drafts/03-third-draft-chapters-1-to-5/hybrid-learning-training-effectiveness-third-draft-final-v4.pdf). Read it in order. Each section explains **one term**, gives **one small example**, and then shows where it appears in the thesis. The examples with made-up numbers are for learning; they are not survey responses.

**Do not memorise all 41 terms at once.** First read Sections 1–8 (forms, scores, counts, averages). Next read Sections 22–33 (the one main hypothesis). The remaining sections explain supporting checks if the guide asks about them.

## First, what was measured?

One employee answered about **one recent programme** that combined digital and face-to-face learning. The questionnaire had four eligibility/profile questions and 26 rating statements. The statements covered four ideas:

- **Hybrid Learning (HL):** how well the digital and face-to-face parts worked together.
- **Trainer Competence (TC):** how the trainer explained, connected, and supported the activities.
- **Learner Engagement (LE):** how much the employee paid attention, participated, and asked questions.
- **Training Effectiveness (TE):** how useful and applicable the employee felt the learning was.

The main question was: **Do HL, TC, and LE, considered together, relate to TE?** The study recorded perceptions at one time. It cannot show that any one of these caused another.

## Part 1 — Turning forms into numbers

### 1. What is a response?

A **response** is one submitted questionnaire record. Think of one feedback card handed in after a workshop. That card contains many answers, but it is still one response.

The main collection received **132 forms**. After eligibility and profile screening, **103 records** had the required profile information. The main SPSS regression used **102 valid cases** because one record in its analysis file lacked a Trainer Competence mean.

**Say in the viva:** “I received 132 main forms. After screening, 103 were profile-complete, and the main SPSS model used 102 valid cases.”

### 2. What does a 1–5 answer mean?

The 26 statements used five choices: 1 = Strongly Disagree, 2 = Disagree, 3 = Neutral, 4 = Agree, and 5 = Strongly Agree. The number is a **code** for the selected answer.

For example, if an employee agreed that digital material was available before the session, that answer was coded **4**. A 4 is not a mark out of 5 on a test; it is the employee's opinion on that statement.

### 3. What is a construct score?

A **construct** is an idea measured with several questions. Instead of discussing seven Hybrid Learning answers separately every time, the study takes their average to make one HL score per respondent.

*Made-up example:* An employee's seven HL answers are 4, 5, 4, 3, 4, 5, 4. Add them to get 29, then divide by 7. The HL score is **4.14**. TC and LE each use six items; TE uses seven.

The score summarises **that respondent's overall perception** of the construct. In this example, 4.14 means the employee generally rated their Hybrid Learning experience favourably. It does not independently measure the programme's actual quality or the employee's job performance.

**Say:** “I averaged the assigned questions to get one score showing each respondent's overall perception of each construct.”

### 4. Why did the study choose these employees?

This is **purposive sampling**. The researcher approached people who could answer the research question: employees who had experienced both digital and face-to-face learning in one programme.

*Everyday example:* To ask how a particular workshop went, you ask people who attended it. That choice is sensible, but it is **not a random sample** of every bank employee. The results describe the selected respondents; they cannot statistically represent the whole Bank.

### 5. Why do some tables say 102 and others 103?

Start with **103 profile-complete records**. In the SPSS analysis file, one of those records lacked a **Trainer Competence construct mean**. A calculation needing all four construct means could therefore use only **102** records. **Listwise deletion** is the name for leaving that incomplete record out of such a calculation.

That record could still be used for a calculation that did **not** need its missing Trainer Competence mean. For example, SPSS could calculate a Hybrid Learning item mean from **103** available answers. It could also correlate Hybrid Learning with Learner Engagement using **103** cases, because neither score in that pair was the missing Trainer Competence mean.

| Calculation in the PDF | Cases | Where to find it |
| --- | ---: | --- |
| Age, service-length, and job-level counts and percentages | **102** from the selected scored file | Table 4.1; Figures 4.1–4.3 |
| Mean, standard deviation, minimum, maximum, skewness, and kurtosis for **all four construct scores together** | **102** in SPSS Explore | Table 4.2; Figure 4.4 uses these means |
| Mean for each of the seven **individual Hybrid Learning questions**, Q5–Q11 | **103** available item answers in SPSS | Table 4.3; this includes the Q6 mean of 3.990 |
| Counts for each answer choice, 1–5, across Q5–Q30 | **102** from the selected scored file | Table 4.4; Figures 4.5–4.8 |
| One overall Cronbach's alpha for all 26 scored items | **102** valid SPSS cases; one excluded | Table 4.5 |
| Correlations **HL–TC, TC–LE, TC–TE** | **102** for each pair in SPSS | Table 4.6; every pair includes TC |
| Correlations **HL–LE, HL–TE, LE–TE** | **103** for each pair in SPSS | Table 4.6; none of these pairs needs TC |
| Main three-predictor regression and its individual coefficients | **102** valid SPSS cases | Tables 4.7–4.8; the hypothesis decision in Chapter 5 |
| One-sample and paired *t*-tests, Welch comparison, ANOVA, and chi-square suitability tables | **102** from the selected scored file | Tables 4.9–4.11 and the accompanying text |

**Two different “102s” need care.** The main regression used 102 cases in the **saved SPSS output**. The profile, response-count, and supplementary tables used a **separately selected 102-record scored file**. The matching SPSS data file was not available, so the thesis cannot verify that those are exactly the same 102 people or that every underlying item value agrees. For example, HL averages **4.148** in SPSS Table 4.2 but **4.144** in the supplementary scored-file comparison. The main hypothesis decision follows the SPSS regression, not the supplementary file.

The PDF also reports an exploratory PCA with KMO and Bartlett's test, but it does **not** state a separate case count for that check. Do not guess its N in the viva.

**Say:** “The denominator depends on the calculation. SPSS used 102 when all four construct means were required, but some item means and pairs without Trainer Competence used 103. The other 102-case tables came from a separate selected scored file and are labelled as such.”

## Part 2 — Describing what people answered

### 6. Frequency: how many?

A **frequency** is a count. In the 102-record profile table, **56** respondents were aged 35–44. Nothing more is being calculated yet; 56 is simply the number of people in that category.

### 7. Percentage: what share?

A **percentage** turns a count into a share out of 100. For the age group above, 56 ÷ 102 × 100 = **54.9%**.

*Everyday example:* If 5 of 10 people prefer tea, that is 50%. Percentages make groups of different sizes easier to read.

**Say:** “The largest age group was 35–44: 56 of 102 respondents, or 54.9%.”

### 8. Mean: what is the average?

The **mean** is the total of the values divided by the number of values. For ratings 3, 4, and 5, the mean is (3 + 4 + 5) ÷ 3 = **4**.

In the SPSS construct summary, the means were HL **4.148**, TC **4.158**, LE **4.317**, and TE **4.254**. All were above the neutral value of 3; LE was highest and HL lowest among the four. A high mean does not mean every person gave a high rating.

### 9. Standard deviation: how different were the answers?

The **average** tells us the group's typical rating. **Standard deviation (SD)** tells us whether people gave similar ratings or very different ones. If everyone gives exactly the same rating, SD is **0**. As their answers spread out, SD becomes larger.

*Made-up training example:* Five employees in Group A rate a programme **4, 4, 4, 4, 4**. Five in Group B rate it **3, 3, 4, 5, 5**. Both groups have the same average, **4**. But Group A agrees completely, while Group B's opinions differ. Group A has SD **0**; Group B has a larger SD.

In the thesis, the four SDs were **.793 to .863** on the 1–5 scale. So employees generally gave favourable ratings, but they did not all give the same ratings. SD tells us about **agreement or variation**, not whether the training itself was good or bad.

**Say:** “The average tells me the typical rating. Standard deviation tells me how much employees' ratings differed from one another.”

### 10. Minimum and maximum: what were the ends?

The **minimum** is the lowest observed score; the **maximum** is the highest. The SPSS construct table lists **1** and **5** for each construct. These two numbers do not tell us how many people gave those scores. For that, use a frequency table.

### 11. Skewness: which side has most answers?

**Skewness** describes whether a distribution leans to one side. Imagine a queue of marks where most people scored near 5 and only a few scored near 1. The long tail points toward the low scores: this is **negative skew**.

The thesis reports negative skewness of about **−1.8 to −2.1** for the four construct means. Many ratings were near the favourable end of the scale. This describes the *shape* of the answers, not the strength of a relationship.

### 12. Kurtosis: what is the shape around the centre and tails?

**Kurtosis** is another shape measure. It helps describe how concentrated values are and how the tails compare with a normal bell-shaped distribution. It does not tell us whether training worked.

*Everyday example:* Two queues may have the same average waiting time, but one has most waits close together with a few unusual long waits. Their distribution shapes differ.

The thesis reports construct kurtosis values from **4.058 to 6.236**. Sreetama does not need to interpret each value alone; it is read alongside the graphs and skewness.

### 13. Histogram: where do the scores pile up?

A **histogram** is a set of bars showing how many scores fall in each range. Imagine putting exam scores into ranges such as 0–9, 10–19, and so on, then drawing one bar per range.

SPSS produced histograms for the four construct scores. They help show the pile-up toward favourable ratings.

### 14. Boxplot: where is the middle half?

A **boxplot** shows the median and the middle half of scores inside a box. Points outside the usual range are drawn separately as possible unusual values.

*Everyday example:* For a group of travel times, the box shows the central cluster without listing every person's journey. A point far away may be someone delayed by traffic. SPSS drew boxplots for the four construct scores.

### 15. Q–Q plot: does the shape resemble a bell curve?

A **Q–Q plot** compares the observed score pattern with a normal bell-curve pattern. If the dots mostly follow a straight line, the two shapes are fairly similar. If they bend away, the scores depart from that shape.

SPSS drew Q–Q plots. Because many questionnaire ratings were high, the construct scores did not closely follow a normal bell curve.

### 16. Normality test: is the departure statistically noticeable?

A **normality test** tests whether the score distribution could reasonably be treated as normal. Here the reported tests were significant, which means the distributions differed detectably from a normal bell shape.

This test does **not** ask whether training was effective. It checks a property of the scores that matters when reading later tests.

**Say:** “The scores were skewed toward agreement, and the normality checks detected departures from a bell-shaped distribution.”

## Part 3 — Checking the questionnaire

### 17. Cronbach's alpha: do item responses move consistently?

**Cronbach's alpha** asks whether answers across a set of questions tend to move together. It does **not** prove that the questions measure the correct concept.

*Everyday example:* Several thermometers rise together when a room gets warmer. They are consistent. But if every thermometer is badly calibrated, their agreement does not make them accurate.

The saved SPSS output gives **α = .980** for **all 26 scored items pooled together**. That is very high and may partly reflect overlapping questions. It is **not** four separate final-sample alpha values for HL, TC, LE, and TE. A separate 20-person pilot gave preliminary block alphas from **.879 to .929**.

**Say:** “The reported final alpha is for all 26 items combined. It does not, by itself, validate each of the four constructs.”

### 18. PCA: can 26 items be summarised into fewer groups?

**Principal Component Analysis (PCA)** looks for patterns across many item answers and summarises them with fewer components.

*Everyday example:* If 26 questions about a workplace tend to fall into a few recurring topics, PCA looks for those topics in the answer patterns. SPSS extracted **four components** here. That is compatible with the planned four constructs, but it is not proof that every question perfectly measures its intended construct.

### 19. Varimax rotation: why turn the component picture?

**Varimax** is a rotation used after components are extracted. It changes how the component axes are displayed to make item patterns easier to interpret. It does not change anyone's answer.

*Everyday example:* Turn a map on a table so the streets line up more clearly with the page. The streets did not move; the view became easier to read. The thesis used varimax in its exploratory PCA.

### 20. KMO: were the item relationships suitable for PCA?

**Kaiser–Meyer–Olkin (KMO)** is a suitability check before interpreting PCA. A high value means the items share enough patterned relationships for component analysis to be useful.

The reported KMO was **.929**, a strong suitability result. KMO does not say the questionnaire is fully validated.

### 21. Bartlett's test: were the items related at all?

**Bartlett's test** asks whether the item-correlation pattern differs from one in which the items are unrelated. Here it was significant: **χ²(325) = 3664.340, p < .001**. That supports looking for components.

*Everyday example:* Before sorting books into topics based on shared words, check whether the books share any word patterns at all. Bartlett addresses that first question; it does not decide the correct topic labels.

## Part 4 — Testing relationships

### 22. Hypothesis: what exactly was being tested?

A **hypothesis** is a statement the analysis tests. The thesis has **one overall regression hypothesis**.

- **H₀, the null:** HL, TC, and LE do **not jointly** predict TE.
- **H₁, the alternative:** HL, TC, and LE **do jointly** predict TE.

These are about a *statistical relationship* among scores, not proof that the three factors cause effectiveness. The separate coefficients are described, but they are not three extra hypotheses.

### 23. p-value: how surprising would this result be under H₀?

A **p-value** asks: *If H₀ were true, how unusual would a result at least this extreme be, assuming the test's conditions?* A small p-value is evidence against H₀. It is **not** the probability that H₀ is true.

*Everyday example:* If a coin is fair, ten heads in ten tosses would be unusual. That observation would make us question the fair-coin assumption; it would not tell us the exact probability that the coin is unfair.

The thesis used **.05** as its decision line. A result with *p* below .05 is called statistically significant. The overall regression had **p < .001**, so H₀ was rejected. “Significant” does not automatically mean practically important.

### 24. Pearson correlation: do two scores rise together?

A **correlation**, written *r*, describes the direction and strength of a straight-line relationship between **two** scores. It ranges from −1 to +1. Positive means higher scores on one tend to go with higher scores on the other; negative means the opposite.

*Everyday example:* On hot days, more people may buy cold drinks. Temperature and cold-drink sales rise together. One may be connected to the other, but correlation by itself cannot prove the cause.

In the thesis, LE and TE had **r = .765** (pairwise N = 103). HL and TC had **r = .818** (pairwise N = 102). All six reported pairs were positive and significant. Different pairs had different valid case counts.

**Say:** “Higher engagement ratings tended to accompany higher effectiveness ratings. That is a relationship, not proof of cause.”

### 25. Multiple regression: what happens when three predictors enter together?

**Multiple regression** examines one outcome using several predictors at once. Here the outcome is **TE**. The three predictors entered together are **HL, TC, and LE**.

*Everyday example:* Suppose a manager wants to understand customer waiting time using staffing, customer arrivals, and system speed together. Looking at each separately can hide overlap. Regression estimates how the three relate to waiting time when considered in one model.

The thesis's main SPSS regression used **102 cases**. Its overall result was significant: **F(3, 98) = 50.652, p < .001**. This supports H₁ for the **three predictors jointly**.

### 26. R²: how much score variation does the model account for?

**R²** is a number from 0 to 1. It describes the share of the *observed differences in TE scores* accounted for by the fitted regression model in this sample.

*Everyday example:* People give different workshop ratings. A model using three survey scores may account for some of those differences, while other differences remain. R² describes the share accounted for by this model.

The thesis reports **R² = .608**, or **60.8%** of variation in the 102 TE scores. It does **not** mean that the predictors caused 60.8% of training effectiveness.

### 27. Adjusted R²: why reduce R² a little?

Adding more predictors can make ordinary R² rise even if the new predictors help very little. **Adjusted R²** makes an allowance for the number of predictors and the sample size.

The thesis reports **adjusted R² = .596**. It is close to .608, but slightly lower after the adjustment.

### 28. F-test: does the team of predictors help?

The **F-test** in this regression asks whether the three predictors **as a group** improve the model compared with using only the overall TE average.

*Everyday example:* To guess workshop ratings, one option is to give everyone the same average guess. Another uses HL, TC, and LE scores. The F-test asks whether the second approach fits the observed ratings better than the average-only approach.

Here **F(3, 98) = 50.652, p < .001**. So the **overall model** is statistically significant. This is the test that decides the thesis's single H₀/H₁ question.

### 29. What do the 3 and 98 after F mean?

These are **degrees of freedom**, numbers that describe the size of the test. The first is **3** because there are three predictors. The second is **98** because there were 102 cases, minus three predictors, minus one intercept: 102 − 3 − 1 = 98.

She does not need to derive the F formula in the viva. She should read the notation aloud as “F with 3 and 98 degrees of freedom.”

### 30. B: what is the model's estimated score difference?

An **unstandardised coefficient B** keeps the original 1–5 score units. For LE, **B = .560**. In the fitted model, a one-point higher LE score is associated with a **.560-point higher predicted TE score**, *if HL and TC are held fixed*.

This is a model estimate, not a promise that raising one employee's engagement by one point would cause their effectiveness to rise by .560.

### 31. Beta: how do we compare predictors on a common scale?

A **standardised beta (β)** puts coefficients on standard-deviation units. It helps compare the predictors within this model. It is **not a percentage**.

The reported betas are LE **.532**, HL **.194**, and TC **.113**. LE has the largest adjusted coefficient on this common scale. Size alone is not enough; each coefficient also has a *p*-value.

### 32. A coefficient's t-test: does one predictor stand out after adjustment?

The regression gives a separate **t-test and p-value** for each coefficient. It asks whether that predictor's adjusted coefficient differs detectably from zero **while the other two are in the model**.

LE was individually significant (**p < .001**). HL (**p = .096**) and TC (**p = .346**) were **not** individually significant at the .05 level. That does not mean HL or TC are useless or that separate HL and TC hypotheses were rejected; the thesis has one overall hypothesis.

**Say:** “The joint model was significant. Among its individual predictors, only Learner Engagement had a statistically significant adjusted coefficient.”

### 33. Predictor overlap: why are the individual results harder to read?

**Multicollinearity** means predictors are strongly related to one another. HL and TC had **r = .818**. When two predictors contain similar information, separating their individual contributions becomes harder.

*Everyday example:* Two colleagues almost always work the same shifts. Customer ratings may be associated with their joint presence, but a simple comparison cannot clearly assign a separate share to each colleague.

This overlap is a **possible** reason that HL and TC were not individually significant in the joint model. We cannot prove it is the only reason. A **VIF** is a common diagnostic for overlap, but VIF was **not reported** in the saved SPSS regression output. Do not quote a VIF number.

## Part 5 — Extra checks, not the main hypothesis test

The following comparisons used the selected **102-record scored file**. They are exploratory and did **not** decide the thesis's one overall hypothesis.

### 34. One-sample t-test: is a mean different from a fixed number?

A **one-sample t-test** compares a group's mean with a chosen reference number.

*Everyday example:* A school compares its average test score with a published benchmark of 60. Here the reference was **3**, the neutral point of the five-point scale. All four construct means were above 3 with **p < .001**. This repeats the positive descriptive pattern; it does not test the relationship among constructs.

### 35. Paired t-test: do two scores from the same people differ?

A **paired t-test** compares two measurements belonging to the same person.

*Everyday example:* The same employee rates two workshop features. Pairing keeps that employee's two answers together. In this thesis, each person's TE score was compared with their own HL, TC, and LE scores.

None of those three mean differences reached .05 (**p = .110, .169, and .263**). These are **different constructs measured once**, not before-and-after scores.

### 36. Welch's two-group t-test: do two separate groups differ?

A **Welch t-test** compares the means of **two different groups** and allows their score spreads to differ.

*Everyday example:* Compare workshop ratings from one group of officers and another group of managers. Here officers had mean TE **4.163** (n = 56) and managers **4.220** (n = 26). The result was not significant (**t = −.270, p = .788**). Clerical employees were not in this two-group test.

### 37. ANOVA: do three or more group means differ?

**One-way ANOVA** compares several groups at once. It asks whether there is evidence that **at least one** group mean differs; it does not identify which group.

*Everyday example:* Compare workshop ratings across clerical, officer, and managerial staff together. Their TE means were **4.550, 4.163, and 4.220**. The thesis reports **F(2, 99) = 1.629, p = .201**, so there was no statistically significant job-level difference in this supplementary test.

### 38. Duncan: which groups differ after ANOVA?

A **post-hoc test** is a follow-up that tries to locate *which* group means differ after comparing several groups. Duncan is one such procedure.

The thesis mentions Duncan but does **not** claim a Duncan-based difference among the job levels. The ANOVA itself was not significant, so she should not say that one job level scored reliably higher than another.

### 39. Crosstab: how many people fall in each combination?

A **crosstab** is a count table for two categories. For example, its rows could be job levels and its columns could be Agree/Neutral/Disagree. Each cell counts the people in one combination.

The thesis's exploratory crosstabs used construct-mean categories with many possible values, so most cells had very few expected cases.

### 40. Expected count: how full should a crosstab cell be?

An **expected count** is the number a cell would be expected to contain if the two categories were unrelated.

*Everyday example:* If officers are half of a group, and half of everyone agrees, we would expect roughly a quarter of the group in the “officer and agree” cell if job level and agreement were unrelated. Very small expected counts make a chi-square result unreliable.

In the thesis's crosstabs, **98.8–99.3%** of cells had expected counts below 5. That is much too sparse for a reliable conclusion.

### 41. Chi-square: are two categorical patterns related?

**Pearson chi-square** compares the observed crosstab counts with the expected counts. A large enough difference can suggest an association between categorical variables, but only when the table is suitable for the test.

Because the expected counts here were overwhelmingly small, the thesis **does not interpret its chi-square numbers as evidence**. It uses Pearson correlation for the relationships among the scored constructs instead.

## Five answers to remember for the viva

1. **What is your main test?** “Multiple regression with HL, TC, and LE together predicting perceived TE.”
2. **What did it find?** “The overall 102-case model was significant: F(3, 98) = 50.652, p < .001, R² = .608. I rejected the overall null hypothesis.”
3. **Did every predictor stand out separately?** “No. Only LE was individually significant after all three predictors entered the model.”
4. **Does that prove cause?** “No. These are one-time self-reported associations in a purposively selected group.”
5. **Why do some tables use 103 and others 102?** “SPSS used 102 when a calculation required the missing Trainer Competence mean, but 103 for some item means and correlations that did not need it. The other 102-case descriptive and supplementary tables came from a separately selected scored file. My main hypothesis uses the 102-case SPSS regression.”
