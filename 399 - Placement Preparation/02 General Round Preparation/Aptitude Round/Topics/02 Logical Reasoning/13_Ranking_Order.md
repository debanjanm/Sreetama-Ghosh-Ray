# Ranking and Order

> **Difficulty:** Easy  ·  **Target time:** 40 s

## In simple words

**The idea:** Ranking questions place people in a line (by marks, height or position) and ask for a position or a count.

**Think of it like:** A queue at a bank counter: your place from the front and from the back always add up to one more than the queue length.

**Simple steps:**
1. Draw a line of boxes and mark the known positions.
2. Use the formulas below to move between positions.
3. For comparisons (taller, older), write them as a chain: A > B > C.
4. Read the chain to find first, last and in-between.

**Watch out:** Count carefully when asked "between". People between positions 6 and 14 are 7, not 8.

## Rules and formulas
- Total people = (position from top) + (position from bottom) − 1.
- Position from the other end = total − position + 1.
- People between two positions p and q = |p − q| − 1.
- If two people swap places, the gap between their old and new positions gives the total or the number of people between them.
- Comparison chains are transitive: A > B and B > C give A > C.

## Recognise the pattern
"Rank from top/bottom/left/right," "taller/older/richer than," "how many between," "after swapping."

## Solve
1. A student is 7th from the top in a class of 30. From the bottom: 30 − 7 + 1 = **24th**.
2. Sita is 12th from the top and 20th from the bottom. Total = 12 + 20 − 1 = **31**.
3. A > B, B > C, D > A, C > E. Chain: D > A > B > C > E. **D is first and E is last.**
4. In a row, one person is 6th from the left and another 14th from the left. People between them: 14 − 6 − 1 = **7**.

## Tips and traps
Draw the line and number the boxes, especially for swap questions. Check whether positions are counted from the same end. 'Taller than' only gives order, never exact numbers.

## Try it
1. In a class of 25, Ravi is 10th from the top. His position from the bottom? **Answer:** 25 − 10 + 1 = 16th.
2. A row of 40 people; Anu is 15th from the left. Position from the right? **Answer:** 40 − 15 + 1 = 26th.
3. P > Q, Q > R, S > P. Who is tallest and who is shortest? **Answer:** S tallest, R shortest.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.
