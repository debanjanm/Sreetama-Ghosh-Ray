# 08 — Base Paper: Selection, Search Process, and Model-Alpha Comparison

**What a base paper is, per department convention.** Not something named in the official 2026 guidelines PDF, but a convention your guide clearly expects — confirmed by checking 4 reference theses from the same department ([05-past-dissertation-summary.md](05-past-dissertation-summary.md)), every one of which names a single anchor paper and explains how the student's study narrows or extends it. A base paper is the one published study whose variables, mechanism, and (ideally) measurement approach your model is directly modeled after — not just "a paper I cite somewhere," but the specific study you can point to and say "my model is this paper, adapted."

---

## 1. Search Process

Base-paper selection wasn't a separate search — it's the output of the literature work already done across three passes, re-examined specifically for "which one paper is closest":

1. **First-pass search** ([01-initial-literature-search.md](01-initial-literature-search.md)) — ~10 papers, Google Scholar-style web queries on hybrid/blended workplace learning, engagement, training effectiveness.
2. **Systematic matrix** ([03-literature-matrix.md](03-literature-matrix.md)) — expanded to 36 papers/instruments across 10 constructs, queries run against Google Scholar-indexed sources and cross-checked where possible directly against publisher pages (ScienceDirect, SAGE, Emerald, Frontiers, PubMed, Wiley, Taylor & Francis, DOI resolvers). Two entries — including the eventual base paper — were verified by fetching the actual publisher page, not just a search snippet, specifically because they were the strongest candidates and needed the highest confidence.
3. **Targeted follow-up** ([07-model-beta-chain-check.md](07-model-beta-chain-check.md)) — re-fetched the leading candidate directly a second time, specifically to confirm what its model does and doesn't test, before treating it as the anchor for Model-Alpha.

**Selection criteria applied** (same five questions used throughout this project, per [02-guide-suggestion.md](../../chapter-1/version-0/03-guide-suggestion.md) and [04-literature-summary.md](04-literature-summary.md)):

1. Closest match to your actual IV→mediator→DV mechanism (not just similar keywords).
2. Genuine workplace/organizational context — not higher education or K-12.
3. Empirical, testable model (mediation/SEM), not a review or meta-analysis.
4. Independently verifiable — fetched and confirmed, not taken on a search snippet alone.
5. Recent enough to reflect current blended-learning practice, not pre-2015 assumptions.

---

## 2. Candidates Considered and Why Each Was Not Chosen

| # | Candidate | Why it looked promising | Why not chosen as base paper |
|---|---|---|---|
| 1 | Agarwal, Goyal, Kumar & Modi (2026) — Indian financial-services hybrid employee-development | Indian context, financial sector — closest geographic/sector match | Tests a hybrid *intervention* → performance directly; no engagement mediator, no mechanism model. Good supporting citation, wrong shape for a base paper. |
| 2 | Lee (2010) — blended training design, Korean corporate university | Explicitly about workplace training transfer design | 2010, pre-dates current LMS/mobile blended-learning technology; transfer-focused, not engagement-mediation-focused; qualitative+quantitative mixed, not a clean testable SEM model to adapt. |
| 3 | Bin Mubayrik (2018) — systematic review, workplace blended learning | Directly on-topic population (workplace, not higher-ed) | It's a review of 17 studies, not a single empirical model — nothing to structurally adapt. |
| 4 | Wakekar et al. (2026) — blended learning, TB community health workers | Strong empirical design, real retention data (78.2% vs 62.4%) | Health-sector context, not banking/corporate; no engagement variable at all; measures retention as a single test score, not the multi-item structure Model-Alpha uses. |
| 5 | Ye, Kuang & Liu (2022) — ICT self-efficacy, organizational support, blended learning use | Best-verified instrument in the whole matrix (fetched directly, published item-level scales) | Population is teachers, not corporate employees; tests technology antecedents to *use* of blended learning, not a mediation chain to training/retention/performance outcomes. |
| 6 | Jain & Jain (2015) — training effectiveness, Indian banks | Direct Indian-banking-sector match | 2015, pre-dates hybrid/blended-learning framing entirely (compares public/private/foreign banks generally); no mediator tested; fetch blocked (403) — never independently verified. |

None of these six is wrong to cite — several already appear throughout [03](03-literature-matrix.md) as supporting evidence. None of them, though, is the single closest structural match. One paper cleared all five criteria at once.

---

## 3. Base Paper Selected

**Saroj, S., Sahney, S., & Sekar, S. (2026).** "Antecedents and consequences of learners' engagement: examining moderating role of supervisor support in workplace blended learning." *VJIKMS* (Vine Journal of Information and Knowledge Management Systems), Vol. 56, No. 2, pp. 452–474.

