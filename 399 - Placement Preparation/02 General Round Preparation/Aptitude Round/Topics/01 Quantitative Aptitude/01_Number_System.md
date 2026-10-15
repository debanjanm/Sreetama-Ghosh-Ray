# Number System

> **Difficulty:** Easy to Medium  ·  **Target time:** 45 s

## Rules and formulas
- For two positive integers, HCF × LCM = product. For three or more, do not multiply HCF and LCM this way.
- Divisibility: 3 or 9 → digit sum; 4 → last two digits; 8 → last three; 11 → alternating digit sums differ by a multiple of 11.
- If a number leaves the same remainder r on division by a and b, write n = LCM(a,b)k + r, provided 0 ≤ r < both divisors.

## Recognise the pattern
“Smallest multiple/common interval” → LCM. “Largest equal group/tile size” → HCF. “Remainder” → write n = divisor × quotient + remainder before using shortcuts.

## Solve
1. Factor numbers into primes. 36=2²×3² and 48=2⁴×3.
2. HCF uses minimum powers: 2²×3=**12**. LCM uses maximum powers: 2⁴×3²=**144**. Check 12×144=36×48.
3. A number leaves remainder 1 when divided by 4 and also by 6. Numbers are 12k+1. The smallest positive is **1**; if the question says “greater than 6”, it is **13**.

## Tips and traps
Use modular arithmetic to check options instead of calculating a huge number. Do not assume LCM+r is the smallest positive answer unless a lower bound is given. Zero is a multiple of every positive integer, so “smallest” needs careful reading.

## Try it
Find HCF and LCM of 18 and 30. **Answer:** 6 and 90 (18=2×3², 30=2×3×5).

---

Use these as general placement examples. Check the employer's actual test instructions and marking rules.

## More worked patterns

### Pattern 1: Find the remainder when 7^103 is divided by 10.

**Solution:** Units digits cycle 7, 9, 3, 1 every four powers. 103 leaves remainder 3 on division by 4, so the third digit is **3**.

### Pattern 2: Find the smallest number divisible by 12, 18 and 20.

**Solution:** Prime powers: 12=2²×3, 18=2×3², 20=2²×5. The LCM is 2²×3²×5=**180**; using the largest power of each prime avoids overcounting.

### Pattern 3: How many factors does 360 have?

**Solution:** 360=2³×3²×5¹. Choose exponent 0–3, 0–2 and 0–1 independently: 4×3×2=**24** positive factors.

## Deeper patterns (medium to hard)

### Extra formulas and shortcuts
- Trailing zeros in n! = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + …
- If N = pᵃqᵇrᶜ, number of factors = (a+1)(b+1)(c+1); sum of factors = (pᵃ⁺¹−1)/(p−1) × (qᵇ⁺¹−1)/(q−1) × …
- Remainder rule: remainder of a×b (or a+b, aⁿ) on division by m equals the same operation applied to the remainders, then reduced mod m.
- Unit-digit cycles: 2, 3, 7, 8 repeat every 4 powers; 4 and 9 every 2; 0, 1, 5, 6 never change.
- Sums: first n naturals n(n+1)/2; first n odds n²; first n evens n(n+1); first n squares n(n+1)(2n+1)/6.
- Prime test: divide only by primes up to √n.

### Medium patterns

**M1. Trailing zeros in 100!?**

**Solution:** ⌊100/5⌋+⌊100/25⌋ = 20+4 = **24**.

**M2. Remainder when 2⁵⁰ is divided by 7?**

**Solution:** 2³=8≡1 (mod 7). 50=3×16+2, so 2⁵⁰≡2²=**4**.

### Hard patterns

**H1. Sum of all factors of 72?**

**Solution:** 72=2³×3². (1+2+4+8)(1+3+9)=15×13=**195**.

**H2. Four bells ring every 6, 8, 12 and 15 s and ring together at 9:00:00. When next together, and how many times together in the next hour including the start?**

**Solution:** LCM(6,8,12,15)=2³×3×5=120 s, so next at **9:02:00**. In 3600 s there are 3600/120=30 intervals, so **31** times including the start.

### Practice (answers hidden)
1. Unit digit of 3⁴⁵?
2. Largest 4-digit number divisible by 15?
3. Smallest number leaving remainder 3 when divided by 5, 6 and 8?

<details><summary>Answers</summary>

1. 45 mod 4 = 1, so unit digit **3**.
2. 9999/15 = 666 remainder 9, so 666×15 = **9990**.
3. LCM=120, so **123**.

</details>
