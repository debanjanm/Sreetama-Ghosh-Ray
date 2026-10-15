# Number and Letter Series

> **Difficulty:** Easy to Medium  ·  **Target time:** 40 s

## In simple words

**The idea:** A series follows a hidden rule that turns each term into the next. Your job is to find the rule.

**Think of it like:** Spotting the pattern in a yearly increment schedule.

**Simple steps:**
1. Write the differences between neighbouring terms.
2. If they are not constant, check the differences of the differences, or the ratios.
3. If it still fails, split the odd and even positions into two separate series.
4. Test your rule on every step before answering.

**Watch out:** A rule that fits only the first two steps is probably wrong. Check all of them.

## Rule families
Constant differences, second differences, constant ratios, squares/cubes, alternating positions, and a repeated multiply-then-add rule. Letter positions A=1 through Z=26.

## Recognise and solve
Check first differences; then second differences or ratios. Split odd and even positions if one rule fails. Use the same rule on **every** step.

1. 3,7,15,31,? → each doubles and adds 1 → **63**.
2. 2,5,10,17,? → differences 3,5,7, then 9 → **26**.
3. 2,10,4,20,6,30,? → odd-position sequence 2,4,6,**8**.
4. B,D,G,K,? → positions 2,4,7,11 (+2,+3,+4), next 16 → **P**.

## Tips and traps
Several rules can fit four terms; prefer the simplest rule consistent with options. Do not assume a geometric pattern before checking differences.

## Try it
4,9,16,25,? **Answer:** 36 (squares 2² through 6²).

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: Find the next term: 3, 7, 15, 31, ?

**Solution:** Each term is double the previous plus 1: 3→7→15→31→**63**. Check the rule across every gap.

### Pattern 2: Find the next term: 2, 6, 12, 20, 30, ?

**Solution:** Differences are 4, 6, 8, 10; next difference 12. Answer=**42**. Equivalently n(n+1).

### Pattern 3: Find the next letter: A, C, F, J, O, ?

**Solution:** Alphabet positions 1,3,6,10,15 have gaps 2,3,4,5; next position 21 is **U**.

## Deeper patterns (medium to hard)

### Extra rules and tricks
- Famous series: squares (1, 4, 9, 16), cubes (1, 8, 27, 64), primes (2, 3, 5, 7, 11, 13), triangular numbers (1, 3, 6, 10, 15), Fibonacci (each term is the sum of the previous two).
- Combined rules: ×a + b (for example ×2 + 1), ×1, ×2, ×3, … (factorials), n² ± n, n² ± 1.
- Letter series: convert to positions, find the number rule, convert back. Pairs like AZ, BY, CX move one letter forward and one backward.
- 'Wrong number' questions: find the rule that fits most terms, then spot the term that breaks it.

### Medium patterns

**M1. Next term: 2, 3, 5, 8, 12, ?**

**Solution:** Differences are 1, 2, 3, 4, so the next difference is 5: **17**.

**M2. Next term: 6, 11, 21, 41, ?**

**Solution:** Each term is double the previous minus 1: 6→11→21→41→**81**.

### Hard patterns

**H1. Find the wrong number: 3, 8, 15, 24, 34, 48.**

**Solution:** The rule is n²−1 for n = 2, 3, 4, …: 3, 8, 15, 24, 35, 48. So **34** is wrong; it should be 35.

**H2. Next pair: AZ, BY, CX, DW, ?**

**Solution:** The first letter moves forward and the second moves backward by one each time: **EV**.

**H3. Next term: 1, 2, 6, 24, 120, ?**

**Solution:** Multiply by 1, 2, 3, 4, 5, then 6: 120×6 = **720**.

### Practice (answers hidden)
1. 2, 5, 11, 23, 47, ?
2. 1, 1, 2, 3, 5, 8, ?
3. C, F, I, L, ?

<details><summary>Answers</summary>

1. Each term is double the previous plus 1: 47×2+1 = **95**.
2. Fibonacci: 5+8 = **13**.
3. Each letter moves forward 3: **O**.

</details>
