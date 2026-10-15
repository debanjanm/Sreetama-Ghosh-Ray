# Venn Diagrams and Counting

> **Difficulty:** Medium  ·  **Target time:** 75 s

## In simple words

**The idea:** When two groups overlap, people in the overlap are counted twice, so subtract them once.

**Think of it like:** Employees who know Excel, SPSS, or both.

**Simple steps:**
1. Start with the overlap in the middle.
2. Subtract it from each group to get the 'only' parts.
3. Add all parts for 'at least one'.
4. Total minus 'at least one' gives 'neither'.

**Watch out:** 'Only' and 'at least' mean different regions of the diagram.

## Formulas
|A∪B|=|A|+|B|−|A∩B|. Neither = total−union. For three sets, add singles, subtract pairwise intersections, then add triple intersection.

## Recognise and solve
Of 60 people, 35 know Excel, 30 SPSS, 10 both:
- only Excel=35−10=**25**; only SPSS=30−10=**20**;
- at least one=35+30−10=**55**; neither=60−55=**5**.

For three-set questions, start with the triple intersection, then subtract it from pairwise overlaps to get “exactly two.”

## Tips and traps
“At least two” includes the triple region; “exactly two” excludes it. Ensure no region has a negative count; that signals inconsistent data or interpretation.

## Try it
40 people; 22 A, 18 B, 7 both. Neither? **Answer:** 40−(22+18−7)=7.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: In a class of 60, 35 study English, 28 Hindi, and 10 neither. How many study both?

**Solution:** At least one=60−10=50. Inclusion–exclusion: 35+28−both=50, so **13** study both.

### Pattern 2: Of 100 people, 55 like tea, 50 coffee, and 20 both. How many like neither?

**Solution:** Union=55+50−20=85; neither=100−85=**15**.

### Pattern 3: In a survey, 18 like A only, 12 like B only, and 8 like both. How many like at least one?

**Solution:** Add disjoint regions: 18+12+8=**38**; do not double-count the overlap.

## Deeper patterns (medium to hard)

### Extra rules and tricks
- Three sets: exactly one + exactly two + all three = union.
- Exactly two = (sum of pairwise overlaps) − 3 × (all three).
- Only A = A − (A∩B) − (A∩C) + (A∩B∩C).
- Word-relation diagrams: if every member of one group is in another, draw it inside; if only some overlap, draw overlapping circles; if none, draw separate circles.

### Medium patterns

**M1. In a group of 80, 50 like tea, 40 like coffee and 10 like neither. How many like both?**

**Solution:** Union = 70. 50+40−both = 70 gives **20**.

**M2. |A|=30, |B|=25, |C|=20, |A∩B|=10, |B∩C|=8, |A∩C|=6, all three = 4. Find |A∪B∪C|.**

**Solution:** 30+25+20−10−8−6+4 = **55**.

### Hard patterns

**H1. Using the data above, find how many are in exactly two sets and exactly one set.**

**Solution:** Exactly two = (10−4)+(8−4)+(6−4) = **12**. Only A = 30−(10+6−4) = 18, only B = 25−(10+8−4) = 11, only C = 20−(8+6−4) = 10, so exactly one = **39**. Check: 39+12+4 = 55.

**H2. Which diagram represents Doctors, Women and Humans?**

**Solution:** Doctors and Women overlap partly (some doctors are women), and both circles sit **inside Humans**.

### Practice (answers hidden)
1. Of 100 students, 60 play cricket, 45 play football, 15 play both. How many play neither?
2. Only A = 35, only B = 25, both = 10, neither = 5. Total?
3. n(A)=20, n(B)=30, n(A∪B)=40. Find n(A∩B).

<details><summary>Answers</summary>

1. Union = 90, so **10**.
2. 35+25+10+5 = **75**.
3. 20+30−40 = **10**.

</details>
