# Coding and Decoding

> **Difficulty:** Easy to Medium  ·  **Target time:** 45 s

## In simple words

**The idea:** Words are changed by a hidden rule. Find the rule from the example, then apply it to the new word.

**Think of it like:** A secret message where every letter is swapped by the same trick.

**Simple steps:**
1. Write the original and coded letters in two rows with their alphabet numbers.
2. Compare each pair: is it +1, −2, reversed alphabet or a reversed word?
3. Apply the same rule to every letter of the new word.

**Watch out:** After Z, wrap back to A when you shift letters forward.

## Common rules
Alphabet shift, reverse alphabet (A↔Z), rearranged order, number position, and symbol substitutions. Test each character and wrap Z→A for cyclic shifts.

## Recognise and solve
Write input/output letters in two rows. Compare corresponding positions. If simple shifts fail, test reversal or alternating positions.

1. CAT→DBU: each letter +1; DOG→**EPH**.
2. CAT→XZG: reverse alphabet; DOG→**WLT**.
3. If A=1, B=2,... and “BAD” is written 2-1-4, “CAB” is **3-1-2**.

## Tips and traps
One example may permit multiple coding rules; use all provided pairs/options. For “word coded as number,” check whether letters are summed, concatenated, or multiplied rather than assuming.

## Try it
If TEAM→UFBN by +1, CODE→? **Answer:** DPEF.

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: If CAT is coded as DBU, how is DOG coded?

**Solution:** Each letter shifts forward by one: D→E, O→P, G→H. Code=**EPH**. Verify the rule on all letters of CAT.

### Pattern 2: If PAPER is written REPAP, how is TRAIN written?

**Solution:** The coding reverses the whole word, so TRAIN→**NIART**. A single shifted letter would not explain PAPER.

### Pattern 3: In a code, RED=27 using alphabet positions. What is BLUE?

**Solution:** R+E+D=18+5+4=27. B+L+U+E=2+12+21+5=**40**.

## Deeper patterns (medium to hard)

### Extra rules and tricks
- Opposite-letter pairs add up to 27 in position: A↔Z, B↔Y, C↔X, and so on.
- Alternating shifts: +1, −1, +1, −1 across the word. Check each letter separately.
- Sentence codes: find the word common to two sentences and the code common to their codes; that pair matches.
- Number codes: letter positions can be added (CAT = 3+1+20 = 24) or written as separate numbers (3-1-20).
- Always wrap around: after Z comes A, and before A comes Z.

### Medium patterns

**M1. In a code MANGO is NBOHP. How is APPLE coded?**

**Solution:** Each letter moves forward by 1: A→B, P→Q, P→Q, L→M, E→F, so **BQQMF**.

**M2. 'red apple' = pa ka, 'green apple' = pa ta, 'red tomato' = ka ma. Code for 'tomato'?**

**Solution:** 'apple' is common to sentences 1 and 2, so apple = pa. 'red' is common to 1 and 3, so red = ka. That leaves tomato = **ma**.

### Hard patterns

**H1. In a code LOVE is MNWD. How is HATE coded?**

**Solution:** Shifts alternate +1, −1, +1, −1: L→M, O→N, V→W, E→D. For HATE: H→I, A→Z (wrapping), T→U, E→D, so **IZUD**.

**H2. If CLOUD is written XOLFW, how is HAND written?**

**Solution:** It is the reverse alphabet (positions add to 27). H→S, A→Z, N→M, D→W, so **SZMW**.

### Practice (answers hidden)
1. If DOG is FQI, how is CAT coded?
2. If BAD is written 2-1-4, how is BED written?
3. Using the reverse alphabet, code ABC.

<details><summary>Answers</summary>

1. Each letter moves forward 2: C→E, A→C, T→V, so **ECV**.
2. Using alphabet positions: B=2, E=5, D=4, so **2-5-4**.
3. A→Z, B→Y, C→X, so **ZYX**.

</details>
