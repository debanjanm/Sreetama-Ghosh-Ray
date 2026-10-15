# Coded Inequalities

> **Difficulty:** Medium  ·  **Target time:** 60 s

## In simple words

**The idea:** The question hides greater-than and less-than signs behind symbols. Decode the symbols, link the statements into a chain, then see what the chain proves.

**Think of it like:** Comparing salaries: if A earns more than B and B earns more than C, then A earns more than C.

**Simple steps:**
1. Replace each symbol with its real sign using the legend.
2. Join the statements into one chain (A > B ≥ C).
3. Compare the two ends of the chain for each conclusion.
4. A conclusion is true only if the chain forces it.

**Watch out:** A chain that goes up and then down (A > B < C) says nothing about A and C.

## Rules and formulas
- Same direction chains combine: A > B > C gives A > C; A ≥ B > C gives A > C; A ≥ B ≥ C gives only A ≥ C.
- A strict sign anywhere in a same-direction chain makes the ends strict.
- Opposite directions (A > B < C) give no relation between A and C.
- Complementary pair: if neither "A ≥ C" nor "A < C" is certain alone, "either A ≥ C or A < C" is always true. The same holds for "A > C" and "A ≤ C".
- Equal sign: A = B ≥ C gives A ≥ C.

## Recognise the pattern
Symbols such as @, #, $, %, © defined in a legend, followed by "Statements" and "Conclusions I and II".

## Solve
1. Statement: A > B, B ≥ C. Conclusion: A > C → **True**, because the chain contains a strict sign.
2. Statement: P ≥ Q, Q ≥ R. Conclusion: P > R → **Not certain**, only P ≥ R is guaranteed.
3. Statement: X > Y < Z. Conclusion: X > Z → **Not certain**, the chain bends.
4. Legend: P # Q means P > Q; P @ Q means P ≥ Q; P $ Q means P < Q. Statement: A # B, B @ C, C $ D. Decode: A > B, B ≥ C, C < D. Conclusion A > C → **True** (A > B ≥ C). Conclusion A > D → **no relation**.

## Tips and traps
Write the decoded statements on one line before concluding. Keep track of strict versus non-strict signs. Check complementary pairs when two conclusions look opposite.

## Try it
1. A ≥ B > C. Is A > C true? **Answer:** Yes.
2. B < A, B ≤ C. Is there a relation between A and C? **Answer:** No (the chain bends at B).
3. A = B ≥ C. Which is certain, A > C or A ≥ C? **Answer:** A ≥ C.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.
