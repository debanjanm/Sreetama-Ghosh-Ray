# Probability

> **Difficulty:** Hard  ·  **Target time:** 90 s

## In simple words

**The idea:** Probability is the number of ways to win divided by the total number of equally likely ways.

**Think of it like:** Picking one resume at random from a pile and asking how likely it is to be a fresher's.

**Simple steps:**
1. Count all possible outcomes.
2. Count the outcomes you want.
3. Divide: wanted ÷ total.
4. 'At least one' is 1 − P(none). 'And' multiplies. 'Or' adds, then subtract the overlap.

**Watch out:** Without replacement, the second draw has fewer items, so change both the top and the bottom numbers.

## Rules and formulas
- Equally likely outcomes: P(A)=favourable/total.
- P(not A)=1−P(A); P(A or B)=P(A)+P(B)−P(A and B).
- Independent events multiply. Without replacement, the second denominator and counts change.

## Recognise the pattern
“At least one” → complement of none. “Without replacement” → conditional second probability. “Either/or” → account for overlap.

## Solve
1. Two fair coin tosses: P(at least one head)=1−P(TT)=**3/4**.
2. Bag has 3 red and 2 blue. Two blue without replacement: (2/5)(1/4)=**1/10**.
3. Fair die: P(even or >4)=P({2,4,6}∪{5,6})=4/6=**2/3**; 6 is overlap counted once.

## Tips and traps
Check whether outcomes are equally likely. “At least one” includes one, two, etc. Conditional probability cannot normally reuse the original denominator after a draw.

## Try it
Two blue with replacement from the same bag? **Answer:** (2/5)²=4/25.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: Two fair dice are thrown. Find the probability of sum 7.

**Solution:** Six ordered outcomes out of 36: (1,6) through (6,1). Probability=**1/6**.

### Pattern 2: A bag has 3 red and 2 blue balls. Draw two without replacement. Probability both red?

**Solution:** (3/5)×(2/4)=**3/10**. The second draw has four balls left.

### Pattern 3: A fair coin is tossed three times. Probability of at least one head?

**Solution:** Use complement: only TTT has no head, probability 1/8. Answer=**7/8**.

## Deeper patterns (medium to hard)

### Extra formulas and shortcuts
- Deck: 52 cards, 4 suits × 13; 12 face cards; 26 red, 26 black; 4 aces.
- Two dice: 36 outcomes; sum 7 is the most likely (6/36); sums 2 and 12 have 1/36 each.
- Mutually exclusive: P(A∩B)=0. Independent: P(A∩B)=P(A)P(B). These are different ideas.
- Conditional probability: P(A|B) = P(A∩B)/P(B).
- Odds in favour a:b means P = a/(a+b).
- Drawing r items together: use nCr counts for favourable ÷ total.

### Medium patterns

**M1. A card is drawn from 52. P(king or heart)?**

**Solution:** 4+13−1 = 16, so 16/52 = **4/13**.

**M2. Two cards drawn without replacement. P(both aces)?**

**Solution:** (4/52)(3/51) = **1/221**.

### Hard patterns

**H1. A bag has 4 red, 3 blue and 2 green balls. Three drawn together. P(exactly 2 red)?**

**Solution:** 4C2×5C1/9C3 = 6×5/84 = **5/14**.

**H2. P(A)=0.5, P(B)=0.4, P(A∩B)=0.2. Find P(A|B) and check independence.**

**Solution:** P(A|B) = 0.2/0.4 = **0.5**. Since P(A)P(B) = 0.2 = P(A∩B), the events are **independent**.

### Practice (answers hidden)
1. P(sum of two dice = 10)?
2. P(a card is a red face card)?
3. P(exactly 2 heads in 3 tosses)?

<details><summary>Answers</summary>

1. (4,6),(5,5),(6,4) → 3/36 = **1/12**.
2. 6/52 = **3/26**.
3. 3/8.

</details>
