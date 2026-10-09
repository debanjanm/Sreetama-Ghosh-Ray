# Logical Reasoning — Patterns, Methods, and Worked Questions

**Goal:** Convert words into a small diagram, table, or rule. A conclusion must follow from the given premises, even when real-world knowledge suggests otherwise.

## Recognition map

| Clue in question | Representation | First check |
|---|---|---|
| Sequence of numbers/letters | Differences, ratios, alternating positions | Are there two interleaved series? |
| “All”, “some”, “none” | Set diagram / counterexample | Does conclusion hold in every allowed model? |
| “Left/right of”, “between” | Numbered seats | Whose left: your view or their facing direction? |
| People × days/roles | Grid with ✓/✗ | Place fixed clues first |
| “Is the information sufficient?” | Test statements separately | Can two valid answers still occur? |
| Family links | Family tree | Mark gender only if stated |
| Turns and walks | Coordinates | Track final displacement, not distance walked |

## 1. Number and letter series

**Pattern A — differences:** 4, 9, 16, 25, __. Differences 5,7,9; next 11, so **36**. Also squares 2²,3²,4²,5²,6².

**Pattern B — multiplication:** 2, 6, 18, 54, __. Multiply 3 → **162**.

**Pattern C — alternating:** 2, 10, 4, 20, 6, 30, __. Odd positions 2,4,6,**8**; even 10,20,30.

**Pattern D — letters:** B, D, G, K, __. Positions 2,4,7,11; jumps +2,+3,+4,+5 → 16 = **P**.

**Check:** A short series may allow multiple rules. Prefer the simplest consistent rule and use answer options if given.

## 2. Coding and decoding

**Shift:** If CAT→DBU, each letter advances one. DOG→**EPH**. Check wraparound: Z→A.

**Reverse alphabet:** A↔Z, B↔Y, C↔X; CAT→XZG, so DOG→**WLT** (D→W, O→L, G→T).

**Method:** Compare each original-coded letter; test the same rule at every position before applying it.

## 3. Syllogisms and set logic

**Premises:** All analysts are employees. No employee is a contractor.  
**Conclusion:** No analyst is a contractor. **Follows**, because analysts are a subset of employees.

**Premises:** All interns are students. Some students are researchers.  
**Conclusion:** Some interns are researchers. **Does not necessarily follow**; the researcher students may be different from the interns.

**Premises:** Some trainers are managers. All managers are employees.  
**Conclusion:** Some trainers are employees. **Follows**: the trainer-managers exist.

**Counterexample test:** If you can draw one arrangement satisfying all premises but making the conclusion false, mark “does not follow.” Do not infer existence merely from “all A are B” unless the question's convention explicitly treats A as existing.

## 4. Venn counting

**Pattern:** Of 50 students, 30 study Excel, 25 study SPSS, and 10 study both.  
Only Excel = 30−10=**20**; only SPSS = 25−10=**15**; at least one = 30+25−10=**45**; neither = 50−45=**5**.

**Three groups:** Fill the all-three intersection first; subtract it from each pairwise overlap before filling “exactly two.” Pairwise totals often include the triple intersection unless specified otherwise.

## 5. Direction sense

**Pattern:** Walk 4 km north, 3 km east, then 4 km south. Coordinates (0,0)→(0,4)→(3,4)→(3,0). Final location is **3 km east** of start; distance walked is **11 km**.

**Turns:** Starting north, right→east; right again→south. Draw N/E/S/W if facing directions change.

## 6. Blood relations

**Pattern:** Asha is the mother of Bina; Bina is the sister of Charu. What is Asha to Charu? **Mother**, if the statement means Bina and Charu share that mother in the usual family-relation convention. In more formal logic, ask whether full or half siblings are specified; placement problems normally assume the ordinary family tree.

**Ambiguous pattern:** “Rohan's father's only daughter” is Rohan's sister **if Rohan is male**, but could be Rohan herself if Rohan is female. Do not infer gender from a name when the question asks for strict logical necessity.

**Method:** Draw generations as rows; label only explicitly stated gender and relationships.

## 7. Linear seating

**Pattern:** Four people A, B, C, D face north. A sits immediately left of B. C sits at the right end. D is not next to C.  
**Solve:** C is seat 4. D cannot be seat 3, so D is seat 1 or 2. The adjacent A-B pair cannot be 3-4 (C occupies 4), so it is 2-3 or 1-2. If 2-3, D=1 → **D A B C**. If 1-2, D=3, which is next to C and invalid. Unique order **D A B C**.

**Method:** Number seats 1–4; place end constraints; turn “immediately left” into adjacent ordered slots; test remaining cases.

## 8. Grid puzzle

**Pattern:** A, B, C work in HR, Finance, and Sales, one each. A is not in HR. B is in Finance. C is not in Sales.  
**Solve:** B=Finance. Remaining HR/Sales for A/C; C cannot be Sales → C=HR, A=Sales.

| Person | HR | Finance | Sales |
|---|---|---|---|
| A | ✗ | ✗ | ✓ |
| B | ✗ | ✓ | ✗ |
| C | ✓ | ✗ | ✗ |

**Method:** Mark known positives and eliminate that row and column immediately.

## 9. Data sufficiency

**Question:** What is x? (1) x²=16. (2) x>0.  
Statement 1 alone allows +4 or −4; statement 2 alone allows many positives; together x=**4**. **Both statements together, neither alone**.

**Question:** Is n even? (1) n is divisible by 4. (2) n is divisible by 2. Either statement alone is sufficient.  
**Method:** Decide sufficiency without calculating a value if the question asks only yes/no. One definite “yes” or “no” is sufficient.

## 10. Statement, assumption, and conclusion

**Statement:** “The company should send a reminder because some registered students forget deadlines.”  
**Assumption:** A reminder can reach students before the deadline and may help them act. If reminders cannot reach them, the proposal loses its rationale.

**Unsupported conclusion:** “All students will submit after a reminder.” *Some forget* does not guarantee everyone submits.

**Method:** Identify the proposed action or claim, then ask what must be true for the stated reason to support it. Test an assumption by negating it.

## 11. Clocks and calendars

**Clock:** At 3:20, minute hand is 20×6=120° from 12; hour hand is 3×30+20×0.5=100°. Smaller angle = **20°**. If the raw difference exceeds 180°, subtract it from 360°.

**Calendar:** For “day after N days,” calculate N mod 7. If today is Tuesday, 10 days later is 3 days later = **Friday**. For date questions, count leap years and check whether the starting day is included.

## Five-question self-check

1. 5, 11, 23, 47, __ → **95** (double and add 1).
2. All A are B; some B are C. Must some A be C? **No** (possible disjoint overlap).
3. Travel 6 km west then 8 km north. Shortest distance from start? **10 km**.
4. Six people each shake hands once with every other. Total? **15** (6×5/2).
5. Is y positive? (1) y²=9; (2) y>2. Which alone suffices? **Statement 2**; statement 1 permits ±3.

**Practice:** Explain each solution aloud in 30 seconds. If you cannot explain why the wrong options fail, revisit the diagram.
