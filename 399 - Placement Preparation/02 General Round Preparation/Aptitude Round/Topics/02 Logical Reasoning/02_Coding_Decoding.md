# Coding and Decoding

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
