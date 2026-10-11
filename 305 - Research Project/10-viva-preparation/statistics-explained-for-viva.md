# Statistics in my thesis — a simple story for the viva

This guide follows the [thesis PDF](../08-thesis-drafts/03-third-draft-chapters-1-to-5/hybrid-learning-training-effectiveness-third-draft-final-v4.pdf). Imagine Sreetama moving through her work: she collects questionnaires, turns answers into scores, checks those scores, and then asks what they tell her about training. Each section takes the **next question in that story**. The small examples help explain a term; they are not extra survey results.

**SPSS** is the computer program used for the main statistical output. A **scored file** is a table with one employee per row and their coded answers and averages in columns. Read Sections 1–10 first, then Sections 22–33 for the main finding. The other sections are supporting checks she can revisit when needed.

The questionnaire asks about one recent programme that combined digital and face-to-face learning. Its 26 rating statements cover four ideas:

- **Hybrid Learning (HL):** how employees experienced the digital and face-to-face parts together.
- **Trainer Competence (TC):** how they experienced the trainer's explanations and support.
- **Learner Engagement (LE):** how they felt they participated and paid attention.
- **Training Effectiveness (TE):** how useful and applicable they felt the training was.

The main question is whether **HL, TC, and LE together are related to perceived TE** in this group of employees. Their answers were collected at one point in time. They cannot prove that one factor caused another.

## Which diagrams can I actually show?

The PDF prints **eight figures**. Figures 4.1–4.3 show age, service length, and job level. Figure 4.4 shows the four average construct scores. Figures 4.5–4.8 show the answers to individual rating questions. Those are pictures Sreetama can point to in the thesis.

The project's [SPSS figure index](../08-thesis-drafts/03-third-draft-chapters-1-to-5/figures/spss-figure-export-notes.md) names **21 other plots** for possible export, but **none of those 21 appears in this PDF**:

| Plots listed but absent | Number | What they would help her see |
| --- | ---: | --- |
| Construct-score histograms | 4 | Where employees' scores gather. |
| Normal Q–Q plots and detrended Q–Q plots | 8 | Whether scores look like a balanced bell shape. |
| Boxplots | 4 | The middle of the scores and unusually distant scores. |
| PCA scree plot and rotated-component plot | 2 | How the questions may group together. |
| Regression residual histogram, P–P plot, and scatterplot | 3 | Whether the model's prediction mistakes show an unusual pattern. |

A **prediction mistake**, also called a *residual*, is the gap between a person's actual TE score and the score estimated by the regression. The index also mentions plots from supporting tests without listing them one by one. **The index lists these plots for export; they were not inserted into this PDF. The project files do not say why.** It would be wrong to say they were deliberately omitted because they were unimportant. The index's suggested “Figures 4.1–4.4” for histograms are *proposed labels*, not the actual Figures 4.1–4.4 printed in the PDF.

**How to answer if asked to show a missing plot:** “Chapter 4 describes that SPSS check, but this PDF does not reproduce its plot. I can point to the written result; I should not call it a printed figure.”

## Part 1 — From questionnaires to scores

### 1. Response: what did I collect?

**Why:** Before counting anything, I need to know what one record means.

**Think:** One employee submits one questionnaire containing many answers. That is **one response**, not 30 responses.

**In my thesis:** The main survey received **132 questionnaires**. After screening, **103** had the needed profile details. The main SPSS regression used **102** cases because its file lacked a Trainer Competence average for one case.

**Say:** “I received 132 main questionnaires. I had 103 profile-complete records, and the main SPSS model used 102.”

**Find:** Chapter 3, §3.6, Table 3.3 (p. 40).

### 2. Rating code: what does an answer from 1 to 5 mean?

**Why:** I need numbers before I can count or average employees' opinions.

**Think:** If an employee chose “Agree,” I wrote **4** for that answer. The scale is 1 = Strongly Disagree, 2 = Disagree, 3 = Neutral, 4 = Agree, 5 = Strongly Agree. A 4 is an opinion, not a test mark.

**In my thesis:** All **26 rating statements** use this five-choice scale.

**Say:** “I changed each agreement choice into a number from 1 to 5.”

