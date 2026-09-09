# 04 — Key Terminology Glossary

Every term below is explained with an example from your own Model-Alpha v1, not a generic textbook example — so you can point to your own diagram when a panel asks "what do you mean by X."

Current model, for reference throughout:
```
Hybrid Learning ─────┐
                      ├──▶ Learner Engagement ──▶ Training Effectiveness ──▶ Knowledge Retention ──▶ Job Performance
Trainer Competence ───┘
```

---

## 1. Variable Roles

### Independent Variable (IV)
The variable presumed to *cause* or *predict* change in another variable. It's the "input."

**In your model:** Hybrid Learning and Trainer Competence are both IVs at the start of the chain — they predict Learner Engagement.

### Dependent Variable (DV)
The variable being predicted or explained — the "output," what you're measuring the effect on.

**In your model:** Job Performance is the final DV — the outcome everything else is ultimately trying to explain.

**Important nuance — IV/DV is not fixed, it's test-specific:** In a chain model like yours, a variable can be a DV in one regression and an IV in the next. Learner Engagement is the DV in Regression Model 1 (`Engagement = Hybrid Learning + Trainer Competence`), but becomes an IV in Regression Model 2 (`Training Effectiveness = Hybrid Learning + Trainer Competence + Engagement`). Don't call Engagement "the IV" or "the DV" without saying *in which regression* — this is a common point of confusion when defending a chain model.

### Antecedent
A looser term than IV — a variable presumed to come *before* and influence another, used especially when a variable feeds into a mediator rather than directly into the final DV. You've been using this term precisely: Hybrid Learning and Trainer Competence are called **antecedents to Engagement** (not just "IVs") because their role is specifically to feed the mediator, not to be tested against the final outcome directly.

### Mediator
A variable that **explains the mechanism** — it sits between an IV and a DV and carries the effect from one to the other. The question a mediator answers: *"Does X affect Y because it first affects M?"*

**In your model, you have three mediators in sequence (a "serial" mediation chain):**
- Learner Engagement mediates Hybrid Learning/Trainer Competence → Training Effectiveness
- Training Effectiveness mediates Engagement → Knowledge Retention
- Knowledge Retention mediates Training Effectiveness → Job Performance

Full explanation with the "machine" analogy already in [03-atomic-concepts.md](03-atomic-concepts.md) sec 12 — this entry is the quick-reference version.

### Moderator
A variable that changes the **strength or direction** of a relationship between two other variables — it doesn't sit in the causal chain, it answers *"Does the X→Y relationship get stronger/weaker depending on Z?"* rather than "why does X affect Y."

**In your model:** you don't currently have one. Organizational/Supervisor Support was considered as a moderator (it moderates Engagement→Effectiveness in your base paper, Saroj et al. 2026) but was excluded — that's the rejected Model-Beta scope ([07-model-beta-chain-check.md](../../chapter-2/version-0/07-model-beta-chain-check.md)).

**Mediator vs moderator, one line each:** mediator = *mechanism* (why/how); moderator = *condition* (when/for whom). Full contrast already in [03-atomic-concepts.md](03-atomic-concepts.md) sec 12.

### Control Variable
A variable you deliberately measure so you can rule out alternative explanations, even though it's not part of your main model. You're not testing hypotheses about these — you're using them to check whether your main findings hold up across subgroups.

**In your model:** age, years of experience, job level, training frequency (Section A of [01-model-alpha-questionnaire.md](../../chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md)) — used for the t-test/ANOVA subgroup comparisons (H6-H8), not the core chain.

### Confounding Variable
An *un*measured or *uncontrolled* variable that could actually explain a relationship you're attributing to your model — a threat to internal validity, not something you're deliberately testing. Different from a control variable: a control variable is one you *did* account for; a confound is one you *didn't*, and it's a risk.

**Honest limitation to name in Chapter 6:** your design doesn't fully rule out confounds like general job satisfaction, workload, or manager quality independent of training — you control for demographics via subgroup comparison, but that's not the same as statistically isolating confounds the way a randomized experiment would. Say this explicitly rather than let a panel find it.

---

## 2. Statistical Terms

### Parametric vs Non-Parametric Statistics

Your department's own guidelines document says explicitly: *"Tools to be used for statistics can be parametric or non-parametric tests."* Here's what that choice actually means.

**Parametric tests** assume your data follows certain conditions — usually: normally distributed, interval/ratio-level measurement, roughly equal variance across groups. They're more statistically powerful *if* those assumptions hold.

**Non-parametric tests** make no assumption about the distribution — safer when data is skewed, ordinal, or your sample is small, but less powerful (harder to detect a real effect if one exists).

| Your planned test (parametric) | Non-parametric equivalent (fallback if assumptions fail) |
|---|---|
| Pearson correlation | Spearman's rank correlation |
| Independent-samples t-test | Mann-Whitney U test |
| One-way ANOVA | Kruskal-Wallis test |
| Linear/multiple regression | (no direct equivalent — check assumptions carefully before running) |

**Practical note for your project:** Likert-scale data (1-5) is technically ordinal, not interval — using parametric tests on it is a common, generally-accepted convention in social science (treating a 5-point scale as approximately continuous), not a strict violation, but it's worth stating this convention explicitly in your methodology chapter rather than assuming it's obvious. Before running your main analysis, check normality (skewness/kurtosis or a Shapiro-Wilk test in SPSS) — if badly violated, that's your cue to switch to the non-parametric column above for that specific test.

