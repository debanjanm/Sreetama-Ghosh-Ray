# Quantitative Aptitude — Patterns, Methods, and Worked Questions

**Use:** Learn one pattern, cover its solution, solve it yourself, then compare steps. The Infosys HRD notice does not specify topics, calculator rules, or negative marking; these are general placement questions, not an Infosys paper.

## A reliable solving routine

1. Underline the **quantity asked**, its unit, and the base of any percentage.
2. Write a compact equation or table before calculating. For MCQs, estimate first and eliminate impossible options.
3. Check whether the answer is sensible: a discounted price falls, a weighted average lies between group averages, and probability lies between 0 and 1.
4. If no clear route appears quickly, mark the question and return after easier ones. Use the actual test instructions for time and guessing strategy.

| Wording | First move | Trap |
|---|---|---|
| “x% more/less than” | Identify the original base | Reversing a percentage uses a different base |
| “Overall average” | Rebuild total sums | Averaging two averages without group sizes |
| “Together finish” | Add work **rates** | Adding completion times |
| “Same distance” at two speeds | Total distance / total time | Arithmetic mean of speeds |
| “At least one” | Total minus none | Missing several cases |
| Table/chart “growth” | (new − old) / old | Dividing by new value |

## 1. Percentages and reverse percentages

**Pattern:** A salary rises from ₹24,000 to ₹27,000. Percentage rise?  
**Solve:** Difference ₹3,000; base is original ₹24,000; 3,000/24,000 × 100 = **12.5%**.

**Reverse pattern:** After a 20% discount, a course costs ₹960. Original price?  
**Solve:** ₹960 is 80% of original, so original = 960/0.8 = **₹1,200**. Do not add 20% of ₹960.

**Successive change:** A price rises 20%, then falls 10%. Multiplier 1.2 × 0.9 = 1.08, so **8% increase**. Shortcut a + b + ab/100 works with signed values (+20 and −10).

**Fast conversions:** 50%=1/2; 25%=1/4; 20%=1/5; 12.5%=1/8; 10%=1/10. For 15% of 240, use 10% + 5% = 24 + 12 = **36**.

## 2. Ratios, proportions, and weighted averages

**Pattern:** In a 2:3 officer-to-clerk ratio among 75 people, how many clerks?  
**Solve:** Five parts = 75, one part = 15, clerks = 3 × 15 = **45**.

**Changed ratio:** A team has 24 women and 16 men. How many men must join to make the ratio 1:1? **8**: 16 + x = 24.

**Weighted average:** 20 people score 60 and 30 score 80. Overall average = (20×60 + 30×80)/50 = **72**, not (60+80)/2 = 70.

**Replacement:** Five scores average 70; one score 50 is replaced by 80. Total increases 30, so average increases 30/5 = 6 to **76**.

## 3. Profit, loss, and discounts

**Pattern:** Cost ₹500, markup 40%, discount 10% on marked price.  
**Solve:** Marked ₹700; selling price 700×0.9 = ₹630; profit ₹130; profit% = 130/500×100 = **26%**. Discount uses marked price; profit uses cost price.

**Successive discounts:** 20% then 10% gives 0.8×0.9=0.72 of marked price, a **28%** discount, not 30%.

## 4. Simple and compound interest

**Simple interest:** ₹5,000 at 8% per year for 2 years: SI = PRT/100 = **₹800**.

**Compound annually:** Same terms: amount = 5,000×1.08² = ₹5,832; CI = **₹832**. For exactly two annual compounding periods at the same rate, CI−SI = P(R/100)² = **₹32**.

**Check conditions:** That shortcut is for **two periods**, not an arbitrary three-year or changing-rate problem. If compounded half-yearly, divide annual rate by two and double the number of years into periods.

## 5. Time and work

**Pattern:** A completes a task in 6 days, B in 12. Together?  
**Solve:** Per-day rates 1/6 + 1/12 = 1/4; time = **4 days**.

**Work units shortcut:** Assume 12 units total. A does 2/day, B does 1/day, together 3/day; 12/3 = **4 days**.