**Find:** Chapter 3, §3.7 (p. 41); Appendix A.

### 3. Construct score: why average several questions?

**Why:** I want one overall rating for each idea, such as Hybrid Learning, from each employee.

**Think:** A hypothetical employee gives seven HL ratings: 4, 5, 4, 3, 4, 5, 4. Their total is 29. Dividing by 7 gives an **HL score of 4.14**. This describes that employee's **general perception** of HL.

**In my thesis:** HL and TE each use **seven items**. TC and LE each use **six**. Each person's items were averaged within the relevant group. This is a perception score, not an objective test of training quality or job performance.

**Say:** “I averaged the questions for each idea to show how each employee generally perceived it.”

**Find:** Chapter 3, §§3.3 and 3.7, Table 3.2 (pp. 37–38, 41).

### 4. Purposive sampling: why ask these employees?

**Why:** Someone who has not attended a programme with both digital and face-to-face learning could not answer these questions about one such programme.

**Think:** To learn about a training session, I ask people who experienced it. I do not pick random employees who may never have attended it. This deliberate choice is called **purposive sampling**.

**In my thesis:** Eligible Union Bank employees with a recent hybrid-training experience were approached. They are **not a random sample** of the whole Bank.

**Say:** “I selected employees who could answer from their own recent training experience.”

**Find:** Chapter 3, §3.5 (p. 39).

### 5. Why do some results use 102 people and others 103?

**Why:** A table can use a record only when that record has the answer needed for that particular calculation.

**Think:** Imagine 103 forms, but one has no TC average in the SPSS file. A calculation needing TC leaves out that form and uses **102**. A calculation using only HL and LE can still use **103**. Leaving out a case missing a needed value is called **listwise deletion** for calculations that need all specified values.

**In my thesis:** The denominators differ as follows:

| Calculation | Number used | Thesis location |
| --- | ---: | --- |
| Age, service, and job-level counts | **102**, selected scored file | Table 4.1; Figures 4.1–4.3 |
| Summary of all four construct scores | **102**, SPSS | Table 4.2; Figure 4.4 |
| Individual HL item averages, Q5–Q11 | **103**, SPSS | Table 4.3; Q6 has mean **3.990** |
| Counts of each rating choice, Q5–Q30 | **102**, selected scored file | Table 4.4; Figures 4.5–4.8 |
| One alpha for all 26 items | **102**, SPSS | Table 4.5 |
| Correlations involving TC | **102**, SPSS | Table 4.6 |
| Correlations HL–LE, HL–TE, and LE–TE | **103**, SPSS | Table 4.6 |
| Main regression | **102**, SPSS | Tables 4.7–4.8 |
| Extra group comparisons and crosstabs | **102**, selected scored file | Tables 4.9–4.11 |

**One important difference:** The SPSS regression's 102 cases and the separately selected scored file's 102 records have the same *number*, but the matching SPSS data file was unavailable. The thesis cannot confirm they are exactly the same people or that every item value matches. The HL average is **4.148** in the SPSS summary and **4.144** in the supplementary scored-file comparison. The main hypothesis decision follows the **SPSS regression**. The thesis does not give a separate case count for its PCA check, so do not guess one.

**Say:** “The number depends on which answers a calculation needs. I use the 102-case SPSS output for my main regression, and I label the separate 102-record supporting tables.”

**Find:** Chapter 3, §3.6, Table 3.3 (p. 40); Chapter 4, Tables 4.1–4.11 (pp. 48–66).

## Part 2 — What did employees answer?

Now Sreetama has usable ratings. She first describes them before testing any relationship.

### 6. Frequency: how many employees?

**Why:** I first want a simple count of people in each answer group.

**Think:** If I count **56** employees aged 35–44, that 56 is their **frequency**. It says how many, not what share of the group.

**In my thesis:** **56 of 102** employees in the profile table were aged 35–44. The item table similarly counts how many selected each rating.

**Say:** “Frequency is simply the number of employees in a category.”

**Find:** Chapter 4, Tables 4.1 and 4.4 (pp. 48–49, 53–56).

### 7. Percentage: what share of the group?

