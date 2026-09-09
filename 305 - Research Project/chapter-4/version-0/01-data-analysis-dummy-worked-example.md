# 01 — Chapter 4 (Data Analysis and Interpretation): DUMMY DATA Worked Example

> **⚠️ EVERY NUMBER IN THIS FILE IS FAKE.** Generated with a fixed random seed (n=80, matching the department's minimum sample), not collected from real Union Bank employees. Purpose: show exactly how each statistic is calculated so you understand the mechanics before you have real data. **Delete or replace every number here once you run your actual pilot/full data through SPSS.** Don't cite anything in this file in your actual dissertation.

**Why the results look mixed (some significant, some not):** deliberately built that way. A dataset where everything comes out perfectly significant would teach you nothing about how to *write up* a non-significant finding — which you'll almost certainly need to do with real data too (see [MSSW-PROJECT-LAYOUT-AND-WORDINGS.md](../../MSSW-PROJECT-LAYOUT-AND-WORDINGS.md) for exactly this — Hari Kishore's thesis got caught not addressing a contradiction honestly). This file shows both cases.

Instrument: [chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md](../../chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md) (30 items, 6 constructs: HL=8, TC=3, EN=4, TE=5, KR=5, JP=5). Hypotheses: [chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md](../../chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md).

---

## 4.1 Descriptive Analysis

### Step 1 — From raw responses to a construct score

Each respondent answers several Likert items (1-5) per construct. The construct score for that respondent is just the **mean of their items**.

**Worked example — Respondent #1's Learner Engagement (EN) score**, from their 4 EN items:

| Item | EN1 | EN2 | EN3 | EN4 |
|---|---|---|---|---|
| Response | 4 | 3 | 4 | 4 |

```
EN score = (4 + 3 + 4 + 4) / 4 = 15 / 4 = 3.75
```

That single number (3.75) is what goes into every later calculation for this respondent's Engagement — correlation, regression, everything downstream uses construct scores like this, not raw items.

### Step 2 — Demographic profile (dummy, n=80)

| Age group | n | % |
|---|---|---|
| Below 25 | 9 | 11.3% |
| 25-34 | 18 | 22.5% |
| 35-44 | 22 | 27.5% |
| 45-54 | 21 | 26.3% |
| 55 and above | 10 | 12.5% |

| Experience | n | % |
|---|---|---|
| <5 years | 13 | 16.3% |
| 5-10 years | 26 | 32.5% |
| 11-15 years | 19 | 23.8% |
| 16-20 years | 11 | 13.8% |
| >20 years | 11 | 13.8% |

| Job level | n | % |
|---|---|---|
| Clerical | 36 | 45.0% |
| Officer | 26 | 32.5% |
| Managerial | 15 | 18.8% |
| Other | 3 | 3.8% |

| Delivery-mode group (derived from Section A Q5/Q6, used for H6/H7) | n | % |
|---|---|---|
| Digital-only | 15 | 18.8% |
| Classroom-only | 19 | 23.8% |
| Blended | 46 | 57.5% |

### Step 3 — Construct-level means and SD

| Construct | Items | Mean | SD | Interpretation (per [04-base-questionnaire sec 5](../../chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md) scale) |
|---|---|---|---|---|
| Hybrid Learning (HL) | 8 | 3.77 | 0.52 | High (3.41-4.20) |
| Trainer Competence (TC) | 3 | 3.51 | 0.65 | High |
| Learner Engagement (EN) | 4 | 3.70 | 0.53 | High |
| Training Effectiveness (TE) | 5 | 3.80 | 0.56 | High |
| Knowledge Retention (KR) | 5 | 3.50 | 0.61 | High (just above the 3.41 cutoff) |
| Job Performance (JP) | 5 | 3.76 | 0.53 | High |

**How to read this:** SD tells you spread, not just level. TC (SD=0.65) has the most disagreement among respondents; HL and EN (SD≈0.52-0.53) are the most consistent.

---

## 4.2 Inferential Analysis

### Step 4 — Reliability: Cronbach's Alpha, fully worked (EN, 4 items)

Formula (already defined conceptually in [chapter-1/version-0/05-key-terminology-glossary.md](../../chapter-1/version-0/05-key-terminology-glossary.md)):