**One leaves:** A does 1/6 per day; B 1/12. Together 2 days complete 2×1/4=1/2. If A then works alone, remaining half takes (1/2)/(1/6)=**3 more days**.

**Pipes:** Inlet fills in 5 hours, outlet empties in 10: net rate 1/5−1/10=1/10 tank/hour; **10 hours** to fill from empty.

## 6. Speed, distance, and time

**Equal distances:** Go 60 km at 30 km/h, return 60 km at 60 km/h. Total 120 km, total time 2+1=3 h, average speed **40 km/h**, not 45.

**Train crossing a platform:** 120 m train crosses 180 m platform at 15 m/s. It must cover 120+180=300 m; time **20 s**.

**Relative speed:** Two people 5 km apart move toward each other at 4 and 6 km/h; meeting time = 5/(4+6) = **0.5 h**. Same direction uses the difference in speeds.

**Conversion:** 36 km/h = 36×5/18 = **10 m/s**.

## 7. Mixtures and concentration

**Pattern:** Mix 20% and 50% solutions to get 30%.  
**Solve:** Let quantities of low and high concentration be L and H: .2L+.5H=.3(L+H), so .2H=.1L and **L:H=2:1**. Check with 2 L at 20% and 1 L at 50%: 0.9 L active in 3 L =30%.

**Replacement:** 10 L of 40% solution has 4 L active. Remove 2 L of well-mixed solution (0.8 L active) and add 2 L water: 3.2/10 = **32%**. The formula initial concentration ×(1−removed/total)^n applies to repeated *equal-volume replacement with full mixing each time*.

## 8. Data interpretation

| Quarter | Applicants | Offers | Joined |
|---|---:|---:|---:|
| Q1 | 200 | 50 | 40 |
| Q2 | 250 | 60 | 45 |
| Q3 | 300 | 75 | 60 |

**Pattern A — growth:** Applicants Q1→Q2: (250−200)/200 = **25%**.  
**Pattern B — offer conversion:** Q3 offers/applicants = 75/300 = **25%**.  
**Pattern C — joining rate:** Q2 joined/offers = 45/60 = **75%**.  
**Pattern D — aggregate:** Total joined = 40+45+60 = **145**; overall joined/offers = 145/(50+60+75) = 145/185 ≈ **78.4%**. Do not average the three quarterly rates unless denominators are equal.

**Chart routine:** Read title, period, units, legend, and whether figures are cumulative. For close answer choices calculate exactly; approximation is useful only when choices are well separated.

## 9. Probability and counting

**Without replacement:** Bag has 3 red, 2 blue. Probability both draws blue = (2/5)(1/4) = **1/10**. With replacement it would be (2/5)² = 4/25.

**At least one:** Two fair coin tosses; P(at least one head) = 1 − P(no head) = 1−(1/2)² = **3/4**.

**Choose versus order:** Choose 2 people from 5 for a team: 5C2=**10**. Assign president and secretary from 5: 5P2=**20**, because roles distinguish order.

## 10. Number patterns and algebra

**Remainder pattern:** A number leaves remainder 2 on division by 3 and 5. Numbers are 15k+2; the smallest **positive** one is **2** if k=0 is permitted. If it must be **greater than both divisors**, the smallest is **17**. Read the wording before applying LCM+r.

**Quadratic:** For 2x²−7x+3=0, sum of roots = −b/a = 7/2; product = c/a = 3/2. Factorisation gives roots **3 and 1/2**.

## Practice: solve before reading answers

1. After a 25% rise, a value is 500. Original? **400** (500/1.25).
2. Groups of 12 and 18 average 50 and 60. Combined average? **56** ((600+1080)/30).
3. A completes a job in 10 days, B in 15. Together? **6 days** (1/10+1/15=1/6).
4. A 15% discount followed by 20% discount: effective discount? **32%** (1−.85×.8).
5. Draw one card from a standard 52-card deck. Probability of a heart? **1/4** (13/52).

**Next step:** Repeat only missed patterns, then use [Aptitude Practice Set](Aptitude_Practice_Set.md) under a timer.