**Why:** A count is easier to understand when I know how large the whole group is.

**Think:** Divide the 56 employees aged 35–44 by the 102 employees in that table, then multiply by 100. The result is **54.9%**.

**In my thesis:** The profile table gives both counts and percentages. The percentage is the share **of the people used in that table**.

**Say:** “56 of the 102 respondents in that table were aged 35–44, which is 54.9%.”

**Find:** Chapter 4, Table 4.1 (pp. 48–49).

### 8. Mean: what was the group's average rating?

**Why:** I want one number that sums up the group's ratings for each idea.

**Think:** Ratings 3, 4, and 5 add to 12. Divide by three people: their **mean**, or average, is **4**.

**In my thesis:** The SPSS averages were HL **4.148**, TC **4.158**, LE **4.317**, and TE **4.254**. All are above the neutral rating of 3. LE is highest; HL is lowest *among these four*, though still above neutral. An average does not mean everyone answered alike.

**Say:** “All four average ratings were favourable. Engagement was highest, and Hybrid Learning was comparatively lowest.”

**Find:** Chapter 4, Tables 4.2–4.3 (pp. 51–53).

### 9. Standard deviation: did employees agree with one another?

**Why:** Two groups can have the same average even when one group agrees and the other has mixed opinions.

**Think:** Ratings **4, 4, 4, 4, 4** all agree. Ratings **3, 3, 4, 5, 5** have the same average, 4, but vary more. **Standard deviation (SD)** is 0 when everyone gives the same value; it grows as scores spread out.

**In my thesis:** The four construct SDs were **.793 to .863** on the 1–5 scale. Employees tended to rate training favourably, but their ratings were not identical.

**Say:** “The mean tells me the average opinion; SD tells me how much opinions differed.”

**Find:** Chapter 4, Table 4.2 (p. 51).

### 10. Minimum and maximum: what were the lowest and highest scores?

**Why:** I want to know the ends of the observed scores.

**Think:** In the set 2, 3, 4, 5, the **minimum** is 2 and the **maximum** is 5. That does not tell me how many people gave each one.

**In my thesis:** Table 4.2 reports **1** as the minimum and **5** as the maximum for each construct.

**Say:** “Minimum and maximum show the ends of the observed scores, not how common those scores were.”

**Find:** Chapter 4, Table 4.2 (p. 51).

### 11. Skewness: which way does the thin end point?

**Why:** An average can hide that most people chose high ratings while a few chose low ones.

**Think:** Imagine ten employees choosing 5 and only one choosing 1. On a left-to-right score chart, the big pile is on the **right**, near 5. The few low scores make a thin **tail** stretching left. **Skewness** describes that uneven shape. It is called *negative* or *left* skew because the **tail**, not the pile, points left.

**In my thesis:** The four construct skewness values were about **−1.8 to −2.1**. Many scores were high, with fewer low scores.

**Say:** “Most scores were high. A few lower scores made a left tail, so skewness was negative.”

**Find:** Chapter 4, Table 4.2 (p. 51); §4.1.3 (p. 60).

### 12. Kurtosis: how are scores packed and spread at the ends?

**Why:** I also want to understand how tightly scores gather and whether some are far from the main group.

**Think:** Picture the score chart as a hill. The **peak** is its tallest part; the **tails** are its thin ends. **Kurtosis** is one number describing the shape, especially the tails, compared with a familiar balanced hill called a **bell curve**. It is **not** just a count of how tall the peak looks.

**In my thesis:** The reported kurtosis values range from **4.058 to 6.236**. This describes the shape of ratings; it says nothing by itself about whether training was good.

**Say:** “Kurtosis describes the shape of the scores, including their tails. It does not rate training quality.”

**Find:** Chapter 4, Table 4.2 (p. 51); §4.1.3 (p. 60).

### 13. Histogram: can I see where scores gather?

**Why:** A picture can make the pile of high and low scores easier to see.

**Think:** A **histogram** is a set of bars for score ranges. A taller bar means more employees' scores fall in that range. If most HL averages are near 4, the bar near 4 is tall.

