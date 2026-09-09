# 07 — Model-Beta "Full Chain" Precedent Check

**Purpose.** Targeted follow-up search (not a re-run of the 36-paper matrix in [03-literature-matrix.md](03-literature-matrix.md)) to test one specific question: is there published precedent for the full 7-variable Model-Beta (Hybrid Learning → Trainer Competence + Org/Supervisor Support → Learner Engagement → Training Effectiveness → Knowledge Retention → Job Performance), strong enough to justify moving off the locked Model-Alpha ([01-research-objectives-and-hypotheses.md](../../chapter-3/objectives-and-hypotheses/version-0/01-research-objectives-and-hypotheses.md))? All sources below were live-searched and, where possible, fetched directly this session (method matches [03](03-literature-matrix.md)'s verification standard).

---

## 1. Full 7-variable chain precedent — search result: none found

Searched multiple phrasings combining hybrid/blended learning, engagement, trainer/instructor competence, organizational/supervisor support, and an outcome chain reaching retention or performance (not stopping at effectiveness/satisfaction). No paper — any year, any context — was found testing all of these together in one model.

Closest partial matches, both already distinguishable by what they leave out:

- **Saroj, Sahney & Sekar (2026)** — has instructor competence, learner engagement, and supervisor support, but stops at employee agility (no KR, no JP). Full detail in Section 2.
- **Bangladesh IJAES study** (sciencepubco.com/index.php/IJAES/article/view/37934) — fetched directly. Tests Blended Learning Effectiveness → Soft Skill Development & Knowledge Acquisition → Employee Performance (n=150, Bangladesh, general corporate sample, no named industry). This reaches performance, but has no trainer competence, no organizational/supervisor support, and no learner engagement construct at all — it uses "soft skills/knowledge acquisition" as its mediators instead. Notable side-finding: blended learning had **no significant direct effect** on employee performance — the effect was fully mediated. Not a Model-Beta precedent, but relevant as a caution that direct effects can vanish once mediators are added (see Section 4 implications).
- **IJRISS "Assessing Blended Learning Outcomes" (Zain, 2026)** — fetched via search snippet/publisher listing. Title looked like a strong match to your exact DV chain (row 22 in [03](03-literature-matrix.md), flagged "worth full-text retrieval"). Now checked: it is a **higher-education student sample** (150 students, Universiti Teknologi MARA, Negeri Sembilan, Malaysia), not a workplace/employee sample, and while it mentions "learner engagement" and "institutional support" descriptively as contributing factors, it does not formally test trainer competence or organizational/supervisor support as separate constructs in a mediation/moderation model. Downgrade this row in your matrix from "worth full-text retrieval" to "checked — population and construct mismatch, not usable as Model-Beta precedent."

**Conclusion for Point 1:** no full-chain precedent exists. This is itself the finding, consistent with what [06-gap.md](06-gap.md) sec 1 gap #4 already predicted.

---

## 2. Saroj, Sahney & Sekar — re-checked directly

Fetched the publisher page directly (doi.org/10.1108/VJIKMS-12-2024-0454 → emerald.com/vjikms/article/56/2/452/1301823), confirming and extending the existing matrix row:

- **Confirmed:** model terminates at employee agility. It does **not** measure knowledge retention or job performance in any form.
- **Publication year:** confirmed 2026 in print (VINE Journal of Information and Knowledge Management Systems, Vol 56(2), pp.452–474), published online 7 October 2025 — matches your existing citation, no correction needed.
- **Full hypothesis list confirmed:** (1) blended-learning acceptance → engagement, (2) instructor competence → engagement, (3) metacognitive skills → engagement, (4) engagement → employee agility, (5) supervisor support moderates engagement→agility.
- **Related work by the same authors, found but not fully accessible:** a conference paper, Saroj, S. & Sahney, S., "The Role of AI-Driven Tools and Workplace Support in Enhancing Employee Agility: The Mediating Role of Learner Engagement," ICMBAI 2025. Title-level only — full text not indexed/fetchable this session. Important: its own title still ends at **employee agility**, the same endpoint as the 2026 paper, not retention or performance. There is no indication from any accessible source that Saroj/Sahney/Sekar (or this closely related conference paper) have extended their model past agility. **Do not cite this conference paper as reaching KR/JP — verify directly if you want to use it, but the title alone argues against it.**

**Conclusion for Point 2:** re-check confirms the existing matrix note exactly. Saroj et al.'s model, and the closest related work by the same authors, stop at employee agility. Neither is a precedent for Model-Beta's KR/JP tail.

---

## 3. 2024–2026 full 7-variable combination — none found (expected null result)

No workplace blended-learning study in the 2024–2026 window was found testing knowledge retention AND job performance AND trainer competence AND organizational support together in one model. As anticipated in your task framing, this rarity is itself evidence: it means Model-Beta (which would need all 7 constructs, including a chain that reaches through KR and JP) has **less published precedent than Model-Alpha already has**, not more. Model-Alpha's 5-variable chain is already, per [06-gap.md](06-gap.md), the first of its kind in the department and rare in the literature; Model-Beta would be an even further step past any existing tested model — an extension of an extension, with zero papers testing the combination as a whole.

This directly strengthens (not weakens) the "chain-depth gap" originality claim in [06-gap.md](06-gap.md) sec 1 gap #4 — but it strengthens it as a description of a gap nobody has filled, which is different from evidence that filling it at Model-Beta's scale, in one master's thesis, is a wise scope decision. That distinction is the crux of the recommendation below.

---

## 4. Sample-size / model-complexity caution — found, and it matters

No single paper was found that critiques this exact scenario by name, but the general methodology literature and your own department precedent ([05-past-dissertation-summary.md](05-past-dissertation-summary.md)) converge on the same caution:

- **SEM guidance:** commonly cited minimums for covariance-based SEM are ~100–150 as a floor, with rule-of-thumb ratios of 5–10 observations per estimated parameter. A 7-construct model with one mediator, one moderator, and a 4-step outcome tail has considerably more estimated paths/parameters than Model-Alpha's 5-construct single chain — at the low end of your department's realistic sample range (80–130, per [05](05-past-dissertation-summary.md) sec 9.1), a full Model-Beta SEM is pushing well past what a 10-per-parameter rule would comfortably support.
- **PLS-SEM is more forgiving of small samples** (the "10-times rule": 10× the largest number of arrows into any single construct) and is explicitly designed for small-sample, complex-model situations — this is a real mitigating option if Sreetama's guide is open to PLS-SEM (as Saroj et al. 2026 itself used SPSS+AMOS, i.e., covariance-based SEM, not PLS). But even proponents of the 10-times rule note it's been "heavily criticised" as insufficient on its own (Hair et al. 2017; Marcoulides & Chin 2013), especially when effect sizes or item reliability are uncertain — both true for a mostly researcher-developed instrument like this one.
- **Regression guidance (the department's actual practice, not SEM):** none of the 8 past MSSW theses reviewed in [05-past-dissertation-summary.md](05-past-dissertation-summary.md) attempted a formal SEM at all — the most statistically ambitious (Sakthipriya 2025, Ravina 2021) used correlation + separate simple/multiple regressions, not a combined mediator+moderator path model. Ravina (2021) explicitly split a 3-DV problem into **three separate simple regressions** rather than one integrated model, at n=100 — a direct department precedent for keeping single models simple even when the underlying theory has more moving parts. The general "10 cases per predictor" rule for regression would put a 7-variable model with cross-paths at the upper edge or past what n=80–130 supports if run as a single combined model (as opposed to a chain of separate simple-regression steps, which is more forgiving but weaker for testing mediation/moderation together).

**Conclusion for Point 4:** no single named critique paper says "don't do this," but the convergent guidance — general SEM/regression sample-size rules, PLS-SEM's own limitations, and the department's own demonstrated practice of simplifying multi-DV designs into separate models at similar sample sizes — all point the same direction: a single combined 7-construct model with simultaneous mediation (engagement) and moderation (org support) tested at n=80–130 is statistically ambitious to the point of risk, independent of whether the theory supports it.

---

## 5. Recommendation — direct answer

**Stay on Model-Alpha. This search does not change the recommendation — if anything it hardens it.**

Reasoning, mapped to what changed vs. what didn't:

- **What's new:** confirmation that Model-Beta (the full 7-variable version, extended with the KR/JP tail) has **zero published precedent anywhere**, not even a partial one. [03-literature-matrix.md](03-literature-matrix.md) sec 4 recommended Model B *as originally scoped* (stopping at Training Effectiveness) because Saroj et al. (2026) was a directly analogous workplace precedent for that shorter chain. That recommendation does not transfer to the 7-variable Model-Beta under discussion here — no paper, including Saroj et al.'s own closely related follow-up work, tests trainer competence + org support + engagement all the way through to retention and performance. Model-Beta would be **built entirely without a workplace precedent for its most distinctive feature** (the combination of antecedent + moderator + a 4-step outcome tail), which is a materially different — and weaker — position than Model-Alpha is already in.
- **What's unchanged:** the sample-size reality. Model-Alpha's 5-variable single-chain design was already structurally ambitious relative to department precedent (per [06-gap.md](06-gap.md) sec 2 and [05](05-past-dissertation-summary.md) sec 9.2). Model-Beta adds two more constructs, one of which needs to function as a moderator (org support) — a materially harder statistical target than a straight mediation chain — on the same 80-130-respondent sample. Nothing found in this search suggests that's realistic; several things found (SEM sample-size minimums, PLS-SEM's own caveats, department precedent of simplifying rather than combining multi-DV models) argue against it.
- **What this means practically:** Model-Alpha remains the right scope for the thesis itself. If Sreetama or her supervisor still wants the trainer-competence/org-support story told, the honest move — consistent with how [06-gap.md](06-gap.md) sec 3.2 already framed the Model-Alpha decision — is to **name Model-Beta explicitly in Chapter 5/6 as a "future research" extension**, citing exactly this search: the combination is theoretically motivated (each individual link has some support — Saroj et al. for competence/support→engagement; the existing Model-Alpha chain for engagement→...→performance) but has never been tested as one integrated model, and doing so credibly would need a larger sample and likely PLS-SEM rather than a department-typical regression battery. That is a strong, honest, low-risk way to use this file's findings — as a limitations/future-research paragraph, not a scope change.

**Bottom line: no new evidence justifies moving to Model-Beta. The absence of precedent that motivated Model-Alpha's original scoping decision is, if anything, more true of the full Model-Beta than it was understood to be — recommend keeping Model-Alpha locked and citing this file when writing the future-research section.**

---

**Cross-references:** [03-literature-matrix.md](03-literature-matrix.md) sec 4 · [06-gap.md](06-gap.md) sec 1, 3.2 · [05-past-dissertation-summary.md](05-past-dissertation-summary.md) sec 9.1 · [01-research-objectives-and-hypotheses.md](../../chapter-3/objectives-and-hypotheses/version-0/01-research-objectives-and-hypotheses.md) · [03-model-alpha-questionnaire.md](../../chapter-3/questionnaire/version-0/03-model-alpha-questionnaire.md) · [PLAN.md](../../PLAN.md)
