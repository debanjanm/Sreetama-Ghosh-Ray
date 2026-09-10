# 01 — Model-Alpha v1: Final Instrument, Compressed to 30 Items (v2)

**Why this version exists.** Department norms PDF (`university-files/MSSW - Project Norms and Schedule 2026.pdf`): *"No. of questions in questionnaire should be not more than 30."* v1 ([chapter-3/questionnaire/version-1/01-model-alpha-questionnaire.md](../../version-1/scratchpad/01-model-alpha-questionnaire.md)) had 55 Likert items — a violation that actually predated Model-Alpha entirely (even the original 42-item draft broke the cap). This version compresses to exactly 30, keeping all 6 constructs (no construct dropped — model/hypotheses from [chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md](../../../objectives-and-hypotheses/version-1/scratchpad/01-research-objectives-and-hypotheses.md) are unchanged, still valid at construct level).

**Selection method — not arbitrary cutting.** Every kept item was chosen using the existing decision-basis log ([chapter-2/version-0/04-literature-summary.md](../../../../chapter-2/version-0/scratchpad/04-literature-summary.md)):
1. Items flagged **"re-anchor recommended"** (validated-scale-backed — e.g. HL10-12 → Ye et al. UBL scale; JP1/2/4/9 → Koopmans IWPQ) were prioritized to keep — strongest citation support.
2. Items flagged as **theoretically central** were kept regardless (HL13 — "most theoretically important item," the Garrison & Kanuka integration definition).
3. Within a sub-dimension with 3 near-duplicate researcher-developed items and no re-anchor basis, kept the single cleanest/most direct statement, cut the other two.
4. Engagement (the core mediator) and Job Performance (the final DV) were given slightly more than the bare per-construct average, since they carry the most weight in the hypothesis chain.

**Allocation: 30 items across 6 constructs**

| Construct | v1 items | v2 items | Kept |
|---|---|---|---|
| Hybrid Learning | 15 | **8** | 1 each Flexibility/Accessibility/Interaction + all 3 Technology (validated) + 2 Integration (theoretically central) |
| Trainer Competence | 8 | **3** | 1 per dimension, dropped Process dimension entirely (least-verified section overall, per item-wording caution already flagged) |
| Learner Engagement | 5 | **4** | Dropped 1 (redundant with kept items), balanced 2 dedication / 2 absorption |
| Training Effectiveness | 9 | **5** | 1 Relevance + 2 Learning (Kirkpatrick Level 2 — strongest citation basis in whole TE section) + 2 Application |
| Knowledge Retention | 9 | **5** | Spans all 3 original sub-themes (remembering / understanding-recall / continued retention) |
| Job Performance | 9 | **5** | All 4 re-anchor-recommended items (IWPQ-backed) + 1 application item |
| **Total** | **55** | **30** | |

**A real trade-off this creates — say this explicitly in Chapter 3, don't let it surprise you later:** with most Hybrid Learning sub-dimensions now down to 1 item, the **per-dimension diagnostic scorecard** originally planned (file `chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md` sec 4 — "Flexibility=4.10, Technology=3.20" style breakdown for the HR recommendations chapter) is no longer statistically meaningful for most dimensions — you can't compute a sub-scale reliability or even a stable mean from a single item. Only the **overall construct-level score** (all 8 HL items averaged) stays fully valid. If the dimension-level breakdown matters to your recommendations chapter, that requires more items per dimension — which conflicts directly with the 30-item cap. Pick one: report at construct level only (defensible, matches what the item budget actually supports), or flag in your limitations section that dimension-level granularity was sacrificed for compliance with the department's item-count rule.

---

## Response Scale

1 – Strongly Disagree · 2 – Disagree · 3 – Neither Agree nor Disagree · 4 – Agree · 5 – Strongly Agree

## Section A: Basic Information

Unchanged from [chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md](../../version-0/scratchpad/01-base-questionnaire-and-calculation.md) — age group, years of experience, job level, training frequency in last 12 months, % delivered digitally, % delivered face-to-face. (6 questions, not counted against the 30-item Likert cap — see note below.)