**In my thesis:** §4.1.3 discusses SPSS histograms for the four construct scores, but **their pictures are not printed in this PDF**. The separate item-response charts in Figures 4.5–4.8 are printed; they are not these histograms. The figure index lists the four histograms for export but gives no reason for their absence.

**Say:** “A histogram would show where scores gather. Chapter 4 discusses this check, but the construct histograms are not printed here.”

**Find:** Chapter 4, §4.1.3 (p. 60), **text only**.

### 14. Boxplot: where is the middle of the group?

**Why:** I want to see the central group of scores and any scores far away from it.

**Think:** Put all scores in order. The **median** is the middle score; the **middle half** is the central 50% of scores. A **boxplot** puts a box around that middle half and may show far-away scores as dots.

**In my thesis:** Chapter 4 mentions boxplots, but **none is printed in this PDF**. The figure index lists four boxplots for export and gives no reason for their absence.

**Say:** “A boxplot would show the middle half and unusual scores. I can point to the discussion, not a printed boxplot.”

**Find:** Chapter 4, §4.1.3 (p. 60), **text only**.

### 15. Q–Q plot: do scores look like a balanced hill?

**Why:** I need to check whether the score pattern resembles the balanced shape assumed in some statistical work.

**Think:** A **bell curve** is a smooth hill with many values near the middle and fewer at both ends. A **Q–Q plot** puts dots against a straight guide line. Dots close to the line suggest a similar shape; dots bending away suggest a different shape.

**In my thesis:** Chapter 4 mentions Q–Q plots and says the scores departed from a normal bell shape. **No Q–Q plot is printed in this PDF.** The figure index lists four normal and four detrended Q–Q plots for export. A detrended plot is another view of how far the dots depart from the guide line. The index gives no reason for their absence.

**Say:** “The Q–Q plot is a shape check. The thesis reports the conclusion in words but does not print the plot.”

**Find:** Chapter 4, §4.1.3 (p. 60), **text only**.

### 16. Normality test: is the different shape noticeable?

**Why:** I want another check of whether the scores follow that balanced bell shape.

**Think:** If scores crowd near 4 and 5, their shape is not a balanced hill around the middle. A **normality test** checks whether the difference from the bell shape is strong enough to notice statistically.

**In my thesis:** The tests reported a departure from normality for all four construct means. This is a check of the **score pattern**, not a test of whether training worked. The result is described in text; no separate normality-test diagram is printed.

**Say:** “Ratings leaned high, and the normality checks found that the scores did not follow a balanced bell shape.”

**Find:** Chapter 4, §4.1.3 (p. 60), **text only**.

## Part 3 — Did the questions work together?

After describing the answers, Sreetama checks the 26 statements. The questions come in a simple order: **Do related answers move together? Is there enough shared pattern? Are the answers connected at all? What groups appear?** Alpha, KMO, Bartlett, and PCA help with those different questions. None of them alone proves that the questionnaire is perfect.

### 17. Cronbach's alpha: did answers to the questions move together?

**Why:** If several questions belong together, employees who rate one highly often rate related ones highly too.

**Think:** An employee who gives high ratings to several trainer-support questions shows a consistent pattern. **Cronbach's alpha** measures how consistently answers move across a set of questions. Very similar questions can also produce a high alpha, so high consistency alone is not proof of good coverage.

**In my thesis:** The saved SPSS output gives **α = .980** for **all 26 items together**, using 102 valid cases. It does **not** give four separate final-sample alphas. A separate 20-person pilot gave preliminary alphas of **.879 to .929** for the four blocks.

**Say:** “The final alpha shows high consistency for all 26 items together; it does not validate each construct separately.”

**Find:** Chapter 3, §3.10 (p. 45); Chapter 4, Table 4.5 (p. 61).

### 18. KMO: is there enough shared pattern to try grouping questions?

**Why:** Before asking a computer to group the 26 questions, I need to know whether the answers contain enough shared information.

**Think:** If employees' answers to every question were completely separate, grouping them would make little sense. **KMO** is a check of whether grouping is suitable. A higher KMO supports trying it.

**In my thesis:** KMO was **.929**, which supported trying the grouping analysis. It did **not** prove that the eventual groups were correct.