```
α = (k / (k-1)) × (1 − Σ(item variances) / (variance of the summed score))
```

Using the real simulated data (n=80):

| Item | Variance |
|---|---|
| EN1 | 0.4745 |
| EN2 | 0.4745 |
| EN3 | 0.5918 |
| EN4 | 0.4658 |
| **Sum of item variances** | **2.0066** |

Variance of the **summed** score (EN1+EN2+EN3+EN4 per respondent, not the mean) = **4.4658**.

```
α = (4/3) × (1 − 2.0066/4.4658)
  = 1.333 × (1 − 0.4493)
  = 1.333 × 0.5507
  = 0.734
```

**α = 0.734 → acceptable** (department precedent, [chapter-2/version-0/05-past-dissertation-summary.md](../../chapter-2/version-0/05-past-dissertation-summary.md), treats ≥0.60-0.70 as usable, ≥0.70 as good).

Full reliability table (all 6 constructs, same formula applied by software — you'd get this directly from SPSS's Reliability Analysis, not hand-calculate every one):

| Construct | α |
|---|---|
| HL | 0.865 |
| TC | 0.767 |
| EN | 0.734 |
| TE | 0.808 |
| KR | 0.846 |
| JP | 0.811 |

All 6 clear 0.70 — in this dummy run. Real data might not; if any construct comes in under ~0.60, that's your cue to check the [09-literature-summary.md](../../chapter-2/version-0/04-literature-summary.md)-flagged items for that construct (JP5/JP4 redundancy was already flagged there as a candidate to review).

### Step 5 — Correlation, formula worked by hand on a small subset

Pearson's r formula:

```
r = [n·Σxy − Σx·Σy] / √([n·Σx² − (Σx)²] × [n·Σy² − (Σy)²])
```

Doing this by hand on all 80 respondents isn't realistic — SPSS/Excel does it in one click. But here's the mechanics on the **first 10 respondents' HL and EN scores** so you see what the software is actually doing:

| Resp | HL (x) | EN (y) | xy | x² | y² |
|---|---|---|---|---|---|
| 1 | 4.25 | 3.75 | 15.9375 | 18.0625 | 14.0625 |
| 2 | 3.62 | 3.00 | 10.86 | 13.1044 | 9.00 |
| 3 | 4.25 | 3.75 | 15.9375 | 18.0625 | 14.0625 |
| 4 | 3.50 | 3.50 | 12.25 | 12.25 | 12.25 |
| 5 | 3.62 | 2.75 | 9.955 | 13.1044 | 7.5625 |
| 6 | 3.50 | 2.50 | 8.75 | 12.25 | 6.25 |
| 7 | 2.88 | 4.00 | 11.52 | 8.2944 | 16.00 |
| 8 | 4.38 | 3.25 | 14.235 | 19.1844 | 10.5625 |
| 9 | 3.75 | 2.75 | 10.3125 | 14.0625 | 7.5625 |
| 10 | 4.00 | 4.75 | 19.00 | 16.00 | 22.5625 |
| **Σ** | 37.75 | 34.00 | 128.76 | 144.375 | 119.875 |

```
n = 10, Σx = 37.75, Σy = 34.00, Σxy = 128.76, Σx² = 144.375, Σy² = 119.875

numerator   = 10×128.76 − 37.75×34.00 = 1287.6 − 1283.5 = 4.1
denominator = √[(10×144.375 − 37.75²) × (10×119.875 − 34.00²)]
            = √[(1443.75 − 1425.0625) × (1198.75 − 1156.00)]
            = √[18.6875 × 42.75] = √799.09 ≈ 28.27

r (first 10 only) = 4.1 / 28.27 ≈ 0.145
```

That's just illustration on 10 rows — small samples swing a lot. The **real correlation using the full n=80** (computed properly, same formula, just more rows) is:

**r(HL, EN) = 0.343** — moderate positive, consistent with H1 (Hybrid Learning → Engagement).

Full correlation matrix (n=80, from software):

| | HL | TC | EN | TE | KR | JP |
|---|---|---|---|---|---|---|
| **HL** | 1.000 | -0.084 | **0.343** | 0.181 | 0.047 | 0.055 |
| **TC** | | 1.000 | 0.032 | 0.033 | 0.025 | -0.078 |
| **EN** | | | 1.000 | **0.228** | 0.083 | 0.028 |
| **TE** | | | | 1.000 | **0.483** | -0.053 |
| **KR** | | | | | 1.000 | **0.296** |
| **JP** | | | | | | 1.000 |

