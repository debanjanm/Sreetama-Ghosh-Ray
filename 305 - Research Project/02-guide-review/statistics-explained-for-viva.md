# The statistics in this thesis, explained from scratch

For Sreetama. Every technique below is one that actually appears in the thesis (`hybrid-learning-training-effectiveness-third-draft-final-v4.pdf`). Each one has four parts: what it is, a real-life picture, what it showed in your study, and a sentence you can say in the viva.

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
- **Say:** "Each construct score is the arithmetic mean of its items."

### 3. Purposive (non-probability) sampling and eligibility
- **What it is:** choosing people because they fit a condition, not at random.
- **Picture:** to judge a workshop, you ask only the people who attended it. Asking everyone in the bank would not make sense.
- **In your study:** only employees who attended a programme that had both online and classroom parts could answer. 132 forms came in, 103 were complete, and 102 were used in the main test.
- **Say:** "Because the sample is not random, the results describe these respondents and cannot be generalised to the whole Bank."

### 4. Valid cases and listwise deletion
- **What it is:** if a form is missing a number the test needs, the whole form is left out of that test.
- **Picture:** a bingo card with one square missing cannot be checked for a win. The test needs all squares.
- **In your study:** SPSS used 102 cases for the main model because one record had no Trainer Competence score in the analysis file. Some item-level tables use 103.
- **Say:** "The regression ran on 102 valid cases after SPSS dropped one record with a missing construct mean."

---

## B. Describing the data

### 5. Frequency and percentage
- **What it is:** how many people gave each answer, and what share of the group that is.
- **Picture:** counting how many classmates prefer tea, coffee or juice.
- **In your study:** age 35–44 was the largest group, 56 people or 54.9%. Officers were 56 people (54.9%), clerical 20 (19.6%) and managerial 26 (25.5%).
- **Say:** "Just over half the respondents were aged 35–44 and were officers."

### 6. Mean (the average)
- **What it is:** add everything up and divide by how many there are.
- **Picture:** if 5 friends share chocolates equally, the mean is what each one gets.
- **In your study:** Learner Engagement 4.32, Training Effectiveness 4.25, Trainer Competence 4.16, Hybrid Learning 4.15. All are well above the middle score of 3.
- **Say:** "All four constructs were rated positively, with Learner Engagement the highest."

### 7. Standard deviation (how spread out the answers are)
- **What it is:** the average distance of answers from the mean. Small means everyone is close together. Large means opinions are scattered.
- **Picture:** two cricket teams both average 40 runs per batsman. In team A everyone scores about 40. In team B one scores 100 and four score close to zero. Same mean, very different spread. The standard deviation tells them apart.
- **In your study:** about 0.8 for each construct, so most people are within about one point of the average.
- **Say:** "The standard deviations of about 0.8 show moderate agreement among respondents."

### 8. Minimum and maximum
- **What it is:** the lowest and highest score. Here they are 1 and 5. Someone gave the lowest rating and someone the highest.

### 9. Skewness (is the pile lopsided?)
- **What it is:** whether answers bunch up on one side.
- **Picture:** a very easy exam where nearly everyone scores 90 or more and a few score low. The long thin tail points left. That is **negative skew**.
- **In your study:** skewness is between −1.8 and −2.1 for all constructs, because most people chose 4 or 5.
- **Say:** "The negative skewness reflects ratings clustered at the agree end of the scale."

### 10. Kurtosis (how tall and pointy the pile is)
- **What it is:** how sharply the answers peak in the middle and how heavy the tails are.
- **Picture:** a tall thin hill against a wide flat one. Yours is a tall, sharp hill, with a high peak at "agree".
- **In your study:** kurtosis ranges from about 4 to 6.

