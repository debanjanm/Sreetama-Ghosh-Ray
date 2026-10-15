# Seating Arrangements

> **Difficulty:** Hard  ·  **Target time:** 120 s

## In simple words

**The idea:** Place the sure things first, join people who must sit together into a block, then eliminate what is impossible.

**Think of it like:** Placing guests at a dinner table using the seating rules.

**Simple steps:**
1. Number the seats and note which way everyone faces.
2. Place anyone whose seat is fixed.
3. Build blocks like 'A is next to B'.
4. Test each possibility and cross out those that break a rule.

**Watch out:** Left and right depend on which way the person faces. Check this carefully.

## Method
Number seats, mark facing direction, place fixed positions, then adjacency blocks and negative constraints. Test every remaining arrangement.

## Recognise and solve
Four people A,B,C,D face north. A immediately left of B; C at right end; D not next to C. C=seat 4. The A-B block cannot be 3-4. Try 2-3 → D=1, yielding **D A B C**. Try 1-2 → D=3 next to C, invalid.

## Tips and traps
For people facing south, their left is page-right. In a circle, fix one person to remove rotational duplicates; facing inward versus outward reverses left/right. “Between” need not mean immediately between unless specified.

## Try it
Three people A,B,C face north. B is immediately right of A; C at left end. Order? **Answer:** C A B.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: A, B, C and D sit in a row facing north. B is immediately right of A; C is immediately left of A; D is at the right end. Find the order.

**Solution:** The block C-A-B must be consecutive. With D at the right end, the order is **C, A, B, D**.

### Pattern 2: Five people sit in a row. P is third from the left and Q is immediately right of P. What is Q’s position from the right?

**Solution:** Q is fourth from the left in a row of five, hence **second from the right**.

### Pattern 3: Four people face the centre in a circle. A is opposite C; B is clockwise next to A. Who is opposite B?

**Solution:** Place A at top, then B clockwise, C opposite A, leaving **D opposite B**. In centre-facing problems, draw the circle first.

## Deeper patterns (medium to hard)

### Extra rules and tricks
- In a row facing north, left is west. Number positions from the left and keep the same numbering throughout.
- Position from left + position from right = total people + 1.
- Circle facing the centre: a person's left is clockwise and right is anticlockwise. If people face outwards, swap them.
- In a circle of n people, the opposite of position p is p + n/2.
- 'Immediate' means adjacent. 'Second to the left' means two seats away.

### Medium patterns

**M1. Five people in a row face north. R is at the extreme left, P is third from the left, Q is immediately right of P, S is immediately left of P. Find the order.**

**Solution:** R sits at 1, P at 3, S at 2, Q at 4, so T takes 5: **R, S, P, Q, T**. P sits in the middle.

**M2. Six people A–F sit in a circle facing the centre. A is opposite D. B is immediately right of A. C is opposite B. F is not adjacent to D. Who is immediately left of A?**

**Solution:** Number seats clockwise: A=1, D=4. Right of A is anticlockwise, so B=6; C opposite B is 3. E and F take 2 and 5; F is not next to D, so F=2 and E=5. Left of A is clockwise, seat 2: **F**.

### Hard patterns

**H1. Seven people face north. A is at the extreme right; B is third to the left of A; C is immediately left of B; D is immediately right of B; E is between D and A; G is at the extreme left. Find the order.**

**Solution:** A=7, B=4, C=3, D=5, E=6, G=1, so F=2: **G, F, C, B, D, E, A**.

**H2. Four friends face the centre. A is between B and C. D is opposite A. Who is opposite B?**

**Solution:** A's neighbours B and C sit opposite each other, and D sits opposite A. Opposite B is **C**.

### Practice (answers hidden)
1. In a row of 7, A is 3rd from the left and B is 4th from the right. How many people sit between them?
2. In a row of 9, a person is 4th from the left. Position from the right?
3. In a circle of 8, who is opposite the person at seat 3?

<details><summary>Answers</summary>

1. B is 4th from the right = 4th from the left, adjacent to A. **0**.
2. 9 − 4 + 1 = **6th**.
3. 3 + 4 = **seat 7**.

</details>