**Read this before regression:** TE↔KR (0.483) is your strongest relationship — matches the chain. TC's correlations with everything are near zero (-0.08 to 0.03) — early warning that H1b (Trainer Competence → Engagement) is going to struggle in regression too.

### Step 6 — Simple regression, fully worked by hand (bivariate: EN = HL only, n=10 subset)

Multiple regression (2+ predictors) needs matrix algebra — that's what SPSS is for, you won't hand-derive it. But **simple** (one-predictor) regression you can, and the logic transfers directly:

```
b (slope)     = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²
a (intercept) = ȳ − b·x̄
```

Using the same 10-respondent HL/EN data above: x̄ = 3.775, ȳ = 3.400.

| Resp | x−x̄ | y−ȳ | (x−x̄)(y−ȳ) | (x−x̄)² |
|---|---|---|---|---|
| 1 | 0.475 | 0.35 | 0.166 | 0.226 |
| 2 | -0.155 | -0.40 | 0.062 | 0.024 |
| 3 | 0.475 | 0.35 | 0.166 | 0.226 |
| 4 | -0.275 | 0.10 | -0.028 | 0.076 |
| 5 | -0.155 | -0.65 | 0.101 | 0.024 |
| 6 | -0.275 | -0.90 | 0.248 | 0.076 |
| 7 | -0.895 | 0.60 | -0.537 | 0.801 |
| 8 | 0.605 | -0.15 | -0.091 | 0.366 |
| 9 | -0.025 | -0.65 | 0.016 | 0.001 |
| 10 | 0.225 | 1.35 | 0.304 | 0.051 |
| **Σ** | | | **0.407** | **1.871** |

```
b = 0.407 / 1.871 ≈ 0.218
a = 3.400 − 0.218×3.775 ≈ 3.400 − 0.823 ≈ 2.577

Regression equation (n=10 illustration): EN = 2.577 + 0.218 × HL
```

Interpretation of `b`: for every 1-point increase in HL score, EN is predicted to rise by ~0.218 points (on this 10-row toy example — the real 80-row multiple regression below gives the actual number to report).

### Step 7 — The 4 real regression models (n=80, from software — this is what you'll actually run and report)

**Model 1: EN = HL + TC** (tests H1, H1b)

| Predictor | B | SE | t | p |
|---|---|---|---|---|
| Intercept | 2.175 | 0.540 | 4.026 | <.001 |
| HL | **0.357** | 0.110 | 3.250 | **.0017** ✅ H1 supported |
| TC | 0.050 | 0.088 | 0.573 | .5682 ❌ H1b **not** supported |

R² = .1215 → HL and TC together explain 12.15% of variance in Engagement. F(2,77) = 5.327, p = .0068 — model overall significant, but that's carried entirely by HL; TC's own path is not significant.

**Model 2: TE = HL + TC + EN** (tests H2, and provides the "with mediator" step for H5a)

| Predictor | B | SE | t | p |
|---|---|---|---|---|
| Intercept | 2.459 | 0.655 | 3.752 | <.001 |
| HL | 0.132 | 0.129 | 1.018 | .3121 |
| TC | 0.032 | 0.097 | 0.331 | .7414 |
| EN | 0.196 | 0.126 | 1.563 | .1222 ❌ H2 **not** supported at p<.05 in this run |

R² = .0652, F(3,76) = 1.766, p = .1608 — **model itself is not significant.** Honest write-up: "Engagement did not significantly predict Training Effectiveness in this sample (β=.196, p=.122)."

**Model 3: KR = HL + TC + EN + TE** (tests H3)

| Predictor | B | SE | t | p |
|---|---|---|---|---|
| Intercept | 1.681 | 0.707 | 2.380 | .0199 |
| HL | -0.043 | 0.129 | -0.334 | .7390 |
| TC | 0.006 | 0.096 | 0.058 | .9537 |
| EN | -0.020 | 0.126 | -0.157 | .8753 |
| TE | **0.537** | 0.114 | 4.728 | **<.0001** ✅ H3 strongly supported |