### 11. Charts: histogram, boxplot, Q–Q plot
- **Histogram:** bars showing how many people gave each score, like a classroom heights chart.
- **Boxplot:** a box holding the middle half of the answers, with a line for the median. Dots outside are unusual answers (outliers).
- **Q–Q plot:** dots that fall on a straight line mean the data look bell-shaped. Dots that bend away mean they do not.
- **In your study:** SPSS drew all three for the four construct scores.

### 12. Normality tests
- **What it is:** a test asking "do these scores follow the classic bell curve?" If the result is significant (p < .05), the answer is **no, they do not**.
- **Picture:** holding a bell-shaped cardboard cut-out over your histogram to see whether it fits.
- **In your study:** the tests were significant. This fits the lopsided shape above. It is common for rating scales, and it is a reason to read the results with care.
- **Say:** "The data are not perfectly bell-shaped because ratings pile up near the top of a five-point scale."

---

## C. Checking the questionnaire

### 13. Cronbach's alpha (do the questions hang together?)
- **What it is:** a number from 0 to 1 showing whether questions meant to measure the same thing give consistent results.
- **Picture:** five thermometers in one room. If they all show about the same temperature, you can trust the reading. If they disagree wildly, something is wrong with them.
- **Rule of thumb:** above .70 is acceptable, above .90 is excellent.
- **In your study:** α = .980 across all 26 questions. That is very high. It can also mean the questions are very similar to each other.
- **Important limit:** it was run once for all 26 questions together, not once per construct. So it shows overall consistency, not that each of the four scales is separately reliable.
- **Say:** "The overall alpha of .980 shows very high internal consistency, but it is not a separate reliability value for each construct."

### 14. Principal Component Analysis (PCA) with varimax rotation, KMO and Bartlett's test
- **What it is:** a way to see how many "groups" the questions naturally fall into.
- **Picture:** sorting a pile of books onto shelves. PCA works out how many shelves the data want. Varimax rotation turns the shelves slightly so each book clearly sits on one shelf.
- **KMO (.929):** "is there enough shared pattern to sort at all?" Above .60 is fine, above .90 is superb.
- **Bartlett's test:** "is there any pattern, or are the questions just random noise?" Yours is significant, so there is a pattern.
- **In your study:** SPSS found four components, which matches your four constructs. It was used only as a supporting check and did not change the model.
- **Say:** "The exploratory component analysis gave four components, which is consistent with the four constructs I designed."

---

## D. Testing relationships

### 15. Hypothesis: the null and the alternative
- **Null hypothesis (H₀):** "nothing is going on." Here: the three predictors do not jointly predict Training Effectiveness.
- **Alternative hypothesis (H₁):** "something is going on." Here: they do.
- **Picture:** a courtroom. H₀ is "innocent until proven guilty". The data must give strong enough evidence to reject it.
- **In your study:** H₀ was rejected, so H₁ is supported.

### 16. Significance level (.05) and the p-value
- **p-value:** "if there were really no relationship, how surprising would my result be?" Small p means very surprising.
- **Picture:** you toss a coin 10 times and get 10 heads. That would be very surprising for a fair coin, so you doubt the coin. A small p-value makes you doubt "no relationship".
- **Rule:** if p is below .05 (less than 5 in 100), we call the result **significant**.
- **In your study:** the correlations and the overall model have p < .001, which means less than 1 chance in 1,000 of such results if nothing were going on.
- **Say:** "A result is significant when p is below .05."

### 17. Pearson correlation (r)
- **What it is:** a number from −1 to +1 showing whether two things rise and fall together.
- **Picture:** ice-cream sales and temperature. When one goes up, so does the other (positive r). Umbrellas sold and sunny days move in opposite directions (negative r).
- **Strength:** about .1 weak, .3 moderate, .5 and above strong.
- **In your study:** all pairs are positive and significant. The strongest with Training Effectiveness is Learner Engagement (r = .765). Hybrid Learning and Trainer Competence are strongly linked with each other (r = .818).
- **Important:** correlation shows things go together. It does not show that one causes the other. Ice-cream does not cause sunburn. Both go up in summer.
- **Say:** "Learner Engagement has the strongest relationship with perceived effectiveness, but this is an association, not proof of cause."