**Say:** “KMO told me the answer patterns were suitable for an exploratory grouping check.”

**Find:** Chapter 4, §4.1.4 (pp. 60–61), **number reported in text; no KMO diagram**.

### 19. Bartlett's test: are the question answers connected at all?

**Why:** Before grouping the 26 questions, I need to know whether some answers move together. If they were all unrelated, grouping them would make little sense.

**Think:** Suppose employees who give high ratings to one question often give high ratings to another. There is a shared pattern worth examining. **Bartlett's test** checks whether the questions, taken together, show enough relationships to reject the idea that they are all unrelated.

**In my thesis:** The result was **χ²(325) = 3664.340, p < .001**. In plain words, it supported **looking for groups**. It did **not** tell me which questions belong in which group. Section 23 explains the small *p* value.

**Say:** “Bartlett's test showed enough connection among the answers to try grouping the questions.”

**Find:** Chapter 4, §4.1.4 (pp. 60–61), **number reported in text; no Bartlett diagram**.

### 20. PCA: what groups seem to appear?

**Why:** Now that grouping looks possible, I want to see whether several questions tend to rise and fall together.

**Think:** If employees often give similar ratings to several digital-access questions, those questions may share one answer pattern. **Principal Component Analysis (PCA)** looks for such patterns. It calls the resulting groups **components**.

**In my thesis:** SPSS found **four components**. This is an exploratory check consistent with four broad ideas. It does **not** prove that every item belongs in its intended construct. The PDF does not print the **scree plot** or **rotated-component plot** listed in the export index.

**Say:** “PCA found four common answer patterns, but that alone does not fully validate the four constructs.”

**Find:** Chapter 4, §4.1.4 (pp. 60–61), **text only for the four-component result; plots absent**.

### 21. Varimax: why make the grouping easier to read?

**Why:** After PCA finds patterns, I want to see more clearly which questions go most strongly with each one.

**Think:** **Varimax rotation** makes the grouping results easier to read. It helps show which group a question fits most strongly. It does **not** change an employee's answers or the number of people surveyed.

**In my thesis:** SPSS used varimax with the exploratory PCA. The PDF mentions it, but does not print the rotated-component plot listed in the export index.

**Say:** “Varimax helped make the PCA groups easier to interpret; it did not change the questionnaire answers.”

**Find:** Chapter 4, §4.1.4 (pp. 60–61), **text only; plot absent**.

## Part 4 — Is there a relationship among the four scores?

Describing high ratings is not the same as showing a relationship. Sreetama next asks whether employees who rate one part highly also tend to rate another part highly.

### 22. Hypothesis: what was my main question?

**Why:** I need to say exactly what my main statistical test is meant to decide.

**Think:** The **null hypothesis**, H₀, says HL, TC, and LE **together do not** help estimate TE scores. The **alternative**, H₁, says they **do**. These are two possible answers to **one joint question**, not three separate hypotheses.

**In my thesis:** The regression tests this overall relationship. Here “predict” means estimating a TE score from three scores **in these responses**, not forecasting future job performance or proving a cause.

**Say:** “My one main hypothesis asks whether Hybrid Learning, Trainer Competence, and Learner Engagement jointly predict perceived Training Effectiveness.”

**Find:** Chapter 3, §3.2, Table 3.1 (pp. 36–37); Chapter 5, Table 5.1 (p. 72).

### 23. p-value: when should I doubt the 'no relationship' answer?

**Why:** I need a rule for deciding whether the result is hard to explain if H₀ were true.

**Think:** Imagine H₀ says the three scores have no useful joint relationship with TE. A **p-value** asks: *if that were true, how surprising would a result this strong or stronger be?* A small answer gives reason to doubt H₀. It is **not** the chance that H₀ itself is true.

**In my thesis:** The chosen decision line was **.05**. The main model had **p < .001**, below that line, so H₀ was rejected. “Statistically significant” does not automatically mean important in practice.

**Say:** “The overall p-value was below .05, so I rejected the overall null hypothesis.”

**Find:** Chapter 4, Tables 4.6–4.8 (pp. 61–63); Chapter 5, Table 5.1 (p. 72).

