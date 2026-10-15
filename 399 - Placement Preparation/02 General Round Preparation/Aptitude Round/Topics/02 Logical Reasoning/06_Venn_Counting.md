# Venn Diagrams and Counting

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