---

## E. The main test: multiple regression

### 18. Multiple regression
- **What it is:** a method that uses several things at once to predict one outcome, and shows how much each one adds.
- **Picture:** predicting a student's exam score from study hours, attendance and interest in the subject. Regression says how well the three together predict the score, and which one matters most once the others are counted.
- **In your study:** the outcome is Training Effectiveness. The three predictors are Hybrid Learning, Trainer Competence and Learner Engagement.

The numbers it gives, one by one:

| Number | Plain meaning | Your value |
| --- | --- | --- |
| **R²** | The share of why people differ that the predictors explain. Like saying "these three things explain about 61% of the differences in how effective people found the training". | .608, so 60.8% |
| **Adjusted R²** | The same, but marked down so that useless predictors cannot inflate it. | .596 |
| **F-test** | "Do the predictors as a team do better than just guessing the average for everyone?" | F(3, 98) = 50.652, p < .001. Yes |
| **Degrees of freedom (3, 98)** | The number of predictors and the number of free pieces of information left over. You do not need to calculate them, only to know they come with the F. | 3 and 98 |
| **B** (unstandardised) | If this predictor goes up by 1 point and the others stay put, the outcome goes up by this many points. | Learner Engagement .560 |
| **β (beta, standardised)** | The same effect put on a common scale, so predictors can be compared fairly like marks converted to percentages. | LE .532, HL .194, TC .113 |
| **t and p for each predictor** | "Does this one add something on its own?" | Only Learner Engagement does (p < .001) |

- **What the result means in plain words:** the three together explain about 61% of the differences. But when all three are in the model, only Learner Engagement stands out on its own. Hybrid Learning (p = .096) and Trainer Competence (p = .346) do not.
- **Why would Hybrid Learning and Trainer Competence "disappear"?** They overlap (r = .818). Think of two cooks working side by side who always do the same dishes. When the dinner turns out well, you cannot tell who deserves the credit. The regression gives the credit to the person who does something different, here Learner Engagement. It does not mean the two are unimportant.
- **Multicollinearity and VIF:** this is the technical name for that overlap. VIF is a score for it. The SPSS run did not include VIF, so the thesis says so and relies on the correlation instead.
- **Say:** "The model is significant and explains 60.8% of the variation. Learner Engagement is the only individually significant predictor, and the weaker results for the other two reflect their strong overlap, not that they do not matter."

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
- **In your study:** clerical (4.550), officers (4.163) and managers (4.220) were compared on Training Effectiveness. The difference was not significant, F(2, 99) = 1.629, p = .201. Because there was no difference to locate, the follow-up (Duncan) test was not needed.

### 23. Chi-square test and crosstabs (and why they were not used)
- **What it is:** a test for two categories, such as age group and answer type, that counts how many people fall in each cell and checks whether the pattern is unusual.
- **Picture:** a seating chart showing which people sit where. The test needs enough people in every seat to say anything.
- **In your study:** the construct scores have many different values, so almost every cell was nearly empty (98.8–99.3% of the cells had an expected count below 5). The thesis says these tables are too sparse and does not draw conclusions from them.

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
| Cronbach's alpha | Do the questions agree with each other? | .980 overall |
| PCA, KMO, Bartlett | Do the questions fall into groups? | Four groups; KMO .929 |
| Pearson r | Do two things move together? | .66 to .82, all significant |
| Multiple regression | Do the three together predict effectiveness? | Yes, R² = .608; only Learner Engagement stands out |
| One-sample t-test | Is the average above 3? | Yes, for all four |
| Paired t-test | Does one person's two scores differ? | No |
| Welch t-test | Do officers and managers differ? | No |
| One-way ANOVA | Do the three job levels differ? | No |
| Chi-square | Are two categories linked? | Not usable: too few people per cell |
