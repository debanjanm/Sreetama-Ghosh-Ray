# SPSS Beginner's Guide — For This Thesis

This guide is written for someone who has never opened SPSS before. It uses the actual file and variable names already prepared for this study, so you can follow it exactly against your own data.

---

## 1. What SPSS actually is

SPSS (Statistical Package for the Social Sciences, now sold by IBM as "IBM SPSS Statistics") is software built specifically for the kind of analysis this thesis needs — frequencies, reliability (Cronbach's alpha), correlation, and regression — done by clicking menus rather than writing code. It's the standard tool in social-science and management dissertations for exactly that reason: guides and examiners expect to see SPSS output tables, not a spreadsheet formula.

Two windows matter, and you'll switch between them constantly:
- **Data Editor** — where your data lives (this is what you'll import).
- **Output Viewer** — opens automatically the first time you run any analysis; every table and chart you produce appears here, in order, and can be saved as one file.

---

## 2. Getting it on Windows

**First, check if you already have free access** — this is the most likely path and the right one to check before paying anything:
- MSSW / your university library or IT department may provide a **free student license** or a campus-wide install. Ask the department office or check the university's software portal first. Many Indian universities provide SPSS through their computer labs or a site license you can install on your own laptop for the duration of your programme.

**If no institutional access exists:**
- IBM offers a **free 14-day trial** of SPSS Statistics at ibm.com/products/spss-statistics (search "IBM SPSS Statistics free trial"). Enough to run everything this thesis needs if you do it in one sitting.
- A paid **student/monthly subscription** is available through IBM's own site if the trial isn't enough time.

**Installation steps once you have a download link or installer:**
1. Download the Windows installer (.exe) from the official IBM link or your university portal — not a third-party mirror.
2. Run the installer, accept the license, choose the default install location.
3. It will ask for a license — either an authorization code (from your university) or it will activate the trial automatically.
4. Restart if prompted. Open "IBM SPSS Statistics" from the Start menu.

Avoid downloading SPSS from random file-sharing sites — beyond the legal issue, cracked installers are a common malware vector.

---

## 3. Orientation — what you're looking at

When SPSS opens, you'll see the **Data Editor** with two tabs at the bottom-left:
- **Data View** — rows are respondents, columns are variables (HL1, HL2, etc.) — looks like Excel.
- **Variable View** — one row per variable, showing its name, type, decimal places, and label. You won't need to touch this manually; importing the CSV fills it in for you.

The menu bar across the top (Analyze, Graphs, Transform, etc.) is where everything happens. **Analyze** is the one you'll use almost exclusively.

---

## 4. Importing this study's data

Your file is `final-analysis-data.csv`, already scored (103 rows, one per profile-complete respondent, with `Hybrid_Learning`, `Trainer_Competence`, `Learner_Engagement`, `Training_Effectiveness` already calculated as construct means).

1. Open SPSS → **File → Open → Data...**
2. In the file-type dropdown, choose **CSV (*.csv)**.
3. Browse to `final-analysis-data.csv` and open it.
4. A "Text Import Wizard" appears:
   - Does your file match a predefined format? → **No**.
   - Delimited, and "Are variable names included at the top?" → **Yes**.
   - Delimiter → **Comma**.
   - Click through **Next** on the remaining screens (defaults are fine), then **Finish**.
5. Check Data View — you should see 103 rows and columns including `response_id`, `HL1`...`TE7`, and the four construct-mean columns.

**Shortcut:** a ready-made syntax file, `final-analysis-spss-syntax.sps`, already exists in this same folder and does steps above automatically plus runs every analysis below in one go. To use it: **File → Open → Syntax**, open that file, then **Run → All**. The menu steps below are for understanding *what* that syntax does and for running things individually if you want to double-check one result at a time.

---

## 5. Running each analysis (menu method)

### 5.1 Respondent profile (frequencies)

**Analyze → Descriptive Statistics → Frequencies**
Move `age_group`, `service_length`, `job_level` into the "Variable(s)" box → **OK**.
Output: a frequency table per variable — matches Chapter 4's Tables 4.2–4.4.

### 5.2 Item and construct descriptives (mean, SD)

**Analyze → Descriptive Statistics → Descriptives**
Move `HL1` through `TE7` and the four construct-mean columns into the box.
Click **Options**, tick Mean, Std. deviation, Minimum, Maximum → **Continue → OK**.
Output: one table with mean/SD per item and per construct — matches Tables 4.5–4.9.

### 5.3 Reliability — Cronbach's alpha (do this four times, once per construct)

**Analyze → Scale → Reliability Analysis**
- Move **HL1 to HL7 only** into "Items" → Model: **Alpha** → **OK**. Note the alpha value.
- Repeat with **TC1 to TC6** only.
- Repeat with **LE1 to LE6** only.
- Repeat with **TE1 to TE7** only.

Important: each run uses *only* the items for that one construct — don't mix constructs in the same run, or the alpha will be meaningless. Expected results for this dataset: HL ≈ .962, TC ≈ .969, LE ≈ .958, TE ≈ .972 (Table 4.10).

### 5.4 Correlation (tests H1, H2, H3)

**Analyze → Correlate → Bivariate**
Move all four construct-mean columns (`Hybrid_Learning`, `Trainer_Competence`, `Learner_Engagement`, `Training_Effectiveness`) into "Variables".
Correlation Coefficient: **Pearson** (default, leave checked). Test of Significance: **Two-tailed** (default) → **OK**.
Output: a 4×4 correlation matrix with significance stars — matches Table 4.11. Read HL↔LE, TC↔LE, and LE↔TE for H1/H2/H3.

### 5.5 Regression Model 1 — what predicts Learner Engagement?

| Role | Variable | In SPSS |
|---|---|---|
| **Dependent variable** (the outcome being explained) | Learner Engagement — `Learner_Engagement` | "Dependent" box |
| **Independent variable 1** (predictor) | Hybrid Learning — `Hybrid_Learning` | "Independent(s)" box |
| **Independent variable 2** (predictor) | Trainer Competence — `Trainer_Competence` | "Independent(s)" box |

This is a multiple regression: two independent variables, one dependent variable. It supports H1 and H2.

**Analyze → Regression → Linear**
1. Move `Learner_Engagement` into **Dependent**.
2. Move `Hybrid_Learning` and `Trainer_Competence` into **Independent(s)**. Leave Method as *Enter*.
3. Click **Statistics**, tick Estimates, Model fit and **Collinearity diagnostics**, then **Continue → OK**.

Output: Model Summary (R, R²), ANOVA (F, significance) and Coefficients (B, Beta, t, Sig., Tolerance, VIF), matching Tables 4.13–4.14. Expected: R² = .569, F(2,100) = 66.070, VIF = 3.024.

### 5.6 Regression Model 2 — what predicts Training Effectiveness?

| Role | Variable | In SPSS |
|---|---|---|
| **Dependent variable** (the outcome being explained) | Training Effectiveness — `Training_Effectiveness` | "Dependent" box |
| **Independent variable** (predictor) | Learner Engagement — `Learner_Engagement` | "Independent(s)" box |

This is a simple regression: one independent variable, one dependent variable. It supports H3.

**Analyze → Regression → Linear**
1. Move `Training_Effectiveness` into **Dependent**. If Model 1's variables are still in the boxes, clear them first.
2. Move `Learner_Engagement` into **Independent(s)**.
3. Click **Statistics**, tick Estimates and Model fit, then **Continue → OK**.

Output matches Tables 4.15–4.16. Expected: R² = .585, F(1,101) = 142.647.

**Note on Learner Engagement:** it is the dependent variable in Model 1 and the independent variable in Model 2. This is not a mistake. It lets the two models describe a chain (Hybrid Learning and Trainer Competence → Learner Engagement → Training Effectiveness). Each is a separate association model, and neither is a formal mediation test. Say that plainly in the viva.

---

## 6. Reading the output — the four numbers examiners actually look at

- **Cronbach's Alpha** (Reliability output, top table) — above .70 is "acceptable," this study's values are all above .95.
- **Pearson Correlation (r) and Sig. (2-tailed)** — in the correlation matrix, `Sig.` below .05 means the relationship is statistically significant; the number above it is `r`.
- **R Square** (Model Summary table, regression) — the percentage of variation explained.
- **Sig.** in the Coefficients table — below .05 means that predictor's effect is statistically significant on its own within the model.

If a number you get doesn't match the expected values quoted above, don't panic — first check you selected the *construct-mean* columns (not the individual item columns) for correlation/regression, and only the correct 6 or 7 items for each reliability run.

---

## 7. Saving your output for the guide and viva

In the **Output Viewer** window: **File → Save As** → save as a `.spv` file (SPSS's own output format) — this preserves every table you ran, in order, exactly as produced. Keep this file; it's your proof that the numbers in Chapter 4 were actually run in SPSS, not just typed in.

To put a table into a Word document: right-click the table in the Output Viewer → **Copy** → paste into Word. It pastes as an editable table, not an image.

---

## 8. If something goes wrong

- **"Text Import Wizard" shows garbled columns** → you probably picked the wrong delimiter; go back and choose Comma, not Tab or Semicolon.
- **Reliability gives a negative or very low alpha** → you've likely included an item from the wrong construct, or a reverse-scored item is mixed in unreversed (this study has no reverse-scored items, so this shouldn't occur if only the correct 6–7 items are selected).
- **Regression won't run / "insufficient valid cases"** → check for typos in variable names in the Data Editor; all included item responses should appear as whole-number scores from 1 to 5.
