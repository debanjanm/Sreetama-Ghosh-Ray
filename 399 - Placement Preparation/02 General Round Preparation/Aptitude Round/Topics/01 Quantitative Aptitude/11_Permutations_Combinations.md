# Permutations and Combinations

> **Difficulty:** Hard  ·  **Target time:** 90 s

## In simple words

**The idea:** These are counting questions. If order matters, use permutations. If you are just choosing, use combinations.

**Think of it like:** Picking 3 people for a committee (order does not matter) versus giving gold, silver and bronze (order matters).

**Simple steps:**
1. Ask: does order matter?
2. Yes: nPr. No: nCr.
3. For rules like 'A and B together', glue them into one block, count, then multiply by the ways inside the block.
4. For 'at least one', count all ways and subtract the ways with none.

**Watch out:** Repeated letters or identical items reduce the count, so divide by the factorial of each repeat.

## Rules and formulas
- Ordered selection nPr=n!/(n−r)!; unordered selection nCr=n!/[r!(n−r)!].
- Distinct linear arrangements of n items: n!; repeated letters: n! divided by factorial of repeat counts.
- Circular arrangements (rotations equivalent, reflections distinct): (n−1)!.

## Recognise the pattern
“Choose a team” → combinations; “assign different posts/arrange in order” → permutations. “At least one” → often count total minus none.

## Solve
1. Choose 2 from 5: 5C2=5×4/2=**10**.
2. Choose chair and secretary from 5: 5P2=5×4=**20**.
3. Arrange letters in LEVEL: 5!/(2!2!)=**30**.
4. A and B must sit together among 4 distinct people in a line: treat AB as one block → 3!×2!=**12**.

## Tips and traps
Check whether positions are labelled and whether identical objects count as distinct. For a circular table, “clockwise versus anticlockwise identical” changes the count; read the convention.

## Try it
How many ways to select 3 of 6? **Answer:** 6C3=20.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: How many 3-digit numbers can be formed from 1, 2, 3, 4 without repetition?

**Solution:** Choose ordered digits: 4×3×2=**24**. Order matters.

### Pattern 2: Choose a committee of 3 from 7 people. How many committees?

**Solution:** Order does not matter: C(7,3)=7×6×5/(3×2×1)=**35**.

### Pattern 3: Arrange the letters of LEVEL. How many distinct arrangements?

**Solution:** Five letters, with two L and two E: 5!/(2!2!)=**30**.

## Deeper patterns (medium to hard)

### Extra formulas and shortcuts
- nCr = nC(n−r); nCr + nC(r+1) = (n+1)C(r+1).
- Digit formation: choose the first digit first if 0 is not allowed there.
- 'At least' problems: total − none. Handshakes among n people = nC2; diagonals of an n-sided polygon = n(n−3)/2.
- Dividing n distinct items into equal groups of size k: n!/((k!)^g · g!), with g groups.
- Necklace or garland (no reflection difference): (n−1)!/2.

### Medium patterns

**M1. How many 3-digit numbers can be formed from 0,1,2,3,4 without repetition?**

**Solution:** First digit 4 ways (not 0), second 4, third 3: 4×4×3 = **48**.

**M2. A committee of 4 from 5 men and 4 women, with at least 2 women.**

**Solution:** 2W2M: 6×10=60; 3W1M: 4×5=20; 4W: 1. Total **81**.

### Hard patterns

**H1. 8 people sit around a table. Two particular people must not sit together.**

**Solution:** Total 7! = 5,040; together 6!×2 = 1,440; answer **3,600**.

**H2. Distinct arrangements of MISSISSIPPI?**

**Solution:** 11!/(4!·4!·2!) = 39,916,800/1,152 = **34,650**.

### Practice (answers hidden)
1. Handshakes among 10 people?
2. Diagonals of a hexagon?
3. Select 2 men and 2 women from 5 men and 4 women.

<details><summary>Answers</summary>

1. 10C2 = **45**.
2. 6×3/2 = **9**.
3. 10×6 = **60**.

</details>