### 24. Pearson correlation: do two scores rise together?

**Why:** Before putting three scores into one model, I can look at each pair.

**Think:** If employees who rate their engagement highly also tend to rate effectiveness highly, those two scores **move together**. **Pearson correlation**, written *r*, describes the direction and strength of that straight-line relationship. A positive number means they tend to rise together. It does not prove why.

**In my thesis:** LE and TE had **r = .765** using 103 available pairs. HL and TC had **r = .818** using 102. All six reported pairs were positive and statistically significant; the pairs used different valid case counts.

**Say:** “Higher engagement scores tended to come with higher effectiveness scores, but correlation does not prove cause.”

**Find:** Chapter 4, §4.2.1, Table 4.6 (pp. 61–62).

### 25. Multiple regression: what if I consider three scores together?

**Why:** HL, TC, and LE overlap. I want to examine their **joint** relationship with TE and see what each adds while the others are considered.

**Think:** TE is the **outcome** I am trying to understand. HL, TC, and LE are three **predictors** used to estimate it. The calculation combining them is a **multiple-regression model**. It is like considering three parts of the same employee's training experience together instead of one at a time.

**In my thesis:** The main SPSS regression used **102** cases. Its overall result was **F(3, 98) = 50.652, p < .001**. The three predictors **together** had a statistically significant relationship with TE.

**Say:** “I tested all three predictors together against perceived Training Effectiveness. The overall model was significant.”

**Find:** Chapter 3, §3.9 (pp. 42–44); Chapter 4, §4.2.2 (pp. 62–64).

### 26. R²: how much of the difference in TE scores fits the model?

**Why:** Employees have different TE scores. I want to know how much of those observed differences the fitted model accounts for.

**Think:** If everyone's TE score were the same, there would be no difference to explain. They are not the same. **R²** describes the share of these differences accounted for by the three-score model **within this sample**.

**In my thesis:** **R² = .608**, or **60.8%** of the variation in TE scores among the 102 cases. It does **not** mean the three factors *caused* 60.8% of training effectiveness.

**Say:** “The model accounted for 60.8% of the differences in employees' perceived effectiveness scores in this sample.”

**Find:** Chapter 4, Table 4.7 (p. 63).

### 27. Adjusted R²: why is there a second, slightly smaller number?

**Why:** A model can appear to fit better simply because I added more predictors.

**Think:** **Adjusted R²** gives the model a small allowance for how many predictors it uses and how many cases it has. It is a more cautious companion to R².

**In my thesis:** Adjusted **R² = .596**, slightly below the ordinary value of .608.

**Say:** “After allowing for the three predictors and the sample size, the model's adjusted value was .596.”

**Find:** Chapter 4, Table 4.7 (p. 63).

### 28. F-test: do the three predictors help as a team?

**Why:** I need one test for my **overall** hypothesis.

**Think:** An average-only model would give everyone the same estimated TE score. The regression uses each employee's HL, TC, and LE scores. The **F-test** asks whether that three-score model fits the actual TE scores better than the average-only model.

**In my thesis:** **F(3, 98) = 50.652, p < .001**. This supports H₁ for the predictors **together**. It does not say all three are individually significant.

**Say:** “The F-test showed that the three-predictor model was significant overall, so I rejected H₀.”

**Find:** Chapter 4, Table 4.7 (p. 63); Chapter 5, Table 5.1 (p. 72).

### 29. Degrees of freedom: what are the 3 and 98 beside F?

**Why:** The result is written as F(3, 98), and I should be able to read it.

**Think:** The **3** refers to the three predictors. The **98** comes from 102 cases after allowing for the three predictors and one starting value: 102 − 3 − 1 = 98. These bookkeeping numbers are called **degrees of freedom**.

**In my thesis:** The notation is **F(3, 98)**. She need not calculate F by hand.

**Say:** “I read it as F with 3 and 98 degrees of freedom. The 3 refers to my three predictors.”

**Find:** Chapter 4, Table 4.7 (p. 63).

### 30. B: what does a one-point difference mean in the model?

**Why:** After the overall test, I want to understand a predictor's result in the questionnaire's original 1–5 units.