| Field | Detail |
|---|---|
| DOI | doi.org/10.1108/VJIKMS-12-2024-0454 |
| Verification | Fetched directly from publisher (emerald.com) — twice, in [03](03-literature-matrix.md) and again in [07](07-model-beta-chain-check.md). Highest-confidence source in the entire matrix. |
| Country / context | India — genuine workplace blended-learning training setting (organization not named in the paper) |
| Sample | 375 employees |
| Method | Survey, Structural Equation Modeling (SPSS + AMOS) |
| Variables tested | Blended-learning acceptance, Instructor competence, Metacognitive skills → **Learner Engagement** (mediator) → Employee agility (outcome); Supervisor support (moderator on engagement→agility) |
| Key findings | Acceptance, instructor competence, and metacognitive skills all positively predict engagement; engagement positively predicts employee agility; supervisor support strengthens the engagement→agility relationship |

### Why this paper, specifically

- It is the **only** paper in the 36-paper matrix set in a genuine workplace blended-learning training context with a formally tested mediation model — every other close candidate is either higher-education, a review, or missing the mediator entirely.
- **Engagement as the central mediator** is exactly Model-Alpha's own core mechanism — this isn't a paper you're citing for background, it's the paper whose actual causal logic you're adapting.
- **2026 publication** — reflects current blended-learning practice, not pre-pandemic assumptions carried over from older instructional-design literature.
- **Independently verified twice** by direct publisher fetch — not resting on a search-engine snippet the way several other matrix entries had to be flagged ("link not verified," "403 on fetch").
- **India-based** — closer geographic/cultural context to Union Bank of India than the alternative candidates, even though the organization itself isn't named.

---

## 4. How Model-Alpha Narrows and Extends the Base Paper

Per department convention (every reference thesis checked states this explicitly, not just "similar topic") — direct comparison:

| Base paper (Saroj, Sahney & Sekar, 2026) | Model-Alpha (this study) | Relationship |
|---|---|---|
| Blended-learning acceptance, Instructor competence, Metacognitive skills → Engagement | Hybrid Learning (5-dimension: flexibility/accessibility/interaction/technology/integration) → Engagement | **Narrowed** — single multi-dimensional IV replaces the base paper's three separate antecedents; Instructor competence and Metacognitive skills specifically dropped from formal testing (see sec 5 below) |
| Engagement → Employee agility (single endpoint) | Engagement → Training Effectiveness → Knowledge Retention → Job Performance (3-step chain) | **Extended** — Model-Alpha goes further downstream than the base paper attempts; agility is a single outcome, Model-Alpha tests a full Kirkpatrick-style progression |
| Supervisor support as moderator | Not tested | **Dropped** — see open decision below |
| n=375, unnamed Indian workplace | Target ~80-130, Union Bank of India specifically (department sample-size norm, [05](05-past-dissertation-summary.md) sec 9.1) | **Narrowed context** — single named organization, smaller but department-typical sample |

**One-paragraph version for Chapter 2:**

> This study adopts Saroj, Sahney and Sekar's (2026) engagement-mediation model as its base paper — the only identified study testing learner engagement as a mediator between blended-learning antecedents and a workplace outcome in a genuine organizational training context. The present study narrows the base paper's three antecedents (blended-learning acceptance, instructor competence, metacognitive skills) to a single multi-dimensional Hybrid Learning construct, and does not test supervisor support as a moderator. It extends the base paper's single outcome (employee agility) into a three-step outcome chain — Training Effectiveness, Knowledge Retention, and Job Performance — providing a more granular, Kirkpatrick-aligned view of downstream impact than the base paper's model reaches. The study is further narrowed in context to a single Indian public-sector bank, Union Bank of India, rather than an unnamed general workplace sample.

---

## 5. The Open Question This Raises Again

The base paper's own tested model includes **Instructor/Trainer Competence** as a direct predictor of engagement — the exact variable [previous discussion] flagged as the strongest case for reconsidering exclusion. Naming Saroj et al. (2026) as your base paper and then not testing trainer competence is a visible gap your guide is likely to ask about directly, precisely because it's sitting inside the paper you just named as your anchor. This doesn't force a decision now — it's the same open item logged in [SEQUENCE.md](../../SEQUENCE.md) blockers — but naming the base paper formally makes this the most likely single question at your defense, so it's worth deciding before submission rather than after a panel raises it.

---

**Cross-references:** [02-guide-suggestion.md](../../chapter-1/version-0/03-guide-suggestion.md) · [01-initial-literature-search.md](01-initial-literature-search.md) · [03-literature-matrix.md](03-literature-matrix.md) · [04-literature-summary.md](04-literature-summary.md) · [05-past-dissertation-summary.md](05-past-dissertation-summary.md) · [07-model-beta-chain-check.md](07-model-beta-chain-check.md) · [01-research-objectives-and-hypotheses.md](../../chapter-3/objectives-and-hypotheses/version-0/01-research-objectives-and-hypotheses.md) · [PLAN.md](../../PLAN.md)