R² = .2356, F(4,75) = 5.780, p = .0004. Once TE is in the model, HL/TC/EN drop to near-zero — TE is doing essentially all the work predicting KR here.

**Model 4: JP = HL + TC + EN + TE + KR** (tests H4)

| Predictor | B | SE | t | p |
|---|---|---|---|---|
| Intercept | 3.275 | 0.678 | 4.831 | <.0001 |
| HL | 0.069 | 0.119 | 0.577 | .5655 |
| TC | -0.061 | 0.089 | -0.691 | .4919 |
| EN | 0.035 | 0.117 | 0.303 | .7630 |
| TE | -0.263 | 0.120 | -2.193 | **.0314** — significant but *negative* |
| KR | **0.372** | 0.107 | 3.477 | **.0009** ✅ H4 supported |

R² = .1514, F(5,74) = 2.640, p = .0299. **Worth a comment in your write-up:** TE's negative coefficient here (while its zero-order correlation with JP was ~0, see matrix) is a *suppression effect* — once KR is controlled for, TE's unique contribution flips sign. Don't panic if you see this with real data; name it, don't ignore it.

### Step 8 — Mediation tests, Baron & Kenny + Sobel, fully worked

Per [chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md](../../chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md), 4 steps per mediator:
1. **c** — total effect (X → Y, no mediator)
2. **a** — X → M
3. **b** and **c′** — X + M → Y (b = mediator's effect, c′ = X's remaining direct effect)
4. **Indirect effect** = a×b; test significance via Sobel: `z = a·b / √(b²·SEa² + a²·SEb²)`

**H5a — EN mediates HL → TE:**

| Path | Value | SE | p |
|---|---|---|---|
| c (total, HL→TE) | 0.197 | — | .1078 (n.s.) |
| a (HL→EN) | 0.352 | 0.109 | .0018 ✅ |
| b (EN→TE \| HL) | 0.199 | 0.125 | .1143 (n.s.) |
| c′ (direct, HL→TE \| EN) | 0.127 | — | .3229 (n.s.) |

```
indirect = a×b = 0.352 × 0.199 = 0.0701
Sobel SE = √(b²·SEa² + a²·SEb²) = √(0.199²×0.109² + 0.352²×0.125²)
         = √(0.03960×0.01188 + 0.12390×0.01563)
         = √(0.00047 + 0.00194) = √0.00241 ≈ 0.0490
Sobel z = 0.0701 / 0.0490 ≈ 1.431 → p ≈ .152
```

**Not significant.** Write-up: "Contrary to H5a, Learner Engagement did not significantly mediate the relationship between Hybrid Learning and Training Effectiveness in this sample (Sobel z=1.43, p=.152) — note the total effect (c) itself was already non-significant, so mediation could not be demonstrated regardless."

**H5b — TE mediates EN → KR:**

```
a (EN→TE) = 0.242 (p=.0423)   b (TE→KR|EN) = 0.533 (p<.0001)
c (total, EN→KR) = 0.096 (p=.4652, n.s.)   c′ (direct) = -0.033 (p=.7803, n.s.)
indirect = 0.242 × 0.533 = 0.1288
Sobel SE = √(0.533²×0.109²... ) ≈ 0.0680
Sobel z = 0.1288/0.0680 ≈ 1.895 → p ≈ .058
```

**Borderline** — just above the conventional .05 cutoff. Honest phrasing: "a marginally non-significant indirect effect (p=.058) suggestive of mediation, falling just short of conventional significance — a larger sample may resolve this."

**H5c — KR mediates TE → JP:**

```
a (TE→KR) = 0.526 (p<.0001)   b (KR→JP|TE) = 0.367 (p=.0008)
c (total, TE→JP) = -0.051 (p=.6387, n.s.)   c′ (direct) = -0.243 (p=.0371, significant, negative)
indirect = 0.526 × 0.367 = 0.1927
Sobel z ≈ 2.831 → p ≈ .0046 ✅ significant
```

**The interesting case.** The indirect effect (via KR) is significant even though the *total* effect (c) was not — this is called **inconsistent mediation** (direct and indirect effects have opposite signs, partly cancelling out). Worth naming explicitly if it happens with real data — a student who only checks "is c significant?" before testing mediation would wrongly conclude "no relationship to explain," missing a genuine effect happening underneath.

### Step 9 — t-test and ANOVA, worked from group means