### Reliability — Cronbach's Alpha
Whether the items *within one construct* are measuring the same thing consistently. Already covered in [01-base-questionnaire-and-calculation.md](../../chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md) sec 6, Test 2 — this entry just flags it belongs in this glossary too. Run separately for each of your 6 constructs now (HL, Trainer Competence, Engagement, TE, KR, JP) — not one alpha for the whole 55-item instrument.

### Validity
Whether you're actually measuring what you claim to measure — a different question from reliability (you can be reliably wrong).
- **Content validity** — do the items adequately cover the construct? Established via expert/supervisor review of your instrument (your next step).
- **Face validity** — does it look reasonable to a non-expert respondent? Established via pilot testing.
- **Construct validity** — does it actually measure the underlying theoretical construct, not something else? Harder to establish with a small master's-level study; citing your items back to theory (per [04-literature-summary.md](../../chapter-2/version-0/04-literature-summary.md)) is your main defense here.

### Construct, Dimension, Item — the measurement hierarchy
- **Construct** — the abstract thing you're trying to measure (e.g., "Hybrid Learning").
- **Dimension** (sub-construct) — a named component of the construct (e.g., Hybrid Learning's five dimensions: Flexibility, Accessibility, Interaction, Technology, Integration).
- **Item** — one actual questionnaire statement (e.g., HL1: "I can choose when to go through the online parts of the training").

Your instrument follows this hierarchy throughout — useful to state explicitly in Chapter 3 as your measurement model.

### Correlation vs Regression vs Mediation — what each one actually tells you
- **Correlation** — are two variables related? (Doesn't tell you direction of causality, or control for other variables.)
- **Regression** — does one or more variables *predict* another, controlling for the others in the same model? (Still not proof of causation, but a stronger claim than plain correlation.)
- **Mediation test** (Baron & Kenny or Hayes PROCESS) — does the predictor's effect on the outcome *run through* a third variable? This is the only one of the three that directly tests your H5a-c hypotheses.

### SEM (Structural Equation Modeling) and Path Analysis
SEM is the method your base paper (Saroj, Sahney & Sekar, 2026) uses — it tests an entire multi-variable model (all paths simultaneously) in one statistical procedure, typically in software like AMOS or R (lavaan). Your project instead runs the chain as a series of separate regressions plus a mediation macro (PROCESS) — a simpler, SPSS-based approach, standard at the department's level per [05-past-dissertation-summary.md](../../chapter-2/version-0/05-past-dissertation-summary.md) (none of the 8 reference theses used SEM). Worth naming this explicitly as a methodological difference from your base paper if asked why you didn't replicate its exact statistical method.

### Sample, Population, Sampling Technique
- **Population** — everyone your study is theoretically about (Union Bank of India employees who've had blended training).
- **Sample** — the actual respondents you collect data from (target ~80-130, per department norm).
- **Sampling technique** — how you select them. Your plan uses **convenience sampling** (whoever is accessible/willing), the technique used in every one of your 8 reference theses — not random sampling, which limits how far you can generalize findings, worth naming as a limitation.

### Pilot Test
A small trial run of your instrument (department norm: 20-30 respondents, per [05-past-dissertation-summary.md](../../chapter-2/version-0/05-past-dissertation-summary.md) sec 9.1) before full data collection — used to check reliability (Cronbach's alpha per section) and catch confusing items before they cost you real respondents.

### Hypothesis: H0 vs H1, Directional vs Non-Directional
- **Null hypothesis (H0)** — "no significant relationship/difference exists." What your statistical test tries to reject.
- **Alternative hypothesis (H1, H2...)** — what you actually predict (e.g., your H1: "Hybrid Learning has a significant positive effect on Learner Engagement" implicitly has an H0: "no significant effect").
- **Directional** — predicts the direction of effect ("positive effect") — all your chain hypotheses (H1, H1b, H2-H4) are directional.
- **Non-directional** — predicts a relationship exists without specifying direction — none of your current hypotheses are non-directional, but useful to know the term if a supervisor asks about it.

### Cross-Sectional vs Longitudinal Design
- **Cross-sectional** — data collected at one point in time. **This is your design** — one questionnaire, one round of data collection.
- **Longitudinal** — data collected at multiple points over time (e.g., Agarwal et al. 2026 in your matrix tracked employees over time).

Worth naming explicitly as a limitation: your KR (retention) and JP (performance) items ask respondents to self-report *perceived* change, since you're not measuring the same person before and after training at two separate time points. This is the same practical constraint already discussed for KR1-9 in [04-literature-summary.md](../../chapter-2/version-0/04-literature-summary.md) sec 4.

---

**Cross-references:** [02-guide-suggestion.md](02-guide-suggestion.md) · [03-atomic-concepts.md](03-atomic-concepts.md) (full mediator/moderator explanation) · [01-base-questionnaire-and-calculation.md](../../chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md) (stats basics already covered) · [04-literature-summary.md](../../chapter-2/version-0/04-literature-summary.md) · [05-past-dissertation-summary.md](../../chapter-2/version-0/05-past-dissertation-summary.md) · [01-research-objectives-and-hypotheses.md v1](../../chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md) · [01-model-alpha-questionnaire.md v1](../../chapter-3/questionnaire/version-2/01-model-alpha-questionnaire.md) · [PLAN.md](../../PLAN.md)
