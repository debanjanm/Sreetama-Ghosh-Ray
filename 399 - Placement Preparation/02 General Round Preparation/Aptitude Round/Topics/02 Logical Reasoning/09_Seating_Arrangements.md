# Seating Arrangements

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