Formula: `t = (M1 − M2) / SE(difference)`, where for unequal variances (Welch's t): `SE = √(SD1²/n1 + SD2²/n2)`.

**H7 test — Job Performance, Blended vs Digital-only:**

| Group | n | Mean | SD |
|---|---|---|---|
| Blended | 46 | 3.748 | 0.527 |
| Digital-only | 15 | 3.747 | 0.639 |

```
SE = √(0.527²/46 + 0.639²/15) = √(0.00604 + 0.02722) = √0.03326 ≈ 0.1824
t = (3.748 − 3.747) / 0.1824 ≈ 0.006
```

**t ≈ 0.006, p ≈ .995 — no difference at all.** H7 not supported in this dummy run.

**One-way ANOVA** (3 groups, KR and JP) — formula: `F = MSbetween / MSwithin`, software-computed here since hand-deriving sums of squares across 80 rows isn't practical, but the logic is: does the variance *between* group means exceed the variance *within* each group by more than chance?

| Outcome | Digital-only mean | Classroom-only mean | Blended mean | F(2,77) | p |
|---|---|---|---|---|---|
| KR (H6) | 3.347 | 3.421 | 3.587 | 1.101 | .3377 (n.s.) |
| JP (H7) | 3.747 | 3.779 | 3.748 | 0.025 | .9757 (n.s.) |

Neither H6 nor H7 supported here — group means look different on paper (Blended highest on KR) but not enough given the spread within each group.

---

## 4.3 Interpretation of Results — Hypothesis Summary Table

| # | Hypothesis | Result (dummy) | Decision |
|---|---|---|---|
| H1 | HL → EN | β=.357, p=.0017 | ✅ Supported |
| H1b | TC → EN | β=.050, p=.568 | ❌ Not supported |
| H2 | EN → TE | β=.196, p=.122 | ❌ Not supported |
| H3 | TE → KR | β=.537, p<.0001 | ✅ Supported |
| H4 | KR → JP | β=.372, p=.0009 | ✅ Supported |
| H5a | EN mediates HL→TE | Sobel z=1.43, p=.152 | ❌ Not supported |
| H5b | TE mediates EN→KR | Sobel z=1.90, p=.058 | ⚠️ Marginal |
| H5c | KR mediates TE→JP | Sobel z=2.83, p=.005 | ✅ Supported (inconsistent mediation) |
| H6 | Blended > digital-only on KR | F=1.10, p=.338 | ❌ Not supported |
| H7 | Blended > digital/classroom on JP | F=0.03, p=.976 | ❌ Not supported |

**Note the honest pattern:** the "downstream" half of the chain (TE→KR→JP) held up well; the "upstream" half (HL/TC→EN→TE) mostly didn't in this particular dummy run. With real data your pattern will differ — the point of this exercise is the *method* of reading and reporting results like this, not these specific numbers.

## 4.4 Comparison with Previous Studies

With real results, compare against [chapter-2/version-0/08-base-paper.md](../../chapter-2/version-0/08-base-paper.md) (Saroj, Sahney & Sekar 2026 — your base paper) and the wider matrix in [chapter-2/version-0/03-literature-matrix.md](../../chapter-2/version-0/03-literature-matrix.md). E.g., if your H1 (HL→EN) comes out supported like this dummy run, that's consistent with the base paper's own acceptance→engagement path.

## 4.5 Theoretical and Practical Implications

Placeholder — write after real results. Structure: one paragraph theoretical (what this adds to the literature gap named in [chapter-2/version-0/06-gap.md](../../chapter-2/version-0/06-gap.md)), one paragraph practical (HR strategy scorecard style, per [chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md](../../chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md) sec 12 format).

---

**Cross-references:** [chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md](../../chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md) · [chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md](../../chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md) · [chapter-1/version-0/05-key-terminology-glossary.md](../../chapter-1/version-0/05-key-terminology-glossary.md) · [chapter-5/version-0/01-conclusion-dummy-worked-example.md](../../chapter-5/version-0/01-conclusion-dummy-worked-example.md) · **real-chapter skeleton:** [02-chapter4-template-academic-prose.md](02-chapter4-template-academic-prose.md) · [PLAN.md](../../PLAN.md) · [SEQUENCE.md](../../SEQUENCE.md)
