# Syllogisms

> **Difficulty:** Medium  ·  **Target time:** 60 s

## In simple words

**The idea:** The statements are about groups of things. Drawing circles shows what must be true.

**Think of it like:** Departments in a company: all HR staff are employees, but not all employees are in HR.

**Simple steps:**
1. Draw one circle for each group in the first statement.
2. Add the next statement to the picture.
3. Try to draw the picture in more than one valid way.
4. A conclusion is correct only if it is true in every valid drawing.

**Watch out:** 'Some A are B' does not mean 'all A are B', and it does not prove 'some A are not B'.

## Rules
“All A are B” means A⊆B; “No A are B” means sets do not overlap; “Some A are B” asserts at least one overlap. A conclusion follows only if true in every permitted arrangement.

## Recognise and solve
1. All analysts are employees. No employee is a contractor. Therefore no analyst is a contractor: **follows**.
2. All interns are students. Some students are researchers. Some interns are researchers: **does not necessarily follow**.
3. Some trainers are managers; all managers are employees. Some trainers are employees: **follows**.

## Tips and traps
Draw a counterexample to disprove a conclusion. “All A are B” alone does not prove A exists under strict formal logic. Some exams use their own “either/or” or existence convention; follow the paper's instructions.

## Try it
No managers are interns; some analysts are managers. Can some analysts be interns? **Answer:** possibly, but it is not guaranteed and cannot be concluded.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: All analysts are employees. Some employees are trainers. Does “some analysts are trainers” follow?

**Solution:** **No.** The two employee subsets may be disjoint. Overlap is possible, but not guaranteed.

### Pattern 2: Some managers are mentors. All mentors are employees. Does “some managers are employees” follow?

**Solution:** **Yes.** The managers who are mentors must also be employees; this preserves the “some” witness.

### Pattern 3: No interns are managers. All trainees are interns. Can any trainee be a manager?

**Solution:** **No.** Trainees are a subset of interns, which excludes managers.

## Deeper patterns (medium to hard)

### Extra rules and tricks
- Conversions: 'No A is B' converts to 'No B is A'. 'Some A are B' converts to 'Some B are A'. 'All A are B' converts to 'Some B are A'. 'Some A are not B' does not convert.
- Standard results: All + All gives All; All + No gives No; Some + All gives Some; No + All (second group inside the first) gives No for the new group.
- Test a conclusion by trying to draw the circles in a way that breaks it. If you can, the conclusion does not follow.
- Either-or: if two conclusions are complementary (for example 'Some A are B' and 'No A is B') and neither is certain on its own, the pair 'either I or II' can follow.

### Medium patterns

**M1. All cats are animals. All animals are living. Does 'All cats are living' follow?**

**Solution:** **Yes.** All + All gives All.

**M2. No pen is a pencil. Some pencils are erasers. Does 'Some erasers are not pens' follow?**

**Solution:** **Yes.** The erasers that are pencils cannot be pens.

### Hard patterns

**H1. Some doctors are teachers. All teachers are writers. (I) Some doctors are writers. (II) All doctors are writers.**

**Solution:** Only **I follows**. The doctors who are teachers are writers; others are unknown.

**H2. All HR staff are managers. Some managers are leaders. (I) Some HR staff are leaders. (II) Some leaders are managers.**

**Solution:** Only **II follows**. The leaders who are managers may or may not include HR staff.

### Practice (answers hidden)
1. All pens are tools. Some tools are red. Do some pens have to be red?
2. No manager is a clerk. All clerks are staff. Does 'Some staff are not managers' follow?
3. Some A are B. No B is C. Does 'Some A are not C' follow?

<details><summary>Answers</summary>

1. **No.** The red tools may not include any pens.
2. **Yes.** Clerks are staff and are not managers.
3. **Yes.** The A that are B cannot be C.

</details>