## Section B: Hybrid Learning (8 items)

HL1. I can choose when to go through the online parts of the training. *(Flexibility)*

HL4. I can easily find and access the online training materials. *(Accessibility)*

HL7. I get sufficient opportunities to interact with the trainer and ask questions during the training. *(Interaction)*

HL10. I feel confident that I can make good use of the digital platform used for training. *(Technology — re-anchored to Ye, Kuang & Liu 2022 ICTSE item I2, "I think I can make good use of the online teaching platform," adapted from instructor self-efficacy to trainee self-efficacy framing — see note below)*

HL11. Technical problems do not usually interfere with my learning. *(Technology — researcher-developed. No genuine match exists anywhere in Ye et al.'s 17 published items; an earlier draft incorrectly tagged this "re-anchored" before anyone had actually checked the real item wording — corrected here.)*

HL12. The online content helps me understand the topics covered in the training. *(Technology — researcher-developed, same correction as HL11 — no match in Ye et al.'s published items.)*

**Note on the HL10-12 re-anchoring check (2026-09-11):** Ye, Kuang & Liu's (2022) published instrument (ICTSE, OSBL, ABL, UBL — 17 items, Appendix 1 of the paper) was pulled and checked item-by-item against HL10-12 for the first time here. Every one of Ye et al.'s items is phrased from the *instructor's* perspective ("I think I can use computers well for teaching," "I use online teaching methods to match the learning tasks of offline courses") — not the *trainee's* perspective HL10-12 need (a bank employee rating their own experience of using the training platform). Their UBL scale specifically, which HL10 was previously tagged against, is entirely about teaching behaviour and has no trainee-facing analog at all. Only ICTSE item I2 ("I think I can make good use of the online teaching platform") is close enough in content to genuinely adapt — HL10 above is that adaptation, with the perspective changed from teaching to learning/using. HL11 (technical reliability) and HL12 (content comprehension support) have no equivalent anywhere in Ye et al.'s 17 items and are left as researcher-developed rather than forced into a false match.

HL13. The online and classroom sessions are well connected as part of the same training programme. *(Integration — theoretically central item, Garrison & Kanuka 2004)*

HL14. The classroom sessions build on what I learned during the online sessions. *(Integration)*

## Section C: Trainer Competence (3 items)

TC1. The trainer/facilitator has strong knowledge of the training subject matter. *(Content)*

TC3. The trainer is comfortable using the digital tools and platforms involved in the training. *(Technical)*

TC7. The trainer motivates me to actively participate in the training. *(Motivation)*

## Section D: Learner Engagement (4 items)

EN1. I stay fully engaged and attentive during the training sessions, whether online or in-person. *(Dedication)*

EN2. I feel absorbed in the training activities rather than simply going through the motions. *(Absorption)*

EN3. I actively participate in discussions, exercises, or activities during the training. *(Dedication)*

EN4. I put genuine effort into understanding the training content, not just completing it. *(Absorption)*

## Section E: Training Effectiveness (5 items)

TE1. The content covered in the training is relevant to the work I do. *(Relevance)*

TE4. The training helps me understand the topics covered clearly. *(Learning — Kirkpatrick Level 2)*

TE5. I gain useful knowledge from the training. *(Learning — Kirkpatrick Level 2)*

TE7. The training provides knowledge and skills that I can use in my day-to-day work. *(Application)*

TE8. I am able to apply the skills learned during training to my job. *(Application)*

## Section F: Knowledge Retention (5 items)

KR1. I can still recall the main points covered during the training.

KR2. Even weeks or months later, I can remember the key concepts covered in the training.

KR4. I can explain the main ideas from the training in my own words.

KR7. I retain important knowledge from training for a reasonable period of time.

KR9. Revision or refresher materials help me remember what I learned.

## Section G: Job Performance (5 items)

JP1. The knowledge and skills gained from training help me perform my work more accurately. *(Re-anchored, Koopmans IWPQ)*

JP2. Training has helped improve the overall quality of my work. *(Re-anchored)*

JP4. Training helps me complete my work more efficiently. *(Re-anchored)*

JP7. I regularly apply what I learned during training in my job.

JP9. Overall, the training has improved my job performance. *(Re-anchored — global/summary item)*

## Optional Final Questions

Unchanged from [chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md](../../version-0/scratchpad/01-base-questionnaire-and-calculation.md) — 3 open-ended questions on hybrid training experience. (Not counted against the 30-item Likert cap.)

---

## A note on what "30 questions" covers

The department norm doesn't define whether "30 questions" means Likert items only, or everything including demographics and open-ended questions. Every reference thesis that reported item counts ([chapter-2/version-0/05-past-dissertation-summary.md](../../../../chapter-2/version-0/scratchpad/05-past-dissertation-summary.md)) reported their *substantive Likert item count* (23-28), with demographics reported separately in "Section A" — this instrument follows that same convention: **30 refers to the Likert items (Sections B-G above)**, with 6 demographic questions and 3 open-ended questions kept separate. If your supervisor interprets the cap as covering everything, Section A would need trimming too — confirm this reading with them, same as the page-count/sample-size assumptions already flagged.

---

## Scoring

Same averaging method as [chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md](../../version-0/scratchpad/01-base-questionnaire-and-calculation.md) sec 3, applied to each construct's now-smaller item set:

- **Hybrid Learning score** = average of HL1, HL4, HL7, HL10-14 (8 items)
- **Trainer Competence score** = average of TC1, TC3, TC7 (3 items)
- **Learner Engagement score** = average of EN1-4 (4 items)
- **Training Effectiveness score** = average of TE1, TE4, TE5, TE7, TE8 (5 items)
- **Knowledge Retention score** = average of KR1, KR2, KR4, KR7, KR9 (5 items)
- **Job Performance score** = average of JP1, JP2, JP4, JP7, JP9 (5 items)

**Dimension-level scoring (Flexibility/Accessibility/Technology/etc.) is no longer applicable for most sub-dimensions** — see the trade-off note above. Only Technology (3 items, HL10-12) and Integration (2 items, HL13-14) retain enough items for a meaningful sub-dimension mean; Flexibility, Accessibility, and Interaction are down to single items and should be reported as individual item responses, not averaged sub-scale scores.

## Statistical Analysis

Same pipeline as [chapter-3/questionnaire/version-1/01-model-alpha-questionnaire.md](../../version-1/scratchpad/01-model-alpha-questionnaire.md) — correlation matrix, 4 regression models, serial mediation test (Hayes PROCESS Model 6 or Baron & Kenny fallback) — structure unchanged, only the item counts feeding each construct score are smaller. See that file for the full statistical write-up; not repeated here since nothing about the *analysis plan* changed, only the *instrument*.

**One thing worth flagging for Cronbach's alpha specifically:** Trainer Competence now has only 3 items — alpha is still computable but less stable with so few items. If your pilot test shows TC's alpha below an acceptable threshold, you may need to swap in a different item from the original 8 (see [chapter-3/questionnaire/version-1/01-model-alpha-questionnaire.md](../../version-1/scratchpad/01-model-alpha-questionnaire.md) for the full TC1-8 set) rather than adding items back, since that would break the 30-item cap again.

---

**Cross-references:** [chapter-3/questionnaire/version-1/01-model-alpha-questionnaire.md](../../version-1/scratchpad/01-model-alpha-questionnaire.md) (full 55-item version, source of all wording) · [chapter-3/questionnaire/version-0/01-base-questionnaire-and-calculation.md](../../version-0/scratchpad/01-base-questionnaire-and-calculation.md) · [chapter-2/version-0/04-literature-summary.md](../../../../chapter-2/version-0/scratchpad/04-literature-summary.md) (selection basis) · [chapter-3/objectives-and-hypotheses/version-1/01-research-objectives-and-hypotheses.md](../../../objectives-and-hypotheses/version-1/scratchpad/01-research-objectives-and-hypotheses.md) · [PLAN.md](../../../../PLAN.md) · [SEQUENCE.md](../../../../SEQUENCE.md)