**Think:** An **unstandardised coefficient**, called **B**, keeps those units. For LE, B is **.560**. In the fitted model, an LE score one point higher goes with an estimated TE score **.560 points higher**, comparing cases with the same HL and TC scores.

**In my thesis:** This is an **association in the model**, not a promise that making someone more engaged will cause that change.

**Say:** “When HL and TC were taken into account, a one-point higher engagement score went with a .560-point higher estimated effectiveness score.”

**Find:** Chapter 4, Table 4.8 (p. 63).

### 31. Beta: which predictor stands out on one common ruler?

**Why:** The three predictor scores do not all vary by exactly the same amount. I need a fairer way to compare their model coefficients.

**Think:** **Standardised beta**, written **β**, puts the coefficients on one common ruler. It is **not a percentage**. A larger beta shows a larger adjusted relationship on that ruler, but I must still check the p-value.

**In my thesis:** LE had **β = .532**, HL **.194**, and TC **.113**. LE had the largest adjusted coefficient.

**Say:** “On the common beta scale, Learner Engagement had the largest adjusted relationship with TE.”

**Find:** Chapter 4, Table 4.8 (p. 63).

### 32. Individual t-tests: which predictor still stands out when all three enter?

**Why:** A significant **team** result does not mean every team member has a clear separate result.

**Think:** The coefficient's **t-test** asks whether one predictor's adjusted result stands out from zero while the other two remain in the model.

**In my thesis:** LE was individually significant (**p < .001**). HL (**p = .096**) and TC (**p = .346**) were **not** individually significant at the .05 line. The thesis has **one overall hypothesis**; it does not reject separate HL or TC hypotheses that were never stated.

**Say:** “The model was significant overall, but only Learner Engagement was individually significant after adjustment.”

**Find:** Chapter 4, Table 4.8 (p. 63); Chapter 5, Table 5.2 (p. 72).

### 33. Predictor overlap: why is it hard to separate HL and TC?

**Why:** HL and TC may partly carry the same information about one training experience.

**Think:** Employees who rated HL highly also often rated TC highly. If two predictors move together, the model has a harder time separating what is distinct about each. This is called **multicollinearity**, or predictor overlap.

**In my thesis:** HL and TC correlated at **r = .818**. This overlap is a **possible** reason their separate coefficients did not stand out, not a proven explanation. **VIF** is a common overlap check, but the saved SPSS regression did **not** report a VIF value. Do not quote one.

**Say:** “HL and TC were strongly related, which makes their separate model contributions harder to distinguish.”

**Find:** Chapter 4, Table 4.6 (pp. 61–62); §4.2.2 (p. 64).

## Part 5 — Extra questions, separate from the main hypothesis

These supporting comparisons used a **separately selected 102-record scored file**. They do not decide the main SPSS hypothesis. Think of them as follow-up questions after the main result.

### 34. One-sample t-test: is an average above the neutral rating?

**Why:** I want to compare the group's average with **3**, the middle or neutral choice on the response scale.

**Think:** A **one-sample t-test** compares one group average with one fixed number. Here the fixed number is 3.

**In my thesis:** All four construct averages were above 3, with **p < .001**. This supports the description of favourable ratings. It does **not** test whether HL, TC, and LE jointly relate to TE.

**Say:** “The one-sample tests compared each average with neutral 3; all four were above it.”

**Find:** Chapter 4, §4.2.3, Table 4.9 (pp. 64–65).

### 35. Paired t-test: how did two scores from the same employees compare?

**Why:** Each employee has an HL score and a TE score, for example. I can compare those two scores **within the same person**.

**Think:** A **paired t-test** keeps each employee's two scores together, then asks whether one type of score tends to be higher than the other. This is **not** a before-and-after test here; both scores came from one survey.

**In my thesis:** TE was compared in turn with HL, TC, and LE. None of those three average differences met the .05 decision line (**p = .110, .169, and .263**).

**Say:** “I compared two scores from the same employees. These were different questionnaire ideas, not before-and-after measurements.”

**Find:** Chapter 4, §4.2.3, Table 4.10 (p. 65).

### 36. Welch t-test: did officers and managers rate TE differently?

