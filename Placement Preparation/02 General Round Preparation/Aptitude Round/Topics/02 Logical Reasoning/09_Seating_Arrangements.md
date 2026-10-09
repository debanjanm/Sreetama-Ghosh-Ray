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