**Why:** Now I am comparing **two separate groups** of employees rather than two scores from the same person.

**Think:** A **Welch t-test** compares two group averages while allowing the groups to have different spreads. Here the two groups are officers and managers.

**In my thesis:** Officers had average TE **4.163** (**56** people); managers had **4.220** (**26** people). The test gave **t = −.270, p = .788**, so it did not show a statistically clear difference. Clerical staff were not part of this two-group test.

**Say:** “The officer and manager TE averages were close; the Welch test did not find a clear difference.”

**Find:** Chapter 4, §4.2.3 (p. 65).

### 37. ANOVA: what if I compare all three job levels?

**Why:** I want one check across clerical staff, officers, **and** managers.

**Think:** **ANOVA** compares several group averages at once. It asks whether at least one group seems different; it does not tell me which group that is.

**In my thesis:** Their average TE scores were **4.550**, **4.163**, and **4.220**. The result was **F(2, 99) = 1.629, p = .201**. Since .201 is above .05, the test did not show a clear job-level difference.

**Say:** “The three job-level averages differed numerically, but ANOVA did not find a statistically clear difference.”

**Find:** Chapter 4, §4.2.3 (pp. 65–66).

### 38. Duncan: if groups differed, which ones would it compare?

**Why:** ANOVA asks whether *any* group differs. A follow-up would ask *which* groups differ.

**Think:** **Duncan** is one follow-up comparison. It checks particular pairs after looking at several groups.

**In my thesis:** Duncan is mentioned, but the ANOVA was **not significant**. The thesis does **not** claim that Duncan proved one job level rated TE higher than another.

**Say:** “Duncan was a follow-up check, but I do not claim a reliable difference between job levels.”

**Find:** Chapter 4, §4.2.3 (p. 66).

### 39. Crosstab: how many employees fall into two categories at once?

**Why:** Sometimes I want to count combinations of two categories.

**Think:** A **crosstab** is a grid. One side might list job levels; the other might list response categories. A cell counts employees who are in **both** categories, such as officers who chose Agree.

**In my thesis:** The exploratory crosstabs made many small cells when scores were put into categories. That made the next test hard to trust.

**Say:** “A crosstab counts people in each combination of two categories.”

**Find:** Chapter 4, §4.2.3, Table 4.11 (p. 66).

### 40. Expected count: how many would be in a cell if there were no link?

**Why:** Before interpreting a crosstab test, I need to check whether its cells have enough cases.

**Think:** An **expected count** is the number we would expect in a cell if the two categories were unrelated. If most expected cells contain almost nobody, the test becomes unreliable.

**In my thesis:** **98.8–99.3%** of the crosstab cells had expected counts below 5. The tables were far too sparse for a dependable chi-square conclusion.

**Say:** “Almost all expected cells were too small, so I did not rely on those chi-square results.”

**Find:** Chapter 4, §4.2.3, Table 4.11 (p. 66).

### 41. Chi-square: can the crosstab show a relationship?

**Why:** I might want to know whether two **categories**, rather than two average scores, are related.

**Think:** **Chi-square** compares the counts actually in the crosstab with the expected counts if the categories were unrelated. That comparison needs a table with enough cases in its cells.

**In my thesis:** Because so many expected counts were below 5, the thesis **does not treat its chi-square numbers as reliable evidence**. Pearson correlation was used for the scored-construct relationships instead.

**Say:** “The crosstabs were too sparse to support a reliable chi-square conclusion.”

**Find:** Chapter 4, §4.2.3, Table 4.11 (p. 66).

## Five answers to remember first

1. **What did I analyse?** “One recent hybrid-training programme as rated by the employees who answered my questionnaire.”
2. **What was the main test?** “A 102-case SPSS regression with HL, TC, and LE together estimating perceived TE.”
3. **What did it find?** “The model was significant overall: F(3, 98) = 50.652, p < .001, R² = .608. I rejected the overall null hypothesis.”
4. **Did all three stand out separately?** “No. Only LE had an individually significant adjusted coefficient.”
5. **Does this prove cause or represent the whole Bank?** “No. These are one-time ratings from selected employees.”
